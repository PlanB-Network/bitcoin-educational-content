---
term: ERLAY
---

Kavandatud võrguprotokoll, et parandada kinnitamata tehingute edastamise tõhusust Bitcoin sõlmede vahel.


Praegu levitatakse iga tehingut süsteemi kaudu, milles iga sõlme edastab tehingu, millest ta on teadlik, kõigile oma eakaaslastele. Probleemiks on see, et see toob kaasa palju dubleerimist ja ribalaiuse kasutamist. Paljud tehingu ülekanded ei ole vajalikud, sest vastuvõtja teab juba nendest tehingutest ja iga sõlme peab igast tehingust teadma ainult üks kord. Erlay teeb ettepaneku piirata vaikimisi 8-ga nende eakaaslaste arvu, kellele sõlmpunkt saadab otse tehinguid, millest ta teab, ning kasutada seejärel minisketch-tööribaasil põhinevat kooskõlastusprotsessi, et jagada puuduvaid tehinguid tõhusamalt.


Erlay vähendaks ribalaiuse tarbimist umbes 40% võrra, muutes Full node toimimise kättesaadavamaks piiratud internetiühendusega kasutajatele ja edendades seeläbi võrgu paremat detsentraliseerimist. See protokoll säilitaks ka ühenduste arvu kasvades peaaegu konstantse ribalaiuse tarbimise. See tähendab, et sõlmede operaatoritel oleks palju lihtsam aktsepteerida väga suurt arvu ühendusi oma eakaaslastelt, mis suurendaks Bitcoin võrgu turvalisust, vähendades tahtliku või juhusliku jagunemise ohtu. Lisaks muudaks Erlay raskemaks tehingu päritolusõlme määramise, suurendades seega konfidentsiaalsust nende sõlmede kasutajate jaoks, kes ei tegutse Tori all.


Erlay on kavandatud BIP330-s.