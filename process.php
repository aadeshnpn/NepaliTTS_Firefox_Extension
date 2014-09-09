<?php 
header('Content-Type: text/html; charset=utf-8');
#echo "Hello World";
if(isset($_GET['q']))
{
	$data=$_GET['q'];
	$data=trim($data);
	$date=stripslashes($data);
	$data=htmlspecialchars($data);
}

//The Client
#echo $data;
error_reporting(E_ALL);

$helo="HELO";
$port="4444";
$address="192.168.1.14";
$fname="FNAME ".$_GET['fname'];
#echo $fname;
#echo $ttsdata;
$ttsdata="DATA ".$data;
$quit="QUIT";
$dot=".";
/* Create a TCP/IP socket. */
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket === false) {
    echo "socket_create() failed: reason: " . socket_strerror(socket_last_error()) . "</br>";
} else {
    #echo "socket successfully created.</br>";
}

#echo "Attempting to connect to '$address' on port '$port'...";
$result = socket_connect($socket, $address, $port);
if ($result === false) {
    echo "socket_connect() failed.\nReason: ($result) " . socket_strerror(socket_last_error($socket)) . "</br>";
} else {
    #echo "successfully connected to $address.</br>";

    #echo "Sending $helo to server.</br>";
    socket_write($socket, $helo, strlen($helo));
  
    $output1 = socket_read($socket, 2048);
    #echo "Response from server is: $output1\n";
    //sleep(2);
    
    #echo "Sending $fname to server.\n";
    socket_write($socket, $fname, strlen($fname));
   
    $output2 = socket_read($socket, 2048);
    #echo "Response from server is: $output2\n";
    //sleep(2);

    #echo "Sending $ttsdata to server.\n";
    socket_write($socket, $ttsdata, strlen($ttsdata));
    
    $output3 = socket_read($socket, 2048);
    #echo "Response from server is: $output3\n";
    //sleep(2);
	
    #echo "Closing Connection to server to server.\n";
    #socket_write($socket, $dot,strlen($dot));
    socket_write($socket, $quit,strlen($quit));

    $output6=socket_read($socket,2048);
    #echo "Response from server is: $output6\n";
    //sleep(2);
	}


#echo "Closing socket...";
socket_close($socket);
echo "http://192.168.1.14/test/dewplayer-multi.swf?mp3=http://192.168.1.14/tts/wav/".$_GET['fname'].".mp3&autoplay=1";

?>