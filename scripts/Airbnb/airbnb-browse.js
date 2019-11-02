

$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
      $(this).toggleClass('active');
    });

    var metadata;


    d3.csv("/datasets/airbnb/ego_metadata.csv", function (error, data) {
      metadata = data;
    });


    loadCities = function (countryname) {
        var i = 0;
        var rowDiv;
        d3.selectAll(".cities > *").remove();
        metadata.filter(function (d) {

            return d.Country == countryname;
        }).forEach(function (d,i) {

            console.log(d.City);
            if(i%3 == 0){
                rowDiv = d3.select(".cities")
                                .append("div")
                                .attr('class', 'row')
                    .style('padding-top','2%');

            }

            rowDiv.append('div')
                .attr('class', 'col-md-4')
                .append('div')
                .attr('class', 'card')
                .append('div')
                .attr('class', 'card-body')
                .text(d.City)
                .on('click', function () {
                    // var a = new loadFlower("/datasets/airbnb/filepath", d.City, "neighbourhood", "room_type" );
                    window.location = "/Airbnb/airbnb-create-flower.html?path="+ "/datasets/airbnb/filepath" + "&ego=" + d.City + "&petalColumn=" + "neighbourhood" + "&extensionColumn=" + "room_type";
                });



        });



    }







  });


