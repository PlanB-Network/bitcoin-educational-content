---
name: Ocean Mining

description: Inleiding tot Ocean Mining
---

![signup](assets/cover.webp)


**mei 2024**


Ocean Mining is een enigszins unieke Mining pool. Hier zijn geen accounts, e-mailadressen of wachtwoorden nodig. Net als Bitcoin is alles transparant, pseudoniem en kunnen bijdragers kiezen uit vier verschillende bloksjablonen.


### Compensatiesysteem


Het vergoedingssysteem van Ocean heet TIDES, "Transparent Index of Distinct Extended Shares". Dit systeem registreert het werk van de miners, bekend als "shares". De pool berekent het percentage "aandelen" voor elke bijdrager en voegt vervolgens hun Bitcoin Address toe aan de bloksjabloon van de pool als begunstigde van dit percentage van de Block reward.


Het blokkensjabloon wordt ongeveer elke 10 seconden bijgewerkt om rekening te houden met de meest lucratieve nieuwe transacties en om de verdeling van de Block reward te wijzigen als dat nodig is.


![signup](assets/rem.webp)


Het maakt niet uit of je machines verbonden zijn of niet op het moment dat de pool een nieuw blok ontgint. Het reeds ingediende werk wordt bewaard voor de volgende acht blokken die door de pool worden gevonden.


Het werk voor acht blokken bewaren in plaats van de tellers op nul te zetten bij elk nieuw gedolven blok, betekent dat je compensatie pas 100% is als de pool acht blokken heeft gevonden nadat je bent begonnen met bijdragen. Dit betekent ook dat je gecompenseerd blijft worden voor acht blokken als je stopt met bijdragen aan de pool.


Dit mechanisme vlakt de compensatie af en ontmoedigt "poolhoppen", waarbij regelmatig van pool wordt gewisseld afhankelijk van welke pool het meest waarschijnlijk het volgende blok zal vinden.


### Opnames


De werking van Ocean Mining stelt zijn bijdragers in staat om "schone" bitcoins terug te krijgen, dat wil zeggen bitcoins die direct door Block reward zijn uitgegeven.


In tegenstelling tot de meeste andere pools, ontvangt Ocean de nieuw gemijnde bitcoins niet; de adressen van de bijdragers zijn direct geïntegreerd in het bloksjabloon.


Voorlopig is het minimumbedrag om echt te profiteren van de schone bitcoins 1.048.576 Sats. Bij elk blok dat door de pool wordt gedolven, moet jouw "aandeel" recht geven op meer dan 1.048.576 Sats om direct door de Block reward aan jou te worden uitbetaald.

Anders wordt je Sats door Ocean bewaard totdat je totale beloning dit bedrag overschrijdt.


Alle bitcoins die Ocean tijdelijk bewaart, staan op deze Address: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, alles is verifieerbaar op de TimeChain.](https://Mempool.space/Address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)

Het is ook mogelijk om je Sats op te nemen via Lightning met BOLT12. We zullen kijken hoe we dit kunnen instellen.


### Zwembadkosten


De kosten variëren van 0% tot 2%, afhankelijk van het gekozen bloksjabloon.


## De transparantie van de oceaan


### Gegevens contribuant


![signup](assets/1.webp)


Alle informatie over de pool is transparant, inclusief alle gebruikersgegevens. Laten we een voorbeeld nemen om dit punt te begrijpen:


[Op het Ocean dashboard] (https://ocean.xyz/dashboard), heb je talrijke stukjes informatie zoals de Hashrate over de laatste zes maanden, het aantal deelnemers in de pool, het totale aantal gemijnde bitcoins, enz.


We zullen ons concentreren op de "Contributors" sectie. Je kunt de lijst van alle bijdragers zien met hun gemiddelde Hashrate over de laatste drie uur en ook het percentage **"shares"** en **"Hash"** ten opzichte van de rest van de pool.


**"Aandelen %"** is het percentage werk geleverd door de bijdrager in het venster van de laatste acht blokken vergeleken met de rest van de pool.


**"Hash %"** is het percentage van de gemiddelde Hashrate geleverd door de bijdrager over de laatste drie uur vergeleken met de rest van de pool.


![signup](assets/2.webp)


Je zult zien dat de "Contributors" worden aangeduid met een Bitcoin Address. Je kunt op elk van deze adressen klikken voor meer details.


Als we de eerste nemen, degene met de hoogste Hashrate [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), dan kun je alle details over deze gebruiker zien: Hashrate, aantal gemijnde bitcoins, met welk blok, en zelfs de details van elk van hun machines (ASIC's). Ze blijven echter anoniem, net als bij Bitcoin.


### Blok Sjabloon


Linksboven op het dashboard zie je "Volgende blok". Op deze pagina zijn er vier verschillende bloksjablonen. Ocean stelt elke medewerker in staat om het bloksjabloon te kiezen dat hij of zij wil ondersteunen. Dit heeft geen directe invloed op je compensatie. Als de pool een blok minen, worden alle deelnemers gecompenseerd, ongeacht het sjabloon dat ze hebben gekozen. Hierdoor kan iedereen gewoon "stemmen" voor het bloksjabloon dat bij hen past.


![signup](assets/3.webp)


**CORE:** Toeslag 2%, dit is het klassieke Bitcoin core sjabloon zonder filter, zoals geschreven op hun pagina "Inclusief transacties en de meeste spam"


**CORE+ANTISPAM:** Toeslag 0%, Bitcoin core met een filter tegen bepaalde transacties zoals Ordinals "Inclusief transacties en beperkt spam"


**OCEAN:** Vergoeding 0%, Bitcoin Knot "Omvat alleen transacties en redelijk kleine gegevens"


**DATA-VRIJ:** Toeslag 0%, Bitcoin Knot "Omvat alleen transacties zonder willekeurige gegevens"


### Onderscheid tussen Bitcoin core en Bitcoin knoop

Bitcoin core is de software waarmee ongeveer 99% van de Bitcoin knooppunten over de hele wereld kan werken. Bitcoin is een protocol, wat betekent dat er, net als op het internet, waar meerdere browsers zijn, verschillende softwareprogramma's naast elkaar kunnen bestaan op dezelfde TimeChain. Echter, uit zorg voor compatibiliteit en om het risico van bugs te beperken die onuitwisbare sporen op de TimeChain zouden achterlaten, werken bijna alle Bitcoin ontwikkelaars op Bitcoin core. Bitcoin Knots is een Fork van Bitcoin core, wat betekent dat het het grootste deel van hun code deelt, wat het risico op bugs sterk beperkt. Deze Fork is gemaakt door Luke Dashjr, die meer beperkende regels wilde toepassen dan Bitcoin core, zonder een Hard Fork te maken. Nu bestaan Bitcoin core en Bitcoin knopen naast elkaar dankzij de consensus van Nakamoto.


## Een werknemer toevoegen


Om een worker toe te voegen, begin je met het kiezen van je bloksjabloon. Deze keuze bepaalt de pool URL die je op je Miner (ASIC's) moet invoeren.



- **CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- **CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- **OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- **DATA-VRIJ**: `stratum+tcp://datafree.mine.ocean.xyz:3404`


Voer vervolgens in het gebruikersveld een Bitcoin Address in die je bezit. Hier is de lijst met compatibele Address types:


- **P2PKH** (Origineel Address type. Begint met "1")
- **P2SH** (Meerdere handtekeningen of P2SH-SegWit. Begint met "3")
- **Bech32** (SegWit. Begint met "bc".)
- **Bech32m** (Taproot. Begint met "bc". Langer dan Bech32.)


Als je meerdere mijnwerkers hebt, kun je voor allemaal dezelfde Address invoeren, zodat hun Hash tarieven gecombineerd worden en als één Miner verschijnen. Je kunt ze ook van elkaar onderscheiden door ze elk een eigen naam te geven. Om dit te doen, voeg je gewoon ".workername" toe na de Bitcoin Address.


Gebruik ten slotte `x` voor het wachtwoordveld.


**Voorbeeld:**

Als je het **OCEAN** sjabloon kiest, je Bitcoin Address is `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` en je wilt je Miner "Brrrr" noemen, dan moet je de volgende informatie invoeren in de Interface van je Miner:



- **URL**: `stratum+tcp://mine.ocean.xyz:3334`
- **GEBRUIKER**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- **WACHTWOORD**: `x`


Enkele minuten na het opstarten van Mining, kun je je gegevens zien op de Ocean site door te zoeken naar je Address.


### Dashboard Overzicht


- **Aandelen in Beloningsvenster**: Deze gegevens geven het aantal aandelen aan, het werk dat je naar de pool hebt gestuurd in het venster van de laatste 8 blokken die door de pool zijn gedolven.
- **Geschatte beloningen in vensters**: Schatting van het aantal Sats dat je zult verdienen met het werk dat je al hebt gedaan. Hierbij wordt geen rekening gehouden met transactiekosten, maar alleen met de coinbase, de nieuwe bitcoins die door het netwerk worden uitgegeven.
- **Geschatte verdiensten volgende blok**: Schatting van het aantal Sats dat wordt verdiend als er nu een blok wordt gedolven. Onthoud, als deze waarde minder is dan 1.048.576 Sats, ontvang je de Sats niet direct op je Address. Ze worden naar Ocean's Address gestuurd. Ze worden naar Ocean's Address gestuurd, totdat jouw verdiensten deze drempel overschrijden.


Hieronder zie je een grafiek die je Hashrate geschiedenis tot 6 maanden weergeeft.


![signup](assets/4.webp)


Hier zie je je gemiddelde Hashrate over verschillende tijdschalen, van 60 tot 24 uur, evenals de geschiedenis van blokken die zijn gedolven door de pool waarvoor je hebt bijgedragen en bent beloond.


![signup](assets/5.webp)


Je hebt de optie om een CSV-bestand van deze geschiedenis te exporteren met de knop **Download CSV**.


![signup](assets/6.webp)


In de volgende sectie heb je een lijst van alle mijnwerkers die je met deze Address aan de pool hebt gekoppeld. Je hebt natuurlijk hun individuele Hashrate, maar ook het aantal Sats dat ze individueel hebben ontvangen voor hun werk.


![signup](assets/7.webp)


Je kunt op de **Nickname** van een Miner klikken. Je krijgt dan alle informatie die we net zagen, maar dan specifiek voor die Miner.


En onderaan de pagina vind je aanvullende informatie over de geschiedenis van de betalingen op je Address, de Sats die je hebt gedolven maar nog niet hebt ontvangen, en het totale aantal Sats dat je hebt gedolven.


![signup](assets/8.webp)


Hier kun je zien dat in het vak **Estimated Time Until Minimum Payout** staat Lightning omdat we een BOLT12-aanbieding hebben ingesteld.


### Lightning-opnames instellen


Zoals je hebt begrepen, streeft Ocean naar maximale transparantie en minimale bewaring (het voor jou bewaren van je Sats).


Daarom is het voor Lightning-opnames nodig om **BOLT12-aanbiedingen** te gebruiken. Dit is een nieuwe manier van betalen op de Lightning Network die in 2024 opkomt en verschillende dingen mogelijk maakt:


- Het is een herbruikbare betaallink, waardoor automatische betalingen mogelijk zijn en, in tegenstelling tot een Lightning Address, is de BOLT12 niet ongeldig.
- Het is ook een betaalmethode die bewijs levert dat de betaling is verricht, wat niet het geval is met LNURL's.
- Heel belangrijk, het kan gebruikt worden in combinatie met een Bitcoin handtekening om te bewijzen dat je zowel de houder bent van de BTC Address als van de BOLT12 aanbieding.

Vanaf vandaag (mei 2024) bestaan er weinig oplossingen om deze methode te gebruiken. In dit voorbeeld gebruiken we een Start9-server met Core Lightning. Wanneer andere tools, zoals bijvoorbeeld Phoenix Wallet, BOLT12-aanbiedingen hebben geïntegreerd, blijft deze tutorial van toepassing. Zorg ervoor dat je open kanalen hebt met inkomende liquiditeiten, anders werken betalingen niet.


Ga eerst naar je dashboard op de Ocean site door je BTC Address in te voeren en klik dan op het tabblad **Configuratie**.


![signup](assets/9.webp)


We kopiëren hier de tekst **Beschrijving**:

`OCEAN Uitbetalingen voor bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv``


Ga nu naar je Core Lightning Interface op je Start9-server (of een Wallet die een BOLT12-aanbod kan leveren).


![signup](assets/10.webp)


Klik op **Ontvangen**.


Vink **Aanbieding** aan, plak dan de eerder gekopieerde tekst in het veld **Beschrijving** en laat het veld **Bedrag** leeg.


![signup](assets/11.webp)


Klik op **generate aanbieding**.


![signup](assets/12.webp)


Je hebt een herbruikbare en permanente betaallink gegenereerd waarvoor geen centrale server nodig is zoals bij Lightning-adressen. Kopieer de link en keer terug naar de Ocean-pagina.


Plak de betaallink in het veld **Lightning BOLT12 Offer** en laat het veld **Block Height** op de standaardwaarde staan. Klik op **generate**.


![signup](assets/13.webp)


Om Ocean te verzekeren dat deze betaallink inderdaad van jou is zonder een accountsysteem te gebruiken, moet je het zojuist gegenereerde bericht ondertekenen met je privésleutel die overeenkomt met de Bitcoin Address die je gebruikt. Er bestaan veel oplossingen om een bericht te ondertekenen met uw privésleutel. In deze tutorial nemen we het voorbeeld van BlueWallet, maar de methode is hetzelfde voor alle wallets.


![signup](assets/14.webp)


Ervan uitgaande dat je privésleutel in BlueWallet zit (je kunt hetzelfde doen met een Hardware Wallet), klik je op de betreffende Wallet.


![signup](assets/15.webp)


Dan op de **...** rechtsboven.


![signup](assets/15bis.webp)


En **Teken/Verifieer bericht**.


![signup](assets/16.webp)


In dit venster heb je drie velden: **Address**, **Handtekening** en **Bericht**.


In het veld **Address** voer je Bitcoin Address in. Als we teruggaan naar ons voorbeeld, is het de Address: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.


Laat het veld **Handtekening** leeg.

En plak het gegenereerde bericht in het **Bericht** veld op de pagina van Ocean: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`

Klik op **Aanmelden**.


Dit zal generate een cryptografische handtekening opleveren die bewijst dat jij de eigenaar bent van de Address `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`, en deze handtekening is uniek dankzij het bericht van Ocean, gegenereerd vanuit de BOLT12 betaallink.


![signup](assets/17.webp)


Kopieer de handtekening en plak deze op de pagina van Ocean en klik vervolgens op **CONFIRM**.


![signup](assets/18.webp)


Je zou een bevestigingsbericht moeten zien.


![signup](assets/19.webp)


Ga nu naar het tabblad **Mijn statistieken**. Bovenaan wordt aanvullende informatie weergegeven met de BOLT12-betalingslink die u eerder hebt gegenereerd met Core Lightning op Start9.


![signup](assets/20.webp)