<?php

$uri_post = $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];


//$val1 = ':9091/indicadores_services.php';
$val2 = '/indicadores_services.php';
$val = ':8080/homebanking/validalogin.jsp';

$hostname = php_uname('n');
//echo "href: " . $val;

if ((strpos($uri_post, $val1) !== false) || (strpos($uri_post, $val2) !== false) ) {
   //echo "login services php<br>";

   if ($_SERVER['REQUEST_METHOD'] == 'GET')
      {
      //echo "post POST<br>";

      $url = "http://python-indicadores-services:9091/indicadores";

      //$data = array('key1' => 'value1', 'key2' => 'value2');

      // use key 'http' even if you send the request to https://...
      $options = array(
         'http' => array(
             'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
             'method'  => 'GET'
         )
      );

      $context  = stream_context_create($options);
      $result = file_get_contents($url, false, $context);
      if ($result === FALSE) { /* Handle error */ }

      //var_dump($result);


      header("HTTP/1.1 200 OK");
      //echo json_encode($result);
      echo $result;
      //echo "error:" .$error . "code status: " .$http_status;

      exit();
    }

}else{
    echo "href invalida - >uri_post: ". $uri_post ."  ". $val ;
    exit();
}

