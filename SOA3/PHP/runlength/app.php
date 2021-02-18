<!DOCTYPE html>
<html>
<head>
    <title>Run - Length</title>
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
      $inpval = "";
      $opval = "";

      if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $msg = $_POST['value'];
        $inpval = $msg;
        $list = array();
      array_push($list,run_length_algorithm_encode($msg));
      // array_push($list,run_length_algorithm_Decode(run_length_algorithm_encode($msg)));
      $Obj = new \stdClass();
      $Obj->compressed = $list;
      $opval = json_encode($Obj);
      // echo $JSON;
  }

  function run_length_algorithm_encode($msg){
      $encoded_msg = "" ;
      $i = 0;
      while ($i <= (strlen($msg))-1){
          $count = 1;
          $ch = $msg[$i];
          $j = $i ;
          while ($j < (strlen($msg))-1){
              if ($msg[$j] == $msg[$j+1]){
                  $count = $count+1;
                  $j = $j+1;
              }
              else{
                  break;
              }
          }
          $encoded_msg=$encoded_msg . $ch . (string)($count);
          $i = $j+1;
      }
      return $encoded_msg;
  }
      ?>
<div class="workarea">
  <h2><u>Run - Length</u></h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
<label for="message">Enter text:</label><br>
<input type="text" id="value" name="value" required><br>
<input type="submit" value="Submit">
</form>
<form class="response_form">
  <label for="response">Input</label><br>
  <input type="text" id="sresponse" name="sresponse" value='<?php echo $inpval?>'><br>
<label for="response">Result</label><br>
<input type="text" id="sresponse" name="sresponse" value='<?php echo $opval?>'><br>

</form>
</div>
</body>
</html>
