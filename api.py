from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota inicial da API
@app.route('/v1/', methods=['GET'])
def index():
    return jsonify({
        'message': 'Bem vindo'
    })

# Rota para erro de página não encontrada, erro 400
@app.errorhandler(404)
def page_not_found(e):
    # Registro de log
    return jsonify({'message': 'Rota nao encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")