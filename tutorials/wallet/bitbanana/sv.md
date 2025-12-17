---
name: BitBanana
description: Mobil manager för din Lightning-nod
---

![cover](assets/cover.webp)



I den här handledningen lär du dig hur du installerar och konfigurerar BitBanana på Android för att styra din Lightning-nod från din smartphone. Vi kommer att se hur du ansluter appen till din befintliga infrastruktur (Umbrel, RaspiBlitz, myNode eller någon LND/Core Lightning-nod), gör Lightning-betalningar, fjärrhanterar dina kanaler, ser dina routingintäkter och säkerhetskopierar dina konfigurationer. Du kommer också att lära dig om de bästa säkerhetsrutinerna för att skydda åtkomst till din nod och hur den jämförs med Zeus, ett populärt alternativ.



## Vi presenterar BitBanana



BitBanana är en Android-mobilapplikation med öppen källkod som förvandlar din smartphone till en komplett instrumentpanel för fjärrstyrning av din Lightning-nod. Till skillnad från Lightning-plånböcker, som bäddar in en lokal nod på telefonen, antar BitBanana en 100% fjärrkontrollfilosofi: appen har ingen satoshi och ansluter endast till din befintliga infrastruktur.



Applikationen är utvecklad av Michael Wünsch under MIT-licens och garanterar total transparens utan insamling av personuppgifter och verifierade reproducerbara builds. BitBanana har inbyggt stöd för LND och Core Lightning via standard URI:er (`lndconnect://` och `clngrpc://`), vilket drastiskt förenklar den initiala konfigurationen. Applikationen känner också igen LndHub och Nostr Wallet Connect för användare utan en personlig nod, även om dessa lägen fungerar som förmyndare med begränsad funktionalitet.



Gränssnittet ger full tillgång till alla kritiska funktioner i din nod: skicka och ta emot betalningar (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), hantering av Lightning-kanaler (öppning, stängning, avgiftsjustering, ombalansering), avancerad myntkontroll och hantering av vakttorn. BitBanana implementerar också flera robusta säkerhetslager: biometrisk låsning, stealth-läge, Emergency PIN och inbyggt Tor-stöd för att anonymisera anslutningar.



## Plattformar som stöds och installation



### Installation



BitBanana är exklusivt tillgänglig för Android 8.0 eller högre. Applikationen finns inte på iOS, och ingen version är planerad. Denna begränsning förklaras av projektets historia: BitBanana är den direkta efterträdaren till Zap Android, ursprungligen utvecklad av Michael Wünsch, som bestämde sig för att fortsätta sitt arbete under sitt eget varumärke. Zap var en familj av separata applikationer (Zap Android, Zap iOS, Zap Desktop) som utvecklades av olika bidragsgivare med separata kodbaser. BitBanana följer bara Android-grenen.



Dessutom innebär iOS-ekosystemet betydande regulatoriska och tekniska begränsningar för Lightning-applikationer som inte är frihetsberövande. År 2023 avvisade Apple en Zeus-uppdatering på grund av "licensöverträdelser" och år 2024 lämnade Phoenix Wallet den amerikanska App Store på grund av osäkerhet kring regelverket för Lightning-tjänsteleverantörer. Dessa hinder förklarar varför många Lightning-utvecklare föredrar Android, som erbjuder en mer öppen policy för applikationer som inte är avsedda för frihetsberövande.



Tre installationsmetoder finns tillgängliga för Android: Google Play Store (5000+ installationer, automatiska uppdateringar), F-Droid (reproducerbara builds, källkodsverifiering) eller manuell APK från GitHub.



![BitBanana](assets/fr/01.webp)



Den officiella bitbanana.app-webbplatsen (vänster) skryter med "100% självförvaltande med NOLL datainsamling". Den centrala skärmen visar de tre nedladdningsalternativen: F-Droid (rekommenderas), Google Play och APK. Skärmen till höger visar aviseringstillståndet för betalningsvarningar.



Programmet begär behörigheter: nätverk (nodanslutning), kamera (QR-koder), NFC (LNURL), bakgrundstjänster (meddelanden), biometri (säkerhet) och WireGuard VPN. Inga spårare, ingen datainsamling. Aktivera lösenord eller biometrisk låsning för att säkra åtkomst.



## Inledande konfiguration



### Ansluta till en LND-nod



För att ansluta BitBanana till din LND-nod (Umbrel, RaspiBlitz, myNode), skaffa en `lndconnect` URI eller QR-kod som innehåller adressen, TLS-certifikatet och autentiseringsmacaronen.



För denna handledning använder vi en LND-nod via umbrel. För mer information, vänligen se vår dedikerade handledning :



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



I Lightning Node-applikationen öppnar du menyn längst upp till höger och väljer "Connect wallet".



![BitBanana](assets/fr/04.webp)



Välj **gRPC (Tor)** för att ansluta via Tor (rekommenderas). QR-koden och detaljer (Host .onion, Port 10009, Macaroon) visas.



![BitBanana](assets/fr/02.webp)



I BitBanana trycker du på "CONNECT NODE", skannar QR-koden eller klistrar in URI:n. Auktorisera kameraåtkomst och kontrollera sedan den .onion-adress som visas innan du bekräftar.



**Core Lightning**-anslutning



Om du använder Core Lightning (CLN) istället för LND förblir processen identisk, med URI `clngrpc://` som innehåller de ömsesidiga TLS-certifikaten. Core Lightning har inbyggt stöd för BOLT12 (erbjudanden), vilket möjliggör återanvändbara fakturor och återkommande betalningar som inte är tillgängliga på LND.



**Anslutning utan personlig nod (LNbits/hosted)**



Om du inte har en Lightning-nod kan BitBanana ansluta till hostade tjänster via LndHub (protokollet som används av BlueWallet och LNbits) eller Nostr Wallet Connect (NWC). Observera: dessa lägen fungerar i depåläge (tjänsten är värd för dina medel) med begränsad funktionalitet. Du kan inte hantera kanaler eller konfigurera routingavgifter, och du kan bara skicka och ta emot Lightning-betalningar.



För mer information om LNbits eller Nostr Wallet Connect, vänligen se våra olika handledningar:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Daglig användning



### Interface huvud



På startskärmen visas ditt Lightning-saldo, och menyn längst upp till vänster ger tillgång till följande avsnitt: Kanaler, Routing, Signera/Verifiera, Noder, Kontakter, Inställningar, Backup. Klockikonen (längst upp till höger) öppnar transaktionshistoriken. Med knapparna "Send" och "Receive" längst ned kan du skicka och ta emot dina satoshis.



![BitBanana](assets/fr/05.webp)



### Blixtnedslag och on-chain-betalningar



![BitBanana](assets/fr/10.webp)



**Skicka en betalning:** Tryck på "Skicka"-knappen från startskärmen. Betalningsskärmen (till vänster) erbjuder dig att klistra in en adress eller betalningsdata i fältet "Address eller betalningsdata", med en QR-skanner längst upp till höger för att skanna koder. Du kan också välja en kontakt som sparats i Kontakter för att slippa skanna varje gång.



BitBanana känner på ett intelligent sätt igen alla betalningsformat: klassiska Lightning-fakturor (teckensträngar som börjar med `lnbc`), Lightning Address (e-postformat som `utilisateur@domaine.com`), LNURL-pay-koder för dynamiska betalningar, LNURL-withdraw för uttag av medel och till och med Keysend-betalningar direkt till en Lightning-offentlig nyckel utan föregående faktura. Programmet utför automatiskt de nödvändiga LNURL-resolutionerna i bakgrunden.



När fakturan har laddats visar BitBanana alla detaljer: exakt belopp, beräknade routningsavgifter, betalningsbeskrivning (om den tillhandahålls av mottagaren) och fakturans utgångsdatum. Efter bekräftelse dirigeras betalningen via dina Lightning-kanaler. Du kan sedan se rutten som tagits hopp för hopp och de avgifter som faktiskt betalats i transaktionsinformationen.



**Ta emot betalning:** Tryck på knappen "Ta emot". En väljare (höger skärm) låter dig välja mellan Lightning (omedelbar betalning via dina kanaler) och On-Chain. För ett Lightning-kvitto anger du önskat belopp i satoshis (eller lämnar 0 för att skapa en faktura utan fast belopp som betalaren ska fylla i) och lägger till en valfri beskrivning som ska visas på fakturan. BitBanana genererar omedelbart en Lightning-faktura med QR-kod för skanning. Du kan också kopiera fakturan som text och skicka den via e-post. Så snart betalningen har tagits emot får du en push-notis och transaktionen visas omedelbart i historiken med alla detaljer.



### Kanaler och routing



![BitBanana](assets/fr/06.webp)



Avsnittet "Channels" visar dina sändnings- och mottagningsmöjligheter och listar dina kanaler med unika avatarer. Varje kanal visar sin likviditetsfördelning mellan lokalt och externt saldo. Tryck på en kanal för fullständig information och åtgärder (stängning, ändring av routningsavgifter). De tre prickarna längst upp till höger ger tillgång till alternativet "Rebalance" för att ombalansera dina kanalers likviditet. Knappen "+" öppnar en ny kanal.



I avsnittet Routing (central skärm) visas vidarebefordringsintäkter per period (1D, 1W, 1M, 3M, 6M, 1Y) med detaljerad vidarebefordringshistorik för att optimera din strategi.



Med Sign/Verify (höger skärm) kan du kryptografiskt signera/verifiera meddelanden för att bevisa nodkontroll.



### Multi-noder och parametrar



![BitBanana](assets/fr/07.webp)



**Manage Nodes**: listar dina noder, med knappar för att lägga till manuellt, skanna QR eller växla mellan noder. Framför allt kan du ställa in olika typer av anslutningar till samma nod: LAN, VPN eller Tor.



**Hantera kontakter**: lagrar dina Lightning-kontakter för snabba betalningar.



**Inställningar**: Anpassa valuta, språk, avatarer. Avsnittet Säkerhet och sekretess: App Lock (PIN/biometri), Dölj saldo (stealth-läge), Tor (IP-anonymisering). Konfiguration av prisorakel, blockutforskare, anpassade avgiftsberäknare.



## Fördelar och begränsningar



**Höjdpunkter:**




- Total mobilitet: styr din Lightning-nod från var som helst
- Full funktionalitet: betalningar (LNURL, Lightning Address, BOLT 12), kanalhantering, myntkontroll, vakttorn, multi-noder
- Säkerhet: PIN/biometri, stealth-läge, nöd-PIN, inbyggd Tor, blockering av skärmdumpar
- Gratis, öppen källkod (MIT), inga provisioner, ingen datainsamling



**Begränsningar:**




- Kräver en aktiv Lightning-nod (eller LNbits i förvaringsläge)
- Ingen iOS-version planerad
- Att säkra åtkomsten till telefonen är avgörande (macaroon admin = total åtkomst till noden)



## Bästa praxis



**Säkerhet:**




- Aktivera PIN/biometriskt lås (förhindrar obehörig åtkomst till noden)
- Skapa en nöd-PIN (raderar känsliga uppgifter i händelse av hot)
- Dela aldrig din inloggnings URI eller macaroon
- Stealth-läge i fientliga miljöer



**Inloggning:**




- VPN mesh (Tailscale, ZeroTier): bästa kompromissen mellan hastighet och säkerhet
- Tor: maximal sekretess, högre latenstid
- Clearnet: undvik om det inte är nödvändigt (IP-exponering, öppna portar)



### Säkerhetskopiering och återställning



Slutligen finns menyn "Backup", där du kan spara dina konfigurationer för telefonmigrering eller ominstallation.



![BitBanana](assets/fr/08.webp)



**Viktigt:** Säkerhetskopian innehåller INTE seed eller säkerhetskopior av kanaler (som ska göras på noden). Den innehåller: nodkonfigurationer (adresser, certifikat, macaroons), etiketter, kontakter, parametrar. Med knappen Restore kan du importera en befintlig säkerhetskopia. Bekräftelse krävs innan du sparar.



![BitBanana](assets/fr/09.webp)



Ange ett krypteringslösenord (höger skärm). Systemet öppnar filväljaren (vänster skärm) för att spara `BitBananaBackup_2025-XX-XX.dat`. Bekräftelse "Backup skapad".



** Säkerhet: ** Lagra säkerhetskopian krypterad (personligt moln, USB, NAS). Dela aldrig filer eller lösenord. Testa återställningen regelbundet. Säkerhetskopian återställer anslutningar, inte medel.



## BitBanana vs Zeus: Vad är skillnaden?



Om du utforskar mobilappar för hantering av en Lightning-nod kommer du sannolikt att stöta på Zeus, ett populärt alternativ till BitBanana. Till skillnad från BitBanana, som uteslutande fokuserar på fjärrstyrning av en befintlig nod, tar Zeus ett mer omfattande grepp och erbjuder två driftsätt: en Lightning-nod inbäddad direkt i applikationen (inbäddat läge med integrerad LND) och fjärranslutning till en extern nod, precis som BitBanana.



Denna dubbla funktionalitet gör Zeus särskilt attraktiv för nybörjare som vill experimentera med Lightning utan någon tidigare infrastruktur. Embedded mode möjliggör omedelbar uppstart med en komplett mobil nod, medan avancerade användare kan växla till fjärranslutning när deras personliga nod har konfigurerats. Zeus stöder även LND och Core Lightning för fjärranslutning, t.ex. BitBanana.



En annan stor fördel med Zeus är att den är tillgänglig på flera plattformar (iOS och Android), medan BitBanana endast är Android-baserad. Zeus innehåller också Olympus LSP-infrastruktur för att underlätta mottagandet av Lightning-betalningar via just-in-time-kanaler, ett Point of Sale-system för handlare och integrerad swapfunktionalitet för att hantera likviditeten.



BitBanana behåller dock sina specifika styrkor: ett enklare, mer strömlinjeformat gränssnitt, en bättre användarupplevelse (UX) tack vare dess exklusiva fokus på fjärrkontroll och ett pedagogiskt tillvägagångssätt med kontextuella förklaringar. Zeus erbjuder fler funktioner, men på bekostnad av ett mer komplext gränssnitt. Applikationen är fortfarande särskilt lämpad för användare som vill styra en nod uteslutande på avstånd, utan att behöva ta hand om den.



Om du vill veta mer om Zeus kan du ta en titt på följande handledningar:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Slutsats



BitBanana förvandlar din Android-smartphone till en komplett Lightning-instrumentpanel och erbjuder oöverträffad mobilitet för nodoperatörer. Applikationen täcker alla funktioner: betalningar (alla format), kanalhantering, myntkontroll, vakttorn, multi-nod, med förbättrad säkerhet (PIN/biometri, Tor, Emergency PIN).



BitBanana är helt suverän och samlar inte in några uppgifter och äventyrar varken sekretessen eller kontrollen över dina medel. Öppen källkod (MIT) garanterar transparens.



## Resurser



### Officiell dokumentation




- [BitBananas webbplats](https://bitbanana.app)
- [Komplett dokumentation] (https://docs.bitbanana.app)
- [GitHub-källkod] (https://github.com/michaelWuensch/BitBanana)



### Installation




- [Google Play Store] (https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold] (https://f-droid.org/packages/app.michaelwuensch.bitbanana)