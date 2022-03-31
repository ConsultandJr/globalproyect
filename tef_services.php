<?php

$uri_post = $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];


$val = ':9091/tef_services.php';


$hostname = php_uname('n');
//echo "href: " . $val;

if (strpos($uri_post, $val) !== false) {
   //echo "tef services php<br>";

   if ($_SERVER['REQUEST_METHOD'] == 'POST')
      {
      //echo "post POST<br>";
      $op = $_POST['op'];
      //echo "op: ". $op;
      if (strpos($op, "tef_id") !== false) {
          $url = "http://python-tef-services:9091/id_tef";
          $ch = curl_init();

          curl_setopt($ch,CURLOPT_URL, $url);
          //curl_setopt($ch,CURLOPT_GET, true);
          curl_setopt($ch, CURLOPT_FAILONERROR, true);
          curl_setopt($ch,CURLOPT_RETURNTRANSFER, true);
          curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);

          $result = curl_exec($ch);
          $error =  curl_error($ch);
          $http_status = curl_getinfo($ch, CURLINFO_HTTP_CODE);

          header("HTTP/1.1 200 OK");
          //echo json_encode($result.",".$type_post);
          echo "result:".$result;
          //echo "error:" .$error . "code status: " .$http_status;
          exit();
      }
      if (strpos($op, "save_data_tef") !== false) {
          $url = "http://python-tef-services:9091/save_data_tef";
          $fecha = $_POST['fecha'];
          $monto_transferido = $_POST['monto_transferido'];
          $user_id = $_POST['user_id'];
          $saldo = $_POST['saldo'];
          $cuenta_origen = $_POST['cuenta_origen'];
          $cuenta_destino = $_POST['cuenta_destino'];
          $comentario = $_POST['comentario'];
          $email = $_POST['email'];

          $fields = [
             'fecha'      => $fecha,
             'monto_transferido' => $monto_transferido,
             'user_id' => $user_id,
             'saldo' => $saldo,
             'cuenta_origen' => $cuenta_origen,
             'cuenta_destino' => $cuenta_destino,
             'comentario' => $comentario,
             'email' => $email
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

          header("HTTP/1.1 200 OK");
          //echo json_encode($result.",".$type_post);
          echo "result:".$result;
          //echo "error:" .$error . "code status: " .$http_status;
          exit();
      }
      if (strpos($op, "save_data_saldo_destino") !== false) {
          $url = "http://python-tef-services:9091/save_data_saldo_destino";
          $nuevo_monto = $_POST['nuevo_monto'];
          $user_id = $_POST['user_id'];

          $fields = [
             'nuevo_monto' => $nuevo_monto,
             'user_id' => $user_id
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

          header("HTTP/1.1 200 OK");
          //echo json_encode($result.",".$type_post);
 echo "result:".$result;
          //echo "error:" .$error . "code status: " .$http_status;
          exit();
      }
      if (strpos($op, "save_data_saldo_origen") !== false) {
          $url = "http://python-tef-services:9091/save_data_saldo_origen";
          $nuevo_monto = $_POST['nuevo_monto'];
          $user_id = $_POST['user_id'];

          $fields = [
             'nuevo_monto' => $nuevo_monto,
             'user_id' => $user_id
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

          header("HTTP/1.1 200 OK");
          //echo json_encode($result.",".$type_post);
          echo "result:".$result;
          //echo "error:" .$error . "code status: " .$http_status;
          exit();
      }

   }

}else{
    echo "href invalida - >uri_post: ". $uri_post ."  ". $val ;
    exit();
}

