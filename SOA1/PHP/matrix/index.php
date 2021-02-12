<!DOCTYPE html>
    <html>
    <head>
    <title>Matrix Operations</title>
    <style>
    body {
      background-color: #4db8ff;
      text-align: center;
      color: white;
      font-family: Arial, Helvetica, sans-serif;
    }
    span {
      color : white;
        font-style: oblique;
    }
    .info {
      background-color : #0099ff;
        padding : 20px;
        margin: -10px -10px 0 -10px;
    }
    .api_proc {
      background-color: #6600cc;
        padding:7px;
        border-radius:20px;
    }
    .err_proc {
            background-color: red;
            padding: 7px;
            border-radius: 20px;
   }
    .workarea {
    text-align : left;
    padding : 50px;
    }

    input[type=text] {
      width:150%;
      padding: 12px 20px;
      margin: 8px 0;
      display: inline-block;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;

    }
    input[type=submit] {
      width: 40%;
      background-color:   #00b359;
      color: white;
      padding: 10px 20px;
      margin: 8px 0;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size:17px;
    }

    input[type=submit]:hover {
      background-color: #00994d;
    }
    .response_form {
      padding-top:50px;
    }
    </style>
    </head>
    <body>
      <?php
      $op = 0; $row = 3; $col = 5; $opName = ""; $result = ""; $strMat = "1,2,3,4,5,6,7,8,9,0,11,12,13,14,15";

      function transpose($row,$col,$matrixA){

        $tMatrix = array();
        foreach($matrixA as $idx=>$drow){
          foreach($drow as $idxv => $val){
              $tMatrix[$idxv][] = $val;
          }
        }
        $tmpArr = array();
        foreach ($tMatrix as $arr) {
        $tmpArr[] = implode(',', $arr);
        }
        return 'Transpose => '.implode(',',$tmpArr);

      }

    function lowerDiagonal($row,$col, $matrixA){
      $rtempMat = array(); $ltempMat = array(); $lMatrix = array(); $rMatrix = array();

      for($i=0;$i<$row;$i++){
        for($j=0;$j<$col;$j++){
          if ($j < $i){
            array_push($ltempMat,$matrixA[$i][$j]);
          }
          else{
            array_push($ltempMat, 0);
          }

          if (($j >= 1) && ($i + $j > $col - 1)){
            array_push($rtempMat,$matrixA[$i][$j]);
          }

          else{
            array_push($rtempMat,0);
          }
        }
        array_push($rMatrix,$rtempMat);
        array_push($lMatrix,$ltempMat);
        $rtempMat = array(); $ltempMat = array();
      }
      $tmpArr = array();
      foreach ($lMatrix as $arr) {
      $tmpArr[] = implode(',', $arr);
      }
      $tmpArr2 = array();
      foreach ($rMatrix as $arr) {
      $tmpArr2[] = implode(',', $arr);
      }
      return "LowerLeft => ".implode(",",$tmpArr)." | Lower_Right => ".implode(", ",$tmpArr2);
    }

    function upperDiagonal($row,$col, $matrixA){
      $rtempMat = array(); $ltempMat = array(); $lMatrix = array(); $rMatrix = array();

      for($i=0;$i<$row;$i++){
        for($j=0;$j<$col;$j++){
          if ($j > $i){
            array_push($ltempMat,$matrixA[$i][$j]);
          }
          else{
            array_push($ltempMat, 0);
          }

          if (($j <= 1) && ($i + $j < $col - 1)){
            array_push($rtempMat,$matrixA[$i][$j]);
          }

          else{
            array_push($rtempMat,0);
          }
        }
        array_push($rMatrix,$rtempMat);
        array_push($lMatrix,$ltempMat);
        $rtempMat = array(); $ltempMat = array();
      }
      $tmpArr = array();
      foreach ($lMatrix as $arr) {
      $tmpArr[] = implode(',', $arr);
      }
      $tmpArr2 = array();
      foreach ($rMatrix as $arr) {
      $tmpArr2[] = implode(',', $arr);
      }
      return "UpperLeft => ".implode(", ",$tmpArr)." | UpperRight => ".implode(", ",$tmpArr2);
    }




      if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $op = $_POST['op']; $row = $_POST['row']; $col = $_POST['col']; $strMat = $_POST['matrix'];

        if(empty($op) || empty($row) || empty($col) || empty($strMat)){

          echo "<p class='err_proc'>Invalid Inputs</p>";
        }
        $tempMat = array(); $matrixA = array(); $colBkp = $col;

        $strMat = explode(",",$strMat);
        foreach($strMat as $idx=>$key){
          if($idx < $col){
            array_push($tempMat,$key);
          }
          else{
            array_push($matrixA,$tempMat);
            $tempMat = array();
            $col += $colBkp;
            array_push($tempMat,$key);
          }
          array_push($matrixA,$tempMat);
        }
        $col = $colBkp;

        if($op == 0){
          $result  = transpose($row, $col, $matrixA);
        }elseif($op == 1){
          $result  = upperDiagonal($row, $col, $matrixA);
        }elseif($op == 2){
          $result  = lowerDiagonal($row, $col, $matrixA);
        }else{
          echo "<p class='err_proc'>Invalid Operation</p>";
        }
        $strMat = implode(",",$strMat);
      }
      ?>



    <div class="info">
    <h1>Matrix Operations</h1>
    <p>API Usage : Returns the result of given matrix and operation</p>
    <p class="api_proc">API Call Format : <span>http://localhost:5000/matops?op=0&row=3&col=5&matrix=1,2,3,4,5,6,7,8,9,0,1,2,3,4,5</span></p>
    </div>
    <div class="workarea">

    <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
        <label for="op">Operation </br> (0 - Transpose, 1 - Upper Diagonal Left & Right, 2 - Lower Diagonal Left & Right, 3 - Swivel)</label><br>
        <input type="text" id="op" name="op" value='<?php echo $op?>'><br>
        <label for="row">Rows</label><br>
        <input type="text" id="row" name="row" value='<?php echo $row?>'><br>
        <label for="col">Columns</label><br>
        <input type="text" id="col" name="col" value='<?php echo $col?>'><br>
        <label for="matrix">Matrix </br>(Comma seperated values. Ex. 1,2,3,4,5,6,7,8,9,0,1,2,3,4,5)</label><br>
        <textarea type="text" id="matrix" name="matrix" rows="4" cols="50" ><?php echo $strMat?></textarea>
        <br>
        <input type="submit" value="Submit">
      </form>
      <form class="response_form">
        <label for="response">Result of <?php echo $opName?></label><br>
        <textarea id="response" name="response" rows="4" cols="50" > <?php echo $result?></textarea>
      </form>
    </div>

    </body>
    </html>
