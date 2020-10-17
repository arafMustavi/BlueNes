# Nesternship | HR Project | Medical Data

Medical Temperature Data Extraction as a part of the ongoing NesternShip program

## Task 01:
Read Data from the excel file in the .xlsx format

### Reports on Task 1

**12/10/2020 05:55 PM** : Started working with **xlrd** package of python to read the data. Following the geeksforgeeks in the following link: https://www.geeksforgeeks.org/reading-excel-file-using-python/

**12/10/2020 06:16 PM** : The excel file can be read easily using **xlrd** packatge. Need to have a peep into **openpyxl** package

**12/10/2020 09:41 PM** : The **xlrd** package takes significant amount of time to read a large dataset. So its better to have some sort of log rint in dataset reading 

**13/10/2020 12:45 PM** : https://forms.gle/5Ne37GvjajT4RoKW8 is the demo data receiver app

**13/10/2020 12:55 PM** : Google Spreadsheet Data Access | https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html

## Task 02:
Create Executable file from .py

### Reports on Task 2

**13/10/2020 11:52 PM** : Tried https://datatofish.com/executable-pyinstaller/ to create Executable file. But the pip did not find pyinstaller 

**13/10/2020 12:01 PM** : Tried https://youtu.be/jnAoz_ZfMjE . Again failed

Error I am getting :

ERROR: Could not install packages due to an EnvironmentError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Max retries exceeded with url: /packages/82/96/21ba3619647bac2b34b4996b2dbbea8e74a703767ce24192899d9153c058/pyinstaller-4.0.tar.gz (Caused by NewConnectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x0000021A8CDFF580>: Failed to establish a new connection: [Errno 11002] getaddrinfo failed'))

**13/10/2020 12:07 PM** : Resolved the ERROR . It was due to my bad Internet (-_-) F-U-Wifi.

Procedures to install the ##pyinstaller :
```

C:\Users\Araf\AppData\Local\Programs\Python\Python38\Scripts

pip install pyinstaller

```
 
## Task 03:
Plot the temperature Data Graph 

### Reports on Task 2

**14/10/2020 01:36AM** : Draft of plotting based on the dummy data is completed in the dummyDATAplot.py | Need to create executable and Tkinter based small GUI
  
**14/10/2020 02:42PM** : Using the date as x_label creates a mess up | Should go with values i.e: 1 2 3 4 5 and so on

**14/10/2020 02:51PM** : pyinstaller works! Created The ClickMe HelloWorld in .exe format

