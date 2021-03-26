var LotsOfPointsMode = {};
var pointcount = 0;


// When the mode starts this function will be called.
// The `opts` argument comes from `draw.changeMode('lotsofpoints', {count:7})`.
// The value returned should be an object and will be passed to all other lifecycle functions
LotsOfPointsMode.onSetup = function(opts) {
  var state = {};
  state.count = opts.count || 0;
  return state;
};

LotsOfPointsMode.onTap = function(state, e) {
    // `this.newFeature` takes geojson and makes a DrawFeature
    pointcount = pointcount + 1;
    const coords = [e.lngLat.lng, e.lngLat.lat];
    var point = this.newFeature({
      type: 'Feature',
      id: pointcount,
      properties: {
        count: state.count,
        id: pointcount,
      },
      geometry: {
        type: 'Point',
        coordinates: coords
      }
    });
    this.addFeature(point); // puts the point on the map
    addPoint(e.lngLat.lng, e.lngLat.lat, pointcount)
    state.lastFeature = draw.get(pointcount);
    getPointbyPointMatchings(50, pointcount, e.lngLat.lng, e.lngLat.lat);
    return state;
  };

LotsOfPointsMode.onDrag = function(state, e) {
  //console.log('on drag')
  if (state.selectedFeature) {
    const x = e.lngLat.lng;
    const y = e.lngLat.lat;
    const coords = [e.lngLat.lng, e.lngLat.lat];
    const id = state.selectedFeature.properties.id;
    state.newFeature = JSON.parse(JSON.stringify(state.selectedFeature));
    state.newFeature.geometry.coordinates = coords;
    state.newFeature.id = id;
    draw.delete(id);
    draw.add(state.newFeature);
    
    canvas.style.cursor = 'crosshair';
    return state;
  }
}

LotsOfPointsMode.onMouseUp = function(state, e) {
  //console.log('mouse up')
  if (state.selectedFeature) {
    movePoint(state.newFeature.geometry.coordinates[0], state.newFeature.geometry.coordinates[1], state.newFeature.id);
  }
  map.dragPan.enable();
}

LotsOfPointsMode.onMouseDown = function(state, e) {
  //console.log('mouse down')
  const coords = [e.lngLat.lng, e.lngLat.lat];
  const features = this.map.queryRenderedFeatures(e.point, {
    layers: [
      'gl-draw-point-inactive.hot',
      'gl-draw-point-inactive.cold',
    ]
  });
  if (features.length == 0) {}
  else {
    map.dragPan.disable();
    state.selectedFeatureId = features[0].properties.id;
    state.selectedFeature = features[0];
    canvas.style.cursor = 'move';
  }
}

// Whenever a user clicks on the map, Draw will call `onClick`
LotsOfPointsMode.onClick = function(state, e) {
  // `this.newFeature` takes geojson and makes a DrawFeature
  //console.log('on Click')
  const coords = [e.lngLat.lng, e.lngLat.lat];
  const features = this.map.queryRenderedFeatures(e.point, {
    layers: [
      'gl-draw-point-inactive.hot',
      'gl-draw-point-inactive.cold',
    ]
  });

  if (!features.length) {
    pointcount = pointcount + 1;
    var point = this.newFeature({
      type: 'Feature',
      id: pointcount,
      properties: {
        count: state.count,
        id: pointcount,
        name: "point_" + pointcount,
      },
      geometry: {
        type: 'Point',
        coordinates: coords
      }
    });
    this.addFeature(point); // puts the point on the map
    state.lastFeature = draw.get(pointcount);
    addPoint(e.lngLat.lng, e.lngLat.lat, pointcount)
    getPointbyPointMatchings(50, pointcount, e.lngLat.lng, e.lngLat.lat);
    return state;
  }
  else {
    var currentCircleColor = map.getPaintProperty(
      features[0].layer.id, 
      'circle-color');
    
    if (currentCircleColor == '#3bb2d0' || "['match', ['get', 'id'], features[0].properties.id ,'#ff0000', '#3bb2d0']") {
      map.setPaintProperty 
        (
          features[0].layer.id, 
          'circle-color',
          ['match', ['get', 'id'], features[0].properties.id ,'#ff0000', '#3bb2d0']
        )
    }
    else {
      map.setPaintProperty
        (
          features[0].layer.id, 
          'circle-color',
          '#3bb2d0'
        )
    }
  }
};

// Whenever a user clicks on a key while focused on the map, it will be sent here
LotsOfPointsMode.onKeyUp = function(state, e) {
  if (e.keyCode === 27) {
    canvas.style.cursor = 'grab';
    return this.changeMode('simple_select');
  }
};

// This is the only required function for a mode.
// It decides which features currently in Draw's data store will be rendered on the map.
// All features passed to `display` will be rendered, so you can pass multiple display features per internal feature.
// See `styling-draw` in `API.md` for advice on making display features
LotsOfPointsMode.toDisplayFeatures = function(state, geojson, display) {
  display(geojson);
};
