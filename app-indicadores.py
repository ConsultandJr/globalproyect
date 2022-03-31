from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from datetime import date
import requests
import mariadb
import oneagent
import autodynatrace


app = Flask(__name__)

@app.route("/indicadores",  methods = ['GET'])

def indicadores():


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
       cur = conn.cursor(buffered=True)
       today = str(date.today()) + " 00:00:00"

       sql1 = "select ind_valor from indicadores where ind_fecha = " + "'" + today + "'"

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
          for (ind_valor) in cur:
              ind_valor = ind_valor
          cur.close()
          conn.close()
          return '{}'.format(ind_valor)
       else:
          r = requests.get('https://mindicador.cl/api')
          sql2 = "insert into indicadores (ind_fecha, ind_valor) values(STR_TO_DATE('" + today + "','%Y-%m-%d %H:%i:%s')," + '"' + str(r.json()) + '"' + ")"

          if not oneagent.initialize():
             print('Error initializing OneAgent SDK.')
          sdk = oneagent.get_sdk()
          dbinfo = sdk.create_database_info('homebankingdb', oneagent.sdk.DatabaseVendor.MARIADB,oneagent.sdk.Channel(oneagent.sdk.ChannelType.TCP_IP, 'mariadb-services:3306'))
          with sdk.trace_sql_database_request(dbinfo, sql1) as tracer:
            tracer.start()
            cur.execute(sql2)
            conn.commit()
            tracer.end()
            pass
          oneagent.shutdown()


          sql3 = "select ind_valor from indicadores where ind_fecha = " + "'" + today + "'"

          if not oneagent.initialize():
             print('Error initializing OneAgent SDK.')
          sdk = oneagent.get_sdk()
          dbinfo = sdk.create_database_info('homebankingdb', oneagent.sdk.DatabaseVendor.MARIADB,oneagent.sdk.Channel(oneagent.sdk.ChannelType.TCP_IP, 'mariadb-services:3306'))
          with sdk.trace_sql_database_request(dbinfo, sql1) as tracer:
            tracer.start()
            cur.execute(sql3)
            #conn.commit()
            tracer.end()
            pass
          oneagent.shutdown()

          result_rows = cur.rowcount
          for (ind_valor) in cur:
              ind_valor = ind_valor
          cur.close()
          conn.close()
          return '{}'.format(ind_valor)
    else:
       return '{}'.format("Error"),500
   
