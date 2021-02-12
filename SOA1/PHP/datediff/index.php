<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Date Difference</title>
    <style>
    body {
        font-family: Arial, Helvetica, sans-serif;
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
  <?php
  require "controller/sum.php";
  // header("content-type:application/json");
  $result = "";
  $d1 ="";
  $d2 ="";
  $t1 ="";
  $t2 ="";
  $times="";
  if(!empty($_GET["d1"]) && !empty($_GET["d2"]) ){
      $d1= $_GET["d1"];
      $d2= $_GET["d2"];
      $t1= $_GET["t1"];
      $t2= $_GET["t2"];
      $times=tum($t1,$t2);
      $result=sum($d1,$d2,$t1,$t2);
  }
  ?>
<form name="dateparser" action="index.php" method="GET">
  <label>From date and time :</label><br>
 <input type="date" name="d1" required>&nbsp;&nbsp;
  <input type="time" id="t1" name="t1" step="1" required><br><br>
 <label>To date and time :</label><br>
 <input type="date" name="d2" required>&nbsp;&nbsp;
  <input type="time" id="t2" name="t2" step="1" required><br><br>
 <input type="submit" value="Find difference">
</form>
<br>
<label>From date :</label> <?php echo $d1;?>
<br>
<label>From time :</label> <?php echo $t1;?>
<br>
<br>
<label>To date :</label><?php echo $d1;?>
<br>
<label>To time :</label> <?php echo $t2;?>
<br>
<br>
<label> Result [dd,mm,yy] : </label>
<?php
 echo $result;
 ?>
 <br>
 <label> Time [ss,mm,yy] : </label>
 <?php
  echo $times;
  ?>
</body>
</html>
