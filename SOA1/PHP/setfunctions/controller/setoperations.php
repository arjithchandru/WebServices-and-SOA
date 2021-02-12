<?php
function array_union($x, $y)
   {
      $aray=  array_merge(
            array_intersect($x, $y),
            array_diff($x, $y),
            array_diff($y, $x)
        );
        return $aray;
   }
function intersect_array($x, $y)
     {
       $aray = array_intersect($x, $y);
       return $aray;
     }
Function differce_array($x, $y)
  {
    $aray = array_merge(
      array_diff($x, $y),
      array_diff($y, $x)
    );
    return $aray;
  }
