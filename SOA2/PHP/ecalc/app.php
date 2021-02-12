<!DOCTYPE html>
<html>
<head>
    <title>Ecalc</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
        }
        .workarea {
            text-align: left;
            padding: 50px;
        }
        input[type=text] {
            width: 60%;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        input[type=submit] {
            width: 40%;
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
  $ovolts ="";
  $owatts="";
  $oampere="";
  $volts ="";
  $watts="";
  $ampere="";
  $oKV="";
  $oKW="";
function cal_amperes($v, $p){
    if($p != "None" && $v != "None" || $p != "" && $v != ""){
      $i = $p / $v;
    return $i;
    }
  }
function cal_volts($i, $p){
      if ($i != "None" && $p != "None" || $i != "" && $p != ""){
           $v = $p / $i;
          return $v;
        }
      }
function cal_watts($i, $v){
            if ($i != "None" && $v != "None" || $i != "" && $v != "" ){
                $p = $i * $v;
                return $p;
              }
            }
function cal_kiloWatt($P){
$kW = $P / 1000;
return $kW;
}
function cal_kiloVoltamps($I, $V){
    $s = $V / 1000;
    $SkVA = $I * $s;
    return $SkVA;
  }
if ($_SERVER["REQUEST_METHOD"] == "POST") {
              $watts  = $_POST['watts'];
              $ampere  = $_POST['ampere'];
              $volts  = $_POST['volts'];
              if($watts == ""){
                $owatts = cal_watts($ampere, $volts);
                $oampere = $ampere;
                $ovolts = $volts;
              }
              elseif ($volts == "") {
                $ovolts = cal_volts($ampere, $watts);
                $oampere = $ampere;
                $owatts = $watts;
              }
              else {
                echo "watts".$watts;
                echo "ampere".$ampere;
                echo "volt".$volts;
                $oampere = cal_amperes($volts, $watts);
                $ovolts = $volts;
                $owatts = $watts;
              }
              $oKW = cal_kiloWatt($owatts);
              $oKV = cal_kiloVoltamps($oampere, $ovolts);
            }
?>
<div class="workarea">
<h2><u>E-Calculator</u></h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
<label for="message">Enter watts: </label><br>
<input type="text" id="watts" name="watts" value='<?php echo $watts?>' ><br>
<label for="message">Enter ampere: </label><br>
<input type="text" id="ampere" name="ampere" value='<?php echo $ampere?>' ><br>
<label for="message">Enter volts: </label><br>
<input type="text" id="volts" name="volts" value='<?php echo $volts?>' ><br>
<input type="submit" value="Submit">
</form>
<form class="response_form">
<label for="response">Watts</label><br>
<input type="text" id="stdresponse" name="stdresponse" value='<?php echo $owatts?>'><br>
<label for="response">volts</label><br>
<input type="text" id="vresponse" name="vresponse" value='<?php echo $ovolts?>'><br>
<label for="response">Ampere</label><br>
<input type="text" id="vresponse" name="vresponse" value='<?php echo $oampere?>'><br>
<label for="response">Kilowatt</label><br>
<input type="text" id="vresponse" name="vresponse" value='<?php echo $oKW?>'><br>
<label for="response">Kilovolts</label><br>
<input type="text" id="vresponse" name="vresponse" value='<?php echo $oKV?>'><br>
</form>
</div>
</body>
</html>
