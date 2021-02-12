<?php
require "controller/otpgeneration.php";
if(!empty($_GET["value"]) ){
   $result = generate();
}
else{
  $result = "";
  echo $result;
}
?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>OTP-Generation</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
        }
        input[type=text] {
            width: 30%;
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
    </style>
</head>
<body>
  <h2><u>OTP - Generation</u></h2>
<form name="otpparser" action="index.php" method="GET">
<input type="hidden" name="value" value="12">
 <input type="submit" value="Generate OTP" name="btn">
</form><br>
<label> OTP  : </label>
<?php echo $result ?>
</body>
</html>
