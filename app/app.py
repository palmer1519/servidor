from flask import Flask,render_template, jsonify, Resource 
from flask_mysqldb import MySQL
import requests
import pandas as pd


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'api_rest'

conexion = MySQL(app)


@app.route('/')
def index():
    data = {
    'titulo': 'Servidor Johan :D',
    'bienvenida': 'Challenge 2'
    }
    return render_template('index.html', data=data)

@app.route('/pokemones')
def listar_pokemones():
    data = {}
    try:
        cursor=conexion.connection.cursor()
        sql = 'SELECT name, ability, limi FROM pokemones ORDER BY name ASC'
        cursor.execute(sql)
        pokemones = cursor.fetchall()
        data['pokemones'] = pokemones
        1519
        data['mensaje'] = 'Exito'

    except Exception as ex:
        data['mensaje'] = 'Error...'
        
    return jsonify(data)
    
@app.route('/poke')
def pokemon ():
    url = 'https://pokeapi.co/api/v2/generation/3/'
    
    data = {

    }
    r = requests.get(url, data = data).text
  
    return jsonify(r)

@app.route('/pokemon/<string:pokemon_name>')
def pokemon_page(pokemon_name):
    return render_template('index.html', pokemon_data = find_pokemon(pokemon_name, collection))


class PokemonByName(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json')
        super(PokemonByName, self).__init__()

    def get(self, name):
        pokemon = collection.find_one({'name' : name.capitalize()})
        if pokemon:
            return {'status': 'ok', 'data': pokemon}
        else:
            return {'status': 'error'} 

api.add_resource(PokemonByName,
                 '/pokemon/api/v1.0/pokemon/<string:name>', endpoint='name')


'''@app.route("/get")
def get_iris():

    import pandas as pd
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    return jsonify({
        "message": "Iris Dataset",
        "data": iris.to_dict()
        })
     '''   
        
if __name__=='__main__':
    app.run(debug=True, port=5000)