import setting
import os
import requests
import json

CLIENTID = os.getenv("ClientID")
CLIENTSECRET = os.getenv("ClientSecret")


def jdoodle_compiler(code = 'Print("Helloworld")'):
    #python3 30
    language = 30

    try:
        compiler_url = "https://api.jdoodle.com/v1/execute"
        headers = {"content-type": "application/json"}
        data = {
            'script': code,
            'language': 'python3',
            'versionIndex': '0',
            'clientid': CLIENTID,
            'clientSecret': CLIENTSECRET,
        }

        r = requests.post(compiler_url, data=json.dumps(data), headers=headers)
        response = r.json()
        output = response['output']
        result = "Compilation Error"
        time = None
        mem = None

        if output:
                message = response['statusCode']
                if message == 200:
                    result = "Successfully Executed"
                    output = response['output']
                    time = response['cpuTime']
                    mem = response['memory']
                elif message != "200":
                    result = "Runtime Error"
                    output = response['error']
    except Exception as e:
        print(e)
        result ="Unable to make request!"
        print(result)
        time = None
        mem = None
    resp = {}
    resp['code'] = code
    resp['lang'] = int(language)
    resp['result'] = result
    resp['time'] = time
    resp['memory'] = mem
    #print(resp)
    #print(response)
    return resp, response

jdoodle_compiler("print(100+300)")
    
