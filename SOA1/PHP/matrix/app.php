<!DOCTYPE html>
    <html>
    <head>
    <title>Matrix Operations</title>
    <style>
    body {

      font-family: Arial, Helvetica, sans-serif;
    }

    .workarea {
    text-align : left;
    padding : 50px;
    }

    input[type=text] {
      width:30%;
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

      $opName = "";
      $result = "";
      $strMat = "1,2,3,4,5,6,7,8,9";

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
        return implode(',',$tmpArr);

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
      return "Lower Left => ".implode(",",$tmpArr)." || Lower Right => ".implode(", ",$tmpArr2);
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
      return "Upper Left".implode(", ",$tmpArr)." || Upper Right => ".implode(", ",$tmpArr2);
    }

      if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $op = $_POST['opChoice']; $row = $_POST['row']; $col = $_POST['col']; $strMat = $_POST['matrix'];

        if(empty($op) || empty($row) || empty($col) || empty($strMat)){

          echo "<p >No empty fields are allowed</p>";
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
          $opName = "Transpose";
        }elseif($op == 1){
          $result  = upperDiagonal($row, $col, $matrixA);
          $opName = "Upper Diagonal";
        }elseif($op == 2){
          $result  = lowerDiagonal($row, $col, $matrixA);
          $opName = "Lower Diagonal";
        }else{
          echo "<p >Invalid Operation</p>";
        }
        $strMat = implode(",",$strMat);
      }
      ?>

    <div class="workarea">

    <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">

<label for="opChoice"> Choose Operation : </label><br>
        <select name="opChoice" id="opChoice">
               <option  value="0" selected='true'>Transpose</option>
               <option value="1">Upper Diagonals</option>
               <option  value="2"> Lower Diagonals</option>
           </select><br>

        <label for="row">Rows</label><br>
        <input type="text" id="row" name="row" ><br>
        <label for="col">Columns</label><br>
        <input type="text" id="col" name="col"><br>
        <label for="matrix">Matrix </label><br>
        <textarea type="text" id="matrix" name="matrix" rows="4" cols="50" ><?php echo $strMat?></textarea>
        <br>
        <input type="submit" value="Submit">
      </form>
      <form class="response_form">

        <label> Operation performed :  <?php echo $opName?> </label><br>
        <textarea id="response" name="response" rows="4" cols="50" > <?php echo $result?></textarea>
      </form>
    </div>

    </body>
    </html>
