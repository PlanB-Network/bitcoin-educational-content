---
term: OP_CHECKSIGADD (0XBA)

---
Võtab korstnast välja kolm ülemist väärtust: "avalik võti", "C-scriptNum" "n" ja "allkiri". Kui allkiri ei ole tühi vektor ja ei ole kehtiv, lõpetab skript veaga. Kui allkiri on kehtiv või on tühi vektor (`OP_0`), esitatakse kaks stsenaariumi:


- Kui allkiri on tühi vektor: korstnasse lükatakse `CScriptNum` väärtusega `n` ja täitmine jätkub;
- Kui allkiri ei ole tühi vektor ja jääb kehtima: korstnasse lükatakse `CScriptNum` väärtusega `n + 1` ja täitmine jätkub.

Lihtsustamise eesmärgil teeb `OP_CHECKSIGADD` sarnast operatsiooni nagu `OP_CHECKSIG`, kuid selle asemel, et lükata virna true või false, lisab ta `1` teise väärtuse virna tippu, kui allkiri on kehtiv, või jätab selle väärtuse muutmata, kui allkiri kujutab endast tühja vektorit. `OP_CHECKSIGADD` võimaldab Tapscriptis luua samu mitme allkirja poliitikaid nagu `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY`, kuid see on partiide kaupa kontrollitav, mis tähendab, et traditsioonilise mitme allkirja kontrollimisel eemaldatakse otsinguprotsess ja seega kiirendatakse kontrollimist, vähendades samal ajal sõlmede protsessorite koormust. See opkood lisati Tapscriptis ainult Taproot'i vajaduste jaoks.