<?php
$command = escapeshellcmd('python Button.py');
$output = shell_exec($command);

if ($output==1){
echo "gagné";
}
else{
echo "perdu";
}
?>
