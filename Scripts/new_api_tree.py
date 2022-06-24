from EasyChatApp.models import * 
result_dict = {}
try:
    common_utils_obj = CommonUtilsFile.objects.filter(bot=Bot.objects.get(pk=4))
    exec(str(common_utils_obj[0].code), result_dict) 
except Exception:
    pass
from EasyChatApp.utils import logger as log
import sys
import requests
import json


def f():
    '''
        API TREE FUNCTION
        Author       : Sandeep Sala
        Last Updated : 21/06/2022
        Response
            200: This status code represents the "SUCCESS".
            206: This status code is used to "REDIRECT" the flow to same intent.
            308: This status code is used to search the reponse in all existing intents. If no intent found then it will reprompt the same intent, otherwise it will proceed with the new flow.
            400: If you are using any external API and external API fails then you have to use this status code.
            500: This status code represents the "Internal server error".
        Status message is based status code.
            200: "SUCCESS".
            206: "REDIRECT".
            308: "REDIRECT"
            400: "External API failure."
    '''
    global result_dict
    EX = {'AppName': 'EasyChat', 'user_id': 'None',
          'source': 'None', 'channel': 'None', 'bot_id': 'None'}
    FN = "renderCityAPItree"
    r = {
        'status_code': 500,
        'status_message': 'Internal server error.',
        'cards': [], # [{"title": title, "content": content, "link": link, "img_url": img_url}, {"title": title1, "content": content1, "link": link1, "img_url": img_url1}]
        'choices': [], # [{"display": display, "value": value}, {"display": display1, "value": value1}]
        'images': [], # ["image_link1", "image_link2"]
        'videos': [], # ["video_link1", "video_link2"]
        'recommendations': [], # ["hi", "bye", "good night"]
        'data': {},  #e {"key1": value1, "key2": value2, "is_cache": True}
        'dynamic_widget_type': {},
        'modes': {},
        'modes_param': {},
        'API_REQUEST_PACKET': {'url': '', 'data': '', 'header': ''},
        'API_RESPONSE_PACKET': {'response': ''}
    }
    try:
        log.info(f'Execution of {FN} STARTS', extra=EX)
        # Necessary Variable STARTS

        user_mobile = '{/user_mobile/}'
        # Necessary Variable ENDS

        # API Calls STARTS
        URL = f'https://medfin.mocklab.io/cogno-bot/render-data?mobile={user_mobile}&conversationId=hd83hd8e&workflow=bookAppoinment&event=renderCity&query='
        DATA = requests.get(url=URL, timeout=5)
        r['API_REQUEST_PACKET'].update({'url': URL})
        r['API_RESPONSE_PACKET'].update({'response': DATA})
        # API Calls ENDS

        # Logic STARTS
        # Logic ENDS

        r['status_code'] = 200
        r['status_message'] = 'SUCCESS'
        log.info(f"Execution of {FN} ENDS", extra=EX)
        return r
    except Exception as e:
        error_msg = f'ERROR [{str(e)}] at-line-no [{sys.exc_info()[2].tb_lineno}] in FN'
        r.update({'status_code': 500, 'status_message': error_msg})
        log.error(error_msg, extra=EX)
        return r
