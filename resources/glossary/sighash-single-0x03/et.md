---
term: (0X03)

---
SigHashi tüüp Bitcoini tehingu allkirjades kasutatav lipuke, mis näitab, et allkiri kehtib kõigi tehingu sisendite ja ainult ühe väljundi kohta, mis vastab sama sisendi indeksile, mis on allkirjastatud. Seega on iga sisend, mis on allkirjastatud `SIGHASH_SINGLE`-ga, konkreetselt seotud konkreetse väljundiga. Teised väljundid ei ole allkirjaga seotud ja neid saab seetõttu hiljem muuta. Seda tüüpi allkiri on kasulik keerukates tehingutes, kus osalejad soovivad siduda teatud sisendid konkreetsete väljunditega, jättes samal ajal paindlikkust teistele tehingu väljunditele.