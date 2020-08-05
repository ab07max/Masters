<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="./styles.css">
</head>
<body>

<?php
  include './sidemenu.html';
?>
<div class="main">
  <h1>Address Book</h1>
</div>
<div class="body-content">
<h2>Add Information</h2>
        <form method="post" enctype="multipart/form-data" action="">
            <table>
                <tr>
                    <td>First Name: </td>
                    <td><input type="text" size="25" maxlength="25" name="firstname"></td>
                </tr>
                <tr>
                    <td>Last Name: </td>
                    <td><input type="text" size="25" maxlength="25" name="lastname" required/></td>
                </tr>
                <tr>
                    <td>Phone Number: </td>
                    <td><input type="text" size="25" maxlength="25" name="phone" required/></td>
                </tr>
                <tr>
                    <td>Address: </td>
                    <td><textarea name="personal-address" rows="3" cols="25"></textarea></td>
                </tr>
                </table><br/>
                <input type="reset" value="Reset">
                <input type="submit" value="Add" id="add" name="add"><br/>
        </form>
</div>
</body>
</html>

<?php
  include('configuration.php');
  if(isset($_REQUEST['add'])){
      $F_NAME = $_REQUEST["firstname"];
      $L_NAME = $_REQUEST["lastname"];
      $PHONE = $_REQUEST["phone"];
      $address = explode( "\n", $_REQUEST["personal-address"]);
      //var_dump($address);
      $sql="INSERT INTO `AddressBook`(`F_NAME`, `L_NAME`, `ADDRESS_LINE_1`, `ADDRESS_LINE_2`, `ADDRESS_LINE_3`, `Phone_number`) VALUES ('$F_NAME','$L_NAME', '$address[0]', '$address[1]', '$address[2]', '$PHONE')";
      mysqli_query($con,$sql);
?>
      <script>
        alert("Successfully added to databases!");
        window.location="index.php";
      </script>	
<?php		
  }
?>