from tciaexplorer import TciaExplorer
import os
import json
import requests
import sys

api_key = os.getenv("TCIA_API_KEY")

tcia = TciaExplorer(api_key=api_key) #set api_key

def processInput(inhash, req):
    key = str(raw_input("Enter the Sno or "+str(req)+": "))
    if key in inhash:
        out = inhash[key]
        return out
    else:
        print("Invalid "+str(req))
        print("Try again")
        processInput(inhash, req)

def buildHash(attribute, data):
    _hash = {}
    print("Sno. \t"+attribute)
    i=1
    for row in data:
        print(str(i) + "\t"+str(row[attribute]))
        _hash[str(i)] = row[attribute]
        _hash[row[attribute]] = row[attribute]
        i+=1
    return _hash

######Fetch collections############
try:
    collections = json.loads(tcia.get_collection_values().text)
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)

collectionHash = buildHash("Collection", collections)
collection = processInput(collectionHash, "Collection")

print ("Fetching patients for collection: "+ collection)

############Fetch Patients#############
try:
    patients = json.loads(tcia.get_patient(collection=collection).text)
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)

patientHash = buildHash("PatientName", patients)
patient = processInput(patientHash, "PatientID")
print ("Fetching study for patientID: "+patient)


###################Fetch study###############
try:
    patientStudy  = json.loads(tcia.get_patient_study(patientID=patient).text)
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)

patientStudyHash = buildHash("StudyInstanceUID", patientStudy)
patientStudy = processInput(patientStudyHash, "studyInstanceUID")
print("Fetching series for the studyInstanceUID: "+ patientStudy)

##########Fetch series#############3

try:
    patientSeries = json.loads(tcia.get_series(studyInstanceUID=patientStudy).text)
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)

patientSeriesHash = buildHash("SeriesInstanceUID", patientSeries)
patientSeries = processInput(patientSeriesHash, "seriesInstanceUID")
print("Fetching images for the seriesInstanceUID: "+patientSeries)

##################Fetch images#############
try:
    images = (tcia.get_image(seriesInstanceUID=patientSeries))
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)

#print(images)
fileName = str(raw_input("Enter the filename to save: "))
f = open(fileName+".zip", "wb")
f.write(images.content)
f.close()


