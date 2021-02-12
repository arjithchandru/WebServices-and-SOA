<!DOCTYPE html>
<html>
<head>
    <title>Basic Static Calculator</title>
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
      $standardevi = "";
      $variances = "";
      $value = "";
      $flag = 0;
      if ($_SERVER["REQUEST_METHOD"] == "POST") {
          $number  = $_POST['value'];
          $arr = explode(',',$number);
          $arrayOfNumbers = explode(',',$number);
          if (empty($number)) {
              echo "<p class='err_proc'>Invalid Figure</p>";
              $flag = 1;
          }
            else {
              // function Stand_Deviation($arr){
                      $num_of_elements = count($arr);
                      $variance = 0.0;
                              // calculating mean using array_sum() method
                      $average = array_sum($arr)/$num_of_elements;
                      foreach($arr as $i)
                      {
                          // sum of squares of differences between
                                      // all numbers and means.
                          $variance += pow(($i - $average), 2);
                      }
                    $standardevi = (float)sqrt($variance/$num_of_elements);
                    $variances = $variance /$num_of_elements;
            }
                if (empty($standardevi) && $flag != 1) {
                      echo "<p class='err_proc'>Something Went Wrong !</p>".$standardevi;
                  }
              }
          ?>
    <div class="workarea">
<h2><u>Standard deviation, Variance</u></h2>
        <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
            <label for="message">Enter numbers: eg(25,12,15,16,21)</label><br>
            <input type="text" id="value" name="value" value='<?php echo $value?>' required><br>
            <input type="submit" value="Submit">
        </form>
        <form class="response_form">
            <label for="response">Standard Deviation</label><br>
            <input type="text" id="stdresponse" name="stdresponse" value='<?php echo $standardevi?>'><br>
            <label for="response">variance</label><br>
            <input type="text" id="vresponse" name="vresponse" value='<?php echo $variances?>'><br>
        </form>
    </div>
</body>
</html>
