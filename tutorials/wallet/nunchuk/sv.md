---
name: Nunchuk
description: Wallet mobil lämplig för alla
---
![cover](assets/cover.webp)



## En kraftfull Wallet


Nunchuk kom i slutet av 2020 med en tydlig filosofi: att göra multisignatur till en standard. Den utformades därför för att utföra mycket avancerade funktioner, med det värdefulla valet att bygga designen direkt på Bitcoin Core, referensprogramvaran för Bitcoin-ekosystemet.



Efter mer än 4 år av utveckling och användning är den redo att testas i stor skala. Om du är nybörjare och inte känner till Nunchuk kommer den här guiden att hjälpa dig att ta dina första steg och upptäcka den här programvaran, vars avancerade funktioner du kommer att kunna lära dig om när du har kommit förbi den första effekten. Handledningen i sig är tillägnad mellananvändare som har de nödvändiga färdigheterna för att följa alla steg, men det kan vara en inspiration för alla att ta reda på hur man kan öka färdigheterna. Vi kommer att börja med mobilversionen, och detta påpekande är nödvändigt, eftersom Nunchuk har programvaran för att köra på datorer också.



## Nedladdningar


Det första steget är definitivt att bestämma var du ska ladda ner appen. Gå till den [officiella webbplatsen] (https://nunchuk.io/) där du kan hitta lite dokumentation (inte mycket men det är en början), funktionspresentationen samt, mot slutet av sidan, alla nedladdningslänkar.



📌 För denna handledning bestämde jag mig för att visa dig hur du laddar ner Software Wallet från Github-förvaret och hur du verifierar utgåvan innan du installerar den på din mobiltelefon. ** Följande procedur kan endast göras från din dator **, så jag rekommenderar att du gör alla dessa steg från din stationära eller bärbara dator och - efter alla verifieringar - överför `.apk` -filen till din mobiltelefon.



![image](assets/en/01.webp)



Om dina kunskaper inte är särskilt avancerade kan du välja att ladda ner `.apk` från de officiella butikerna och hoppa direkt till konfigurationsdelen av denna handledning. Om du å andra sidan vill ta språnget, fortsätt att följa steg för steg.



Så från din stationära dator klickar du på _Besök vårt arkiv för öppen källkod_



Länken kommer att ta dig till Nunchuks Github-sida, där du hittar ett antal repos. Vi kommer att fokusera på _nunchuk-android_ en



![image](assets/en/02.webp)



På nästa skärm, leta till höger i avsnittet om _Releases_ och välj _Latest_



![image](assets/en/03.webp)



Under _Assets_ laddar du ner versionen (i det här exemplet 1.67.apk), tillsammans med SHA256SUMS-filen och SHA256SUMS.asc.



![image](assets/en/04.webp)



För att hitta utvecklarens GPG-nyckel, gå tillbaka till avsnittet _Releases_ i arkivet och leta efter 1.9.53 (eller tidigare) som innehåller länken för att få och ladda ner _GPG-nyckeln_



![image](assets/en/05.webp)



Vi kommer att fortsätta med verifiering genom ett praktiskt verktyg som erbjuds av Sparrow wallet, som har ett särskilt fönster för detta ändamål och stöder PGP-signaturer och SHA256 Manifests.



Starta sedan Sparrow och välj _Verify Download_ från menyn _Tools_.



![image](assets/en/06.webp)



I fönstret som dyker upp hittar du fält att "fylla i": välj knappen _Browse_ till höger och välj, för varje fält, motsvarande filer som du just har laddat ner från Github. När du har slutfört alla steg kommer fönstret att se ut som följer, med Green-markeringar och Hash-bekräftelse av manifestet.



![image](assets/en/07.webp)


**N.B. skärmdumpen är från en Windows PC, samma praxis kan användas för alla operativsystem på din dator, bara ha Sparrow wallet installerat. Och verifierad!**



Du kan hitta guiden till Sparrow wallet för att ladda ner denna Software Wallet


https://planb.network/en/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Du kan sedan överföra filen `.apk` från din dator till din telefon



![image](assets/en/08.webp)



och installera Nunchuk



![image](assets/en/09.webp)



Innan du startar Nunchuk på din telefon öppnar du Orbot och lägger till nykomlingen i listan över appar som ska dirigeras under Tor.



![image](assets/en/11.webp)



Kör nu Nunchuk. För projektfunktioner - som inte är ämnet för denna handledning - kommer Nunchuk, när den öppnas, att uppmana dig att logga in via en e-post eller Google-profil. Om du inte planerar att utnyttja Nunchuk Inc:s avancerade planer, **undvik att logga in** och fortsätt genom att välja alternativet _Continue as guest_.



![image](assets/en/12.webp)



## Inställningar


Nunchuk presenterar sig med ett _Home_-fönster, där det är lätt att förstå dess användningsfilosofi och som vi kommer att utveckla om en stund.



Längst ned hittar du menyerna och som första steg väljer du _Profile_ för att komma åt inställningarna.



![image](assets/en/10.webp)



Välj sedan _Display settings_ och fortsätt att ignorera uppmaningen att skapa ett konto.



![image](assets/en/14.webp)



På skärmen nedan kan du kontrollera om Wallet är online och du kan ansluta din server, var noga med att följa instruktionerna på länken som erbjuds genom att klicka på _den här guiden_.



![image](assets/en/15.webp)



Spara inställningarna med kommandot _Save network settings_, gå tillbaka till menyn _Profile_ och välj _Security settings_.



![image](assets/en/16.webp)



I den här menyn ställer du in hur du vill förhindra att appen öppnas. För att förhindra oönskad åtkomst kan du skydda Nunchuk med telefonens biometri och/eller lägga till en säkerhets-PIN-kod.



![image](assets/en/17.webp)



Ta också en titt på menyn _Om_, som du alltid hittar i fönstret _Profil_



![image](assets/en/18.webp)



som gör att du kan kontrollera appens version eller kontakta utvecklarna om det behövs.



![image](assets/en/19.webp)



## Nyckelgenerering och Wallet


Som det är lätt att gissa från Nunchuks filosofi är programvaran avsedd som ett användbart verktyg för att hantera plånböcker med flera signaturer. För att utföra denna funktion tillåter Nunchuk skapandet av Wallet genom att separera dem från de nycklar som behövs för att ordna digitala signaturer.



I själva verket innebär den ideala driften av Nunchuk skapandet av plånböcker som bara kan vara klockor, beroende av nycklar som kan vara "kalla"



I de tidigare skärmarna kanske du har märkt att det finns en meny längst ned som heter _Keys_. Om du precis har laddat ner Nunchuk kommer du i både _Home_ och _Keys_ att se en stor knapp som inbjuder dig att lägga till en nyckel, _Add Key_.



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**Det är precis så här Nunchuk fungerar:** först generate/importerar du nycklarna och sedan skapar du Wallet och konfigurerar den för att välja vilka nycklar som ska godkänna upplåsningen av de medel som lagras på den.



Även när det gäller Wallet singlesig skapar du nyckeln först och först sedan Wallet. Och det är precis vad vi ska göra nu, vi börjar med en Wallet singlesig för att bryta isen och upptäcka Nunchukens funktioner.



Klicka på _Lägg till nyckel_



![image](assets/en/22.webp)



Nunchuk visar ett antal signaturenheter som stöds, men för att börja väljer du _Software_.



![image](assets/en/23.webp)



Nunchuk kommer generate en Mnemonic som kommer att lagras på enheten. Du måste sedan skriva ner ordföljden för säkerhetskopieringen, skapa de bästa miljöförhållandena och se till att du har tid att göra det på ett bra och tyst sätt. Programvaran visar Mnemonic endast en gång, oavsett om du väljer att visa den nu eller senare, så välj _Create and backup now_.



![image](assets/en/24.webp)



Nunchuk genererar 24 ords Mnemonic-meningar, som visas omedelbart på nästa skärm



![image](assets/en/25.webp)



och gjorde sedan en snabb kontroll där du ombads välja rätt ord bland tre alternativ som motsvarar numret i Mnemonic-sekvensen.


Om du har skrivit Mnemonic på rätt sätt blir knappen _Continue_ funktionsduglig. Tryck på den för att gå vidare.



![image](assets/en/26.webp)



Namnge din nyckel och tryck på _Continue_.



![image](assets/en/27.webp)



I slutet av dessa steg kommer du att få frågan om du vill lägga till en [passphrase](https://planb.network/en/resources/glossary/passphrase-bip39) till din Mnemonic-fras. Om du inte har den nödvändiga kunskapen om hur du använder passphrase, ordnar med säkerhetskopiering eller hur det fungerar rekommenderar jag att du väljer _Jag behöver ingen lösenfras_.



![image](assets/en/28.webp)



Nyckeln skapas slutligen och visas för dig i menyn:




- Med _Key Spec_ anges huvudfingeravtrycket
- Du har inställningar, de tre prickarna längst upp till höger, där du kan radera nyckeln eller signera ett meddelande
- Bredvid nyckelns namn finns en spets-ikon som du kan klicka på för att ändra nyckelns namn, t.ex. för att hålla ordning på dina nycklar i framtiden.
- Som ett sista kommando kan du kontrollera nyckelns hälsostatus: genom att trycka på _Run health check_ kan du få appen att kontrollera om en nyckel är skadad.



När du är klar klickar du på _Done_



![image](assets/en/29.webp)



I menyn _Keys_ ser du din första tangent visas.



![image](assets/en/30.webp)



Genom att gå till menyn _Home_ visas möjligheten att skapa Wallet. Klicka på _Create new wallet_.



![image](assets/en/31.webp)



Nunchuk visar dig ett antal möjligheter som till största delen har att göra med tjänster som företaget erbjuder och som inte är föremål för denna handledning.



I den här guiden kommer vi att skapa en _Hot Wallet och en _Custom wallet_ genom att beskriva detaljerna.


Låt oss börja med _Custom wallet_.



![image](assets/en/32.webp)



På ett enkelt sätt kommer appen att be dig att namnge denna nya Wallet och välja skriptet för adresserna. För handledningen valde jag att lämna standardinställningen, _Native segwit_. När du är klar väljer du _Continue_



![image](assets/en/33.webp)



Konfigurationen av Wallet fortsätter med att be dig att ställa in med vilken nyckel fonderna i denna Wallet ska låsas upp. Om det finns flera nycklar kommer du att visas en lista att välja mellan. Vi har för tillfället bara skapat en, så vi väljer att sätta en bock på den. I det nedre högra hörnet kan du se hur Nunchuk kommer att be dig att ställa in dina framtida Wallet multisignaturer, vilket ökar antalet _Krävda nycklar_.



![image](assets/en/34.webp)



Eftersom vi skapar en singlesig lämnar vi `1` och klickar på _Continue_.



Sist visas en verifieringsskärm där du kan kontrollera funktionerna i Wallet:




- namnet
- `1/1 Multisig` tage, vilket är hur Nunchuk kallar Wallet singlesig
- skripttypen, `Native SegWit`
- nyckeln `Keys`, med dess fingeravtryck och härledningsväg



När du är nöjd trycker du på _Create wallet_



![image](assets/en/35.webp)



Wallet har skapats och du kan ladda ner filen [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) som en säkerhetskopia. För att återgå till huvudmenyn klickar du på pilen i det övre vänstra hörnet.



![image](assets/en/36.webp)



Du befinner dig i _Home_, där du ser den nyskapade Wallet som rapporterar saldot och status för anslutningen. Genom att klicka i det blå fältet får du tillgång till Wallet:s huvudfunktioner.



![image](assets/en/37.webp)





- Lins-ikonen i det övre högra hörnet gör att du kan göra en transaktionssökning;
- `View Wallet config` ger tillgång till konfigurationsmenyn, där du kan redigera namnet på Wallet och aktivera avancerade alternativ, uppe till höger (som du inte kan få skärmdumpar av). Här kan du exportera Wallet-konfigurationen, etiketter, byta ut nycklar, ändra [gap limit] (https://planb.network/en/resources/glossary/gap-limit) och mycket mer.



## Transaktioner med Nunchuk



Utmärkelser _Mottagare



![image](assets/en/38.webp)



Appen är programmerad att visa QR-koden för Address eller kopiera/dela scriptPubKey för att ta emot medel i kedjan.



![image](assets/en/39.webp)



Vi hade en UTXO som anlände på den här första Address:an,



![image](assets/en/40.webp)



men vi klickar ändå på _Receive_ för att få en ny.



![image](assets/en/41.webp)



Syftet är att du ska få reda på att Nunchuk rapporterar denna nya Address till dig som en _Oanvänd adress_ men också visar dig att du har _Utnyttjade adresser_ och antalet av dessa.



### Utbetalningstransaktion med myntkontroll



När den andra UTXO också har anlänt går du tillbaka till Wallet:s huvudskärm för att kontrollera statusen för de två inkommande transaktionerna och, viktigast av allt, klicka på alternativet _Visa mynt_



![image](assets/en/42.webp)



där du kommer att visas enskilda UTXO. Här kan du välja att se en särskild genom att klicka på den lilla pilen bredvid beloppet



![image](assets/en/43.webp)



och kolla när den kom, beskrivningen, blockera UTXO så att den inte spenderas och mer.



![image](assets/en/44.webp)



Men om du går tillbaka till menyn _Coins_ genom att klicka på pilen i det övre högra hörnet kan du aktivera "Coin Control" för att spendera dina UTXO:er på ett mer kontrollerat sätt.



I följande exempel valde jag att markera UTXO av 21.000 Sats och sedan klicka på symbolen i det nedre vänstra hörnet.



![image](assets/en/45.webp)



Nunchuk öppnar automatiskt fönstret _Ny transaktion_ för att spendera denna UTXO. I utgiftstransaktionen måste du först ställa in beloppet manuellt eller genom att välja _Sänd alla valda_ för att skicka hela myntkontrollsaldot utan att generera rester. När beloppet har ställts in väljer du _Continue_



![image](assets/en/46.webp)



Nu visar Nunchuk var du ska klistra in Address som du ska överföra pengarna till, ge en beskrivning och slutföra transaktionen.



![image](assets/en/47.webp)



Om du väljer _Create transaction_ delegeras den automatiska avgifts- och transaktionshanteringen till appen. Jag rekommenderar att du väljer _Custom transaction_ för att få mer kontroll.



I den här nya skärmen är det viktigt att välja




- _Subtrahera avgift från sändningsbelopp_, för att förhindra att avgifter betalas av en annan UTXO som befinner sig i Wallet, spenderar den och genererar en rest (vilket är en undvikbar förlust av integritet);
- och sedan sätta avgifterna manuellt efter att ha kontrollerat utforskaren.



När du har gjort alla dessa steg klickar du på _Continue_



![image](assets/en/48.webp)



På nästa skärm visas en fullständig sammanfattning av transaktionen. Om allt är okej, bekräfta genom att välja _Confirm and create transaction_.



![image](assets/en/49.webp)



Med _Pending signatures_ meddelar Nunchuk att transaktionen väntar på din underskrift för att godkänna utgiften, vilket du gör genom att klicka på _Sign_.



![image](assets/en/50.webp)



Kommandot _Broadcast_ visas längst ned för att sprida den slutförda och signerade transaktionen.



![image](assets/en/51.webp)



### Utbetalningstransaktion från menyn _Send_



Medan vi på huvudsidan i Wallet ser transaktionen gå ut och vänta på bekräftelse, använder vi _Send_-menyn för att simulera en daglig utgift.



![image](assets/en/52.webp)



Genom att klicka på _Send_ får du upp skärmen för att skicka transaktionen, som är densamma som den som just visades, men utan att gå igenom myntkontrollen.



Även i detta andra exempel valde jag att välja _Custom transaction_ och skicka hela beloppet, men jag kunde ha ställt in det manuellt. När du har bestämt vilket belopp du vill skicka trycker du på _Continue_.



![image](assets/en/53.webp)



Gör sedan alltid en bedömning om avgifterna ska dras från UTXO i fråga (i detta exempel är valet tvunget, eftersom det bara finns ett), justera avgifterna manuellt enligt situationen vid den aktuella tidpunkten i Mempool och tryck på _Continue_.



![image](assets/en/54.webp)



Om sammanfattningsbilden är tillfredsställande väljer du _Confirm and create transaction_.



![image](assets/en/55.webp)



Signera transaktionen med _Sign_



![image](assets/en/56.webp)



och sprider den till nätverket.



![image](assets/en/57.webp)



Wallet befinner sig vid denna punkt med saldot noll och historiken uppdateras.



![image](assets/en/58.webp)



## Skapande av en "Hot Wallet"



Sist, och för att inte utelämna något från de inledande stadierna av Nunchuk mobile, låt oss se hur detta skapar vad appen kallar "Hot Wallet"



I _Home_-menyn på Nunchuk, där listan med plånböcker visas, klickar du på `+` i det övre högra hörnet.



![image](assets/en/59.webp)



Välj _Hot wallet_ bland alternativen



![image](assets/en/60.webp)



Nunchuk ger några råd om hantering av Hot plånböcker på presentationssidan, där du väljer _Continue_ för att fortsätta.



![image](assets/en/61.webp)



Efter några ögonblick skapas Wallet och visas i listan i brunaktig färg. Det är med denna färg som Nunchuk varnar dig för att du ännu inte har säkerhetskopierat Wallet.



![image](assets/en/62.webp)



Klicka på namnet på Wallet för att komma åt dess konfigurationer, och du kanske ser en inbjudan att säkerhetskopiera Mnemonic-frasen omedelbart.



![image](assets/en/63.webp)



Proceduren är densamma som vi har sett tidigare, så vi kommer inte att gå igenom den igen. När det är gjort kommer Nunchuk att ta dig till den relevanta nyckelsidan, som du kan redigera som den du skapade med _Custom_-proceduren.



![image](assets/en/64.webp)



Prova också _Kör hälsokontroll_



![image](assets/en/65.webp)



eller för att se hur du visar alla dina plånböcker i appens _Home_.



![image](assets/en/66.webp)



## Att komma ihåg att fortsätta självständigt


Precis som det finns en ordning för skapande, det vill säga att först generera nycklarna och sedan Wallet, måste du upprätthålla den omvända ordningen för att ta bort dessa objekt från din app.



Om du behöver ta bort en av nycklarna bör du först vara förutseende nog att ta bort Wallet eller plånböckerna, som använder en av signaturnycklarna för transaktioner: först tar du bort plånböckerna och först därefter nycklarna. Om du inte följer den här ordningen kommer du att upptäcka att du inte kan ta bort nyckeln.



Nu när du vet hur du kommer igång med Nunchuk kan du fortsätta att studera den här appen och upptäcka dess hemligheter. I den här handledningen har vi bara tagit de första stegen, men det finns mer sofistikerade applikationer och avancerade behov som denna Software Wallet kan hjälpa dig att uppfylla.