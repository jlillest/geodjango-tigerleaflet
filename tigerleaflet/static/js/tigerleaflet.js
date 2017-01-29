
var link_prefix ='';
var geoJson;
var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info');
    this.update();
    return this._div;
};

info.update = function (properties) {
    var html = '<h2>' + (properties ? properties.name : "") + '</h2>';
    this._div.innerHTML = html;
};

function tigerleafletMap(mapName, coordinates=[37.22, -90.41], zoom=3) {
    var map = L.map(mapName).setView(coordinates, zoom);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map);
    info.addTo(map);
    return map
}

function getGeojson(map_data) {
  link_prefix = map_data['prefix'];

  $.ajax({
    type: "POST",
    url: map_data['url'],
    data: map_data['data'],
  }).done(function (ajax) {
    addData(map_data['map'], map_data['function'], map_data['zoom'], ajax);
  });
}

function addData(map, goToFunction, zoom, data) {
  geojson = L.geoJson(data, {
    style: function (feature) {
        return getStyle(getColor(feature.properties.fips_code));
    },
    onEachFeature: function (feature, layer) {
        layer.on({
            mouseover: highlightFeature,
            mouseout: resetHighlight,
            click: goToFunction,
        });
    }
  }).addTo(map);

  if (zoom)
  {
    map.fitBounds(geojson);
  }
}

function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle(getStyle('#000000'))

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }

    info.update(layer.feature.properties);
}

function resetHighlight(e) {
    geojson.resetStyle(e.target);
    info.update();
}

function goToState(e) {
    var feature = e.target.feature;
    var state_usps_code = feature.properties.usps_code.toLowerCase();
    window.location.href = link_prefix + state_usps_code;
}

function goToCounty(e) {
    var usps_code = e.target.feature.properties.usps_code.toLowerCase();
    var county_name = e.target.feature.properties.name.toLowerCase().split(' ').join('_');
    window.location.href = link_prefix + usps_code + '/' + county_name;
}

function getStyle(color_code) {
    return {
        color: color_code,
        weight: 5,
        dashArray: '',
        fillOpacity: 0.5,
    }
}

function getColor(number) {
    var colors = ['#D9DA32', '#8D8B6F',
                  '#1EBBC0', '#85B410',
                  '#96D480', '#802E46',
                  '#055647', '#C67521',
                  '#C9732B', '#09274D' ];
    return colors[number % 10];
}
