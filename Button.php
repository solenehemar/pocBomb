<html>
<body>

<?php
$command = escapeshellcmd('python ButtonTape.py');
$output = shell_exec($command);
echo $output
?>


<form action="/ButtonTape.php" method="GET">
  <input type="hidden" name="act" value="run">
  <input type="submit" value="Play !">
</form>

</body>
</html>
