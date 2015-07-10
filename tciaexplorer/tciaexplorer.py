import requests
import json


class TciaExplorer:
    GET_IMAGE = "getImage"
    GET_MANUFACTURER_VALUES = "getManufacturerValues"
    GET_MODALITY_VALUES = "getModalityValues"
    GET_COLLECTION_VALUES = "getCollectionValues"
    GET_BODY_PART_VALUES = "getBodyPartValues"
    GET_PATIENT_STUDY = "getPatientStudy"
    GET_SERIES = "getSeries"
    GET_PATIENT = "getPatient"
    GET_SERIES_SIZE = "getSeriesSize"
    CONTENTS_BY_NAME = "ContentsByName"

    def __init__(self, api_key, baseUrl="https://services.cancerimagingarchive.net/services/v3", resource="TCIA"):
        self.api_key = api_key
        self.baseUrl = baseUrl + "/"+resource+"/query/"

    def parse_params(self, params):
        req_params = dict((k,v) for k,v in params.items() if v)
        return req_params

    def get_collection_values(self, format="json"):
        params={"format":format, "api_key": self.api_key}
        payload = self.parse_params(params)
        response = requests.get(self.baseUrl+ self.GET_COLLECTION_VALUES, params=payload)
        return response

    def get_patient(self,collection=None, format="json"):
        params = {"Collection":collection, "api_key": self.api_key, "format": format}
        payload = self.parse_params(params)
        response = requests.get(self.baseUrl+ self.GET_PATIENT, params=payload)
        return response

    def get_patient_study(self, patientID=None,collection=None,studyinstanceUID=None, format="json"):
        params = {"Collection": collection, "PatientID": patientID, "StudyInstanceUID": studyinstanceUID, "api_key": self.api_key, "format":format}
        payload = self.parse_params(params)
        response = requests.get(self.baseUrl+ self.GET_PATIENT_STUDY , params=payload)
        return response

    def get_series(self, collection=None, studyInstanceUID=None, patientID=None,seriesInstanceUID = None, modality = None, bodyPartExamined = None, manufacturerModelName = None, manufacturer = None, format="json"):
        params = {"Collection": collection, "StudyInstanceUID": studyInstanceUID, "SeriesInstanceUID": seriesInstanceUID, "Modality" :modality, "BodyPartExamined": bodyPartExamined, "ManufacturerModelName":manufacturerModelName, "Manufactuere": manufacturer, "api_key": self.api_key, "format": format}
        payload = self.parse_params(params)
        response  = requests.get(self.baseUrl+ self.GET_SERIES, params=payload)
        return response

    def get_image(self,seriesInstanceUID=None):
        params = {"SeriesInstanceUID": seriesInstanceUID, "api_key": self.api_key,format:"json"}
        payload=  self.parse_params(params)
        response = requests.get(self.baseUrl + self.GET_IMAGE, params=payload)
        return response

