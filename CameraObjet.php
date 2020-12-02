<?php
$command = escapeshellcmd('python3 cameratest.py --prototxt MobileNetSSD_deploy.prototxt --model MobileNetSSD_deploy.caffemodel --confidence 0.9');
$output = shell_exec($command);

if ($command==1){
echo "gagné";
}
else{
echo "perdu";
}
?>
