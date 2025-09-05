---
name: COLDCARD Q - Avancerad
description: Använda COLDCARD Q:s avancerade alternativ
---
![cover](assets/cover.webp)


![video](https://youtu.be/6L2hhT0J27s)


I en tidigare handledning gick vi igenom den första konfigurationen av COLDCARD Q och dess grundläggande funktioner för nybörjare. Om du precis har fått ditt COLDCARD Q och inte har konfigurerat det ännu, rekommenderar jag att du börjar med den handledningen innan du fortsätter här:


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Den här nya handledningen handlar om COLDCARD Q:s avancerade alternativ, som är utformade för avancerade och paranoida användare. Faktum är att COLDCARDs skiljer sig från andra hårdvaruplånböcker genom sina många avancerade säkerhetsfunktioner. Naturligtvis behöver du inte använda alla dessa alternativ. Välj bara de som passar din säkerhetsstrategi.


**Varning**, felaktig användning av några av dessa avancerade alternativ kan leda till förlust av dina bitcoins eller förstörelse av din Hardware Wallet. Jag rekommenderar därför starkt att du läser råden och förklaringarna för varje alternativ noggrant.


Innan du börjar ska du se till att du har tillgång till en fysisk säkerhetskopia av din Mnemonic-fras med 12 eller 24 ord och kontrollera dess giltighet via följande meny: `Avancerat/Verktyg > Farozonen > seed-funktioner > Visa seed-ord`.


![CCQ](assets/fr/01.webp)


## BIP39 passphrase


Om du inte vet vad en BIP39 passphrase är, eller om det inte är helt klart för dig hur den fungerar, rekommenderar jag starkt att du tar en titt på den här handledningen i förväg, som täcker de teoretiska grunder som behövs för att förstå riskerna med att använda en passphrase :


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Tänk på att när du har konfigurerat passphrase på din Wallet räcker inte din Mnemonic ensam för att återfå åtkomst till dina bitcoins. Du behöver både Mnemonic och passphrase. Dessutom måste du ange passphrase varje gång du låser upp ditt COLDCARD Q. Detta förbättrar säkerheten genom att göra fysisk åtkomst till COLDCARD och kunskap om PIN-koden otillräcklig utan passphrase.


På COLDCARDs har du två alternativ för att hantera din passphrase:


1. **Klassisk inmatning:** Du matar in passphrase manuellt varje gång du använder din Hardware Wallet, precis som du gör med andra hårdvaruplånböcker. COLDCARD Q förenklar denna uppgift med sitt kompletta tangentbord.


2. **Du kan välja att kryptera din passphrase och lagra den på ett microSD-kort. I så fall måste du sätta in microSD-kortet i COLDCARD Q varje gång du använder det. Observera att detta microSD-kort endast fungerar i ditt COLDCARD Q och inte är en säkerhetskopia. Det är därför mycket viktigt att du också behåller en kopia av din passphrase på ett fysiskt medium, t.ex. papper eller metall.


För att ställa in din BIP39 passphrase, gå till menyn "*passphrase*".


![CCQ](assets/fr/02.webp)


Ange din passphrase med hjälp av tangentbordet. Var noga med att välja en stark passphrase (lång och slumpmässig) och gör en fysisk säkerhetskopia.


![CCQ](assets/fr/03.webp)


När du har ställt in din passphrase kommer COLDCARD Q att visa dig huvudnyckelns fingeravtryck för den nya Wallet som är associerad med denna passphrase. Var noga med att spara detta fingeravtryck. När du anger din passphrase igen när du använder din enhet i framtiden kan du kontrollera att fingeravtrycket som visas matchar det du sparade. Denna kontroll säkerställer att du inte har gjort något misstag när du angav din passphrase.


![CCQ](assets/fr/04.webp)


Du kan nu trycka på "*ENTER*" för att använda denna passphrase till din Mnemonic-fras och aktivera den nya Wallet. Om du föredrar att spara denna passphrase på ett microSD-kort, sätt in kortet i lämplig kortplats och tryck på "*1*".


![CCQ](assets/fr/05.webp)


Din passphrase är nu applicerad. Nyckelavtrycket visas på startskärmen och högst upp på skärmen.


![CCQ](assets/fr/06.webp)


Varje gång du låser upp ditt COLDCARD Q måste du gå till menyn "*passphrase*" och ange din passphrase på samma sätt som ovan, för att tillämpa den på den Mnemonic som finns lagrad i enheten och få tillgång till rätt Bitcoin Wallet.


![CCQ](assets/fr/07.webp)


Om du har sparat passphrase på ett microSD-kort ska du sätta in det i COLDCARD varje gång du använder det och öppna menyn "*passphrase*". Ditt COLDCARD laddar passphrase direkt från microSD-kortet, så du behöver inte ange den manuellt. Klicka på "*Restore Saved*".


![CCQ](assets/fr/08.webp)


Kontrollera att längden och första bokstaven i den laddade passphrase är korrekta.


![CCQ](assets/fr/09.webp)


Bekräfta att det fingeravtryck som visas stämmer överens med ditt Wallet och klicka på "*Restore*".


![CCQ](assets/fr/10.webp)


Tänk på att om du använder en passphrase innebär det att du måste importera en ny uppsättning nycklar som härrör från kombinationen av din Mnemonic-fras och passphrase till din Wallet-hanteringsprogramvara (som Sparrow wallet). För att göra detta, följ steget "*Konfigurera en ny Wallet på Sparrow*" i denna andra handledning :


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

## Lås upp alternativ


COLDCARDs drar också nytta av en mängd alternativ för upplåsningsprocessen för enheten. Låt oss ta reda på mer om dessa avancerade alternativ.


### Trickade PIN-koder


En Trick PIN-kod är en sekundär PIN-kod som skiljer sig från den som definieras under den första konfigurationen av enheten. Denna kod används för att utlösa specifika förkonfigurerade åtgärder så snart den anges när COLDCARD slås på. Du kan konfigurera flera Trick PIN-koder, var och en kopplad till en annan åtgärd. Med dessa funktioner kan du anpassa ditt COLDCARD till din personliga säkerhetsstrategi. De är särskilt användbara i fall av fysiskt tvång, t.ex. under ett rån (som i Bitcoin-samhället ofta kallas en "*$5 wrench attack*").


Om du vill aktivera en Trick PIN-kod och koppla den till en åtgärd går du till menyn `Inställningar > Inloggningsinställningar > Trick PIN-koder`.


![CCQ](assets/fr/11.webp)


Välj "*Lägg till nytt trick*".


![CCQ](assets/fr/12.webp)


Ställ in PIN-koden så att den är kopplad till åtgärden och kom ihåg att spara den.


![CCQ](assets/fr/13.webp)


Välj sedan den åtgärd som ska utföras automatiskt varje gång du anger den här Trick PIN-koden. Här är listan över åtgärder som är tillgängliga för en PIN-kod:




- "*Brick själv*: Denna åtgärd förstör båda COLDCARD Q-chipen om Trick PIN-koden anges, vilket gör enheten helt oanvändbar. Det blir då omöjligt att sälja vidare, återanvända eller ens returnera den till Coinkite. Enheten blir oåterkalleligen föråldrad. Denna funktion kan användas vid ett rån för att övertyga en angripare om att han aldrig kommer att kunna komma åt dina bitcoins. ** Observera**: utan en fysisk säkerhetskopia av din Mnemonic-fras och alla passphrase kommer dina bitcoins att gå förlorade permanent.


![CCQ](assets/fr/14.webp)




- "*Wipe seed*": Denna meny erbjuder flera åtgärder för att radera seed, dvs. återställa COLDCARD utan att förstöra det. Till skillnad från alternativet "*Brick Self*" kommer det att vara möjligt att konfigurera om enheten med hjälp av en säkerhetskopia av din Mnemonic-fras. Men utan denna säkerhetskopia kommer dina bitcoins att gå förlorade. Här är de tillgängliga alternativen:
 - "*Wipe & Reboot* : Tar bort seed och startar om COLDCARD utan att visa någon information på skärmen.
 - "*Silent Wipe*": Raderar tyst seed och låser upp COLDCARD på en slumpmässigt vald falsk Wallet som om ingenting hade hänt.
 - "*Wipe -> Wallet*": Tar diskret bort seed och låser upp COLDCARD på en förkonfigurerad sekundär Wallet, utformad som ett lockbete. Denna Wallet kan innehålla en liten del av dina Bitcoin besparingar för att tillfredsställa en angripare.
 - "*Säg torkad, stopp*": Raderar seed och visar meddelandet `seed is wiped, Stop` på skärmen.


![CCQ](assets/fr/15.webp)




- "*Duress Wallet*": Med denna åtgärd låser Trick PIN-koden upp en Wallet som härrör från seed med hjälp av BIP85. Denna sekundära Wallet kan användas som lockbete för att tillfredsställa en angripare. COLDCARD fungerar som om det vore den riktiga Wallet, men utan huvud-PIN-koden (som skiljer sig från Trick-PIN-koden) kommer angriparen aldrig att kunna komma åt den riktiga Wallet. Denna strategi är utformad för att få människor att tro att den Wallet som är kopplad till Trick PIN-koden är den enda som existerar.


![CCQ](assets/fr/16.webp)




- "*Inloggning nedräkning*": Den här menyn grupperar åtgärder med en nedräkning innan de utförs. **Varning**, vissa av dem kan förstöra din enhet eller resultera i förlust av dina bitcoins. Här är de tillgängliga underåtgärderna:
 - "*Wipe & Countdown* : Raderar seed från COLDCARD:s minne och startar sedan en nedräkning på en timme. Utan att spara din Mnemonic eller passphrase kommer dina bitcoins att gå förlorade. Det här alternativet är utformat för att lura en angripare att tro att enheten kommer att låsas upp i slutet av nedräkningen, när den i själva verket kommer att återställas till fabriksinställningarna.
 - "*Nedräkning och tegelsten*": Startar en nedräkning på en timme, i slutet av vilken COLDCARD förstör sina två säkra chip, vilket gör det permanent oanvändbart. Utan backup kommer dina bitcoins att gå förlorade. Denna åtgärd är utformad för att lura en angripare, som tror att han väntar på en upplåsning, när enheten i själva verket kommer att självförstöras.
 - "*Just nedräkning* : Utlöser en enkel nedräkning på en timme, varefter COLDCARD startar om utan någon ytterligare åtgärd. seed raderas inte och enheten förblir intakt. Var noga med att inte förväxla denna åtgärd med alternativet "*Login Countdown*", som diskuteras i följande avsnitt, som lägger till en nedräkning till huvud-PIN-koden samtidigt som den ger tillgång till den riktiga Wallet.


![CCQ](assets/fr/17.webp)




- "*Se tomt ut*": Denna åtgärd får COLDCARD att se tomt ut, vilket ger intrycket att seed har raderats. I själva verket händer ingenting och seed förblir intakt. Detta simulerar ett oanvänt eller återställt COLDCARD.


![CCQ](assets/fr/18.webp)




- "*Just Reboot* : När Trick PIN-koden används startar COLDCARD helt enkelt om. Ingen annan åtgärd utförs.


![CCQ](assets/fr/19.webp)




- "*Delta-läge*": Denna komplexa åtgärd, som är reserverad för erfarna användare, är utformad för att motverka mycket sofistikerade tvångsattacker, oavsett om de kommer från en stat eller en släkting med privilegierad information. När Delta-läget är aktiverat ger COLDCARD tillgång till den riktiga Wallet, vilket gör det möjligt för en angripare att navigera och verifiera att det är rätt Wallet. Transaktionssignaturer blockeras dock, vilket förhindrar all Bitcoin-överföring. Dessutom är tillgången till Mnemonic-frasen inaktiverad och alla försök att hämta den kommer att resultera i att den raderas. För att öka trovärdigheten måste Trick PIN-koden som används med Delta Mode ha samma prefix som den riktiga PIN-koden (för att visa samma anti-phishing-ord), men suffixet måste vara annorlunda.


![CCQ](assets/fr/20.webp)


När du har valt en åtgärd ska du bekräfta ditt val.


![CCQ](assets/fr/21.webp)


Du kan sedan se alla konfigurerade Trick PIN-koder i den särskilda menyn.


![CCQ](assets/fr/22.webp)


Genom att välja en befintlig Trick PIN kan du kontrollera den tillhörande åtgärden. Du kan också dölja den med "*Hide Trick*", vilket gör den osynlig i Trick PIN-menyn. Du kan radera den genom att klicka på "*Delete Trick*" eller ändra PIN-koden med bibehållen tillhörande åtgärd med "*Change PIN*".


![CCQ](assets/fr/23.webp)


Med alternativet "*Add If Wrong*", som finns i menyn "*Trick PIN*", kan du konfigurera en specifik åtgärd som automatiskt utlöses efter ett visst antal felaktiga försök att ange master-PIN-koden. Antalet tillåtna försök kan ställas in under konfigurationen.


### Förvrängningsnycklar


Med alternativet Scramble Keys kan du förvränga de siffror som visas på knappsatsen när du anger din PIN-kod. Denna funktion skyddar din PIN-kod, även om den skulle övervakas av personer eller kameror.


För att aktivera detta alternativ, gå till menyn `Inställningar > Inloggningsinställningar > Scramble Keys`.


![CCQ](assets/fr/24.webp)


Välj alternativet "*Scramble Keys*".


![CCQ](assets/fr/25.webp)


När du låser upp ditt COLDCARD Q kommer knapparna på knappsatsen från och med nu att tilldelas nya nummer slumpmässigt varje gång du använder dem.


![CCQ](assets/fr/26.webp)


### Nedräkning för inloggning


Med det här alternativet kan du införa en systematisk nedräkning varje gång du försöker låsa upp ditt COLDCARD. Det kan integreras i din säkerhetsstrategi genom att fördröja åtkomsten till enheten i händelse av stöld eller genom att införa en fördröjning innan du undertecknar en transaktion, till exempel för att skydda dig i händelse av ett rån. Denna nedräkning gäller dock för alla dina användningsområden, även när du använder ditt COLDCARD på ett legitimt sätt, vilket också kräver tålamod. Var noga med att inte förväxla detta alternativ med åtgärden "*Just Countdown*", som endast aktiveras när en specifik Trick PIN används.


För att konfigurera detta alternativ, gå till menyn `Inställningar > Inloggningsinställningar > Nedräkning för inloggning`.


![CCQ](assets/fr/27.webp)


Välj nedräkningstid. Om du t.ex. väljer 1 timme, måste du vänta 1 timme för varje försök att låsa upp COLDCARD Q.


![CCQ](assets/fr/28.webp)


Varje gång du låser upp kommer du att uppmanas att ange din PIN-kod.


![CCQ](assets/fr/29.webp)


Vänta sedan på den tid som anges av nedräkningen.


![CCQ](assets/fr/30.webp)


I slutet av nedräkningen måste du ange din PIN-kod igen för att komma åt enheten.


![CCQ](assets/fr/31.webp)


### Inloggning för kalkylator


Med detta alternativ kan du dölja ditt COLDCARD som en miniräknare när du låser upp det. För att aktivera denna funktion, gå till menyn `Inställningar > Inloggningsinställningar > Inloggning med miniräknare`.


![CCQ](assets/fr/32.webp)


Aktivera alternativet genom att markera det.


![CCQ](assets/fr/33.webp)


Från och med nu visas en fungerande miniräknare med grundläggande kommandon varje gång enheten slås på.


![CCQ](assets/fr/34.webp)


Du kan t.ex. beräkna SHA256 Hash för "*Plan B Network*".


![CCQ](assets/fr/35.webp)


För att låsa upp COLDCARD från miniräknarläget börjar du med att ange PIN-koden med ett prefix följt av ett bindestreck. Om din PIN-kod till exempel är `00-00` (den här koden är svag och bara ett exempel, så välj en stark PIN-kod), skriv `00-`. COLDCARD kommer då att visa dina två ord mot nätfiske.


![CCQ](assets/fr/36.webp)


Ange sedan din fullständiga PIN-kod, åtskild av ett mellanslag eller ett bindestreck, till exempel: `00 00`.


![CCQ](assets/fr/37.webp)


COLDCARD lämnar då kalkylatorläget och låses upp på normalt sätt.


## Förstör ditt COLDCARD på ett snyggt sätt


Om du planerar att göra dig av med ditt COLDCARD Q, t.ex. för att du nu använder en annan Hardware Wallet, är det viktigt att förstöra enheten på rätt sätt. Detta säkerställer att ingen information som rör din Wallet kan återskapas av tredje part.


Det finns tre nivåer av informationsförstöring, beroende på dina behov. Innan du börjar, se till att din Wallet har importerats till en annan Hardware Wallet, att du har tillgång till alla dina medel och framför allt att du har din Mnemonic-fras och alla passphrase, som båda är funktionella. Utan en Wallet-backup kommer förstörelsen av ditt COLDCARD att leda till förlust av dina bitcoins.


Den första nivån av förstörelse består av att endast radera seed. Detta alternativ raderar din Mnemonic-fras från COLDCARDs minne, samtidigt som enheten förblir funktionell. Det är idealiskt om du vill använda COLDCARD Q igen vid ett senare tillfälle. För att radera seed ur minnet, gå till menyn `Avancerat/Verktyg > Farozon > seed Funktioner > Förstör seed`.


![CCQ](assets/fr/38.webp)


Den andra nivån av förstörelse består i att permanent inaktivera COLDCARDs två säkra chip via programvaran. Denna åtgärd gör enheten helt oanvändbar. Du kommer inte att kunna sälja den vidare, återanvända den eller returnera den till Coinkite: den kommer att förstöras permanent. För att fortsätta, följ stegen som beskrivs i föregående avsnitt angående "*Brick Me*" PIN-koden, och ange sedan avsiktligt denna PIN-kod när du låser upp COLDCARD.


Den tredje nivån innebär fysisk förstörelse av COLDCARD Q:s säkra komponenter. Precis som tidigare kommer detta att göra enheten oåterkalleligt oanvändbar. För att göra detta, använd en borr för att göra ett hål i de två chipen på enhetens övre högra sida (när den är vänd upp och ner), nära "*SHOOT HERE*"-inskriptionen.


**Viktiga försiktighetsåtgärder** :




- För att undvika risken för elektriska stötar ska du ta ut batterierna ur enheten och koppla bort den från elnätet innan du hanterar den.
- Vänta några minuter efter att maskinen stängts av innan du börjar borra.
- Använd isolerade handskar och skyddsglasögon för att garantera din säkerhet.


![CCQ](assets/fr/39.webp)


När chipen har stansats, försök inte att återansluta COLDCARD Q.


Grattis, du har nu fått tillgång till COLDCARD Q:s avancerade alternativ!


Om du tyckte att den här handledningen var användbar skulle jag vara mycket tacksam om du lämnar en Green-tumme nedan. Dela gärna den här handledningen på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också den här andra handledningen, där vi diskuterar användningen av en direkt konkurrent till CCQ, Ledger Flex :


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a