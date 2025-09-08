---
name: YubiKey 2FA
description: Hur använder man en fysisk säkerhetsnyckel?
---
![cover](assets/cover.webp)


Numera har tvåfaktorsautentisering (2FA) blivit viktigt för att förbättra säkerheten för onlinekonton mot obehörig åtkomst. I och med ökningen av cyberattacker är det ibland otillräckligt att enbart förlita sig på ett lösenord för att säkra sina konton.


2FA introducerar ytterligare en Layer av säkerhet genom att kräva en andra form av autentisering utöver det traditionella lösenordet. Denna verifiering kan ske på olika sätt, t.ex. genom en kod som skickas via SMS, en dynamisk kod som genereras av en särskild app eller en fysisk säkerhetsnyckel. Användningen av 2FA minskar avsevärt riskerna för att dina konton ska äventyras, även om ditt lösenord skulle bli stulet.


I en annan handledning förklarade jag hur man ställer in och använder en TOTP 2FA-applikation:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Här ska vi se hur du använder en fysisk säkerhetsnyckel som en andra autentiseringsfaktor för alla dina konton.


## Vad är en fysisk säkerhetsnyckel?


En fysisk säkerhetsnyckel är en enhet som används för att förbättra säkerheten för dina onlinekonton genom tvåfaktorsautentisering (2FA). Dessa enheter liknar ofta små USB-nycklar som måste sättas in i en dators port för att verifiera att det verkligen är den legitima användaren som försöker ansluta.

![SECURITY KEY 2FA](assets/notext/01.webp)

När du loggar in på ett konto som skyddas av 2FA och använder en fysisk säkerhetsnyckel måste du inte bara ange ditt vanliga lösenord utan även sätta in den fysiska säkerhetsnyckeln i din dator och trycka på en knapp för att validera autentiseringen. Den här metoden lägger alltså till ytterligare en Layer i säkerhet, för även om någon lyckas komma över ditt lösenord kan de inte komma åt ditt konto utan att fysiskt inneha nyckeln.


Den fysiska säkerhetsnyckeln är särskilt effektiv eftersom den kombinerar två olika typer av autentiseringsfaktorer: bevis på kunskap (lösenordet) och bevis på innehav (den fysiska nyckeln).


Denna 2FA-metod har dock också nackdelar. För det första måste du alltid ha säkerhetsnyckeln tillgänglig om du vill komma åt dina konton. Du kan behöva lägga till den i din nyckelring. För det andra, till skillnad från andra 2FA-metoder, innebär användning av en fysisk säkerhetsnyckel en initial kostnad eftersom du måste köpa den lilla enheten. Priset på säkerhetsnycklar varierar i allmänhet mellan 30 och 100 euro beroende på vilka funktioner som väljs.


## Vilken fysisk säkerhetsnyckel ska man välja?


För att välja din säkerhetsnyckel måste du ta hänsyn till flera kriterier.

Först och främst måste du kontrollera de protokoll som stöds av enheten. Som ett minimum rekommenderar jag att du väljer en nyckel som stöder OTP, FIDO2 och U2F. Dessa detaljer lyfts vanligtvis fram av tillverkare i produktbeskrivningar. För att verifiera kompatibiliteten för varje nyckel kan du också besöka [dongleauth.com](https://www.dongleauth.com/dongles/).

Se också till att nyckeln är kompatibel med ditt operativsystem, även om välkända varumärken som Yubikey i allmänhet stöder alla allmänt använda system.


Du bör också välja nyckel utifrån vilken typ av portar som finns på din dator eller smartphone. Om din dator till exempel bara har USB-C-portar ska du välja en nyckel med en USB-C-kontakt. Vissa nycklar erbjuder också anslutningsalternativ via Bluetooth eller NFC.

![SECURITY KEY 2FA](assets/notext/02.webp)

Du kan också jämföra enheter baserat på deras ytterligare funktioner som vatten- och Dust-motstånd samt tangentens form och storlek.


När det gäller varumärken för säkerhetsnycklar är Yubico det mest kända med sina [YubiKey-enheter] (https://www.yubico.com/), som jag personligen använder och rekommenderar. Google erbjuder också en enhet med [Titan Security Key] (https://store.google.com/fr/product/titan_security_key). För alternativ med öppen källkod är [SoloKeys](https://solokeys.com/) (ej OTP) och [NitroKey](https://www.nitrokey.com/products/nitrokeys) intressanta alternativ, men jag har aldrig haft möjlighet att testa dem.


## Hur använder man en fysisk säkerhetsnyckel?


När du har fått din säkerhetsnyckel behöver du inte göra några särskilda inställningar. Nyckeln är normalt klar att använda direkt efter mottagandet. Du kan omedelbart använda den för att säkra dina onlinekonton som stöder den här typen av autentisering. Jag ska till exempel visa dig hur jag säkrar mitt Proton-mailkonto med den här fysiska säkerhetsnyckeln.

![SECURITY KEY 2FA](assets/notext/03.webp)

Du hittar alternativet för att aktivera 2FA i dina kontoinställningar, ofta under avsnittet "*Password*" eller "*Security*". Klicka på kryssrutan eller knappen som gör att du kan aktivera 2FA med en fysisk nyckel.

![SECURITY KEY 2FA](assets/notext/04.webp)

Anslut nyckeln till din dator.

![SECURITY KEY 2FA](assets/notext/05.webp)

Tryck på knappen på din säkerhetsnyckel för att validera.

![SECURITY KEY 2FA](assets/notext/06.webp)

Ange ett namn för att komma ihåg vilken tangent du använde.

![SECURITY KEY 2FA](assets/notext/07.webp)

Och där har du det, din säkerhetsnyckel har framgångsrikt lagts till för 2FA-autentisering av ditt konto.

![SECURITY KEY 2FA](assets/notext/08.webp)

Om jag i mitt exempel försöker återansluta till mitt Proton-mailkonto kommer jag först att bli ombedd att ange mitt lösenord tillsammans med mitt användarnamn. Detta är den första autentiseringsfaktorn.

![SECURITY KEY 2FA](assets/notext/09.webp)

Sedan ombeds jag att koppla in min säkerhetsnyckel för den andra autentiseringsfaktorn.

![SECURITY KEY 2FA](assets/notext/10.webp)

Därefter måste jag trycka på knappen på den fysiska nyckeln för att validera autentiseringen, och jag är återansluten till mitt Proton-mailkonto.

![SECURITY KEY 2FA](assets/notext/11.webp)

Upprepa den här åtgärden för alla onlinekonton som du vill skydda på det här sättet, särskilt för kritiska konton som dina e-postkonton, dina lösenordshanterare, dina moln- och onlinelagringstjänster eller dina finansiella konton.