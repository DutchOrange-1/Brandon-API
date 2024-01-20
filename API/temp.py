# import the connect method
import re
from mysql.connector import connect, Error
import json


def upload_data(id, val, user, db_name):
      try:

                  # define a connection object
                  conn = connect(
                        user = 'apiuser',
                        password = 'redacted',
                        host = 'localhost',
                        database = 'databases')
                  print('A connection object has been created.')
                  # open cursor, define and run query, fetch results

                  cursor = conn.cursor()
                  query = 'INSERT INTO '+db_name+' (probe_id, value, date, user) VALUES ('+str(id)+', '+str(val)+', NOW(),\''+user+'\')'
                  cursor.execute(query)
                  conn.commit()
                  conn.close()
                  return(200)

      except Error as err:
            print('Error message on data upload: ' + err.msg)
            return(500)

def collect_data(probe_id, db_name, amount):
      try:
                  # define a connection object
                  conn = connect(
                        user = 'apiuser',
                        password = 'redacted',
                        host = 'localhost',
                        database = 'databases')
                  print('A connection object has been created for collection.')
                  # open cursor, define and run query, fetch results

                  cursor = conn.cursor()
                  query = 'SELECT date, value  FROM '+db_name+' WHERE probe_id = '+probe_id+' ORDER BY date DESC LIMIT '+amount+''
                  cursor.execute(query)
                  rows = cursor.fetchall()
                  conn.close()
                  for row in rows:
                        print("D: " + str(row[0]))
                        print("V: " + str(row[1]))

                  data = {}
                  for row in rows:
                         data[str(row[0])] = str(row[1])

                  print("DATA:")
                  print(data)
                  return ({'status': 69}, data)


      except Error as err:
            print('Error message on data upload: ' + err.msg)
            return ({'status': 500},{})

class temperature:
     
      #Uploads temperature values
      def upload_temperature(user, token, id, val):
            try:

                  # define a connection object
                  conn = connect(
                        user = 'apiuser',
                        password = 'redacted',
                        host = 'localhost',
                        database = 'databases')
                  print('A connection object has been created.')
                  # open cursor, define and run query, fetch results

                  cursor = conn.cursor()
                  query = 'SELECT * FROM datasets WHERE user = \'' + user + '\';'
                  cursor.execute(query)
                  result = cursor.fetchall()
                  conn.close()
                  
                  # print(result[0][3])
                  if len(result) == 0:
                        print("404 - No datasets found")
                        return(404)
                  elif result[0][3] == token:
                        print("Token is correct") 
                        return upload_data(id, val, user, result[0][1])

                  else:
                        print("400 - Incorrect token")
                        return(400)      

            except Error as err:
                  print('Error message: ' + err.msg)
                  return(500)

      #Gets the temperature values. 
      def get_temperature(user, token, probe_id, amount):
            
            try:
                  # define a connection object
                  conn = connect(
                        user = 'apiuser',
                        password = 'redacted',
                        host = 'localhost',
                        database = 'databases')
                  print('A connection object has been created.')
                  # open cursor, define and run query, fetch results

                  cursor = conn.cursor()
                  query = 'SELECT * FROM datasets WHERE user = \'' + user + '\';'
                  cursor.execute(query)
                  result = cursor.fetchall()
                  conn.close()
                  
                  # print(result[0][3])
                  if len(result) == 0:
                        print("404 - No datasets found")
                        return ({'status': 404},{})
                  
                  elif result[0][3] == token:
                        print("Token is correct - collection") 
                        return collect_data(probe_id, result[0][1],  amount)

                  else:
                        print("400 - Incorrect token")
                        return ({'status': 400},{})     

            except Error as err:
                  print('Error message: ' + err.msg)
                  return ({'status': 500},{})
      


