---
name: Tårta Wallet
description: Handledning om Cake Wallet och Silent Payments
---

![cover](assets/cover.webp)


Denna guide utforskar [**Cake Wallet**](https://cakewallet.com/): en öppen källkod, icke-frihetsberövande, integritetsfokuserad Wallet med flera valutor tillgänglig för Android, iOS, macOS, Linux och Windows. Vi kommer att dyka in i dess Bitcoin-specifika sekretessfunktioner, gå igenom att skicka / ta emot Bitcoin via **Silent Payments** (ett förbättrat On-Chain sekretessprotokoll) och titta på implementeringen av PayJoin v2 för asynkrona transaktioner.


## 🎉 Viktiga funktioner



- [**Silent Payments (BIP-352)**](https://BIPs.dev/352/) förbättrar den tidigare [BIP 47 betalningskoder](https://silentpayments.xyz/docs/comparing-proposals/bip47/) även kallad "PayNyms" med återanvändbara stealth-adresser. När en avsändare använder din Tyst Betalning Address, härleder deras Wallet en unik engångs Address med olika nycklar som kommer att kombineras till en unik engångs Taproot Address. Blockchain-posterna visar orelaterade transaktioner, vilket förhindrar koppling av inkommande betalningar. Tysta betalningar erbjuder en rad fördelar, bland annat:
    - Återanvändbara adresser: Inget behov av att generate en ny Address för varje transaktion, vilket ger en bättre användarupplevelse och ökad integritet
    - Ingen kostnadsökning: Tysta betalningar ökar inte storleken på eller kostnaden för transaktioner.
    - Förbättrad anonymitet: Utomstående observatörer kan inte koppla transaktioner till en Silent Payment Address.
    - Ingen interaktion mellan avsändare och mottagare krävs: Transaktioner kan göras utan någon kommunikation mellan parterna.
    - Unika adresser för varje betalning: Eliminerar risken för oavsiktlig återanvändning av Address.
    - Ingen server krävs: Tysta betalningar kan göras utan att det behövs en dedikerad server.
- PayJoin v2** mildrar transaktionsgrafanalys genom att slå samman sändarnas och mottagarnas inmatningar till en enda transaktion. Cake Wallet implementerar två kritiska framsteg:
    - Asynkrona transaktioner**: Avsändare och mottagare behöver inte längre vara online samtidigt för att genomföra en privat transaktion.
    - Serverlös kommunikation**: Ingen av parterna behöver köra en PayJoin-server, vilket undanröjer ett stort tekniskt hinder.
- Coin Control** möjliggör manuellt val av UTXO under transaktioner. Detta förhindrar oavsiktlig koppling av adresser när flera UTXO:er med olika ursprung används.
- TOR**-stöd, vilket gör det möjligt för användare att dirigera sin nätverkstrafik genom Tor-nätverket
- Med RBF** (Replace-By.Fee) kan du justera avgiften efter att du har skickat en transaktion.


## 1️⃣ Konfigurera din Wallet


Cake Wallet erbjuder ett brett utbud av plattformsstöd. Du kan välja mellan `Android`, `iOS / macOS`, `Linux` och `Windows`.  För att börja, besök https://docs.cakewallet.com/get-started/ och välj ditt operativsystem.


![image](assets/en/01.webp)


Efter installationen ställer du in ett PIN-kod (4 eller 6 siffror). Du kommer då att se:


1. "Skapa en ny Wallet" (för nya användare)

2. `Restore Wallet` (för befintliga plånböcker)


![image](assets/en/02.webp)


På nästa skärm kan du välja mellan ett brett utbud av kryptovalutor. Välj `Bitcoin` och tryck på `Nästa` och ange ett `Wallet-namn` för att identifiera Wallet. Genom att trycka på `Avancerade inställningar` visas en rad `Privacy Stettings`. Gör dessa ändringar:



- Fiat API:** välj `Tor Only` (skickar prisförfrågningar via Tor)
- Swap:** välj `Tor Only` (anonymiserar Exchange trafik)


Typ BIP-39 seed genereras som standard, med möjlighet att ändra till typ Electrum seed. Härledningsvägarna är följande:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Om du vill lägga till en extra säkerhet Layer kan du sätta upp en `passphrase`.  Huvudsyftet med en passphrase är att ge ytterligare skydd mot fysiska attacker. Även om en angripare hittar seed-frasen kan de inte komma åt din Wallet utan rätt passphrase. Med andra ord representerar seed-frasen ensam en Wallet, medan seed-frasen plus passphrase skapar en helt annan Wallet utan någon koppling till originalet. Denna funktion möjliggör också "hemliga plånböcker" som skyddas av passphrase och ger dig trovärdig förnekelse. I en tvångssituation kan du avslöja seed-frasen medan du håller större tillgångar säkra i den passphrase-skyddade Wallet.


Om du redan kör din egen nod kan du växla `Add New Custom Node` och tillhandahålla din `Node Address` för att validera transaktioner och block inom din egen infrastruktur. När du är klar trycker du på `Continue` och `Next` för att skapa din Wallet.


![image](assets/en/03.webp)


På nästa skärm får du en ansvarsfriskrivning:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


För att lära dig bästa praxis för att spara din Mnemonic-fras, se denna handledning:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Tryck på `Jag förstår. Visa mig min seed` och spara dessa ord på en säker plats! Tryck sedan på `Verifiera seed` och efter verifiering `Öppna Wallet`.


## 2️⃣ Inställningar


Innan vi går in på djupet ska vi ta en titt på "Startskärm" och "Inställningar".


På startskärmen kan vi se olika objekt som visas:



- i `Hamburgermenyn` kommer vi till `inställningar`
- Tillgängligt saldo
- Silent Payments Card för att börja skanna transaktioner som skickas till din Silent Payment Address
- PayJoin-kort för att `aktivera` PayJoin som integritetsskyddande och avgiftsbesparande funktion
- längst ner finns genvägar till `Wallet Översikt`, `Motta`, `Swappa` mellan Bitcoin och andra valutor, `Sända` och `Köpa`


![image](assets/en/11.webp)


Genom att trycka på ikonen `Hamburgermeny` öppnas inställningsmenyn. Låt oss granska alternativen.


![image](assets/en/05.webp)


### A - Anslutning och synkronisering 🔗


Här kan vi återansluta Wallet, hantera noder och ansluta till vår egen nod (rekommenderas). Med `Silent Payments Scanning` kan vi anpassa skanningen genom att ange antingen `Scan from BLOCK height` eller `Scan from date`.


![image](assets/en/06.webp)


Som en "Alpha"-funktion finns det också möjlighet att "Aktivera inbyggd Tor" för att dirigera trafik genom Tor-nätverket.


### B - Inställningar för tysta betalningar 🔈


Vi kan växla mellan Silent Payments-kortet på hemskärmen för att visa den här funktionen. Om du aktiverar `Alltid skanning` kan Wallet kontinuerligt övervaka Blockchain för inkommande tysta betalningar. Vi kan ange skanningsparametrar för att anpassa skanningsprocessen till våra behov enligt beskrivningen ovan.


![image](assets/en/07.webp)


### C - Säkerhet och backup 🗝️


För att säkra vår Wallet kan vi skapa en säkerhetskopia genom att följa anvisningarna i appen. Detta säkerställer att vi har en säker kopia av våra privata nycklar, så att vi kan återställa vår Wallet om den tappas bort eller blir stulen. Dessutom kan vi visa vår seed-fras och våra privata nycklar, ändra vår PIN-kod, aktivera biometrisk autentisering, signera/verifiera och ställa in 2FA för ett extra Layer-skydd.


![image](assets/en/08.webp)


**Notera**: Från och med september 2025 måste biometrisk autentisering med fingeravtryck på Android-enheter fungera med minst en biometrisk implementering av klass 2. För mer information se [här] (https://source.android.com/docs/security/features/biometric/measure#biometric-classes). Detta krav kan dock komma att ändras i framtiden.


### D - Sekretessinställningar 🔒


Vi kan också förbättra vår Wallet:s säkerhet genom att använda Tor för att kryptera vår internetanslutning och skydda vår integritet när vi besöker externa källor. Dessutom kan vi förhindra skärmdumpar för att hålla vår Wallet-information konfidentiell, aktivera autogenererade adresser för att skapa nya för varje transaktion och inaktivera köp-/säljåtgärder för att förhindra obehöriga transaktioner. Dessutom kan vi "Aktivera PayJoin", vilket är en annan sekretessfunktion som vi kommer att granska senare.


![image](assets/en/09.webp)


### E - Övriga inställningar 🔧


Andra inställningar gör att vi kan hantera avgiftsprioriteringen och ställa in standardavgiftsnivån för våra transaktioner. Detta gör det möjligt för oss att kontrollera de transaktionsavgifter som är förknippade med våra Tysta betalningar, med hänsyn till aktuellt nätverksutnyttjande.


![image](assets/en/10.webp)


## 3️⃣ Ta emot ₿itcoin med hjälp av tysta betalningar


Det finns flera alternativ och Address-typer tillgängliga för mottagning av Bitcoin. `SegWit (P2WPKH)` *(börjar med bc1q....)* är standardalternativet.  Låt oss välja `Silent Payments` i det här exemplet.


För att ta emot en Silent Payment, tryck först på ikonen `Receive` i Cake Wallet. Därefter anger du det belopp du förväntar dig att få. För att specificera typen av Address, tryck på `Receive` igen högst upp på skärmen igen och välj sedan `Silent Payments` från alternativen.


På huvudskärmen visas din återanvändbara Silent Payment QR-kod och Address. Som förväntat är Address ganska lång:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Använd nu en BIP-352-kompatibel Wallet (t.ex. Blue Wallet) för att skanna denna QR-kod och skicka betalningen. Du kommer att se att Wallet härleder en unik destination Address från din tysta Address.


![image](assets/en/13.webp)


## 4️⃣ Skicka ₿itcoin med hjälp av tysta betalningar


Eftersom Blue Wallet endast kan "skicka" tysta betalningar, kommer vi att använda en annan BIP 352 kompatibel Wallet som mottagande part. Denna process är identisk med den för en vanlig Bitcoin-transaktion.



- Tryck på `Sänd` på startskärmen
- antingen klistra in vår återanvändbara `sp1qq...` Address eller skanna QR-koden direkt i appen.
- Välj hur mycket du vill spendera från ditt tillgängliga saldo
- Tryck på `Send` längst ner på skärmen för att bekräfta transaktionen


När vi har angett `sp1qq...` Address, härleder Wallet automatiskt en motsvarande `bc1p...` Taproot Address (P2TR) i bakgrunden, som kommer att användas för den tysta betalningen.


Vi har möjlighet att skriva en intern anteckning för varje transaktion, justera avgiftsinställningarna eller välja vissa UTXO:er för transaktionen med hjälp av funktionen "Coin Control".


![image](assets/en/14.webp)


swipea till höger för att bekräfta transaktionen.


När du har skickat transaktionen kommer du att få frågan om du vill lägga till den här kontakten i din Address-bok.


![image](assets/en/15.webp)


## 6️⃣ PayJoin


Låt oss granska vad PayJoin är [om] (https://docs.cakewallet.com/cryptos/Bitcoin/#PayJoin):


_Payjoin v2 är en integritetsbevarande och avgiftsbesparande funktion i Bitcoin som gör det möjligt för avsändaren och mottagaren av en transaktion att arbeta tillsammans för att skapa en enda transaktion. Denna transaktion har ingångar från *både* avsändaren och mottagaren, vilket bryter de vanligaste övervakningsteknikerna mot Bitcoin och möjliggör bättre skalning och avgiftsbesparingar under vissa omständigheter också._


För att lära dig mer om PayJoin kan du också besöka följande handledning.


https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

För att använda PayJoin behöver båda parter en PayJoin-kompatibel Wallet, och mottagaren måste ha minst en Coin eller utgång i sin Wallet. Följ dessa steg för att börja:


1. Tryck på `Hamburger Menu` och tryck på `Privacy`-knappen

2. Växla alternativet `Använd PayJoin`

3.  Tryck på `Receive` på hemskärmen och du kommer att presenteras med en PayJoin QR-kod och kopieringsknapp (när du väljer SegWit)


![image](assets/en/16.webp)


## 7️⃣ Övriga funktioner


Det finns flera andra funktioner som "swappar" i flera valutor, "köp och sälj" -alternativ med olika leverantörsanslutningar och kakspecifika program som "Cake Pay", som låter dig köpa förbetalda kort eller presentkort.


![image](assets/en/17.webp)


## 🎯 Slutsats


Detta är vår recension av Cake Wallet, som erbjuder praktisk Bitcoin-sekretess tack vare funktioner som Silent Payments (BIP-352) och PayJoin v2.


Tysta betalningar ersätter engångsadresser med återanvändbara smygadresser för att förhindra On-Chain-koppling av inkommande transaktioner. Även om synkroniseringsproblemen i tidigare versioner har förbättrats avsevärt, krävs det vissa ökade beräkningskrav för att skanna och upptäcka tysta betalningar, vilket kräver mer resurser och bandbredd.


PayJoin v2 stör kedjeanalysen genom att slå samman avsändarens och mottagarens inmatningar till en enda transaktion utan extra avgifter eller central samordning. Detta bryter den gemensamma input-Ownership-heuristiken, vilket är en betydande fördel eftersom det innebär att du inte kan anta att alla inputs tillhör avsändaren.


För användare som prioriterar finansiell anonymitet är Cake Wallet ett genomförbart alternativ. Den införlivar sekretessprotokoll direkt i sin kärnfunktionalitet, vilket gör dem tillgängliga utan teknisk komplexitet. När övervakningen av offentliga blockkedjor ökar hjälper verktyg som detta till att upprätthålla transaktionell integritet där det betyder mest. En bredare implementering av dessa standarder inom Wallet-landskapet skulle vara en välkommen utveckling.


## 📚 Resurser


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://BIPs.dev/352/](https://BIPs.dev/352/)


https://PayJoin.org/