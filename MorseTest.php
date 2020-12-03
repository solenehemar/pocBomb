<?php
session_start();

if (if ($_GET['freq']==$_GET['response']){
echo "gagné";
?>

<form action="/POCwebpage.html" method="GET">
  <input type="hidden" name="go" value="run">
  <input type="submit" value="Menu">
</form>
<?php
}

elseif (if ($_GET['freq']!=$_GET['response']) && $_SESSION['livesMorse']<=0) {
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
echo "perdu\n";
$_SESSION['livesButton']=$_SESSION['livesMorse']-1;
echo "you have ".$_SESSION['livesMorse']." lives left";
?>

<form action="/Morse.php" method="GET">
  <input type="hidden" name="ouch" value="run">
  <input type="submit" value="Try again !">
</form>

<form action="/POCwebpage.html" method="GET">
  <input type="hidden" name="go" value="run">
  <input type="submit" value="Menu">
</form>

<?php
}