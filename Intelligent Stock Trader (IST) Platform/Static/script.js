document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('fetchButton').addEventListener('click', fetchData);
});

function fetchData() {
  const stockSymbol = document.getElementById('stockSymbol').value;

  fetch('/predict_stock', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ stockSymbol: stockSymbol }),
  })
    .then(response => response.json())
    .then(data => {
      createChart(data);
    })
    .catch(error => console.error('Error:', error));
}

function createChart(data) {
  // Ensure the dates array is available
  if (!data.dates || data.dates.length === 0) {
    console.error('No valid dates provided in the data.');
    return;
  }

  // Combine data for all lines
  var combinedData = data.dates.map(function (date, i) {
    return [new Date(date), data.actual[i], data.fitted[i]];
  });

  // Load Google Charts
  google.charts.load('current', { packages: ['corechart', 'line'] });
  google.charts.setOnLoadCallback(drawChart);

  function drawChart() {
    // Create a DataTable
    var dataTable = new google.visualization.DataTable();
    dataTable.addColumn('date', 'Date');
    dataTable.addColumn('number', 'Actual Prices');
    dataTable.addColumn('number', 'Fitted Values');
    

    // Add data rows
    dataTable.addRows(combinedData);

    // Define chart options
    var options = {
      title: 'Stock Price Prediction',
      legend: { position: 'bottom' },
      hAxis: { title: 'Date' },
      vAxis: { title: 'Values' },
    };

    // Create and draw the chart
    var chart = new google.visualization.LineChart(document.getElementById('stockChart'));
    chart.draw(dataTable, options);
  }
}


