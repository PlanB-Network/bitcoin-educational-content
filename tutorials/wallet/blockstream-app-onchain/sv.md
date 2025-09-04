---
name: Blockstream-app - Onchain
description: Installera Blockstream App på mobilen och hantera onchain-transaktioner
---
![cover](assets/cover.webp)


## 1. Inledning


### 1.1 Mål för handledning





- Den här handledningen förklarar hur du använder mobilapplikationen **Blockstream App** för att hantera en Bitcoin **onchain** Wallet, dvs. transaktioner som registreras direkt på den huvudsakliga Blockchain Bitcoin.
- Den omfattar installation, inledande konfiguration, skapande av en Software Wallet och åtgärder för att ta emot och skicka bitcoins.
- Obs: Andra handledningar i bilagorna handlar om Liquid, Watch-Only och skrivbordsversionen.



![image](assets/fr/01.webp)



### 1.2 Målgrupp





- Nybörjare**: Användare som vill hantera sina bitcoins med en intuitiv mobilapplikation.
- Användare på mellannivå**: Personer som vill förstå onchain-funktionaliteter och integritetsalternativ som Tor eller SPV.



### 1.3. Påminnelser om Hot plånböcker





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: alla namn på en applikation som installeras på en smartphone, dator eller annan internetansluten enhet och som gör det möjligt att hantera och säkra privata nycklar från en Bitcoin Wallet.
- Till skillnad från **hardware wallets**, även kända som **Cold wallets**, som isolerar nycklar offline, fungerar mjukvaruplånböcker i en uppkopplad miljö, vilket gör dem mer sårbara för cyberattacker.





- Rekommenderad användning** :
    - Idealisk för hantering av måttliga mängder Bitcoin, särskilt för dagliga transaktioner.
    - Lämplig för nybörjare eller användare med begränsade tillgångar, för vilka en Hardware Wallet kan verka överflödig.





- Begränsningar**: Mindre säkert för förvaring av stora belopp eller långsiktiga besparingar. I så fall bör du välja en Hardware Wallet.




## 2. Vi presenterar Blockstream App





- Blockstream App** är en mobil (iOS, Android) och stationär applikation för hantering av Bitcoin-portföljer och tillgångar på Liquid Network. Den förvärvades av [Blockstream] (https://blockstream.com/) 2016 och hette tidigare *Green Address* och sedan *Blockstream Green*.
- Viktiga egenskaper** :
    - Onchain**-transaktioner på Blockchain Bitcoin.
    - Nätverkstransaktioner **Liquid** (Sidechain för snabba, konfidentiella utbyten).
    - Watch-only**-portföljer för övervakning av fonder utan tillgång till nycklar.
    - Sekretessalternativ: anslutning via **Tor**, anslutning till en **personlig nod** via Electrum, eller **SPV**-verifiering för att minska beroendet av tredjepartsnoder.
    - Fungerar **Replace-by-fee (RBF)** för att påskynda obekräftade transaktioner.
- Kompatibilitet**: Integrerar hårdvaruplånböcker som **Blockstream Jade**.
- Interface**: Intuitiv för nybörjare, med avancerade alternativ för experter.
- Obs**: Denna guide fokuserar på användning av onchain. Andra handledningar i bilagorna täcker Liquid, Watch-Only och skrivbordsversionen.



## 3. Installera och konfigurera Blockstream-appen



### 3.1. Ladda ner





- För Android** :
    - Ladda ner [Blockstream App] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) från Google Play Store.
    - Alternativ: Installera via APK-filen som finns på [Blockstreams officiella GitHub] (https://github.com/Blockstream/green_android).
- För iOS** :
    - Ladda ner [Blockstream App] (https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) från App Store.
- Obs**: Var noga med att ladda ner från officiella källor för att undvika bedrägliga applikationer.



### 3.2. Initial konfiguration





- Startskärm**: När programmet öppnas för första gången visas en skärm utan en konfigurerad Wallet. Skapade eller importerade portföljer kommer att visas här senare.



![image](assets/fr/02.webp)





- Anpassa inställningar**: Klicka på "Application settings", justera alternativen nedan, klicka på "Save", starta om applikationen och skapa din portfölj.



![image](assets/fr/03.webp)



#### 3.2.1. Förbättrad sekretess (endast Android)





- Funktion**: Inaktiverar skärmdumpar, döljer förhandsvisningar av program i aktivitetshanteraren och låser åtkomsten när telefonen är låst.
- Varför?** : Skyddar dina data mot obehörig fysisk åtkomst eller skadlig programvara som fångar skärmen.


#### 3.2.2. Anslutning via Tor





- Funktion**: Dirigera nätverkstrafik via **Tor**, ett anonymt nätverk som krypterar dina anslutningar.
- Varför?**: Dölj din IP Address och skydda din integritet, perfekt om du inte litar på ditt nätverk (t.ex. offentligt Wi-Fi).
- Nackdel**: Kan göra programmet långsammare på grund av kryptering.
- Rekommendation**: Aktivera Tor om sekretess är en prioritet, men testa anslutningshastigheten.


#### 3.2.3. Ansluta till en personlig nod





- Funktion**: Ansluter applikationen till din egen **kompletta Bitcoin-nod** via en **Electrum**-server.
- Varför? Ger total kontroll över Blockchain-data, vilket eliminerar beroendet av Blockstream-servrar.
- Förutsättning**: En konfigurerad Bitcoin-nod.
- Rekommendation**: Avancerade användare som vill ha maximal suveränitet.


#### 3.2.4. Verifiering av SPV





- Funktion**: Använder **Simplified Payment Verification (SPV)** för att direkt verifiera vissa Blockchain-data utan att ladda ner hela kedjan.
- Varför?**: Minskar beroendet av Blockstreams standardnod, samtidigt som den är lättviktig för mobila enheter.
- Nackdel**: Mindre säker än en Full node, eftersom den förlitar sig på tredjepartsnoder för viss information.
- Rekommendation**: Aktivera SPV om du inte kan använda en personlig nod, men föredrar en Full node för optimal säkerhet.





## 4. Skapa en Bitcoin onchain-portfölj



### 4.1. Starta skapandet





- Varning**: Sätt upp din portfölj i en privat miljö, utan kameror eller observatörer.
- Klicka på "Kom igång" på startsidan:



![image](assets/fr/04.webp)





- Om du vill hantera en **Cold Wallet** (offline Wallet): klicka på **"Connect Jade"** för att använda Hardware Wallet Blockstream Jade eller andra kompatibla Cold-plånböcker.



![image](assets/fr/05.webp)





- Nästa skärm visas:



![image](assets/fr/06.webp)





- (1) **"Inställning av mobil Wallet"** : Skapa en ny Hot Wallet (Hot Wallet).
- (2) **"Återställ från säkerhetskopia"**: Importera en befintlig portfölj med hjälp av en Mnemonic-fras (12 eller 24 ord). Varning för detta: Importera inte en Cold Wallet-fras, eftersom den kommer att exponeras på en ansluten enhet, vilket ogiltigförklarar dess säkerhet.
- (3) **"Endast bevakning"**: Importera en befintlig skrivskyddad portfölj för att se saldot (t.ex. för din Cold Wallet) utan att exponera Mnemonic-frasen. Se handledningen för Watch Only i appendix.



**I denna handledning**: Klicka på **"Setup Mobile Wallet"** för att skapa en Hot Wallet.


Din Wallet skapas automatiskt och Wallet:s startsida, som här kallas "My Wallet 5", visas:



![image](assets/fr/07.webp)



**Viktigt**: Blockstream App har förenklat skapandet av en Wallet genom att inte automatiskt visa den 12 ord långa seed frasen. *Även om portföljen nu skapas med ett klick riskerar du att förlora tillgången till dina fonder om du inte sparar din seed-fras*.



### 4.2. Spara seed mening





- På startskärmen i Wallet klickar du på fliken "Säkerhet" och sedan på prompten "Säkerhetskopiera" eller menyn "Återställningsfras":



![image](assets/fr/08.webp)



seed:s 12-ordsfras kommer att visas så att du kan spara den.





- Skriv ner din återställningsfras med största försiktighet. Skriv ner den på papper eller metall och förvara den på en säker plats (säker, offline-plats). Denna fras är ditt enda sätt att få tillgång till dina bitcoins om du förlorar din enhet eller raderar applikationen.
- Det är också viktigt att notera att vem som helst med den här frasen kan stjäla alla dina bitcoins. Förvara dem aldrig digitalt:
 - Ingen skärmdump
 - Ingen säkerhetskopiering i molnet, via e-post eller meddelanden
 - Ingen kopiera/klistra in (risk för att spara i urklipp)



**! Denna punkt är kritisk**. För mer information om säkerhetskopiering :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Bekräfta seed mening



Innan du skickar pengar till en Address som är associerad med denna seed-mening måste du testa säkerhetskopian av dina 12 ord.



För att göra detta skriver vi ner en referens, tar bort Wallet, återställer den med säkerhetskopian och kontrollerar att referensen är oförändrad.





- På Wallet:s startskärm klickar du på fliken "Inställningar", sedan på "Wallet Detaljer" och kopierar zPub ([extended public key](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602):



![image](assets/fr/09.webp)



Observera: en zpub Address kan importeras till din Blockstream-applikation för funktionen "Watch Only" (se bilaga).





- Ta bort applikationen och återställ sedan Wallet via **"Återställ från säkerhetskopia"** genom att ange Mnemonic-frasen och kontrollera att zpub är oförändrad. Om ja, då är din säkerhetskopia korrekt och du kan skicka pengar till Wallet.





- Om du vill veta mer om hur du utför ett återställningstest finns här en särskild handledning :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.5. Säkra tillgången till applikationen



Lås åtkomsten till applikationen med en stark PIN-kod:




- Från startskärmen i Wallet, gå till **"Säkerhet"** och klicka sedan på **"PIN"**
- Ange och bekräfta **en slumpmässig 6-siffrig PIN-kod**.



**Biometriskt alternativ**: Tillgängligt för ökad bekvämlighet, men mindre säkert än en robust PIN-kod (risk för obehörig åtkomst, t.ex. fingeravtryck eller ansiktsskanning under sömn).



**Notera**: PIN-koden säkrar enheten, men endast seed-frasen kan användas för att hämta ut pengar.





## 5. Användning av Wallet i kedjan



### 5.1. Ta emot bitcoins





- Från portföljens startsida klickar du på "**Transact**" och sedan på **"Receive"**.



![image](assets/fr/10.webp)





- Programmet visar en **blank mottagning Address** (SegWit v0-format, som börjar med `bc1q...`). Om du använder en ny Address varje gång du tar emot en Bitcoin förbättras din sekretess.





- Tillval** :
    - (1) "Bitcoin": klicka för att välja en onchain- eller Liquid-försändelse och välj tillgången.
    - (2) Klicka på pilarna för att välja en annan ny Address som är kopplad till denna seed-mening.
    - (3) Du kan också välja en Address bland de som redan används/visas genom att klicka på de tre punkterna längst upp till höger och sedan på "List of Addresses"
    - (4) För att begära ett specifikt belopp, klicka på de tre prickarna längst upp till höger, välj "Begär belopp" och ange önskat belopp. QR kommer att uppdateras och Address kommer att ersättas av en Bitcoin betalnings URI.




![image](assets/fr/11.webp)





- Dela Address/URI genom att klicka på "**Share**", kopiera texten eller skanna QR-koden.
- Verifiering**: Kontrollera Address som delas med mottagaren så långt det är möjligt för att undvika fel eller attacker (t.ex. skadlig kod som ändrar urklipp).



### 5.2. skicka bitcoins





- Från portföljens startsida klickar du på "**Transact**" och sedan på **"Send"** :



![image](assets/fr/12.webp)





- Ange detaljer** :
    - (1) Ange mottagarens **Address** genom att klistra på den eller skanna en QR-kod.
    - (2) Kontrollera tillgångarna och det konto från vilket medlen skickas.
    - (3) Ange det **belopp** som ska skickas. Du kan välja enhet: BTC, satoshis, USD, ...


Lägsta belopp (dush limit) den 20.03.2025 är 546 Sats.




    - (4) Välj **transaktionsavgifter** :
        - Välj bland de föreslagna alternativen (t.ex. snabb, medel, långsam) beroende på hur brådskande ärendet är, så visas en ungefärlig överföringstid.
        - För anpassade avgifter justerar du manuellt antalet Satoshi per vbyte (se [Mempool.space](https://Mempool.space/) för marknadspriser).




![image](assets/fr/13.webp)





- Check** :
    - Kontrollera Address, belopp och avgifter på skärmen för sammanfattning.
    - Ett Address-fel kan leda till oåterkallelig förlust av pengar. Akta dig för skadlig kod som ändrar urklipp.



![image](assets/fr/14.webp)





- Bekräftelse**: Tryck på "Skicka"-knappen för att signera och distribuera transaktionen.
- Uppföljning**: På fliken "Transact" i Wallet visas transaktionen som "väntande" tills den bekräftas (1 till 6 bekräftelser):



![image](assets/fr/15.webp)





- Så länge transaktionen inte har bekräftats kan du med hjälp av funktionen "Replace by fee" (se bilaga) påskynda hanteringen genom att höja transaktionsavgifterna:



![image](assets/fr/16.webp)




## Bilagor



### A1. Övriga Blockstream handledningsprogram



Använda Liquid Network



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Importera och spåra en Wallet i "Watch Only"-läge



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Skrivbordsversion



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Förklaring av Replace-by-fee (RBF)



**Definition**: Replace-by-fee (RBF) är en funktion i Bitcoin-nätverket som gör det möjligt för avsändaren att påskynda bekräftelsen av en **onchain**-transaktion genom att gå med på att betala en högre avgift.



**Begränsningar** :




- RBF är inte tillgänglig för Liquid eller Lightning-transaktioner.
- Den första transaktionen måste markeras som RBF-kompatibel när den skapas, vilket Blockstream App gör automatiskt.



**Mer info:**




- [Ordlista] (https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Bästa praxis



Följ dessa rekommendationer för att använda **Blockstream App** på ett säkert och effektivt sätt. De hjälper dig att skydda dina pengar, optimera dina transaktioner och bevara din sekretess i nätverken **Bitcoin (onchain)**, **Liquid** och **Lightning**.





- Säkra din återställningsfras** :
 - Självstudier: Spara din Mnemonic-fras



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Använd säker autentisering** :
 - Aktivera en **stark PIN-kod** eller **biometrisk autentisering** (fingeravtryck eller ansiktsigenkänning) för att skydda åtkomsten till programmet.
 - Dela aldrig med dig av din PIN-kod eller biometriska data.





- Skydda din integritet** :
 - generate en ny Address för varje onchain eller Liquid mottagning för att begränsa spårning på Blockchain.
 - Aktivera funktionerna "Enhanced Privacy", "Tor" och "SPV".
 - För maximal sekretess ska du ansluta din Wallet till din egen Bitcoin-nod via en Electrum-server istället för att använda den publika noden





- Välj det nätverk som passar bäst för dina behov** :
 - Onchain**: Företrädesvis för långvarig förvaring eller transaktioner med stora värden (avgifter försumbara i förhållande till beloppet).
 - Liquid**: Används för snabba, billiga överföringar med ökad sekretess.
 - Blixten**: Välj omedelbara överföringar till låg kostnad för små belopp.





- Kontrollera alltid leveransadresser** :
 - Innan du skickar pengar, kontrollera Address noggrant. Pengar som skickas till fel Address är förlorade för alltid. Använd kopiera/klistra in eller QR-kodskanning, kopiera/ändra aldrig en Address för hand.





- Optimera kostnaderna** :
 - För transaktioner i kedjan ska du välja lämpliga avgifter (långsam, medelhög, snabb) beroende på hur brådskande ärendet är och hur mycket nätverket är överbelastat.
 - Använd Liquid eller Lightning för små mängder.





- Håll ansökan uppdaterad




### A4. Ytterligare resurser





- Officiella länkar:**
 - [Officiell webbplats] (https://blockstream.com/)**
 - [Support för mobilapplikationen](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : dokumentation och chatt
 - [GitHub] (https://github.com/Blockstream/green_android)**





- Block Explorers :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Blixten: **[1ML (Lightning Network)](https://1ml.com/)**





- Utbildning och handledning:** **[Plan ₿ Network](https://planb.network/)** :
 - Säkra din återställningsfras



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Ordlista] (https://planb.network/fr/resources/glossary/liquid-network)**



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Ordlista] (https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb