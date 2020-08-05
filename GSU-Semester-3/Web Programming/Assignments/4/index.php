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
<div class="body-content"><br/><br/>
<?php
  include './view.php';
?>
<input type="submit" value="add" onClick="window.location.href='add.php';"><br/>
</div>
</body>
</html>
