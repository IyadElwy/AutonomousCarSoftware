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
    </style>

    <script>
        function sendCommand(command) {
            if (command == "change_mode") {
                var mode = $("change_mode_input").text();
                if (mode == "DRIVING") {
                    $("change_mode_input").text("TRAINING");
                } else if (mode == "TRAINING") {
                    $("change_mode_input").text("AI");
                } else if (mode == "AI") {
                    $("change_mode_input").text("DRIVING");
                }
            }

            $.get('/', { command: command });
            event.preventDefault();
            event.returnValue = false;

        }
        function keyPress(event) {
            code = event.keyCode;
            if (code == 119) {
                sendCommand('f');
            }
            else if (code == 97) {
                sendCommand('l');
            }
            else if (code == 115) {
                sendCommand('s');
            }
            else if (code == 100) {
                sendCommand('r');
            }
            else if (code == 122) {
                sendCommand('b');
            }
        }
        $(document).keypress(keyPress);
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
            <td class="controls" id="change_mode_input" onpointerdown="sendCommand('change_mode');">DRIVING</td>
        </tr>
        <tr>
            <td class="controls" onpointerup="sendCommand('s_fb')" onpointerdown="sendCommand('b');">B</td>
            <td>
                <table align="center">
                    <tr>
                        <td class="controls" onpointerup="sendCommand('s_lr')" onpointerdown="sendCommand('r');">R</td>
                        <td class="controls" onpointerup="sendCommand('s_lr')" onpointerdown="sendCommand('l');">L</td>

                    </tr>

                </table>
            </td>
        </tr>



    </table>
</body>

</html>