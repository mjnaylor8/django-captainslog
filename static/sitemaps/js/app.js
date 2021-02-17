
        var mbat = "{{mapbox_access_token}}"
        mapboxgl.accessToken=mbat;

        var map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/light-v9',
        center: [0, 40],
        zoom: 1
        });

        var geojson_visited = {
        type: 'FeatureCollection',
            features: [
                {% for i in sites_visited %}
                    {
                    type: 'Feature',
                        geometry: {
                            type: 'Point',
                            coordinates: {% tuple_to_array i.location %},
                        },
                        properties: {
                            id : i
                            title: "<div class='place-title'><a href='{{ i.get_absolute_url }}'>{{ i.name }}</div>",
                            description: "<div class='place-star'>{{ i.star_rating }}</a><br/></div>"
                        },
                    },
                    //var lngLatWithTag = {% tuple_to_array i.location %};
                    //var marker = new mapboxgl.Marker() .setLngLat(lngLatWithTag) .addTo(map); 
                {% endfor %}
            ]
        };

            // add markers to map
            geojson_visited.features.forEach(function(marker) {
           
            // create a HTML element for each feature
            var el = document.createElement('div');
            var ei = document.createElement('i');
            ei.classList.add('fas', 'fa-map-marker-alt', 'fa-2x');
            el.appendChild(ei);
            el.className = 'marker-light-red';
            //el.className = 'fas fa-map-marker-alt'
            console.log(marker.geometry.coordinates, marker.properties.title, marker.properties.description, el);
            // visited
            //red = new mapboxgl.Marker(el) .setLngLat(marker.geometry.coordinates) .addTo(map) .setPopup(new mapboxgl.Popup({ offset: 25 }) // add popups
            //.setHTML(marker.properties.title + marker.properties.description))
            new mapboxgl.Marker(el)
            .setLngLat(marker.geometry.coordinates)
            .setPopup(new mapboxgl.Popup({ offset: 25 }) // add popups
            .setHTML(marker.properties.title + marker.properties.description))
            .addTo(map);
            });
            
            map.on('load', function (e) {
                /* Add the data to your map as a layer */
                map.addLayer({
                    "id": "locations",
                    "type": "symbol",
                    /* Add a GeoJSON source containing place coordinates and information. */
                    "source": {
                    "type": "geojson",
                    "data": geojson_visited
                    },
                    "layout": {
                    "icon-image": "circle-11",
                    "icon-allow-overlap": true,
                    }
                });
                buildLocationList(geojson_visited);
            });
            geojson_visited.features.forEach(function(geojson_visited, i){
                geojson_visited.properties.id = i;
                console.log(geojson_visited.properties.id)
            });
            function buildLocationList(data) {
                data.features.forEach(function(geojson_visited, i){
                    /**
                     * Create a shortcut for `store.properties`,
                     * which will be used several times below.
                    **/
                    var prop = geojson_visited.properties;
                    /* Add a new listing section to the sidebar. */
                    var listings = document.getElementById('listings');
                    var listing = listings.appendChild(document.createElement('div'));
                    /* Assign a unique `id` to the listing. */
                    listing.id = "listing-" + prop.id;
                    /* Assign the `item` class to each listing for styling. */
                    listing.className = 'item';

                    /* Add the link to the individual listing created above. */
                    var link = listing.appendChild(document.createElement('a'));
                    console.log(prop.id, prop.title)
                    link.href = '#';
                    link.className = 'title';
                    link.id = "link-" + prop.id;
                    link.innerHTML = prop.title;

                    /* Add details to the individual listing. */
                    var details = listing.appendChild(document.createElement('div'));
                    details.innerHTML = prop.description;
                    //if (prop.phone) {
                    //details.innerHTML += ' · ' + prop.phoneFormatted;
                    //}
                });
                }
