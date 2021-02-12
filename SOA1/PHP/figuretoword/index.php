<!DOCTYPE html>
<html><head>
    <title>FigureToWord</title>
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
        .response_form {
            padding-top: 30px;
        }
    </style>
</head>
<body>
<?php
    $number = "3450";
    $words = "";
    $flag = 0;
    $a = array("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", '30'=>"thirty", '40'=>"forty", '50'=>"fifty", '60'=>"sixty", '70'=>"seventy", '80'=>"eighty", '80'=>"ninety");
    $levels = array(" ", "hundred ", "thousand ", "lakh ", "crore ");
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $number = $numBkp = $_POST['value'];
        if (empty($number)) {
            echo "<p class='err_proc'>Invalid Number</p>";
            $flag = 1;
        }
        else {
            $noOfDigits = strlen($number);
            $digitsLeft = 0;
            $cValue = array();
            if ($noOfDigits > 9)  {
                echo "<p class='err_proc'>value canot be more than 999999999 !</p>";
                $flag = 1;
            }
            else{
               while( $digitsLeft < $noOfDigits){
                $curNum = floor($number % (($digitsLeft == 2) ? 10 : 100));
                $number = floor($number / (($digitsLeft == 2) ? 10 : 100));
                if($curNum){
                    $level = count($cValue);
                    $cValue [] = ($curNum < 20) ? $a[$curNum].' '.$levels[$level] : $a[floor($curNum / 10) * 10].' '.$a[$curNum % 10].' '.$levels[$level];
                }
                else $cValue[] = null;
                $digitsLeft += (($digitsLeft == 2) ? 10 : 100) == 10 ? 1 : 2;
            }
                $words = implode('', array_reverse($cValue));
                $number = $numBkp;
            }
            }
        if (empty($words) && $flag != 1) {
            echo "<p class='err_proc'>Please re-submit !</p>".$words;
        }
    }
?>
<h2><u>Figure to word</u></h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
  <label for="message">Figures</label><br>
  <input type="text" id="value" name="value" value='<?php echo $number?>'><br>
  <input type="submit" value="Submit">
</form>
<form class="response_form">
  <label for="response">Words</label><br>
  <input type="text" id="response" name="response" value='<?php echo $words?>'><br>
</form>
</body>
</html>
