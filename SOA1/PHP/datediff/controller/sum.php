<?php
function tum($t1,$t2)
{
    $time1 = explode(':',$t1);
    $time2 = explode(':',$t2);

    if ($time2[2] >= $time1[2]){
    $r[2] = $time2[2] - $time1[2];
  }
else{
    $r[2] = ($time2[2] + 60) - $time1[2];
    $time2[1] -= 1;
}
if ($time2[1] >= $time1[1]){
    $r[1] = $time2[1] - $time1[1];
  }
else{
    $r[1] = ($time2[1] + 60) - $time1[1];
    $time2[0] -= 1;
}
if ($time2[0] >= $time1[0]){
    $r[0] = $time2[0] - $time1[0];
  }
else{
    $r[0] = ($time2[0] + 24) - $time1[0];
    // $date2 -= 1;
}
  $str = implode(':', $r);
  return $str;
}
function sum($d1,$d2,$t1,$t2)
{
  $date1=$d1;
  $date2=$d2;
  $d1=explode('-',$date1);
  $d2=explode('-',$date2);
  $time1 = explode(':',$t1);
  $time2 = explode(':',$t2);
$diff = abs(strtotime($date2) - strtotime($date1));
$years = floor($diff / (365*60*60*24));
$months = floor(($diff - $years * 365*60*60*24) / (30*60*60*24));
$days = floor(($diff - $years * 365*60*60*24 - $months*30*60*60*24)/ (60*60*24));

if ($time2[2] >= $time1[2]){
$r[2] = $time2[2] - $time1[2];
}
else{
$r[2] = ($time2[2] + 60) - $time1[2];
$time2[1] -= 1;
}
if ($time2[1] >= $time1[1]){
$r[1] = $time2[1] - $time1[1];
}
else{
$r[1] = ($time2[1] + 60) - $time1[1];
$time2[0] -= 1;
}
if ($time2[0] >= $time1[0]){
$r[0] = $time2[0] - $time1[0];
}
else{
$r[0] = ($time2[0] + 24) - $time1[0];
$days -= 1;
}
    $t[0]=$days;
    $t[1]=$months;
    $t[2]=$years;
    for($i=0;$i<3;$i++)
     $t[$i];
    return json_encode($t);
}
?>
