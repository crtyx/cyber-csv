![image](https://github.com/crtyx/cyber-csv/assets/61663707/cc41af25-714a-4527-b379-731d7aead09f)


#cyber-csv
# A basic python script that converts Cybersole JSON to CSV and vice versa.

https://www.python.org/downloads/

///////

- Please make sure you have the latest Python version installed and that you insall any requirements.

  // HOW TO USE //
  
- Create a folder place your Cybersole 5.x JSON file inside along with the cyber-csv python script.
  
- Place your JSON inside the folder and make sure its named 'billing.json' and/or your CSV file named 'billing.csv'

- Open a CMD/powershell window inside said folder and type py cybercsv.py

- Select your option [Note - Only Cybersole JSONs + Only CSVs generated with this script. are compatitible]

  The script will then import and convert your Cybersole JSON into a CSV where you can manually edit via RONSEDITOR (Recommended) for convenience. When you are done you can then repeat the steps inside the script to convert your modified CSV back to a functional Cybersole JSON.

  //// Alpha / Not extensively tested ///

  All data is stored locally on your device and nothing is transferred elsewhere obviously.

///////////////

UPDATE // 

Cybersole added support for CSV import HOWEVER currently this script does not export the CSV into a format that is fully compatible, so your options are;

 1) Export JSON to CyberCSV CSV format, edit the CSV and then export back to JSON and import.
 2) Export JSON to CyberCSV format and then transfer your data to the official Cybersole template (Below)

This script will still be useful to export your JSON to a CSV as Cybersole only supports importing of CSV and not exporting.

Official Cybersole CSV Template:
https://docs.google.com/spreadsheets/d/1g0YX_OTldXQ_aqHsIgpW0rC-l3s5IhvvvnX3617wMnk/edit?usp=sharing
