if (!mapboxgl.supported()) {
    alert('Your browser does not support Mapbox GL helolo');
} else {
    $(document).ready(function () {
        var coordinatesGeocoder = function (query) {
// match anything which looks like a decimal degrees coordinate pair
            var matches = query.match(/^[ ]*(?:Lat: )?(-?\d+\.?\d*)[, ]+(?:Lng: )?(-?\d+\.?\d*)[ ]*$/i);
            if (!matches) {
                return null;
            }

            function coordinateFeature(lng, lat) {
                return {
                    center: [lng, lat],
                    geometry: {
                        type: "Point",
                        coordinates: [lng, lat]
                    },
                    place_name: 'Lat: ' + lat + ' Lng: ' + lng, // eslint-disable-line camelcase
                    place_type: ['coordinate'], // eslint-disable-line camelcase
                    properties: {},
                    type: 'Feature'
                };
            }

            var coord1 = Number(matches[1]);
            var coord2 = Number(matches[2]);
            var geocodes = [];

            if (coord1 < -90 || coord1 > 90) {
// must be lng, lat
                geocodes.push(coordinateFeature(coord1, coord2));
            }

            if (coord2 < -90 || coord2 > 90) {
// must be lat, lng
                geocodes.push(coordinateFeature(coord2, coord1));
            }

            if (geocodes.length === 0) {
// else could be either lng, lat or lat, lng
                geocodes.push(coordinateFeature(coord1, coord2));
                geocodes.push(coordinateFeature(coord2, coord1));
            }

            return geocodes;
        };

        function translate_to_string(obj) {
            var lat = obj.lat;
            var lng = obj.lng;
            return lng + "," + lat
        }

        function translate_to_reversed_string(obj) {
            var lat = obj.lat;
            var lng = obj.lng;
            return lat + "," + lng
        }

        function replace_order(array) {
            return [array[1], array[0]]
        }

        var geocoders = {};
        $(".js-mapbox-input-location-field").each(function () {
            var input = $(this);
            var id = input.attr("id");
            var map = new mapboxgl.Map({
                container: id + '-map-mapbox-location-field',
                style: map_attrs[id].style,
                center: map_attrs[id].center,
                zoom: map_attrs[id].zoom,
            });
            //start of added for maptype selection
            var layerList = document.getElementById('menu');
            if (layerList !== null) {
            var inputs = layerList.getElementsByTagName('input');
            function switchLayer(layer) {
                var layerId = layer.target.id;
                map.setStyle('mapbox://styles/mapbox/' + layerId);
                }
                
                for (var i = 0; i < inputs.length; i++) {
                inputs[i].onclick = switchLayer;
            }}
            //end of added for maptype selection
            
            //start of added cursor arrow controls
            //pixels the map pans when the up or down arrow is clicked
            var deltaDistance = 100;
            
            //degrees the map rotates when the left or right arrow is clicked
            var deltaDegrees = 25;
            
            function easing(t) {
                return t * (2 - t);
            }
            
            map.on('load', function () {
                map.getCanvas().focus();
            
                map.getCanvas().addEventListener(
                'keydown',
                function (e) {
                    e.preventDefault();
                    if (e.which === 38) {
                        // up
                        map.panBy([0, -deltaDistance], {
                        easing: easing
                        });
                    } else if (e.which === 40) {
                    // down
                    map.panBy([0, deltaDistance], {
                    easing: easing
                    });
                    } else if (e.which === 37) {
                    // left
                    map.easeTo({
                    bearing: map.getBearing() - deltaDegrees,
                    easing: easing
                    });
                    } else if (e.which === 39) {
                    // right
                    map.easeTo({
                    bearing: map.getBearing() + deltaDegrees,
                    easing: easing
                    });
                    }
                },
                true
                );
            });
            //end of added cursor arrow controls
            if (input.val()) {
                var marker = new mapboxgl.Marker({draggable: false, color: map_attrs[id].marker_color,});
                marker.setLngLat(map_attrs[id].center)
                    .addTo(map);
                input.val(replace_order(map_attrs[id].center));

            }

            var geocoder = new MapboxGeocoder({
                accessToken: mapboxgl.accessToken,
                mapboxgl: mapboxgl,
                localGeocoder: coordinatesGeocoder,

            });
            geocoders[id] = geocoder;
            map.getCanvas().style.cursor = map_attrs[id].cursor_style;
            if (!map_attrs[id].rotate) {
                map.dragRotate.disable();
                map.touchZoomRotate.disableRotation();
            }
            if (map_attrs[id].track_location_button) {
                map.addControl(new mapboxgl.GeolocateControl({
                    positionOptions: {
                        enableHighAccuracy: true
                    },
                    trackUserLocation: true,
                }));
            }
            if (map_attrs[id].geocoder) {
                map.addControl(geocoder, "top-left");
            }

            if (map_attrs[id].fullscreen_button) {
                map.addControl(new mapboxgl.FullscreenControl());
            }
            if (map_attrs[id].navigation_buttons) {
                map.addControl(new mapboxgl.NavigationControl());
            }
            geocoder.on("result", function (e) {
                $("div.mapboxgl-marker.mapboxgl-marker-anchor-center").not(".mapboxgl-user-location-dot").remove();

                input.val(replace_order(e.result.geometry.coordinates));
                var marker = new mapboxgl.Marker({draggable: false, color: map_attrs[id].marker_color,});
                marker.setLngLat(e.result.geometry.coordinates)
                    .addTo(map);
                
                $(document).trigger("reverse-geocode", [id, e.result.place_name,])
            });

            map.on("click", function (e) {
                $("#" + id + "-map-mapbox-location-field .mapboxgl-marker.mapboxgl-marker-anchor-center").not(".mapboxgl-user-location-dot").remove();
                input.val(translate_to_reversed_string(e.lngLat));
                var marker = new mapboxgl.Marker({draggable: false, color: map_attrs[id].marker_color,});
                marker.setLngLat(e.lngLat)
                    .addTo(map);

                var url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + translate_to_string(e.lngLat) + ".json?access_token=" + mapboxgl.accessToken;
                $.get(url, function (data) {
                    try {
                        reverse_name = data.features[0].place_name;
                    }
                    catch
                        (e) {
                        reverse_name = "undefined address";
                    }
                        //make sure there is some context to look at
                        if (data.features[0].context){
                            //get 1st address line
                            address_line_all = data.features[0].place_name.split(",");
                            address_line = address_line_all[0]
                            //set up variables for the other bits of address we might get
                            var country;
                            var region;
                            var district;
                            var place;
                            var locality;
                            var postcode;

                            //loop through the context getting bits of address
                            $.each(data.features[0].context, function(i, v){

                                var dotPosition = v.id.indexOf(".");
                                var idtext = v.id.substring(0, dotPosition);

                                switch(idtext) {
                                    case "country":
                                        country = v.text;
                                        break;
                                    case "region":
                                        region = v.text;
                                        break;
                                    case "district":
                                        district = v.text;
                                        break;
                                    case "place":
                                        place = v.text;
                                        break;
                                    case "locality":
                                        locality = v.text;
                                        break;
                                    case "postcode":
                                        postcode = v.text;
                                        break;
                                    default:
                                        
                                }
                            });
                        }
                    // now save all the bits of address we have found
                    if (country !== null){
                        $(document).trigger("reverse-geocode-country", [id, country,])
                    };
                    if (region !== null){
                        $(document).trigger("reverse-geocode-region", [id, region,])
                    };
                    if (district !== null){
                        $(document).trigger("reverse-geocode-district", [id, district,])
                    };
                    if (place !== null){
                        $(document).trigger("reverse-geocode-place", [id, place,])
                    };
                    if (locality !== null){
                        $(document).trigger("reverse-geocode-locality", [id, locality,])
                    };
                    if (postcode !== null){
                        $(document).trigger("reverse-geocode-postcode", [id, postcode,])
                    };
                    if (address_line !== null){
                        $(document).trigger("reverse-geocode-line", [id, address_line,])
                    };
                    //set the geocoder contents to the address found
                    geocoder.setInput(reverse_name);
                    $(document).trigger("reverse-geocode", [id, reverse_name,]);
                });
            });
        });

        $(".js-mapbox-address-input-location-field").each(function () {
            var addressinput = $(this);
            if (addressinput.val()) {
                geocoders[addressinput.attr("id")].setInput(addressinput.val());
            }
        });
        
    });
}