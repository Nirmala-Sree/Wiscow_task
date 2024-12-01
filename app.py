from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Welcome to the Secure Wisecow App!"

# Path to your SSL certificate and key
cert_path = os.path.join(os.getcwd(), 'certs', 'wisecow-cert.pem')
key_path = os.path.join(os.getcwd(), 'certs', 'wisecow-key.pem')

# Ensure the SSL certificates are found, or raise an error
if not os.path.isfile(cert_path) or not os.path.isfile(key_path):
    raise FileNotFoundError("SSL certificates not found at specified paths!")

if __name__ == '__main__':
    # Run the Flask app with SSL
    app.run(host='0.0.0.0', port=5000, ssl_context=('certs/wisecow-cert.pem', 'certs/wisecow-key.pem'))
