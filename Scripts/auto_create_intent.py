import xlrd 
import json
from EasyChatApp.models import *

loc = ("Intent.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

row = sheet.nrows
col = sheet.ncols
for i in range(2,row):
    question = sheet.cell_value(i,0)
    print(question) 
    variation= sheet.cell_value(i,1)
    answer_1 = json.dumps(sheet.cell_value(i,2))
    answer_2 = json.dumps(sheet.cell_value(i,3))
    answer_3 = json.dumps(sheet.cell_value(i,4)) 
    answer_4 = json.dumps(sheet.cell_value(i,5))
    answer_5 = json.dumps(sheet.cell_value(i,6))
    data_message = question.replace(" ","_")+'_message'
    api_name = question.replace(" ","_").replace("'","")+'_API'
    api_code = 'from EasyChatApp.utils import logger\nimport sys\ndef f():\n    ex = {\'AppName\': \'EasyChat\', \'user_id\': \'None\', \'source\': \'None\', \'channel\': \'None\', \'bot_id\': \'None\'}\n    response = {}\n    response[\'status_code\'] = 500\n    response[\'status_message\'] = \'Internal server error.\'\n    response[\'data\'] = {}\n    response[\'recommendations\'] = []\n    response[\'API_REQUEST_PACKET\'] = {\'url\':\'\'}\n    response[\'API_RESPONSE_PACKET\'] = {\'data\':\'\'}\n    try:\n        \n        a =  '+answer_1+' \n        b =  '+answer_2+'\n        c =  '+answer_3+'\n        d =  '+answer_4+'\n        e =  '+answer_5+'\n        \n        status = "{/kotak_811_status/}"\n        data = \'\'\n        if status == \'1\':\n            data = a\n        if status == \'2\':\n            data = b\n        if status == \'3\':\n            data = c\n        if status == \'4\':\n            data = d\n        if status == \'5\':\n            data = e\n        \n        response[\''+data_message+'\'] = data\n        response[\'status_code\'] = \'200\'\n        return response\n    except Exception as E:\n        exc_type, exc_obj, exc_tb = sys.exc_info()\n        logger.error(\''+api_name+': %s at %s\',str(E), str(exc_tb.tb_lineno), extra=ex)\n        response[\'status_code\'] = 500\n        response[\'status_message\'] = \'ERROR :-  \'+str(E)+ \' at line no: \' +str(exc_tb.tb_lineno)\n        return response\n'
    api_obj = ApiTree.objects.create(name=api_name, api_caller=api_code)
    text_response        = "{/"+data_message+"/}"
    intent_name          = question
    training_data = [ training.strip() for training in variation.split("$$$")]
    training_data.append(question)
    training_data_dict = {}
    for index, sentence in enumerate(training_data):
        training_data_dict[str(index)] = sentence
    training_data_dict = json.dumps(training_data_dict)
    
    bot_obj = Bot.objects.get(pk=1, is_deleted=False)
    intent_obj = Intent.objects.create(name=intent_name,training_data=training_data_dict)
    for channel in Channel.objects.all(): 
        intent_obj.channels.add(channel)
    intent_obj.bots.add(bot_obj)
    intent_obj.save()
    response_obj = BotResponse.objects.create()
    previous_tree_sentence = json.loads(response_obj.sentence)["items"]
    sentence_json = {
        "items": [
            {
            "text_response": text_response,
            "speech_response": text_response,
            "hinglish_response": text_response,
            "text_reprompt_response": text_response,
            "speech_reprompt_response": text_response,
            "tooltip_response": ""
        }]
    }
    modes = {
        "is_typable": "true",
        "is_button": "true",
        "is_slidable": "false",
        "is_date": "false",
        "is_dropdown": "false",
        "is_datepicker": "false",
        "auto_trigger_last_intent": "false",
        "is_attachment_required": "false",
        "is_single_datepicker": "false",
        "is_multi_datepicker": "false",
        "is_timepicker": "false",
        "is_single_timepicker": "false",
        "is_multi_timepicker": "false",
        "is_range_slider": "false",
        "is_radio_button": "false",
        "is_check_box": "false",
        "is_drop_down": "false",
        "is_video_recorder_allowed": "false"
    }
    modes_param = {
        "is_slidable": {"max": "","min": "","step": ""},
        "datepicker_list": [{"placeholder": "Date"}],
        "last_identified_intent": "",
        "choosen_file_type": "none"
    }
    response_obj.sentence = json.dumps(sentence_json)
    response_obj.modes = json.dumps(modes)
    response_obj.modes_param = json.dumps(modes_param)
    response_obj.save()
    intent_obj.tree.response = response_obj
    intent_obj.tree.name = intent_name
    intent_obj.tree.api_tree = api_obj
    intent_obj.tree.save()
    intent_obj.save()
