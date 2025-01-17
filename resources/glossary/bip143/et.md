---
term: BIP143

---
Võtab kasutusele uue viisi tehingu hashinguks allkirja kontrollimiseks SEGWit-järgsetes skriptides. Eesmärgiks on minimeerida üleliigseid operatsioone kontrollimise ajal ja lisada UTXOde väärtus sisendisse allkirja. See lahendab kaks peamist probleemi, mis on seotud algse tehingu hashimise algoritmiga:


- Andmete hashimise kvadraatiline kasv koos allkirjade arvuga;
- Sisendväärtuse lisamata jätmine allkirja, mis kujutas endast ohtu riistvara rahakottidele, eriti seoses teadmisega tekkinud tehingutasudest.

Kuna BIP141-s selgitatud SegWit-uuendus toob sisse uue tehinguvormi, mille käsikirja vanad sõlmed ei verifitseeri, kasutab BIP143 seda võimalust selle probleemi lahendamiseks, ilma et see nõuaks kõva kahvlitamist. Seetõttu on BIP143 osa SegWit soft fork'ist.