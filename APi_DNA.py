from flask import Flask, jsonify, request
from ADN import comprovation as dna
import pymysql as mysql

app = Flask(__name__)

@app.route('/',methods=['GET'])
def mutation():
    return jsonify({"API":"Mutations","Urls":{1:{"url":"http://127.0.0.1:3000/valMutations","method":"Post"},2:{"url":"http://127.0.0.1:3000/stats","method":"Get"}},"json_elements":{"name":"Required","dna":"Required"}})

@app.route('/stats',methods=['GET'])
def stats():
    db = mysql.connect(host='localhost', user= 'sw15_b', passwd='B03', db='mutation' )
    cursor = db.cursor()
    sql = 'SELECT COUNT(id_dna) AS dna FROM dna where mutation_dna = "True";'
    cursor.execute(sql)
    for dna in cursor.fetchall() :
        mutados = dna[0]
    sql = 'SELECT COUNT(id_dna) AS dna FROM dna where mutation_dna = "False";'
    cursor.execute(sql)
    for dna in cursor.fetchall() :
        noMutados = dna[0]
    print(noMutados,mutados)
    db.commit()
    db.close()
    ratio = mutados/noMutados
    return jsonify({"dats":{"count_mutations":mutados,"count_no_mutation": noMutados,"ratio": ratio}})

@app.route('/valMutations',methods=['POST'])
def valMutations():
    print(request.json)
    try:
        if request.json["name"] or request.json["dna"]:
            val = dna(request.json["dna"])
            if val == True:
                resp = jsonify({"mutation":val,"message":"Se encontraron mutaciones"})
                resp.status_code = 200
                print(request.json)
                print(val)
                pyMysql(request.json,val)
            else:
                resp = jsonify({"mutation":val,"message":"No se encontraron mutaciones"})
                resp.status_code = 403
                pyMysql(request.json,val)
        else:
            resp = jsonify({"error":"name","message":"Falta un elemento"})
            resp.status_code = 400
    except:
        resp = jsonify({"message":"Hubo un error","errores":{1:"falta name",2:"falta dna",3:"DNA ya fue creado",4:"la cadena no es valida"}})
        resp.status_code = 400
    return resp


def pyMysql(dats,validation):
    dna = ""
    dna = dats["dna"]
    db = mysql.connect(host='localhost', user= 'sw15_b', passwd='B03', db='mutation' )
    cursor = db.cursor()
    if validation == True:
        sql = 'INSERT INTO dna(id_dna, name_dna, chain_dna, mutation_dna) \
        VALUES (NULL,"{0}","{1}","True")'.format(dats["name"],dna,)
    else:
        sql = 'INSERT INTO dna(id_dna, name_dna, chain_dna, mutation_dna) \
        VALUES (NULL,"{0}","{1}","False")'.format(dats["name"],dna)
    
    print(sql)
    cursor.execute(sql)
    db.commit()
    db.close()
if __name__ == '__main__':
    """
        direccion de la api http://127.0.0.1:3000
    """
    app.run(debug=True, port=3000)