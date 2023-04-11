var LotsOfPointsMode = {};
var pointcount = 0;
const defaultPointColor = "#3bb2d0";
const defaultPointOutlineColor = "#fff";
const selectedPointColor = "#ff0000";
const selectedPointOutlineColor = "#00ff00";
const defaultPointRadius = 3;
const defaultPointOutlineRadius = 5;
const selectedPointRadius = 5;
const selectedPointOutlineRadius = 7;

const updateSelectedColours = (features, features2, state) => {
	map.setPaintProperty(features[0].layer.id, "circle-color", [
		"match",
		["get", "id"],
		features[0].properties.id,
		selectedPointColor,
		defaultPointColor,
	]);
	map.setPaintProperty(features[0].layer.id, "circle-radius", [
		"match",
		["get", "id"],
		features[0].properties.id,
		selectedPointRadius,
		defaultPointRadius,
	]);
	map.setPaintProperty(features2[0].layer.id, "circle-color", [
		"match",
		["get", "id"],
		features2[0].properties.id,
		selectedPointOutlineColor,
		defaultPointOutlineColor,
	]);
	map.setPaintProperty(features2[0].layer.id, "circle-radius", [
		"match",
		["get", "id"],
		features2[0].properties.id,
		selectedPointOutlineRadius,
		defaultPointOutlineRadius,
	]);

	state.selectedFeatureId = features[0].properties.id;
	state.selectedFeature = features[0];
	state.selectedFeature2Id = features2[0].properties.id;
	state.selectedFeature2 = features2[0];
	selectedPointId = features[0].properties.id;
	selectedPoint = features[0];
	deletept.disabled = selectedPoint ? "" : "disabled";

	return state;
}

const resetSelectedColours = (features, features2, state) => {
	map.setPaintProperty(features[0].layer.id, "circle-color", "#3bb2d0");
	map.setPaintProperty(features[0].layer.id, "circle-radius", 3);
	map.setPaintProperty(features2[0].layer.id, "circle-color", "#fff");
	map.setPaintProperty(features2[0].layer.id, "circle-radius", 5);
	var currentCircleColor = map.getPaintProperty(
		features[0].layer.id,
		"circle-color"
	);
	//console.log('cc', currentCircleColor)
	//console.log(features[0], features2[0])
	state.selectedFeatureId = null;
	state.selectedFeature = null;
	state.selectedFeature2Id = null;
	state.selectedFeature2 = null;
	selectedPointId = null;
	selectedPoint = null;
	deletept.disabled = selectedPoint ? "" : "disabled";

	return state;
}

const addDeletePoint = (state, e) => {
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

		canvas.style.cursor = "crosshair";
		return state;
	}
}

// When the mode starts this function will be called.
// The `opts` argument comes from `draw.changeMode('lotsofpoints', {count:7})`.
// The value returned should be an object and will be passed to all other lifecycle functions
LotsOfPointsMode.onSetup = function (opts) {
	var state = {};
	state.count = opts.count || 0;
	return state;
};

LotsOfPointsMode.onTap = function (state, e) {
	//console.log('on tap')
	const coords = [e.lngLat.lng, e.lngLat.lat];
	var width = 15;
	var height = 15;

	const features = this.map.queryRenderedFeatures([
		[e.point.x - width / 2, e.point.y - height / 2],
		[e.point.x + width / 2, e.point.y + height / 2]
		], {
		layers: ["gl-draw-point-inactive.hot", "gl-draw-point-inactive.cold"],
	});
	const features2 = this.map.queryRenderedFeatures([
		[e.point.x - width / 2, e.point.y - height / 2],
		[e.point.x + width / 2, e.point.y + height / 2]
		], {
		layers: [
			"gl-draw-point-point-stroke-inactive.hot",
			"gl-draw-point-point-stroke-inactive.cold",
		],
	});

	//if there is no feature and nothing selected then add a point
	if (!features.length && !selectedPoint) {
		//('!features.length && !selectedPoint')
		pointcount = pointcount + 1;
		var point = this.newFeature({
			type: "Feature",
			id: pointcount,
			properties: {
				count: state.count,
				id: pointcount,
				name: "point_" + pointcount,
			},
			geometry: {
				type: "Point",
				coordinates: coords,
			},
		});
		this.addFeature(point); // puts the point on the map
		state.lastFeature = draw.get(pointcount);
		addPoint(e.lngLat.lng, e.lngLat.lat, pointcount);
		canvas.style.cursor = "crosshair";
		getPointbyPointMatchings(5, pointcount, e.lngLat.lng, e.lngLat.lat);
		return state;
	}
	//if there is a feature and there is also one which is selected
	if (features.length && selectedPoint) {
		//console.log('features.length && selectedPoint', state.selectedFeatureId, features[0].properties.id)
		//if the feature selected is not the same as the feature clicked
		//then change the selected feature
		if(state.selectedFeatureId != features[0].properties.id) {
			//console.log('state.selectedFeatureId != features[0].properties.id', state.selectedFeatureId != features[0].properties.id)
			updateSelectedColours(features, features2, state);
			map.dragPan.disable();
			state.selectedFeatureId = features[0].properties.id;
			state.selectedFeature = features[0];
			canvas.style.cursor = "move";
		}
		else {
			//reset the point to be not selected
			resetSelectedColours(features, features2, state);
			map.dragPan.enable();
			canvas.style.cursor = "crosshair";
		}
		return state;
	}

	//if there is nothing under the point selected then we want to move the point
	if (!features.length && selectedPoint) {
		//console.log('!features.length && selectedPoint', e.lngLat.lng, e.lngLat.lat, state.selectedFeature.geometry.coordinates, state.selectedFeatureId)
		addDeletePoint(state, e);
		movePoint(
			state.newFeature.geometry.coordinates[0],
			state.newFeature.geometry.coordinates[1],
			state.newFeature.id
		);
		//console.log('moving point')
		map.dragPan.enable();
		canvas.style.cursor = "crosshair";
	}

	//if there is something under the point selected and nothing is selected then select it
	if (features.length && !selectedPoint) {
		//console.log('features.length && !selectedPoint')
		updateSelectedColours(features, features2, state);
	}

};

LotsOfPointsMode.onDrag = function (state, e) {
	//console.log('on drag')
	addDeletePoint(state, e);

};

LotsOfPointsMode.onTouchMove = function (state, e) {
	//console.log('on touch move')
	addDeletePoint(state, e);
};

LotsOfPointsMode.onMouseUp = function (state, e) {
	//console.log('mouse up')
	//if there is a selected feature and a new feature
	//the coords are different from the newFeature
	//created in drag event then update HistoryIndex with new position
	//the drag event has handled the create and delete as point moved in drag
	if (state.selectedFeature &&
		state.newFeature &&
		state.newFeature.geometry.coordinates != state.selectedFeature.geometry.coordinates) {
		movePoint(
			
			state.newFeature.geometry.coordinates[0],
			state.newFeature.geometry.coordinates[1],
			state.newFeature.id
		);
		//console.log('moving point');
	}
	state.newFeature = null;
	map.dragPan.enable();
	canvas.style.cursor = "crosshair";
};

LotsOfPointsMode.onTouchEnd = function (state, e) {
	//console.log('touch end')
	//if there is a selected feature and a new feature
	//the coords are different from the newFeature
	//created in drag event then update HistoryIndex with new position
	//the drag event has handled the create and delete as point moved in drag
	if (state.selectedFeature &&
		state.newFeature &&
		state.newFeature.geometry.coordinates != state.selectedFeature.geometry.coordinates) {
		movePoint(
			
			state.newFeature.geometry.coordinates[0],
			state.newFeature.geometry.coordinates[1],
			state.newFeature.id
		);
		//console.log('moving point');
	}
	state.newFeature = null;
	map.dragPan.enable();
	canvas.style.cursor = "crosshair";
};

LotsOfPointsMode.onMouseDown = function (state, e) {
	//console.log('mouse down')
	const coords = [e.lngLat.lng, e.lngLat.lat];
	const features = this.map.queryRenderedFeatures(e.point, {
		layers: ["gl-draw-point-inactive.hot", "gl-draw-point-inactive.cold"],
	});
	if (features.length == 0) {
	} else {
		map.dragPan.disable();
		state.selectedFeatureId = features[0].properties.id;
		state.selectedFeature = features[0];
		canvas.style.cursor = "move";
	}
	return state;
};

LotsOfPointsMode.onTouchStart = function (state, e) {
	//console.log('on touch start')
	const coords = [e.lngLat.lng, e.lngLat.lat];
	const features = this.map.queryRenderedFeatures(e.point, {
		layers: ["gl-draw-point-inactive.hot", "gl-draw-point-inactive.cold"],
	});
	if (features.length == 0) {
	} else {
		map.dragPan.disable();
		state.selectedFeatureId = features[0].properties.id;
		state.selectedFeature = features[0];
		canvas.style.cursor = "move";
	}
};

// Whenever a user clicks on the map, Draw will call `onClick`
LotsOfPointsMode.onClick = function (state, e) {
	// `this.newFeature` takes geojson and makes a DrawFeature
	//console.log('click', state)
	const coords = [e.lngLat.lng, e.lngLat.lat];
	const features = this.map.queryRenderedFeatures(e.point, {
		layers: ["gl-draw-point-inactive.hot", "gl-draw-point-inactive.cold"],
	});
	const features2 = this.map.queryRenderedFeatures(e.point, {
		layers: [
			"gl-draw-point-point-stroke-inactive.hot",
			"gl-draw-point-point-stroke-inactive.cold",
		],
	});

	//if there is no feature and nothing selected then add a point
	if (!features.length && !selectedPoint) {
		//console.log('!features.length && !selectedPoint')
		pointcount = pointcount + 1;
		var point = this.newFeature({
			type: "Feature",
			id: pointcount,
			properties: {
				count: state.count,
				id: pointcount,
				name: "point_" + pointcount,
			},
			geometry: {
				type: "Point",
				coordinates: coords,
			},
		});
		this.addFeature(point); // puts the point on the map
		state.lastFeature = draw.get(pointcount);
		addPoint(e.lngLat.lng, e.lngLat.lat, pointcount);
		canvas.style.cursor = "crosshair";
		getPointbyPointMatchings(5, pointcount, e.lngLat.lng, e.lngLat.lat);
		return state;
	}
	//if there is a feature and there is also one which is selected
	if (features.length && selectedPoint) {
		//console.log('features.length && selectedPoint', state.selectedFeatureId, features[0].properties.id)
		//if the feature selected is not the same as the feature clicked
		//then change the selected feature
		if(state.selectedFeatureId != features[0].properties.id) {
			//console.log('state.selectedFeatureId != features[0].properties.id', state.selectedFeatureId != features[0].properties.id)
			updateSelectedColours(features, features2, state);
			map.dragPan.disable();
			state.selectedFeatureId = features[0].properties.id;
			state.selectedFeature = features[0];
			canvas.style.cursor = "move";
		}
		else {
			//reset the point to be not selected
			resetSelectedColours(features, features2, state);
			map.dragPan.enable();
			canvas.style.cursor = "crosshair";
		}
		return state;
	}

	//if there is nothing under the point selected then we want to move the point
	if (!features.length && selectedPoint) {
		//console.log('!features.length && selectedPoint', e.lngLat.lng, e.lngLat.lat, state.selectedFeature.geometry.coordinates, state.selectedFeatureId)
		addDeletePoint(state, e);
		movePoint(
			state.newFeature.geometry.coordinates[0],
			state.newFeature.geometry.coordinates[1],
			state.newFeature.id
		);
		//console.log('moving point')
		map.dragPan.enable();
		canvas.style.cursor = "crosshair";
	}

	//if there is something under the point selected and nothing is selected then select it
	if (features.length && !selectedPoint) {
		//console.log('features.length && !selectedPoint')
		updateSelectedColours(features, features2, state);
	}

	}


		// var currentCircleColor = map.getPaintProperty(
		// 	features[0].layer.id,
		// 	"circle-color"
		// );
		// //console.log(currentCircleColor)
		// //if (currentCircleColor == '#3bb2d0' || "['match', ['get', 'id'], features[0].properties.id, '#ff0000', '#3bb2d0']") {
		// if (currentCircleColor == "#3bb2d0" || !selectedPoint) {
		// 	map.setPaintProperty(features[0].layer.id, "circle-color", [
		// 		"match",
		// 		["get", "id"],
		// 		features[0].properties.id,
		// 		"#ff0000",
		// 		"#3bb2d0",
		// 	]);
		// 	map.setPaintProperty(features[0].layer.id, "circle-radius", [
		// 		"match",
		// 		["get", "id"],
		// 		features[0].properties.id,
		// 		5,
		// 		3,
		// 	]);
		// 	map.setPaintProperty(features2[0].layer.id, "circle-color", [
		// 		"match",
		// 		["get", "id"],
		// 		features2[0].properties.id,
		// 		"#00ff00",
		// 		"#fff",
		// 	]);
		// 	map.setPaintProperty(features2[0].layer.id, "circle-radius", [
		// 		"match",
		// 		["get", "id"],
		// 		features2[0].properties.id,
		// 		7,
		// 		5,
		// 	]);
		// 	state.selectedFeatureId = features[0].properties.id;
		// 	state.selectedFeature = features[0];
		// 	selectedPointId = features[0].properties.id;
		// 	selectedPoint = features[0];
		// 	deletept.disabled = selectedPoint ? "" : "disabled";
		// } else {
		// 	//console.log('reset color')
		// 	map.setPaintProperty(features[0].layer.id, "circle-color", "#3bb2d0");
		// 	map.setPaintProperty(features[0].layer.id, "circle-radius", 3);
		// 	map.setPaintProperty(features2[0].layer.id, "circle-color", "#fff");
		// 	map.setPaintProperty(features2[0].layer.id, "circle-radius", 5);
		// 	var currentCircleColor = map.getPaintProperty(
		// 		features[0].layer.id,
		// 		"circle-color"
		// 	);
		// 	//console.log('cc', currentCircleColor)
		// 	//console.log(features[0], features2[0])
		// 	state.selectedFeatureId = null;
		// 	state.selectedFeature = null;
		// 	selectedPointId = null;
		// 	selectedPoint = null;
		// 	deletept.disabled = selectedPoint ? "" : "disabled";
		// }
	// }
//};

// Whenever a user clicks on a key while focused on the map, it will be sent here
LotsOfPointsMode.onKeyUp = function (state, e) {
	//console.log('on keyup');
	if (e.keyCode === 27) {
		canvas.style.cursor = "grab";
		return this.changeMode("simple_select");
	}
	if (e.keyCode === 8) {
		//console.log('backspace');
	}
};

// This is the only required function for a mode.
// It decides which features currently in Draw's data store will be rendered on the map.
// All features passed to `display` will be rendered, so you can pass multiple display features per internal feature.
// See `styling-draw` in `API.md` for advice on making display features
LotsOfPointsMode.toDisplayFeatures = function (state, geojson, display) {
	display(geojson);
};
