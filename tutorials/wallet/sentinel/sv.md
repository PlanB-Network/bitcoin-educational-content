---
name: Sentinel endast för bevakning
description: Vad är en Watch-only wallet och hur använder man den?
---

![cover](assets/cover.webp)


---

**\*VARNING:** Efter gripandet av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april fortsätter Sentinel-appen att fungera, men **det är obligatoriskt att använda din egen Dojo** för att komma åt Blockchain-information och sända transaktioner.\*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

> Håll dina privata nycklar privata.

I den här artikeln utforskar vi allt du behöver veta om watch-only plånböcker. Vi diskuterar hur de fungerar och undersöker de olika applikationer som finns på marknaden. Slutligen erbjuder vi en detaljerad handledning om en av de mest populära Watch-only wallet-applikationerna: Sentinel.


## Vad är en Watch-only wallet?


En Watch-only wallet, eller en skrivskyddad Wallet, är en typ av programvara som är utformad så att användaren kan observera transaktioner som är kopplade till en eller flera specifika publika Bitcoin-nycklar, utan att ha tillgång till motsvarande privata nycklar.


Denna typ av applikation lagrar endast de data som krävs för att övervaka en Bitcoin Wallet, inklusive visning av dess saldo och transaktionshistorik, men den har inte tillgång till de privata nycklarna. Därför är det omöjligt att spendera de bitcoins som finns i Wallet i den applikation som endast övervakar.

![watch-only](assets/en/1.webp)

Watch-only används i allmänhet tillsammans med en Hardware Wallet. Detta gör det möjligt att lagra Wallet:s privata nycklar "Cold" på en enhet som inte är ansluten till internet, som har en minimal attackyta och isolerar de privata nycklarna från potentiellt sårbara miljöer. Applikationen för enbart bevakning lagrar å andra sidan enbart den utökade publika nyckeln (`xpub`, `zpub`, etc.) för Bitcoin Wallet. Denna överordnade nyckel gör det inte möjligt att upptäcka de tillhörande privata nycklarna och tillåter följaktligen inte att bitcoins spenderas. Den gör det dock möjligt att härleda barns publika nycklar och mottagaradresser. Med kunskap om adresserna till Wallet som säkrats av Hardware Wallet kan watch-only-applikationen spåra dessa transaktioner i Bitcoin-nätverket, vilket ger användaren möjlighet att övervaka sitt saldo och generate nya mottagningsadresser utan att behöva ansluta sin Hardware Wallet varje gång.


## Vilken Watch-only wallet ska man använda?


För närvarande är den mest omfattande applikationen för endast bevakning [Sentinel] (https://sentinel.watch/), utvecklad av teamen på Samourai Wallet. Den omfattar alla väsentliga funktioner för en bra Watch-only wallet:



- Stöd för utökade nycklar, publika nycklar och adresser;
- Möjligheten att organisera flera konton eller plånböcker i samlingar;
- Generering av adresser för att ta emot bitcoins på ens Hardware Wallet utan att kräva direkt användning;
- Möjligheten att konstruera och sända transaktioner offline;
- Möjlighet att ansluta till en egen Bitcoin-nod;
- Integrering av Tor för ökad integritet.

De unika nackdelarna med Sentinel ligger i det faktum att applikationen är exklusivt tillgänglig för Android och att den inte stöder plånböcker med flera signaturer. Om du äger en Android-enhet och din Wallet är en klassisk enstaka signatur rekommenderar jag därför Sentinel.

För dem som vill spåra en Wallet med flera signaturer är Blue Wallet den enda applikationen jag känner till som erbjuder ett klockläge för dessa typer av plånböcker, och den är tillgänglig på både Android och iOS.


För iOS-användare som letar efter ett alternativ till Sentinel kan [Green Wallet](https://blockstream.com/Green/) eller [Blue Wallet](https://bluewallet.io/watch-only/) vara alternativ, även om deras klockfunktionalitet inte är lika omfattande som Sentinels.

![watch-only](assets/notext/2.webp)


## Hur använder man Sentinel Watch-only wallet?


### Installation och konfigurering


Börja med att installera Sentinel-applikationen. Du kan göra detta antingen från Google Play Store eller genom att använda [APK tillgänglig för nedladdning på den officiella webbplatsen] (https://sentinel.watch/download/).


![watch-only](assets/notext/3.webp)


När du öppnar applikationen första gången får du välja mellan:



- "Anslut till Dojo";
- `Anslut till Samourais server`.


Dojo, som utvecklats av Samourai-teamet, är en fullständig Bitcoin-nodversion som kan installeras fristående eller läggas till med ett klick till node-in-box-lösningar som [Umbrel] (https://umbrel.com/) och [RoninDojo] (https://ronindojo.io/).


[**-> Upptäck hur du installerar RoninDojo v2 på en Raspberry Pi.**](https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8)


Om du har en egen Dojo kan du ansluta den i det här skedet. Genom att göra det kommer du att dra nytta av den högsta sekretessnivån när du kontrollerar transaktionsinformationen för ditt Bitcoin-nätverk.


![watch-only](assets/notext/4.webp)


Annars är det möjligt att välja Samourais standardserver. Du kan också välja om du vill ansluta via Tor eller inte.


![watch-only](assets/notext/5.webp)


Du kommer då att komma till Sentinels huvudsida.


![watch-only](assets/notext/6.webp)


För att komma igång kan du konfigurera applikationen. Klicka på de tre små prickarna i övre högra hörnet och sedan på `Settings`.


![watch-only](assets/notext/7.webp)

Genom att välja `User PIN code` har du möjlighet att ange ett lösenord för att säkra åtkomsten till din Watch-only wallet. Du har också möjlighet att ändra referensvalutan för att konvertera dina saldon till fiat-valuta, eller till och med att dölja fiat-värden genom att aktivera alternativet `Dölj fiat-värden`. För ökad säkerhet kan du aktivera `Disable Screenshots`, som förhindrar skärmdumpar av din Sentinel-applikation och därmed undviker att information avslöjas på en extern skärm.

![watch-only](assets/notext/8.webp)


I den här inställningsmenyn har du också möjlighet att säkerhetskopiera din Sentinel.


### Använda Watch-only wallet


Från startsidan trycker du på den blå knappen "NY" för att lägga till en ny utökad offentlig nyckel att spåra. Du har sedan möjlighet att skanna QR-koden för din nyckel, eller att direkt klistra in nyckeln (`xpub`, `zpub`...) genom att välja `Pasta Pubkey`.


![watch-only](assets/notext/9.webp)


I allmänhet är `xpub` för din Wallet direkt tillgänglig via den programvara för Wallet-hantering som du använder. Om du t.ex. hanterar din Hardware Wallet med Sparrow finns denna information på fliken "Inställningar" under avsnittet "Keystore".


![watch-only](assets/notext/10.webp)


När du har angett den utökade publika nyckeln i Sentinel erbjuder programmet dig att skapa en ny samling. En samling representerar en uppsättning utökade publika nycklar som är organiserade tillsammans. Det här alternativet ger dig möjlighet att inte bara lista alla dina "xpubar", utan att klassificera dem på ett ordnat sätt. Om du till exempel har en Samourai Wallet med flera konton (insättning, premix, postmix ...) kan du samla alla dessa konton under samlingen `Samourai`. För plånböcker som hanteras för din familj kan du skapa en samling med namnet `Family`.


Välj "Skapa ny samling". Ange sedan ett namn för den utökade nyckel som du just har integrerat. Om jag till exempel skannar insättningskontot för min Samourai Wallet, skulle jag namnge den här nyckeln `Deposit`. Klicka på `SAVE` för att slutföra.


![watch-only](assets/notext/11.webp)


Ge sedan samlingen ett namn och tryck på valideringsikonen längst upp till höger på skärmen för att spara samlingen. Din samling är nu synlig på Sentinels startskärm.


![watch-only](assets/notext/12.webp)


Om du vill lägga till en annan utökad publik nyckel klickar du på `NEW` igen och anger din nyckel.


![watch-only](assets/notext/13.webp)

Du kommer sedan att uppmanas att välja den samling du vill integrera den här nyckeln i, eller att skapa en ny. I mitt fall har jag till exempel skapat en samling specifikt för min Ledger Wallet.

![watch-only](assets/notext/14.webp)


För att se de utökade nycklarna för en samling i detalj klickar du bara på den. Du kan sedan navigera genom de olika flikarna för att se transaktionshistoriken.


![watch-only](assets/notext/15.webp)


Från en samling, genom att trycka på de tre små prickarna längst upp till höger och sedan på `Visa oanvända utgångar`, kan du komma åt en lista över UTXO som innehas av den spårade Wallet.


![watch-only](assets/notext/16.webp)


### Skicka och ta emot Bitcoins från Sentinel


Som med alla bra Watch-only wallet låter Sentinel dig generate mottagande adresser för att ta emot bitcoins på den spårade Wallet. Men Sentinel erbjuder också en annan avancerad funktion: skapandet och sändningen av en Partially Signed Bitcoin Transaction (PSBT). Således kan Wallet som håller de privata nycklarna underteckna denna transaktion, som, när den väl har undertecknats, kan sändas på Bitcoin-nätverket av Sentinel. Låt oss se hur man gör allt detta.


**Försiktighet, det rekommenderas inte att ta emot bitcoins på en mottagande Address som inte verifierats av Wallet själv.** Om Wallet som håller de privata nycklarna, till exempel en Hardware Wallet, inte uttryckligen har bekräftat att en viss Address är ansluten till den, är det riskabelt att skicka bitcoins till denna Address. Utan denna bekräftelse finns det faktiskt ingen garanti för att Address verkligen tillhör din Wallet. Därför bör mottagningsfunktionen hos en Watch-only wallet användas med försiktighet, med tanke på att de skickade medlen potentiellt kan gå förlorade.


För att ta emot bitcoins via Sentinel väljer du den samling du är intresserad av och klickar sedan på fliken som motsvarar den utökade publika nyckel som du vill överföra pengar till.


![watch-only](assets/notext/17.webp)


Klicka slutligen på pilikonen längst ner till vänster på skärmen. Sentinel genererar då en tom mottagnings Address åt dig. Du kan kopiera den eller skanna den med hjälp av QR-koden.


![watch-only](assets/notext/18.webp)


För att generate en PSBT från Sentinel, och därmed initiera en utgiftstransaktion, går du till den förlängda nyckeln för den Wallet från vilken du vill göra betalningen. Låt oss till exempel ta mitt insättningskonto på min Samourai Wallet. Klicka sedan på pilikonen längst ner till höger på skärmen.


![watch-only](assets/notext/19.webp)


Ange alla parametrar som är relaterade till din transaktion:



- Ange mottagarens Address (genom att klicka på QR-kodsymbolen har du möjlighet att skanna denna Address);
- Ange det belopp som ska skickas till denna Address;
- Bestäm transaktionsavgifterna.


När du har fyllt i alla nödvändiga fält för din transaktion trycker du på knappen `KOMPONERA OSIGNERAD TRANSAKTION`.


![watch-only](assets/notext/20.webp)


Du kommer då att få tillgång till PSBT, som representerar en konstruerad men osignerad Bitcoin-transaktion, eftersom Sentinel inte har tillgång till dina privata nycklar. Du har möjlighet att kopiera denna transaktion, exportera den som en `.PSBT`-fil eller skanna den via den animerade QR-koden.


![watch-only](assets/notext/21.webp)


Gå sedan till din Wallet som har de privata nycklarna för att signera transaktionen (Samourai, Hardware Wallet ...).


![watch-only](assets/notext/22.webp)


När transaktionen är signerad kan du gå tillbaka till Sentinel för att sända den. Detta gör du genom att från startmenyn klicka på de tre små prickarna uppe till höger och sedan på `Broadcast transaction`.


![watch-only](assets/notext/23.webp)


Du har möjlighet att ange din signerade PSBT på tre olika sätt:



- Genom att klistra in det direkt från ditt urklipp;
- Genom att importera den från en `.PSBT`-fil;
- Genom att skanna den via en QR-kod.


![watch-only](assets/notext/24.webp)


När den signerade transaktionen är inlagd i den grå ramen kan du klicka på Green `BROADCAST TRANSACTION`-knappen för att sända den på Bitcoin-nätverket. Sentinel kommer att ge dig sin txid.


![watch-only](assets/notext/25.webp)