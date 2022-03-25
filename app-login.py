from flask import Flask, jsonify, request
from flask import Response
import mariadb
import sys

app = Flask(__name__)
@app.route("/login",  methods = ['POST'])
def login():

    #code =  Response(status=201)

    #try: 
      connxxx = mariadb.connect(
          user="root",
          password="Ts0ft2022#",
          host="mariadb-services",
          port=3306,
          database="homebanking"

      )
    #except mariadb.Error as e:
    #  print(f"Error connecting to MariaDB Platform: {e}")
    #  sys.exit(1) 
    
      if connxxx:
    
        cur = conn.cursor()
        user_rut =  request.form['user_rut']
        user_password = request.form['user_password']
        #type = request.form['type']

        #user_rut = "13352626-9"
        #user_password = "123456"
        
        cur = conn.cursor(buffered=True)
 
        cur.execute("SELECT user_rut,user_name FROM usuarios WHERE user_rut=? and user_password=?", (user_rut, user_password))
        #cur.execute("SELECT user_rut, user_name FROM usuarios")
  
        #print("SELECT user_rut,user_name FROM usuarios WHERE user_rut=? and user_password=?", (user_rut, user_password)) 

        result_rows = cur.rowcount

        if result_rows > 0:
            for (user_rut, user_name) in cur:
               name = user_name
               rut = user_rut
               #print (rut,"|",name)  
               #print ("code: ", code)               
            cur.close()
            conn.close()
            return '{}{}{}'.format(rut,",",name)
            #return '{}'.format("Error"),500
        else:
            cur.close()
            conn.close()
            return "Rut o password invalido"
      else:
        return '{}'.format("Error"),500   
   
