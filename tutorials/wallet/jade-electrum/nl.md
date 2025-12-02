---
name: Jade - Electrum
description: Hoe uw Jade of Jade Plus gebruiken met Electrum (desktop)
---

![cover](assets/cover.webp)



_Deze handleiding komt uit een [Bitcoin Workshops les](https://officinebitcoin.it/lezioni/jadeele/index.html)_



De tutorial is gemaakt met Jade Classic, maar de handelingen zijn ook geldig voor degenen die Jade Plus hebben.



Na het initialiseren van Jade kun je het gaan gebruiken en - om dat te doen - een wallet scherm kiezen.



Jade is een apparaat dat gebruikt kan worden met verschillende wallet, of companion apps zoals Blockstream ze noemt op haar site.



In deze tutorial zie je de stappen voor het gebruik van de Electrum Wallet, via een USB-kabelverbinding.



## Overdracht van openbare sleutel



Zet je geïnitialiseerde Jade aan. Zodra je hem aanzet ziet hij er zo uit:




![img](assets/en/32.webp)



Als je _Unlock Jade_ selecteert, krijg je het menu waarin je moet kiezen hoe je je apparaat met de companion app verbindt.



Met de Electrum kun je Jade alleen via USB aansluiten, dus kies deze methode.



Start Electrum, dat als standaardoptie de laatst gebruikte wallet zal openen.



Als dit de eerste keer is dat u Jade met Electrum verbindt, selecteer dan _Create New Wallet_ en daarna _Finish_.



![img](assets/en/34.webp)



Naam wallet.



![img](assets/en/35.webp)



Selecteer Standaard Wallet.



![img](assets/en/36.webp)



Bij het kiezen van de sleutelbewaarplaats is het essentieel om _Use a hardware device_ te selecteren.



![img](assets/en/37.webp)



Electrum begint met het scannen naar het hardwareapparaat.



![img](assets/en/38.webp)



Door USB op de computer aan te sluiten (aan de USB C-kant al verbonden met Jade), verschijnt de wallet hardware in de vergrendelmodus. Jade ontgrendelt door de zescijferige pincode in te voeren die tijdens de installatie is ingesteld.




![img](assets/en/39.webp)



Ontgrendeld Hardware-apparaat, Electrum detecteert Jade. Ga verder door op _Volgende_ te klikken.



![img](assets/en/40.webp)



Op dit punt vraagt Electrum je om het beleidsscript in te stellen: kies _Native Segwit_.



![img](assets/en/41.webp)



De fase van de overdracht van de openbare sleutel van wallet van Jade naar Electrum begint.



Wanneer het exporteren van de openbare sleutel is voltooid, is het proces voltooid.



Het horloge is klaar en Electrum waarschuwt voor voltooiing met het volgende scherm.



![img](assets/en/42.webp)



wallet is daadwerkelijk aangemaakt en je kunt het gaan verkennen: je ziet de _adressen_, de _wallet informatie_ en - het belangrijkste - je ziet rechtsonder de indicatie dat het een apparaat van Blockstream is. De groene stip naast het Blockstream-logo geeft aan dat het apparaat is ingeschakeld en correct is verbonden met het lokale netwerk.



![img](assets/en/43.webp)



## Transacties ontvangen en uitgeven



Vanuit het menu _Ontvangen_ van Electrum, generate een `scriptPubKey` (adres) om geld te ontvangen. Begin altijd met een klein bedrag en doe een ontvang+geef test.



![img](assets/en/44.webp)



Als je satss hebt ontvangen, kun je hun aankomst controleren in het menu _Geschiedenis_.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



Zodra de transactie is bevestigd, kun je deze UTXO uitgeven en de test voltooien.



De kosten bestaan uit het gebruik van Jade om te tekenen.



Ga naar het _Verstuur_ menu van Electrum, plak een scriptPubKey, en controleer het goed.



![img](assets/en/47.webp)



Druk op _Betalen_ wanneer u klaar bent.



Het transactievenster wordt geopend, waarin het belangrijk is om de juiste transactiekosten in te stellen. Als je klaar bent met alle instellingen klik je rechtsonder op _Preview_.



![img](assets/en/48.webp)



Het transactievenster toont enkele belangrijke details, allereerst de status: `Onondertekend`.



In dit stadium zie je ook het _Teken_ commando, waarop je moet klikken om de handtekening met Jade te plaatsen.



![img](assets/en/49.webp)



Nu begint een communicatiefase tussen het display wallet en het hardware-apparaat, waarin Electrum je waarschuwt om de instructies op het hardware-apparaat te volgen, dat is ingeschakeld en klaar is om te tekenen.



![img](assets/en/50.webp)



**Maar eerst kun je beter verifiëren wat je ondertekent: alle parameters van de transactie die je zojuist hebt ingesteld, verschijnen ook op Jade** en je kunt ze allemaal verifiëren.



![img](assets/en/51.webp)



Om verder te gaan moet je de cursor altijd op de pijl `→` plaatsen die naar de volgende stappen leidt en nooit op de pijl `X` tenzij je de bewerking wilt beëindigen zonder deze te voltooien.



Het verificatiegedeelte eindigt met de weergave van de vergoeding. Op dit punt is bevestiging gelijk aan het zetten van je handtekening.



![img](assets/en/52.webp)



Gedurende een kort moment verwerkt Jade de bewerking, wanneer deze is voltooid keert hij terug naar het hoofdmenu.



![img](assets/en/53.webp)



Op Electrum kun je de status van de transactie zien, die is veranderd van `Onondertekend` in `Gehandtekend` en nu is het mogelijk, voor jou, om het te propageren door te klikken op _Broadcast_.



![img](assets/en/54.webp)



wallet, aldus getest, kan worden gebruikt om UTXO te ontvangen, bedoeld voor veilige opslag.



![img](assets/en/55.webp)



Deze handleiding is een voorbeeld van hoe je je Jade, aangesloten via USB, kunt gebruiken met een wallet watch-only. Electrum is een klassiek voorbeeld, maar je kunt ook de voorkeur geven aan andere wallet software. Jade exporteert de publieke sleutel naar vele andere wallets: zoek de vergelijkbare functies waarover je leest in deze tutorial, om je te begeleiden en te ontdekken hoe je je favoriete companio app kunt gebruiken.