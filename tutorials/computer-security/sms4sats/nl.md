---
name: SMS4Sats
description: Ontvang en verstuur anoniem sms'jes door te betalen in Bitcoin Lightning
---

![cover](assets/cover.webp)



SMS-verificatie is een must geworden voor veel online diensten. Of het nu is om een account aan te maken op een platform, een registratie te valideren of een identiteit te bevestigen, websites vragen bijna systematisch om een telefoonnummer. Deze wijdverspreide praktijk vormt een groot probleem voor iedereen die zijn privacy wil beschermen: je persoonlijke nummer wordt een permanente identificatiecode, die je verschillende digitale activiteiten koppelt aan je echte identiteit en de deur openzet voor ongewenste commerciële verzoeken.



**SMS4Sats** speelt op dit probleem in door tijdelijke telefoonnummers aan te bieden voor het ontvangen en versturen van SMS berichten. De dienst onderscheidt zich door zijn niet-registratiemodel en exclusieve Bitcoin betaling via Lightning Network. Voor een paar satesjis krijg je een wegwerpnummer waarmee je een registratie kunt valideren zonder ooit je persoonlijke nummer te onthullen.



Deze handleiding leidt je door de drie SMS4Sats functies: een verificatie SMS ontvangen, een anonieme SMS versturen en een tijdelijk nummer huren voor enkele uren.



## Wat is SMS4Sats?



SMS4Sats is een online dienst die toegankelijk is op [sms4sats.com](https://sms4sats.com) en die anoniem SMS-beheer via betaling in Bitcoin Lightning mogelijk maakt. De dienst biedt drie verschillende functionaliteiten: ontvangst van verificatiecodes voor eenmalig gebruik, versturen van sms'jes naar elk willekeurig nummer en verhuur van tijdelijke nummers voor meerdere uren.



### Filosofie en bedrijfsmodel



Het project is ontworpen om maximale vertrouwelijkheid en financiële soevereiniteit te garanderen. Door geen account aan te maken en alleen Bitcoin Lightning betalingen te accepteren, elimineert SMS4Sats de noodzaak om persoonlijke gegevens te verstrekken. Er is geen e-mailadres, creditcard of persoonlijke informatie nodig. Alleen een Lightning-betaling is vereist om toegang te krijgen tot de diensten.



De service ondersteunt meer dan 400 sites en applicaties in ongeveer 120 landen en dekt daarmee de meeste verificatiebehoeften. Deze uitgebreide geografische dekking maakt validatie van registraties op verschillende platforms mogelijk, van sociale netwerken tot berichtendiensten.



### Voorwaardelijk betalingsmodel



SMS4Sats gebruikt voorwaardelijke Lightning facturen (hodl facturen) voor haar SMS ontvangst functionaliteit. Dit mechanisme zorgt ervoor dat je alleen wordt gefactureerd als de SMS daadwerkelijk is ontvangen. Als er geen bericht binnenkomt binnen de toegewezen tijd (maximaal 20 minuten), wordt de betaling automatisch geannuleerd en worden de satoshi's teruggestuurd naar je wallet. Deze garantie geldt niet voor de verzend- en huurfuncties, die niet worden terugbetaald.



## De drie functies van SMS4Sats



De interface van SMS4Sats is georganiseerd rond drie tabbladen die overeenkomen met drie verschillende toepassingen: **RECEIVE** om verificatiecodes te ontvangen, **SEND** om anonieme SMS te versturen en **RENT** om een tijdelijk nummer te huren.



### SMS ontvangen



Met de hoofdfunctie kun je een tijdelijk nummer krijgen om een unieke verificatiecode te ontvangen. Zodra de code is ontvangen en gebruikt, wordt het nummer permanent gedeactiveerd.



### Een sms verzenden



Met deze functie kun je een sms versturen naar een willekeurig telefoonnummer zonder je identiteit te onthullen. De ontvanger ontvangt het bericht van een anoniem nummer.



### Een act huren



Voor gebruikers die meerdere SMS berichten willen ontvangen op één nummer, biedt SMS4Sats een tijdelijke huur optie. Met deze optie kunt u meerdere berichten ontvangen en versturen tijdens de huurperiode.



**Noot over prijzen** : De prijzen in deze handleiding zijn indicatief. Ze variëren afhankelijk van het land van het nummer, de doeldienst en de huidige vraag. Een sms naar Telegram Frankrijk kan bijvoorbeeld tussen 1.500 en 5.000 satoshis kosten, afhankelijk van de voorwaarden. Controleer altijd het exacte bedrag van de Lightning-factuur voordat u betaalt.



## Een verificatie-SMS ontvangen



Laten we in detail bekijken hoe je SMS4Sats gebruikt om een verificatiecode te ontvangen, geïllustreerd door het aanmaken van een Telegram account.



### Stap 1: Selecteer land en service



Ga naar [sms4sats.com](https://sms4sats.com) en blijf op de **RECEIVE** tab. Selecteer het land van het gewenste nummer in het vervolgkeuzemenu. Als de doelservice van je abonnement wordt vermeld, selecteer deze dan om de kans op ontvangst te optimaliseren.



![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)



In dit voorbeeld selecteren we Frankrijk als land en Telegram als doeldienst. Klik op **NEXT** om door te gaan naar de volgende stap.



### Stap 2: Betaal de Lightning-factuur



Een bliksemfactuur wordt weergegeven in de vorm van een QR-code. Het bedrag varieert naargelang het land en de geselecteerde dienst. Scan de QR-code met je Lightning wallet of kopieer de factuur om handmatig te betalen.



![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)



Let op het belangrijke bericht: "Geen sms-code = geen betaling". Als je geen sms ontvangt, wordt je betaling automatisch geannuleerd en terugbetaald binnen maximaal 20 minuten.



### Stap 3: Ontvang het tijdelijke nummer



Zodra de betaling is bevestigd, wordt het tijdelijke telefoonnummer onmiddellijk weergegeven. Een teller toont de resterende tijd om de sms te ontvangen.



![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)



Kopieer dit nummer (hier +33 7 74 70 09 66) om het te gebruiken voor de dienst waarvoor je je wilt registreren.



### Stap 4: Gebruik het nummer op de doelservice



Voer het tijdelijke nummer in op de applicatie of website waar je je account aanmaakt. In ons Telegram voorbeeld voer je het nummer in, bevestig je het en wacht je op de verificatiecode.



![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)



Het proces is identiek aan de conventionele registratie: je voert het nummer in, Telegram stuurt een verificatiecode per sms en vervolgens maak je een account aan.



### Stap 5: De verificatiecode ophalen



Keer terug naar de SMS4Sats interface. Zodra de SMS is ontvangen, wordt de activeringscode automatisch weergegeven. Klik op **COPY CODE** om deze eenvoudig te kopiëren.



![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)



Voer deze code in op de doelservice om je registratie te voltooien. Het tijdelijke nummer wordt dan permanent gedeactiveerd.



## Anoniem een sms versturen



Met SMS4Sats kun je ook sms-berichten naar elk nummer sturen zonder je identiteit te onthullen.



### Stap 1: Het bericht schrijven



Klik op het tabblad **Verstuur**. Voer het telefoonnummer van de bestemming met het internationale kengetal in en schrijf je bericht (maximaal 1600 tekens).



![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)



Klik op **NEXT** om door te gaan naar de betaling.



### Stap 2: Betalen en verzenden



Betaal de Lightning-factuur die wordt weergegeven. Zodra de betaling is bevestigd, wordt de sms onmiddellijk naar de ontvanger verzonden.



![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)



Er wordt een bevestigingscode weergegeven om te bevestigen dat het bericht is verzonden. De ontvanger ontvangt de sms van een anoniem nummer.



## Een tijdelijk nummer huren



Voor gebruik waarbij meerdere sms-berichten op hetzelfde nummer nodig zijn, kun je met de functie HUREN een nummer voor meerdere uren huren.



### Huurconfiguratie



Klik op het tabblad **Verhuur**. Selecteer het land en de duur.



![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)



**Belangrijke punten om op te merken:**




- Prijzen variëren per land en verblijfsduur
- Huurprijzen worden niet terugbetaald**, in tegenstelling tot sms-berichten voor eenmalig gebruik
- Gehuurde nummers werken over het algemeen niet met Telegram
- Deze optie is geschikt voor het abonneren op meerdere diensten na elkaar



Zodra je op **NEXT** hebt geklikt en de Lightning-factuur hebt betaald, krijg je een nummer dat je voor de duur van de huurperiode kunt gebruiken om sms-berichten te ontvangen en te versturen.



## Voordelen en beperkingen



### Hoogtepunten



**Geen persoonlijke gegevens nodig**: Het model zonder registratie garandeert dat er geen persoonlijke gegevens worden verzameld.



**Drie extra functies**: Ontvangen, verzenden en huren dekken de meeste behoeften.



**Betaling alleen in Bitcoin** : Lightning Network staat directe en pseudonieme transacties toe.



**Automatische terugbetaling**: Bij het ontvangen van sms-berichten garandeert het hodl-facturatiesysteem dat je alleen betaalt als de sms aankomt.



### Te overwegen beperkingen



**Relatieve beveiliging van SMS-kanalen**: SMS-codes zijn geen robuuste verificatiemethode en mogen niet worden gebruikt voor gevoelige accounts.



**Variabele compatibiliteit**: Veel sites detecteren en blokkeren virtuele nummers. Er kunnen meerdere pogingen nodig zijn.



**Niet-herbruikbare nummers**: Na eenmalig gebruik wordt het nummer gerecycled en kan het niet worden teruggewonnen.



**Huren zonder terugbetalingsgarantie**: In tegenstelling tot eenmalige SMS-berichten, geldt voor verhuur geen geld-terug-garantie.



## Beste praktijken



### Gebruik Tor voor meer privacy



SMS4Sats is toegankelijk via [Tor](sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion). Deze configuratie maskeert je IP-adres wanneer je toegang krijgt tot de service.



### Kritieke accounts vermijden



Gebruik nooit een wegwerpnummer voor je belangrijke accounts (bank, belangrijkste e-mail). Als deze platformen vereisen dat je je nummer op een later tijdstip opnieuw valideert, verlies je de toegang tot de account.



### Scheid uw digitale identiteiten



Voor pseudonieme accounts combineer je het tijdelijke nummer met een wegwerp e-mailadres en een browser die je niet normaal gebruikt.



### Kies een stevige 2FA



Nadat je account is aangemaakt, activeer je sterkere authenticatieoplossingen: TOTP-toepassing (Aegis, Ente Auth) of FIDO2 fysieke beveiligingssleutel.



## Conclusie



SMS4Sats is een complete oplossing voor vertrouwelijk SMS-beheer. Of je nu een verificatiecode wilt ontvangen, een anoniem bericht wilt versturen of een tijdelijk nummer wilt huren, de service voldoet aan een groot aantal vertrouwelijkheidsbehoeften, dankzij betaling in Bitcoin Lightning.



Houd echter rekening met de beperkingen: de dienst garandeert geen absolute anonimiteit en is niet geschikt voor gevoelige of langdurige accounts. Als je SMS4Sats verstandig gebruikt en je bewust bent van de beperkingen, is het een praktisch hulpmiddel om weer controle te krijgen over je telefoongesprekken.



## Bronnen





- [SMS4Sats officiële website](https://sms4sats.com)
- [Service FAQ](https://sms4sats.com/faq)
- [Tor-adres](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)