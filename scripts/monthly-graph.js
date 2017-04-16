
Plotly.d3.csv('../data/monthly.csv', function(rows){
  var trace = {
    type: 'scatter',                    // set the chart type
    mode: 'lines',                      // connect points with lines
    x: rows.map(function(row){          // set the x-data
      return row['Date'];
    }),
    y: rows.map(function(row){          // set the y-data
      return row['Price'];
    }),
    line: {                             // set the width of the line.
      width: 1
    },
  };

  var layout = {
    title: 'Henry Hub Natural Gas Spot Price Monthly',
    yaxis: {title: "Dollars per Million Btu"},       // set the y axis title
    xaxis: {
      showgrid: false,                  // remove the x-axis grid lines
      tickformat: "%B, %Y"
    },
    margin: {                           // update the left, bottom, right, top margin
      l: 40, b: 20, r: 10, t: 30
    }
  };

  Plotly.plot(document.getElementById('monthly-graph'), [trace], layout, {showLink: false});
});
