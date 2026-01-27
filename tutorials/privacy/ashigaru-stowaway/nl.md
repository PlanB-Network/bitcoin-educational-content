---
name: Ashigaru - Stowaway
description: Hoe maak ik een Payjoin transactie op Ashigaru?
---
![cover](assets/cover.webp)



> *Dwing blockchain spionnen om alles wat ze denken te weten te heroverwegen.*

Payjoin is een Bitcoin transactiestructuur die ontworpen is om de vertrouwelijkheid van de gebruiker te verbeteren door een directe samenwerking met de ontvanger van de betaling. Er bestaan verschillende implementaties om de implementatie te vergemakkelijken en het proces te automatiseren. De bekendste is ongetwijfeld Stowaway, oorspronkelijk ontwikkeld door het Samurai Wallet team en nu geïntegreerd in de fork Ashigaru.



## Hoe werkt Stowaway?



Zoals eerder vermeld, integreert Ashigaru een PayJoin tool genaamd `Stowaway`. Deze is beschikbaar in de Ashigaru app op Android. Om een Payjoin uit te voeren, moet de ontvanger (die ook de rol van medewerker op zich neemt) software gebruiken die compatibel is met Stowaway, op dit moment dus alleen Ashigaru.



Stowaway is gebaseerd op een categorie transacties die Samurai "Cahoots" noemt. Een Cahoot is een gezamenlijke transactie tussen meerdere gebruikers, waarbij informatie wordt uitgewisseld buiten de Bitcoin blockchain om. Ashigaru biedt momenteel twee Cahoots tools aan: Stowaway (Payjoins) en StonewallX2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Cahoots transacties vereisen de uitwisseling van gedeeltelijk ondertekende transacties tussen gebruikers. Dit proces kan lang en vervelend zijn, vooral als het op afstand wordt uitgevoerd. Het is echter nog steeds mogelijk om dit handmatig te doen, als de medewerkers zich op dezelfde locatie bevinden. Concreet betekent dit het scannen van vijf QR-codes na elkaar, uitgewisseld tussen de twee deelnemers.



Op afstand wordt deze methode te complex. Om dit te verhelpen heeft Samourai een op Tor gebaseerd versleuteld communicatieprotocol genaamd "*Soroban*" ontwikkeld. Dankzij Soroban zijn de uitwisselingen die nodig zijn voor een Payjoin geautomatiseerd en vinden ze op de achtergrond plaats.



Deze versleutelde communicatie vereist een verbinding en authenticatie tussen de deelnemers van Cahoot. Daarom vertrouwt Soroban op de Paynyms van gebruikers. Als je nog niet weet hoe Paynyms werken, bekijk dan deze tutorial voor meer informatie:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

In een notendop is een Paynym een unieke identificatiecode die aan uw wallet is gekoppeld en waarmee u verschillende functies kunt activeren, waaronder versleutelde uitwisselingen. Het heeft de vorm van een identificatiecode en een afbeelding. Hier is bijvoorbeeld degene die ik gebruik op de Testnet:



![Image](assets/fr/01.webp)



**Samengevat:**





- payjoin" = Specifieke samenwerkingsstructuur voor transacties;





- `Stowaway` = Payjoin implementatie beschikbaar op Ashigaru ;





- `Cahoots` = Naam gegeven door Samourai aan al hun soorten gezamenlijke transacties, in het bijzonder de Payjoin `Stowaway`, vandaag overgenomen op Ashigaru ;





- soroban = Gecodeerd communicatieprotocol opgezet op Tor dat samenwerking met andere gebruikers mogelijk maakt in een `Cahoots` transactie;





- paynym" = Unieke wallet identificatie gebruikt om communicatie tot stand te brengen met een andere gebruiker op "Soroban", om een "Chahoots" transactie uit te voeren.



Voor een meer diepgaande kijk op hoe Payjoins werken en hun nut in onchain privacy, raad ik deze andere tutorial aan:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Hoe maak ik een verbinding tussen Paynyms?



Om te beginnen moet je natuurlijk Ashigaru installeren en een :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Om een Cahoots transactie op afstand uit te voeren, inclusief een PayJoin (*Stowaway*) via Ashigaru, moet u eerst de gebruiker waarmee u wilt samenwerken "volgen" via hun Paynym. In het geval van een Stowaway, betekent dit het volgen van de persoon naar wie u bitcoins wilt sturen. Als u nog niet weet hoe u een andere Paynym moet volgen, vindt u de gedetailleerde procedure in deze tutorial :



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Hoe maak ik een Payjoin op Ashigaru?



Om een Stowaway transactie uit te voeren, klikt u op de afbeelding van uw Paynym in de linkerbovenhoek van het scherm en opent u het menu `Samenwerken`. De persoon die samen met u deelneemt aan de transactie moet hetzelfde doen, tenzij u persoonlijk QR-codes uitwisselt.



![Image](assets/fr/02.webp)



Je hebt twee opties: selecteer `Initiate` als je de verzender van de betaling bent, of `Participate` als je de begunstigde van deze samenvoeging bent.



![Image](assets/fr/03.webp)



Als je de ontvanger bent, is de procedure heel eenvoudig. Voor samenwerking op afstand via het Soroban-netwerk klik je op `Deelnemen`, kies je de account die je wilt gebruiken en druk je op `LISTEN FOR CAHOOTS REQUESTS` om te wachten op de aanvraag die de betaler stuurt.



![Image](assets/fr/04.webp)



Aan de andere kant, voor in-person samenwerking via het scannen van QR-codes, ga je naar de startpagina van je wallet, druk je op het QR-codepictogram bovenaan het scherm en scan je de QR-code van de betaler die de transactie initieert.



![Image](assets/fr/05.webp)



Als je de rol van betaler hebt, dus degene die de transactie initieert, ga dan naar het menu `Samenwerken` en selecteer vervolgens `Initieer`.



![Image](assets/fr/06.webp)



Voor het type transactie, aangezien we een Payjoin Stowaway willen maken, kies deze optie.



![Image](assets/fr/07.webp)



Je kunt dan kiezen tussen online samenwerking (*Cahoots* via *Soroban*) of face-to-face samenwerking, met QR-code uitwisselingen.



![Image](assets/fr/08.webp)



### Cahoots online



Als je de `Online` optie hebt gekozen, selecteer dan de ontvanger van de Paynyms die je volgt.



![Image](assets/fr/09.webp)



Klik op `Transactie instellen` en kies vervolgens de rekening waarvan je de uitgave wilt doen.



![Image](assets/fr/10.webp)



Op de volgende pagina voer je de transactiegegevens in: het bedrag dat naar de ontvanger moet worden gestuurd en het tarief. Het is niet nodig om een ontvangstadres in te voeren, omdat de ontvanger dit zelf doorgeeft tijdens PSBT uitwisselingen.



Klik vervolgens op `Review transaction setup`.



![Image](assets/fr/11.webp)



Controleer de informatie zorgvuldig, zorg ervoor dat je medewerker luistert naar de *Cahoots* verzoeken en klik dan op de groene `BEGIN TRANSACTIE` knop om de uitwisseling van PSBTs via Soroban te starten.



![Image](assets/fr/12.webp)



Wacht tot beide deelnemers de transactie hebben ondertekend en zend deze dan uit op het Bitcoin netwerk.



![Image](assets/fr/13.webp)



### Persoonlijke gesprekken



Als je de inwisseling persoonlijk wilt uitvoeren, selecteer dan het `STONEWALL X2` transactietype en kies vervolgens de `In Persoon / Handmatig` optie.



![Image](assets/fr/14.webp)



Klik op `Transactie instellen` en kies vervolgens de rekening waarvan je de uitgave wilt doen.



![Image](assets/fr/15.webp)



Op de volgende pagina voer je de transactiegegevens in: het bedrag dat naar de ontvanger moet worden gestuurd en het tarief. Het is niet nodig om een ontvangstadres in te voeren, omdat de ontvanger dit zelf doorgeeft tijdens PSBT uitwisselingen.



Klik vervolgens op `Review transaction setup`.



![Image](assets/fr/16.webp)



Controleer de details en druk vervolgens op de groene knop `BEGIN TRANSACTION` om te beginnen met het uitwisselen van PSBT's via het scannen van QR-codes.



![Image](assets/fr/17.webp)



De uitwisseling gebeurt door afwisselend te scannen met de medewerker: klik op `SHOW QR CODE` om je QR code aan je medewerker te tonen, die hem zal scannen. Hij zal dan klikken op `SHOW QR CODE` om de zijne weer te geven, en u scant het met `LAUNCH QR Scanner`. Herhaal dit proces tot alle vijf uitwisselingsstappen voltooid zijn.



![Image](assets/fr/18.webp)



Zodra alle uitwisselingen zijn voltooid, controleer je de details van de transactie en geef je deze vrij door de groene pijl onder aan het scherm te slepen.



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). De structuur is als volgt:



![Image](assets/fr/20.webp)



*Krediet: [mempool.space](https://mempool.space/)*



Als we deze transactie analyseren, zien we mijn UTXO van `164.211 sats` aan de invoerzijde, evenals de UTXO van `190.002 sats` die toebehoort aan de werkelijke ontvanger van de betaling. Aan de uitvoerzijde ontvang ik een UTXO van `63.995 sats`, terwijl de ontvanger een UTXO van `290.002 sats` ontvangt. Als we de inputs en outputs vergelijken, zien we dat de ontvanger inderdaad `100.000 sats` heeft verdiend, wat overeenkomt met het bedrag van mijn werkelijke betaling, en dat ik `100.000 sats` heb verloren, waarbij ik de mining kosten heb opgeteld.



Uiteraard kan ik deze structuur beschrijven omdat ik de transactie zelf heb gebouwd. Maar voor een waarnemer van buitenaf is het over het algemeen onmogelijk om te bepalen welke UTXO's bij welke deelnemer horen, zowel bij de invoer als bij de uitvoer.



Om je kennis van onchain privacy management op Bitcoin te verdiepen, raad ik je aan mijn BTC 204 training op Plan ₿ Academy te volgen:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c