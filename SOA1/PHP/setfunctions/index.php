<?php
$a = "";
$b = "";
$val ="";
$result= "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
if(!empty($_POST["setoperation"]) ){
  $val = $_POST["setoperation"];
  $a = $_POST['setA'];
  $b = $_POST['setB'];
  $seta = explode(',',$a);
  $setb = explode(',',$b);
  if($val == "union"){
   // $result = array_union($seta, $setb);
   $result =implode(',', (array_merge($seta, $setb)));
 }elseif ($val == "intersect") {
     //$result = intersect_array($seta, $setb);
     $result = implode(',', (array_intersect($seta, $setb)));
   }else {
     //$result = differce_array($seta, $setb);
     $result = implode(',', (array_diff($seta, $setb)));
   }
}
}
?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SET- theory</title>
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
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
<!-- <input type="hidden" name="value" value="12"> -->
<br>
<label >Set A : </label><br>
            <input type="text" id="setA" name="setA" required><br>
            <label for="message">Set B : </label><br>
            <input type="text" id="setB" name="setB" required><br>
            <label for="message">Operation </label><br>
            <select name="setoperation" id="setoperation" required>
              <option value="union">Union</option>
              <option value="interset">Intersection</option>
              <option value="diff">Difference</option>
            </select>
            <br>
 <input type="submit" value="Generate array" name="btn">
</form><br>
<label >Set A : </label><?php echo $a ?>  <br>
<label >Set B : </label><?php echo $b ?>  <br>
<label >Operation : </label><?php echo $val ?>  <br>
<label >Result : </label>
<?php echo $result ?>
</body>
</html>
