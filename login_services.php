<?php
header('Access-Control-Allow-Origin: *');
$uri_post = $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];

$val_ext = 'nginx-services2-homebanking.apps.ocp.tsoftlabs.com/login_services.php';
$val_int = ':8080/login_services.php';

//$val = ':8080/homebanking/validalogin.jsp';

$hostname = php_uname('n');
//echo "href: " . $val;

if (strpos($uri_post, $val_int) !== false || strpos($uri_post, $val_ext) !== false) {
   //echo "login services php<br>";

   if ($_SERVER['REQUEST_METHOD'] == 'POST')
      {
      //echo "post POST<br>";
      $user_rut = $_POST['user_rut'];
      $pass = $_POST['user_password'];
      $type_post = $_POST['type_post'];
      $user_name = $_POST['name'];

      //$user = '13352626-9';
      //$pass = '123456';
      //$type = 'login';

      $url = "";

      if (strpos($type_post, "login") !== false) {

          $url = "http://python-login-services:9091/login";
          $data = array('user_rut'      => $user_rut,
                        'user_password' => $pass,
                        'type_post'     => $type_post

           );

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
          //echo json_encode($result.",".$type_post);
          echo $result. ",Post PHP:".$user_rut.",".$type_post;
          //echo "error:" .$error . "code status: " .$http_status;
          exit();

      }
     if (strpos($type_post, "usuario_tef") !== false) {
          $url = "http://python-login-services:9091/usuario_tef";

          $data = array('user_name'      => $user_name );

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
          //echo json_encode($result.",".$type_post);
          echo $result. ",Post PHP:".$user_name.",".$type_post;
          //echo "error:" .$error . "code status: " .$http_status;
          exit();

      }
      if (strpos($type_post, "usuarios_tef") !== false) {
          $url = "http://python-login-services:9091/usuarios_tef";

          #$data = array('user_name'      => $user_name );

          $options = array(
              'http' => array(
                  'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
                  'method'  => 'GET'
              )
          );
          $context  = stream_context_create($options);
          $result = file_get_contents($url, false, $context);
          if ($result === FALSE) { /* Handle error */ }

          header("HTTP/1.1 200 OK");
          //echo json_encode($result.",".$type_post);
          echo $result. ",GET PHP:".",".$type_post;
          //echo "error:" .$error . "code status: " .$http_status;
          exit();
      }

   }

}else{
    echo "href invalida - >uri_post: ". $uri_post ."  val_int: ". $val_int . " val_ext: ". $val_ext ;
    exit();
}

