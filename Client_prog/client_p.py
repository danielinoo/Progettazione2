from flask import Flask, jsonify, render_template, request
api = Flask(__name__)


@api.route("/")
def primapagina():
    return render_template('primapagina.html')


@api.route("/visualizza_voli")
def opzione1():

    
    return 


@api.route("/visualizza_aeroporti")
def opzione2():
    return



@api.route("/visualizza_compagnie")
def opzione3():
    pass



@api.route("/query_utente",methods = ['POST'])
def opzione4():
    pass






if __name__ == '__main__'  :    
    api.run(host="0.0.0.0", port=8080)