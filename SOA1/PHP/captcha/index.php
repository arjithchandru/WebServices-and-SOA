<!DOCTYPE html>
<html>
<head>
<title>Captcha</title>
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
    $value =  "";$image = "";
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
		$captchaText = $_POST['value'];
		$captchaImage = imagecreatetruecolor(170, 36);
		$background = imagecolorallocate($captchaImage, 245, 245, 237);
		$frontdesign = imagecolorallocate($captchaImage, rand(1, 200), rand(1, 200), rand(1, 200));
		imagefill($captchaImage, 0, 0, $background);
		imagestring($captchaImage, rand(1, 20), rand(1, 20), rand(1, 20), $captchaText, $frontdesign);
		define('Root', dirname(__FILE__));
		$file = Root . $captchaText . '.png';
		imagepng($captchaImage,$file);
        if ($captchaImage) {
        ob_start();
        imagepng($captchaImage);
        $imgData=ob_get_clean();
        $image = '<img src="data:image/png;base64,'.base64_encode($imgData).'" />';
    }
        $value = $captchaText;
        imagedestroy($captchaImage);
	}
?>
<h2><u>Captcha</u></h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
  <label for="message">Captcha Text : </label><br>
  <input type="text" id="value" name="value" value='<?php echo $value?>'><br>
  <input type="submit" value="Submit">
</form>
<form class="response_form">
  <label for="response">Result : </label>
  <?php echo $image?>
</body>
</html>
