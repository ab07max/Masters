<?php
 
if($_GET){
 
	$n = $i = $_GET['stars'];
 
	while ($i--){
		echo str_repeat('*', $n - $i)."<br>";
	}
}
?>
<html>
	<head></head>
	<body>
		<form>
			Enter number of lines: <input type="text" name="stars" />
		</form>
	</body>
</html>