<?php
    if(isset($_POST['details'])) {
        echo $_POST['personal-name'];
        echo $_POST['personal-age'];
        echo $_POST['personal-education'];
        echo $_POST['personal-email'];
        echo $_POST['personal-phone'];
        echo $_POST['personal-address'];
    }
?>

<html lang="en">
    <head>
        <title>
            CW8 - E5
        </title>
        <style></style>
    </head>
    <body>
        <h2>Personal Information</h2>
        <form method="post" enctype="multipart/form-data" action="exercise5.php">
            <h4>Contact details</h4>
            <table>

                <tr>
                    <td>Name: </td>
                    <td><input type="text" size="40" maxlength="35" name="personal-name"></td>
                </tr>

                <tr>
                    <td>Age: </td>
                    <td><input type="text" size="10" maxlength="10" name="personal-age"></td>
                </tr>

                <tr>
                    <td>Education: </td>
                    <td><textarea name="personal-education" rows="3" cols="25"></textarea></td>
                </tr>

                <tr>
                    <td>Contact Email: </td>
                    <td><input type="text" size="40" maxlength="40" name="personal-email"></td>
                </tr>

                <tr>
                    <td>Contact Phone: </td>
                    <td><input type="text" size="40" maxlength="40" name="personal-phone"></td>
                </tr>

                <tr>
                    <td>Address: </td>
                    <td><textarea name="personal-address" rows="3" cols="25"></textarea></td>
                </tr>

            </table><br/>
            <input type="reset" value="Reset">
            <input type="submit" value="Submit" id="details" name="details">
        </form>
    </body>
</html>
