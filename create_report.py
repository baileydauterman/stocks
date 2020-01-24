import pandas as pd
import os
import numpy as np

#Start csv imports
bitlocker = pd.read_csv("BitLocker on C Drive - Copy.csv")
classroom = pd.read_csv("Classroom Computers.csv")
exad = pd.read_csv("Exclude - AD.csv")
exencryption = pd.read_csv("Exclude - Encryption.csv")
exeol = pd.read_csv("Exclude - EOL OS.csv")
exsep = pd.read_csv("Exclude - SEP.csv")
fv = pd.read_csv("FileVault Encrypted Macs.csv")
macsep = pd.read_csv("Mac SEP Report - Copy.csv")
main = pd.read_csv("Main Computer Report - Copy.csv",skiprows=(2,3))
main = main.replace(np.nan, "")
main = main.replace(0, "")

#aggregate all office data into a single dataframe
office = pd.read_csv("MS Office Version 2007.csv")
office["Version"] = "2007"

office10 = pd.read_csv("MS Office Version 2010.csv")
office10["Version"] = "2010"
office = office.append(office10, ignore_index=True)

office13 = pd.read_csv("MS Office Version 2013.csv")
office13["Version"] = "2013"
office = office.append(office13, ignore_index=True)

office16 = pd.read_csv("MS Office Version 2016.csv")
office16["Version"] = "2016"
office = office.append(office16, ignore_index=True)

office19 = pd.read_csv("MS Office Version 2019.csv")
office19["Version"] = "2019"
office = office.append(office19, ignore_index=True)
office.drop_duplicates(subset='Device Name',keep='last', inplace=True) #drops all duplicates and keeps the last one which is the most recent version of office
office

report = pd.DataFrame() #creates main dataframe


report = pd.DataFrame()
#add device name
report.insert(0,column="Device Name", value=main["Device Name"])

#add os name
report.insert(1,column="OS Name", value=main["OS Name"])
rows = main.shape[0]
osversions = []
for row in range(0,rows):
    name = main.iloc[row]["Device Name"]
    win10 = main.iloc[row]["Win 10 Version"]
    win7 = main.iloc[row]["Win 7 SP Version"]
    macos = main.iloc[row]["macOS Version"]
    
    if not win10 == "":
        osversions.append(win10)
    elif not win7 == "":
        osversions.append(win7)
    elif not macos == "":
        osversions.append(macos)
    else:
        osversions.append("")
#add machine type and os version
report.insert(2,column="OS Version", value=osversions)
report.insert(3,column="Machine Type", value=main["Machine Type"])

#add support group
report["Support Group"] = ""

#add symantec version
report["Symantec Version"] = ""

size = main.shape[0]
for row in range(0,size):
    name = main.iloc[row]['Device Name']
    av = main.iloc[row]['Product Name']
    version = main.iloc[row]['Product Version']
    if av == "Symantec Endpoint Protection":
        ind = report.index[report['Device Name']==name]
        report.at[ind[0],'Symantec Version'] = version

#add filvault encryption
report.insert(6,column="Domain Name", value=main["Domain Name"])
report["FileVault Encryption"] = ""
    
size = fv.shape[0]
for row in range(0,size):
    name = fv.iloc[row]['Device Name']
    ind = report.index[report['Device Name']==name]
    
    status = fv.iloc[row]['Protection Status']
    
    if "on" in status:
        status = "Yes"
    else:
        status = "No"
    
    report.at[ind[0],'FileVault Encryption'] = status

#add bitlocker encryption
report["BitLocker Encryption"] = ""
    
size = bitlocker.shape[0]
for row in range(0,size):
    name = bitlocker.iloc[row]['Device Name']
    ind = report.index[report['Device Name']==name]
    
    status = bitlocker.iloc[row]['Protection Status']
    
    if "on" in status:
        status = "Yes"
    else:
        status = "No"
    
    report.at[ind[0],'Bitlocker Encryption'] = status
#add Serial number, ip address, last date reported, login name
report.insert(9,column="Serial Number", value=main["Serial Number"])
report.insert(10,column="IP Address", value=main["IP Address"])
report.insert(11,column="Last Reported", value=main["Last Date Reported"])
report.insert(12,column="Login Name", value=main["Login Name"])

#add AD exception
report["AD Exception"] = ""
    
size = exad.shape[0]
for row in range(0,size):
    name = exad.iloc[row]['Device name']
    ind = report.index[report['Device Name']==name]
    report.at[ind[0],'AD Exception'] = "Yes"

#add encryption exception
report["Encryption Exception"] = ""
    
size = exencryption.shape[0]
for row in range(0,size):
    name = exencryption.iloc[row]['Device name']
    ind = report.index[report['Device Name']==name]
    report.at[ind[0],'Encryption Exception'] = "Yes"

#add OS EOL Exception
report["OS EOL Exception"] = ""

size = exeol.shape[0]
for row in range(0,size):
    name = exeol.iloc[row]['Device name']
    ind = report.index[report['Device Name']==name]
    report.at[ind[0],'OS EOL Exception'] = "Yes"

#add SEP column
report["SEP Exception"] = ""

size = exsep.shape[0]
for row in range(0,size):
    name = exsep.iloc[row]['Device name']
    ind = report.index[report['Device Name']==name]
    report.at[ind[0],'SEP Exception'] = "Yes"

#add office column
report["MS Office Version"] = ""

size = office.shape[0]
for row in range(0,size):
    name = office.iloc[row]['Device Name']
    version = office.iloc[row]['Version']
    ind = report.index[report['Device Name']==name]
    report.at[ind,'MS Office Version'] = version

#Output the excel to cwd
report = report.fillna("")
report.to_excel("Ivanti Report Thing.xlsx")