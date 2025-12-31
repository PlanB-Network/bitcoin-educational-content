---
name: White Noise
description: Een besloten, gedecentraliseerde berichtentoepassing gebaseerd op de Nostr en MLS protocollen
---

![cover](cover.webp)




## Inleiding



"Te midden van moeilijkheden liggen kansen". Dit citaat van Albert Einstein herinnert ons eraan dat problemen niet definitief zijn, maar de zaden bevatten van nieuwe, innovatieve oplossingen.



De motivaties achter de lancering van de oplossing die we in deze tutorial presenteren, illustreren dit perfect. Het is **White Noise**, geboren uit noodzaak.



In de woorden van de oprichter, Max Hillebrand, waarover *Bitcoin Magazine* bericht: "We zijn dit project gestart bij gebrek aan alternatieven." Hij legt uit dat "bestaande versleutelingstoepassingen inefficiënt zijn op grote schaal: 100 mensen toevoegen aan een groepsgesprek vertraagt de versleuteling aanzienlijk. Gedecentraliseerde platformen bieden ondertussen geen privé berichten. Het open relaysnetwerk van Nostr stelt iedereen in staat om ideeën te verspreiden, maar de bescherming van directe berichten blijft dramatisch ontoereikend. We realiseerden ons: om vrijheid te beschermen, moesten we deze systemen samenvoegen."



## Wat is White Noise?



White Noise is een open source berichtentoepassing ontwikkeld door een team zonder winstoogmerk. De applicatie bevordert veiligheid, privacy en decentralisatie. In tegenstelling tot conventionele toepassingen is er geen telefoonnummer of e-mailadres nodig.


White Noise onderscheidt zich door de integratie van twee fundamentele protocollen - Nostr en MLS - die de technische basis vormen.



Nostr (Notes and Other Stuff Transmitted by Relays) is een gedecentraliseerd, open-source protocol dat is ontworpen om censuur te weerstaan.  Het protocol gebruikt relais, sleutelparen en clients.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Met white Noise kun je zelfs je eigen relay-instellingen kiezen voor maximale privacy.



MLS (Messaging Layer Security) daarentegen is een beveiligingsprotocol dat end-to-end versleuteling van berichten mogelijk maakt. Met andere woorden, berichten zijn alleen toegankelijk voor de eindpunten, d.w.z. de verzender en ontvanger van het bericht. Dit betekent dat relais die betrokken zijn bij het routeren van berichten geen toegang hebben tot de inhoud ervan.



Hier is een snelle vergelijking tussen White Noise en een aantal van de bekendste berichtentoepassingen.



| Points de comparaisons      | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| Chiffrement E2EE / 1:1      | ✅ Oui       | Facultatif | ✅ Oui           | ✅ Oui   | ✅ Oui    | ✅ Oui            | ✅ Oui  |
| Chiffrement de groupe E2EE  | ✅ Oui       | ❌ Non      | ✅ Oui           | ✅ Oui   | ✅ Oui    | Facultatif       | ✅ Oui  |
| Anonymisation de l'identité | ✅ Oui       | Facultatif | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Serveur open source         | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Client open source          | ✅ Oui       | ✅ Oui      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Serveur décentralisé        | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Année de création           | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |


## Aan de slag met White Noise



### White Noise installatie



Ga naar de [White Noise website] (https://www.whitenoise.chat/) en klik op **Download**.



![screen](assets/fr/03.webp)



White Noise is momenteel alleen beschikbaar op mobiele apparaten.


Druk op in de nieuwe interface die verschijnt:





- de **Zapstore** of **Android APK** knop als je het wilt downloaden op Android ;
- op de knop **iOS TestFlight** als je een iPhone gebruikt.



![screen](assets/fr/04.webp)



In deze tutorial gaan we een Android-download uitvoeren.


Als je kiest voor downloaden via **Zapstore**, dan word je daar naartoe geleid. Eenmaal op Zapstore, typ **White Noise** in de zoekbalk. Ga dan verder met downloaden door op **Installeren** te klikken.



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



Als je ervoor kiest om het APK-bestand te downloaden, word je doorgestuurd naar de White Noise GitHub repository om de juiste versie voor je smartphone te kiezen.



De beschikbare APK-bestanden zijn :





- whitenoise-0.2.1-arm64-v8a.apk** (57,7 MB), geschikt voor recente telefoons met 64-bits processors;
- whitenoise-0.2.1-armeabi-v7a.apk** (47.5 MB) geschikt voor oudere telefoons met 32-bits processors.



Je hebt ook **.sha256** bestanden, die gewoon controlesommen zijn om de integriteit van de download te verifiëren.



![screen](assets/fr/07.webp)



Zodra de download is voltooid, installeert en opent u de toepassing.



![screen](assets/fr/08.webp)



### Initiële instelling gebruikersaccount



Voor uw eerste verbinding met White Noise drukt u op de **Register** knop.



![screen](assets/fr/09.webp)



Configureer vervolgens je profiel door een profielfoto en een naam te kiezen en een korte beschrijving van jezelf toe te voegen. Je hoeft je echte identiteit (naam en foto) niet in te vullen.


Merk op dat White Noise automatisch een naam (pseudoniem) voor je kiest, die je kunt houden of veranderen. Druk ten slotte op de **Einde** knop.



![screen](assets/fr/10.webp)



U wordt doorgestuurd naar het **homescherm** van White Noise, waar uw gesprekken worden weergegeven. Uw account is nu ingesteld en klaar voor gebruik. U kunt uw profiel delen of vrienden zoeken om een chat te starten.



![screen](assets/fr/11.webp)




### White Noise interfaces ontdekken



In de hoofdinterface zie je bovenaan het scherm :



In de linkerbovenhoek is het profielicoon een miniatuur van je profielfoto of de eerste letter van je profielnaam. Klik erop om naar je accountinstellingen te gaan.



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



In de rechterbovenhoek vind je het pictogram om een nieuw gesprek te starten.



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## Instellingen gebruikersaccount



Druk op het profielpictogram in de linkerbovenhoek om de instellingen te openen.



![screen](assets/fr/16.webp)



Bovenaan de interface **Instellingen** vind je je foto en profielnaam, gevolgd door je publieke sleutel die je kunt delen met behulp van de QR-code ernaast.



![screen](assets/fr/17.webp)



Net daaronder vind je de knop **Verander account**, waarmee je verbinding kunt maken met een ander profiel binnen de applicatie.



![screen](assets/fr/18.webp)



Dan heb je een eerste sectie met vier (4) submenu's zoals :





- Profiel wijzigen**



In dit submenu kunt u de profielnaam, het Nostr adres (NIP-05)... wijzigen. Vergeet niet op **Opslaan** te klikken om je wijzigingen op te slaan.



![screen](assets/fr/19.webp)





- Profielsleutels**



Hier heb je toegang tot je publieke en private (geheime) sleutels. White Noise herinnert je eraan dat je privésleutel onder geen beding openbaar mag worden gemaakt.



![screen](assets/fr/20.webp)





- Netrelais



In dit submenu kun je **algemene relais** (relais gedefinieerd voor gebruik in al je Nostr toepassingen), **inbox relais** en **key pack relais** toevoegen of verwijderen.



Om dit te doen, tik je op het **vuilnis** pictogram voor een relais om het te verwijderen, of tik je op het **+** (plus) pictogram om een nieuw relais toe te voegen.



![screen](assets/fr/21.webp)





- Loskoppelen**



Klik op dit submenu om je account los te koppelen van de applicatie. Maar zorg ervoor dat je je privésleutels offline hebt opgeslagen, anders kun je je later niet meer aanmelden.



![screen](assets/fr/22.webp)




Een tweede sectie biedt submenu's:





- Toepassingsinstellingen



Hier kun je het uiterlijk (thema en weergavetaal) van de applicatie definiëren en zelfs gegevens verwijderen als je denkt dat deze gecompromitteerd zijn of als je je zelf in gevaar voelt.



![screen](assets/fr/23.webp)





- Doneer aan White Noise



Je kunt het team achter White Noise (een non-profitorganisatie) steunen met donaties via hun Lightning-adres of hun Bitcoin stille betaaladres.



![screen](assets/fr/24.webp)



Helemaal onderaan staan de **ontwikkelaarsinstellingen**.



![screen](assets/fr/25.webp)




## Een gesprek beginnen



Laten we eens kijken hoe je een gesprek begint. Op het moment van schrijven biedt White Noise drie communicatieopties. We verkennen achtereenvolgens **Privégesprekken** (**Chat 1:1**), d.w.z. tussen jou en één andere persoon, **Groepsgesprekken** en **Mediabestanden versturen**.




### Kat 1:1



Om een nieuwe correspondent toe te voegen, klik je in de hoofdinterface op het pictogram om een nieuw gesprek te starten.


Scan vervolgens de QR-code van de publieke sleutel (1) of plak de publieke sleutel (2) van je nieuwe correspondent in de zoekbalk om hem of haar te vinden.



![screen](assets/fr/26.webp)



Tik vervolgens op de knop **Start gesprek** om een gesprek te starten met je correspondent. Je kunt je correspondent ook **Volgen** of hem/haar uitnodigen voor een groepsgesprek door op de knop **Toevoegen aan groep** te drukken.



![screen](assets/fr/27.webp)



Je eerste bericht aan een nieuwe correspondent is vergelijkbaar met een uitnodigingsverzoek. Dit verzoek moet worden geaccepteerd door je correspondent voordat je met hem/haar kunt communiceren. Als hij/zij weigert, wel, dan is er geen gesprek mogelijk.



![screen](assets/fr/28.webp)



Bovendien kunnen ze de inhoud van je eerste bericht niet lezen zolang ze je uitnodiging niet accepteren.



Zodra hij je uitnodiging accepteert, kan hij je antwoorden en kunnen jullie naadloos en veilig communiceren.



![screen](assets/fr/29.webp)



Bovendien heb je in een discussie extra functionaliteiten.



U kunt lang op een specifiek bericht drukken om opties weer te geven zoals :




- reageren op het bericht met een emoji (1) ;
- maak een **direct citaat** om het bericht te beantwoorden door op **Reply** (2) te drukken;
- kopieer het bericht door op **Kopie** (3) te drukken.



![screen](assets/fr/30.webp)





- verwijder een bericht alleen met de knop **Verwijder** als het van jou afkomstig is.



![screen](assets/fr/31.webp)



Je kunt binnen een gesprek zoeken.



Klik op de avatar van de correspondent bovenaan het scherm om naar "gespreksinformatie" te gaan en tik op de knop **Zoek in gesprek**.



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



Typ in de zoekbalk die verschijnt het woord waarop je wilt zoeken en start de zoekopdracht. Je ziet dan je zoekwoorden gemarkeerd in **vet**.



![screen](assets/fr/34.webp)




### Groepsgesprekken



Gespreksgroepen kunnen worden aangemaakt op White Noise.



Om dit te doen, raak je het pictogram aan in de opstartinterface van een nieuw gesprek en klik je vervolgens op **Nieuw groepsgesprek**. Voer vervolgens in de zoekbalk de publieke sleutel in van het eerste lid dat u aan uw groep wilt toevoegen.



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



Als deze optie niet werkt, voer dan in de interface **Een nieuw gesprek starten** de publieke sleutel in van het eerste lid dat je aan de groep wilt toevoegen in de zoekbalk. Je kunt ook de QR-code scannen die bij zijn of haar publieke sleutel hoort.



In plaats van op de knop **Gesprek starten** te tikken, klikt u deze keer op de knop **Aan groep toevoegen**.



![screen](assets/fr/37.webp)



Tik in het pop-upmenu dat verschijnt op **Nieuw groepsgesprek**.



![screen](assets/fr/38.webp)



Druk vervolgens op **Doorgaan** (u hoeft de openbare sleutel niet opnieuw in te voeren).



![screen](assets/fr/39.webp)



Als maker van de groep ben je automatisch de beheerder. Vul de groepsgegevens in, zoals **groepsnaam en -beschrijving**, en klik vervolgens op de knop **Groep aanmaken**.



![screen](assets/fr/40.webp)



De gebruiker die je als eerste lid toevoegt, en alle anderen die je later toevoegt, ontvangen een melding waarin ze worden uitgenodigd om lid te worden van de groep. Ze moeten akkoord gaan door op **Aanvaarden** te klikken om lid te worden van de groep.



![screen](assets/fr/41.webp)



Het is ook mogelijk om een nieuw lid met wie je al aan het chatten bent toe te voegen aan een bestaande groep. Klik hiervoor op de avatar van de correspondent bovenaan het scherm om naar de "gespreksinformatie" te gaan en tik op de knop **Toevoegen aan groep**.



![screen](assets/fr/42.webp)



In de nieuwe interface die verschijnt, **vink** de groep aan waaraan je hem wilt toevoegen en tik op **Toevoegen aan groep**. Je hoeft alleen nog maar te wachten tot hij akkoord gaat om zich bij de groep aan te sluiten.



![screen](assets/fr/43.webp)



Merk op dat alleen een groepsbeheerder groepsinformatie kan wijzigen en leden kan toevoegen of verbannen. Sleutelrotatie voorkomt ook dat verbannen leden toekomstige berichten kunnen ontsleutelen.



Om een lid te verwijderen, tikt u in de hoofdinterface van de groep op het groepspictogram bovenaan om de interface met groepsinformatie te openen.



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



Klik vervolgens op de naam van het lid en **Verwijderen uit groep**. Vanuit deze interface kun je hem ook een bericht sturen, volgen of toevoegen aan een andere groep.



![screen](assets/fr/46.webp)



### Multimediabestanden verzenden



Op dit moment kunnen op White Noise alleen foto's worden gedeeld tussen gebruikers. Of je nu in een privégesprek bent of in een groepschat, om dit te doen, moet je :





- druk op het symbool **plus (+)** aan de linkerkant van het invoerveld voor tekstberichten.



![screen](assets/fr/47.webp)





- klik dan onderaan op het vakje **Foto's** om naar je galerij te gaan.



![screen](assets/fr/48.webp)





- kies de foto('s) om te verzenden.



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## Belangrijke punten om te onthouden



White Noise biedt een goed niveau van vertrouwelijkheid en superieure beveiliging. Aan de andere kant is het een zeer recente toepassing, niet erg wijdverspreid en nog in de kinderschoenen. Bijgevolg is het nog te vroeg om actieve conclusies te trekken. Het is mogelijk dat er tijdens het gebruik enkele storingen optreden.



Op dit moment mist het bepaalde functionaliteiten (geen audio- of videogesprekken, geen verzending van audio- of videomediabestanden) in vergelijking met populaire berichtentoepassingen.



Desondanks blijft White Noise een interessante optie voor gesprekken waarbij vertrouwelijkheid van het grootste belang is (bijvoorbeeld met familie, goede vrienden of activisten voor een gemeenschappelijk doel), ook al kost het een beetje moeite om het te installeren (via alternatieve applicatiewinkels of APK-bestanden) en te leren (een beetje het concept van sleutelparen, clients en relays met het Nostr protocol onder de knie krijgen).



Nu weet je hoe je White Noise kunt gebruiken om veilig te communiceren met je vrienden en familie. Geef ons een duimpje omhoog als je deze tutorial nuttig vindt.



We raden je onze tutorial over Tox Chat aan, een applicatie waarmee je kunt chatten zonder tussenpersonen via het gedecentraliseerde Tox protocol.



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3