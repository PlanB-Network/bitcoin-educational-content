---
name: BIP-85
description: Hur kan jag använda BIP-85 för att generate flera seedphrases från en huvud seed?
---
![cover](assets/cover.webp)



## 1. Förståelse av BIP-85



### 1.1 Vad är BIP-85?



BIP-85 är en avancerad funktion som gör att du kan skapa flera **seed sekundära fraser** från en **seed huvudfras**.



Varje seed sekundär mening kan användas för att skapa en helt oberoende Bitcoin-portfölj. Dessa portföljer kan användas för en mängd olika ändamål: en Hot Wallet på mobilen, en portfölj för en släkting, en separat sparportfölj etc.



Alla seed underfraser är **matematiskt härledda**, men det är **omöjligt att spåra tillbaka till seed huvudfrasen** från en underfras. Detta säkerställer fullständig separation mellan varje portfölj.



Så länge du har tillgång till din seed-huvudfras (och den tillhörande passphrase om du använder en sådan) kan du regenerera alla seed-sekundärfraser **identiskt** utan att behöva spara dem separat.



### 1.2 Varför använda BIP-85?



BIP-85 är användbart om du vill :





- Skapa flera oberoende Bitcoin-portföljer utan flera säkerhetskopior
- Hantera dina medel enligt olika användningsområden (besparingar, utgifter, familj, projekt)
- Garantera skyddsåtgärder för släktingar ("Uncle Jim"-funktionen)
- Ta bort en portfölj utan att förlora tillgången till dina fonder
- Förenkla din säkerhet: bara en seed-nyckelfras att skydda



### 1.3 Fördelar jämfört med BIP-32



Med BIP-32 kan en enda seed-mening användas för att generate en komplett hierarki av Bitcoin-konton och adresser, med hjälp av avledningsvägar (till exempel: `m/44'/0'/0'/0/0`). Varje sökväg kan representera ett separat konto, men **alla förblir länkade till samma seed mening**. Så om denna seed-fras äventyras blir **alla härledda konton tillgängliga**.



Med BIP-85 kan en seed huvudmening användas för att generate flera helt oberoende seed sekundärmeningar: **Om en av dessa sekundära meningar äventyras kommer angriparen aldrig att kunna gå tillbaka till den huvudsakliga seed eller få tillgång till de andra portföljerna**.


Detta gör det möjligt att dela upp riskerna i olika fack:





- Du kan använda en sekundär seed för Hot Wallet eller tillfällig användning och acceptera en högre exponering.
- Även om denna Hot Wallet äventyras är dina andra medel, som skyddas av andra sekundära frön eller hålls offline, **förblir säkra**.



För både BIP-32 och BIP-85 gäller å andra sidan att om den huvudsakliga seed äventyras är **alla fonder sårbara**. Det är därför viktigt att skydda den med högsta möjliga säkerhetsnivå.



![image](assets/fr/02.webp)


## 2. Praktiska användningsfall för BIP-85



Med BIP-85 kan du skapa flera Bitcoin-portföljer från en enda seed-kärnfras, var och en med sin egen seed-sekundärfras. Här är fem praktiska användningsfall för att organisera och säkra dina Bitcoin-medel. Varje fall förklarar varför det är mer praktiskt att använda BIP-85 än att hantera flera konton med en enda seed-fras via BIP-32.



### 2.1 Begränsning av risken i en mindre säker portfölj





- Scenario**: Du använder en "Hot Wallet" Wallet (installerad på en internetansluten enhet) för dagliga transaktioner.
- Lösning BIP-85**: Du skapar en seed sekundärfras som är avsedd för denna portfölj.
- Fördel jämfört med BIP-32**: Du behöver inte importera seed:s primära fras till din telefon, vilket minskar risken för hackning. Endast den sekundära seed-frasen äventyras, vilket skyddar dina andra plånböcker. Med BIP-32 måste du använda seed:s huvudfras och en förbikopplingsväg, vilket exponerar alla dina medel.



### 2.2 Skapa en portfölj för en familjemedlem





- Scenario**: Du sätter upp en Bitcoin Wallet för någon som står dig nära (t.ex. din mamma), samtidigt som du kan återställa den om de tappar bort den.
- Lösning BIP-85**: Du skapar en dedikerad seed sekundär mening och delar endast denna.
- Fördel jämfört med BIP-32**: Med BIP-32 kräver skapandet av ett konto för en närstående att du antingen delar din huvudsakliga seed-fras, riskerar alla dina medel och komplicerar hanteringen för din närstående (hantering av förgreningsvägar), eller skapar en ny seed-fras för att spara utöver din huvudsakliga seed-fras.



### 2.3 Underlätta förvaltningen av separata portföljer





- Scenario**: Du separerar dina bitcoins för olika ändamål (t.ex. långsiktiga besparingar, icke-KYC-fonder).
- Lösning BIP-85**: Du skapar seed sekundära fraser som är dedikerade till varje mål.
- Fördel jämfört med BIP-32**: Med BIP-32 delar alla konton samma seed-fras, vilket komplicerar hanteringen i tredjepartsportföljer eftersom det krävs att avledningsvägar som `m/44'/0'/0'` hanteras. Dessutom är det inte möjligt att tilldela ett separat konto per enhet (t.ex. "besparingar på Coldcard", "dagligen på mobilen", "semestrar på Trezor"). BIP-85 tilldelar en unik seed sekundärfras per mål, som är lätt att identifiera och importera separat på varje enhet.



### 2.4 Använda en tillfällig Wallet för transaktioner





- Scenario**: Du behöver en tillfällig portfölj för en engångstransaktion eller för att bevara sekretessen (t.ex. blandning av fonder, interaktion med Exchange KYC etc.).
- Lösning BIP-85**: Du skapar en seed sekundär mening, använder den för transaktionen och förstör den sedan om det behövs, eftersom du vet att den kan återskapas.
- Fördel jämfört med BIP-32**: Med BIP-32 är ett tillfälligt konto beroende av seed:s huvudmening, vilket innebär att alla dina medel exponeras om de äventyras.





## 3. Innan du börjar





- Hårdvara** (tillval)
 - Coldcard Mk4 eller Q1
 - MicroSD-kort





- Grundläggande kunskaper
 - Förstå Mnemonic-fraser (BIP-39): en lista med 12-24 ord för att spara en portfölj.
 - Vet vad en Bitcoin Wallet är: programvara eller enhet för att hantera dina bitcoins, och hur du återställer den med en Mnemonic-fras.
 - Mer information finns i bilagorna.





- Kompatibel** programvara
 - Sparrow wallet (dator, för endast bevakning eller avancerad hantering)
 - Nunchuck (mobil, för flera signaturer)
 - BlueWallet (mobil)
 - ...





- 3.4 Coldcard**-konfiguration
 - Initiera en seed-mening med 24 ord på Coldcard.
 - Valfritt: Lägg till en passphrase för att säkra åtkomst till BIP-85-filialer.
 - Aktivera användbara alternativ: NFC (för export), avaktivera USB på batteri (säkerhet).




## 4. Steg-för-steg-handledning



Följ dessa steg för att skapa, använda och hämta en sekundär Mnemonic med BIP-85 på ditt Coldcard.



### 4.1 generate a seed sekundär mening



Du kommer att skapa en seed sekundärfras från din seed huvudfras.


Slå på ditt Coldcard och ange din PIN-kod.





- 1. Om du har applicerat en passphrase på din huvud seed:**
 - Från startskärmen, gå till `passphrase`.
    - Välj `Add Word` och ange ditt lösenord.
    - Tryck på `Apply`.
    - Kontrollera Wallet:s identitet: Gå till `Avancerat > Visa identitet` för att notera Wallet:s fingeravtryck.





- 2. Gå till menyn BIP-85**
 - Från startskärmen, gå till `Avancerat > Härled seed B85`
 - Läs varningen och bekräfta.



ColdCard informerar dig om att de frön som genereras är matematiskt härledda från din huvudsakliga seed, men kryptografiskt helt oberoende.


![image](assets/fr/03.webp)





- 3. Välj ett format


Välj seed frasformat: 12, 18 eller 24 ord. Kontrollera antalet ord som accepteras av den Wallet som du vill importera din seed-fras till.


![image](assets/fr/04.webp)





- 4. Välj index
 - Ange ett index mellan 0 och 9999.
 - Detta index är avgörande för att regenerera den sekundära seed vid ett senare tillfälle. Förvara den försiktigt med en etikett som t.ex: "Index 1 = Wallet mobil", "Index 2 = familjeprojekt", "Index 4 = testblandning", ...
 - Om du tappar bort den förlorar du inte tillgången till dina pengar, men du måste testa kombinationer från 0 till 9999 för att hitta dem.


![image](assets/fr/05.webp)





- 5. Notera eller exportera seed sekundär mening**


ColdCard visar nu en ny seed sekundär mening. Du kan :




 - Den **noten manuellt**.
 - Tryck på :
     - 1` för att spara det på SD-kortet
     - `2` för att **införa "använd denna seed"**-läge på ColdCard (användbart för export eller för att signera en transaktion)
     - 3` för att visa en **QR-kod** (som ska skannas med en mobilapplikation som BlueWallet eller Nunchuck)
     - 4` för att skicka det med **NFC**



💡 Vid denna tidpunkt har du en oberoende seed-fras som kan användas i alla Wallet BIP39 (Trezor, Ledger, BlueWallet, Nunchuck...).


![image](assets/fr/06.webp)


![image](assets/fr/07.webp)


### 4.2 Använda den sekundära seed



Du kan nu använda denna härledda seed för att skapa en ny portfölj i :




- en mobilapp
- en annan Hardware Wallet
- en Multisig-portfölj



### 4.3 Återskapa en förlorad seed sekundärfras



Upprepa processen för att när som helst hämta en sekundär seed:


1. Starta om ditt ColdCard


2. Ange din PIN-kod


3. Ange din passphrase, om den är definierad


4. Gå till `Avancerat > Avleda seed B85`


5. Välj format (12/18/24 ord)


6. Ange samma index (t.ex. `1`)


7. Du kommer att få exakt samma sekundära seed




## 5. Gränser, risker och bästa praxis



### 5.1 Beroende av seed huvudmening + passphrase



Användningen av BIP85 är helt beroende av seed:s 24 ord långa huvudmening, samt av passphrase om du har använt en sådan.




- Från dessa två Elements kan alla seed sekundära fraser regenereras.
- Utan en av dessa 2 Elements förlorar du tillgång till alla derivatportföljer.



### 5.2 Risker vid konfiguration med flera signaturer



Vi avråder starkt från att använda sekundära seed-fraser som genereras från samma primära seed-fras i en multi-sig-konfiguration: om enheten eller den primära seed-frasen äventyras kan alla multi-sig-nycklar återskapas av en angripare.



### 5.3 Programvarukompatibilitet



Det är inte alla applikationer som direkt stöder BIP85-derivering. Frön som genereras via BIP85 är dock standard BIP39-frön (12, 18 eller 24 ord) och kan därför användas i alla BIP39-kompatibla portföljer.



### 5.4 BIP85 konto register



Vi rekommenderar att du håller ett uppdaterat personligt register över seed sekundära fraser.




- Det gör att du snabbt kan ta reda på vilket BIP85-index som motsvarar vilken portfölj, utan att behöva hålla på med seed sekundära fraser.
- Detta register ska vara minimalistiskt, utan något uttryckligt omnämnande av Bitcoin, och ska förvaras separat från huvudregistret seed. Kom ihåg att nämna det i din arvsplan.



Registret kan innehålla :




- bIP85 index används (nummer från 0 till 9999)
- ett användnings- eller referensnamn (t.ex. Hot Wallet, personligt sparande, Wallet från mamma)
- vid behov, Wallet-fingeravtrycket för verifiering i ColdCard



### 5.5 Säkerhetskopiering



Säkerhetskopiorna måste innehålla :




- den viktigaste seed
- gW-76 (om den används)



Förvara aldrig tillsammans:




- de viktigaste seed och passphrase
- huvudregistret seed och BIP85-kontoregistret



Mer information finns i bilagorna.




## BILAGOR



## A.1 Ordlista





- [BEEP] (https://planb.network/resources/glossary/bip)
- [BIP-32] (https://planb.network/resources/glossary/bip0032)
- [BIP-39] (https://planb.network/resources/glossary/bip0039)
- [BIP-85] (https://planb.network/resources/glossary/bip0085)
- [seed fras] (https://planb.network/resources/glossary/recovery-phrase)
- [passphrase] (https://planb.network/resources/glossary/passphrase-bip39)
- [Multisig] (https://planb.network/resources/glossary/multisig)




### A.2 Spara din återställningsfras



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


### A.3 Förståelse av passphrase BIP39



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7


### A.4 Hur Bitcoin-portföljer fungerar



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f