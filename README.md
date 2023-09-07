# MonitoramentoDados
 Projeto de Monitoramento de Dados.


 * Iniciando o repositório.



 <!DOCTYPE html>
<html>
<head>
    <title>Plotly with Flask</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<link rel="stylesheet" href="index.css">
</head>
<body>

  <div id="titulo">
    
  </div>
    <div id="plot">
        {{ plot_div|safe }}
        
         
    </div>
    

<tr></tr>


    <script>
        // Function to reload the plot div every 10 seconds
        function refreshPlot() {
            $.ajax({
                url: "/",
                type: "GET",
                success: function(data) {
                    $("#titulo").html("<h1>Monitoramento de Fluxo</h1>");
                    $("#plot").html(data);
                    
                  
                }
            });
        }

        // Call the refreshPlot function after 10 seconds (10000 milliseconds)
        setInterval(refreshPlot, 10);
    </script>
</body>
</html>

