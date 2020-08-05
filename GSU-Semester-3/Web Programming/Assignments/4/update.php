<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="./styles.css">
</head>
<body>

<?php
  include './sidemenu.html';
    include('configuration.php');
    $addressID = $_GET['id'];
    if(!empty($addressID)) {
        $sql = "SELECT * FROM AddressBook WHERE AddressID = " . $addressID;
        $query = mysqli_query($con,$sql);
        $row = mysqli_fetch_array($query,MYSQLI_ASSOC);
        // var_dump($row);
    }
?>
<div class="main">
  <h1>Address Book</h1>
</div>
<div class="body-content">
<h2>Personal Information</h2>
        <form method="post" enctype="multipart/form-data" action="">
            <table>
                <tr>
                    <td>First Name: </td>
                    <td><input type="text" size="25" maxlength="25" name="firstname" value="<?php echo $row['F_NAME']?>"></td>
                </tr>
                <tr>
                    <td>Last Name: </td>
                    <td><input type="text" size="25" maxlength="25" name="lastname" value="<?php echo $row['L_NAME']?>"></td>
                </tr>
                <tr>
                    <td>Phone Number: </td>
                    <td><input type="text" size="25" maxlength="25" name="phone" value="<?php echo $row['Phone_number']?>"></td>
                </tr>
                <tr>
                    <td>Address: </td>
                    <td><textarea name="personal-address" rows="3" cols="25"><?php echo $row['ADDRESS_LINE_1']. "\n" . 
                    $row['ADDRESS_LINE_2']. "\n" . $row['ADDRESS_LINE_3']?></textarea></td>
                </tr>
                </table><br/>
                <input type="submit" value="Update" id="update" name="update"><br/>
        </form>
</div>
</body>
</html>

<?php
  
  if(isset($_REQUEST['update'])){
      $F_NAME = $_REQUEST["firstname"];
      $L_NAME = $_REQUEST["lastname"];
      $PHONE = $_REQUEST["phone"];
      $address = explode( "\n", $_REQUEST["personal-address"]);
      //var_dump($address);
      $sql="UPDATE `AddressBook` SET `F_NAME` = '$F_NAME', `L_NAME` = '$L_NAME', `ADDRESS_LINE_1` = '$address[0]', `ADDRESS_LINE_2` = '$address[1]', `ADDRESS_LINE_3` = '$address[2]', `Phone_number` = '$PHONE' WHERE `AddressID` = $addressID";
      //var_dump($sql);
      if(mysqli_query($con,$sql)) {
?>
      <script>
        alert("Successfully updated the databases!");
        window.location="index.php";
      </script>	
<?php		
      }
  }
?>