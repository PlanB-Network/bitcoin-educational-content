---
term: INDEKSI/TXINDEX/
---

Datoteke u Bitcoin Core koje su posvećene indeksiranju svih transakcija prisutnih u Blockchain. Ovo indeksiranje omogućava brzo pretraživanje detaljnih informacija o transakciji koristeći njen identifikator (txid), bez potrebe za prolaskom kroz ceo Blockchain. Kreiranje ovih indeksirajućih datoteka je opcija koja nije podrazumevano omogućena u Bitcoin Core. Ako ova funkcija nije omogućena, vaš čvor će indeksirati samo transakcije povezane sa novčanicima pridruženim vašem čvoru. Da biste omogućili indeksiranje svih transakcija, morate postaviti parametar `-txindex=1` u `Bitcoin.conf` datoteci. Ova opcija je posebno korisna za aplikacije i usluge koje često pretražuju istoriju transakcija Bitcoin.