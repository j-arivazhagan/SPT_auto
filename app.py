from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import paramiko
import os
from datetime import datetime  # Import datetime for unique filenames

app = Flask(__name__)
socketio = SocketIO(app)

ssh = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    global ssh
    data = request.form
    host = data.get('host')
    username = data.get('username')
    port = int(data.get('port'))
    passphrase = data.get('passphrase')
    private_key = request.files.get('private_key')

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Save the private key locally
        if private_key:
            key_path = os.path.join('output', 'uploaded_key.pem')
            private_key.save(key_path)
            key = paramiko.RSAKey.from_private_key_file(key_path, password=passphrase)
            ssh.connect(host, username=username, port=port, pkey=key)
        else:
            password = data.get('password')
            ssh.connect(host, username=username, port=port, password=password)

        socketio.emit('update', {'message': 'Logged in successfully!'})
        return jsonify({"status": "success", "message": "Logged in successfully"})
    except Exception as e:
        socketio.emit('update', {'message': f"Login failed: {str(e)}"})
        return jsonify({"status": "error", "message": str(e)})

@app.route('/fetch_ifconfig', methods=['POST'])
def fetch_ifconfig():
    try:
        if not ssh:
            socketio.emit('update', {'message': "Not logged in to the server"})
            return jsonify({"status": "error", "message": "Not logged in to the server"})

        socketio.emit('update', {'message': 'Fetching ifconfig...'})
        stdin, stdout, stderr = ssh.exec_command('ifconfig')
        output = stdout.read().decode()
        error = stderr.read().decode()

        if error:
            socketio.emit('update', {'message': f"Error executing ifconfig: {error}"})
            return jsonify({"status": "error", "message": error})

        ifconfig_path = os.path.join('output', 'ifconfig.txt')
        with open(ifconfig_path, 'w') as f:
            f.write(output)

        socketio.emit('update', {'message': 'ifconfig fetched successfully!'})
        return jsonify({"status": "success", "message": "ifconfig fetched successfully", "output": output})
    except Exception as e:
        socketio.emit('update', {'message': f"Exception: {str(e)}"})
        return jsonify({"status": "error", "message": str(e)})

@app.route('/run_nmap', methods=['POST'])
def run_nmap():
    try:
        if not ssh:
            socketio.emit('update', {'message': "Not logged in to the server"})
            return jsonify({"status": "error", "message": "Not logged in to the server"})

        command = request.form.get('nmap_command')
        socketio.emit('update', {'message': f"Running Nmap command: {command}"})

        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        if error:
            socketio.emit('update', {'message': f"Error executing Nmap: {error}"})
            return jsonify({"status": "error", "message": error})

        # Generate a unique filename with a timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        nmap_path = os.path.join('output', f'nmap_output_{timestamp}.txt')
        
        # Save the output to the unique file
        with open(nmap_path, 'w') as f:
            f.write(output)

        socketio.emit('update', {'message': f'Nmap scan completed! Output saved to {nmap_path}'})
        return jsonify({"status": "success", "message": "Nmap scan completed", "output": output, "file": nmap_path})
    except Exception as e:
        socketio.emit('update', {'message': f"Exception: {str(e)}"})
        return jsonify({"status": "error", "message": str(e)})
    
if __name__ == '__main__':
    os.makedirs('output', exist_ok=True)
    socketio.run(app, debug=True)
