---
name: BTCPay Server bijwerken
description: Voer een beveiligingsupdate uit op je BTCPay Server-instantie en roteer de gegevens die ertoe doen
---

![cover](assets/cover.webp)

Als je je eigen betalingsverwerker draait, ben je ook je eigen beveiligingsteam. Wanneer de BTCPay Server-onderhouders een beveiligingsrelease publiceren, patcht niemand je instantie voor je: de update, de verificatie en de daaropvolgende rotatie van gegevens zijn aan jou.

Deze tutorial doorloopt de hele procedure, ongeacht hoe je BTCPay Server hebt geïnstalleerd: controleer de draaiende versie, voer de update uit op jouw type installatie, verifieer dat deze daadwerkelijk is doorgevoerd, en roteer de geheimen die een aanvaller mogelijk heeft buitgemaakt terwijl je instantie kwetsbaar was.

Als je BTCPay Server nog niet hebt geïnstalleerd, begin dan met de installatiehandleiding:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## De kritieke kwetsbaarheid van augustus 2026

⚠️ **Kritieke beveiligingswaarschuwing (7 augustus 2026):** een kritieke kwetsbaarheid in BTCPay Server wordt actief misbruikt en kan leiden tot verlies van middelen. Werk je instantie onmiddellijk bij naar **versie 2.4.2** via `Admin Dashboard > Server > Maintenance > Update`, en controleer daarna of de footer `2.4.2` weergeeft. Als je niet meteen kunt bijwerken, sluit je BTCPay Server dan af. Zodra je hebt bijgewerkt, moet je ook al je macaroons en je `macaroons.db` volledig vernieuwen, de authenticatiestrings van elke andere Lightning-backend volledig vernieuwen, en, als je binnen BTCPay Server een hot on-chain wallet hebt aangemaakt, die middelen verplaatsen en de wallet opnieuw aanmaken. Integrators moeten ook NBXplorer bijwerken naar versie 2.6.10. Bron: [BTCPay Server 2.4.2 release notes](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Versie 2.4.2 werd gepubliceerd op 7 augustus 2026. De release notes vermelden dat deze een kritieke kwetsbaarheid verhelpt die al in het wild werd misbruikt, gerapporteerd door `brunoerg` en `benthecarman` via het Bitcoin Red Team-initiatief. Dezelfde release verhelpt ook een omzeiling van TOTP-tweefactorauthenticatie via Greenfield Basic-authenticatie, en schakelt Greenfield Basic-authenticatie standaard vijf minuten na het aanmaken van een account uit.

Uit "actief misbruikt" volgen twee gevolgen:

- **Bijwerken is niet optioneel en niets om voor volgende week in te plannen.** Een niet-gepatchte instantie die vanaf het internet bereikbaar is, moet ofwel worden bijgewerkt, ofwel worden uitgeschakeld.
- **Bijwerken alleen is niet genoeg.** Als je instantie was gecompromitteerd voordat je patchte, heeft de aanvaller mogelijk al kopieën van je Lightning-gegevens en van elk hot-wallet-sleutelmateriaal dat BTCPay Server voor je heeft gegenereerd. Die geheimen blijven na de update geldig totdat je ze roteert. De rotatiesectie hieronder is het onderdeel dat mensen overslaan, en het is het onderdeel dat je middelen daadwerkelijk beschermt.

## Stap 1 — Achterhaal welke versie je draait

Log in op je BTCPay Server en kijk naar de **footer van een willekeurige pagina**: de versiestring wordt daar weergegeven. Je kunt ook `Admin Dashboard > Server > Maintenance` openen, waar de huidige versie en de updatebediening te zien zijn.

Als je instantie de Greenfield API blootstelt, geeft `GET /api/v1/server/info` de versie ook terug.

Alles onder `2.4.2` is kwetsbaar.

## Stap 2 — Bijwerken

### Self-hosted Docker-installatie (de standaardinstallatie)

Dit geldt voor de officiële Docker-installatie, die je krijgt via de BTCPay Server-documentatie, via de one-click launcher van LunaNode, en via de meeste VPS-installaties.

Het eenvoudigste pad is via de webinterface:

1. Ga naar `Admin Dashboard > Server > Maintenance`.
2. Klik op **Update**.
3. Wacht tot de containers zijn opgehaald en herstart. De interface zal enkele minuten niet beschikbaar zijn.

Als de webinterface onbereikbaar is, of als je liever de logs bekijkt, doe het dan via SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Bij een standaardinstallatie is `$BTCPAY_BASE_DIRECTORY` gelijk aan `/root`, dus de map is `/root/btcpayserver-docker`. Het script haalt de nieuwste images op, herbouwt de containers en toont de resulterende versies.

De Docker-installatie levert NBXplorer samen met BTCPay Server, dus een standaardupdate brengt ook NBXplorer naar de aanbevolen `2.6.10`. Als je NBXplorer apart draait — typisch voor integrators en aangepaste stacks — werk het dan expliciet bij.

### Umbrel

Open het Umbrel-dashboard, ga naar de **App Store**, zoek BTCPay Server en voer de update uit als die wordt aangeboden.

⚠️ **Belangrijk:** app-store-pakketten worden opnieuw verpakt door het Umbrel-team en kunnen uren tot dagen achterlopen op upstream. Controleer na het bijwerken de versie in de footer van BTCPay Server. Als deze nog steeds onder `2.4.2` ligt, **stop dan de app** vanuit het Umbrel-dashboard en wacht op de verpakte release in plaats van een kwetsbare instantie te laten draaien.

De speciale Umbrel-handleiding behandelt de app zelf:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Zelfde logica: werk BTCPay Server bij vanuit de StartOS-marketplace, en verifieer daarna de versie in de footer. Als de verpakte versie nog geen `2.4.2` is, stop dan de service totdat dit wel zo is.

### Beheerde hosting en hosting door derden

Als iemand anders je instantie beheert (een hostingprovider, een vereniging, de server van een vriend), heb je nog steeds de bevestiging nodig. Vraag de beheerder naar de versiestring die in de footer wordt getoond, en vraag expliciet of de hieronder beschreven rotatie van gegevens na de update is uitgevoerd. "We hebben bijgewerkt" is niet hetzelfde antwoord als "we hebben je macaroons geroteerd".

## Stap 3 — Verifieer dat de update daadwerkelijk is doorgevoerd

Herlaad de interface van BTCPay Server en lees de versie in de footer af. Deze moet `2.4.2` of hoger tonen.

Vertrouw er niet op dat het updatecommando zonder fout afsluit: op machines met beperkte middelen kan het ophalen van een image stilzwijgend mislukken, waardoor de vorige container blijft draaien. Lees elke keer de versie af.

## Stap 4 — Roteer je gegevens

Dit is de stap die "gepatcht" omzet in "veilig". Omdat de kwetsbaarheid al werd misbruikt voordat de fix uitkwam, moet je elk geheim dat je instantie bevatte behandelen alsof het mogelijk bekend is bij een aanvaller.

### Lightning: LND

Genereer zowel de macaroons **als** het bestand `macaroons.db` opnieuw. Alleen de macaroon-bestanden verwijderen is niet genoeg — LND leidt macaroons af van de root key die in `macaroons.db` is opgeslagen, waardoor een aanvaller die een kopie van een oude macaroon bezit toegang houdt totdat die database opnieuw wordt aangemaakt.

De procedure is: stop LND, verwijder `macaroons.db` en de `*.macaroon`-bestanden uit de netwerkmap (voor mainnet is dat `data/chain/bitcoin/mainnet/` binnen de LND-datamap), en herstart en ontgrendel LND vervolgens, waardoor ze opnieuw worden aangemaakt. Maak eerst een back-up van de map, en koppel elke toepassing die de oude macaroons gebruikte opnieuw — BTCPay Server zelf, Zeus, Thunderhub, RTL, Alby en elk script dat je hebt geschreven.

Als je LND ook via het internet blootstelt, controleer dan tegelijkertijd het TLS-certificaat en eventuele `lnd.conf`-gegevens.

### Lightning: andere backends

Alles wat zich met een string bij je node authenticeert, moet een nieuwe string krijgen:

- **Core Lightning**: genereer de rune of de toegangsgegevens die voor de verbinding worden gebruikt opnieuw.
- **Phoenixd**: roteer het HTTP-wachtwoord.
- **LNbits en vergelijkbare**: trek de admin- en invoice-sleutels in en geef nieuwe uit.
- **Verbindingsstrings van externe nodes** die in de winkelinstellingen van BTCPay Server zijn opgeslagen: herschrijf deze met de nieuwe geheimen.

### Hot on-chain wallet die binnen BTCPay Server is gegenereerd

Als je BTCPay Server een on-chain wallet voor je liet genereren — in tegenstelling tot het koppelen van een hardware wallet of het importeren van een xpub waarvan de sleutels nooit op de server hebben gestaan — dan heeft die seed op de machine geleefd.

Beschouw deze als verbrand:

1. Maak een nieuwe wallet aan, bij voorkeur met een hardware wallet zodat de sleutels nooit meer op de server staan.
2. Veeg de middelen van de oude wallet naar de nieuwe.
3. Vervang het afleidingsschema in de winkelinstellingen door de nieuwe wallet.
4. Hergebruik de oude seed nooit.

Watch-only-opstellingen (xpub of hardware wallet) hebben dit niet nodig: de privésleutels stonden nooit op de server. Dit is precies waarom de installatiehandleiding ze aanbeveelt.

### BTCPay Server-accounts en API-sleutels

Doe meteen ook het volgende:

- Wijzig de wachtwoorden van elk gebruikersaccount op de instantie.
- Trek alle Greenfield-**API-sleutels** in en geef nieuwe uit.
- Registreer tweefactorauthenticatie opnieuw, aangezien 2.4.2 een 2FA-omzeiling verhelpt.
- Open `Admin Dashboard > Server > Users` en controleer of er geen onverwacht account bestaat.
- Controleer recente **uitbetalingen (payouts)**, **pull payments** en **terugbetalingen** op vermeldingen die je niet zelf hebt aangemaakt.
- Controleer je webhooks en hun geheimen.

## Stap 5 — Blijf op de hoogte voor de volgende keer

Beveiligingsreleases helpen alleen de beheerders die ervan horen:

- Volg de [BTCPay Server-releases op GitHub](https://github.com/btcpayserver/btcpayserver/releases) — GitHub kan je e-mailen bij elke nieuwe release van een repository.
- Volg de aankondigingskanalen van het project en de [officiële blog](https://blog.btcpayserver.org/).
- Houd je instantie op een versie die je snel kunt bijwerken: hoe verder je achterloopt, hoe pijnlijker een noodupdate wordt.

Zelf hosten geeft je soevereiniteit over je betalingen. De prijs van die soevereiniteit is precies dit: release notes lezen en degene zijn die patcht.
