/* ------------------------------------------------------------------------------
 *
 *  # D3.js - histogram chart
 *
 *  Demo d3.js histogram chart setup with tooltip and random data
 *
 * ---------------------------------------------------------------------------- */

// Setup module
// ------------------------------

var D3BarHistogram = (function () {
  //
  // Setup module components
  //

  // Chart
  var _barHistogram = function () {
    if (typeof d3 == "undefined") {
      console.warn("Warning - d3.min.js is not loaded.");
      return;
    }

    // Main variables
    var element = document.getElementById("d3-histogram"),
      height = 400;

    // Initialize chart only if element exsists in the DOM
    if (element) {
      // Basic setup
      // ------------------------------

      // Define main variables
      var d3Container = d3.select(element),
        margin = { top: 15, right: 20, bottom: 20, left: 60 },
        width =
          d3Container.node().getBoundingClientRect().width -
          margin.left -
          margin.right,
        height = height - margin.top - margin.bottom - 5;

      // Generate a Bates distribution of 10 random variables.
      var values = d3.range(100).map(d3.random.bates(4));

      // Data format
      var formatCount = d3.format(",.0f");

      // Colors
      var color = d3.scale
        .ordinal()
        .range([
          "#98abc5",
          "#8a89a6",
          "#7b6888",
          "#6b486b",
          "#a05d56",
          "#d0743c",
          "#ff8c00",
        ]);

      // Construct scales
      // ------------------------------

      // Horizontal
      var x = d3.scale.linear().domain([0, 1]).range([0, width]);

      // Generate a histogram using twenty uniformly-spaced bins.
      var data = d3.layout.histogram().bins(x.ticks(10))(values);

      console.log("x", x);
      console.log("vals", values);
      console.log("data", data);

      // Vertical
      var y = d3.scale
        .linear()
        .domain([
          0,
          d3.max(data, function (d) {
            return d.y;
          }),
        ])
        .range([height, 0]);

      // Create axes
      // ------------------------------

      // Horizontal
      var xAxis = d3.svg.axis().scale(x).orient("bottom");

      // Create chart
      // ------------------------------

      // Add SVG element
      var container = d3Container.append("svg");

      // Add SVG group
      var svg = container
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      // Add tooltip
      // ------------------------------

      // Create tooltip
      var tip = d3
        .tip()
        .attr("class", "d3-tip")
        .offset([-25, 0])
        .html(function (d) {
          return (
            "Current value: " +
            "<span class='font-weight-semibold'>" +
            formatCount(d.y) +
            "</span>"
          );
        });

      // Initialize tooltip
      svg.call(tip);

      //
      // Append chart elements
      //

      // Add bars
      // ------------------------------

      // Group each bar
      var bar = svg
        .selectAll(".d3-bar")
        .data(data)
        .enter()
        .append("g")
        .attr("class", "d3-bar")
        .attr("transform", function (d) {
          return "translate(" + x(d.x) + "," + y(d.y) + ")";
        })
        .on("mouseover", tip.show)
        .on("mouseout", tip.hide);

      // Append bars
      bar
        .append("rect")
        .attr("x", 1)
        .attr("width", x(data[0].dx) - 3)
        .attr("height", function (d) {
          return height - y(d.y);
        })
        .style("fill", function (d) {
          return color(d);
        });

      // Append text
      bar
        .append("text")
        .attr("class", "d3-text")
        .attr("dy", ".75em")
        .attr("y", -15)
        .attr("x", x(data[0].dx) / 2)
        .style("text-anchor", "middle")
        .text(function (d) {
          return formatCount(d.y);
        });

      // Append axes
      // ------------------------------

      // Horizontal
      svg
        .append("g")
        .attr("class", "d3-axis d3-axis-horizontal")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

      // Resize chart
      // ------------------------------

      // Call function on window resize
      window.addEventListener("resize", resize);

      // Call function on sidebar width change
      var sidebarToggle = document.querySelectorAll(".sidebar-control");
      if (sidebarToggle) {
        sidebarToggle.forEach(function (togglers) {
          togglers.addEventListener("click", resize);
        });
      }

      // Resize function
      //
      // Since D3 doesn't support SVG resize by default,
      // we need to manually specify parts of the graph that need to
      // be updated on window resize
      function resize() {
        // Layout variables
        width =
          d3Container.node().getBoundingClientRect().width -
          margin.left -
          margin.right;

        // Layout
        // -------------------------

        // Main svg width
        container.attr("width", width + margin.left + margin.right);

        // Width of appended group
        svg.attr("width", width + margin.left + margin.right);

        // Axes
        // -------------------------

        // Horizontal range
        x.range([0, width]);

        // Horizontal axis
        svg.selectAll(".d3-axis-horizontal").call(xAxis);

        // Chart elements
        // -------------------------

        // Bar group
        svg.selectAll(".d3-bar").attr("transform", function (d) {
          return "translate(" + x(d.x) + "," + y(d.y) + ")";
        });

        // Bar rect
        svg
          .selectAll(".d3-bar rect")
          .attr("x", 1)
          .attr("width", x(data[0].dx) - 3);

        // Bar text
        svg.selectAll(".d3-bar text").attr("x", x(data[0].dx) / 2);
      }
    }
  };

  //
  // Return objects assigned to module
  //

  return {
    init: function () {
      _barHistogram();
    },
  };
})();

// Initialize module
// ------------------------------

document.addEventListener("DOMContentLoaded", function () {
  D3BarHistogram.init();
});
