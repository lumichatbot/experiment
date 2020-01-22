TRANSLATE_URL = 'http://0.0.0.0:5000/webhook'
DEPLOY_URL = 'http://172.17.0.2:5000/deploy'

TRANSLATE_API_TEMPLATE = '''{
  "id": "28419e8b-2ce2-4587-84b2-98be5c49739d",
  "timestamp": "2018-05-29T18:39:06.145Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "#INTENT_TEXT",
    "action": "input.nile",
    "actionIncomplete": false,
    "parameters": {
      "origin": "#ORIGIN",
      "destination": "#DESTINATION",
      "policy-target": [],
      "security-level": "",
      "middlebox": [
        #MIDDLEBOXES
      ]
    },
    "contexts": [],
    "metadata": {
      "intentId": "64cdfdeb-18dd-4c76-be0a-4b55021ad1eb",
      "webhookUsed": "true",
      "webhookForSlotFillingUsed": "false",
      "endConversation": true,
      "webhookResponseTime": 203,
      "intentName": "Waypoint Intent"
    },
    "fulfillment": {
      "speech": "",
      "messages": [
        {
          "type": 0,
          "speech": ""
        }
      ]
    },
    "score": 0.7900000214576721
  },
  "status": {
    "code": 200,
    "webhookTimedOut": false
  },
  "sessionId": "493f83f0-6fab-429b-ba95-104eeb316cd9"
}'''

DEPLOY_API_TEMPLATE = '''{
  "id": "28419e8b-2ce2-4587-84b2-98be5c49739d",
  "timestamp": "2018-02-28T18:39:06.145Z",
  "intent": "#INTENT_NILE"
}'''
