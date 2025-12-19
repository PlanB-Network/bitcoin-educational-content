---
name: COLDCARD Q - Key Teleport
description: Vad är Key Teleport och hur använder jag det?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Vad är **Key Teleport**-funktionen som Coinkite erbjuder med sin flaggskeppsenhet ColdCardQ?



*Med **Key Teleport** kan du på ett säkert sätt överföra konfidentiella data mellan 2 ColdCardQ. Överföringskanalen behöver inte ens vara krypterad, utan kan vara offentlig.*



Detta kan användas för att överföra:





- **gW-0-fraser** (ColdCard Q:s seed-mästare eller de hemligheter som finns lagrade i ColdCardQ:s [seed Vault](https://coldcard.com/docs/temporary-seeds/#seed-vault).
- **konfidentiella anteckningar och lösenord**: detta kan vara vilken hemlighet som helst eller hela katalogen [Secure Notes & Passwords] (https://coldcard.com/docs/secure_notes/) på din ColdCardQ.
- en säkerhetskopia av hela din **ColdCardQ**: den ColdCardQ som tar emot denna säkerhetskopia får inte ha en seed Master för att detta ska fungera.
- gW-3 (**Partiellt signerade Bitcoin-transaktioner**) som en del av ett system med flera signaturer.



Detta kräver att du har uppgraderat din [enhetens firmware till version v1.3.2Q] (https://coldcard.com/docs/upgrade/) eller högre.



## Hur använder jag Key Teleport?



### 1- För att överföra alla typer av data



Här tittar vi på överföringen av seed-meningar, anteckningar, lösenord eller en hel överföring av en ColdCardQ-backup. PSBT-överföringar för transaktioner med flera signaturer kommer att behandlas senare.



#### Förbered enheten för att ta emot hemligheterna



I menyn **"Advanced / Tools**" på ditt ColdCardQ väljer du **"Key Teleport (start)"**.


På nästa skärm föreslås ett 8-siffrigt lösenord, här "20420219". Du måste kommunicera detta lösenord till avsändaren. Använd till exempel sms för att skicka lösenordet, eller ditt säkra meddelandesystem, eller till och med ett röstsamtal.



Klicka sedan på **"Enter**"-knappen på din ColdCardQ för att gå vidare till nästa steg.




![CCQ-key-teleport](assets/fr/01.webp)




En QR-kod genereras på skärmen. Återigen måste du kommunicera denna QR-kod till ColdCardQ-"avsändaren". Det enklaste sättet att göra detta är via ett videosamtal.



**SÄND INTE DENNA QR-KOD VIA SAMMA ÖVERFÖRINGSKANAL SOM ANVÄNDES FÖR ATT SKICKA DET TIDIGARE 8-SIFFRIGA LÖSENORDET**.



![CCQ-key-teleport](assets/fr/02.webp)



*För er som är intresserade, låt oss försöka förstå den underliggande mekanismen som gör det möjligt att överföra hemligheter via osäkra kanaler*



*Vad vi faktiskt gör här är att initiera en överföring av hemligheter via Diffie-Hellman-metoden, som behandlas i BTC204-kursen som jag har inkluderat nedan *



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*Vi har för närvarande:*




- genererade ett efemärt nyckelpar (offentligt/privat respektive Ka och ka med Ka=G.ka, G är ECDH-generatorpunkten) och ett 8-siffrigt lösenord.
- använder detta lösenord för att kryptera den offentliga nyckeln (Ka) med AES-256-CTR och överför sedan detta lösenord via en kommunikationskanal A till den "sändande" ColdCardQ.
- slutligen sände vi det krypterade paketet till avsändaren via QR-koden ovan, med hjälp av en andra kommunikationskanal B som skiljer sig från den första.



#### Förbered den enhet som ska skicka hemligheterna



Från den sändande enheten klickar du på knappen **"QR"** för att skanna QR-koden som skickats till dig av den mottagande enheten och anger sedan det 8-siffriga lösenordet som du fick i föregående steg via en separat kanal. Vi är nu redo att börja skicka data från den "sändande" enheten.



**Var vänlig ange inte det 8-siffriga lösenordet felaktigt, eftersom inget felmeddelande kommer att visas och processen kommer att fortsätta. Den slutliga dataöverföringen kommer dock att misslyckas och du måste börja om**.



![CCQ-key-teleport](assets/fr/03.webp)



*För de mer nyfikna bland er, låt oss ta en ny titt på vad vi håller på med när det gäller kryptografi och hemlig överföring:*




- vi importerade de krypterade uppgifterna genom att skanna QR-koden på den mottagande enheten.
- sedan dekrypterade vi dem med hjälp av det 8-siffriga lösenord som skickats till oss via en sekundär kanal.
- vi har därför tillgång till den publika nyckeln (Ka) som genererats av mottagaren från början
- Vi skapar sedan generate ett nytt efemärt nyckelpar (Kb/kb, med Kb=G.kb) på den sändande enheten, som vi använder för att tillämpa ECDH på Ka. Vi utför därför operationen kb.Ka=Ks , där Ks kallas **"Sessionsnyckel"**.




Du ombeds nu att välja vilken typ av hemligheter som ska överföras mellan de 2 ColdCardQs (konfidentiella anteckningar, lösenord, fullständig säkerhetskopia, frön i ditt valv, seed device master).



![CCQ-key-teleport](assets/fr/04.webp)



Här kommer vår hemlighet att vara ett kort meddelande genom att välja **"Quick Text Message"**. Skriv ditt meddelande (för oss "Plan ₿ Academy rocks") och tryck sedan på **"ENTER"**.


Enheten genererar sedan ett nytt slumpmässigt lösenord som kallas **"Teleport Password"** , i exemplet "NE XG BT SK".



![CCQ-key-teleport](assets/fr/05.webp)



Tryck på **"ENTER"** så får du en ny QR-kod. Låt den skannas av den mottagande enheten. Och på en annan kommunikationskanal sänder du **"Teleport Password"** till mottagaren.



![CCQ-key-teleport](assets/fr/06.webp)



*Här igen, för den nyfikne, under detta skede:*




- efter att ha valt de hemligheter som ska överföras, vi generate ett nytt slumpmässigt lösenord som heter **"Teleport Password"**.
- vi krypterar sedan hemligheterna med AES-256-CTR med hjälp av **"Session Key"**, "Ks", som genererades i föregående steg.
- vi prefixar paketet som redan är krypterat med **"Session Key"** med vår Kb-offentliga nyckel, och lägger sedan till ytterligare en Layer av AES-256-CTR-kryptering med **"Teleport Password"**. Hela saken kodas sedan som en QR-kod




#### Slutför överföringen av hemligheter till den mottagande enheten



Tryck på **"QR"**-knappen för att skanna QR-koden som presenteras av den sändande enheten via visio-kanalen. Du kommer att bli ombedd att ange ditt **"Teleport Password"** för oss "NE XG BT SK".



![CCQ-key-teleport](assets/fr/07.webp)





Uppgifterna dekrypteras sedan och görs begripliga för den mottagande enheten. Det mottagna meddelandet är verkligen "Plan ₿ Academy rocks". Det är allt.



![CCQ-key-teleport](assets/fr/08.webp)



*Vad hände egentligen under denna sista etapp :*?




- vi har dekrypterat de data som sänds av avsändaren med hjälp av **"Teleport Password"**.
- har vi alltså den publika nyckeln Kb och vårt hemliga meddelande krypterat med **"Session Key"**, "Ks". Men hur kan vi göra detta eftersom vi som mottagare inte känner till Ks, som skapades av avsändaren?
- Vi måste använda vår privata nyckel "ka" från det första steget **"Förbered den enhet som ska ta emot data"** till den offentliga nyckeln *Kb*.
- Faktum är att genom att beräkna ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks, hittar vi Ks. Som slutligen används för att dechiffrera det hemliga meddelandet.



### 2- För att överföra PSBT till Multisig (avancerad)



Detta förutsätter att din Wallet Multisig redan har skapats och att din ColdCardQ-enhet redan har förinställts för att kunna utföra transaktioner med flera signaturer. Om så inte är fallet finns förklaringar tillgängliga [här](https://coldcard.com/docs/Multisig/) på Coinkites webbplats.



En snabb påminnelse om vad en Wallet (Multisig) med flera signaturer är.



För att spendera dina Wallet-medel behövs vanligtvis bara en privat nyckel för att låsa upp UTXO:erna som är kopplade till dina adresser.


I fallet med en Wallet Multisig kan upp till 15 privata nycklar och därmed 15 signaturer behövas för att spendera medlen. Detta är känt som en "M av N"-portfölj, där N är mellan 1 och 15 och M är antalet signaturer som krävs för att medlen ska kunna spenderas. Till exempel kommer en Wallet Multisig 3 av 5 att kräva minst 3 signaturer av 5 möjliga.



Utmaningen är sedan att samordna mellan undertecknare för att underteckna en "PSBT" för "Partially Signed Bitcoin Transaction" i sin tur. I detta sammanhang kan "**Key Teleport**" användas för att överföra PSBT mellan medundertecknare på ett enkelt och konfidentiellt sätt. Ett enkelt videosamtal mellan medundertecknare gör susen.



Så här går det till på en Multisig 3 av 4.



**Undertecknande 1:**



Signatär 1 importerar och signerar PSBT. Slutligen klickar han på **"T"** för att använda **"Key Teleport"** för att överföra PSBT till undertecknare 2.



![CCQ-key-teleport](assets/fr/09.webp)




Efter att ha valt undertecknare 2 genom att klicka på **"ENTER"**, tillhandahålls ett "TELEPORT PASSWORD" (här JJ YC AB 6A), som måste överföras till undertecknare 2 via en annan kommunikationskanal. Till exempel ett SMS eller ett röstsamtal, men **inte** ett videosamtal.



Tryck på **"ENTER"** igen och en QR-kod som representerar PSBT signerad av 1 och sedan krypterad med "TELEPORT PASSWORD" visas.



![CCQ-key-teleport](assets/fr/10.webp)



**Underskrift 2:**



Undertecknare 2 skannar den QR-kod som han fått av undertecknare 1. Därefter anger han "TELEPORT PASSWORD" som överförs via den sekundära kommunikationskanalen för att dekryptera de överförda uppgifterna.



Signatär 2 undertecknar transaktionen och klickar sedan på **"T"** för att sända PSBT till signatär 3 via "Key Teleport".


Det är uppenbart att 2 signaturer redan har använts. Allt som saknas är underskrift av undertecknare 3 för att transaktionen ska vara giltig. Välj undertecknare 3 genom att klicka på **"ENTER"**.



![CCQ-key-teleport](assets/fr/11.webp)



Och ett nytt "TELEPORT-lösenord" skapas, följt av en QR-kod som kodar PSBT signerad av 1 och 2 och sedan krypterad med detta nya "TELEPORT-lösenord" (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**Signatur 3:**



Upprepa samma steg som ovan.


Undertecknare 3 skannar den QR-kod som han fått av undertecknare 2. Därefter anger han "TELEPORT PASSWORD" som sänds via den sekundära kommunikationskanalen.



Signatär 3 signerar transaktionen och den här gången, eftersom 3 av 4 signaturer har använts, anges transaktionen som slutförd och är klar för distribution via olika medier (SD-kort, NFC, QR etc.).



![CCQ-key-teleport](assets/fr/13.webp)



Om ColdCardQ:s "Push Tx"-funktion är aktiverad är det bara att fästa ColdCardQ på baksidan av en NFC-aktiverad internetansluten enhet (smartphone/surfplatta) för att sända transaktionen via Bitcoin-nätverket.



![CCQ-key-teleport](assets/fr/14.webp)



*För PSBT-överföringar från en undertecknare till en annan används "Key Teleport" helt enkelt via ett "Teleport Password" i varje steg, vilket krypterar PSBT när det överförs från en undertecknare till en annan. Eftersom de överförda uppgifterna inte kan användas för att stjäla pengar behövs ingen Diffie-Hellman, vilket är fallet när man skickar mycket konfidentiella hemligheter (seed, lösenord etc...)*.



![CCQ-key-teleport](assets/fr/15.webp)



*Källa: [ColdCards officiella webbplats [ColdCards officiella webbplats] (https://coldcard.com/)*