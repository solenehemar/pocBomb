<?php
session_start();

if(!isset($_SESSION['livesMorse'])){
$_SESSION['livesMorse']=3;
}

$command = escapeshellcmd('python Morse.py');
$output = shell_exec($command);
?>


<form action="/MorseTest.php" method="GET">
  <div>
    <label for="freq">What is the frequence ?</label>
    <input name="freq" id="freq" value="0">
  </div>
  <div>
    <input name="response" id="response" value=<?php echo $output;?> type = "hidden">
  </div>
  <div>
    <button>Send value</button>
  </div>
</form>