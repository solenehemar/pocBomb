<?php
session_start();
$command = escapeshellcmd('python3 cameratest.py --prototxt MobileNetSSD_deploy.prototxt --model MobileNetSSD_deploy.caffemodel --confidence 0.9');
$output = shell_exec($command);


if ($output==1){
echo "winner";
?>

<form action="/POCwebpage.html" method="GET">
  <input type="hidden" name="go" value="run">
  <input type="submit" value="Menu">
</form>
<?php
}

else{
echo "loser\n";
$_SESSION['livesWebcam']=$_SESSION['livesWebcam']-1;

if ($_SESSION['livesWebcam']<=0) {
echo "you have no more life for this bomb";
?>
<form action="/POCwebpage.html" method="GET">
  <input type="hidden" name="go" value="run">
  <input type="submit" value="Menu">
</form>
<?php
session_destroy();
}


else{
echo "you have ".$_SESSION['livesWebcam']." lives left";
?>

<form action="/Webcam.php" method="GET">
  <input type="hidden" name="ouch" value="run">
  <input type="submit" value="Try again !">
</form>

<form action="/POCwebpage.html" method="GET">
  <input type="hidden" name="go" value="run">
  <input type="submit" value="Menu">
</form>

<?php
}
}
