# Author       : Sandeep Sala
# Last Updated : 11/05/2020 03:02 PM

from EasyChatApp.utils import logger as log
import sys,requests,json,re,xmltodict

def f():
    '''
        API TREE FUNCTION 
        Dict Variable 'r' is the default response,
        Do not Replace r.
    '''
    log.info("Execution of FunctionName STARTS")
    r = {
        'status_code'          : 500,
        'status_message'       : 'Internal server error.' ,
        'cards'                : [],
        'choices'              : [],
        'images'               : [],
        'videos'               : [],
        'recommendations'      : [],
        'API_REQUEST_PACKET'   : {"url"         : ""},
        'API_RESPONSE_PACKET'  : {"respone_data": ""} 
    }
    try:
        # Necessary Variable STARTS
        # Necessary Variable ENDS

        # API Calls STARTS
        URL      = "https://www.colive.in/webservices/api/Reports/GetReceiptDetails"
        PAYLOAD  = json.dumps({"CustomerID" : CustomerID})
        HEADER   = {"Content-Type":"application/json","auth_id":"8E8CA351-110E-4272-8A15-DD26E3B3E8C5"}
        DATA     = requests.post(url=URL,headers=HEADER,data=PAYLOAD,timeout=15).json()
        r['API_REQUEST_PACKET'].update({"url":URL,"header":HEADER,"payload":PAYLOAD})
        r['API_RESPONSE_PACKET'].update({"respone_data":DATA})
        # API Calls ENDS

        # Logic STARTS
        # Logic ENDS

        r['status_code'] = 200
        log.info("Execution of FunctionName ENDS")
        return r
    except Exception as e:
        error_msg = f'ERROR [{str(e)}] at-line-no [{sys.exc_info()[2].tb_lineno}] in FunctionName'
        r.update({'status_code':500,'status_message':error_msg})
        log.error(error_msg)
        return r