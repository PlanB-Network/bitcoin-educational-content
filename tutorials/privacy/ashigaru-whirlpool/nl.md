---
name: Ashigaru - Whirlpool Coinjoin
description: Hoe maak ik coinjoins op de Ashigaru-toepassing?
---

![cover](assets/cover.webp)



"*een bitcoin wallet voor op straat*"



In deze tutorial leer je wat een coinjoin is en hoe je er een maakt met de Ashigaru Terminal applicatie en de Whirlpool implementatie, een coinjoin protocol dat geërfd is van Samourai Wallet.



## Hoe Whirlpool muntverbindingen werken



In deze tutorial zal ik niet terugkomen op het begrip coinjoin, het nut ervan of de theoretische werking van Whirlpool, omdat deze onderwerpen al in detail zijn uitgelegd in deel 5 van de BTC 204 training op Plan ₿ Academy. Als je de werking van Whirlpool of het principe van een coinjoin nog niet onder de knie hebt, raad ik je ten zeerste aan dit deel 5 te raadplegen alvorens verder te gaan:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Hier zijn echter een paar snelle feiten en cijfers die van pas kunnen komen.



Whirlpool compatibele portefeuilles gebruiken 4 afzonderlijke rekeningen om te voldoen aan de behoeften van het coinjoin proces:




- De **Deposito** rekening, geïdentificeerd door index `0'` ;
- De **Bad Bank** (of *doxic exchange*) rekening, geïdentificeerd door de index `2,147,483,644'` ;
- De rekening **Premix**, geïdentificeerd met de index `2 147 483 645'` ;
- De **Postmix**-rekening, geïdentificeerd met de index `2 147 483 646'`.



Op Ashigaru zijn in november 2025 twee poolwaarden beschikbaar (deze lijst zal de komende maanden waarschijnlijk evolueren: vergeet dus niet om de waarden te controleren terwijl je leest):




- 0.25 BTC`, met een inschrijfgeld van `0,0125 BTC`;
- 0.025 BTC, met een inschrijfgeld van 0,00125 BTC.



Bij elke mengcyclus kunnen tussen 5 en 10 UTXO's betrokken zijn bij de invoer en uitvoer.



![Image](assets/fr/01.webp)



## Software-eisen



Om coinjoins te maken met Whirlpool, heb je drie aparte programma's nodig:





- Ashigaru Terminal**, waarmee je je coinjoins direct vanaf je computer kunt beheren;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, de applicatie op je smartphone waarmee je overal je bitcoins kunt uitgeven in *postmix*;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, een Bitcoin node-implementatie die je een soevereine verbinding met het netwerk garandeert, zonder afhankelijkheid van een server van derden.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Installeer elk van deze tools door hun respectievelijke tutorials te volgen, waarna je kunt beginnen met het maken van je eerste coinjoins.



## Bitcoins ontvangen



Na het aanmaken van je portefeuille begin je met een enkele rekening, aangeduid met de index `0'`. Dit is de `Deposit` account. Naar deze rekening stuur je bitcoins die bestemd zijn voor coinjoins. U kunt ze ontvangen via de Ashigaru applicatie (zie deel 5 van de specifieke tutorial), of via Ashigaru Terminal (ook beschreven in deel 5 van de specifieke tutorial).



Zodra je depositorekening ten minste het bedrag bevat dat nodig is om deel te nemen aan de kleinste pool (plus servicekosten en het minimum dat nodig is om de mining kosten te dekken), ben je klaar om je eerste coinjoins te starten.



![Image](assets/fr/02.webp)



## Maak de Tx0



Zodra het geld op je stortingsrekening is aangekomen en de transactie is bevestigd, kun je het coinjoin-proces starten. Open hiervoor op Ashigaru Terminal het menu `Wallets` en selecteer je wallet. Als je wallet vergrendeld is, zal de software je om je wachtwoord en passphrase vragen.



![Image](assets/fr/03.webp)



Selecteer vervolgens de `Betaalrekening`.



![Image](assets/fr/04.webp)



Ga naar het menu `UTXOs`.



![Image](assets/fr/05.webp)



Hier zie je een lijst van alle UTXO's in je stortingsaccount. Selecteer degene die je wilt versturen in de coinjoin cycli.



Voor meer vertrouwelijkheid en om *Common Input Ownership Heuristic (CIOH)* te vermijden, wordt aanbevolen om slechts één UTXO per ingang in Whirlpool te gebruiken (een gedetailleerde uitleg van dit principe is te vinden in BTC 204).



Druk op de `ENTER` toets van je toetsenbord om een UTXO te selecteren: er verschijnt een sterretje `(*)` naast om aan te geven dat het geselecteerd is.



![Image](assets/fr/06.webp)



Klik vervolgens op de knop `Mix Selected`.



![Image](assets/fr/07.webp)



Als je een UTXO hebt die groot genoeg is om deel te nemen aan een van de twee beschikbare pools, kun je de bestemmingspool selecteren met de pijltjes. Op deze pagina zie je de details van je Tx0 :




- het aantal UTXO's dat naar de pool gaat;
- de verschillende toegepaste vergoedingen (servicekosten en mining vergoedingen) ;
- de hoeveelheid van de *doxische verandering*.



Controleer de informatie zorgvuldig en klik dan op `Broadcast` om de Tx0 uit te zenden.



![Image](assets/fr/08.webp)



Ashigaru zal dan de TXID van je Tx0 weergeven, om te bevestigen dat de transactie is uitgezonden op het netwerk.



![Image](assets/fr/09.webp)



## Samenvoegen



Zodra de Tx0 is uitgezonden, gaat u terug naar de startpagina van uw depositorekening, klikt u op `Rekeningen` en selecteert u de `Premix` account.



![Image](assets/fr/10.webp)



In het `UTXOs` menu zie je de verschillende geëgaliseerde onderdelen, klaar om de samenvoegingscycli te starten. Zodra Tx0 is bevestigd, zal Ashigaru Terminal automatisch de eerste mengcyclus starten.



![Image](assets/fr/11.webp)



Zodra de Tx0 is bevestigd, zal de eerste coinjoin transactie automatisch worden aangemaakt en uitgezonden door Ashigaru Terminal. Door naar `Rekeningen > Postmix > UTXO's` te gaan, kunt u uw geëgaliseerde UTXO's bekijken, die wachten op bevestiging van hun eerste cyclus.



![Image](assets/fr/12.webp)



Je kunt Ashigaru Terminal nu op de achtergrond laten draaien: het zal je tracks automatisch blijven mixen en remixen.



## Muntverbindingen afwerken



Nu kun je je munten zichzelf automatisch laten remixen. Het Whirlpool model betekent dat er geen extra kosten zijn voor het remixen: geen servicekosten, geen mining kosten. Uw munten laten deelnemen aan meer mengcycli kan uw vertrouwelijkheid dus alleen maar ten goede komen.



Voor een beter begrip van dit mechanisme en hoeveel cycli het de moeite waard is om op te wachten, raad ik aan dit artikel te lezen:



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Om het aantal remixen te zien dat door elk van je stukken is uitgevoerd, open je het menu `UTXOs` in de `Postmix` account.



![Image](assets/fr/13.webp)



Om uw gemengde munten uit te geven, gaat u naar de Ashigaru-applicatie, die dezelfde wallet gebruikt als uw Ashigaru Terminal-software. De wallet die bij het openen wordt weergegeven, komt overeen met uw `Betaalrekening`. Om toegang te krijgen tot de `Postmix` rekening, die je gemengde UTXO's bevat, klik je op het Whirlpool symbool in de rechterbovenhoek.



![Image](assets/fr/14.webp)



In dit account zie je al je munten die momenteel worden gemengd. Om ze uit te geven, druk je op het `+`-symbool rechtsonder in het scherm en selecteer je vervolgens `Versturen`.



![Image](assets/fr/15.webp)



Vul de details van je transactie in: het adres van de ontvanger, het te verzenden bedrag en, als je wilt, kies je een specifieke transactiestructuur om je vertrouwelijkheid verder te vergroten (zie de bijbehorende tutorials).



![Image](assets/fr/16.webp)



Controleer de transactiegegevens zorgvuldig en sleep vervolgens de pijl onder aan het scherm om de zending te bevestigen.



![Image](assets/fr/17.webp)



Je transactie is ondertekend en uitgezonden op het Bitcoin netwerk.



![Image](assets/fr/18.webp)



## Doxische verandering uitgeven



Onthoud: Het model van Whirlpool is gebaseerd op de egalisatie van je stukken op Tx0, voordat ze de pools ingaan. Het is dit mechanisme dat het volgen van UTXO's doorbreekt. Naar mijn mening is dit het meest efficiënte coinjoin-model, maar het heeft één nadeel: het genereert een *wissel* die niet door het coinjoin-proces gaat.



Deze verandering komt overeen met een UTXO aangemaakt voor elke Tx0. Het is geïsoleerd in een specifieke rekening met de naam `Doxxic Change` of `Bad Bank`, afhankelijk van de software, om te voorkomen dat het samen met je andere UTXO's wordt gebruikt. Dit is erg belangrijk, omdat deze UTXO's niet gemengd zijn: hun traceerbaarheidslinks blijven intact en ze kunnen je vertrouwelijkheid in gevaar brengen door een verbinding te leggen tussen jou en je coinjoin-activiteit. Ga er dus voorzichtig mee om en **gebruik ze nooit samen met andere UTXO's**, al dan niet gemengd. Het combineren van een giftige UTXO met een gemengde UTXO zal alle privacywinst tenietdoen die je hebt behaald met coinjoinen.



Op dit moment biedt Ashigaru geen directe toegang tot deze `Doxxic Change` account (tenminste, ik heb het nog niet gevonden). Deze functie zal waarschijnlijk worden toegevoegd in een toekomstige update. In de tussentijd is de enige manier om deze fondsen op te halen het importeren van je seed in Sparrow Wallet. Deze laatste zal normaal gesproken automatisch detecteren dat dit een wallet is die gebruikt wordt met Whirlpool en je toegang geven tot alle vier de accounts, inclusief de `Doxxic Change` account. Je kunt deze UTXO's dan uitgeven als gewone bitcoins vanuit Sparrow.



Hier zijn verschillende mogelijke strategieën om je UTXO's voor vreemde valuta van coinjoins te beheren zonder je privacy in gevaar te brengen:





- Mengen in kleinere pools:** Als je giftige UTXO groot genoeg is om zich bij een kleinere pool aan te sluiten, is dit over het algemeen de beste optie. Wees echter voorzichtig dat je nooit verschillende giftige UTXO's samenvoegt om dit te bereiken, omdat dit een link zal creëren tussen je verschillende entries in Whirlpool.





- Markeer ze als onbesteedbaar:** Een andere voorzichtige aanpak is om ze gewoon op hun aparte rekening te houden en ze onaangeroerd te laten. Dit voorkomt dat je ze per ongeluk uitgeeft. Als de waarde van bitcoin stijgt, kunnen er nieuwe pools worden geopend die zijn aangepast aan hun grootte.





- Donaties doen:** Je kunt ervoor kiezen om deze giftige UTXO's om te zetten in donaties aan Bitcoin ontwikkelaars, open-source projecten of verenigingen die BTC accepteren. Zo kun je ze op een nuttige manier weggooien en tegelijkertijd het ecosysteem steunen.





- Koop prepaid cadeaubonnen of Visa-kaarten:** Platforms zoals [Bitrefill](https://www.bitrefill.com/) stellen je in staat om je bitcoins in te wisselen voor cadeaubonnen of herlaadbare Visa-kaarten die je in winkels kunt gebruiken. Dit kan een eenvoudige en discrete manier zijn om je giftige UTXO's uit te geven.





- Ruil ze voor Monero:** Samourai Wallet bood vroeger een nu niet meer bestaande BTC/XMR atomic swap service aan. Als er een gelijkaardige dienst bestaat (ik ken er persoonlijk geen), is het een uitstekende oplossing om deze UTXO's te isoleren, ze om te zetten naar Monero en ze dan uiteindelijk terug te sturen naar Bitcoin. Deze methode was echter duur en afhankelijk van de beschikbare liquiditeit. Deze methode was echter duur en afhankelijk van beschikbare liquiditeit.





- Overbrengen naar de Lightning Network:** Deze UTXO's overbrengen naar de Lightning Network om te profiteren van lagere transactiekosten is een mogelijk interessante optie. Deze methode kan echter bepaalde informatie onthullen, afhankelijk van je gebruik van Lightning, en moet daarom met voorzichtigheid worden gebruikt.



## Hoe kan ik meer te weten komen over de kwaliteit van onze coinjoin cycli?



Een muntcombinatie is pas echt effectief als er een hoge mate van uniformiteit is tussen de invoer- en uitvoerbedragen. Deze uniformiteit verhoogt het aantal mogelijke interpretaties voor een buitenstaander, wat op zijn beurt de onzekerheid over de transactie verhoogt. Om deze onzekerheid te meten, gebruiken we het concept van entropie toegepast op de transactie. Het Whirlpool model wordt erkend als een van de meest effectieve in dit opzicht, omdat het een uitstekende homogeniteit tussen de deelnemers garandeert. Voor een meer diepgaande kijk op dit principe, raad ik je aan het laatste hoofdstuk van deel 5 van de BTC 204-opleiding te raadplegen.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

De prestaties van verschillende coinjoin-cycli worden gemeten aan de hand van de grootte van de sets waarin een munt verborgen zit. Deze verzamelingen definiëren wat bekend staat als *anonsets*. Er zijn twee soorten: de eerste meet de vertrouwelijkheid bij retrospectieve analyse (van het heden naar het verleden) en de tweede meet de weerstand bij prospectieve analyse (van het verleden naar het heden). Voor een volledige uitleg van deze twee indicatoren, lees de volgende tutorial (of, nogmaals, de BTC 204 training):



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Hoe beheer je de postmix?



Na het uitvoeren van verschillende coinjoin cycli, is de beste strategie om je UTXO's in de `Postmix` account te houden en ze oneindig te laten remixen totdat je ze echt moet uitgeven.



Sommige gebruikers geven er de voorkeur aan om hun gemengde bitcoins over te dragen naar een wallet die beveiligd is met wallet hardware. Deze optie is mogelijk, maar vereist een zekere mate van nauwkeurigheid om ervoor te zorgen dat de vertrouwelijkheid die is verkregen met coinjoins niet wordt aangetast.



Het samenvoegen van UTXO's is de meest voorkomende fout. Het is belangrijk om nooit gemengde UTXO's te combineren met ongemengde UTXO's in dezelfde transactie, anders loop je het risico dat de *Common Input Ownership Heuristic (CIOH)* wordt geactiveerd. Dit betekent dat je je UTXO's rigoureus moet beheren, met name door ze duidelijk en nauwkeurig te labelen. Over het algemeen is het samenvoegen van UTXO's een slechte praktijk die vaak leidt tot verlies van vertrouwelijkheid als het slecht beheerd wordt.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Je moet ook voorzichtig zijn met het consolideren van gemengde UTXO's. Beperkte consolidaties kunnen worden overwogen als de UTXO's significante anonsets hebben, maar ze verminderen onvermijdelijk je niveau van vertrouwelijkheid. Vermijd massale of overhaaste consolidaties, die worden uitgevoerd voordat er voldoende remixen zijn gemaakt, omdat ze afleidende verbanden kunnen leggen tussen je pre- en post-mix stukken. In geval van twijfel kun je het beste je postmix UTXO's niet consolideren en ze één voor één overbrengen naar je wallet hardware, waarbij je telkens een nieuw leeg ontvangstadres genereert. Vergeet niet elke overgebrachte UTXO te labelen.



We raden ten zeerste af om je postmix UTXO's te verplaatsen naar portefeuilles die minderheidsscripts gebruiken. Als je bijvoorbeeld deelnam aan Whirlpool vanuit een multi-sig portfolio in `P2WSH`, dan zullen er maar weinig mensen zijn die dit type script delen. Door je postmix UTXO's naar ditzelfde type script te sturen, verminder je je anonimiteit aanzienlijk. Afgezien van het type script, kunnen andere specifieke wallet fingerprints je vertrouwelijkheid in gevaar brengen, dus het beste is om ze uit te geven van de Ashigaru applicatie.



Tot slot, zoals bij alle Bitcoin transacties, mag je nooit een ontvangstadres hergebruiken. Elke betaling moet naar een nieuw, uniek, leeg adres worden gestuurd.



De eenvoudigste en veiligste methode is om je gemengde UTXO's te laten rusten in hun `Postmix` account, ze op natuurlijke wijze te laten remixen en ze alleen uit te geven wanneer nodig vanuit Ashigaru.



De Ashigaru en Sparrow wallets bevatten extra beveiligingen tegen de meest voorkomende fouten die geassocieerd worden met blockchain analyse, waardoor u de vertrouwelijkheid van uw transacties kunt behouden.