import hashlib
from urllib.parse import unquote
import base64
import json
import requests

# Credentials:
admin_email = "zkui@yopmail.com"
secret_key = "39e760479d69f61ada2f598007cab3aa"
xor_key = "666666"


def check_token(client_domain, hash_generated, uid, token, timestamp):
    url = "https://"+client_domain+".darwinbox.in/checkToken"
    payload=json.dumps({
        "hash":hash_generated,
        "Uid": uid,
        "timestamp": timestamp,
        "token": token
    })
    headers = {
    'Content-Type': 'application/json'
    }
    r = requests.request("GET", url, headers=headers, data = payload)
    content = json.loads(r.text)
    print(f"CHECK TOKEN: {content}")
    return content["message"]    

def XOREncryption(input_str, key):
    no_of_itr = len(input_str)
    output_str = ""
    for i in range(no_of_itr):
        current = (input_str[i])
        current_key = key[i%len(key)]
        output_str += chr(ord(current) ^ ord(current_key))
    return output_str

def XOR_DECODING(url_data_param, xor_key):
    print("Input Parameter:\n"+url_data_param+"\n")

    # Step0: URL Decode
    url_params_decoded = unquote(url_data_param)
    print("URL Decoded: "+url_params_decoded+"\n")

    # Step1 : Base64 Decode
    base64_decoded = base64.b64decode(url_params_decoded)
    print(f"Base64 Decoded: {base64_decoded}\n")

    # Step2 : XOR encryption with xor key
    xored = XOREncryption(base64_decoded.decode(), xor_key)
    print(f"XORED: {xored}") 

    # Step3: Base64 Decode
    base64_decoded_2 = base64.b64decode(xored)
    print(f"Base64 Decoded 2: {base64_decoded_2}\n")

    # Step4: JSON Decode
    payload = json.loads(base64_decoded_2.decode())
    print(f"Output Payload: {payload}\n")

    # Step5: Check Hash:
    client_domain = payload["company_name"]
    hash_recieved = payload["hash"]
    timestamp = str(payload["timestamp"])
    uid = payload["Uid"]
    token = payload["token"]
    pattern = admin_email+secret_key+timestamp
    hash_obj = hashlib.sha512(pattern.encode())
    hash_generated = hash_obj.hexdigest()
    print(hash_generated)
    return check_token(client_domain, hash_generated, uid, token, timestamp)




URL = "https://kotak-life-uat.allincall.in/chat/bot/?id=2&email=xyz@kotak.com&ename=xyz&esource=allincall?data=U098WlRhcEZUdX8Af1p4BmxubFp7cndPZ35aQFVxB15XYUFDbwQPQn9fQV9ScVpCbG54Bm9hB0F%2FXFlOeFx3THtcYwV4TG9PenV8WW9ueFl%2FXFlfb1x7BXtxcwR4XHMDe2JvQXhMY094XHcGbHFzA3tMUQR5YWMGbFxVBXhycwV7YXtBb0xjBnhhewN7YWBcbFx%2FT2xcZ095clFBeAR7BHlyY0F7YmcCeFxkXnlyVQd7W2xab1tzAnlycFt5YW8CewR%2FTHtid0x7THBbe0xaXHhbZF57YWxfbHJzTHtMcFp4YWdPeXJsW3tcbwN5cWcEe1tzA29Md0x7W3sHeFt%2FX3p1fGBXYWdfeV9%2FTntce196dXxaVG50RVQFWlpsYA9DVE9%2FAH9dY0F7cnMFf19BX28ED0JVcXBDU2APQ29hB1p%2FXFlfYARaRWxyc196dXxbV258TFJxA15UYWNfeV98fFRYZFpsBXxeUnFaQFRYe196dXxFb254BlRbcEJsZX8Af11wXVRhWkN%2FX0FfVARsW1dheFpuBAdAb1taRWxlfwB%2FX39Ff1sPW2xbWlxsYA9FVAR4XlJxWkBUWg9cV25kA39cWV9kcWBFV3FdX3p1fEBsW2xGbwRgUFRxD1xvbmRGVAQDUFVxWkNvBA9dbGV%2FAH9ff0V%2FWGRAVwRgQ39cWV97YnBabFxaXXtyewJ4THcCbwRvB3ticFtvTFEHeExkXnhMXQZ7TGMCbFtjX1BnCws%3D"
URL_DATA_PARAM = URL.split("data=")[1]
print(XOR_DECODING(URL_DATA_PARAM, xor_key))
  