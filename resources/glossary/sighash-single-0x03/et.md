---
term: SIGHASH_SINGLE (0X03)
---

SigHash lipu tüüp, mida kasutatakse Bitcoin'i tehingute allkirjastamisel, et näidata, et allkiri kehtib kõigi tehingu sisendite kohta ja ainult ühe väljundi kohta, mis vastab samale sisendile allkirjastatud indeksile. Seega on iga `SIGHASH_SINGLE`-ga allkirjastatud sisend spetsiifiliselt seotud teatud väljundiga. Teisi väljundeid allkiri ei hõlma ja seetõttu saab neid hiljem muuta. Selline allkiri on kasulik keerukate tehingute puhul, kus osalejad soovivad teatud sisendeid siduda spetsiifiliste väljunditega, jättes samal ajal paindlikkuse tehingu teiste väljundite jaoks.