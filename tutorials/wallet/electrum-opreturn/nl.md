---
name: Electrum OP_RETURN
description: Registreer een bericht op de Blockchain Bitcoin met Electrum
---

![cover](assets/cover.webp)




Deze stap-voor-stap tutorial laat je zien hoe je een bericht schrijft op de Blockchain Bitcoin met behulp van het Wallet Electrum. Deze handeling gebruikt de OP_RETURN instructie om tekst in te voegen in een transactie, die openbaar zichtbaar is op de Blockchain. Volg deze eenvoudige stappen voor een succesvolle registratie.



---
## Vereisten





- Een computer (Windows, macOS of Linux).
- Internetverbinding.
- Een paar satoshis (Sats) of bitcoins (BTC) in je Wallet om het transactiebedrag en de kosten te dekken.
- Een tekst-naar-hex converter (bijvoorbeeld een online site) of een speciale tool zoals [deze OP_RETURN scriptgenerator] (https://resources.davidcoen.it/opreturnelectrum/).



---

## Stap 1: Download en installeer Electrum



![image](assets/fr/01.webp)



1. Bezoek de officiële website van Electrum: [electrum.org](https://electrum.org/).


2. Download de versie die overeenkomt met je besturingssysteem (Windows, macOS, Linux).


3. Installeer Electrum volgens de instructies van het installatieprogramma.


4. Controleer de integriteit van het gedownloade bestand (optioneel, maar aanbevolen om veiligheidsredenen) door de handtekening of Hash van het bestand te vergelijken.



→ Meer informatie over de Electrum-tutorial:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Stap 2: Maak of importeer een Wallet



1. Start Electrum.


2. Kies Maak een nieuwe Wallet of Herstel een bestaande Wallet als je al een seed frase (herstelfrase) hebt.


3. Volg de instructies om uw Wallet te configureren:




 - Maak voor een nieuwe Wallet een notitie van je seed zin en bewaar deze op een veilige plaats (papier, kluis, enz.).
 - Voor een bestaande Wallet voert u uw seed zin in om deze te herstellen.


4. Stel een wachtwoord in om je Wallet te beveiligen.



→ Meer informatie over de Electrum-tutorial:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Stap 3: Controleer beschikbare fondsen



Zorg ervoor dat je Wallet genoeg bitcoins (BTC) of satoshis (Sats) bevat om :




- Transactiebedrag (bijvoorbeeld 0,00001 BTC of 1000 Sats).
- Transactiekosten, die variëren afhankelijk van de grootte van het netwerk (over het algemeen een paar duizend Sats).



Raadpleeg de Balans in Electrum om je fondsen te controleren.



![image](assets/fr/02.webp)



Maak indien nodig BTC of Sats over om je Wallet te voeden. Ga hiervoor naar het tabblad 'Ontvangen' en klik op 'Verzoek aanmaken':



![image](assets/fr/03.webp)



Dit toont een ontvangst Address:



![image](assets/fr/04.webp)



→ Meer informatie over de Electrum-tutorial:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Stap 4: Het bericht voorbereiden voor inscriptie



Selecteer het bericht dat je wilt invoeren (bijvoorbeeld `Dank Satoshi`). Opmerking: OP_RETURN berichten zijn beperkt tot 80 bytes, d.w.z. ongeveer 80 ASCII karakters.



*Neem even de tijd om na te denken: wat je op de Blockchain Bitcoin schrijft is eeuwig en voor iedereen toegankelijk, dus :*




- een prachtige uitdrukking van onze menselijkheid achterlaten,
- vermijd het invoeren van inhoud waar u spijt van kunt krijgen



*Blockchain ruimte en je bitcoins zijn kostbaar, gebruik ze verstandig en met intentie*



Converteer je bericht naar hexadecimaal :




- Je kunt een [online tool] (https://www.rapidtables.com/convert/number/ascii-to-hex.html) gebruiken, maar pas op dat je daar geen gevoelige gegevens verwerkt (hoewel informatie die bedoeld is voor publicatie op Blockchain Bitcoin via een OP_RETURN in principe geen vertrouwelijkheidsproblemen oplevert);
- Voor meer vertrouwelijkheid kun je de conversie lokaal uitvoeren met een kleine Python :



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



Voorbeeld: `Dank Satoshi` in ASCII geeft `5468616e6b73205361746f736869` in hexadecimaal.



Bereid het transactiescript voor. Hier is een voorbeeld van het verwachte formaat:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



die bestaat uit :





- **Bestemming Address**: Een geldige Bitcoin Address. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. Dit kan je eigen Address zijn, als je het overgemaakte geld naar jezelf wilt terugstorten;
- **Getransfereerd bedrag**: het bedrag van de transactie, hier `0.00001` BTC. **Let op**: aangezien de eenheid die in Electrum wordt gebruikt BTC is, moet het bedrag in het transactiescript ook worden uitgedrukt in BTC, en niet in Sats ;
- Script **OP_RETURN**: Het bericht geconverteerd naar hexadecimaal voorafgegaan door script(`OP_RETURN <messsage>), 0`. Hier staat `5468616e6b73205361746f736869` voor het bericht in hexadecimaal.



⚠️ **Voorzichtig**: Het is erg belangrijk om `0` aan te geven na de OP_RETURN, omdat deze opcode het script als ongeldig markeert, waardoor de uitvoer permanent onbruikbaar wordt. Netwerkknooppunten zullen deze uitvoer verwijderen uit hun UTXO set. Als je een andere waarde dan `0` invoert, zal deze onherroepelijk verloren gaan: je bitcoins zullen als verbrand worden beschouwd. Daarom moet je altijd `0` invoeren bij een OP_RETURN om de gewenste gegevens te registreren, maar zonder er geld aan te koppelen, dat verloren zou gaan.



Tip: Gebruik de [OP_RETURN Generator] tool (https://resources.davidcoen.it/opreturnelectrum/) om het script automatisch generate te maken. Zelfs als deze tool voorstelt om het bedrag in BTC in te voeren, houd de eenheid geconfigureerd in Electrum.



![image](assets/fr/05.webp)



Om de eenheid die door Electrum wordt gebruikt te wijzigen, zoek je in de menubalk naar "Voorkeuren" en kies je op het tabblad "Eenheden" BTC / mBTC / bits of Sats :



![image](assets/fr/06.webp)




---

## Stap 5: Verzend de transactie



Ga in Electrum naar de tab Verzenden.



![image](assets/fr/07.webp)



Plak in het veld "Betalen aan" het voorbereide script (bijvoorbeeld het bovenstaande).



![image](assets/fr/08.webp)



Het veld "Betalen aan" moet worden weergegeven in Green en het transactiebedrag moet op de regel eronder verschijnen.



Controleer het bedrag en de eenheid ervan in het veld Bedrag.



Klik op "Betalen..." en pas je transactiekosten aan op basis van het bedrag dat je bereid bent te betalen en de snelheid waarmee je wilt dat je transactie wordt verwerkt door een Miner en wordt geïntegreerd in een blok.



![image](assets/fr/09.webp)



Klik op OK en bevestig de transactie met je wachtwoord. Er verschijnt een bevestigingsvenster.




---

## Stap 6: Registratie verifiëren



Zodra de transactie is bevestigd (dit kan enkele minuten duren), ga je naar het tabblad "Geschiedenis".



![image](assets/fr/10.webp)



Klik met de rechtermuisknop op de transactie en selecteer "Weergeven op verkenner" om de details te bekijken.



Als alternatief, kopieer de bestemming Address (bijvoorbeeld `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) en bekijk het op een Blockchain verkenner zoals [Mempool.space](https://Mempool.space/) of [blockstream.info](https://blockstream.info/).



Zoek naar het OP_RETURN veld in de transactiedetails om je bericht te zien.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Tips en best practices





- Test met een klein bedrag: Begin met een kleine transactie (bijv. Sats 1000) om kostbare fouten te voorkomen.
- Zorg ervoor dat de uitvoer die OP_RETURN bevat gelijk is aan nul, anders zullen je bitcoins permanent verloren gaan.
- Controleer de eenheid: Controleer of het ingevoerde bedrag overeenkomt met de eenheid die wordt weergegeven in Electrum (BTC, mBTC of Sats).
- Transactiekosten: Als het netwerk overbelast is, verhoog dan de kosten voor snellere bevestiging.
- Kort bericht: OP_RETURN berichten zijn beperkt tot 80 bytes. Plan je bericht dienovereenkomstig.



---

## Nuttige bronnen





- Download Electrum: [electrum.org](https://electrum.org/)
- OP_RETURN script generator: [resources.davidcoen.it/opreturnelectrum/] (https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain Verkenners: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)