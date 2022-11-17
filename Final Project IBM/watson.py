import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('nbPZzv8SUFp7DJWPMWSOl4qS2n1kZBCKajJslWE8od21')
assistant = AssistantV2(
    version="2022-11-03",
    authenticator=authenticator
)
assistant.set_service_url("https://api.us-south.assistant.watson.cloud.ibm.com")
session = assistant.create_session("4ec44adc-1174-45c0-a989-515faa25e696").get_result()
session_json = json.dumps(session,indent=2)
session_dict = json.loads(session_json)
session_id = session_dict['session_id']
print(session_id)

# assistant.delete_session("4ec44adc-1174-45c0-a989-515faa25e696",session_id).get_result()
# print("Session Delete")

message = assistant.message(
    "4ec44adc-1174-45c0-a989-515faa25e696",
    session_id,
    input={'text':'I WANT A JOB'},
    context={
        'metadata':{
            'deployment':'Mydeployment'
        }
    }
).get_result()

print(json.dumps(message,indent=2)) 