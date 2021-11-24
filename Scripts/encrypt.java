import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.UnsupportedEncodingException;
import java.security.GeneralSecurityException;
import java.util.Base64;

public class AESCBCPKCS5Encryption {

  private static final String ALGORITHM = "AES/CBC/PKCS5Padding";
  public static String encrypt(String message, String key) throws GeneralSecurityException, UnsupportedEncodingException {
    if(message == null || key == null){
      throw new IllegalArgumentException("text to be encrypted and key should not be null");
    }
    Cipher cipher = Cipher.getInstance(ALGORITHM);
    byte[] messageArr = message.getBytes();
    SecretKeySpec keySpec = new
SecretKeySpec(Base64.getDecoder().decode(key), "AES");
    byte[] ivParams = new byte[16];
    byte[] encoded = new byte[messageArr.length + 16];
    System.arraycopy(ivParams,0,encoded,0,16);
    System.arraycopy(messageArr, 0, encoded, 16, messageArr.length);
    cipher.init(Cipher.ENCRYPT_MODE, keySpec, new IvParameterSpec(ivParams));
    byte[] encryptedBytes = cipher.doFinal(encoded);
    encryptedBytes = Base64.getEncoder().encode(encryptedBytes);
    return new String(encryptedBytes);
  }
  public static String decrypt(String encryptedStr, String key) throws GeneralSecurityException, UnsupportedEncodingException {
    if(encryptedStr == null || key == null){
      throw new IllegalArgumentException("text to be decrypted and key should not be null");
    }
    Cipher cipher = Cipher.getInstance(ALGORITHM);
    SecretKeySpec keySpec = new
SecretKeySpec(Base64.getDecoder().decode(key), "AES");
    byte[] encoded = encryptedStr.getBytes();
    encoded = Base64.getDecoder().decode(encoded);
    byte[] decodedEncrypted = new byte[encoded.length-16];
    System.arraycopy(encoded, 16, decodedEncrypted, 0,encoded.length-16);
    byte[] ivParams = new byte[16];
    System.arraycopy(encoded,0, ivParams,0, ivParams.length);
    cipher.init(Cipher.DECRYPT_MODE, keySpec, new IvParameterSpec(ivParams));
    byte[] decryptedBytes = cipher.doFinal(decodedEncrypted);
    return new String(decryptedBytes);
  }

  public static void main(String[] args) throws GeneralSecurityException, UnsupportedEncodingException {
    String str ="vendor_id=INT_GTW&msg_code=KB0125&format=json&data={\"header\":{\"msg_code\":\"KB0125\",\"source\":\"ALLINCALL\",\"channel\":\"WHATSAPP\",\"txn_ref_number\":\"ALLINCALL_WHATSAPP_0001\",\"txn_datetime\":\"1510304150743\",\"ip\":\"10.10.1.19\",\"device_id\":\"XYWZPQR123\"},\"detail\":{\"entity_code\":\"KMBL\",\"appl_id\":\"6ad8818bd795971460b7a91723c211ef\",\"mode\":\"A\",\"mobile_no\":\"1111111111\",\"filler1\":\"\",\"filler2\":\"\",\"filler3\":\"\",\"filler4\":\"\",\"filler5\":\"\"}}";
    String key = "115f2538ee70d1d3212a61faa6761ade";
    String enc = encrypt(str, key);
    System.out.println(enc);
    String dec = decrypt(enc, key);
    System.out.println(dec);
  }

}