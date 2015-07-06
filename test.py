from tciaexplorer import TciaExplorer

tcia = TciaExplorer(api_key="16ade9bc-f2fa-4a37-b357-36466a0020fc")

print(tcia.get_collection_values().content)
print(tcia.get_patient(collection="TCGA-GBM").content)
print(tcia.get_patient_study(patientID="TCGA-VP-A87C").content)
print(tcia.get_series(seriesInstanceUID="1.3.6.1.4.1.14519.5.2.1.7777.4006.246322038387835648676649859085"))
