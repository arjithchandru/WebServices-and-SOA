<!DOCTYPE html>
<html>
<head>
    <title>GCF,LCM</title>
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
      function gcd($a, $b){
        while ($b > 0){
          $temp = $b;
          $b = $a % $b;
          $a = $temp;
        }
        return $a;
      }
      $gcdvalue = "";
      $value="";
      $lcmvalue="";
      $inpval = "";
      if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $number  = $_POST['value'];
        $inpval = $number;
        $arr = explode(',',$number);
        $array = explode(',',$number);
        // print_r($array);
        $arrcount = count($arr);
        $result = $arr[0];
        $ans = $array[0];
        for ($x = 0; $x < $arrcount; $x++) {
        $result = gcd($result, $arr[$x]);
        }
        $gcdvalue = $result;
        for ($i = 0; $i < $arrcount; $i++){
          // $ans = (
          //           (($array[$i] * $ans)) / (gcd($array[$i], $ans))
          //   );
            $aar = $array[$i] * $ans;
            //echo "aar".$aar;
            $abr = gcd($array[$i], $ans);
            //echo "abr".$abr;
            $ans = $aar/$abr;
            //echo "ans".$ans;
        }
        $lcmvalue = $ans;
      }
      ?>
<div class="workarea">
  <h2><u>GCF, LCM</u></h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
<label for="message">Enter numbers: eg(25,12,13)</label><br>
<input type="text" id="value" name="value" value='<?php echo $value?>'required><br>
<input type="submit" value="Submit">
</form>
<form class="response_form">
  <label for="response">Input</label><br>
  <input type="text" id="sresponse" name="sresponse" value='<?php echo $inpval?>'><br>
<label for="response">GCF</label><br>
<input type="text" id="sresponse" name="sresponse" value='<?php echo $gcdvalue?>'><br>
<label for="response">LCM</label><br>
<input type="text" id="sresponse" name="sresponse" value='<?php echo $lcmvalue?>'><br>
</form>
</div>
</body>
</html>
