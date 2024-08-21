---
term: OP_CHECKSIGADD (0XBA)
---

Võtab virnast ülemised kolm väärtust: `avalik võti`, `CScriptNum` `n` ja `allkiri`. Kui allkiri ei ole tühi vektor ja ei ole kehtiv, lõpeb skript veaga. Kui allkiri on kehtiv või on tühi vektor (`OP_0`), esitatakse kaks stsenaariumi:
* Kui allkiri on tühi vektor: virnale lükatakse `CScriptNum`, mille väärtuseks on `n`, ja täitmine jätkub;
* Kui allkiri ei ole tühi vektor ja jääb kehtivaks: virnale lükatakse `CScriptNum`, mille väärtuseks on `n + 1`, ja täitmine jätkub.
Lihtsustatult öeldes teostab `OP_CHECKSIGADD` operatsiooni, mis on sarnane `OP_CHECKSIG`-iga, kuid asemel, et virnale lükata tõene või väär, lisab see teisele väärtusele virna tipus `1`, kui allkiri on kehtiv, või jätab selle väärtuse muutmata, kui allkiri esindab tühja vektorit. `OP_CHECKSIGADD` võimaldab luua Tapscriptis samu multisignatuuri poliitikaid nagu `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY`, kuid partii viisil kontrollitavas vormis, mis tähendab, et see eemaldab traditsioonilise multisigi kontrollimisel otsinguprotsessi ja seega kiirendab kontrollimist, vähendades samal ajal operatiivkoormust sõlmede CPU-del. See operaator lisati Tapscripti ainult Taprooti vajaduste jaoks.