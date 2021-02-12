<!DOCTYPE html>
<html>
<head>
    <title>Trigonomentry</title>
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
  $sinvalue = "";
  $cosvalue="";
  $tanvalue="";
  $secvalue="";
  $cosecvalue="";
  $cotvalue="";
  $value="";
  $inpval="";
function my_sin($theta){
    $theta = $theta * (3.1415/180);
    $d_theta = ($theta + 3.1415) %(2 * 3.1415);
    $theta = $d_theta - 3.1415;
    $result = 0;
    $termsign = 1;
    $power = 1;
    for($i = 0 ; $i <10 ; $i++){
      $factorial_value = fun_Factorial($power);
      $pow_theta = $theta**$power;
      $result = $result + (($pow_theta/$factorial_value) * $termsign);
      $termsign = $termsign * (-1);
      $power = $power + 2;
    }
    return $result;
  }
function my_cos($theta_c){
  $dummy_var = my_sin($theta_c);
  $var_dum = $dummy_var * $dummy_var;
  $pow_c = 1 - $var_dum;
  $result_c = sqrt($pow_c);
  return $result_c;
}
function my_tan($theta){
    $va = my_sin($theta);
    $vb =  my_cos($theta);
    return($va/$vb);
}
function my_sec($theta){
  $vbsec = my_cos($theta);
    return  (1 / $vbsec);
}
function my_cosec($theta){
  $vbcosec = my_sin($theta);
    return  (1 / $vbcosec);
}
function my_cot($theta){
  $vbcot = my_tan($theta);
    return ( 1 / $vbcot);
}
  function fun_factorial($nums){
        $factorial = $nums;
        if($factorial == 0){
          $factorial = 1;
        }
        else{
        for ($x = 1; $x <= $nums; $x++){
          $factorial = $factorial * $x;
        }
      }
      return $factorial;
    }
  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $number  = $_POST['value'];
    $inpval = $number;
    $sinvalue = my_sin($number);
    // echo $number;
    $cosvalue = my_cos($number);
    $tanvalue = my_tan($number);
    $secvalue = my_sec($number);
    $cosecvalue = my_cosec($number);
    $cotvalue = my_cot($number);
  }
?>
<div class="workarea">
  <h2><u>Trigonomentry</u></h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
<label for="message">Enter degree: eg(60)</label><br>
<input type="text" id="value" name="value" value='<?php echo $value?>'required><br>
<input type="submit" value="Submit">
</form>
<form class="response_form">
<label for="response">Input</label><br>
<input type="text" id="sresponse" name="sresponse" value='<?php echo $inpval?>'><br>
<label for="response">Sin</label><br>
<input type="text" id="sresponse" name="sresponse" value='<?php echo $sinvalue?>'><br>
<label for="response">Cos</label><br>
<input type="text" id="sresponse" name="sresponse" value='<?php echo $cosvalue?>'><br>
<label for="response">Tan</label><br>
<input type="text" id="sresponse" name="sresponse" value='<?php echo $tanvalue?>'><br>
<label for="response">Sec</label><br>
<input type="text" id="sresponse" name="sresponse" value='<?php echo $secvalue?>'><br>
<label for="response">Cosec</label><br>
<input type="text" id="sresponse" name="sresponse" value='<?php echo $cosecvalue?>'><br>
<label for="response">Cot</label><br>
<input type="text" id="sresponse" name="sresponse" value='<?php echo $cotvalue?>'><br>
</form>
</div>
</body>
</html>
