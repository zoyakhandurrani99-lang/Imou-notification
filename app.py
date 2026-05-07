from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/imou', methods=['POST'])
def receive():
    data = request.json
    time = datetime.datetime.now()
    print(f"Camera accessed at: {time}")
    print("Data received:", data)
    real_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print(f"Request from IP: {real_ip}")
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
