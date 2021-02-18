<!DOCTYPE html>
<html>
<head>
    <title>LZW</title>
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

      $compressedval = "";
      $decompressedval="";
      $inpval = "";

      class LZW
{
    function compress($unc) {
        $i;$c;$wc;
        $w = "";
        $dictionary = array();
        $result = array();
        $dictSize = 256;
        for ($i = 0; $i < 256; $i += 1) {
            $dictionary[chr($i)] = $i;
        }
        for ($i = 0; $i < strlen($unc); $i++) {
            $c = $unc[$i];
            $wc = $w.$c;
            if (array_key_exists($w.$c, $dictionary)) {
                $w = $w.$c;
            } else {
                array_push($result,$dictionary[$w]);
                $dictionary[$wc] = $dictSize++;
                $w = (string)$c;
            }
        }
        if ($w !== "") {
            array_push($result,$dictionary[$w]);
        }
        return implode(",",$result);
    }

    function decompress($com) {
        $com = explode(",",$com);
        $i;$w;$k;$result;
        $dictionary = array();
        $entry = "";
        $dictSize = 256;
        for ($i = 0; $i < 256; $i++) {
            $dictionary[$i] = chr($i);
        }
        $w = chr($com[0]);
        $result = $w;
        for ($i = 1; $i < count($com);$i++) {
            $k = $com[$i];
            if ($dictionary[$k]) {
                $entry = $dictionary[$k];
            } else {
                if ($k === $dictSize) {
                    $entry = $w.$w[0];
                } else {
                    return null;
                }
            }
            $result .= $entry;
            $dictionary[$dictSize++] = $w . $entry[0];
            $w = $entry;
        }
        return $result;
    }
}
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $msg = $_POST['value'];
    $inpval = $msg;
    $lzw = new LZW();
    $com = $lzw->compress($msg);
    $dec = $lzw->decompress($com);
    $list = array();
    array_push($list,$com);

    $Obj = new \stdClass();
    $Obj->Compressed = $list;
    array_push($list,$dec);
    $Objs = new \stdClass();
    $params = array();
    array_push($params, $msg);
    $Objs->decompressed = $params;

    $compressedval = json_encode($Obj);
    $decompressedval = json_encode($Objs);
}

      ?>
  <div class="workarea">
  <h2><u>LZW</u></h2>
  <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
  <label for="message">Enter text:</label><br>
  <input type="text" id="value" name="value" required><br>
  <input type="submit" value="Submit">
  </form>
  <form class="response_form">
  <label for="response">Input</label><br>
  <input type="text" id="sresponse" name="sresponse" value='<?php echo $inpval?>'><br>
  <label for="response">Compressed</label><br>
  <input type="text" id="sresponse" name="sresponse" value='<?php echo $compressedval?>'><br>
  <label for="response">De-compressed</label><br>
  <input type="text" id="sresponse" name="sresponse" value='<?php echo $decompressedval?>'><br>
  </form>
  </div>
  </body>
  </html>
