<?php
    if(isset($_POST['details'])) {
        $color = $_POST["text-color"];
        $font = $_POST["text-font"];
        $weight = $_POST["text-weight"];
        $text = $_POST["text1"];
        $fontProperty="";
        $fontWeight="";
        switch ($font) {
            case 'times':
                $fontProperty = 'Times New Roman';
                break;
            case 'hevel':
                $fontProperty = 'Helvetica';
                break;
            case 'arial':
                $fontProperty = 'Arial';
                break;
        }
        switch ($weight) {
            case 'eight':
                $fontWeight = '8px';
                break;
            case 'ten':
                $fontWeight = '10px';
                break;
            case 'twelve':
                $fontWeight = '12px';
                break;
        }
        echo "<span style='font-family:". $fontProperty ."; color:". $color ."; font-size:". $fontWeight .";'>" . $text . "</span>";
    }
?>


<!DOCTYPE html>
<html>
    <head>
        <metacharset="UTF-8">
        <title>
            Assignment - 3
        </title>
    </head>
    <body style="text-align: center;">
        <h1>Assignment - 3</h1><br/>
        <form method="post" enctype="multipart/form-data" action="index.php">
            <label for="text-color">Choose a color:</label>
            <select name="text-color" id="text-color">
            <option value="red">Red</option>
            <option value="green">Green</option>
            <option value="Blue">Blue</option>
            </select><br/><br/>

            Choose a font:
            <input type="radio" id="times" name="text-font" value="times">
            <label for="times">Times</label>
            <input type="radio" id="hevel" name="text-font" value="hevel">
            <label for="hevel">Hevel</label>
            <input type="radio" id="arial" name="text-font" value="arial">
            <label for="arial">Arial</label><br/><br/>

            <label for="text-weight">Choose a font weight:</label>
            <select name="text-weight" id="text-weight">
            <option value="eight">8px</option>
            <option value="ten">10px</option>
            <option value="twelve">12px</option>
            </select><br/><br/>

            <textarea id="text1" name="text1" rows="4" cols="50"></textarea><br/><br/>

            <input type="reset" value="Reset">
            <input type="submit" value="Submit" id="details" name="details">
        </form>
    </body>
</html>    