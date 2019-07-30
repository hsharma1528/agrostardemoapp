from flask import Flask
import socket
demoapp = Flask(__name__)

@demoapp.route('/')
def welcome():
    return 'Welcome to Demo app'

@demoapp.route('/hostname')
def hostname():
    return socket.gethostname()

@demoapp.route('/status')
def status():
    return 'App is running'

if __name__ == '__main__':
    demoapp.run(host="0.0.0.0", port=80)
    
