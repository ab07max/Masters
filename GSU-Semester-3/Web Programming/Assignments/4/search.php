<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="./styles.css">
</head>
<body>

<?php
  include './sidemenu.html';
  include './configuration.php';
?>
<div class="main">
  <h1>Address Book</h1>
</div>
<div class="body-content"><br/><br/>

<form method="post" enctype="multipart/form-data" action="">
<input type="text" placeholder="Enter the search text" id="search-text" name="search-text" required/><br/><br/>

<input type="submit" value="Search by First Name" id="byFName" name="byFName">
<input type="submit" value="Search by Last Name" id="byLName" name="byLName">
<input type="submit" value="Search by Phone Number" id="byPhone" name="byPhone"><br/>
</form>
</div>
<?php
    $searchItem = $_POST['search-text'];
    if($searchItem) {
        $whereClause = " WHERE ";
        if(isset($_POST['byFName'])) {
            $whereClause .= "F_NAME='";
        }
        if(isset($_POST['byLName'])) {
            $whereClause .= "L_NAME='";
        }
        if(isset($_POST['byPhone'])) {
            $whereClause .= "Phone_number='";
        }
        $sql = "SELECT * FROM AddressBook" . $whereClause . $searchItem . "'";
        // var_dump($sql);
        $query = mysqli_query($con,$sql);
        $row = mysqli_fetch_array($query, MYSQLI_ASSOC);
        if($row)
            header("Location: details.php?id=".$row['AddressID']);
        else {
?>
        <script>
            window.alert("No record with given search text exists!");
        </script>
<?php    
        }
    }    
?>
</body>
</html>
