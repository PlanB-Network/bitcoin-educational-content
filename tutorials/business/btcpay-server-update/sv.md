---
name: Uppdatera BTCPay Server
description: Tillämpa en säkerhetsuppdatering på din BTCPay Server-instans och rotera de autentiseringsuppgifter som spelar roll
---

![cover](assets/cover.webp)

Att driva din egen betalningsprocessor innebär att du också är ditt eget säkerhetsteam. När underhållarna av BTCPay Server publicerar en säkerhetsuppdatering är det ingen som patchar din instans åt dig: uppdateringen, verifieringen och den efterföljande roteringen av autentiseringsuppgifter är din uppgift att utföra.

Denna handledning går igenom hela proceduren, oavsett hur du har driftsatt BTCPay Server: kontrollera vilken version som körs, tillämpa uppdateringen för din typ av driftsättning, verifiera att den faktiskt slog igenom, och rotera de hemligheter som en angripare kan ha kommit över medan din instans var sårbar.

Om du ännu inte har driftsatt BTCPay Server, börja med installationsguiden:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Den kritiska sårbarheten i augusti 2026

⚠️ **Kritisk säkerhetsvarning (7 augusti 2026):** en kritisk sårbarhet som påverkar BTCPay Server utnyttjas aktivt och kan leda till förlust av medel. Uppdatera din instans till **version 2.4.2** omedelbart via `Admin Dashboard > Server > Maintenance > Update`, kontrollera sedan att sidfoten visar `2.4.2`. Om du inte kan uppdatera direkt, stäng ner din BTCPay Server. Efter uppdateringen måste du också uppdatera dina macaroons och din `macaroons.db` fullständigt, uppdatera autentiseringssträngarna för alla andra Lightning-backends fullständigt, och, om du genererade en het on-chain-plånbok inuti BTCPay Server, flytta de medlen och återskapa plånboken. Integratörer bör även uppdatera NBXplorer till version 2.6.10. Källa: [BTCPay Server 2.4.2 release notes](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Version 2.4.2 publicerades den 7 augusti 2026. Utgåvenoteringarna anger att den åtgärdar en kritisk sårbarhet som redan utnyttjades i praktiken, rapporterad av `brunoerg` och `benthecarman` genom Bitcoin Red Team-insatsen. Samma utgåva åtgärdar också en kringgåelse av TOTP-tvåfaktorsautentisering via Greenfield Basic-autentisering, och inaktiverar Greenfield Basic-autentisering som standard fem minuter efter kontoskapande.

Två konsekvenser följer av "utnyttjas aktivt":

- **Att uppdatera är inte valfritt och inget att schemalägga till nästa vecka.** En opatchad instans som är nåbar från internet måste antingen uppdateras eller stängas av.
- **Att uppdatera räcker inte i sig.** Om din instans komprometterades innan du patchade den kan angriparen redan ha kopior av dina Lightning-autentiseringsuppgifter och av allt nyckelmaterial för heta plånböcker som BTCPay Server genererade åt dig. Dessa hemligheter förblir giltiga efter uppdateringen tills du roterar dem. Roteringsavsnittet nedan är det steg folk hoppar över, och det är det som faktiskt skyddar dina medel.

## Steg 1 — Ta reda på vilken version du kör

Logga in på din BTCPay Server och titta i **sidfoten på valfri sida**: versionssträngen visas där. Du kan också öppna `Admin Dashboard > Server > Maintenance`, som visar den aktuella versionen och uppdateringskontrollerna.

Om din instans exponerar Greenfield-API:et returnerar `GET /api/v1/server/info` versionen också.

Allt under `2.4.2` är sårbart.

## Steg 2 — Uppdatera

### Självhostad Docker-driftsättning (standardinstallationen)

Detta gäller den officiella Docker-driftsättningen, vilket är vad du får från BTCPay Server-dokumentationen, från LunaNodes engångsstartare och från de flesta VPS-installationer.

Den enklaste vägen är webbgränssnittet:

1. Gå till `Admin Dashboard > Server > Maintenance`.
2. Klicka på **Update**.
3. Vänta tills containrarna hämtas och startas om. Gränssnittet kommer att vara otillgängligt i några minuter.

Om webbgränssnittet inte går att nå, eller om du föredrar att se loggarna, gör det via SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Vid en standardinstallation är `$BTCPAY_BASE_DIRECTORY` lika med `/root`, så katalogen är `/root/btcpayserver-docker`. Skriptet hämtar de senaste avbildningarna, återskapar containrarna och skriver ut de resulterande versionerna.

Docker-driftsättningen levereras med NBXplorer tillsammans med BTCPay Server, så en standarduppdatering tar även NBXplorer till den rekommenderade `2.6.10`. Om du kör NBXplorer separat — typiskt för integratörer och anpassade stackar — uppdatera det uttryckligen.

### Umbrel

Öppna Umbrel-instrumentpanelen, gå till **App Store**, hitta BTCPay Server och tillämpa uppdateringen om en sådan erbjuds.

⚠️ **Viktigt:** app-store-paket ompaketeras av Umbrel-teamet och kan ligga efter uppströmsversionen med timmar eller dagar. Kontrollera versionen i BTCPay Server-sidfoten efter uppdateringen. Om den fortfarande är under `2.4.2`, **stoppa appen** från Umbrel-instrumentpanelen och vänta på den paketerade utgåvan i stället för att låta en sårbar instans fortsätta köra.

Den dedikerade Umbrel-guiden täcker själva appen:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Samma logik: uppdatera BTCPay Server från StartOS-marknadsplatsen, verifiera sedan versionen i sidfoten. Om den paketerade versionen ännu inte är `2.4.2`, stoppa tjänsten tills den är det.

### Hanterad hosting och tredjepartshosting

Om någon annan driver din instans (en hostingleverantör, en förening, en väns server) behöver du fortfarande bekräftelsen. Fråga operatören om versionssträngen som visas i sidfoten, och fråga uttryckligen om den efterföljande roteringen av autentiseringsuppgifter som beskrivs nedan har utförts. "Vi uppdaterade" är inte samma svar som "vi roterade dina macaroons".

## Steg 3 — Verifiera att uppdateringen faktiskt slog igenom

Ladda om BTCPay Server-gränssnittet och läs versionen i sidfoten. Den måste visa `2.4.2` eller högre.

Lita inte på att uppdateringskommandot avslutas utan fel: på begränsade maskiner kan en avbildningshämtning misslyckas tyst och lämna den föregående containern körande. Läs versionen, varje gång.

## Steg 4 — Rotera dina autentiseringsuppgifter

Det är det här steget som gör "patchad" till "säker". Eftersom sårbarheten utnyttjades innan rättningen släpptes, behandla varje hemlighet din instans innehöll som potentiellt känd för en angripare.

### Lightning: LND

Regenerera macaroons **och** filen `macaroons.db`. Att bara ta bort macaroon-filerna räcker inte — LND härleder macaroons från rotnyckeln som lagras i `macaroons.db`, så en angripare som har en kopia av en gammal macaroon behåller åtkomst tills den databasen återskapas.

Proceduren är: stoppa LND, ta bort `macaroons.db` och `*.macaroon`-filerna från nätverkskatalogen (för mainnet, `data/chain/bitcoin/mainnet/` inuti LND:s datakatalog), starta sedan om och lås upp LND, vilket återskapar dem. Säkerhetskopiera katalogen först, och para om varje applikation som använde de gamla macaroons — BTCPay Server självt, Zeus, Thunderhub, RTL, Alby, och alla skript du skrev.

Om du också exponerar LND över internet, granska dess TLS-certifikat och eventuella `lnd.conf`-autentiseringsuppgifter samtidigt.

### Lightning: andra backends

Allt som autentiserar mot din nod med en sträng måste få en ny sträng:

- **Core Lightning**: regenerera runen eller de åtkomstuppgifter som används för anslutningen.
- **Phoenixd**: rotera HTTP-lösenordet.
- **LNbits och liknande**: återkalla och utfärda på nytt admin- och fakturanycklarna.
- **Anslutningssträngar för fjärrnoder** som lagras i BTCPay Server store settings: skriv om dem med de nya hemligheterna.

### Het on-chain-plånbok genererad inuti BTCPay Server

Om du lät BTCPay Server generera en on-chain-plånbok åt dig — till skillnad från att ansluta en hårdvaruplånbok eller importera en xpub vars nycklar aldrig rörde vid servern — så levde det seedet på maskinen.

Betrakta det som brännt:

1. Skapa en ny plånbok, helst med en hårdvaruplånbok så att nycklarna aldrig ligger på servern igen.
2. Sopa in medlen från den gamla plånboken till den nya.
3. Ersätt härledningsschemat i store settings med den nya plånboken.
4. Återanvänd aldrig det gamla seedet.

Watch-only-uppsättningar (xpub eller hårdvaruplånbok) behöver inte detta: de privata nycklarna var aldrig på servern. Det är precis därför installationsguiden rekommenderar dem.

### BTCPay Server-konton och API-nycklar

Medan du ändå är igång:

- Ändra lösenorden för varje användarkonto på instansen.
- Återkalla och utfärda på nytt alla Greenfield-**API-nycklar**.
- Registrera om tvåfaktorsautentisering, med tanke på att 2.4.2 åtgärdar en kringgåelse av 2FA.
- Öppna `Admin Dashboard > Server > Users` och kontrollera att inget oväntat konto finns.
- Granska nyligen genomförda **payouts**, **pull payments** och **återbetalningar** för poster du inte skapade.
- Granska dina webhooks och deras hemligheter.

## Steg 5 — Håll dig informerad inför nästa gång

Säkerhetsuppdateringar hjälper bara de operatörer som får höra om dem:

- Bevaka [BTCPay Server-utgåvorna på GitHub](https://github.com/btcpayserver/btcpayserver/releases) — GitHub kan skicka e-post till dig vid varje ny utgåva av ett repository.
- Följ projektets tillkännagivandekanaler och den [officiella bloggen](https://blog.btcpayserver.org/).
- Håll din instans på en version du snabbt kan uppdatera: ju längre efter du ligger, desto smärtsammare blir en akut uppdatering.

Att självhosta ger dig suveränitet över dina betalningar. Priset för den suveräniteten är precis detta: att läsa utgåvenoteringar och vara den som patchar.
</content>
<parameter name="i">Write Swedish translation