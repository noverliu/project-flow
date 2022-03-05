import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings

base_url = settings.FLOWABLE_API['URL']
auth = HTTPBasicAuth(settings.FLOWABLE_API['AUTH']['USER'], settings.FLOWABLE_API['AUTH']['PWD'])

def startProcess(processId, requestId, vars=[]):
  data = {
    'processDefinitionId': processId,
    'variables': [
      *vars,
      {
        'name': 'requestId',
        'value': requestId
      } 
    ]
  }
  response = requests.post('%s/runtime/process-instances' % (base_url), json=data, verify=False, auth=auth)
  return response.json()
def getDefinitions(key):
  response = requests.get('%s/repository/process-definitions?key=%s&order=desc&sort=version' % (base_url, key), verify=False, auth=auth)
  return response.json()
