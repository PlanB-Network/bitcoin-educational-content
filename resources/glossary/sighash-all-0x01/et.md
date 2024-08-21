---
term: SIGHASH_ALL (0X01)
---

SigHash lipu tüüp, mida kasutatakse Bitcoin'i tehingute allkirjastamisel, et näidata, et allkiri kehtib tehingu kõikide komponentide kohta. Kasutades `SIGHASH_ALL`, hõlmab allkirjastaja kõiki sisendeid ja väljundeid. See tähendab, et ei sisendeid ega väljundeid ei saa pärast allkirjastamist muuta ilma seda kehtetuks muutmata. Selline SigHash lipu tüüp on Bitcoin'i tehingutes kõige levinum, kuna see tagab tehingu täieliku lõplikkuse ja terviklikkuse.