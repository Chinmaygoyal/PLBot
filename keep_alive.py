from flask import Flask
from threading import Thread
from update import updateAll


app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()

@app.route('/update', methods=['HEAD','GET'])
def updateFunc():
    # Update the standings and the fixtures
    updateAll()
    return "Updating standings and fixtures"