---
term: FIBRE
---

Akronim za "*Fast Internet Bitcoin Relay Engine*". To je protokol koji je dizajnirao Matt Corallo 2016. godine kako bi ubrzao distribuciju Bitcoin blokova širom sveta. Njegov cilj je bio da smanji kašnjenja u propagaciji što bliže fizičkim granicama. FIBRE je imao za cilj da osigura pravedniju distribuciju Mining prilika, tako što bi se pobrinulo da proporcija blokova koje učesnik iskopa tačno odražava njihov doprinos u smislu računarske snage, bez obzira na njihov položaj u mreži.


Zaista, latencija u prenosu blokova može favorizovati velike, dobro povezane Mining grupe, često locirane blizu jedna druge, na štetu manjih. Ovaj fenomen bi, tokom vremena, mogao povećati centralizaciju Mining i smanjiti ukupnu sigurnost sistema. Da bi se rešio ovaj problem, FIBRE je uveo kodove za ispravljanje grešaka i prenos dodatnih podataka kako bi se nadoknadio gubitak paketa, kao i korišćenje kompaktnih blokova sličnih onima opisanim u BIP152, sve to funkcionišući putem UDP-a kako bi se zaobišla određena TCP ograničenja. Ipak, FIBRE je napušten 2020. godine, uglavnom zbog zavisnosti od jednog održavaoca i činjenice da je usvajanje BIP152 učinilo takav sistem manje neophodnim.