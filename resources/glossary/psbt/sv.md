---
term: PSBT
definition: Standardiserat format för att konstruera och dela delvis signerade Bitcoin-transaktioner.
---

Akronym för "Partially Signed Bitcoin Transaction". Det är en specifikation som introducerades med BIP174 för att standardisera det sätt på vilket oavslutade transaktioner konstrueras i programvara relaterad till Bitcoin, t.ex. Wallet-programvara. En PSBT kapslar in en transaktion där inmatningarna kanske inte är fullständigt signerade. Den innehåller all nödvändig information för att en deltagare ska kunna signera transaktionen utan att ytterligare data krävs. En PSBT kan således anta tre olika former:


- En fullt konstruerad transaktion, men ännu inte undertecknad;
- En delvis signerad transaktion, där vissa inmatningar är signerade medan andra ännu inte är det;
- Eller en fullständigt signerad Bitcoin-transaktion som kan konverteras så att den är redo att sändas ut i nätverket.


PSBT-formatet underlättar driftskompatibilitet mellan olika Wallet-programvaror och signaturanordningar (Hardware Wallet). För närvarande används version 0 av PSBT, enligt definitionen i BIP174, men version 2 föreslås via BIP370.


> ► *Version 1 av PSBT existerar inte. Eftersom version 0 var den första versionen kallades den andra versionen informellt för version 2. Ava Chow, som författade BIP370, beslutade därför att tilldela nummer 2 till denna nya version för att undvika förvirring.*