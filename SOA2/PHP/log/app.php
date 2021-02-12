<!DOCTYPE html>
<html>
<head>
    <title> Lograthim </title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
        }
        .workarea {
            text-align: left;
            padding: 30px;
        }
        input[type=text] {
            width: 25%;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        input[type=submit] {
            width: 20%;
            background-color: #00b359;
            color: white;
            padding: 10px 20px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 17px;
        }
        input[type=submit]:hover {
            background-color: #00994d;
        }
        .response_form {
            padding-top: 50px;
        }
    </style>
</head>
<body>
  <?php
$data = "";
$result = "";
$OpName = "";
function nLog($x) {
   $n = 99999999;
   $pw = (1/$n);
   $resu = pow($x,$pw);
   $res = $resu - 1;
  $rea  = $n*$res;
  return $rea;
}
function clog($x, $base) {
    $result = nLog($x) / nLog($base);
    return $result;
}
function antiLog($a,$b){
    $c = 1;
    for ($i=1; $i < $b+1; $i++) {
      $c = $c * $a;
    }
    return $c;
}
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $opChoice = $_POST['opChoice'];
    if ($opChoice == 0){
        $data = $_POST['numb'];
        $base = $_POST['base'];
        $OpName = "Log ";
        $result = clog($data, $base);
        $data .= ' base '.$base;
    }
    elseif ($opChoice == 1){
        $data = $_POST['numn'];
        $result = nLog($data);
        $OpName = "Natural Log ";
    }
    elseif($opChoice == 2){
        $data = $_POST['numa'];
        $pow = $_POST['pow'];
        $result = antiLog($data, $pow);
        $OpName = "AntiLog ";
        $data .= ' power '.$pow;
    }
}
?>
<body>
    <div class="workarea">
      <h2><u>Lograthim</u></h2>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
      <label for="data">Choose operation : </label>
            <select name="opChoice" id="opChoice" onchange="changeset()">
                <option id="log" value="0" selected='true'>Logarithm(log)</option>
                <option id="nlog" value="1">Natural Logarithm (ln)</option>
                <option id="antilog" value="2"> Anti-logarithm </option>
            </select>
            </br>
            <div id="opset1" style="display: block;">
                <label for="data">Enter Number : </label>
                <input type="text" id="numb" name="numb"></br>
                <label for="data">Enter Base : </label>
                <input type="text" id="base" name="base"></br>
            </div>
            <div id="opset2" style="display: none;">
                <label for="data">Enter Number:</label>
                <input type="text" id="numn" name="numn"></br>
            </div>
            <div id="opset3" style="display: none;">
                <label for="data">Enter Number:</label>
                <input type="text" id="numa" name="numa"></br>
                <label for="data">Enter Power:</label>
                <input type="text" id="pow" name="pow"></br>
            </div>
            <input type="submit" value="Submit">
        </form>
        <form class="response_form">
            <label for="result"><?php echo $OpName; ?> of <?php echo $data; ?> is : </label>
            <input type="text" id="result" name="result" value="<?php echo $result; ?>"></br>
        </form>
    </div>
    <script>
        function changeset() {
            const opChoice = document.getElementById('opChoice').value;
            if (opChoice == '0') {
                document.getElementById('opset1').style.display = "block"
                document.getElementById('opset2').style.display = "none"
                document.getElementById('opset3').style.display = "none"
                document.getElementById('result').value = ""
            } else if (opChoice == '1') {
                document.getElementById('opset1').style.display = "none"
                document.getElementById('opset2').style.display = "block"
                document.getElementById('opset3').style.display = "none"
                document.getElementById('result').value = ""
            } else {
                document.getElementById('opset1').style.display = "none"
                document.getElementById('opset2').style.display = "none"
                document.getElementById('opset3').style.display = "block"
                document.getElementById('result').value = ""
            }
        }
    </script>
</body>
</html>
