<html>
<body>

<?php
if ($_GET['freq']==$_GET['response']){
echo "gagné";

<form action="/POCwebpage.html" method="GET">
  <input type="hidden" name="act" value="run">
  <input type="submit" value="Menu">
</form>

}
else{
echo "perdu";

<form action="/Morse.php" method="GET">
  <input type="hidden" name="act" value="run">
  <input type="submit" value="Try again !">
</form>

<form action="/POCwebpage.html" method="GET">
  <input type="hidden" name="act" value="run">
  <input type="submit" value="Menu">
</form>
}


<body>
<html>


