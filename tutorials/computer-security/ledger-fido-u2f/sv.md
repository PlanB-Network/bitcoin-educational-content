---
name: "Ledger U2F & FIDO2"
description: Förbättra din online-säkerhet med Ledger
---
![cover](assets/cover.webp)



Ledger-enheter är hårdvaruplånböcker som ursprungligen utformades för att säkra en Bitcoin Wallet, men de har också avancerade alternativ för stark autentisering på webben. Tack vare att de är kompatibla med protokollen **U2F** och **FIDO2** kan du säkra åtkomsten till dina onlinekonton genom att skapa en andra autentiseringsfaktor.



U2F-protokollet (Universal 2nd Factor) introducerades av Google och Yubico 2014 och standardiserades sedan av FIDO Alliance. Det gör det möjligt att lägga till en andra fysisk autentiseringsfaktor (2FA) när man loggar in. När den är aktiverad måste användaren, utöver det klassiska lösenordet, godkänna varje försök att ansluta till sitt konto genom att trycka på en knapp på sin Ledger. I det här sammanhanget fungerar Ledger på ett liknande sätt som en Yubikey. U2F är i själva verket en delkomponent av FIDO2-standarden, som omfattar den samtidigt som den ger betydande förbättringar, inklusive inbyggt stöd för moderna webbläsare och större flexibilitet i hanteringen av autentiseringsnycklar.



Dessa metoder baseras på asymmetrisk kryptografi: inga hemliga data överförs, vilket gör nätfiske eller avlyssningsattacker ineffektiva. U2F och FIDO2 stöds nu av många onlinetjänster.



I den här guiden visar vi hur du aktiverar U2F och FIDO2 för tvåfaktorsautentisering med din Ledger.



**U2F och FIDO2 stöds på alla Ledger-enheter som är utrustade med den senaste firmware: från version 2.1.0 för Nano X och Nano S classic, och från version 1.1.0 för Nano S Plus. Stax- och Flex-modellerna är kompatibla.**



## Installera applikationen Ledger Security Key



Om du använder en Ledger-enhet vet du förmodligen att den inbyggda programvaran inte innehåller alla funktioner som behövs för att hantera kryptoplånböcker. Om du till exempel vill använda en Bitcoin Wallet måste du installera programmet "* Bitcoin*". På samma sätt måste du installera applikationen "*Security Key*" för att hantera MFA-nycklar.



Innan du börjar ska du se till att du har konfigurerat din Bitcoin Wallet på din Ledger. Det är viktigt att du sparar din Mnemonic korrekt, eftersom nycklarna som används för 2FA härrör från denna Mnemonic. Om din Ledger försvinner eller skadas kan du återfå åtkomst till dina nycklar genom att ange din Mnemonic-fras på en annan Ledger-enhet (för tillfället stöds ännu inte FIDO2-identifierare i läget "*lösenordslöst*" på Ledgers, så det finns inga residenta identifierare).



Anslut din Ledger till din dator och lås upp den.



![Image](assets/fr/01.webp)



För att installera applikationen, öppna programvaran [Ledger Live] (https://www.Ledger.com/Ledger-live) och gå sedan till fliken "*My Ledger*". Leta reda på applikationen "*Security Key*" och installera den på din enhet.



![Image](assets/fr/02.webp)



Programmet "*Security Key*" ska nu visas tillsammans med de andra programmen som är installerade på din Ledger.



![Image](assets/fr/03.webp)



Klicka på applikationen för att lämna den öppen för nästa steg i handledningen.



![Image](assets/fr/04.webp)



## Använd U2F/FIDO2 för 2FA med en Ledger



Gå till det konto som du vill säkra med tvåfaktorsautentisering. Till exempel kommer jag att använda ett Bitwarden-konto. Du hittar vanligtvis 2FA-alternativet i tjänsteinställningarna, under flikarna "*autentisering*", "*säkerhet*", "*inloggning*" eller "*lösenord*".



![Image](assets/fr/05.webp)



I avsnittet om tvåfaktorsautentisering väljer du alternativet "*Passkey*" (termen kan variera beroende på vilken webbplats du använder).



![Image](assets/fr/06.webp)



Du kommer ofta att bli ombedd att bekräfta ditt nuvarande lösenord.



![Image](assets/fr/07.webp)



Ge din säkerhetsnyckel ett namn så att du lätt kan känna igen den och klicka sedan på "*Läs nyckel*".



![Image](assets/fr/08.webp)



Dina kontouppgifter visas på Ledger:s display. Tryck på "*Register*"-knappen för att bekräfta (eller båda knapparna samtidigt, beroende på vilken modell du använder).



![Image](assets/fr/09.webp)



Accessnyckeln har registrerats framgångsrikt.



![Image](assets/fr/10.webp)



Registrera denna säkerhetsnyckel.



![Image](assets/fr/11.webp)



När du loggar in på ditt konto kommer du från och med nu, utöver ditt vanliga lösenord, att bli ombedd att ansluta din Ledger.



![Image](assets/fr/12.webp)



Du kan sedan trycka på "*Log in*"-knappen på din Ledger-display för att bekräfta autentiseringen (eller på båda knapparna samtidigt, beroende på vilken modell du använder).



![Image](assets/fr/13.webp)



Fördelen med att använda en Hardware Wallet Ledger för tvåfaktorsautentisering är att du enkelt kan återställa dina nycklar tack vare Mnemonic-frasen. Utöver denna grundläggande säkerhetskopia kan du också använda en nödkod som tillhandahålls av varje tjänst där du har aktiverat 2FA. Med den här nödkoden kan du ansluta till ditt konto om du tappar bort din säkerhetsnyckel. Den ersätter därför 2FA för en anslutning vid behov.



På Bitwarden kan du t.ex. komma åt denna kod genom att klicka på "*Visa återvinningskod*".



![Image](assets/fr/14.webp)



Jag rekommenderar att du förvarar den här koden på en annan plats än där du förvarar ditt huvudlösenord, för att förhindra att de stjäls tillsammans. Om du till exempel sparar ditt lösenord i en lösenordshanterare ska du förvara din 2FA-nödkod på papper, separat.



Detta tillvägagångssätt ger dig två nivåer av säkerhetskopiering i händelse av förlust av din Ledger för 2FA-autentisering: en första säkerhetskopiering med Mnemonic-frasen för alla dina konton och en andra kontospecifik säkerhetskopiering med nödkoderna. Det är dock viktigt att **inte förväxla Mnemonic:s roll med nödkodens**:




- Mnemonic-frasen på 12 eller 24 ord ger dig inte bara tillgång till de nycklar som används för 2FA på alla dina konton, utan också till dina bitcoins som är säkrade med din Ledger ;
- Med nödkoden kan du tillfälligt kringgå 2FA-begäran endast på det berörda kontot (i det här exemplet endast på Bitwarden).



Grattis, du har nu kommit igång med att använda din Ledger för MFA! Om du tyckte att den här handledningen var användbar skulle jag vara mycket tacksam om du lämnade en Green-tumme nedan. Du får gärna dela den här handledningen på dina sociala nätverk. Tack så mycket!



Jag skulle också rekommendera den här andra handledningen, där vi tittar på en annan lösning för U2F- och FIDO2-autentisering:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e