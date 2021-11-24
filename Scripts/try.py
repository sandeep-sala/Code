
number = "9925135992"

request_packet  = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <getProposal_cust xmlns="http://tempuri.org/">
            <strMobileNo>"""+ number +"""</strMobileNo>
            <strSource>SB!L!F@</strSource>
            <strAuthKey>SBI@@L!</strAuthKey>
            </getProposal_cust>
        </soap:Body>
    </soap:Envelope>"""

response_packet = ""







from requests import post