from tciaexplorer import TciaExplorer
import os
import json
import requests
api_key = os.getenv("TCIA_API_KEY")
#print (api_key)
tcia = TciaExplorer(api_key=api_key)
#print(tcia.get_collection_values().content)
#print(tcia.get_patient(collection="TCGA-GBM").content)
#print(tcia.get_patient_study(patientID="TCGA-VP-A87C").content)
#print(tcia.get_series(seriesInstanceUID="1.3.6.1.4.1.14519.5.2.1.7777.4006.246322038387835648676649859085"))

try:   
    collections = json.loads(tcia.get_collection_values().text)
except requests.exceptions.RequestException as e:    
    print(e)
    sys.exit(1)

i=1
collectionHash = {}
for c in collections:
    print(str(i)+" "+ str(c["Collection"]))
    collectionHash[i] = c["Collection"]
    i+=1
collection = input("Enter the collection: ")
collection = (collectionHash[int(collection)])
print ("Fetching patients for collection: "+ collection)

try:
    patients = json.loads(tcia.get_patient(collection=collection).text)
except requests.exceptions.RequestException as e:    
    print(e)
    sys.exit(1)

i=1
patientHash = {}
for p in patients:
    print(str(i)+" "+str(p["PatientName"]))
    patientHash[i] = p["PatientName"]
    i+=1
patient = input("Enter the patient: ")
patient = (patientHash[int(patient)])
print (patient)

try:
    patientStudy  = json.loads(tcia.get_patient_study(patientID=patient).text)
except requests.exceptions.RequestException as e:    
    print(e)
    sys.exit(1)


patientStudyHash = {}
i=1
for p in patientStudy:
    print(str(i) + " "+str(p["StudyInstanceUID"]))
    patientStudyHash[i] = p["StudyInstanceUID"]
    i+=1
#print (patientStudyHash)
patientStudy = input("Enter the study: ")
patientStudy = (patientStudyHash[int(patientStudy)])
print(patientStudy)

try:
    patientSeries = json.loads(tcia.get_series(studyInstanceUID=patientStudy).text)
except requests.exceptions.RequestException as e:    
    print(e)
    sys.exit(1)

patientSeriesHash = {}
i=1

for p in patientSeries:
    print(str(i) + " "+str(p["SeriesInstanceUID"]))
    patientSeriesHash[i] = p["SeriesInstanceUID"]
    i+=1
patientSeries = input("Enter the series: ")
patientSeries = patientSeriesHash[int(patientSeries)]
print(patientSeries)


try:
    images = (tcia.get_image(seriesInstanceUID=patientSeries))
except requests.exceptions.RequestException as e:    
    print(e)
    sys.exit(1)

print(images)
fileName = input("Enter the filename to save: ")
f = open(fileName, "wb")
f.write(images.content)
f.close()


