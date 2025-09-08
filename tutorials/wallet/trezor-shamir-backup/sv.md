---
name: Trezor Shamir Backup
description: Mnemonic-fraser med en eller flera aktier på Trezor
---
![cover](assets/cover.webp)



*Bildkredit: [Trezor.io] (https://trezor.io/)*



## Nya alternativ för säkerhetskopiering på Trezor



Sedan 2023 har Trezor erbjudit ett nytt backupformat som heter ***Single-share Backup***, som gradvis ersätter det klassiska BIP39-baserade tillvägagångssättet som finns på de flesta plånböcker. Till skillnad från traditionella Mnemonic-fraser på 12 eller 24 ord baseras detta nya format på en enda fras på 20 ord som härrör från en standard som utvecklats av SatoshiLabs: **SLIP39**. Syftet är att förbättra backupens robusthet och läsbarhet, samtidigt som det möjliggör en smidig övergång till en distribuerad backupmodell.



Denna distribuerade modell kallas ***Multi-share Backup***. Den bygger på samma princip, men istället för att generera en enda Mnemonic-fras delar den upp den i flera fragment som kallas ***shares***, som var och en är en Mnemonic-fras i sig själv. För att återställa Wallet måste ett visst antal av dessa *delar* (definierat av ett *tröskelvärde*) återförenas. Till exempel, i ett 3-av-5-system, kommer alla 3 *andelar* av de 5 att återställa Wallet. Observera att Trezors distribuerade backup-system skiljer sig från Multisig-plånböcker. För att spendera dina bitcoins krävs endast din Hardware Wallet Trezor. Endast en signatur krävs. Distribution gäller endast på nivån för Mnemonic-fras, dvs. säkerhetskopian.



![Image](assets/fr/01.webp)



Detta system löser problemet med Mnemonic-frasens "single point of failure" utan de nackdelar som är förknippade med att hantera en Multisig eller passphrase BIP39. Återställningsprocessen baseras inte längre på en enda information, utan på flera, med den extra fördelen av förlusttolerans tack vare tröskelvärdet.



Användare som har skapat en Wallet med *Single-share Backup* kan när som helst byta till *Multi-share Backup* utan att behöva migrera sin Wallet. Mottagningsadresser och konton kommer att förbli identiska. Systemet *Multi-share* påverkar endast säkerhetskopian, medan resten av Wallet förblir oförändrad.



Multi-share Backup* är tillgängligt på Trezor Model T, Safe 3 och Safe 5. Denna funktion stöds inte av Trezor Model One.



**Viktigt att notera:** Trezors *Multi-share*-system är kryptografiskt säkert, eftersom det använder *Shamirs Secret Sharing*-schema för distribution. Vi avråder starkt från att tillämpa ett liknande system manuellt genom att dela en klassisk Mnemonic-fras själv. Det är en dålig praxis som avsevärt ökar risken för stöld och förlust av dina bitcoins, så gör det inte. En klassisk Mnemonic-fras lagras i sin helhet.



## Shamirs hemliga delning i SLIP39



Den kryptografiska mekanism som ligger till grund för *Multi-share* säkerhetskopiering på Trezor är *Shamir's Secret Sharing Scheme* (SSSS). Principen är följande: hemlig information (i det här fallet seed i Wallet) omvandlas till ett matematiskt polynom. Flera punkter i detta polynom beräknas sedan, var och en av dem blir en andel. Den ursprungliga hemligheten rekonstrueras genom polynominterpolation, genom att samla ett minsta antal punkter (tröskelvärdet).



Ingen hemlig information kan härledas från ett antal aktier under tröskelvärdet, vilket garanterar perfekt teoretisk säkerhet för den hemliga informationen. Med andra ord kan inte ens en angripare med obegränsad datorkraft gissa sig till seed om tröskelvärdet inte nås.



SLIP39 använder detta schema för att distribuera seed Wallet. Varje delning är en mening på 20 ord, byggd från en lista med 1024 ord (skiljer sig från BIP39-listan).



## Konfigurera en Multi-share Backup på en Trezor



När du skapar din Wallet på Trezor har du tre olika alternativ:




- Använd en klassisk BIP39 Mnemonic-fras med 12 eller 24 ord;
- Använd en Mnemonic-fras som delas med en person (SLIP39);
- Konfigurera flera Mnemonic-fraser i Multi-share (SLIP39).



Om du väljer en Single-share SLIP39 Mnemonic-fras kan du uppgradera till en Multi-share vid ett senare tillfälle utan att behöva återställa Wallet. Om du däremot börjar med en klassisk BIP39 Wallet (fras med 12 eller 24 ord) kan du inte konvertera den direkt till en Multi-share. Du måste skapa en ny Multi-share Wallet från grunden och överföra dina medel från den gamla Wallet till den nya via en eller flera Bitcoin-transaktioner. Detta är en mer komplex och kostsam operation. Om du vill göra denna migrering rekommenderar jag att du köper en ny Hardware Wallet Trezor för att undvika att behöva ange din seed på en Wallet-programvara.



I den här handledningen tittar vi först på hur man ställer in en Multi-share när man skapar en Wallet, och sedan, i ett efterföljande avsnitt, ser vi hur man konverterar en Single-share till en Multi-share på en befintlig Wallet.



Om du behöver hjälp med den första installationen av din enhet har vi också en detaljerad handledning för varje Trezor-modell:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### På en ny Wallet



Du har nu slutfört den inledande konfigurationen av din Trezor och är redo att skapa Wallet. I Trezor Suite klickar du på knappen "*Skapa ny Wallet*".



![Image](assets/fr/02.webp)



Välj alternativet "*Multi-share Backup*" och klicka sedan på "*Create Wallet*".



![Image](assets/fr/03.webp)



Acceptera användarvillkoren på din Trezor och bekräfta skapandet av Wallet.



![Image](assets/fr/04.webp)



I Trezor Suite klickar du på "*Fortsätt att säkerhetskopiera*".



![Image](assets/fr/05.webp)



Läs instruktionerna noggrant, bekräfta dem och klicka sedan på "*Create Wallet backup*".



![Image](assets/fr/06.webp)



För mer information om hur du sparar och hanterar dina Mnemonic-fraser rekommenderar jag starkt att du följer den här andra handledningen, särskilt om du är nybörjare:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

På Trezor väljer du det totala antalet aktier som du vill konfigurera. De vanligaste konfigurationerna är 2-de-3 och 3-de-5. I det här exemplet skapar jag en 2-de-3, så jag väljer 3 andelar. Varje andel kommer att representera en Mnemonic-fras på 20 ord.



*För Safe 5-användare, även om det står "*Tryck för att fortsätta*" på skärmen, måste du faktiskt svepa upp för att bekräfta



![Image](assets/fr/07.webp)



Bekräfta sedan tröskelvärdet, dvs. det antal aktier som krävs för att återfå tillgång till Wallet och de bitcoins som den innehåller.



![Image](assets/fr/08.webp)



Trezor kommer att skapa dina olika shares (Mnemonic-fraser) med hjälp av sin slumptalsgenerator. Se till att du inte blir iakttagen under denna operation. Skriv ner de ord som visas på skärmen på det fysiska medium som du väljer. Det är viktigt att hålla orden numrerade och i sekventiell ordning.



Jag rekommenderar att du antecknar varje del på ett separat medium och noggrant hanterar förvaringen av dem för att undvika att flera är tillgängliga på samma plats. För en 2-av-3-konfiguration som min skulle ett alternativ till exempel vara att förvara en andel hemma hos mig, en annan hos en betrodd vän och den sista i ett bankfack. Valet av förvaringsplats beror på din personliga säkerhetsstrategi.



Du kan se längst upp på skärmen vilken aktie du för närvarande tittar på.



naturligtvis får du aldrig dela dessa ord på Internet, som jag gör i den här handledningen. Detta exempel Wallet kommer endast att användas på Testnet och kommer att raderas i slutet av handledningen.**_



![Image](assets/fr/09.webp)



För att gå vidare till nästa ord klickar du längst ner på skärmen. Du kan gå bakåt genom att glida nedåt. När du har skrivit ner alla ord håller du fingret på skärmen för att gå vidare till nästa del och upprepar proceduren.



![Image](assets/fr/10.webp)



I slutet av varje share-inspelning ombeds du att markera orden i din Mnemonic-fras för att bekräfta att du har skrivit ner dem korrekt.



![Image](assets/fr/11.webp)



Nu har du gjort en lyckad säkerhetskopiering av din Wallet med hjälp av alternativet Multi-share. Du kan nu fortsätta med resten av konfigurationsinstruktionerna.



### På en befintlig Wallet med en enda andel



Om du redan har en Trezor Wallet med en single-share backup (en SLIP39 Mnemonic fras, inte den klassiska BIP39 frasen), och vill förbättra tillgängligheten och säkerheten för din Wallet backup, kan du sätta upp ett multi-share system utan att behöva överföra dina bitcoins.



För att göra detta, anslut och lås upp din Hardware Wallet. I Trezor Suite går du till Inställningar.



![Image](assets/fr/12.webp)



Gå till fliken "*Device*".



![Image](assets/fr/13.webp)



Klicka sedan på "* Skapa säkerhetskopiering med flera delningar *".



![Image](assets/fr/14.webp)



Läs instruktionerna och klicka sedan på "*Create Multi-share Backup*".



![Image](assets/fr/15.webp)



Du måste sedan ange din nuvarande Mnemonic-fras (single-share) på Trezor-skärmen. Välj antal ord (standard är 20).



![Image](assets/fr/16.webp)



Använd sedan Trezors tangentbord på skärmen för att skriva in varje ord i din aktuella Mnemonic-fras.



![Image](assets/fr/17.webp)



Du kan sedan välja konfiguration för din Multi-share Backup genom att följa instruktionerna i föregående avsnitt.



![Image](assets/fr/18.webp)



När du har skapat din Multi-share Backup måste du bestämma vad du ska göra med din ursprungliga Single-share Mnemonic-fras. Eftersom Bitcoin Wallet förblir densamma kommer denna enda fras alltid att ge åtkomst till den. Detta beror på din säkerhetsstrategi, men i allmänhet är det tillrådligt att förstöra denna fras för att eliminera denna enda punkt av fel, vilket är just syftet med Multi-share Backup. Om du bestämmer dig för att förstöra den, se till att du gör det på ett säkert sätt, eftersom ** det fortfarande ger tillgång till dina bitcoins **.



Grattis, du är nu uppdaterad om användningen av Single-share och Multi-share säkerhetskopior på Trezor hårdvaruplånböcker. Om du vill ta din Wallet-säkerhet ett steg längre, ta en titt på denna handledning om BIP39-lösenordsfraser:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Om du tyckte att den här handledningen var användbar skulle jag vara tacksam om du lämnar en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!



## Ytterligare resurser





- [SLIP-0039: Shamirs hemliga delning för Mnemonic-koder] (https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Multi-share Backup på Trezor] (https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Shamirs hemliga delning] (https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).