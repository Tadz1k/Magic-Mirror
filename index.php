<?php
$servername = "";
$username = "";
$password = "";
$dbname = "";
?>
<html>
	<head>
	<meta charset = "UTF-8"/>
        <title>Żółw</title>
	</head>
	<body>
		<div id="top">
			<header id="header">Nagłówek szablonu</header>
				<form action="" method="GET">
					Notatka 1:
					<input type="text" name="val1" id="val1" accept-charset='UTF-8'></input><select name = "weight1"><option value = "1">1 (low)</option><option value = "2">2 (med)</option><option value = "3">3 (hi)</option></select><br>
					Notatka 2:
					<input type="text" name="val2" id="val2"></input><select name = "weight2"><option value = "1">1 (low)</option><option value = "2">2 (med)</option><option value = "3">3 (hi)</option></select><br>
					Notatka 3:
					<input type="text" name="val3" id="val3"></input><select name = "weight3"><option value = "1">1 (low)</option><option value = "2">2 (med)</option><option value = "3">3 (hi)</option></select><br>
					<input type="submit" name="notatki" value="send"></input>
				</form>
			<footer id="footer">Stopka serwisu</footer>
		</div>
	</body>
</html>

<?php  
if( isset($_GET['notatki']) )
{
	$conn = new mysqli($servername, $username, $password, $dbname);
	$conn->set_charset("utf8");
    $val1 = $_GET['val1'];
    $val2 = $_GET['val2'];
	$val3 = $_GET['val3'];
	$pri1 = $_GET['weight1'];
	$pri2 = $_GET['weight2'];
	$pri3 = $_GET['weight3'];

	$sql = "UPDATE mirror_notes SET note1 = '$val1', note2 = '$val2', note3 = '$val3', priority1 = '$pri1', priority2 = '$pri2', priority3 = '$pri3' WHERE id = 1";
	if($conn -> query($sql) == TRUE)	{
		echo "Gtowe";
	}	else	{
		echo "Błąd." .$conn->error;
	}
	mysqli_close($conn);
	$text = sprintf("data: NOTES");
	$headers = array($text);
	curl_send($headers);
}


function curl_send($headers)	{
	$ch = curl_init('ip:8080');
	curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
	curl_exec($ch);
	curl_close($ch);
}
  
  
?> 
