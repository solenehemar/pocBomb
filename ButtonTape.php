<?php
$command = escapeshellcmd('python Button.py');
$output = shell_exec($command);

if ($command==1){
echo "gagné";
}
else{
echo "perdu";
}
?>
