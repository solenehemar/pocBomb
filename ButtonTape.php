<?php
session_start();
$command = escapeshellcmd('python Button.py');
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
$_SESSION['livesButton']=$_SESSION['livesButton']-1;

if ($_SESSION['livesButton']<1) {
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
echo "you have ".$_SESSION['livesButton']." lives left";
?>

<form action="/Button.php" method="GET">
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


