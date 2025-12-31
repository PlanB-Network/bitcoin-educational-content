---
name: Heritage
description: En Bitcoin-portfölj med integrerad arvsmekanism via Taproot-skript
---

![cover](assets/cover.webp)



Att föra vidare bitcoins i händelse av dödsfall eller oförmåga utgör en stor utmaning för alla innehavare av kryptotillgångar. Utan en lämplig arvsplan blir dessa tillgångar oåterkalleliga för dina nära och kära.



Heritage ger ett elegant svar genom att implementera en dödmansmekanism direkt på Bitcoin-blockkedjan. Denna wallet med öppen källkod gör det möjligt att konfigurera on-chain-successionsvillkor: om ägaren inte gör några ytterligare transaktioner under en definierad period kan förutbestämda alternativa nycklar frigöra pengarna.



## Vad är kulturarv?



Heritage är en Bitcoin-portfölj som naturligt integrerar en arvsmekanism via Taproot-skript. Denna programvara med öppen källkod har utvecklats under MIT-licens av Jérémie Rodon och garanterar transparens och hållbarhet.



Heritage använder Taproot-skript som kodas i Bitcoin-adresser. Varje UTXO integrerar två typer av utgiftsvillkor:





- Primär sökväg** : Ägaren kan spendera sina bitcoins när som helst med sin primära nyckel
- Alternativa vägar**: För varje utsedd arvinge kombinerar ett skript dess publika nyckel med ett tidslås



Varje ägartransaktion skjuter automatiskt upp aktiveringsdatumet för arvsklausulerna. I händelse av långvarig inaktivitet (dödsfall, oförmåga) utlöses villkoren automatiskt.



## Kulturarvstjänst (valfritt)



Heritage erbjuder två användningsalternativ:



**Gör det själv (gratis)**: Enbart applikationen med öppen källkod. Du hanterar allt självständigt med din egen nod. Det här alternativet erbjuder inbyggd backupåtkomst, inbyggt arv och exklusiv kontroll över dina bitcoins. Du måste dock skapa dina egna varningar (kalender, påminnelser) så att du inte glömmer att förnya dina tidslås, och det finns inga automatiska meddelanden till dina arvingar.



** Använd tjänsten (0,05% per år)** : Tjänsten btc-heritage.com lägger till funktioner för att förenkla hanteringen:




- Automatiska påminnelser innan dina tidsfrister löper ut
- Automatiska meddelanden till arvingar för att vägleda dem genom återvinningsprocessen
- Prioriterat stöd
- Förenklad hantering av deskriptorer



Avgift: 0,05% av förvaltat belopp per år, minst 0,5 mBTC/år. Första året gratis.



Tjänsten är inte frihetsberövande: dina privata nycklar lämnar aldrig din enhet. Arvet kan inte komma åt dina pengar.



## Heritage CLI



För avancerade användare som föredrar terminalen erbjuder Heritage ett kommandoradsverktyg (CLI) för detaljerad kontroll och luftgapad maskindrift.



![Page Heritage CLI](assets/fr/03.webp)



Fullständig CLI-dokumentation finns på [btc-heritage.com/heritage-cli] (https://btc-heritage.com/heritage-cli). Här hittar du instruktioner för nedladdning, anslutning till tjänsten, skapande av plånböcker (med Ledger eller lokala nycklar), hantering av arvingar och transaktioner.



Denna handledning fokuserar på Desktop-applikationen, som är mer tillgänglig för de flesta användare.



## Heritage skrivbord



Heritage Desktop är en grafisk applikation med ett intuitivt gränssnitt som guidar användaren genom varje steg i konfigurationsprocessen.



### Nedladdningar



Gå till [btc-heritage.com] (https://btc-heritage.com) och klicka på "Download application".



![Page d'accueil Heritage](assets/fr/01.webp)



Välj den version som motsvarar ditt operativsystem (Linux 64bits eller Windows 64bits). Binaries är inte digitalt signerade, vilket kan leda till säkerhetsvarningar.



![Page de téléchargement](assets/fr/02.webp)



### Installation på Linux



På Linux distribueras programmet i AppImage-format. Innan du kan köra det måste du installera `libfuse2`-beroendet:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Gör sedan filen körbar och kör den:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### Första lanseringen



Vid första lanseringen erbjuder guiden för ombordstigning dig tre val:



![Onboarding initial](assets/fr/05.webp)





- Skapa en Wallet** med kulturarv: Skapa en ny wallet med kulturarvsplan
- Ärva bitcoins**: Återfå bitcoins som en arvinge
- Utforska på egen hand**: Utforska funktioner utan hjälp



Välj "Setup an Heritage Wallet" för att skapa din första wallet.



### Bitcoin nätverksanslutning



Välj hur du vill ansluta till Bitcoin-nätverket:



![Choix connexion](assets/fr/06.webp)





- Använda Heritage Service**: Hanterad infrastruktur, enklare för arvtagare
- Använda min egen nod**: Anslut till din egen Bitcoin Core- eller Electrum-nod



I den här handledningen använder vi vår egen nod.



### Hantering av privat nyckel



Välj hur du vill hantera dina privata nycklar:



![Gestion des clés](assets/fr/07.webp)





- Med en Ledger hårdvaruenhet** : Maximal säkerhet med wallet-hårdvara (rekommenderas)
- Lokal lagring med lösenord**: Lokalt lagrade nycklar med lösenordsskydd
- Återställ en befintlig wallet** : Återställ från en befintlig seed



### Konfiguration av noder



Om du använder din egen nod guidar programmet dig genom konfigurationen. Se till att din Bitcoin- eller Electrum-nod är :




- Installerad och igång
- Synkroniserad med Bitcoin-nätverket
- Konfigurerad för att acceptera RPC-anslutningar (för Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



Klicka på "My Bitcoin node is up and running" när din nod är klar.



### Statuspanel



Klicka på "Status" i det övre högra hörnet och sedan på "Open Configuration" för att komma åt anslutningsparametrarna.



![Panneau Status](assets/fr/09.webp)



Ange webbadressen till din Electrum-server (t.ex. `umbrel.local:50001` om du använder Umbrel).



![Configuration Electrum](assets/fr/10.webp)



### Skapande av wallet



När anslutningen har upprättats klickar du på "Create Wallet" i fliken WALLETS.



![Créer wallet](assets/fr/11.webp)



En popup-fönster förklarar den delade arkitekturen i Heritage :



![Architecture split](assets/fr/12.webp)



1. **Nyckelleverantör (offline)**: Hanterar dina privata nycklar och signerar transaktioner. Kan vara en Ledger eller en wallet programvara.


2. **Online Wallet**: Hanterar synkronisering med Bitcoin-nätverket, skapande av adresser och sändning av transaktioner.



Fyll i formuläret för skapande :



![Formulaire création wallet](assets/fr/13.webp)





- Wallet Namn**: Ett unikt namn för att identifiera din wallet
- Leverantör av nycklar**: Välj Local Key Storage för denna handledning
- Ny/återställa**: Välj "New" för att generate en ny seed
- Antal ord**: 24 ord rekommenderas för maximal säkerhet



Ange ett starkt lösenord och välj alternativ för Online Wallet :



![Options Online Wallet](assets/fr/14.webp)





- Lokal nod**: Använder din egen Electrum eller Bitcoin Core-nod
- Heritage-tjänst**: Använder Heritage-tjänsten (rekommenderas för anmälningsfunktioner)



Klicka på "Create Wallet" för att slutföra skapandet.



### Interface från wallet



Din wallet är nu skapad. Gränssnittet visar :



![Interface wallet](assets/fr/15.webp)





- Balans
- Knapparna SEND och RECEIVE
- Transaktionshistorik
- Historia om konfiguration av arv
- wallet adresser



### Skapa arvingar



Gå till fliken "ARVTAGARE" för att skapa dina arvingar.



![Page Heirs](assets/fr/16.webp)



Popup-fönstret med information förklarar:




- Arvingar är Bitcoin publika nycklar som är associerade med individer
- Varje arvinge har sin egen minnesfras
- Den första arvtagaren bör vara en "Backup" för dig själv (i händelse av förlust av din huvudsakliga wallet)



#### Skapande av backup-arvtagare



Klicka på "Create Heir" och döp den till "Backup".



![Création héritier Backup](assets/fr/17.webp)



I popup-fönstret förklaras varför en mening på 12 ord utan passphrase är säker för arvingarna:


1. **Ingen omedelbar tillgång**: Arvtagarnycklar kan inte få tillgång till medel förrän tidslåset har löpt ut


2. **Kompromissdetektering**: Om någon får tillgång till frasen kan du uppdatera Heritage-konfigurationen


3. **Långsiktig tillgänglighet**: En passphrase kan glömmas bort efter många år



Konfigurera arvtagaren :



![Configuration héritier](assets/fr/18.webp)





- Nyckelleverantör** : Lokal lagring av nycklar
- Ny**: Generera en ny seed
- Antal ord**: 12 ord



Slutför skapandet :



![Finalisation héritier](assets/fr/19.webp)





- Typ av arv**: Utökad offentlig nyckel
- Exportera till tjänst**: Valfritt, möjliggör automatisk avisering av arvingar



Backup-arvtagaren är nu skapad:



![Héritier créé](assets/fr/20.webp)



#### Spara arvtagarens minnesfras



Klicka på Backup-hjälten och sedan på "Show Mnemonic" :



![Afficher mnemonic](assets/fr/21.webp)



**VIKTIGT: Notera dessa 12 ord och förvara dem på ett säkert ställe. Detta är nyckeln till att återfå pengarna.



![Phrase mnémotechnique](assets/fr/22.webp)



#### Avlägsnande av seed från ansökan



När du har skrivit ner frasen går du till arvsparametrarna (kugghjulsikonen):



![Paramètres héritier](assets/fr/23.webp)



Använd "Strip Heir Seed" för att ta bort den privata nyckeln från programmet. Bekräfta att du har sparat frasen.



![Strip Heir Seed](assets/fr/24.webp)



Detta är en säkerhetsåtgärd: endast den publika nyckeln finns kvar i programmet, vilket är tillräckligt för att konfigurera arv.



#### Skapande av en andra arvinge



Upprepa processen för att skapa en andra arvinge (t.ex. "Satoshi"). Du kommer nu att ha två arvingar:



![Deux héritiers](assets/fr/25.webp)





- Säkerhetskopia**: Din personliga nyckel för nödsituationer
- Satoshi**: En utpekad arvtagare



### Konfiguration av kulturarv



Gå tillbaka till din wallet och klicka på ikonen Inställningar:



![Paramètres wallet](assets/fr/26.webp)



I avsnittet "Heritage Configuration" klickar du på "Create":



![Heritage Configuration](assets/fr/27.webp)



Sätt tidsgränser för varje arvtagare:



![Configuration délais](assets/fr/28.webp)





- Säkerhetskopia**: 180 dagar (6 månader) - Förfallodag: 2026-06-18
- Satoshi**: 455 dagar (15 månader) - Förfallodag: 2027-03-20



**Viktigt**: Varje arvinge måste ha en längre fördröjning än den föregående. Den första arvtagaren (Backup) kommer att få tillgång till pengarna först.



Konfigurera också :



![Configuration finale](assets/fr/29.webp)





- Referensdatum**: Startdatum för beräkning av ledtider
- Minsta förfallodag**: Minsta fördröjning efter en transaktion (10 dagar rekommenderas)



Klicka på "Create" för att validera konfigurationen.



Heritage-konfigurationen är nu aktiv:



![Configuration active](assets/fr/30.webp)



Den visar båda arvingarna med deras respektive tidsfrister och utgångsdatum.



### Spara deskriptorer



**Viktigt**: Spara dina wallet-beskrivningar. Utan dem, även med den mnemoniska frasen, är det omöjligt att återfå fonden.



Klicka på "Backup Descriptors":



![Bouton Backup](assets/fr/31.webp)



Spara JSON-filen som innehåller dina Bitcoin-descriptors:



![Backup descripteurs](assets/fr/32.webp)



Denna fil bör överlämnas till dina arvingar, tillsammans med deras respektive minnesfraser.



### Ta emot bitcoins



Klicka på "RECEIVE" för att generate en mottagningsadress:



![Recevoir bitcoins](assets/fr/33.webp)



Gratulerar till din Heritage Wallet! Din Heritage Wallet är redo att ta emot bitcoins. Varje genererad adress införlivar automatiskt dina Heritage-villkor.



När du har tagit emot en transaktion uppdateras ditt saldo:



![Solde mis à jour](assets/fr/34.webp)



I historiken visas transaktionen och den tillhörande Heritage-konfigurationen.



---

## Återvinning av en arvinge



När den fastställda tiden har löpt ut kan arvtagaren återkräva medlen.



### Förkunskapskrav



Arvtagaren behöver :


1. Hans 12 ord långa minnesfras


2. Den ursprungliga backup-filen för wallet-descriptor (JSON)



### Skapa en arvtagare Wallet



På fliken "INHERITANCES" påminner en popup dig om dessa förutsättningar:



![Page Heir Wallets](assets/fr/35.webp)



**Vänligen notera**: Utan backup-filen med deskriptorn är det OMÖJLIGT att få tillgång till fonderna, även med rätt minnesfras.



Klicka på "Skapa arvtagare Wallet":



![Créer Heir Wallet](assets/fr/36.webp)



Vänligen fyll i formuläret:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Arvtagare Wallet Namn**: Ett namn för att identifiera denna arvtagare wallet
- Nyckelleverantör** : Lokal lagring av nycklar
- Återställ**: Välj detta alternativ för att ange en befintlig fras



Ange de 12 orden i arvingens mnemoniska fras och konfigurera Heritage Provider:



![Entrée mnemonic](assets/fr/38.webp)





- Leverantör av arv**: "Local" för att använda din egen nod med backup-filen



Ladda JSON-backupfilen och klicka på "Skapa arvtagare Wallet" :



![Chargement backup](assets/fr/39.webp)



### Interface Arvtagare Wallet



Arvtagaren Wallet skapas. Initialt, om tidslåset ännu inte har löpt ut, är inget arv tillgängligt:



![Pas d'héritage disponible](assets/fr/40.webp)



När fördröjningen har löpt ut och medlen har synkroniserats med Bitcoin-nätverket visas de i listan över arv:



![Héritage disponible](assets/fr/41.webp)



Gränssnittet visar :




- Typ av nyckel och fingeravtryck
- Summa ärvda medel
- Aktuellt disponibelt belopp (0 sat om tidslåset ännu inte har löpt ut)
- Förfallo- och utgångsdatum



När förfallodagen har uppnåtts överför "Spend"-knappen bitcoins till en personlig wallet.



---

## Bästa praxis



### Spara deskriptorer



wallet descriptors är avgörande för att rekonstruera dina Heritage-adresser. **Utan deskriptorerna, även med din minnesfras, kommer du inte att kunna hitta dina fonder.



### Säkerhet för nycklar





- Använd en Ledger för huvudnyckeln om möjligt
- Förvara aldrig arvingars domar på samma ställe som dina egna
- Sprida information i flera medier och på flera platser



### Dokumentation för dina anhöriga



Skriv tydliga instruktioner som förklarar varje steg i återvinningsprocessen. Dina arvingar kanske inte känner till Bitcoin i det kritiska ögonblicket.



## Alternativa lösningar



Det finns andra lösningar för att hantera överföringen av dina bitcoins, inklusive Liana och Bitcoin Keeper. Du hittar våra handledningar nedan:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Slutsats



Heritage gör att du kan planera din Bitcoin-succession på ett suveränt sätt via Desktop-applikationen. Genomförandet kräver att man noga överväger lämpliga tidsramar och skyddar hemligheter. Glöm inte att föra vidare till dina arvingar:




- Deras 12 ord långa minnesfras
- Backup-filen för deskriptorn
- Instruktioner för återställning



## Resurser





- [Heritage officiella webbplats](https://btc-heritage.com)
- [Dokumentation CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)