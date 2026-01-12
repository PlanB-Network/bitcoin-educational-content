---
name: Alias Vault
description: Krachtige tool voor het beheren van wachtwoorden, twee-factor authenticatie en aliassen (met ingebouwde e-mailserver) - Ook zelf te hosten!
---

![cover](assets/cover.webp)



Online privacy en beveiliging is een onderwerp dat iedereen, ongeacht zijn of haar bedrijf, goed in de gaten moet houden.



Deze kwesties maken bovendien deel uit van een wereld die voortdurend in beweging is: steeds meer ontwikkelaars nemen deel aan het onderwerp en brengen implementaties voor gevestigde oplossingen en nieuwe producten.



Dit is het geval met **Leendert de Borst** en zijn `Alias Vault`, een revolutionaire tool (de eerste in zijn soort) waarmee je wachtwoorden kunt beheren en opslaan, wachtwoordrecords kunt gebruiken om je te authenticeren bij webservices, twee-factor authenticatie kunt beheren, maar vooral generate echte _aliassen_ kunt beheren, allemaal in één Interface.



**Maar daar stopt Alias Vault niet**.



## Belangrijkste kenmerken



Alias Vault werkt in de cloud op de servers van de ontwikkelaar of zelf gehost in zijn eigen infrastructuur, een optie waarvoor Docker-bestanden en image beschikbaar zijn om te installeren met een scipt. Naast de web Interface zijn er extensies beschikbaar voor alle populaire browsers, evenals mobiele apps voor iOS en Android; de laatste kan ook worden gedownload van F-Droid, waarbij de officiële Google store wordt omzeild.



In één Interface is Alias Vault:




- Gratis en open bron**
- Password Manager**, om alle complexe wachtwoorden op te slaan. Met behulp van de browserextensie voltooit de wachtwoordmanager aanmeldingen op websites
- 2FA**, ter ondersteuning van verificatie met twee factoren
- Alias manager met ingebouwde e-mailserver**: Alias Vault maakt geen aliassen aan die e-mail doorsturen naar de mailbox van een gebruiker, maar maakt echte alter-ego's aan, compleet met voornaam, achternaam, geslacht, gebruikersnaam, wachtwoord en verjaardag (als deze informatie vereist is).



Een uitgebreide en grondige documentatie maakt deel uit van het pakket, dat nieuwkomers zal begeleiden bij het ontdekken van deze krachtige tool.



## Geen persoonlijke gegevens!



Het begint, zoals altijd, vanaf de [aliasvault.net](aliasvault.net) website. Zoals gezegd kan Alias Vault worden gebruikt op de eigen server, of vanuit de cloud van de ontwikkelaar om ermee kennis te maken voordat wordt overgestapt op de zelf gehoste oplossing.



De site heeft echt in het oog springende en goed onderhouden graphics, maar het goede komt pas als je het in handen krijgt: **maak je account aan**.



![img](assets/en/01.webp)



Tot je grote verrassing zul je merken dat Alias Vault niet om persoonlijke informatie vraagt: het enige wat je nodig hebt om de account aan te maken is een bijnaam, een woord dat je kent, zolang het maar beschikbaar is. Ga akkoord met de Servicevoorwaarden, kies het woord en ga verder.



![img](assets/en/02.webp)



Stel nu het **`hoofdwachtwoord`** in, dit is de belangrijkste informatie in je hele nieuwe systeem. Met dit ene wachtwoord ben jij in feite de enige die toegang heeft tot het account, omdat het je `vault` versleuteld houdt op de server die je informatie zal hosten.



![img](assets/en/03.webp)



Feit: U hebt uw eigen wachtwoordmanager en aliasmanager gemaakt, maar zonder uw eigen werkende, privé e-mail Address op te geven.



![img](assets/en/04.webp)



Alias Vault heet je welkom in een veilige, nieuwe, persoonlijke maar ook lege ruimte. En nu beginnen we het een beetje te bevolken.



Als je al een wachtwoordmanager hebt, kun je het bestand importeren van degene die je gebruikt om de verschillen met andere aanbieders te evalueren, of misschien de aliasmanager elimineren zodat je alles in één applicatie kunt beheren.



![img](assets/en/05.webp)



Alias Vault is heel eenvoudig: je hebt één hoofdpagina, namelijk `Home`, met twee menu's:




- `Credentials`: hiermee kun je identiteiten en aliassen aanmaken en beheren
- `Email`: een inbox waar je binnenkomende berichten kunt controleren op aliassen die je hebt aangemaakt.



![img](assets/en/06.webp)



We zijn geïnteresseerd in het aanmaken van een eerste `alias`, dus ga naar de rechterbovenhoek van de pagina en klik op _+New Alias_.



![img](assets/en/07.webp)



In eerste instantie ziet het menu er minimaal uit, volgens de filosofie van Alias Vault. Om de mogelijkheden van deze functie te ontdekken, klik je op _Create via advanced mode_.



![img](assets/en/08.webp)



Het bovenste deel van het eerste scherm kun je gebruiken om wachtwoordgegevens te importeren die je al gebruikt voor diensten waar je een abonnement op hebt, of die je het vaakst online gebruikt.



Als u twee-factor authenticatie hebt ingeschakeld op een (of alle) van de bovenstaande diensten, kunt u met Alias Vault ook deze extra Layer van beveiliging beheren door de `geheime sleutel` te importeren. Alias Vault creëert de `TOTP` die nodig is voor toegang.



![img](assets/en/09.webp)



**Let op**: In de ruimte die is gereserveerd voor de e-mail Address, stelt Alias Vault standaard zijn eigen domein voor; om de juiste Address te gebruiken waarmee je eerder accounts hebt aangemaakt, klik je op _Enter custom domain_, zodat je na `@` het juiste domein kunt instellen.



![img](assets/en/14.webp)



Het onderste deel van dit scherm is het leukst. Klik op _Generate Random Alias_ en Alias Vault maakt aparte identiteiten voor je aan voor verschillende behoeften, elk met een eigen mailbox, zeer robuuste wachtwoorden op niveau, aangevuld met andere gegevens zoals geslacht, geboortedatum en een geschikte bijnaam.



![img](assets/en/10.webp)



Vanuit een bijbehorend menu kunt u de instellingen wijzigen die van invloed zijn op het genereren van wachtwoorden, zoals het kiezen van alleen kleine letters en het elimineren van tekens die dubbelzinnig kunnen zijn.



![img](assets/en/11.webp)



Je kunt de alias e-mail gebruiken die wordt voorgesteld door Alias Vault, of domeinen wijzigen als je op het bijbehorende vervolgkeuzemenu klikt.



![img](assets/en/12.webp)



Voordat je deze e-mail gebruikt voor een aanmeldservice, kun je de functionaliteit testen door een bericht van een eigen Address naar de nieuw aangemaakte mailbox te sturen.



![img](assets/en/13.webp)



**⚠️ WAARSCHUWING**: Het ontvangen van e-mails is mogelijk dankzij de ingebouwde server van Alias Vault, maar hiermee kunt u alleen e-mails ontvangen en niet beantwoorden of de e-mailbox gebruiken met de "conventionele" functies van een `alias` service. Het verschilt dus sterk van Simple Login, Addy en andere platforms die zich uitsluitend op dit soort diensten richten. Voor het voorbeeld van Simple Login kun je de speciale tutorial bekijken:



https://planb.academy/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

Om een alias te verwijderen die je als test hebt aangemaakt, hoef je alleen maar in te loggen op je `Home`, dan `Credentials` en te klikken op de identiteit die je wilt verwijderen. De _Delete_ opdracht verschijnt in de rechterbovenhoek zodat je verder kunt gaan.



![img](assets/en/16.webp)



## Browser extensie



Afhankelijk van wat je nodig hebt, kun je je toevlucht nemen tot de browserextensie, die te vinden is in de meest gebruikte browsers.



![img](assets/en/15.webp)



Het installeert zoals je al deed met alle andere extensies, dus ik zal niet uitweiden over dat detail.



De browserextensie is er om het gemakkelijker te maken om in te loggen bij online diensten of om nieuwe aliassen aan te maken als dat nodig is: als de dienst is opgeslagen in je Alias Vault-records, doet de auto-fill wat nodig is.



![img](assets/en/17.webp)



De enige voorzichtigheid is om te controleren of Alias Vault actief is. De applicatie heeft namelijk een standaardinstelling waarbij het pauzeert na een periode van inactiviteit. Dit is een zeer nuttige functie, **als je bijvoorbeeld even weg moet van je computer om te voorkomen dat iemand anders toegang krijgt tot je accounts**. Een gestroomlijnde procedure stelt je in staat om opnieuw in te loggen door het `master password` in te voeren, als de vorige sessie nog in de cache zit. De tijd om uit te loggen is een van de parameters die je kunt aanpassen en naar wens kunt verkorten of verlengen.



## Mobiele app



Zoals alle zichzelf respecterende apps van dit soort heeft Alias Vault een versie voor mobiele apparaten, in zowel Android- als iOS-omgevingen. Voor Android kun je de app downloaden van [F-Droid](https://f-droid.org/packages/net.aliasvault.app/).



Op het moment van dit schrijven (eind augustus 2025), beschouwt de mobiele app `auto-fill` als een experimentele functie, die niet werkt behalve met zeer weinig sites. Totdat deze volledig is geïmplementeerd, moet je voor het gebruik van Alias Vault op mobiel gegevens kopiëren/plakken.



Zodra je de app hebt gedownload uit de store, voer je om in te loggen gewoon de gebruiker en het `masterwachtwoord` in die je hebt aangemaakt op de webapp.



![img](assets/en/18.webp)



Bij het openen van uw `vault` wordt u gevraagd of u biometrisch gecontroleerde toegang wilt inschakelen, een extra Layer beveiliging om te voorkomen dat iemand anders toegang krijgt tot uw wachtwoorden als diegene toevallig uw telefoon in handen heeft.



![img](assets/en/19.webp)



Als je beslist om biometrische controle in te stellen, ga je gang. Als je de stap overslaat en je bedenkt je, dan kun je het later ook nog instellen via het _Instellingen_ menu.



Zodra u klaar bent met inloggen, ziet u dat de gegevens die u al hebt aangemaakt weer gesynchroniseerd zijn.



![img](assets/en/20.webp)



De mobiele app kan worden doorgestuurd naar de link naar de `vault` die op de eigen server wordt gehost.



![img](assets/en/22.webp)



En het is precies de zelfgehoste versie die we in de volgende sectie kort zullen behandelen in Address.



## Self-Hosting: volledige controle over uw gegevens



Alias Vault, om eerlijk te zijn, is niet de eerste `wachtwoordmanager` waarmee je de service op je infrastructuur kunt implementeren. Er zijn anderen, maar sommige hebben beperkingen of zijn gedeeltelijk closed source.



De kans is uniek: **beëindig de afhankelijkheid van externe serviceproviders of clouds, maar gebruik uw eigen lokale server om de wachtwoorden, aliassen en uiterst gevoelige informatie die met dit alles gepaard gaat te bewaken en te beheren**. Met Alias Vault kunt u de e-mailservice ook laten verwijzen naar uw eigen e-mailserver voor extra vertrouwelijkheid.



Het is tijd om naar [documentatie](https://docs.aliasvault.net/installation/) te gaan, om uit te vinden hoe je Alias Vault zelf kunt hosten.



![img](assets/en/23.webp)



Alias Vault draait op Docker Compose, dus minimale ervaring met Linux en Docker is vereist. Je kunt beginnen met de basisinstallatie en daarna verder gaan met meer geavanceerde oplossingen.



Je server moet draaien op een 64-bits machine, met een Linux-distributie, 1 GB RAM en minstens 16 GB opslagruimte; de versie van Docker (CE) moet minstens 20.10 of hoger zijn, terwijl Docker Compose een versie vanaf 2.0 vereist.



Ik besloot om Alias Vault uit te proberen met een thin client, waarop DietPi is geïnstalleerd als distributie, een Debian Bookworm basis, geoptimaliseerd tot de essentie en waarop `Docker` en `Docker Compose` al draaien.



Maak eerst een map aan in je home, open `terminal` en plak het commando om het installatiescript uit te voeren.



```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```



![img](assets/en/24.webp)



![img](assets/en/25.webp)



Wanneer de installatie is voltooid, vind je je toegangsgegevens:


```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```



Controleer de inhoud van de map na de installatie.



![img](assets/en/29.webp)



Gebruik het commando om Alias Vault te starten:



``` Start-Alias-Kluis


./install.sh start


```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```


localhost/gebruiker/start


```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```



![img](assets/en/31.webp)



## Overwegingen over encryptie en beveiliging



![img](assets/en/32.webp)



Volgens wat Lanedirt zegt op de site, in de documentatie en op Github, blijft met Alias Vault **alle informatie (componenten) die je op Alias Vault plaatst, strak gebonden aan het apparaat, versleuteld en ontoegankelijk voor iedereen die het `master password` niet kent**.



Het `hoofdwachtwoord` is dus het fundamentele element van de hele `kluis`. Nadat het is ingevoerd, wordt het verwerkt met het `Argon2id` algoritme, een sleutelafleidingsfunctie uit het Hard geheugen, om te voorkomen dat het geheim het apparaat verlaat.



Alles blijft verborgen, zelfs voor de beheerder van de cloud of de hostingservice. In feite heb je vanuit het beheerderspaneel geen toegang tot gebruikersgegevens, je kunt alleen weten of ze aliassen hebben aangemaakt, e-mails hebben ontvangen en verder weinig.



Alle opgeslagen inhoud wordt versleuteld en ontsleuteld met cryptografische sleutels die zijn afgeleid van het `hoofdwachtwoord`. **Alleen versleutelde gegevens worden opgeslagen op de server, niets verschijnt in platte tekst**. Als een gebruiker zijn hoofdwachtwoord vergeet of verliest, is de account die eraan gekoppeld is onherroepelijk verloren, omdat de server geen toegang heeft tot de platte tekst.



Voor de zelf gehoste versie is er het script om het `master password` te resetten, maar dit voorkomt gegevensverlies niet.



![img](assets/en/33.webp)



Aangezien Alias Vault zich in het _Beta_ stadium bevindt, kan het zijn dat je problemen hebt om toegang te krijgen als je het hoofdwachtwoord wijzigt/bijwerkt. Ik stel voor dat u vanaf het begin een robuust en complex wachtwoord kiest, zodat u kunt experimenteren met de service en uiteindelijk kunt beslissen of u het wilt gebruiken. Als u na het bijwerken van het wachtwoord problemen hebt met toegang tot de cloud, neem dan contact op met de ondersteuning van Alias Vault.



Voor een volledig begrip van de architectuur en beveiliging van Alias Vault, raad ik u ten zeerste aan om [deze pagina](https://docs.aliasvault.net/architecture/) te raadplegen, die details bevat over de cryptografie die ten grondslag ligt aan de werking.



## Wegenkaart


Het is de bedoeling van de ontwikkelaars om Alias Vault volwassen en stabiel te maken voor het einde van 2025, om zo de toekomstige gebruikskenmerken te definiëren.



Alias Vault is en blijft open source en gratis, maar waarschijnlijk niet onbeperkt zoals in bèta. Sommige betaalde functies worden momenteel geïmplementeerd, zoals al is aangekondigd.



Er zijn team/familieplannen en ondersteuning voor hardwaresleutels, de laatste voor authenticatie met FIDO2 of WebAuth.



## Wie heeft Alias Vault nodig?



**Een tool als deze is ideaal voor iedereen die online privacy op de eerste plaats zet**.



Uw identiteit vormt naar alle waarschijnlijkheid de kern van de zaken die u online doet en moet met alle middelen worden beschermd om **die** gegevens weg te houden van services, bedrijven en tussenpersonen die er alles aan willen doen om uw online gedrag in handen te krijgen.



Alias Vault geeft je weer volledige controle over je referenties, waardoor je niet of nauwelijks afhankelijk bent van derden om je meest gevoelige gegevens te bewaken en te versleutelen.



De architectuur en cryptografische faciliteiten van Alias Vault zijn ideaal voor soevereine individuen, kleine en middelgrote bedrijven, ontwikkelteams en alle **open source** applicatie enthousiastelingen. Als u in een van deze categorieën valt: veel plezier met het ontdekken van Alias Vault.