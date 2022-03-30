<?php

$uri_post = $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];


$val = ':9091/saldos_services.php';

//$val = ':8080/homebanking/validalogin.jsp';

$hostname = php_uname('n');
//echo "href: " . $val;

if (strpos($uri_post, $val) !== false){
    //echo "if 1<br>";

   if ($_SERVER['REQUEST_METHOD'] == 'POST') //($_SERVER['REQUEST_METHOD'] == 'GET')
      {
      $op = $_POST['op'];
      //echo "post POST saldos<br>";
      //echo "op: ". $op;
      //echo "if 2<br>";


      if (strpos($op, "home_saldos") !== false) {
          //echo "if 3<br>";
          //echo "post POST saldos<br>";
          $user_id = $_POST['user_id'];
          //$pass = $_POST['user_password'];
          //$type = $_POST['type'];

          //$user_id = '13352626-9';
          //$pass = '123456';
          //$type = 'login';

          $url = "http://python-saldos-services:9091/home_saldos";

          $data = array('user_id'      => $user_id );

          $options = array(
              'http' => array(
                  'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
                  'method'  => 'POST',
                  'content' => http_build_query($data)
              )
          );
          $context  = stream_context_create($options);
          $result = file_get_contents($url, false, $context);
          if ($result === FALSE) { /* Handle error */ }

          /*$fields = [
            'user_id'      => $user_id
          ];

          $fields_string = http_build_query($fields);

          $ch = curl_init();
         curl_setopt($ch,CURLOPT_URL, $url);
          curl_setopt($ch,CURLOPT_POST, true);
          curl_setopt($ch,CURLOPT_POSTFIELDS, $fields_string);
          curl_setopt($ch, CURLOPT_FAILONERROR, true);
          curl_setopt($ch,CURLOPT_RETURNTRANSFER, true);
          curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);

          $result = curl_exec($ch);
          $error =  curl_error($ch);
          $http_status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
          */

          header("HTTP/1.1 200 OK");
          //echo json_encode($result);
          echo $result;
          //echo "error:" .$error . "code status: " .$http_status;
          exit();
       }
       if (strpos($op, "mov_saldos") !== false) {
          $user_id = $_POST['user_id'];
          //$pass = $_POST['user_password'];
          //$type = $_POST['type'];

          //$user_id = '13352626-9';
          //$pass = '123456';
          //$type = 'login';

          $url = "http://python-saldos-services:9091/mov_saldos";

          $data = array('user_id'      => $user_id );

          $options = array(
              'http' => array(
                  'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
                  'method'  => 'POST',
                  'content' => http_build_query($data)
              )
          );
          $context  = stream_context_create($options);
          $result = file_get_contents($url, false, $context);
          if ($result === FALSE) { /* Handle error */ }

          header("HTTP/1.1 200 OK");
          //echo json_encode($result);
          echo $result;
          //echo "error:" .$error . "code status: " .$http_status;
          exit();
       }
   }
}else{
    echo "href invalidax - >uri_post: ". $uri_post ."  ". $val ;
    exit();
}


