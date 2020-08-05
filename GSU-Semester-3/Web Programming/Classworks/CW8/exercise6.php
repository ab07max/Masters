<?php
    if(isset($_POST['details'])) {
        echo "Mail Sent! Check your Inbox.";
        $to = "vbhamidipati1@student.gsu.edu"; //$advisorid
        $subject = "Form Details of EX-5";
        $message = "Name: ". $_POST['personal-name']. "<br/>
        Age: " . $_POST['personal-age'] . "<br/>
        Education: " . $_POST['personal-education'] . "<br/>
        Email: " . $_POST['personal-email'] . "<br/>
        Phone: " . $_POST['personal-phone'] . "<br/>
        Address: " . $_POST['personal-address'];

        // Always set content-type when sending HTML email
        $headers = "MIME-Version: 1.0" . "\r\n";
        $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

        // More headers
        $headers .= 'From: WPSummer@cs.gsu.edu'."\r\n";

        mail($to,$subject,$message,$headers);
    }
?>

<html lang="en">
    <head>
        <title>
            CW8 - E6
        </title>
        <style></style>
    </head>
    <body>
        <h2>Personal Information</h2>
        <form method="post" enctype="multipart/form-data" action="exercise6.php">
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
