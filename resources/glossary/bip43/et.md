---
term: BIP43

---
Parandusettepanek, millega võetakse kasutusele tuletamise tee tase, et kirjeldada HD-rahakoti struktuuris kasutatavat sihtotstarbevälja, mis on varem kasutusele võetud BIP32-s. Vastavalt BIP43-le on HD-rahakoti esimene tuletamistasand, kohe pärast "m/"-ga tähistatud põhivõti, reserveeritud eesmärgi numbrile, mis näitab ülejäänud tuletamise standardit. See number salvestatakse karastatud indeksina. Näiteks kui rahakott järgib SegWit standardit (BIP84), siis on selle tuletamise tee algus järgmine: `m/84'/`. BIP43 võimaldab seega täpsustada standardeid, mida iga rahakoti tarkvara järgib, et tagada nende parem koostalitlusvõime. Ülejäänud tuletamise tee standardiseerimine on kirjeldatud dokumendis BIP44.