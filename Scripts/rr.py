from EasyChatApp.utils import logger
# from django.utils.encoding import smart_str, smart_unicode
import requests
import sys
import xmltodict
import json
import ast
import re
exc_type, exc_obj, exc_tb = sys.exc_info()

def f(x):
    json_response = {}
    json_response["status_code"]="500"
    json_response["cards"]=
    json_response["status_message"]="Internal Server Error"
    json_response["data"]={"alert_message":"Internal Server Error"}
    
    try:
        location = "{/google_home_location/}"
        strs = location.replace("'",'"')
        loc = json.loads(strs.replace('u',''))
        user_pincode = loc["zipCode"]
        
        url="https://online.bharti-axalife.com/MiscServices/PolicyAuthenticationWebService/PolicyAuthenticationWebService.svc"
        headers = {'content-type': 'text/xml', 'SOAPAction':'http://tempuri.org/IPolicyAuthenticationWebService/GetBranchDetails'}
        body = """<?xml version="1.0" encoding="UTF-8"?>
                 <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/" xmlns:pol="http://schemas.datacontract.org/2004/07/PolicyAuthenticationWebService">
                <soapenv:Header/>
                  <soapenv:Body>
                    <tem:GetBranchDetails>
                      <!--Optional:-->
                      <tem:objBranchDetailsListRequest>
                        <!--Optional:-->
                        <pol:PartnerKey>WHTSAPP01CH7</pol:PartnerKey>
                        <!--Optional:-->
                        <pol:BranchPin>"""+user_pincode+"""</pol:BranchPin>
                        <!--Optional:-->
                        <pol:CityName></pol:CityName>
                      </tem:objBranchDetailsListRequest>
                    </tem:GetBranchDetails>
                  </soapenv:Body>
                </soapenv:Envelope>"""
                
        r = requests.post(url = url,data=body,headers=headers)
        k = ((r.content).decode("utf-8")).replace("\xa0","").replace("\xc2","")
        data = xmltodict.parse(k)["s:Envelope"]["s:Body"]
        json_data = json.loads(json.dumps(data,indent=4))
        if (json_data["GetBranchDetailsResponse"]["GetBranchDetailsResult"]["a:ErrorCode"] == "000"):
            branchdetails = (json_data["GetBranchDetailsResponse"]["GetBranchDetailsResult"]["a:BranchDetailsList"]["a:BranchDetails"])
            branchlist = []
            if(type(branchdetails) == dict):
                branchname = branchdetails['a:BranchName']
                branchadd = branchdetails['a:BranchAddress']
                map_location = "https://www.google.com/maps/search/"+branchname+","+branchadd
                branchlist.append({"title": branchname,"img_url":"https://www.bharti-axagi.co.in/sites/default/files/bagi_logo.png","link": map_location,"content": branchadd})
                json_response["data"]={"alert_message":"We found following branch nearby"}
                
            elif(type(branchdetails)== list):
                for branch in branchdetails:
                    branchname = str(branch['a:BranchName'])
                    branchadd = str(branch['a:BranchAddress'])
                    map_location = "https://www.google.com/maps/search/"+branchname+","+branchadd
                    branchlist.append({"title": branchname,"img_url":"https://www.bharti-axagi.co.in/sites/default/files/bagi_logo.png","link": map_location ,"content": branchadd})
                json_response["data"]={"alert_message":"We found following branches nearby"}
                
            json_response["data"]["branchcards"] = branchlist
            
        elif (json_data["GetBranchDetailsResponse"]["GetBranchDetailsResult"]["a:ErrorCode"] == "030"):
            # message = json_data["GetBranchDetailsResponse"]["GetBranchDetailsResult"]["a:ErrorDesc"]
            json_response["data"]={"alert_message":"We do not provide service in this location"}
            json_response["data"]["branchcards"] = []
            
        json_response["status_code"]="200"
        json_response["status_message"]="SUCCESS"
        return json_response
    except Exception as e:
        logger.error("Error %s at %s", str(e), str(exc_tb.tb_lineno))
        return json_response