class ReviewChart{
    // constructor(divid){
    //     this.chartsvg = d3.select(divid).append("svg");
    // }

    initChart(result){
        var width = 1200,
          height = 500;
        var x1 = d3.scaleBand()
                .range([0, width])
                .padding(0.2);
        var y1 = d3.scaleLinear()
                .range([height, 0]);

        x1.domain(result[1].map(function(d) { return d.year; }));
        y1.domain(d3.extent(result[1], function(d) { 
        return +d.num_of_reviews; 
        }));

        var svg2 = d3.select("#reviews_bar_chart").append("svg")
        .attr("width", width)
        .attr("height", height+100)
        .append("g")
        .attr("transform", 
                "translate(" + 40 + "," + 40 + ")");


        svg2.selectAll(".review-bar")
        .data(result[1])
        .enter().append("rect")
        .style("fill", function(d){
            return "#e48268"
        })
        .attr("class", "review-bar")
        .attr("id", function(d) { return d.year; })
        .attr("x", function(d) { 
            return x1(d.year);
        })
        .attr("width", x1.bandwidth()-30)
        .attr("y", function(d) {
            return  y1(d.num_of_reviews);
        })
        .attr("height", function(d) { return height - y1(d.num_of_reviews); })
        .on("mouseover", function(d){
            var year = d.year;
            svg2.selectAll("rect")
                .style("opacity", function(d){
                if(d.year == year){
                    return 1;
                } else {
                    return 0.25;
                }
                })
        })
        .on("mouseout", function(d){
            svg2.selectAll("rect")
            .style("opacity", 1);
  })


  svg2.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x1)
      .tickFormat(function(d) {
          return d;
        }));
      //   .selectAll("text")
      // .attr("y", 0)
      // .attr("x", 40)
      // .attr("dy", ".35em")
      // .attr("transform", "rotate(90)");
  

// add the y Axis
svg2.append("g")
  .call(d3.axisLeft(y1));
    }

    updateRangeValues(minyear, maxyear){
        var bars = $(".review-bar");
        for(var i=0; i<bars.length; i++){
            var each_bar = $(bars[i]);
            if(minyear > each_bar.attr("id") || each_bar.attr("id") > maxyear){
                each_bar.css("fill", "#DDD");
            }else{
                each_bar.css("fill", "#e48268");
            }
        }
    }
}

class ListingChart{
    
    initChart(result){
        var width = 1200,
          height = 500;
        var x1 = d3.scaleBand()
                        .range([0, width])
                        .padding(0.2);
        
        var y2 = d3.scaleLinear()
        .range([height, 0]);

        x1.domain(result[1].map(function(d) { return d.year; }));
        y2.domain(d3.extent(result[2], function(d) { 
            return +d.num_of_listings; 
          }));

        var svg3 = d3.select("#listings_bar_chart").append("svg")
            .attr("width", width)
            .attr("height", height+100)
            .append("g")
            .attr("transform", 
                  "translate(" + 40 + "," + 40 + ")");


        svg3.selectAll(".listing-bar")
            .data(result[2])
          .enter().append("rect")
            .style("fill", function(d){
                return "#6bacd0"
            })
            .attr("class", "listing-bar")
            .attr("id", function(d) { return d.year; })
            .attr("x", function(d) { 
              return x1(d.year);
            })
            .attr("width", x1.bandwidth())
            .attr("y", function(d) {
              return  y2(d.num_of_listings);
            })
            .attr("height", function(d) { return height - y2(d.num_of_listings); })
            .on("mouseover", function(d){
              var year = d.year;
              svg3.selectAll("rect")
                  .style("opacity", function(d){
                    if(d.year == year){
                      return 1;
                    } else {
                      return 0.25;
                    }
                  })
            })
            .on("mouseout", function(d){
              svg3.selectAll("rect")
              .style("opacity", 1);
            })
          
          
            svg3.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x1)
                .tickFormat(function(d) {
                    return d;
                  }));
                //   .selectAll("text")
                // .attr("y", 0)
                // .attr("x", 40)
                // .attr("dy", ".35em")
                // .attr("transform", "rotate(90)");
            

        // add the y Axis
        svg3.append("g")
            .call(d3.axisLeft(y2));
    }

    updateRangeValues(minyear, maxyear){
        var bars = $(".listing-bar");
        for(var i=0; i<bars.length; i++){
            var each_bar = $(bars[i]);
            if(minyear > each_bar.attr("id") || each_bar.attr("id") > maxyear){
                each_bar.css("fill", "#DDD");
            }else{
                each_bar.css("fill", "#6bacd0");
            }
        }
    }
}