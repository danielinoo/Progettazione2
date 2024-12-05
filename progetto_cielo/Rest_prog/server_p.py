from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

api = Flask(__name__)


#http://127.0.0.1:5004/
db_config = {
    #ip addr
    "host": "172.19.130.81",  # va cambiato ogni volta che ri accende/riavvia la macchina
    "port": "5432",
    "dbname": "cielo",
    "user": "postgres",
    "password": "postgres"
}

def get_db_connection():
    try:
        return psycopg2.connect(**db_config, cursor_factory=RealDictCursor)
    except Exception as e:
        return str(e)


@api.route("/", methods=['GET'])
def lesgosky():
     return "<p> bello zi </p>"


@api.route('/visualizza_volo', methods=['GET'])
def visualizza_volo():
    connection = get_db_connection()
    cursor = connection.cursor()
    #eseguo query
    cursor.execute("select * from volo")
    #recupero dati
    rows = cursor.fetchall()
    cursor.close()
    return rows 

@api.route('/visualizza_aeroporti', methods=['GET'])
def visualizza_aeroporti():
    connection = get_db_connection()
    cursor1 = connection.cursor()
    #eseguo query
    cursor1.execute("select * from aeroporto")
    rows = cursor1.fetchall()
    cursor1.close()
    return rows   

@api.route('/visualizza_compagnie', methods=['GET'])
def visualizza_compagnie():

    connection = get_db_connection()
    cursor2 = connection.cursor()
    #eseguo query
    cursor2.execute("select * from compagnia")
    rows = cursor2.fetchall()
    cursor2.close()
    return rows 


# @api.route('/query_utente', methods = ['POST'])
# def query_utente():

#         content_type = request.headers.get('Content-Type')
#         if content_type == 'application/json':
#             query_ut= str(request.json.get('query'))
#             try:

#                 connection = get_db_connection()
#                 cursor3 = connection.cursor()
#                 cursor3.execute(query_ut)
#                 rows = cursor3.fetchall()
#                 cursor3.close()

#                 return rows
#             except (Exception, psycopg2.DatabaseError) as error:

#                     error = str(error)
#                     return jsonify({"ATTENZIONE": "ERRORE", "Msg": error}), 404
#         else:
#             return jsonify({"Esito": "ERRORE", "Msg": "content-type non supportato "}) 


@api.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Risorsa non trovata"}), 404

@api.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Errore interno del server"}), 500




if __name__ == '__main__'  :    
    api.run(host="0.0.0.0", port=5004)

