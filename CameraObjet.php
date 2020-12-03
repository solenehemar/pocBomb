<html>
<body>

<?php
$command = escapeshellcmd('python3 cameratest.py --prototxt MobileNetSSD_deploy.prototxt --model MobileNetSSD_deploy.caffemodel --confidence 0.9');
$output = shell_exec($command);


if ($output==1){
echo "gagné";

<form action="/POCwebpage.html" method="GET">
  <input type="hidden" name="act" value="run">
  <input type="submit" value="Menu">
</form>

}
else{
echo "perdu";

<form action="/Webcam.php" method="GET">
  <input type="hidden" name="act" value="run">
  <input type="submit" value="Try again !">
</form>

<form action="/POCwebpage.html" method="GET">
  <input type="hidden" name="act" value="run">
  <input type="submit" value="Menu">
</form>
}
?>

<body>
<html>
