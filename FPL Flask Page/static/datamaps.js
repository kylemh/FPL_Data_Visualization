//convert the Python DataFrame to JSON
var data={{table.to_json(orient ='records') |safe}}
//create an empty object for Datamap
//Datamap expects data in format:
// { "USA": { "fillColor": "#42a844", numberOfWhatever: 75},
// "FRA": { "fillColor": "#8dc386", numberOfWhatever: 43 } }
var dataToMap = {};
 
//pick some values for the color scale range
var maxValue = 25000000;
var minValue = d3.min(data, function(d) { return +d.tourout;} );
 
//create color palette function
var paletteScale = d3.scale.linear()
.domain([minValue,maxValue])
.range(["#EFEFFF","#02386F"]); // blue color
 
//our data does not have the 3 letter ISO code
//so we try to get it by matching the country name
var ctr = Datamap.prototype.worldTopo.objects.world.geometries;
data.forEach(function(d){ //
var iso = "";
for (var i = 0, j = ctr.length; i < j; i++) {
if (ctr[i].properties.name.startsWith(d.countries)){
iso=ctr[i].id};
}
//fill dataset in appropriate format
var value = d.tourout;
dataToMap[iso] = { tourout: value, fillColor: paletteScale(value) };
});
//render map
var map = new Datamap({element: document.getElementById('container'),fills: { defaultFill: '#F5F5F5' },
data: dataToMap});