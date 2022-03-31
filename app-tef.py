from flask import Flask, jsonify, request
from flask import Response
import mariadb
import sys
import json
import oneagent
import autodynatrace


app = Flask(__name__)

@app.route("/id_tef",  methods = ['POST','GET'] )
def id_tef():

      try:
          conn = mariadb.connect(
          user="root",
          password="Ts0ft2022#",
          host="mariadb-services",
          port=3306,
          database="homebankingdb"
          )
      except mariadb.Error as e:
         print(f"Error connecting to MariaDB Platform: {e}")
         sys.exit(1)

      if conn:

         cur = conn.cursor()
         #user_rut =  request.form['user_id']
         #user_rut = "25654345-2"

         cur = conn.cursor(buffered=True)

         sql1 = "SELECT tef_id FROM tef order by tef_fecha asc"

         sdk = oneagent.get_sdk()
         dbinfo = sdk.create_database_info('homebankingdb', oneagent.sdk.DatabaseVendor.MARIADB,oneagent.sdk.Channel(oneagent.sdk.ChannelType.TCP_IP, 'mariadb-services:3306'))
         with sdk.trace_sql_database_request(dbinfo, sql1) as tracer:
           tracer.start()
           cur.execute(sql1)
           rv = cur.fetchall()
           row_headers=[x[0] for x in cur.description]
           tracer.end()
           pass
         oneagent.shutdown()

         #row_headers=[x[0] for x in cur.description]
         #rv = cur.fetchall()
         result_rows = cur.rowcount
         json_data=[]
         if result_rows > 0:
            for result in rv:
               json_data.append(dict(zip(row_headers,result)))
            cur.close()
            conn.close()
            return json.dumps(json_data)
         else:
            cur.close()
            conn.close()
            tef_id = 0
            return '{}{}'.format("tef_id:", tef_id)
            #return '{}{}'.format("tef:{id: + +  }")

      else:
         return '{}'.format("Error"),500

@app.route("/save_data_tef",  methods = ['POST','GET'] )
def save_data_tef():

      try:
          conn = mariadb.connect(
          user="root",
          password="Ts0ft2022#",
          host="mariadb-services",
          port=3306,
          database="homebankingdb"
          )
      except mariadb.Error as e:
         print(f"Error connecting to MariaDB Platform: {e}")
         sys.exit(1)

      if conn:

         cur = conn.cursor()

         fecha = request.form['fecha']
         monto = request.form['monto_transferido']
         user_rut =  request.form['user_id']
         saldo = request.form['saldo']
         cuenta_origen = request.form['cuenta_origen']
         cuenta_destino = request.form['cuenta_destino']
         comentario = request.form['comentario']
         email = request.form['email']


         #user_rut = "25654345-2"

         cur = conn.cursor(buffered=True)
         sql1 = "insert into tef (tef_fecha,tef_valor,user_id,user_saldo,tef_cuenta_origen,tef_cuenta_destino,tef_comentario,user_mail) values(STR_TO_DATE('" + fecha + "','%d-%m-%Y %H:%i:%s')," + monto + "," + "'" +  user_rut + "'"+ "," + saldo + "," + cuenta_origen + "," + cuenta_destino + "," + "'" + comentario + "'" + "," + "'" +  email + "'" + ")"


         sdk = oneagent.get_sdk()
         dbinfo = sdk.create_database_info('homebankingdb', oneagent.sdk.DatabaseVendor.MARIADB,oneagent.sdk.Channel(oneagent.sdk.ChannelType.TCP_IP, 'mariadb-services:3306'))
         with sdk.trace_sql_database_request(dbinfo, sql1) as tracer:
           tracer.start()
           cur.execute(sql1)
           #rv = cur.fetchall()
           tracer.end()
           pass
         oneagent.shutdown()
         #cur.execute(sql)
         cur.close()
         conn.commit()
         conn.close()

         return '{}{}'.format("sql inserto OK:",sql1)
      else:
         return '{}'.format("Error"),500



@app.route("/save_data_saldo_destino",  methods = ['POST','GET'] )
def save_data_saldo_destino():

      try:
          conn = mariadb.connect(
          user="root",
          password="Ts0ft2022#",
          host="mariadb-services",
          port=3306,
          database="homebankingdb"
          )
      except mariadb.Error as e:
         print(f"Error connecting to MariaDB Platform: {e}")
         sys.exit(1)

      if conn:

         cur = conn.cursor()

         user_rut =  request.form['user_id']
         saldo = request.form['nuevo_monto']

         cur = conn.cursor(buffered=True)
         sql1 = "UPDATE saldos SET sal_valor=" + saldo + "  WHERE sal_name='cuenta corriente' and user_id=" + "'" + user_rut + "'"
         sdk = oneagent.get_sdk()
         dbinfo = sdk.create_database_info('homebankingdb', oneagent.sdk.DatabaseVendor.MARIADB,oneagent.sdk.Channel(oneagent.sdk.ChannelType.TCP_IP, 'mariadb-services:3306'))
         with sdk.trace_sql_database_request(dbinfo, sql1) as tracer:
          tracer.start()
          cur.execute(sql1)
          cur.close()
          conn.commit()
          conn.close()
          tracer.end()
          pass
         oneagent.shutdown()
         #cur.execute(sql)
         #conn.close()

         return '{}{}'.format("sql:",sql1)
      else:
         return '{}'.format("Error"),500
@app.route("/save_data_saldo_origen",  methods = ['POST','GET'] )
def save_data_saldo_origen():

      try:
          conn = mariadb.connect(
          user="root",
          password="Ts0ft2022#",
          host="mariadb-services",
          port=3306,
          database="homebankingdb"
          )
      except mariadb.Error as e:
         print(f"Error connecting to MariaDB Platform: {e}")
         sys.exit(1)

      if conn:

         cur = conn.cursor()

         user_rut =  request.form['user_id']
         saldo = request.form['nuevo_monto']

         cur = conn.cursor(buffered=True)
         sql1 = "UPDATE saldos SET sal_valor=" + saldo + "  WHERE sal_name='cuenta corriente' and user_id=" + "'" + user_rut + "'"

         sdk = oneagent.get_sdk()
         dbinfo = sdk.create_database_info('homebankingdb', oneagent.sdk.DatabaseVendor.MARIADB,oneagent.sdk.Channel(oneagent.sdk.ChannelType.TCP_IP, 'mariadb-services:3306'))
         with sdk.trace_sql_database_request(dbinfo, sql1) as tracer:
          tracer.start()
          cur.execute(sql1)
          cur.close()
          conn.commit()
          conn.close()
          tracer.end()
          pass
         oneagent.shutdown()

         #cur.execute(sql)
         #cur.close()
         #conn.commit()
         #conn.close()

         return '{}{}'.format("sql:",sql1)
      else:
         return '{}'.format("Error"),500

