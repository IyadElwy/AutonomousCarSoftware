<html>

<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">

<head>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js" type="text/javascript"
        charset="utf-8"></script>

    <style>
        .controls {
            width: 250px;
            height: 100px;
            font-size: 32pt;
            text-align: center;
            padding: 15px;
            background-color: green;
            color: white;
            user-select: none;
        }

        body{
        	touch-action: manipulation;
        }
    </style>

    <script>
        function sendCommand(command) {
            if (command == "change_mode") {
                var mode = document.getElementById("change_mode_input").innerText;
                if (mode == "DRIVING") {
                   document.getElementById("change_mode_input").innerText = "TRAINING";
                } else if (mode == "TRAINING") {
                   document.getElementById("change_mode_input").innerText = "AI";
                } else if (mode == "AI") {
                    document.getElementById("change_mode_input").innerText = "DRIVING";
                }
            }

            $.get('/', { command: command });
            event.preventDefault();
            event.returnValue = false;

        }
        
    </script>
</head>

<body style="user-select: none;   -webkit-user-select: none;
  -ms-user-select: none; touch-action: manipulation;">
    </br>
    </br>
    </br>
    </br>
    </br>
    </br>
    </br>

    <table border="1" width="100%">
        <col style="width:40%">
        <col style="width:30%">

        <tr>
            <td class="controls" onpointerup="sendCommand('s_fb')" onpointerdown="sendCommand('f');">F</td>
            <td class="controls" id="change_mode_input">DRIVING</td>
        </tr>
        <tr>
            <td class="controls" onpointerup="sendCommand('s_fb')" onpointerdown="sendCommand('b');">B</td>
            <td>
                <table align="center">
                    <tr>
                        <td class="controls" onpointerup="sendCommand('s_lr')" onpointerdown="sendCommand('r');">L</td>
                        <td class="controls" onpointerup="sendCommand('s_lr')" onpointerdown="sendCommand('l');">R</td>

                    </tr>

                </table>
            </td>
        </tr>



    </table>
</body>

</html>
