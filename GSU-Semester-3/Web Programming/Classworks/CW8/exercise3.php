<?php

function word_count($input) {
    $inputLength = strlen($input);
    $words = 0;
    for($i = 0; $i < $inputLength; $i++)
        if($input[$i] == ' ') 
            $words ++;
    echo "word count: ", $words + 1;
}
 
if($_GET){
 
	$words = $_GET['words'];
    word_count($words);
    
}
?>
<html>
	<head></head>
	<body>
		<form>
			Enter your input: <input type="text" name="words" />
		</form>
	</body>
</html>