<?php
    date_default_timezone_set("America/New_York");
    if(isset($_POST['details'])) {
        $hours = $_POST['hours'];
        $today=date("l Y-m-d h:i:sa");
        // echo "Created date is " . $d;
        
        echo "<table border='1' class='container'>";
        echo "<tr>
            <th colspan=4 class='table_header' id='today'>" . $today . "</th>
        </tr>
        <tr>
            <th>Time</th>
            <th>User1</th>
            <th>User2</th>
            <th>User3</th>
        </tr>
        ";
        $minutes = "00";
        $hour = date('h', strtotime("now"));
        $meridian = date('A', strtotime("now"));
        $count = 0;
        $even_row = 'background-color:#86cefd;';
        $odd_row = 'background-color:#BCE4FE;';
        $row = 1;
        for($i = 0; $i <= $hours * 2; $i++) {
            $background = $row % 2 == 0 ? $even_row : $odd_row;
            echo "<tr style='height:40px;".$background."'>";
            echo "<td class='hr_td'>". $hour . ":" . $minutes . " " . $meridian . "</td>";
            if($minutes == "00")
                $minutes = "30";
            else {
                $minutes = "00";
                $hour ++;
            }
            if ($hour == 12 && $minutes == "00") {
                $meridian = $meridian == "AM" ? "PM" : "AM";
            }
            elseif ($hour > 12) {
                $hour = 1;
            }
            echo "<td></td><td></td><td></td>";
            echo "</tr>";
            $row++;
        }
        echo "</table>";
    }
?>


<!DOCTYPE html>
<html>
    <head>
        <metacharset="UTF-8">
        <title>
            Assignment - 3 Bonus
        </title>
        <link rel="stylesheet" type="text/css" href="calendar.css">
    </head>
    <body style="text-align: center;">
        <h1>Assignment - 3 Bonus</h1><br/>
        <form method="post" enctype="multipart/form-data" action="calendar.php">
            <label for="hours">Hours to Show:</label>
            <input type="text" id="hours" name="hours"><br><br>
            <input type="submit" value="Submit" id="details" name="details">
        </form>
    </body>
</html>    