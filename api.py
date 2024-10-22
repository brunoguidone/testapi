from flask import Flask, request, jsonify
import logging, sys

# Configuração do logger para stdout
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s')

app = Flask(__name__)

# Rota inicial da API
@app.route('/v1/', methods=['GET'])
def index():
    logging.info('Requisição bem-sucedida para a rota "/v1/"')
    return jsonify({
        'message': 'Bem vindo'
    })

# Rota para erro de página não encontrada, erro 400
@app.errorhandler(404)
def page_not_found(e):
    logging.error(f'Erro 404: Rota não encontrada - {request.url}')
    return jsonify({'message': 'Rota nao encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")