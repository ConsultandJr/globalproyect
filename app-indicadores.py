from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from datetime import date
import requests
import mariadb
#import oneagent
#from oneagent.common import AgentState
#import autodynatrace


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



       '''if not oneagent.initialize():
          print('Error initializing OneAgent SDK.')

       sdk = oneagent.get_sdk()


       incall = sdk.trace_incoming_remote_call('Indicadores', 'Requests on python-indicadore
       with incall:
          incall.start()
          dbinfo = sdk.create_database_info(
          'homebankingdb', oneagent.sdk.DatabaseVendor.MARIADB,
          oneagent.sdk.Channel(oneagent.sdk.ChannelType.TCP_IP, 'mariadb-services:3306'))

          with sdk.trace_sql_database_request(dbinfo, sql1) as tracer:
            tracer.start()
            cur.execute(sql1)
            tracer.end()
        pass
            #tracer.set_rows_returned(1)
            #Optional
            #tracer.set_round_trip_count(1)
            #Optional
            incall.end()
       oneagent.shutdown()
      '''

       cur.execute(sql1)

       result_rows = cur.rowcount

       if result_rows > 0:
          for (ind_valor) in cur:
              ind_valor = ind_valor
          cur.close()
          conn.close()

          return '{}'.format(ind_valor)
       else:
          r = requests.get('https://mindicador.cl/api')
          sql2 = "insert into indicadores (ind_fecha, ind_valor) values(STR_TO_DATE('" + tod
          cur.execute(sql2)
          #cur.close()
          conn.commit()

          sql3 = "select ind_valor from indicadores where ind_fecha = " + "'" + today + "'"
          cur.execute(sql3)

          result_rows = cur.rowcount
          for (ind_valor) in cur:
              ind_valor = ind_valor
          cur.close()
          conn.close()
          return '{}'.format(ind_valor)
    else:
       return '{}'.format("Error"),500

       
   
