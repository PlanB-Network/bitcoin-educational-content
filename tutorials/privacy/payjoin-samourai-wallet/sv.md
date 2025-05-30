---
name: PayJoin - Samourai Wallet
description: Hur utför man en PayJoin transaktion på Samourai Wallet?
---
![samourai payjoin cover](assets/cover.webp)


***Efter gripandet av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april fungerar Payjoins Stowaway på Samourai Wallet endast genom att manuellt utbyta PSBT mellan de berörda parterna, förutsatt att båda användarna är anslutna till sin egen Dojo. När det gäller Sparrow fungerar Payjoins via BIP78 fortfarande. Det är dock möjligt att dessa verktyg kommer att återlanseras under de kommande veckorna. Under tiden kan du fortfarande läsa den här artikeln för att förstå den teoretiska funktionen av Stowaway.*


om du planerar att utföra en Stowaway manuellt är proceduren mycket lik den som beskrivs i denna handledning. Den största skillnaden ligger i valet av typ av fripassagerartransaktion: istället för att välja `Online`, klicka på `In Person / Manual`. Sedan måste du manuellt Exchange PSBT:erna för att konstruera fripassagerartransaktionen. Om du befinner dig fysiskt nära din medarbetare kan du skanna QR-koderna successivt. Om ni befinner er på avstånd kan JSON-filer utbytas via en säker kommunikationskanal. Resten av handledningen förblir oförändrad


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

> *Tvinga Blockchain-spioner att ompröva allt de tror att de vet *

PayJoin är en specifik Bitcoin-transaktionsstruktur som förbättrar användarens integritet under en utgift genom att samarbeta med betalningsmottagaren. Det finns flera implementeringar som underlättar installationen och automatiseringen av PayJoin. Bland dessa implementeringar är Stowaway, som utvecklats av teamen på Samourai Wallet, den mest kända. Denna handledning förklarar hur man utför en Stowaway PayJoin-transaktion med Samourai Wallet-programmet.


## Hur fungerar Stowaway?


Som tidigare nämnts erbjuder Samourai Wallet ett PayJoin-verktyg som heter "Stowaway" Det är tillgängligt via Sparrow Wallet-programvaran på PC eller Samourai Wallet-applikationen på Android. För att utföra en PayJoin måste mottagaren, som också fungerar som samarbetspartner, använda programvara som är kompatibel med Stowaway, nämligen Sparrow eller Samourai. Dessa två programvaror är kompatibla med varandra, vilket möjliggör en Stowaway-transaktion mellan en Sparrow Wallet och en Samourai Wallet, och vice versa.


Stowaway förlitar sig på en kategori av transaktioner som Samourai kallar "Cahoots" En Cahoot är i huvudsak en samarbetstransaktion mellan flera användare, vilket kräver off-chain-information Exchange. Hittills erbjuder Samourai två Cahoots-verktyg: Stowaway (Payjoins) och StonewallX2 (som vi kommer att utforska i en framtida artikel).


Cahoots-transaktioner innebär utbyte av delvis signerade transaktioner mellan användare. Denna process kan vara lång och besvärlig, särskilt när den görs på distans. Den kan dock fortfarande utföras manuellt med en annan användare, vilket kan vara bekvämt om medarbetarna befinner sig fysiskt nära varandra. I praktiken innebär detta att man manuellt utbyter fem QR-koder som ska skannas successivt.


När det görs på distans blir denna process alltför komplex. För att lösa Address-problemet har Samourai utvecklat ett krypterat kommunikationsprotokoll baserat på Tor, kallat "Soroban" Med Soroban automatiseras de utbyten som är nödvändiga för en PayJoin bakom en användarvänlig Interface. Detta är den andra metoden vi kommer att studera i den här artikeln.


Dessa krypterade utbyten kräver att en anslutning och autentisering upprättas mellan Cahoots-deltagarna. Soroban-kommunikation är därför baserad på användarnas Paynyms. Om du inte är bekant med Paynyms, uppmanar jag dig att läsa den här artikeln för mer information: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/On-Chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)



Enkelt uttryckt är en Paynym en unik identifierare kopplad till din Wallet som möjliggör olika funktioner, bland annat krypterade meddelanden. Paynym presenteras i form av en identifierare och en illustration som representerar en robot. Här är ett exempel på min på Testnet: ![paynym samourai Wallet](assets/en/1.webp)


**I sammanfattning:**


- _Payjoin_ = Specifik struktur för kollaborativa transaktioner;
- _Stowaway_ = PayJoin implementation tillgänglig på Samourai och Sparrow Wallet;
- _Cahoots_ = Samourais namn på alla deras typer av samarbetstransaktioner, inklusive PayJoin Stowaway;
- _Soroban_ = Krypterat kommunikationsprotokoll etablerat på Tor, som möjliggör samarbete med andra användare inom ramen för en Cahoots-transaktion;
- _Paynym_ = Unik identifierare för en Wallet som möjliggör kommunikation med en annan användare på Soroban, för att genomföra en Cahoots-transaktion.


[**-> Läs mer om PayJoin-transaktioner och deras användbarhet**](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)


## Hur upprättar man en förbindelse mellan Paynyms?


För att genomföra en Cahoots-transaktion på distans, särskilt en PayJoin (Stowaway) via Samourai, är det nödvändigt att "följa" den användare som du tänker samarbeta med, med hjälp av deras Paynym. När det gäller en fripassagerare innebär detta att följa den person som du vill skicka bitcoins till.


**Så här går du tillväga för att upprätta denna anslutning:**


Till att börja med måste du få betalningskoden för mottagarens Paynym för PayJoin. I Samourai Wallet-applikationen måste mottagaren trycka på ikonen för sin Paynym (den lilla roboten) längst upp till vänster på skärmen och sedan klicka på sitt Paynym-smeknamn, som börjar med `+...`. Mitt är till exempel `+namelessmode0aF`. Om din samarbetspartner använder Sparrow Wallet, ber jag dig att läsa vår särskilda handledning genom att klicka här.


![connexion paynym samourai](assets/notext/2.webp)


Din medarbetare kommer då att omdirigeras till sin Paynym-sida. Där kan de antingen dela sina Paynym-referenser med dig eller dela sin QR-kod som du kan skanna. För att göra detta måste de klicka på den lilla "dela"-ikonen längst upp till höger på sin skärm.

![partager paynym samourai](assets/en/1.webp)


På din sida startar du din Samourai Wallet-applikation och öppnar menyn "PayNyms" på samma sätt. Om det är första gången du använder din Paynym måste du skaffa identifieraren.


![demander un paynym](assets/notext/3.webp)


Klicka sedan på det blå "+" längst ner till höger på skärmen.

![ajouter paynym collaborateur](assets/notext/4.webp)

Du kan sedan klistra in din medarbetares betalningskod genom att välja `COLLER LE CODE PAIEMENT`, eller öppna kameran för att skanna deras QR-kod genom att trycka på `SCANNEZ LE CODE QR`.![klistra in paynym-identifierare](assets/notext/5.webp)


Klicka på "SUIVRE"-knappen.

![follow paynym](assets/notext/6.webp)

Bekräfta genom att klicka på `YES`.

![confirm follow paynym](assets/notext/7.webp)

Programvaran kommer då att erbjuda dig en "SE CONNECTER"-knapp. Det är inte nödvändigt att klicka på den här knappen för vår handledning. Detta steg krävs endast om du planerar att göra betalningar till den andra Paynym som en del av BIP47, vilket inte är relaterat till vår handledning.

![connect paynym](assets/notext/8.webp)

När mottagarens Paynym följs av din Paynym upprepar du denna operation i motsatt riktning så att mottagaren också följer dig. Du kan sedan utföra en PayJoin.


## Hur gör man en PayJoin på Samourai Wallet?


Om du har slutfört dessa preliminära steg är du äntligen redo att utföra PayJoin-transaktionen! För att göra detta, följ vår videohandledning:


![Payjoin Video Tutorial - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)


**Externa resurser:**


- https://docs.samourai.io/en/spend-tools#stowaway.