import unittest
from tciaexplorer import TciaExplorer
import os
import json
class TciaExplorerTest(unittest.TestCase):

    def setUp(self):
        self.api_key = os.getenv("TCIA_API_KEY")
        self.explorer = TciaExplorer(api_key=self.api_key)

class TestApi(TciaExplorerTest):
    def hasKey(self,obj,key):
        if key in obj:
            return True
        else:
            return False

    def test_get_collection_values(self):
        """Does every object in the array have a 'Collection' member?"""
        collections = json.loads(self.explorer.get_collection_values().text)
        for collection in collections:
            self.assertTrue(self.hasKey(collection, "Collection"))

    def test_get_patient(self):
        """Does every patient have a 'PatientID'?"""
        patients = json.loads(self.explorer.get_patient(collection="TCGA-LUSC").text)
        for patient in patients:
            self.assertTrue(self.hasKey(patient, "PatientID"))

    def test_get_patient_study(self):
        """Does every patient have a 'StudyInstanceUID'"""
        patientStudy  = json.loads(self.explorer.get_patient_study(patientID="TCGA-60-2725").text)
        for ps in patientStudy:
            self.assertTrue(self.hasKey(ps, "StudyInstanceUID"))

    def test_get__series(self):
        """Check for seriesInstanceUID"""
        patientSeries = json.loads(self.explorer.get_series(studyInstanceUID="1.3.6.1.4.1.14519.5.2.1.3023.4012.148221951711235231074338832568").text)
        for ps in patientSeries:
            self.assertTrue(self.hasKey(ps, "SeriesInstanceUID"))



if __name__ == '__main__':
    unittest.main()

