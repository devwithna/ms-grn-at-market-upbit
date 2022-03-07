# encoding: utf-8

from flask import jsonify, request
from flask_script import Manager

from project.app import create_app
from project.services import market
from flask_cors import CORS, cross_origin

market = market.MarketUpbit();
app = create_app()

manager = Manager(app)
CORS(app, resources={r'*': {'origins': '*'}})

@app.route("/get_ohlcv")
def get_ohlcv():
    ticker = request.args.get('ticker')
    priod = int(request.args.get('days'))
    
    return jsonify(market.get_ohlcv(ticker, priod))
    
if __name__ == '__main__':
    manager.run()
