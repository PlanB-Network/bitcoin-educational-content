---
name: PayJoin - Sparv Wallet
description: Hur gör man en PayJoin-transaktion på Sparrow Wallet?
---

![tutorial cover image sparrow payjoin](assets/cover.webp)


_**VARNING:** Efter gripandet av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april fungerar Payjoins Stowaway på Samourai Wallet nu endast genom att manuellt utbyta PSBT mellan de inblandade parterna, förutsatt att båda användarna är anslutna till sin egen Dojo. När det gäller Sparrow fungerar Payjoins via BIP78 fortfarande. Dessa verktyg kan dock komma att startas om under de kommande veckorna. Under tiden kan du alltid läsa den här artikeln för att förstå den teoretiska funktionen av payjoins._


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

> *Tvinga Blockchain-spioner att ompröva allt de tror att de vet *

PayJoin är en specifik Bitcoin-transaktionsstruktur som förbättrar användarens integritet under utgifterna genom att samarbeta med betalningsmottagaren. Det finns flera implementeringar som underlättar installationen och automatiseringen av PayJoin. Bland dessa implementeringar är den mest kända Stowaway som utvecklats av Samourai Wallet-teamet. Denna handledning syftar till att vägleda dig genom processen att göra en Stowaway PayJoin-transaktion med Sparrow Wallet-programvaran.


## Hur fungerar Stowaway?


Som tidigare nämnts erbjuder Samourai Wallet ett PayJoin-verktyg som heter "Stowaway" Det är tillgängligt via Sparrow Wallet-programvaran på PC eller Samourai Wallet-applikationen på Android. För att utföra en PayJoin måste mottagaren, som också fungerar som samarbetspartner, använda programvara som är kompatibel med Stowaway, nämligen Sparrow eller Samourai Wallet. Dessa två programvaror är kompatibla och möjliggör Stowaway-transaktioner mellan en Sparrow Wallet och en Samourai Wallet, och vice versa.


Stowaway förlitar sig på en kategori av transaktioner som Samourai kallar "Cahoots" En Cahoot är i huvudsak en samarbetstransaktion mellan flera användare som kräver off-chain-information Exchange. För närvarande erbjuder Samourai två Cahoots-verktyg: Stowaway (Payjoins) och StonewallX2 (som vi kommer att utforska i en framtida artikel).


Cahoots-transaktioner innebär att delvis signerade transaktioner utväxlas mellan användare. Denna process kan vara lång och besvärlig, särskilt när den görs på distans. Det kan dock fortfarande göras manuellt med en annan användare, vilket kan vara praktiskt om medarbetarna befinner sig fysiskt nära varandra. I praktiken innebär detta att man manuellt utbyter fem QR-koder som ska skannas successivt.


När det görs på distans blir denna process alltför komplex. För att Address detta problem har Samourai utvecklat ett krypterat kommunikationsprotokoll baserat på Tor, kallat "Soroban" Med Soroban automatiseras de nödvändiga utbytena för en PayJoin bakom en användarvänlig Interface. Detta är den andra metoden vi kommer att utforska i den här artikeln.


Dessa krypterade utbyten kräver att en anslutning och autentisering upprättas mellan Cahoots-deltagarna. Soroban-kommunikation förlitar sig på användarnas Paynyms. Om du inte är bekant med Paynyms, uppmanar jag dig att hänvisa till den här artikeln för mer information: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/On-Chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)

Enkelt uttryckt är en Paynym en unik identifierare kopplad till din Wallet som möjliggör olika funktioner, bland annat krypterade meddelanden. Paynym presenteras i form av en identifierare och en illustration som representerar en robot. Här är ett exempel på min på Testnet: ![Paynym Sparrow](assets/en/1.webp)


**I sammanfattning:**



- _Payjoin_ = Specifik struktur för samarbetstransaktioner;
- _Stowaway_ = PayJoin implementation tillgänglig på Samourai och Sparrow Wallet;
- _Cahoots_ = Samourais namn på alla deras typer av samarbetstransaktioner, inklusive PayJoin Stowaway;
- _Soroban_ = Krypterat kommunikationsprotokoll etablerat på Tor, som möjliggör samarbete med andra användare inom ramen för en Cahoots-transaktion.
- _Paynym_ = Unik identifierare för en Wallet som möjliggör kommunikation med en annan användare på Soroban, för att

genomföra en Cahoots-transaktion.


[**-> Läs mer om PayJoin-transaktioner och deras användbarhet**](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)


## Hur upprättar man en förbindelse mellan Paynyms?


För att utföra en Cahoots-transaktion på distans, specifikt en PayJoin (Stowaway) via Samourai eller Sparrow, är det nödvändigt att "följa" den användare du tänker samarbeta med, med hjälp av deras Paynym. När det gäller en fripassagerare innebär detta att följa den person som du vill skicka bitcoins till.


**Så här går du tillväga för att upprätta denna anslutning:**


Först måste du få tag på mottagarens Paynym-identifierare. Detta kan göras med hjälp av deras smeknamn eller betalkod. För att göra detta, från mottagarens Sparrow Wallet, välj fliken `Tools` och klicka sedan på `Show PayNym`.

![Show Paynym](assets/notext/2.webp)

![Paynym Sparrow](assets/en/1.webp)

På din sida öppnar du Sparrow Wallet och går till samma meny `Show PayNym`. Om du använder ditt Paynym för första gången måste du få en identifierare genom att klicka på `Retrieve PayNym`.

![Retrieve paynym](assets/notext/3.webp)

Ange sedan din medarbetares Paynym-identifierare (antingen deras smeknamn `+...` eller deras betalkod `PM...`) i rutan `Find Contact` och klicka sedan på knappen `Add Contact`.

![add contact](assets/notext/4.webp)

Programvaran kommer då att erbjuda dig en "Länk kontakt" -knapp. Det är inte nödvändigt att klicka på den här knappen för vår handledning. Detta steg är endast nödvändigt om du planerar att göra betalningar till Paynym som anges i samband med BIP47, vilket inte är relaterat till vår handledning.


När mottagarens Paynym följs av din Paynym upprepar du denna operation i motsatt riktning så att din mottagare också följer dig. Du kan sedan utföra en PayJoin.


## Hur utför man en PayJoin på Sparrow Wallet?


Om du har slutfört dessa preliminära steg är du äntligen redo att utföra PayJoin-transaktionen! För att göra detta, följ vår videohandledning:

![Payjoin Tutorial - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)


**Externa resurser:**



- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.