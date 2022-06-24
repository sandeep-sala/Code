from CampaignApp.utils import *
from CampaignApp.models import *
from django.conf import settings
from CampaignApp.utils_custom_encryption import CustomEncrypt
import json
import sys
import requests
import base64

API_DOMAIN = 'https://medops.ameyo.net:2204'
API_USERNAME = 'admin'
API_PASSWORD = 'Ameyo@1234'
API_NAMESPACE = 'bff644be_1cb3_4624_99dc_9e90cff86d2e'
EX = {'AppName': 'Campaign'}


def get_jwt_token(username, password):
    API_KEY = "eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE2NDM3MjExNzgsImV4cCI6MTY0NDMyNTk3OCwid2E6cmFuZCI6IjVmZDlhOGM4OGU5Yjc4MzUwMjgyNTczMGU1NDViZmZmIn0.D7ZqAGCioNVHGl1pOMYy9jW-UujNKakuXLq-zZpN5Oc"
    try:
        logger.info("Inside get_jwt_token", extra=EX)
        url = API_DOMAIN + "/v1/users/login"
        userAndPass = base64.b64encode(
            (username+":"+password).encode()).decode("ascii")
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic '+userAndPass
        }
        logger.info("AMEYO_GET_API_KEY Headers: %s", str(headers), extra=EX)
        r = requests.post(url=url, headers=headers, timeout=25, verify=True)
        content = json.loads(r.text)
        logger.info("AMEYO_GET_API_KEY Response: %s", str(content), extra=EX)
        if str(r.status_code) == "200":
            if "users" in content and content["users"] != []:
                API_KEY = content["users"][0]["token"]
        logger.info("AMEYO_GET_API_KEY API Key generated: %s",
                    str(API_KEY), extra=EX)
    except requests.Timeout as RT:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("AMEYO_GET_API_KEY Timeout error: %s at %s",
                     str(RT), str(exc_tb.tb_lineno), extra=EX)
    except Exception as E:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("AMEYO_GET_API_KEY Failed: %s at %s",
                     str(E), str(exc_tb.tb_lineno), extra=EX)
    return API_KEY


def get_payload_body(variable):
    try:
        body = []
        for value in variable:
            body.append({'text': value})
        return body
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("Error: get_payload_body: %s for %s", str(
            e), str(exc_tb.tb_lineno), extra=EX)


def getTextPayload(mobile_number, template_name, language, variables, language_policy="deterministic", namespace=API_NAMESPACE):
    try:
        logger.info("Inside getTextPayload", extra=EX)
        payload = {
            "to": mobile_number,
            "type": "template",
            "template": {
                "namespace": namespace,
                "name": template_name,
                "language": {
                    "policy": language_policy,
                    "code": language
                }
            }
        }
        if len(variables) != 0:
            payload['template']['components'] = []
            param_dict = {"type": "body", "parameters": []}
            for var in variables:
                if var.strip() != "":
                    var_dict = {}
                    var_dict["type"] = "text"
                    var_dict["text"] = var
                    param_dict["parameters"].append(var_dict)
            payload['template']['components'].append(param_dict)
        logger.info("TextPayload: %s", str(payload), extra=EX)
        return json.dumps(payload)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("Error: gettextPayload: %s for %s", str(
            e), str(exc_tb.tb_lineno), extra=EX)


def getImagePayload(mobile_number, template_name, language, variable, link):
    try:
        logger.info("Inside getImagePayload", extra=EX)
        payload = {
            "phone": mobile_number,
            "extra": "na",
            "media": {
                "type": "media_template",
                "template_name": template_name,
                "lang_code": language,
                "header": [
                    {
                        "image": {
                            "link": link,
                        }
                    }
                ],
            }
        }
        if len(variable) != 0:
            payload['media']['body'] = get_payload_body(variable)
        logger.info(payload, extra=EX)
        return json.dumps(payload)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("Error: getImagePayload: %s for %s", str(
            e), str(exc_tb.tb_lineno), extra=EX)


def getVideoPayload(mobile_number, template_name, language, variable, link):
    try:
        logger.info("Inside getVideoPayload", extra=EX)
        payload = {
            "phone": mobile_number,
            "extra": "na",
            "media": {
                "type": "media_template",
                "template_name": template_name,
                "lang_code": language,
                "header": [
                    {
                        "video": {
                            "link": link,
                        }
                    }
                ],
            }
        }
        if len(variable) != 0:
            payload['media']['body'] = get_payload_body(variable)
        logger.info(payload, extra=EX)
        return json.dumps(payload)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("Error: getVideoPayload: %s for %s", str(
            e), str(exc_tb.tb_lineno), extra=EX)


def getDocumentPayload(mobile_number, template_name, language, variables, link, language_policy="deterministic", namespace=API_NAMESPACE, media_type='document'):
    try:
        logger.info("inside getMediaPayload", extra=EX)
        payload = {
            "to": mobile_number,
            "type": "template",
            "template": {
                "namespace": namespace,
                "name": template_name,
                "language": {
                    "policy": language_policy,
                    "code": language
                },
                "components": [
                    {
                        "type": "header",
                        "parameters": [
                            {
                                "type": media_type,
                                media_type: {
                                    "link": link
                                }
                            }
                        ]
                    }
                ]
            }
        }
        if len(variables) != 0:
            param_dict = {"type": "body", "parameters": []}
            for var in variables:
                if var.strip() != "":
                    var_dict = {}
                    var_dict["type"] = "text"
                    var_dict["text"] = var
                    param_dict["parameters"].append(var_dict)
            payload['template']['components'].append(param_dict)
        logger.info("getMediaPayload: %s", str(payload), extra=EX)
        return json.dumps(payload)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("Error: getMediaPayload: %s for %s", str(e),
                     str(exc_tb.tb_lineno), extra=EX)


def getQuickReplyPayload(mobile_number, template_name, language, variable, media_link, namespace=API_NAMESPACE):
    try:
        logger.info("Inside getQuickReplyPayload", extra=EX)
        variable_payload = []
        for item in variable:
            temp_dict = {"type": "text", "text": item}
            variable_payload.append(temp_dict)
        payload = {
            "to": mobile_number,
            "type": "template",
            "template": {
                    "namespace": namespace,
                    "name": template_name,
                    "language": {
                        "policy": "deterministic",
                        "code": language
                    },
                "components": [
                        {
                            "type": "button",
                            "sub_type": "quick_reply",
                            "index": "1",
                            "parameters": [
                                    {
                                        "type": "payload",
                                        "payload": ""
                                    }
                            ]
                        }
                        ],
                "components": [
                        {
                            "type": "body",
                            "parameters": variable_payload
                        }
                        ]
            }
        }
        logger.info("getQuickReplyPayload: %s", str(payload), extra=EX)
        return json.dumps(payload)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("Error: getQuickReplyPayload: %s for %s", str(
            e), str(exc_tb.tb_lineno), extra=EX)


"""
def getCTAPayload(mobile_number, template_name, language, variables, cta_variables=[], media_type="", media_link="", language_policy="deterministic", namespace=API_NAMESPACE):
    try:
        logger.info("Inside getCTAPayload", extra=EX)
        payload = {
            "to": mobile_number,
            "type": "template",
            "template": {
                "namespace": namespace,
                "name": template_name,
                "language": {
                    "policy": language_policy,
                    "code": language
                }
            }
        }
        is_cta_media = False
        if media_type != "" and media_type.lower() in ["image", "video", "document"] and media_link != "":
            is_cta_media = True
        if len(variables) != 0 or len(cta_variables) != 0 or is_cta_media == True:
            payload['template']['components'] = []
            if len(variables) != 0:
                param_dict = {"type": "header", "parameters": []}
                for var in variables:
                    if var.strip() != "":
                        var_dict = {}
                        var_dict["type"] = "text"
                        var_dict["text"] = var
                        param_dict["parameters"].append(var_dict)
                payload['template']['components'].append(param_dict)
            if len(cta_variables) != 0:
                cta_count = 1
                for cta_var in cta_variables:
                    param_dict = {
                        "type": "button",
                        "sub_type": "url",
                        "index": cta_count,
                        "parameters": [
                                {
                                    "type": "text",
                                    "text": cta_var
                                }
                        ]
                    }
                    payload['template']['components'].append(param_dict)
                    cta_count += 1
            if is_cta_media == True:
                param_dict = {
                    "type": "header",
                    "parameters": [
                            {
                                "type": media_type,
                                media_type: {
                                    "link": media_link
                                }
                            }
                    ]
                }
                payload['template']['components'].append(param_dict)
        logger.info("getCTAPayload: %s", str(payload), extra=EX)
        return json.dumps(payload)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("Error: getCTAPayload: %s for %s", str(e),
                     str(exc_tb.tb_lineno), extra=EX)
"""


def getCTAPayload(mobile_number, template_name, language, variables, cta_variables=[], media_type="", media_link="", language_policy="deterministic", namespace=API_NAMESPACE):
    try:
        logger.info("Inside getCTAPayload", extra=EX)
        if len(variables) < 3:
            variables = ["name", "enquired_about", "site_visit_link"]

        payload = {
            "to": mobile_number,
            "type": "template",
            "template": {
                "namespace": namespace,
                "name": template_name,
                "language": {
                    "policy": language_policy,
                    "code": language
                },
                "components": [
                    {
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "text": variables[0]
                            },
                            {
                                "type": "text",
                                "text": variables[1]
                            }
                        ]
                    },
                    {
                        "type": "button",
                        "sub_type": "url",
                        "index": "0",
                        "parameters": [
                            {
                                "type": "text",
                                "text": variables[2]
                            }
                        ]
                    },
                    {
                        "type": "text",
                        "sub_type": "quick_reply"
                    }
                ]
            }
        }

        logger.info("getCTAPayload: %s", str(payload), extra=EX)
        return json.dumps(payload)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("Error: getCTAPayload: %s for %s", str(e),
                     str(exc_tb.tb_lineno), extra=EX)


def sendWhatsAppMessage(payload, api_key):
    try:
        JWT_TOKEN = api_key
        url = API_DOMAIN + "/v1/messages"
        headers = {
            "Authorization": "Bearer " + JWT_TOKEN,
            "Content-Type": "application/json"
        }
        logger.info(payload, extra=EX)
        resp = requests.post(url=url, data=payload, headers=headers)
        resp = json.loads(resp.text)
        logger.info(resp, extra=EX)
        if "messages" in resp and resp["messages"][0] and "id" in resp["messages"][0]:
            resp["request_id"] = resp["messages"][0]["id"]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("Error: sendWhatsAppMessage: %s for %s", str(
            e), str(exc_tb.tb_lineno), extra=EX)
    return resp


def check_mobile_number_capability(JWT_TOKEN, mobile_number):
    capable = False
    check_success = False
    try:
        url = API_DOMAIN + "/v1/contacts"
        payload = {
            "blocking": "wait",
            "contacts": [
                "+"+mobile_number
            ],
            "force_check": False
        }
        headers = {
            "Authorization": "Bearer " + JWT_TOKEN,
            "Content-Type": "application/json"
        }
        logger.info("check_mobile_number_capability URL: ",
                    str(url), extra=EX)
        logger.info("check_mobile_number_capability Headers: ",
                    str(headers), extra=EX)
        logger.info("check_mobile_number_capability Payload: ",
                    str(payload), extra=EX)
        resp = requests.post(url=url, data=json.dumps(
            payload), headers=headers, timeout=20)
        logger.info("check_mobile_number_capability Response: ",
                    str(resp.text), extra=EX)

        if str(resp.status_code) == "200":
            resp = json.loads(resp.text)
            if "contacts" in resp and resp["contacts"] != []:
                contact_details = resp["contacts"][0]
                check_success = True
                if contact_details["status"] == "valid" and "wa_id" in contact_details:
                    mobile_number = contact_details["wa_id"]
                    capable = True

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("Error: check_mobile_number_capability: %s for %s", str(
            e), str(exc_tb.tb_lineno), extra=EX)
    return mobile_number, capable, check_success


def f(x):
    '''
    Format of x:
    x = {
        "mobile_number": '',
        "template": {
            'name': '',
            'type': '',
            'message':'',
            'language': '',
            'link': '',
            'cta_text': ''.
            'cta_link': '',
        },
        "user_details" : [],
        "variables": [],
    }
    '''

    response = {}
    response['status'] = 500
    response['status_message'] = 'Your request was not executed successfully. Please try again later.'
    try:
        x = json.loads(x)

        if bool(x):
            variable = x['variables']
            EX = {'AppName': 'EasyChat', 'user_id': 'None',
                  'source': 'en', 'channel': 'WhatsApp', 'bot_id': 'None'}
            phone_number = str(x['mobile_number'])
            phone_number = phone_number[-10:]
            phone_number = "91" + str(phone_number)

            api_key = get_jwt_token(API_USERNAME, API_PASSWORD)

            logger.info('phone_number: %s', str(phone_number), extra=EX)
            phone_number, capable, check_success = check_mobile_number_capability(
                api_key, phone_number)
            if check_success == False:
                response["status_message"] = "Failed to check mobile number capability. Please report this error."
                return response
            else:
                if capable == False:
                    response["status_code"] = 403
                    response["status_message"] = "Mobile Number not available on WhatsApp to receive the message."
                    return response
            logger.info('phone_number: %s', str(phone_number), extra=EX)
            payload = getTextPayload(
                phone_number, x['template']['name'], x['template']['language'], variable)
            if 'image' in x['template']['type'].lower():
                payload = getImagePayload(
                    phone_number, x['template']['name'], x['template']['language'], variable, x['template']['link'])
            elif 'document' in x['template']['type'].lower():
                payload = getDocumentPayload(
                    phone_number, x['template']['name'], x['template']['language'], variable, x['template']['link'])
            elif 'quick reply' in x['template']['type'].lower():
                payload = getQuickReplyPayload(
                    phone_number, x['template']['name'], x['template']['language'], variable, x['template']['link'])
            elif 'call to action' in x['template']['type'].lower():
                # variable = ["name","enquired_about","site_visit_link"]
                payload = getCTAPayload(
                    phone_number, x['template']['name'], x['template']['language'], variable)
                #payload = getCTAPayload(phone_number, x['template']['name'], x['template']['language'], variable, cta_variables)
        response['request'] = payload
        logger.info(payload, extra=EX)
        response['response'] = sendWhatsAppMessage(payload, api_key)
        response['status'] = 200
        response['status_message'] = 'success'
        return response
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("Inside api integration code: %s at %s",
                     str(e), str(exc_tb.tb_lineno), extra=EX)
        response['status_message'] = 'ERROR :-  ' + \
            str(e) + ' at line no: ' + str(exc_tb.tb_lineno)
        response['response'] = {'status': 'failed'}

    return response
