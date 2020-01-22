import requests
import datetime
import time

from config import *

TEST_CASE = {
    "intent_text": "Hey Lumi, please add firewall from client to server",
    "origin": "client",
    "destination": "server",
    "middleboxes": ["\"firewall\""]
}

if __name__ == "__main__":
    # test case one
    translate_test = TRANSLATE_API_TEMPLATE.replace("#INTENT_TEXT", TEST_CASE['intent_text'])
    translate_test = translate_test.replace("#ORIGIN", TEST_CASE['origin'])
    translate_test = translate_test.replace("#DESTINATION", TEST_CASE['destination'])
    translate_test = translate_test.replace("#MIDDLEBOXES", ','.join(TEST_CASE['middleboxes']))

    response = requests.post(TRANSLATE_URL, data=translate_test)
    reponse_obj = response.json()
    nile_program = reponse_obj['data']
    nile_filename = 'res/nile/{}_nile.nil'.format(
        datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S'))
    with open(nile_filename, 'w') as nile_file:
        nile_file.write(nile_program)

    deploy_test = DEPLOY_API_TEMPLATE.replace("#INTENT_NILE", nile_program)
    response = requests.post(DEPLOY_URL, data=deploy_test)
    reponse_obj = response.json()
    sonata_script = reponse_obj['output']['policy']
    script_filename = 'res/sonata/{}_sonata.sh'.format(
        datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S'))
    with open(script_filename, 'w') as script:
        script.write(sonata_script)
