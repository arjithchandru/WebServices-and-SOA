<?php
function generate()
{
$str = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ";
$stw = str_shuffle($str);
$rnd =rand(3,12);
$stw = substr($stw,3,$rnd);
return $stw;
}
?>
