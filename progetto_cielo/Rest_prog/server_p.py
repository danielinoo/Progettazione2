from flask import Flask, jsonify, request
import psycopg2

host="172.24.111.42"
port = "5432"
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
        password = password,
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
            except (Exception, psycopg2.DatabaseError) as error:

                    error = str(error)
                    return jsonify({"ATTENZIONE": "ERRORE", "Msg": error}), 404
        else:
            return jsonify({"Esito": "ERRORE", "Msg": "content-type non supportato "}) 


# while True:
#     print("\nMenu principale:")
#     print("1. Visualizzare i voli")
#     print("2. Aggiungere un volo")
#     print("3. Modificare un volo")
#     print("4. Uscire")

#     try:
#         scelta = int(input("Scegli un'opzione (1-4): "))

#         if scelta == 1:
#             visualizza_volo()
#         elif scelta == 2:
#             visualizza_aeroporti()
#         elif scelta == 3:
#             visualizza_compagnie()
#         elif scelta == 4:
#             query_utente()
#         else:
#             print("Opzione non valida. Per favore scegli un numero tra 1 e 4.")
#     except ValueError:
#         print("Per favore, inserisci un numero valido.")




if __name__ == '__main__'  :    
    api.run(host="0.0.0.0", port=8085)

