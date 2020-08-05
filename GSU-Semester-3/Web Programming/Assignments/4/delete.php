<?php
    include './configuration.php';
    $addressID = $_GET['id'];
    if(!empty($addressID)) {
        $sql = "DELETE FROM AddressBook WHERE AddressID = " . $addressID;
        $query = mysqli_query($con,$sql);
        //var_dump($sql);
        if ($query) {
?>
        <script>
            alert("Successfully deleted from database!");
            window.location="index.php";
        </script>	
<?php		
        } 
        else {
            ?>
            <script>
                alert("Delete Failed!");
                window.location="index.php";
            </script>	
    <?php
        }
    }
?>