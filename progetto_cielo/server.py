
import psycopg2

host="localhost"
port="5432"
dbname="cielo"
user="postgres"
password="postgres"


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

def visualizza_volo():
    cursor = connection.cursor()
    #eseguo query
    cursor.execute("select * from volo")
    #recupero dati
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print("\n")
    connection.close()

def visualizza_aeroporti():
    cursor1 = connection.cursor()
    #eseguo query
    cursor1.execute("select * from aeroporto")
    rows = cursor1.fetchall()
    for row in rows:
        print(row)
    print("\n")
    connection.close()

def visualizza_compagnie():
    cursor2 = connection.cursor()
    #eseguo query
    cursor2.execute("select * from compagnia")
    rows = cursor2.fetchall()
    for row in rows:
        print(row)
    print("\n")
    connection.close()

def query_utente():
    try:    
        query_ut= input("\ninserisci la tua query:\n")
        cursor3 = connection.cursor()
        cursor3.execute(query_ut)
        rows = cursor3.fetchall()
        for row in rows:
            print(row)
        print("\n")
    except Exception as e:
        print(f"query inserita non valida,{e}")
    finally:
        connection.close()



while True:
    print("\nOperazioni disponibili:")
    print("1. visualizza i voli")
    print("2.visualizza gli aeroposti")
    print("3. visualizza le compagnie")
    print("4. inserisci la tua query")
    print("5. Esci\n")
    a = int(input())

    if a ==1:
        visualizza_volo()
    elif a ==2:
        visualizza_aeroporti()
    elif a ==3:
        visualizza_compagnie()
    elif a ==4:
        query_utente()
    else:
        print("\nbuona giornata")
        break

        


