# Author       : Sandeep Sala
# Last Updated : 23/04/2020 06:00 AM

from EasyChatApp.utils import logger as log
import sys,requests as req,json

def f(message):
    '''
        PIPE PROCESSOR FUNCTION 
        Dict Variable 'r' is the default response,Do not Replace r.
    '''
    log.info("Execution of FunctionName STARTS")
    r = {
        'status_code'           : '500',
        'status_message'        : 'Internal server error.' ,
        'data'                  : {},
        'recur_flag'            : False,
        'message'               : '',
        'API_REQUEST_PACKET'    : {"url"         : ""}, 
        'API_RESPONSE_PACKET'   : {"respone_data": ""} 
    }
    try:
        # Necessary Variable STARTS
        message = message.split("|")[-2].lower()
        # Necessary Variable ENDS

        # API Calls STARTS
        # API Calls ENDS

        # Logic STARTS
        # Logic ENDS

        r['recur_flag'] = True
        r['data'] = {}
        r['status_code'] = '200'
        log.info("Execution of FunctionName ENDS")
        return r
    except Exception as e:
        error_msg = f'ERROR [{str(e)}] at-line-no [{sys.exc_info()[2].tb_lineno}] in FunctionName'
        r.update({'status_code': '500', 'status_message': error_msg})
        log.error(error_msg)
        return r