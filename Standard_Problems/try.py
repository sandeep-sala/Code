import requests as req
import json

import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'x-ms-client-request-id': '',
    'Content-Type': 'multipart/form-data',
    'Ocp-Apim-Subscription-Key': '1e4828c298fb4c76aa6d0c5140cb4da7',
}

params = urllib.parse.urlencode({
    # Request parameters
    'privacy': 'Private',
    'priority': '',
    'description': '',
    'partition': '',
    'externalId': '',
    'externalUrl': '',
    'callbackUrl': '',
    'metadata': '',
    'language': '',
    'videoUrl': 'https://doc-0k-8k-docs.googleusercontent.com/docs/securesc/8gbd5e40o13g55gcu8j0lurb7bis03cc/f1ta78c25ni2gh0l9528bunfr56kdu8k/1587566850000/09767907814616499229/11225790333136774020/1Y-Jf7A5s_dfu-11D0MsEg7l_iXfYF3Ro?e=download&authuser=1&nonce=mrlr9oo5otf5k&user=11225790333136774020&hash=khtja34907rbgo0on5bmiubk7f612jo5',
    'fileName': 'dasda',
    'indexingPreset': 'Default',
    'streamingPreset': 'Default',
    'linguisticModelId': '',
    'personModelId': '',
    'animationModelId': '',
    'sendSuccessEmail': 'False',
    'assetId': '',
    'brandsCategories': '',
    'accessToken': '',
})

conn = http.client.HTTPSConnection('api.videoindexer.ai')
conn.request("POST", "https://api.videoindexer.ai/southeastasia/Accounts/90dd7baf-2272-488a-b008-8292a74291b3/Videos?name={name}&%s" % params, "{body}", headers)
response = conn.getresponse()
data = response.read()
print(data)
conn.close()
