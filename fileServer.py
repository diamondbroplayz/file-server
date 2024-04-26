from bcolors import bcolors
from flask import Flask
from flask import send_from_directory
# import watchdog
import logging
import socket


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def getLocalIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip

print(f'{bcolors.OKGREEN + bcolors.BOLD}  → {bcolors.ENDC + bcolors.BOLD}Local: {getLocalIp()}{bcolors.ENDC}')

def create_app():
    app = Flask(__name__)

    @app.route('/<path:path>')
    def send_report(path):
        return send_from_directory('./', path)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=False)