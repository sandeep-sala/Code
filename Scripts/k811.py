from Crypto.Cipher import AES
from Crypto import Random
import base64

class AESKOTAK811:
    def __init__( self, key ):
        self.BS    = 16
        self.pad   = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS) 
        self.unpad = lambda s : s[0:-ord(s[-1])]
        self.key   = base64.b64decode(key)
        self.iv    = Random.new().read(AES.block_size);

    def encrypt( self, raw ):
        raw    = self.pad(raw)
        cipher = AES.new( self.key, AES.MODE_CBC, self.iv )
        return base64.b64encode( cipher.encrypt( self.iv + raw.encode() ) ).decode()

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        cipher = AES.new( self.key, AES.MODE_CBC, enc[:16] )
        return self.unpad((cipher.decrypt( enc[16:])).decode())

message        = "spiderman"
message        = "vendor_id=INT_GTW&msg_code=KB0125&format=json&data={\"header\":{\"msg_code\":\"KB0125\",\"source\":\"ALLINCALL\",\"channel\":\"WHATSAPP\",\"txn_ref_number\":\"ALLINCALL_WHATSAPP_0001\",\"txn_datetime\":\"1510304150743\",\"ip\":\"10.10.1.19\",\"device_id\":\"XYWZPQR123\"},\"detail\":{\"entity_code\":\"KMBL\",\"appl_id\":\"6ad8818bd795971460b7a91723c211ef\",\"mode\":\"A\",\"mobile_no\":\"1111111111\",\"filler1\":\"\",\"filler2\":\"\",\"filler3\":\"\",\"filler4\":\"\",\"filler5\":\"\"}}"
key            = "115f2538ee70d1d3212a61faa6761ade"
chiper         =  AESKOTAK811(key)
encrypted_data = chiper.encrypt(message)
print(encrypted_data)
decrypted_data = chiper.decrypt(encrypted_data)
print(decrypted_data)