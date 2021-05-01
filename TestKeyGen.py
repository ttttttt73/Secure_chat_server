import okKey

def privateKeyGen(uName, sec_key):
    fName = uName + ".pem"
    okKey.writeKey(fName, sec_key)

def publicKeyGen(uName, sec_key):
    pub_key = okKey.getPubKey(sec_key)
    fName = uName + ".pub"
    okKey.writePubKey(fName, pub_key)

def test_pubEncrypt():
    key = okKey.getKey().to_cryptography_key()
    pubKey = key.public_key()
    cMessage = okKey.pubEncrypt(pubKey, "My message")
    print (cMessage)
    rMessage = okKey.priDecrypt(key, cMessage)
    assert rMessage.decode() == "My message"

isKeyGen= True
if __name__ == "__main__":
    uName = "alice"
    if isKeyGen == False:
        sec_key = okKey.getKey()
        privateKeyGen(uName, sec_key)
        publicKeyGen(uName, sec_key)


    # generate private key and public key
    key = okKey.getKey().to_cryptography_key()
    pubKey = key.public_key()
    keyList = {'priKey': key, 'pubKey': pubKey}
    message = "hello world"
    cMessage = okKey.pubEncrypt(keyList['pubKey'], message)
    decMessage = okKey.priDecrypt(keyList['priKey'], cMessage)
    print(keyList)
    print(decMessage.decode())
