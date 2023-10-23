![image](https://github.com/crtyx/cyber-csv/assets/61663707/87a02167-9023-4e4f-b617-f6f66de52d68)



#cyber-csv
# A basic python script that converts Cybersole JSON to CSV and vice versa.

https://www.python.org/downloads/

///////

- Please make sure you have the latest Python version installed and that you insall any requirements.

  // HOW TO USE //
  
- Create a folder place your Cybersole 5.x JSON file inside along with the cybercsv python script (Or download the latest .zip file, from Releases, extract and copy your Cybersole 5.x JSON into that folder)
  
- Make sure the file is named 'billing.json' and/or your CSV file named 'billing.csv'

- Open a CMD/powershell window inside said folder and type py cybercsv.py

- You may need to install 'colorama' and 'num2words' manually by typing pip install colorama and then pip install num2words

- Select your option [Note - Only Cybersole JSONs + Only CSVs generated with this script are compatitible]

  The script will then import and convert your Cybersole JSON into a CSV where you can manually edit via RONSEDITOR (Recommended) for convenience. When you are done you can then repeat the steps inside the script to convert your modified CSV back to a functional Cybersole JSON.

  //// Alpha / Not extensively tested ///

  All data is stored locally on your device and nothing is transferred elsewhere obviously.

///////////////

- Added option to export payment methods (number, exp, cvv) from a supplied CSV.
- Added option for basic automated address modifying from a supplied csv.

///////////////

UPDATE // 

Cybersole added support for CSV import HOWEVER currently this script does not export the CSV into a format that is fully compatible, so your options are;

 1) Export JSON to CyberCSV CSV format, edit the CSV and then export back to JSON and import.
 2) Export JSON to CyberCSV format and then transfer your data to the official Cybersole template (Below)

This script will still be useful to export your JSON to a CSV as Cybersole only supports importing of CSV and not exporting.

Official Cybersole CSV Template:
https://docs.google.com/spreadsheets/d/1g0YX_OTldXQ_aqHsIgpW0rC-l3s5IhvvvnX3617wMnk/edit?usp=sharing

--

Example of CSV Export from CyberCSV (You could also edit this example and convert to JSON via CyberCSV

- Make sure you are logged into Google, head to 'FILE' and then 'MAKE A COPY'.
https://docs.google.com/spreadsheets/d/1sud1BSVl0BUeNQk3_FMpSzF4Qd6uAoemBgxx0T1ZU_w/edit?usp=sharing

NOTE: If you input your STATE or COUNTRY incorrectly on the CSV then you will have issues importing. Make sure your country and state is EXACTLY as inputted on Cybersole. I have included a list of countries/states pulled from Cybersole HERE: https://docs.google.com/spreadsheets/d/18-FxBT0bDB1TkMM-yl9bm8nyAgwwgliWsjg97fVj_6M/edit?usp=sharing
