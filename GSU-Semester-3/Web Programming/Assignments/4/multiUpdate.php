<?php
include './sidemenu.html';
include './configuration.php';

// fetch records
$result = mysqli_query($con, "SELECT * FROM AddressBook") or die("Error: " . mysqli_error($con));

// delete records
if(isset($_POST['chk_id']))
{
    $arr = $_POST['chk_id'];
    foreach ($arr as $id) {
        //mysqli_query($con,"DELETE FROM AddressBook WHERE AddressID = " . $id);
        header("Location: update.php?id=".$id);
    }
}
?>

<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="./styles.css">
</head>
<body>
<div class="main">
  <h1>Address Book</h1>
</div>
<div class="body-content"><br/><br/>
    <form action="" method="post" id="delete_form">
        <table>
            <thead>
                <tr>
                <th></th>
                <th>ID</th>
                <th>First Name</th>
                </tr>
            </thead>
            <tbody>
                <?php while($row = mysqli_fetch_assoc($result)) { ?>
                <tr>
                    <td><input name="chk_id[]" type="radio" value="<?php echo $row['AddressID']; ?>"/></td>
                    <td><?php echo $row['AddressID']; ?></td>
                    <td><?php echo $row['F_NAME']; ?></td>
                </tr>
                <?php } ?>
                </tbody>
            </table>
            <input id="submit" name="submit" type="submit" value="Update" />
            </form>
                </div>
        </div>
    </div>
</div>
</body>
</html>