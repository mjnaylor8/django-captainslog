$(function() {
    $(document).on("reverse-geocode", function (e, map_id, input) { 
      x = $("#" + map_id + ".js-mapbox-address-input-location-field"); 
      x.val(input); 
    }); 
  }); 
  $(function() {
    $(document).on("reverse-geocode-country", function (e, map_id, input) { 
      x = $("#" + map_id + ".js-mapbox-address-country-field"); 
      x.val(input); 
    }); 
  });
  $(function() {
    $(document).on("reverse-geocode-region", function (e, map_id, input) { 
      x = $("#" + map_id + ".js-mapbox-address-region-field"); 
      x.val(input); 
    }); 
  }); 
  $(function() {
    $(document).on("reverse-geocode-district", function (e, map_id, input) { 
      x = $("#" + map_id + ".js-mapbox-address-district-field"); 
      x.val(input); 
    }); 
  });
  $(function() {
    $(document).on("reverse-geocode-place", function (e, map_id, input) { 
      x = $("#" + map_id + ".js-mapbox-address-place-field"); 
      x.val(input); 
    }); 
  }); 
  $(function() {
    $(document).on("reverse-geocode-locality", function (e, map_id, input) { 
      x = $("#" + map_id + ".js-mapbox-address-locality-field"); 
      x.val(input); 
    }); 
  }); 
  $(function() {
    $(document).on("reverse-geocode-postcode", function (e, map_id, input) { 
      x = $("#" + map_id + ".js-mapbox-address-postcode-field"); 
      x.val(input); 
    }); 
  }); 
  $(function() {
    $(document).on("reverse-geocode-line", function (e, map_id, input) { 
      x = $("#" + map_id + ".js-mapbox-address-line-field"); 
      x.val(input); 
    }); 
  }); 
  /*$(document).on("reverse-geocode", function (e, map_id, input) {
      $("#" + map_id + ".js-mapbox-address-input-location-field").val(input);
  });
  $(document).on("reverse-geocode-country", function (e, map_id, input) {
      $("#" + map_id + ".js-mapbox-address-country-field").val(input);
  });
  $(document).on("reverse-geocode-region", function (e, map_id, input) {
      $("#" + map_id + ".js-mapbox-address-region-field").val(input);
  });
  $(document).on("reverse-geocode-district", function (e, map_id, input) {
      $("#" + map_id + ".js-mapbox-address-district-field").val(input);
  });
  $(document).on("reverse-geocode-place", function (e, map_id, input) {
      $("#" + map_id + ".js-mapbox-address-place-field").val(input);
  });
  $(document).on("reverse-geocode-locality", function (e, map_id, input) {
      $("#" + map_id + ".js-mapbox-address-locality-field").val(input);
  });
  $(document).on("reverse-geocode-postcode", function (e, map_id, input) {
      $("#" + map_id + ".js-mapbox-address-postcode-field").val(input);
  });
  $(document).on("reverse-geocode-line", function (e, map_id, input) {
      $("#" + map_id + ".js-mapbox-address-line-field").val(input);
  });*/
  