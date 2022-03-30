from flask import Flask, jsonify, request
from flask import Response
import mariadb
import sys
import json

app = Flask(__name__)
@app.route("/saldos",  methods = ['POST','GET'] )
def saldos():

    #code =  Response(status=201)

    #try: 
      conn = mariadb.connect(
          user="root",
          password="Ts0ft2022#",
          host="mariadb-services",
          port=3306,
          database="homebankinghb"

      )
      #except mariadb.Error as e:
      #  print(f"Error connecting to MariaDB Platform: {e}")
      #  sys.exit(1) 
    
      if conn:
    
        cur = conn.cursor()
        user_rut =  request.form['user_rut']
        #user_password = request.form['user_password']
        #type = request.form['type']

        user_rut = "25654345-2"
        #user_password = "123456"
        
        cur = conn.cursor(buffered=True)
        
        cur.execute("SELECT sal_name,sal_valor FROM saldos WHERE user_id=" + "'" + user_rut + "'")
        #cur.execute("SELECT sal_name,sal_valor FROM saldos")
        row_headers=[x[0] for x in cur.description]
        rv = cur.fetchall()
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
            return "Sin Datos"
         
      else:
        return '{}'.format("Error"),500   
   
