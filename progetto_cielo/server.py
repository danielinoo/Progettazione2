from flask import Flask, jsonify, request
import psycopg2

host="localhost"
port="5432"
dbname="cielo"
user="postgres"
password="postgres"

api = Flask(__name__)


try:
    connection = psycopg2.connect(
        host = host,
        port = port,
        dbname = dbname,       
        user = user,
        password = password
    )
    print("connessione al database svvenuta con successo")

except Exception as e:
    print(f"Errore durante la connessione al database: {e}")


@api.route('/visualizza_volo')
def visualizza_volo():
    cursor = connection.cursor()
    #eseguo query
    cursor.execute("select * from volo")
    #recupero dati
    rows = cursor.fetchall()
    cursor.close()
    return rows 

@api.route('/visualizza_aeroporti')
def visualizza_aeroporti():
    cursor1 = connection.cursor()
    #eseguo query
    cursor1.execute("select * from aeroporto")
    rows = cursor1.fetchall()
    cursor1.close()
    return rows   

@api.route('/visualizza_compagnie')
def visualizza_compagnie():
    cursor2 = connection.cursor()
    #eseguo query
    cursor2.execute("select * from compagnia")
    rows = cursor2.fetchall()
    cursor2.close()
    return rows 


@api.route('/query_utente', methods = ['POST'])
def query_utente():

        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            query_ut= str(request.json.get('query'))
            try:
                cursor3 = connection.cursor()
                cursor3.execute(query_ut)
                rows = cursor3.fetchall()
                cursor3.close()
                return rows
            except  Exception as e:
                    return jsonify({"ATTENZIONE": "ERRORE", "Msg": e}), 404
        else:
            return jsonify({"Esito": "ERRORE", "Msg": "content-type non supportato "}) 






if __name__ == '__main__'  :    
    api.run(host="0.0.0.0", port=8080)

