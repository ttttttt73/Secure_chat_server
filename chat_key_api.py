from flask import Flask, request, jsonify
from flask_cors import CORS
from base64 import b64encode, b64decode
import okKey
import TestKeyGen


app = Flask(__name__)
CORS(app)


@app.route('/genkey', methods=['POST'])
def genkey():
    json_data = request.get_json(force=True)
    uName = json_data['userName']
    key = okKey.getKey()
    TestKeyGen.privateKeyGen(uName, key)
    TestKeyGen.publicKeyGen(uName, key) 
    return 'OK'


@app.route('/encrypt', methods=['POST'])
def encrypt():
    json_data = request.get_json(force=True)
    message = json_data['message']
    uName = json_data['userName']
    priKey = okKey.readKey(uName + ".pem")
    pubKey = okKey.readPubKey(uName + ".pub")
    key = priKey.to_cryptography_key()
    pubKey = pubKey.to_cryptography_key()
    cMessage = okKey.pubEncrypt(pubKey, message)
    cMessage = b64encode(cMessage).decode('utf-8')
    return {'cMessage' : cMessage}


@app.route('/decrypt', methods=['POST'])
def decrypt():
    json_data = request.get_json(force=True)
    cMessage = json_data['cMessage']
    cMessage = b64decode(cMessage)

    uName = json_data['userName']
    priKey = okKey.readKey(uName + ".pem")
    pubKey = okKey.readPubKey(uName + ".pub")
    priKey = priKey.to_cryptography_key()
    pubKey = pubKey.to_cryptography_key()

    decMessage = okKey.priDecrypt(priKey, cMessage)

    return {'dMessage' : decMessage.decode()}