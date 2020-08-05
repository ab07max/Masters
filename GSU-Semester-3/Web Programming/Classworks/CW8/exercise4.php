<?php

function word_count($input) {
    $input = strtolower(preg_replace("/[^a-zA-Z ]/", "", $input));
    $tok = strtok($input, " \n\t");
    $wordCount = array();
    while ($tok !== false) {
        if (array_key_exists($tok, $wordCount))
            $wordCount[$tok] ++;
        else
            $wordCount[$tok] = 1 ;
        $tok = strtok(" \n\t");
    }
    print_r($wordCount);
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