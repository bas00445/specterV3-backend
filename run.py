from flask import Flask
from flask_socketio import SocketIO, emit, send
from resources.algorithm.FacadeAlg import FacadeAlg
from resources.database.DatabaseFacade import DatabaseFacade
import simplejson
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# @socketio.on('action')
# def handleAction(action):
#     print("Got an action:", action['type'])
#     payload = action['payload']
#     budget = payload['budget']
#     priorities = payload['priorities']

#     database = DatabaseFacade()
#     partsPicker = FacadeAlg(database)
#     bestSpec = partsPicker.getBestParts(budget, priorities)
#     responseData = simplejson.dumps(bestSpec)
#     emit('action', {'type': 'response_get_auto',  'payload': responseData})

# @socketio.on('connect')
# def test_connect():
#     print('A client connected')

# @socketio.on('disconnect')
# def test_disconnect():
#     print('A client disconnect')

@app.route('/')
def index():
  return 'SpecterV3-Server test'

def create_app(config_filename):
    app.config.from_object(config_filename)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from Model import db
    db.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app("config")
    
    port = int(os.environ.get("PORT", 8070))
    # app.run(debug=True, host="0.0.0.0", threaded=True) # For debug
    app.run(host="0.0.0.0", port=port, threaded=True) # For debug
    # socketio.run(app, host="0.0.0.0", port=port, threaded=True) # For deploy socket
