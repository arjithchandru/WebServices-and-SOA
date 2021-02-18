<!DOCTYPE html>
<html>
<head>
    <title>Huffman Coding</title>
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
      $value="";
      $decompressedval="";
      $inpval = "";

      $global_node_res=array();
    class node {
      public $freq;
      public $char;
      public $left;
      public $right;
      public $huff;
      function set_val($freq,$char,$left,$right) {
        $this->freq = $freq;
        $this->char = $char;
        $this->left = $left;
        $this->right = $right;
        $this->huff = "";
      }
      function get_freq() {
        return $this->freq;
      }
      function get_char() {
        return $this->char;
      }
      function get_huff() {
        return $this->huff;
      }
      function get_left() {
        return $this->left;
      }
      function get_right() {
        return $this->right;
      }
    }

      if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $msg = $_POST['value'];
        $inpval = $msg;
        $mg=$msg;
    $freq = array();

    for($i = 0; $i < strlen($msg); $i++) {
        array_push($freq, 1);
        for($j = $i+1; $j <strlen($msg); $j++) {
            if($msg[$i] == $msg[$j]) {
                $freq[$i]++;
                $msg[$j] = '0';
            }
        }
    }
    $h_char=array();
    $h_freq=array();
    for($i = 0; $i < count($freq); $i++) {
        if($msg[$i] != ' ' && $msg[$i] != '0'){
            array_push($h_char, $msg[$i]);
            array_push($h_freq, $freq[$i]);
        }
    }

    $nodes=array();
    for($i = 0; $i < count($h_char); $i++) {
            $Node = new node();
            $Node->set_val($h_freq[$i],$h_char[$i],null,null);
            array_push($nodes,$Node);
    }
    while (count($nodes)>1) {
        usort($nodes,function($first,$second){
            return $first->freq > $second->freq;
        });
        $left = new node();
        $left = $nodes[0];
        $right = new node();
        $right = $nodes[1];
        $left->huff = 0;
        $right->huff = 1;
        $newNode = new node();
        $newNode->set_val($left->get_freq()+$right->get_freq(), $left->get_char().$right->get_char(), $left, $right);
        array_splice($nodes, 0, 2);
        array_push($nodes,$newNode);
    }
    traverse($nodes[0],"");
    $list = array();
    array_push($list,$global_node_res);
    $Obj = new \stdClass();
    $Obj->compressed = $list;

    $Objs = new \stdClass();
    $params = array();
    array_push($params, $mg);
    $Objs->decompressed = $params;


    $compressedval = json_encode($Obj);
    $decompressedval = json_encode($Objs);

}

function traverse($node,$val){
    global $global_node_res;
    $newVal = $val . (string)($node->get_huff());
    if($node->get_left()){
        traverse($node->get_left(), $newVal);
    }
    if($node->get_right()){
        traverse($node->get_right(), $newVal);
    }
    if($node->get_left()==null && $node->get_right()==null){
        array_push($global_node_res, $node->get_char().":".$newVal." ");
    }
}
      ?>
<div class="workarea">
  <h2><u>Huffman Coding</u></h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
<label for="message">Enter text:</label><br>
<input type="text" id="value" name="value" value='<?php echo $value?>'required><br>
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
