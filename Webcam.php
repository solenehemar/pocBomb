<?php
session_start();

if(!isset($_SESSION['livesWebcam'])){
$_SESSION['livesWebcam']=3;
}

$command = escapeshellcmd('python cameraAffiche.py');
$output = shell_exec($command);
echo $output
?>


<form action="/CameraObjet.php" method="GET">
  <input type="hidden" name="act" value="run">
  <input type="submit" value="Play !">
</form>