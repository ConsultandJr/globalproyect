from flask import Flask, jsonify, request
from flask import Response
import mariadb
import sys
import json
import oneagent
import autodynatrace

app = Flask(__name__)
@app.route("/home_saldos",  methods = ['POST','GET'] )
def home_saldos():

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
        user_id =  request.form['user_id']
        #user_password = request.form['user_password']
        #type = request.form['type']

        #user_rut = "25654345-2"
        #user_password = "123456"

        cur = conn.cursor(buffered=True)
        json_dict = create_dict()

        sql1 = "SELECT sal_name,sal_valor FROM saldos WHERE user_id=" + "'" + user_id + "'"
        sdk = oneagent.get_sdk()
        dbinfo = sdk.create_database_info('homebankingdb', oneagent.sdk.DatabaseVendor.MARIADB,oneagent.sdk.Channel(oneagent.sdk.ChannelType.TCP_IP, 'mariadb-services:3306'))
        with sdk.trace_sql_database_request(dbinfo, sql1) as tracer:
           tracer.start()
           cur.execute(sql1)
           rv = cur.fetchall()
           tracer.end()
           pass
        oneagent.shutdown()
        #rv = cur.fetchall()
        result_rows = cur.rowcount
        #json_data=[]
        if result_rows > 0:
            for row in rv:
              json_dict.add(row[0],({"sal_name":row[0],"sal_valor":row[1]}))
            cur.close()
            conn.close()
            return json.dumps(json_dict, indent=2, sort_keys=True)
        else:
            cur.close()
            conn.close()
            return "Sin Datos Saldos" + user_id

      else:
        return '{}'.format("Error"),500

@app.route("/mov_saldos",  methods = ['POST','GET'] )
def mov_saldos():

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
        user_id =  request.form['user_id']
        #user_password = request.form['user_password']
        #type = request.form['type']

        #user_rut = "25654345-2"
        #user_password = "123456"

        cur = conn.cursor(buffered=True)
        json_dict = create_dict()
        #cur.execute("SELECT tef_id,tef_fecha,tef_comentario,tef_valor,tef_cuenta_destino,user_saldo FROM tef WHERE user_id=" + "'" + user_id + "'")
        sql1 = "SELECT tef_id,tef_fecha,tef_comentario,tef_valor,tef_cuenta_destino,user_saldo FROM tef WHERE user_id=" + "'" + user_id + "'"
        sdk = oneagent.get_sdk()
        dbinfo = sdk.create_database_info('homebankingdb', oneagent.sdk.DatabaseVendor.MARIADB,oneagent.sdk.Channel(oneagent.sdk.ChannelType.TCP_IP, 'mariadb-services:3306'))
        with sdk.trace_sql_database_request(dbinfo, sql1) as tracer:
           tracer.start()
           cur.execute(sql1)
           rv = cur.fetchall()
           tracer.end()
           pass
        oneagent.shutdown()
        #cur.execute("SELECT * FROM tef")
        #rv = cur.fetchall()
        result_rows = cur.rowcount
        #json_data=[]
        if result_rows > 0:
            for row in rv:
              json_dict.add(row[0],({"tef_fecha":row[1],"tef_comentario":row[2],"tef_valor":row[3],"tef_cuenta_destino":row[4],"user_saldo":row[5]}))
            cur.close()
            conn.close()
            return json.dumps(json_dict, indent=2, sort_keys=False,default=str)
        else:
            cur.close()
            conn.close()
            return "Sin Datos - Movimientos (TEF) " + user_id

      else:
        return '{}'.format("Error"),500
