<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="./styles.css">

</head>

<?php
  //include './sidemenu.html';
  include('configuration.php');
  $sql = "SELECT * FROM AddressBook";
  $query = mysqli_query($con,$sql);
  $count = mysqli_num_rows($query);
  if($count == 0){
?>	
<script>
  alert("Not Enough Data in the database!");
  window.location="index.php";
</script>	
<?php
      die();
  }
?>


<body>
  <table>
    <tr>
    <th>ID</th>
    <th>NAME</th>
    <th>OPERATION</th>
    </tr>
    <?php
        while($row = mysqli_fetch_array($query,MYSQLI_ASSOC)) {
            echo "<tr>";
            echo "<td>".$row['AddressID']."</td>";
            echo "<td>".$row['F_NAME']."</td>";
            echo "<td><input type='button' value='View' name ='btnView' onclick=\"window.location.href='details.php?id=". $row['AddressID']."'\"/> 
            <input type='button' value='Update' name ='btnUpdate' onclick=\"window.location.href='update.php?id=". $row['AddressID']."'\"/>
            <input type='button' value='Delete' name ='btnDelete' onClick=\"IsDelete(this, '".$row['AddressID']."')\"/></td>";
            echo "</tr>";
        }
    ?>
  </table>
      </body>
</html>

<script>
    function IsDelete(element,id)
    {//（true or false）
        if(confirm("Do you want to delete this record？"))
        {//
            location.href="./delete.php?id="+id;
        }
    }
</script>