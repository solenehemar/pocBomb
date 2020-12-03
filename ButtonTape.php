<html>
<body>

<?php
$command = escapeshellcmd('python Button.py');
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
echo $_SESSION['livesButton']

<form action="/Button.php" method="GET">
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
