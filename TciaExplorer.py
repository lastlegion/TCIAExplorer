import requests
import json

api_key = "16ade9bc-f2fa-4a37-b357-36466a0020fc"
baseUrl="https://services.cancerimagingarchive.net/services/v3"
resource = "TCIA"

base = baseUrl + "/"+resource+ "/query/"

def getCollections():
    response = requests.get(base+ "getCollectionValues", headers={"api_key": api_key})
    print(response)
    return json.loads((response.text))

def getPatient(collection):
    payload= {"api_key": api_key, "Collection": collection}
    response = requests.get(base+"getPatient", params=payload)
    return json.loads(response.text)

def getPatientStudy(patientId):
    payload = {"api_key": api_key, "PatientID": patientId}
    response = requests.get(base+"getPatientStudy", params=payload)
    return json.loads(response.text)


def getSeries(studyInstanceUid):
    payload = {"api_key": api_key, "StudyInstanceUID": studyInstanceUid}
    response  = requests.get(base+"getSeries", params=payload)
    return json.loads(response.text)

def getImage(seriesInstanceUid):
    payload = {"api_key": api_key, "SeriesInstanceUID": seriesInstanceUid}
    response = requests.get(base + "getImage", params=payload)
    return response
