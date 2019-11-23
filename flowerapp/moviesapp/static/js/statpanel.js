var genres = config.flower_name;
console.log(config);

var svg_1strow = d3.select('.sidepanel_1strow').append("svg")
    .attr("width", d3.select('.sidepanel_1strow').style("width").replace("px", ""))
    .attr("height", 55);

svg_1strow.append("text")
    .attr("x", 20)
    .attr("y", 35)
    .text("Select YearRange")
    .attr("font-size", "18px")
    .attr("font-weight", 600);

svg_1strow.append("circle")
    .attr("class", "noofmovies_circle")
    .attr("cx", d3.select("svg").attr("width")-250)
    .attr("cy", 30)
    .attr("r", 6)
    .style("fill", "#ABBD81")

svg_1strow.append("text")
    .attr("x", d3.select("svg").attr("width")-240)
    .attr("y", 35)
    .text("No. of Movies")
    .attr("font-size", "15px");

svg_1strow.append("circle")
    .attr("class", "averagerating_circle")
    .attr("cx", d3.select("svg").attr("width")-135)
    .attr("cy", 30)
    .attr("r", 6)
    .style("fill", "#F47E60")

svg_1strow.append("text")
    .attr("x", d3.select("svg").attr("width")-125)
    .attr("y", 35)
    .text("Average Rating")
    .attr("font-size", "15px");

var defaultnoofmovies = config.statpanel_default_data;
var default_firstyear = defaultnoofmovies[0]["year"];
var default_endyear = defaultnoofmovies[defaultnoofmovies.length-1]["year"];
var nm_xticklist_list = d3.range(default_firstyear, default_endyear, (Math.round((default_endyear - default_firstyear)/10)));
var nummovies_years = defaultnoofmovies.map(function(d) { return d.year; });
var nummovies_count = defaultnoofmovies.map(function(d) { return d.count; });
var nummovies_xticklist = [];

for(var i = 0; i < nm_xticklist_list.length; i++) {
    if(nummovies_years.includes(String(nm_xticklist_list[i])) == true){
        nummovies_xticklist.push(nm_xticklist_list[i])
    }
}

var x_nummovies = d3.scaleBand().range([0, 480]).padding(0.2);
var y_nummovies = d3.scaleLinear().range([145, 0]);

var nummovies_chart = d3.select('.sidepanel_movies_barchart').append("svg")
    .attr("width", d3.select('.sidepanel_1strow').style("width").replace("px", ""))
    .attr("height", 180);

x_nummovies.domain(nummovies_years);
y_nummovies.domain([0, (d3.max(nummovies_count)+3)]);

nummovies_chart.append("g")
    .attr("class", "nummovies_xaxis")
    .style("font-size", "13px")
    .style("font-weight", 100)
    .call(d3.axisTop(x_nummovies).tickValues(nummovies_xticklist))
    .attr("transform", "translate(35, 25)");
nummovies_chart.append("g")
    .attr("class", "grid")
    .call(d3.axisBottom(x_nummovies).tickSize(145).tickFormat(""))
    .attr("transform", "translate(35, 25)");

nummovies_chart.append("g")
    .attr("class", "nummovies_yaxis")
    .style("font-size", "13px")
    .style("font-weight", 100)
    .call(d3.axisLeft(y_nummovies).ticks(5))
    .attr("transform", "translate(35,25)");
nummovies_chart.append("g")
    .attr("class", "grid")
    .call(d3.axisRight(y_nummovies).tickSize(480).tickFormat("").ticks(5))
    .attr("transform", "translate(35, 25)");

nummovies_chart.selectAll(".bar-nummovies")
    .data(defaultnoofmovies)
    .enter().append("rect")
    .attr("class", "bar-nummovies")
    .attr("id", function(d) { return d.year; })
    .attr("x", function(d) { return x_nummovies(d.year); })
    .attr("width", x_nummovies.bandwidth())
    .attr("y", function(d) { return y_nummovies(d.count); })
    .attr("height", function(d) { return 145-y_nummovies(d.count);})
    .style("fill", "#ABBD81")
    .style("cursor", "pointer")
    .attr("transform", "translate(35, 25)");

var nummovieslider = document.getElementById('noofmovies_range');
noUiSlider.create(nummovieslider, {
    connect: true,
    behaviour: 'tap',
    start: [parseInt(default_firstyear), parseInt(default_endyear)],
    step: 1,
    animate: false,
    range: {
        'min' : [parseInt(default_firstyear)],
        'max' : [parseInt(default_endyear)]
    }
});

var noUIhandles = [
    nummovieslider.getElementsByClassName('noUi-handle-lower')[0],
    nummovieslider.getElementsByClassName('noUi-handle-upper')[0]
];

var labels = [];

nummovieslider.noUiSlider.on('update', function (values, handle) {
    noUIhandles[handle].innerText = parseInt(values[handle]);
    updateyears();
});

function updateyears() {
    nummovies_start = parseInt(noUIhandles[0].innerText)
    nummovies_end = parseInt(noUIhandles[1].innerText)
    // updatenummovies(nummovies_start, nummovies_end);
}

