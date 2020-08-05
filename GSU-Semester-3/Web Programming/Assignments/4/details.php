<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="./styles.css">
</head>
<?php
    include './sidemenu.html';
?>
<body>
<div class="main">
  <h1>Address Book</h1>
</div>
<div class="body-content"><br/><br/>
<table>
    <tr>
    <th>AddressID</th>
    <th>FIRST NAME</th>
    <th>LAST NAME</th>
    <th>ADDRESS_1</th>
    <th>ADDRESS_2</th>
    <th>ADDRESS_3</th>
    <th>PHONE</th>
    </tr>
<?php
    include './configuration.php';
    $addressID = $_GET['id'];
    if(!empty($addressID)) {
        $sql = "SELECT * FROM AddressBook WHERE AddressID = " . $addressID;
        $query = mysqli_query($con,$sql);
        //var_dump($sql);
        while($row = mysqli_fetch_array($query,MYSQLI_ASSOC)) {
            echo "<tr>";
            echo "<td>" . $row['AddressID'] . "</td>";
            echo "<td>" . $row['F_NAME'] . "</td>";
            echo "<td>" . $row['L_NAME'] . "</td>";
            echo "<td>" . $row['ADDRESS_LINE_1'] . "</td>";
            echo "<td>" . $row['ADDRESS_LINE_2'] . "</td>";
            echo "<td>" . $row['ADDRESS_LINE_3'] . "</td>";
            echo "<td>" . $row['Phone_number'] . "</td>";
            echo "</tr>";
        }
    }
?>
</div>
</body>
</html>