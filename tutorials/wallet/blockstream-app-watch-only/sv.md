---
name: Blockstream App - Watch-Only
description: Hur konfigurerar jag en Watch-only wallet på Blockstream App?
---

![cover](assets/cover.webp)


## 1. Inledning


### 1.1 Syfte med handledningen





- Den här handledningen förklarar hur du konfigurerar och använder funktionen **Watch-Only** i mobilapplikationen **Blockstream App** för att övervaka en Bitcoin Wallet utan att komma åt dess privata nycklar.
- Den omfattar installation, inledande konfiguration, import av en utökad publik nyckel och användning av den för att spåra saldon och generate-mottagningsadresser.
- Observera: Andra handledningar, som finns i appendix, täcker Onchain, Liquid och skrivbordsversionen.



### 1.2. Målgrupp





- **Nybörjare**: Användare som vill övervaka en Bitcoin-portfölj (ofta associerad med en Hardware Wallet) via en intuitiv mobilapplikation.
- **Användare på mellannivå**: Personer som vill hantera skrivskyddade portföljer samtidigt som de använder sekretessalternativ som Tor eller SPV.
- **Hardware Wallet ägare**: För att kontrollera sina saldon och generate-adresser utan att ansluta sin enhet.
- **Företag och butiker**:
 - Spåra dina transaktioner för bokföringsändamål utan att avslöja dina privata nycklar.
 - Verifiera transaktioner som tagits emot utan att ange sina privata nycklar i betalningssystem online.
 - Gör det möjligt för anställda att använda generate för nya mottagningsadresser utan att ha tillgång till privata nycklar.
- **Organisationer och crowdfunding**: Visa saldot öppet för givare utan att ge tillgång till medel.



### 1.3. Introduktion av Watch-Only



En **Watch-Only** Wallet gör att du kan övervaka transaktionerna och saldot för en Bitcoin Wallet utan att ha tillgång till de privata nycklarna. Till skillnad från en vanlig Wallet lagrar den endast publika data, såsom den **utökade publika nyckeln** (som gav upphov till **xpub**, sedan "zpub", "ypub", etc.), vilket gör det möjligt att få mottagningsadresser och spåra transaktionshistorik på Blockchain Bitcoin. Avsaknaden av privata nycklar gör det omöjligt att betala ut pengar från applikationen, vilket garanterar ökad säkerhet.



![image](assets/fr/10.webp)



**Varför använda en Watch-only wallet?**





- **Säkerhet**: Perfekt för övervakning av en portfölj som skyddas av en **Hardware Wallet** utan att exponera privata nycklar på en ansluten enhet.
- **Bekvämlighet**: Gör att du kan kontrollera saldot och generate nya mottagaradresser utan att ansluta Hardware Wallet.
- **Konfidentialitet**: Kompatibel med alternativ som **Tor** eller **SPV** för att begränsa beroendet av tredjepartsservrar.
- **Användningsfall**: Spåra pengar på resande fot, generera adresser för att ta emot betalningar eller verifiera transaktioner utan att riskera privata nycklar.



![image](assets/fr/01.webp)



### 1.4. Utökade publika nycklar



En **utökad publik nyckel** (xpub, ypub, zpub, etc.) är en uppgift som härrör från en Bitcoin Wallet som genererar alla underordnade publika nycklar och deras tillhörande mottagningsadresser, utan att ge tillgång till de privata nycklarna.





- Så här fungerar det: Den utökade publika nyckeln genereras från seed-frasen via en deterministisk process (BIP-32). Den skapar ett hierarkiskt träd av underordnade publika nycklar, som var och en kan konverteras till en mottagande Address. Genom att använda samma härledningsväg (t.ex. `m/44'/0'/0'`) som den bevakade Wallet genererar Watch-only wallet samma adresser, vilket gör det möjligt att spåra medel och skapa nya mottagningsadresser.



![image](assets/fr/11.webp)





- Utökade typer av publika nycklar
- **xpub**: Används för Legacy-portföljer (adresser som börjar med "1", BIP-44) och Taproot-portföljer (adresser som börjar med "bc1p", BIP-86).
- **ypub**: Utformad för kompatibla SegWit plånböcker (adresser som börjar med "3", BIP-49).
- **zpub**: Associated with native SegWit portfolios (adresser som börjar med "bc1q", BIP-84).
- **Övriga (tpub, upub, vpub, etc.)**: Används för alternativa nätverk (t.ex. Testnet) eller specifika standarder. Exempelvis är tpub för Testnet-nätverket.





- **Distinktion**: Valet mellan xpub, ypub eller zpub beror på typen av Address (legacy, SegWit, Taproot eller nested SegWit) och den BIP-standard som används av Wallet. Kontrollera vilket format som krävs av din källportfölj för att säkerställa kompatibilitet med Blockstream App.





- **Säkerhet och sekretess**: Den utökade publika nyckeln är inte känslig ur säkerhetssynpunkt, eftersom den inte tillåter att medel används (ingen tillgång till privata nycklar). Den är dock känslig när det gäller sekretess, eftersom den avslöjar alla publika adresser och tillhörande transaktionshistorik.



**Recommendation**: Skydda din utökade offentliga nyckel som känslig information.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Hot Wallet påminnelse





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: alla namn på en applikation som installeras på en smartphone, dator eller annan enhet som är ansluten till internet och som gör det möjligt att hantera och säkra privata nycklar från en Bitcoin Wallet.
- Till skillnad från **hardware wallets**, även kända som **Cold wallets**, som isolerar nycklar offline, fungerar mjukvaruplånböcker i en uppkopplad miljö, vilket gör dem mer sårbara för cyberattacker.





- **Rekommenderad användning**:
    - Idealisk för hantering av måttliga mängder Bitcoin, särskilt för dagliga transaktioner.
    - Lämplig för nybörjare eller användare med begränsade tillgångar, för vilka en Hardware Wallet kan verka överflödig.





- **Begränsningar**: Mindre säkert för förvaring av stora belopp eller långsiktiga besparingar. I så fall bör du välja en Hardware Wallet.




## 2. Vi presenterar Blockstream App





- **Blockstream App** är en mobil (iOS, Android) och stationär applikation för hantering av Bitcoin-portföljer och tillgångar på Liquid Network. Den förvärvades av [Blockstream](https://blockstream.com/) 2016 och hette tidigare *Green Address* och sedan *Blockstream Green*.
- **Viktiga egenskaper**:
- Onchain-transaktioner på **Blockchain Bitcoin**.
    - Transaktioner på **Liquid**-nätverket (Sidechain för snabba, konfidentiella utbyten).
- **Watch-only**-portföljer för övervakning av fonder utan tillgång till nycklar.
    - Sekretessalternativ: anslutning via **Tor**, anslutning till en **personlig nod** via Electrum, eller **SPV**-verifiering för att minska beroendet av tredjepartsnoder.
    - Fungerar **Replace-by-fee (RBF)** för att påskynda obekräftade transaktioner.
- **Kompatibilitet**: Integrerar hårdvaruplånböcker som **Blockstream Jade**.
- **Interface**: Intuitiv för nybörjare, med avancerade alternativ för experter.
- **Obs**: Den här guiden fokuserar på användning av onchain. Andra handledningar i bilagorna täcker Onchain, Watch-Only och skrivbordsversionen.




## 3. Installera och konfigurera Blockstream-appen



### 3.1. Ladda ner





- För **Android**:
    - Ladda ner [Blockstream App] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) från Google Play Store.
    - Alternativ: Installera via APK-filen som finns på [Blockstreams officiella GitHub] (https://github.com/Blockstream/green_android).
- För **iOS**:
    - Ladda ner [Blockstream App] (https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) från App Store.
- **Obs**: Var noga med att ladda ner från officiella källor för att undvika bedrägliga applikationer.



### 3.2. Initial konfiguration





- **Startskärm**: När programmet öppnas för första gången visas en skärm utan en konfigurerad Wallet. Skapade eller importerade portföljer kommer att visas här senare.



![image](assets/fr/02.webp)





- **Anpassa inställningar**: Klicka på "Application settings", justera alternativen nedan, klicka på "Save", starta om applikationen och skapa din portfölj.



![image](assets/fr/03.webp)



#### 3.2.1. Förbättrad sekretess (endast Android)





- **Funktion**: Inaktiverar skärmdumpar, döljer förhandsvisningar av program i aktivitetshanteraren och låser åtkomsten när telefonen är låst.
- **Varför?**: Skyddar dina data mot obehörig fysisk åtkomst eller skadlig programvara som fångar skärmen.



#### 3.2.2. Anslutning via Tor





- **Funktion**: Dirigera nätverkstrafik via **Tor**, ett anonymt nätverk som krypterar dina anslutningar.
- **Varför?**: Dölj din IP Address och skydda din integritet, perfekt om du inte litar på ditt nätverk (t.ex. offentligt Wi-Fi).
- **Nackdel**: Kan göra programmet långsammare på grund av kryptering.
- **Rekommendation**: Aktivera Tor om sekretess är en prioritet, men testa anslutningshastigheten.



#### 3.2.3. Ansluta till en personlig nod





- **Funktion**: Ansluter applikationen till din egen **kompletta Bitcoin-nod** via en **Electrum-server**.
- Varför? Ger total kontroll över Blockchain-data, vilket eliminerar beroendet av Blockstream-servrar.
- **Förutsättning**: En konfigurerad Bitcoin-nod.
- **Rekommendation**: Avancerade användare som vill ha maximal suveränitet.



#### 3.2.4. Verifiering av SPV





- **Funktion**: Använder **Simplified Payment Verification (SPV)** för att direkt verifiera vissa Blockchain-data utan att ladda ner hela kedjan.
- **Varför?**: Minskar beroendet av Blockstreams standardnod, samtidigt som den är lättviktig för mobila enheter.
- **Nackdel**: Mindre säker än en Full node, eftersom den förlitar sig på tredjepartsnoder för viss information.
- **Rekommendation**: Aktivera SPV om du inte kan använda en personlig nod, men föredrar en Full node för optimal säkerhet.





## 4. Skapa en "Watch-only"-portfölj med Bitcoin



### 4.1. Återställ utökad offentlig nyckel



För att konfigurera en Watch-only wallet måste du först få den utökade publika nyckeln (xpub, ypub, zpub, etc.) för den Wallet som ska övervakas. Denna information finns i allmänhet tillgänglig i inställningarna eller avsnittet "Wallet-information" i din programvara eller Hardware Wallet.





- Exempel med Blockstream App: Från Wallet:s startskärm går du till "Inställningar", sedan "Wallet Detaljer" och kopierar zpub :



![image](assets/fr/09.webp)





- Alternativ 1: generate en QR-kod som innehåller den utökade publika nyckeln för skanning i nästa steg.
- Alternativ 2: Använd en output descriptor om din Wallet erbjuder det.



### 4.2. importera Wallet Endast bevakning





- **Varning**: Sätt upp din portfölj i en privat miljö, utan kameror eller observatörer.
- På startsidan klickar du på "Skapa en ny portfölj" och sedan på "Kom igång":



![image](assets/fr/04.webp)





- Nästa skärm visas:



![image](assets/fr/06.webp)






- (1) **"Setup Mobile Wallet"** : Skapa en ny Hot Wallet. Se handledningen "Blockstream App - Onchain" i appendix.
- (2) **"Återställ från säkerhetskopia"**: Importera en befintlig portfölj med hjälp av en Mnemonic-fras (12 eller 24 ord). Varning för detta: Importera inte frasen från en Cold Wallet, eftersom den kommer att exponeras på en ansluten enhet, vilket ogiltigförklarar dess säkerhet.
- (3) **"Watch-Only"**: det alternativ vi är intresserade av för denna handledning.





- Välj sedan "**Single signature**" och nätverket "**Bitcoin**":



![image](assets/fr/12.webp)





- Klistra in den utökade publika nyckeln (xpub, ypub, zpub, etc.), skanna motsvarande QR-kod eller ange en output descriptor. Även om applikationen anger "xpub", är nycklarna ypub, zpub etc. också auktoriserade. Klicka sedan på "Connect":



![image](assets/fr/13.webp)




### 4.3. Användning av Wallet Watch-only



När Watch-only wallet har importerats visar den det totala saldot och transaktionshistoriken för adresser som härrör från den utökade publika nyckeln. Endast transaktioner i kedjan är synliga (Liquid-transaktioner ignoreras). Om du vill övervaka en Liquid Wallet upprepar du importen genom att välja "Liquid" i föregående steg.





- **Visa saldo och historik**: från startskärmen kan du visa totalt saldo och historik över transaktioner i kedjan:



![image](assets/fr/14.webp)





- **Generera en mottagande Address**: Klicka på "Transact" och sedan på "Receive" för att skapa en ny Address i kedjan. Dela den via QR-kod eller kopia för att ta emot pengar:



![image](assets/fr/15.webp)





- **Skicka pengar**: Klicka på **"Transact"** och sedan på **"Send"**. Du kan ange :
 - Mottagarens Address.
 - Transaktionens belopp.
 - Transaktionsavgifter.



Men eftersom Watch-only wallet inte har de privata nycklarna kan du inte skicka pengar direkt. För att signera transaktionen ansluter du dina Hardware Wallet eller Exchange PSBT:er genom att skanna QR-koderna (ett alternativ som finns tillgängligt på Coldcard Q, till exempel).



![image](assets/fr/16.webp)





- **Obs**: Kontrollera alltid mottagande Address och transaktionsdetaljer för att undvika fel. Pengar som skickas till fel Address kan inte återfås.




## Bilagor



### A1. Andra självstudier för Blockstream App





- Använda Onchain-nätverket :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- Använda Liquid Network :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Skrivbordsversion :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Utökade publika nycklar





- Ordlista :
 - [Utökade publika nycklar] (https://planb.network/fr/resources/glossary/extended-key)
 - [xpub] (https://planb.network/fr/resources/glossary/xpub)
 - [ypub] (https://planb.network/fr/resources/glossary/ypub)
 - [zpub] (https://planb.network/fr/resources/glossary/zpub)
- Kurs :
 - [Les clés publiques étendues](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




### A3. Bästa praxis



Följ dessa rekommendationer för att använda **Blockstream App** på ett säkert och effektivt sätt. De hjälper dig att skydda dina pengar, optimera dina transaktioner och bevara din sekretess i nätverken **Bitcoin (onchain)**, **Liquid** och **Lightning**.





- **Säkra din återställningsfras**:
 - Självstudier: Spara din Mnemonic-fras



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Använd säker autentisering**:
 - Aktivera en **stark PIN-kod** eller **biometrisk autentisering** (fingeravtryck eller ansiktsigenkänning) för att skydda åtkomsten till programmet.
 - Dela aldrig med dig av din PIN-kod eller biometriska data.





- **Skydda din integritet**:
 - generate en ny Address för varje onchain eller Liquid mottagning för att begränsa spårning på Blockchain.
 - Aktivera funktionerna "Enhanced Privacy", "Tor" och "SPV".
 - För maximal sekretess, anslut din Wallet till din egen Bitcoin-nod via en Electrum-server istället för att använda den offentliga noden





- **Välj det nätverk som passar bäst för dina behov**:
- **Onchain**: Företrädesvis för långvarig förvaring eller transaktioner med stora värden (avgifter försumbara i förhållande till beloppet).
- **Liquid**: Används för snabba, billiga överföringar med förbättrad sekretess.
- **Blixten**: Välj omedelbara överföringar till låg kostnad för små belopp.





- **Kontrollera alltid leveransadresser**:
 - Innan du skickar pengar, kontrollera Address noggrant. Pengar som skickas till fel Address är förlorade för alltid. Använd kopiera/klistra in eller QR-kodskanning, kopiera/ändra aldrig en Address för hand.





- **Optimera kostnaderna**:
 - För transaktioner i kedjan ska du välja lämpliga avgifter (långsam, medelhög, snabb) beroende på hur brådskande ärendet är och hur mycket nätverket är överbelastat.
 - Använd Liquid eller Lightning för små mängder.





- Håll ansökan uppdaterad




### A4. Ytterligare resurser





- **Officiella Blockstream-länkar:**
- [Officiell webbplats](https://blockstream.com/)
- [Support för mobilapplikationen](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): dokumentation och chatt
- [GitHub](https://github.com/Blockstream/green_android)





- **Block Explorers:**
 - På kedjan: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Blixtnedslag: **[1ML (Lightning Network)](https://1ml.com/)**





- **Utbildning och handledning:** **[Plan ₿ Network](https://planb.network/)** :
  - Säkra din återställningsfras



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Ordlista](https://planb.network/fr/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**:
- [Ordlista](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb