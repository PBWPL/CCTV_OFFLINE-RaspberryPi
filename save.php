<?php
file_put_contents('settings.txt',[$_POST['time']]);
header("Location: index.php")
?>