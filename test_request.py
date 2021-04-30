import requests
import argparse
import json


def genkey_test():
    url = "http://localhost:5000/genkey"
    payload_genkey = {
        "userName" : "bb"
    }
    return url, payload_genkey


def encrypt_test():
    url = "http://localhost:5000/encrypt"
    payload_encrypt = {
        "message" : "hello world", 
        "userName" : "bb"
        }
    return url, payload_encrypt


def decrypt_test():
    url = "http://localhost:5000/decrypt"
    cMessage = ""
    payload_decrypt = {
        "cMessage" : cMessage,
        "userName" : "bb"
    }
    return url, payload_decrypt


def parse_args():
    parser = argparse.ArgumentParser(description="test")
    parser.add_argument('mode', help='test mode')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    if args.mode == "genkey":
        url, payload = genkey_test()
    elif args.mode == "encrypt":
        url, payload = encrypt_test()
    elif args.mode == "decrypt":
        url, payload = decrypt_test()
    else:
        raise ValueError("Wrong mode")

    headers = {
        'Content-Type': 'application/json',
    }

    data = json.dumps(payload)

    response = requests.post('http://localhost:5000/genkey', headers=headers, data=data)


