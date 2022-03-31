from flask import Flask, jsonify, request
from flask import Response
import mariadb
import sys
import json
import oneagent
import autodynatrace


app = Flask(__name__)
@app.route("/login",  methods = ['POST'])
def login():

    #code =  Response(status=201)

    #try:
    conn = mariadb.connect(
          user="root",
          password="Ts0ft2022#",
          host="mariadb-services",
          port=3306,
          database="homebankingdb"

    )
    #except mariadb.Error as e:
    #  print(f"Error connecting to MariaDB Platform: {e}")
    #  sys.exit(1)

    if conn:

       cur = conn.cursor()
       user_rut =  request.form['user_rut']
       user_password = ""
       user_password = request.form['user_password']
       type_post = request.form['type_post']
       #user_rut = "13352626-9"
       #user_password = "123456"

       cur = conn.cursor(buffered=True)

       if type_post.find("login")!=-1:
          sql1 = "SELECT user_rut,user_name,user_cuenta,user_mail FROM usuarios WHERE user_rut=" + "'" + user_rut + "' and user_password=" + "'" + user_password + "'"
          if not oneagent.initialize():
             print('Error initializing OneAgent SDK.')
          sdk = oneagent.get_sdk()
          dbinfo = sdk.create_database_info('homebankingdb', oneagent.sdk.DatabaseVendor.MARIADB,oneagent.sdk.Channel(oneagent.sdk.ChannelType.TCP_IP, 'mariadb-services:3306'))
          with sdk.trace_sql_database_request(dbinfo, sql1) as tracer:
           tracer.start()
           cur.execute(sql1)
           tracer.end()
           pass
          oneagent.shutdown()

       result_rows = cur.rowcount
       
       if result_rows > 0:
          for (user_rut, user_name, user_cuenta, user_mail) in cur:
              name = user_name
              rut = user_rut
              cuenta = user_cuenta
              mail = user_mail
          cur.close()
          conn.close()
          return '{}{}{}{}{}{}{}{}{}{}{}'.format(rut,",",name,",",cuenta,",",mail,",Post Python:",user_rut,",",type_post)
       else:
          cur.close()
          conn.close()
          return "Rut o password invalido"
    else:
       return '{}'.format("Error"),500



@app.route("/usuario_tef",  methods = ['POST'])
def usuario_tef():

    #code =  Response(status=201)

    #try:
    conn = mariadb.connect(
          user="root",
          password="Ts0ft2022#",
          host="mariadb-services",
          port=3306,
          database="homebankingdb"

    )
    #except mariadb.Error as e:
    #  print(f"Error connecting to MariaDB Platform: {e}")
    #  sys.exit(1)

    if conn:

       cur = conn.cursor()
       user_name =  request.form['user_name']
       #user_rut = "13352626-9"

       cur = conn.cursor(buffered=True)

       sql1 = "SELECT user_rut,user_banco,user_tip_cuenta,user_cuenta,user_mail FROM usuarios WHERE user_name=" + "'" + user_name + "'"

       if not oneagent.initialize():
             print('Error initializing OneAgent SDK.')
       sdk = oneagent.get_sdk()
       dbinfo = sdk.create_database_info('homebankingdb', oneagent.sdk.DatabaseVendor.MARIADB,oneagent.sdk.Channel(oneagent.sdk.ChannelType.TCP_IP, 'mariadb-services:3306'))
       with sdk.trace_sql_database_request(dbinfo, sql1) as tracer:
         tracer.start()
         cur.execute(sql1)
         tracer.end()
         pass
       oneagent.shutdown()
       result_rows = cur.rowcount

       if result_rows > 0:
          for (user_rut, user_banco, user_tip_cuenta, user_cuenta, user_mail) in cur:
               rut = user_rut
               banco = user_banco
               tip_cuenta = user_tip_cuenta
               cuenta = user_cuenta
               mail = user_mail
          cur.close()
          conn.close()
          #por cada , se debe pasar un {}
          return '{}{}{}{}{}{}{}{}{}'.format(rut,",",banco,",",tip_cuenta,",",cuenta,",",mail)
       else:
          cur.close()
          conn.close()
          return "Error"
    else:
       return '{}'.format("Error"),500

@app.route("/usuarios_tef",  methods = ['GET'])
def usuarios_tef():

    #code =  Response(status=201)

    #try:
    conn = mariadb.connect(
          user="root",
          password="Ts0ft2022#",
          host="mariadb-services",
          port=3306,
          database="homebankingdb"

    )
    #except mariadb.Error as e:
    #  print(f"Error connecting to MariaDB Platform: {e}")
    #  sys.exit(1)

    class create_dict(dict):
       # __init__ function
       def __init__(self):
         self = dict()

       # Function to add key:value
       def add(self, key, value):
         self[key] = value


    if conn:

       cur = conn.cursor()
       cur = conn.cursor(buffered=True)
       json_dict = create_dict()
       sql1 = "select user_id,user_name from usuarios order by user_id"
       if not oneagent.initialize():
             print('Error initializing OneAgent SDK.')
       sdk = oneagent.get_sdk()
       dbinfo = sdk.create_database_info('homebankingdb', oneagent.sdk.DatabaseVendor.MARIADB,oneagent.sdk.Channel(oneagent.sdk.ChannelType.TCP_IP, 'mariadb-services:3306'))
       with sdk.trace_sql_database_request(dbinfo, sql1) as tracer:
         tracer.start()
         cur.execute(sql1)
         tracer.end()
         pass
       oneagent.shutdown()

       rv = cur.fetchall()
       result_rows = cur.rowcount

       if result_rows > 0:
          for row in rv:
              json_dict.add(row[0],({"user_name":row[1]}))
          cur.close()
          conn.close()
          return json.dumps(json_dict, indent=2, sort_keys=True)
       else:
          cur.close()
          conn.close()
          return "Error"
    else:
       return '{}'.format("Error"),500
 
