<center>
<img src="indeks.png">

 <h3> Check Point yourself web portal </h3>  


</center>



<html>
<body>
New public web server registration form: <br/> <br/>


<form action="addweb.php" method="get">
Server Name: <input type="text" name="Name">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
IP Address: <input type="text" name="Address"><br/><br/><br/>
<input type="submit" value="Register" >
</form>

<br/> <br/>

<?php

   if( $_GET["Name"] && $_GET["Address"] ) {
      echo "Registering  ". $_GET['Name']. "   ". $_GET['Address']. ":";
	$output = shell_exec('C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\python.exe register.py'. " ". $_GET['Name']. " ". $_GET['Address']. " ".  '2>&1');
	echo $output;

   }
?>


<br/> <br/><br/> <br/>
<h3> Ready to commit changes? Please click <a href=install.php> here  </a> This operation will take some time </h3>




</body>
</html> 