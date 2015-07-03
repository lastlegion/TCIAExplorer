import TciaExplorer


collections = (TciaExplorer.getCollections())
i=1
collectionHash = {}
for c in collections:
    print(str(i)+" "+ str(c["Collection"]))
    collectionHash[i] = c["Collection"]
    i+=1
collection = input("Enter the collection: ")
collection = (collectionHash[int(collection)])

patients = (TciaExplorer.getPatient(collection))

i=1
patientHash = {}
for p in patients:
    print(str(i)+" "+str(p["PatientName"]))
    patientHash[i] = p["PatientName"]
    i+=1
patient = input("Enter the patient: ")
patient = (patientHash[int(patient)])
print (patient)


patientStudy = TciaExplorer.getPatientStudy(patient)
patientStudyHash = {}
print(patientStudy)
i=1
for p in patientStudy:
    print(str(i) + " "+str(p["StudyInstanceUID"]))
    patientStudyHash[i] = p["StudyInstanceUID"]
    i+=1
#print (patientStudyHash)
patientStudy = input("Enter the study: ")
patientStudy = (patientStudyHash[int(patientStudy)])
print(patientStudy)


patientSeries = TciaExplorer.getSeries(patientStudy)
patientSeriesHash = {}
i=1
print (patientSeries)

for p in patientSeries:
    print(str(i) + " "+str(p["SeriesInstanceUID"]))
    patientSeriesHash[i] = p["SeriesInstanceUID"]
    i+=1
patientSeries = input("Enter the series: ")
patientSeries = patientSeriesHash[int(patientSeries)]
print(patientSeries)

images = TciaExplorer.getImage(patientSeries)
print(images)
fileName = input("Enter the filename to save: ")
f = open(fileName)
f.write(images.content)
f.close()


