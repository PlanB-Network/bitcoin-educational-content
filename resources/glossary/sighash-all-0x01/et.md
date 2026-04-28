---
term: SIGHASH_ALL

definition: SigHashi lipp, mis näitab, et allkiri hõlmab tehingu kõiki sisendeid ja väljundeid.
---
SigHashi tüüp Bitcoini tehingu allkirjades kasutatav lipuke, mis näitab, et allkiri kehtib tehingu kõigi komponentide kohta. Kasutades `SIGHASH_ALL`, katab allkirjastaja kõik sisendid ja kõik väljundid. See tähendab, et ei sisendeid ega väljundeid ei saa pärast allkirjastamist muuta ilma seda kehtetuks muutmata. Seda tüüpi SigHash Flag on Bitcoini tehingutes kõige levinum, kuna see tagab tehingu täieliku lõplikkuse ja terviklikkuse.