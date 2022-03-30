from flask import Flask, jsonify, request
from flask import Response
import mariadb
import sys
import json

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
          cur.execute("SELECT user_rut,user_name,user_cuenta,user_mail FROM usuarios WHERE u

       result_rows = cur.rowcount

       if result_rows > 0:
          for (user_rut, user_name, user_cuenta, user_mail) in cur:
              name = user_name
              rut = user_rut
              cuenta = user_cuenta
              mail = user_mail
          cur.close()
          conn.close()
          return '{}{}{}{}{}{}{}{}{}{}{}'.format(rut,",",name,",",cuenta,",",mail,",Post Pyt
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

       cur.execute("SELECT user_rut,user_banco,user_tip_cuenta,user_cuenta,user_mail FROM us

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
          return '{}{}{}{}{}{}{}{}{}'.format(rut,",",banco,",",tip_cuenta,",",cuenta,",",mai
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
       cur.execute("select user_id,user_name from usuarios order by user_id")
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
