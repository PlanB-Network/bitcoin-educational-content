---
name: Electrum Airgap
description: Ett första steg mot säkerhet, en Cold Wallet med Electrum
---
![cover](assets/cover.webp)



## Cold Wallet



I den här handledningen kommer jag att förklara hur du gör din första luftgapssigneringsenhet, frånkopplad från Internet, även utan att ha en dedikerad Hardware Wallet. Allt du behöver är att ha två datorer tillgängliga:




- en gammal enhet för alltid förhindras från att ansluta till Internet;
- din dator som du använder dagligen.



Denna konfiguration möjliggör en högre grad av säkerhet än den klassiska "Hot Wallet": den gamla datorn - utan nätverksanslutning - är innehavare av dina privata nycklar, som aldrig exponeras på Internet, utan lagras offline ("airgap" eller "Cold").



Istället installerar du en Wallet-display ("watch-only") på din dagliga dator, som är ansluten till nätverket och med vilken du t.ex. kan kontrollera saldon och förbereda kvittotransaktioner.



## Wallet Luftgap: Vad och hur



Genom att utföra stegen i den här guiden installerar vi två Software Wallet Electrum på två olika datorer och skapar slutligen två plånböcker med olika nyckelförråd: Wallet airgap kommer att använda hela hierarkin i Wallet HD, medan Wallet display kommer att genereras med den offentliga huvudnyckeln.



Dessa två plånböcker kommer i alla avseenden att vara mycket olika varandra. Det enda de kommer att ha gemensamt är, som vi ska se, adresserna:




- gW-13 på airgap-datorn kan bara signera men, frånkopplad från nätverket, känner inte till balansen och adresserna som används;
- gW-12 på den dagliga datorn kommer endast att kunna förbereda och sprida transaktioner, utan att kunna förfoga över utgifterna, i avsaknad av de privata nycklarna.



## Preliminär förberedelse



För att ladda ner Electrum rekommenderar jag att du följer de första stegen i denna handledning:



https://planb.network/it/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Efter nedladdningen ska du alltid verifiera utgåvan innan du installerar den och sedan gå vidare till konfigurationen "One Server", som du hittar i hjälpavsnittet under `Starta med en Dummy Wallet`.



Konfigurationen "En server" är endast nödvändig för Wallet som är installerad på den dagliga datorn, eftersom den andra datorn alltid kommer att vara offline.



Följande åtgärder innebär att du övar på två olika datorer (och plånböcker), så för enkelhetens och fokuseringens skull valde jag att ställa in Wallet airgap med det ljusa temat, medan Wallet-displayen har det mörka temat.



## Wallet Skapande av luftgap



När du har laddat ner och verifierat nedladdningen av Electrum, ta en kopia av den körbara filen och ta med den till din dator offline. Starta den sedan och installera Electrum.



Dubbelklicka för att starta Electrum: datorn där du kommer att använda denna Wallet är offline, ignorera nätverksinställningarna och gå till skapandet av Wallet som vi i den här guiden kommer att kalla `airgap`.



![image](assets/en/01.webp)



Välj _Standardplånbok_.



![image](assets/en/02.webp)



Och välj sedan _Create a new seed_ för att få programvaran generate till Mnemonic.



![image](assets/en/03.webp)



Transkribera noggrant de 12 generate orden från Electrum till ett pappersunderlag och fortsätt med verifieringssteget och skriv in orden i ordning när Electrum begär det.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



När Wallet-skapandet är klart, ställ in ett komplext lösenord (`Strong`) för att kryptera Wallet-filen på airgap-enheten. Detta steg är mycket känsligt och viktigt, eftersom lösenordet som valts nu, förhindrar åtkomst till Wallet som har dispositiv makt, att kunna spendera medel underteckna transaktioner.



![image](assets/en/06.webp)



Genom att klicka på _Finish_ definieras Wallet och visas på skärmen. Naturligtvis är indikatorn för nätverksanslutning, dvs. den färgade pricken i det nedre högra hörnet, röd, eftersom datorn är frånkopplad och inte tillåter Wallet att exponera online-nycklarna.



![image](assets/en/07.webp)



## Skapande Wallet av visualisering



Nu när din Wallet har privata offline-nycklar måste du ställa in en Wallet-display, eller "endast klocka", som gör att du kan se saldot och förbereda kvittotransaktioner för att fortsätta samla Sats på ett säkert sätt.



Från Wallet på offline-enheten väljer du menyn _Wallet_ -> _Information_



![image](assets/en/08.webp)



Fönstret med all din Wallet-information visas, där du kan kontrollera `derivation path` och `master fingerprint`, till exempel för att markera dem bredvid orden i Mnemonic-meningen (rekommenderas starkt).



![image](assets/en/09.webp)



Kom ihåg att du tar dessa data från en dator som inte är ansluten, så du måste kopiera/klistra in `zpub` till en textfil och spara den på ett usb-minne.



Nu kan du flytta till datorn som är ansluten till Internet, starta Electrum och skapa en ny Wallet.



Välj _New/Restore_ på menyn _File_.



![image](assets/en/10.webp)



Den nya Wallet är endast för visning, så i den här guiden kallar vi den för "endast för visning".



![image](assets/en/12.webp)



På nästa skärm väljer du _Standardplånbok_ och fortsätter genom att klicka på _Nästa_.



![image](assets/en/13.webp)



Var försiktig när du väljer `Keystore`: för att skapa displayen Wallet välj _Use a master key_. Fortsätt sedan med _Nästa_.



![image](assets/en/14.webp)



Klistra in här den `zpub` som kopierats från Wallet offline och som du tog med till den här datorn via usb-media.



![image](assets/en/15.webp)



Avsluta med att ange ett starkt lösenord även för denna Wallet, eventuellt ett annat än det som valts för motsvarande Cold.



Du kommer att se displayen Wallet visas, med en varning. Meddelandet påminner dig om att detta är en Wallet som endast visas och att du inte kan spendera de tillhörande pengarna med den.



**Notera väl**: **Du måste därför alltid ha de privata nycklarna för att göra dig av med UTXO:erna i denna Wallet**. Med ett bra backupsystem kommer det inte att vara svårt för dig att förbli i full besittning av dina Bitcoins.



![image](assets/en/16.webp)



Denna varning kommer att visas varje gång du öppnar denna Wallet. Klicka på _Ok_ och låt oss gå vidare till verifieringssteget.



## Verifiering av de två Wallet



Som vi lärde oss i början av den här guiden är en Wallet airgap och dess display Wallet två plånböcker som har olika funktioner men **delar samma adresser**.



Om vi tittar på de två plånböckerna sida vid sida, märker vi visuellt att det i Wallet-luckan finns en "seed"-symbol, medan det inte finns någon i den enda klockan. Även denna detalj kommer att hjälpa dig att komma ihåg att Wallet-displayen Wallet inte har privata nycklar.



![image](assets/en/17.webp)



För att göra en korrekt första kontroll väljer du dock menyn "Adresser" i båda plånböckerna: eftersom de delar samma adresser bör adresslistan vara identisk för båda.



![image](assets/en/18.webp)



⚠️ **UPPMÄRKSAMHET**: **det finns ingen mellanväg; adresserna måste vara desamma. Om de är olika är det nödvändigt att radera allt arbete som gjorts hittills och börja om från början**.



Nu kan du fortsätta att göra två olika kontroller. Försök först att radera de två plånböckerna och återskapa dem från början, var och en på lämplig dator. Om du fortsätter att göra denna verifiering är procedurerna för visning av Wallet identiska med de som beskrivs ovan.



För Wallet airgap måste du dock på skärmen `keystore` välja _I already have a seed_ och skriva in orden genom att kopiera dem från din pappersbackup.



Efter att "no-load" -försöket är över kan du försöka göra en transaktion med ett litet belopp och spendera det omedelbart.



## Ta emot och spendera transaktioner



För att börja använda din Electrum airgap kan du göra en kvittotransaktion med en liten summa och sedan spendera den på en egen Address. Du kan sedan bekanta dig med proceduren och verifiera att du har full kontroll över pengarna.



**Notera**: Jag rekommenderar inte att du sätter in en stor summa pengar på Wallet innan du är säker på att du kan utföra alla operationer smidigt.



De steg som förklaras nedan kan vid första anblicken verka komplicerade. Men låt dig inte nedslås av detta: När du väl har gjort ett första försök kommer du att märka att det bara tar några minuter att genomföra dem.



För att ta emot pengar måste du nödvändigtvis använda skärmen Wallet som finns på din dator ansluten till Internet. Från menyn `Receive` klicka på _Create request_ för att få Electrum generate den första tillgängliga Address och använd den för att skicka oss några Satss.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



När transaktionen har spridits kan du redan se att den - vilket är naturligt - endast är synlig på displayen Wallet och inte på Wallet airgap.



![image](assets/en/21.webp)



När din transaktion har bekräftats kan du förbereda utlägget och därmed prova signeringsproceduren från Wallet utanför nätverket. Förbered sedan transaktionen på Watch-only och tryck på _Preview_ för att kontrollera den



![image](assets/en/22.webp)



Du får upp det avancerade transaktionsfönstret där du kan se det:




- transaktionen är inte signerad (`Status: Unsigned);
- kommandona `Sign` och `Broadcast` är spärrade.



Det enda du kan göra är att exportera transaktionen som den är, ta den till Wallet airgap och signera den.



Sätt i ett USB-minne i datorn och välj _Share_ i menyn längst ned till vänster.



![image](assets/en/23.webp)



Välj sedan _Spara till fil_.



![image](assets/en/24.webp)



Spara transaktionen på USB-minnet.



Du kommer att märka att Electrum ger filen ett namn som bär de första siffrorna i transaction ID, och filtillägget är `.PSBT`, vilket betyder `Partially Signed Bitcoin Transaction`.



Extrahera media med filen `.PSBT` och anslut den till datorn offline.



Från Wallet airgap väljer du nu menyn _Tools_, sedan _Load transaction_ och därefter From file_.



![image](assets/en/25.webp)



Med filhanteraren väljer du `.PSBT` från dess plats.



![image](assets/en/29.webp)



Programvaran för datorn utanför nätverket öppnar automatiskt det avancerade transaktionsfönstret, helt identiskt med hur du såg det på Wallet-displayen. Statusen är `Unsigned`, men skillnaden är att kommandot `Sign` här är aktivt. Och det är just det som du måste utföra.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Nu när transaktionen är signerad ska du komma ihåg att din Wallet är på en offline-maskin. Därför - även om du ser kommandot `Broadcast` aktivt - kommer din Wallet inte att kunna sprida transaktionen till Bitcoin-nätverket.



Vad du behöver göra nu är att upprepa åtgärden att exportera den signerade transaktionen till USB-minnet, så att du kan importera den till en dator som är ansluten till Internet och sprida den.



I menyn längst ned till vänster väljer du _Share_ igen och sedan _Save to file_.



![image](assets/en/28.webp)



Nu har filen en annan förlängning: **Istället för `.PSBT` har transaktionen nu tillägget `.txn`. Från och med nu är det så här Electrum kommer att låta dig känna igen signerade transaktioner från osignerade**.



![image](assets/en/30.webp)



För den slutliga överföringen av transaktionen tar du ut USB-minnet ur offlinedatorn och sätter in det i den dator som är ansluten till Internet.



Från Watch-only upprepar du importproceduren, dvs. från menyn _Tools_ väljer du _Load transaction_ och slutligen _From file_.



![image](assets/en/31.webp)



Electrum öppnar transaktionsfönstret åt dig, som skiljer sig markant från det som visades tidigare på denna Wallet, genom att det nu är signerat (`Status: Signed`) och `Broadcast`-kommandot är tillgängligt.



Den sista åtgärden du behöver göra är just det:



![image](assets/en/32.webp)



## Slutsatser



Dina tester är nu avslutade. Om du följde guiden och fick samma resultat har du skapat en Wallet Cold med Electrum, på två olika datorer, som du kan använda på ett luftgapsmässigt sätt för att lagra dina Bitcoins.



De enda sakerna du måste vara mycket uppmärksam på är två:


1) **använd aldrig Wallet airgap till generate mottagningsadresser**. Eftersom den är offline kommer den alltid att erbjuda dig den första Address, som sammanfaller med den du just använde för att göra testtransaktionen;



![image](assets/en/33.webp)



_Som du kan se från bilden ovan känner offline Wallet inte till sin egen Address-historia. Den är helt blind i detta avseende. **Den enda uppgift den kan göra åt dig är att lagra dina offlinenycklar och signera dina transaktioner**_.



2) Använd ett USB-minne som endast är avsett för detta ändamål, **använd inte ett medium som du använder ofta**. Vardagsverktyg är mer benägna att utsättas för cyberattacker, och oavsiktligt kan du attackera även den dator som du håller frånkopplad från nätverket. Ett USB-minne som du bara använder för detta ändamål har mycket få möjligheter att komma i kontakt med din dator online, särskilt om du är en hodler som inte behöver spendera, vilket minskar sannolikheten för att ta emot och sedan överföra virus, skadlig kod etc.