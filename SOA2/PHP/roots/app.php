<!DOCTYPE html>
<html>

<head>
    <title>Roots</title>
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

      // $arr = "";
      // $number = array(2, 3, 5, 6, 7);
      $SQroot = "";
      $CUroot = "";
      $nroot = "";
      $value = "";
      $nvalue = "2";
      $NthRoot="";
      $number="";
      $flag = 0;
      if ($_SERVER["REQUEST_METHOD"] == "POST") {
          $number  = $_POST['value'];
          $input = $number;
          $NthRoot = $_POST['nvalue'];
          $Base = $number;
          if (empty($number)) {
              echo "<p class='err_proc'>Invalid Figure</p>";
              $flag = 1;
          }
          else{
// $SQroot = squareroot($value);
// echo $SQroot;
// $CUroot = NthRoot($Base, $value, $Precision);
                //if the input number is 0 then return 0 as result
                if($input == 0) {
                $SQroot = 0;
                }
                //if the input number is 1 then return 1 as result
                if($input == 1) {
                $SQroot = 1;
                }
                // assigning $input value to a variable $a
                $a = $input;
                $b = 1;
                while($a > $b)
                {
                // calculating the middle number
                $a= ($a + $b)/2;
                // dividing the input number with the middle number
                $b = $input/$a;
                }
                $SQroot = $a;


                $Precision = 101;
                $CNthRoot = 3;

                if ($CNthRoot <  1) return 0;
                if ($Base    <= 0) return 0;
                if ($Base    <  2) return 1;
                $retVal    = 0;
                $guess     = bcdiv($Base, 2, $Precision);
                $continue  = true;
                $step = bcdiv(bcsub($Base, $guess, $Precision), 2, $Precision);
                    while ($continue) {
                        $test = bccomp($Base, bcpow($guess, $CNthRoot, $Precision), $Precision);
                        if ($test == 0) {
                              $continue = false;
                              $retVal   = $guess;
                        }
                        else if ($test > 0) {
                              $step  = bcdiv($step, 2, $Precision);
                              $guess = bcadd($guess, $step, $Precision);
                          }
                        else if ($test < 0) {
                              $guess = bcsub($guess, $step, $Precision);
                          }
                          if (bccomp($step, 0, $Precision) == 0) {
                              $continue = false;
                              $retVal   = $guess;
                          }
                        }
                        $CUroot = $retVal;



                        $Precision = 101;
                        // $CNthRoot = 3;

                        if ($NthRoot <  1) return 0;
                        if ($Base    <= 0) return 0;
                        if ($Base    <  2) return 1;
                        $retVal    = 0;
                        $guess     = bcdiv($Base, 2, $Precision);
                        $continue  = true;
                        $step = bcdiv(bcsub($Base, $guess, $Precision), 2, $Precision);
                            while ($continue) {
                                $test = bccomp($Base, bcpow($guess, $NthRoot, $Precision), $Precision);
                                if ($test == 0) {
                                      $continue = false;
                                      $retVal   = $guess;
                                }
                                else if ($test > 0) {
                                      $step  = bcdiv($step, 2, $Precision);
                                      $guess = bcadd($guess, $step, $Precision);
                                  }
                                else if ($test < 0) {
                                      $guess = bcsub($guess, $step, $Precision);
                                  }
                                  if (bccomp($step, 0, $Precision) == 0) {
                                      $continue = false;
                                      $retVal   = $guess;
                                  }
                                }
                                $nroot = $retVal;
          }



                          if (empty($SQroot) && $flag != 1) {
                                echo "<p class='err_proc'>Something Went Wrong !</p>".$SQroot;
                            }
                        }
                    ?>
              <div class="workarea">
                <h2><u>Square root, Cube root and Nth-root</u></h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
      <label for="message">Enter numbers: eg(25)</label><br>
      <input type="text" id="value" name="value" value='<?php echo $value?>'required><br>
      <label for="message">Nth root: eg(5)</label><br>
      <input type="text" id="nvalue" name="nvalue" value='<?php echo $nvalue?>'><br>
      <input type="submit" value="Submit">
</form>
<form class="response_form">
      <label for="response">Input Value</label><br>
      <input type="text" id="sresponse" name="sresponse" value='<?php echo $number?>'><br>
      <label for="response">Square Root</label><br>
      <input type="text" id="sresponse" name="sresponse" value='<?php echo $SQroot?>'><br>
      <label for="response">Cube Root</label><br>
      <input type="text" id="curesponse" name="curesponse" value='<?php echo $CUroot?>'><br>
      <label for="response">Nth Value</label><br>
      <input type="text" id="nresponse" name="nresponse" value='<?php echo $NthRoot?>'><br>
      <label for="response">Nth Root</label><br>
      <input type="text" id="nresponse" name="nresponse" value='<?php echo $nroot?>'><br>

</form>

</div>
</body>
</html>
