---
name: Wallet of Satoshi - Zelfbehoud
description: Ontdek hoe je de zelfbewaringsmodus van een Wallet of Satoshi portfolio configureert
---

![cover](assets/cover.webp)



***Niet jouw sleutels, niet jouw munten* is meer dan een gezegde, het is een fundamenteel principe van Bitcoin, wat betekent dat als je geen controle hebt over de **private sleutels** die jouw bitcoins ontsluiten, je ze niet echt bezit.



Veel gebruikers beginnen over het algemeen met een **custodial wallet**, en migreren dan naar een **self-custodial wallet**, waarbij ze zelf hun privésleutels beheren.


In deze tutorial laten we je niet kennismaken met een nieuwe zelfbehoudende wallet. In plaats daarvan laten we je kennismaken met een nieuwe functie van ***Wallet of Satoshi*** wallets: **de zelfustodiërende modus**.



Het doel van deze nieuwe integratie is om gebruikers in staat te stellen de controle over hun privésleutels te behouden en tegelijkertijd te profiteren van eenvoud en een vloeiende gebruikerservaring.



Voordat we tot de kern van de zaak komen, nemen we even de tijd om de speciale zelfbewaringsmodus van Wallet of Satoshi (WoS) te onderzoeken.



## Het speciale kenmerk van de zelfbewaringsmodus



De eenvoud en vloeibaarheid van de zelfbewaringsmodus van WoS elimineert de complexiteit van het openen van Lightning-kanalen, het beheren van nodes... Maar hoe is dit mogelijk?



De zelfbewaringsmodus van Wallet of Satoshi wordt aangedreven door **Spark**. Dit is een Layer 2-oplossing voor Bitcoin, gemaakt door Lightspark, met behulp van **statechains** technologie.



Als gevolg daarvan voer je je transacties niet direct uit op de Lightning Network. Interacties tussen het **LN** netwerk en **Spark** vinden plaats via **atomic swaps**.



Bob wil bijvoorbeeld een Lightning-factuur betalen met WoS. Hij maakt zijn satoshi's over, maar op de achtergrond worden deze doorgestuurd naar een **Spark Service Provider (SSP)** op Spark, die op zijn beurt de betaling uitvoert op het Lightning-netwerk.



Omgekeerd wenst Alice rechtstreeks middelen te verkrijgen uit haar WoS-portefeuille. In dit geval ontvangt de **SSP** sats via LN en crediteert onmiddellijk de portefeuille van Alice.



Dus, het is belangrijk om te weten dat om te profiteren van de eenvoud en vloeibaarheid van WoS, je afhankelijk moet zijn van Spark's servers. Echter, in termen van veiligheid, als een SSP kwaadaardig of onbeschikbaar wordt, heb je het **unilateral exit** mechanisme, een veiligheidsmaatregel die je toelaat je fondsen terug te krijgen op Bitcoin on-chain (zelfs als dit traag en duur kan zijn) , wat een zelfbewarende ervaring garandeert die vergelijkbaar is met die van een private Lightning node.



Rekening houdend met al deze parameters kun je dan beslissen hoeveel sats je in je WoS zelfbewaarplaats wilt houden.



Als je nieuw bent met Wallet of Satoshi, moet je natuurlijk de mobiele wallet toepassing downloaden. Als je het echter al gebruikt en wilt weten hoe je de **zelfbewaringsmodus** gebruikt, ga dan direct naar het **zelfbewaringsmodus configureren** gedeelte van deze tutorial.



## Aan de slag met Wallet of Satoshi



Ga naar je applicatiewinkel en download WoS.



![screen](assets/fr/03.webp)



Open de applicatie zodra het downloaden is voltooid en druk op **Start**.



![screen](assets/fr/04.webp)



Je wordt doorgestuurd naar de hoofdinterface van de applicatie. Als je WoS voor het eerst opent, is de portefeuille al functioneel en wordt deze standaard in de bewaarmodus geopend.



![screen](assets/fr/05.webp)



Zelfs als je WoS niet in custodial modus wilt gebruiken, raden we je aan om het eerst te configureren. Raadpleeg daarvoor deze tutorial.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Laten we verder gaan met de configuratie van onze WoS in zelfbewaarneming.



## Configuratie zelfbewaringsmodus



Klik op het hamburgermenu (pictogram met 3 balken) in de rechterbovenhoek van de hoofdinterface.



![screen](assets/fr/06.webp)



Klik dan in het menu dat verschijnt op het submenu **Open Self Custody Wallet**.



![screen](assets/fr/07.webp)



WoS vertelt je onmiddellijk dat *zelfbewaringsmodus komt met een herstelzin. Je bent ook zelf verantwoordelijk voor de veiligheid van je fondsen*.



![screen](assets/fr/08.webp)



Vink de toets "**I Understand**" (1) aan en druk vervolgens op de toets **Open Self Custody Wallet** (2), die in helder geel verschijnt.



![screen](assets/fr/09.webp)



### Een zelfbewarende portefeuille samenstellen



Nadat u op de knop **Open Zelfbehoud Wallet** hebt geklikt, klikt u op de knop **Maak een nieuwe Wallet**.



![screen](assets/fr/10.webp)



WoS maakt dan een self-custodial portfolio voor je aan, wederom binnen dezelfde applicatie. Je kunt op elk gewenst moment schakelen tussen **custodial** modus (beschikbaar in bepaalde regio's) en **self-custodial** modus.



![screen](assets/fr/11.webp)



Eenmaal aangemaakt, wordt u doorgestuurd naar de hoofdinterface van WoS self-custody. Je zult merken dat er geen verschillen zijn tussen het algemene overzicht en de interfaces van een WoS bewaarportefeuille en die van een WoS zelfbewaarportefeuille.



### Uw geheugensteunzin opslaan



Tik op het **Keychain + Backup Wallet** icoon bovenaan het scherm tussen de Wallet of Satoshi naam en het hamburgermenu.



![screen](assets/fr/12.webp)



WoS biedt twee verschillende manieren om je 12 woorden (mnemonische zin) op te slaan: **back-up via Google Drive** en **handmatige back-up**.



Hoewel we aanraden om een handmatige back-up te maken, wat het veiligst is, laten we je ook zien hoe je een back-up maakt via Google Drive.



#### Back-up maken via Google Drive



Klik op de knop **Google Drive Backup**.



![screen](assets/fr/13.webp)



Als je kiest voor een back-up met Google Drive, is het risico groot dat je Google-account in gevaar komt. Een kwaadwillende zou toegang hebben tot het bestand met je 12 woorden en zou zo toegang kunnen krijgen tot je wallet.



Het toevoegen van een wachtwoord om het bestand met je 12 woorden te versleutelen is zeker een goede manier om een extra beveiligingslaag toe te voegen.



Activeer daarom de knop **Vercijferen met een wachtwoord** in de geavanceerde opties.



![screen](assets/fr/14.webp)



Stel in de nieuwe interface die verschijnt een sterk wachtwoord in en bevestig het opnieuw.



![screen](assets/fr/15.webp)



Het is belangrijk om te onthouden dat als je eenmaal een wachtwoord hebt gekozen, je het niet mag vergeten of de drager waarop je het hebt geschreven mag verliezen. Als je het vergeet of verliest, heb je nooit meer toegang tot je 12 woorden, en dus tot je fondsen.



Nadat je je wachtwoord hebt gekozen, selecteer je een Google-account voor de back-up en geef je WoS toegang.



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



Wacht een paar seconden. Bingo! Uw back-up is met succes voltooid.



![screen](assets/fr/18.webp)



Je hebt altijd de mogelijkheid om een extra back-up te maken door de tweede back-upmethode te kiezen: handmatige back-up.


#### Handmatige back-up



Als je kiest voor handmatige back-up, raden we je ten zeerste aan deze tutorial te raadplegen, waarin de best practices voor het veilig back-uppen van je mnemonic phrase worden besproken, zodat je de toegang tot je bitcoins niet verliest.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Druk op de knop **Handmatige back-up**.



![screen](assets/fr/19.webp)



Op de volgende interface herinnert WoS je aan enkele veiligheidsmaatregelen waarmee je rekening moet houden voordat je verdergaat met de handmatige back-up.



Activeer de knop **Ik begrijp** en druk op de knop **Next**.



![screen](assets/fr/20.webp)



Je krijgt dan je 12 woorden te zien. Sla ze op en klik op de knop **Volgende**.



![screen](assets/fr/21.webp)



Druk op deze nieuwe interface de woorden in de juiste volgorde in.



![screen](assets/fr/22.webp)



Klik ten slotte op de knop **Volgende**. Gefeliciteerd! Uw back-up is nu voltooid.



![screen](assets/fr/23.webp)



## Herstel van portefeuille in eigen beheer



Wanneer je je WoS self-custody wallet wilt herstellen of terugzetten na een telefoonwissel of om een andere reden, zijn hier de stappen die je moet volgen.



Om de WoS-portefeuille te openen, klik je op het hamburgermenu in de rechterbovenhoek van de hoofdinterface.


Klik in het menu dat verschijnt op het submenu **Open Self Custody Wallet**.


Druk in de nieuwe interface die verschijnt op de **Restore Existing Wallet** knop.



![screen](assets/fr/24.webp)



Kies een herstelmethode en ga door naar de volgende stap.



![screen](assets/fr/25.webp)



### Herstellen via Google Drive



1. Druk op de knop **Herstel van Google Drive**.


2. Selecteer een Google-account en laat WoS de herstelgegevens ophalen die op je Google Drive zijn opgeslagen.


3. Voer vervolgens je coderingswachtwoord in (als je dat eerder had gedefinieerd, natuurlijk) uit het bestand met je 12 woorden.


4. Wacht enkele ogenblikken tot het herstel in werking treedt en je hebt weer toegang tot je portfolio.



### Handmatige restauratie



1. Druk op de knop **Handmatig herstellen**.


2. Voer vervolgens de 12 woorden van je geheugensteunzin in, waarbij je elk woord voor het startnummer schrijft.


3. Wacht enkele ogenblikken tot het herstel in werking treedt en je hebt weer toegang tot je portfolio.




### Bitcoins overzetten tussen WoS-bewaarneming en WoS-zelfbewaarneming



Als je bitcoins (sats) in je WoS custody wallet hebt en een WoS self-custody wallet aanmaakt, raak je je fondsen niet kwijt. Beter nog, je kunt ze overzetten naar je self-custody portefeuille en vice versa.



Om dit te doen :


Je kunt je bliksem WoS self-custody adres kopiëren of een factuur die je hebt gemaakt.



![screen](assets/fr/26.webp)



Open nu je bewaar wallet en druk op de **Envoyer** knop.



Plak vervolgens het adres of de factuur. Druk een tweede keer op **Envoyer**.



Ga terug naar je zelfbewaarde portefeuille en je zult zien dat je het geld inderdaad had ontvangen.



![screen](assets/fr/27.webp)



## Bitcoins versturen en ontvangen



Wat betreft het verzenden en ontvangen van bitcoins in self-custody modus, net als het algemene overzicht en de interfaces, zijn ze niet anders dan het verzenden en ontvangen van bitcoins via een WoS custody wallet.



Raadpleeg de basistutorial over het gebruik van Wallet of Satoshi op het Plan₿ Netwerk.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

U kunt Wallet of Satoshi nu zelf configureren en bedienen in zelfbewaringsmodus.



Als je deze les nuttig vond, laat dan hieronder een groene duim achter. Hartelijk dank!