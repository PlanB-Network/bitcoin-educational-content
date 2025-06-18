---
name: Threema
description: Säker, anonym direktmeddelandebefordran
---
![cover](assets/cover.webp)



Threema grundades 2012 i Schweiz och är en app för snabbmeddelanden som är utformad för att garantera integritet och säkerhet. Till skillnad från WhatsApp, Telegram eller Signal kräver Threema inget telefonnummer eller e-post Address för att skapa ett konto. Varje användare har en unik identifierare, vilket möjliggör helt anonym registrering.



På den tekniska sidan är kommunikationen över Threema krypterad från början till slut. Mobilapplikationens kod har varit öppen källkod sedan 2020, men serverinfrastrukturen är fortfarande proprietär och centraliserad. Servrarna är uteslutande placerade i Schweiz (ett land som är känt för sitt regelverk för dataskydd).



![Image](assets/fr/01.webp)



Threema har grundläggande klienter för Android och iOS. Det finns också en webbapplikation samt programvara för Windows, Linux och macOS. För att använda dem måste du dock först registrera dig på en mobil enhet.



Threema-applikationen är inte gratis. Den fungerar enligt en modell med engångsköp: 5,99 euro för att använda appen livet ut (eller 4,99 euro om du köper den direkt). För att verkligen kunna använda Threema anonymt måste även betalningen vara anonym. Det är därför du kan köpa en aktiveringsnyckel i bitcoins eller kontanter på "*Threema Shop*" för att aktivera Android-versionen. På iOS måste köpet å andra sidan gå via App Store på grund av Apples begränsningar för intäktsgenerering från appar.



Det finns också en dedikerad affärsversion som heter "*Threema Work*". I den här handledningen koncentrerar vi oss på hemversionen.



| Applikation          | E2EE 1:1       | E2EE grupper   | Anonym registrering | Öppen källkod klient-licens | Öppen källkod server-licens | Decentraliserad server   | Skapandeår        |
| -------------------- | -------------- | -------------- | ------------------- | --------------------------- | --------------------------- | ------------------------ | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                           | ❌                           | ❌                        | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                           | ❌                           | ❌                        | 2011              |
| Facebook Messenger   | ✅              | 🟡 (valfri)    | ❌                   | ❌                           | ❌                           | ❌                        | 2011              |
| Telegram             | 🟡 (valfri)    | ❌              | 🟡                  | ✅                           | ❌                           | ❌                        | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                           | ❌                           | ❌                        | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                           | ✅                           | ❌                        | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                           | ❌                           | ❌                        | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                           | ✅                           | 🟡 (federerad)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                           | N/A                         | 🟡 (via e-post)         | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                           | ✅                           | 🟡 (federerad)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                           | ✅                           | ✅                        | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                           | ✅                           | ✅                        | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                           | ❌                           | 🟡(ingen katalog)       | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                           | N/A                         | ✅                        | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                           | N/A                         | ✅                        | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                           | N/A                         | ✅                        | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                           | N/A                         | ✅                        | 2013              |

*E2EE = End-to-end-kryptering*



## Installera Threema-applikationen



Threema finns tillgänglig på alla plattformar. Du kan ladda ner applikationen direkt från din telefons appbutik:




- [Google Play] (https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold] (https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery] (https://appgallery.huawei.com/#/app/C103713829);
- [App Store] (https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



På Android är det också möjligt att [installera via APK] (https://shop.threema.ch/en/download).



Det finns också [datorversioner] (https://threema.ch/download) (MacOS, Linux och Windows). Den här handledningen visar hur du synkroniserar dem.



## Köpa Threema-licens



När du har installerat applikationen, om du har gått direkt via en appbutik, har du redan betalat för licensen och bör ha omedelbar tillgång till den. Om du gick igenom F-Droid eller APK måste du nu köpa en licens på den officiella webbplatsen.



[Gå till "*Threema Shop*" (https://shop.threema.ch/) och klicka på knappen "*Buy Threema for Android*".



![Image](assets/fr/02.webp)



Välj det antal licenser du vill köpa (bara en om det bara är för dig), välj valuta och välj leveransmetod för licensen. Du kan välja att få licensen via e-post, eller direkt på webbplatsen om du vill vara anonym. Klicka sedan på "*Fortsätt till betalning*".



![Image](assets/fr/03.webp)



Välj din betalningsmetod. I mitt fall kommer jag att betala i bitcoins, vilket jag också rekommenderar att du gör, eftersom det gör att du kan förbli anonym (förutsatt att du använder Bitcoin på rätt sätt) och är mycket bekvämare än en kontant betalning på distans. Klicka sedan på "*Nästa*".



![Image](assets/fr/04.webp)



Om du inte behöver en Invoice klickar du på "*Nästa*" igen utan att ange någon personlig information.



Bekräfta sedan ditt köp genom att klicka på "*Bekräfta betalning*".



![Image](assets/fr/05.webp)



Du måste sedan skicka det angivna beloppet till Bitcoin Address som tillhandahålls (tyvärr stöds inte Lightning ännu). När transaktionen har bekräftats på Blockchain klickar du på "*Close*" bredvid Invoice.



Du kommer då att få tillgång till din licensnyckel. Observera: Om du inte har angett ett e-postmeddelande Address visas denna nyckel endast här. Kom ihåg att spara webbadressen till sidan så att du kan komma åt den senare om det behövs.



![Image](assets/fr/06.webp)



## Skapa ett konto på Threema



Nu när du har din licensnyckel kan du äntligen starta programmet. Vid första lanseringen, om du inte har köpt Threema via en applikationsbutik, kommer du att bli ombedd att ange din licensnyckel som du har köpt på webbplatsen.



![Image](assets/fr/07.webp)



Klicka sedan på knappen "*Set up now*".



![Image](assets/fr/08.webp)



Flytta fingret över skärmen för att generate en källa till entropi, som behövs för att skapa ditt "*Threema ID*".



![Image](assets/fr/09.webp)



Ditt "*Threema ID*" kommer då att visas. Det gör det möjligt för dig att kontakta andra användare. Klicka på "*Nästa*".



![Image](assets/fr/10.webp)



Välj ett lösenord. Det gör att du kan återställa åtkomsten till ditt konto om det skulle behövas. Gör lösenordet så långt och slumpmässigt som möjligt och spara en säker kopia av det, t.ex. i en lösenordshanterare.



![Image](assets/fr/11.webp)



Välj sedan ett användarnamn, som kan vara antingen ditt riktiga namn eller en pseudonym.



![Image](assets/fr/12.webp)



Du kan sedan länka ditt Threema-ID till ditt telefonnummer. Detta gör det lättare för dig att söka bland dina kontakter, men om du använder Threema är det också för att bevara din anonymitet: så det är bäst att inte länka det. Klicka på "*Nästa*".



![Image](assets/fr/13.webp)



När du har slutfört detta steg klickar du på "*Finish*".



![Image](assets/fr/14.webp)



Du är nu ansluten till Threema och kan börja kommunicera.



![Image](assets/fr/15.webp)



## Installera Threema



Först och främst kommer du åt inställningarna genom att klicka på de tre små prickarna uppe i högra hörnet och sedan välja "*Settings*".



![Image](assets/fr/16.webp)



På fliken "*Privacy*" hittar du flera alternativ som du kan anpassa efter dina behov:




- Synkronisera kontakterna på din telefon ;
- Tar emot meddelanden från okända personer;
- Skrivindikator under inmatning av data ;
- Meddelande om mottagande av meddelanden...



![Image](assets/fr/17.webp)



På fliken "*Security*" rekommenderar jag att du aktiverar alternativet "*Locking mechanism*" för att skydda åtkomsten till programmet. Det är också lämpligt att aktivera passphrase för att säkra dina lokala säkerhetskopior.



![Image](assets/fr/18.webp)



Utforska gärna de andra delarna av inställningarna för att anpassa programmet efter dina önskemål.



![Image](assets/fr/19.webp)



## Säkerhetskopiera ditt Threema-konto



Innan du börjar utväxla meddelanden är det viktigt att du planerar ett sätt att återställa ditt konto, särskilt om din telefon byts ut eller försvinner. För att göra detta, klicka på de tre punkterna längst upp till höger på Interface och gå sedan till menyn "*Backups*".



![Image](assets/fr/20.webp)



Här hittar du två alternativ för säkerhetskopiering av dina data:




- "*Threema Safe*";
- "*Data Backup*".



"Threema Safe* sparar all din kontoinformation, förutom dina konversationer, på Threemas servrar. Dessa uppgifter krypteras med det lösenord som du valde när du skapade ditt konto, vilket säkerställer att Threema inte har tillgång till dem. Säkerhetskopior görs automatiskt och regelbundet.



Med "*Threema Safe*", för att återställa ditt konto på en ny enhet, behöver du bara ange ditt "*Threema ID*" och ditt lösenord. Om någon av dessa två uppgifter saknas kommer det att vara omöjligt att återställa ditt konto.



Med det här alternativet kan du bara hämta ditt ID, din profil, dina kontakter, grupper och vissa inställningar, men **inte din samtalshistorik**.



För att aktivera "*Threema Safe*" behöver du bara markera alternativet i menyn "*Backups*".



![Image](assets/fr/21.webp)



Om du också vill säkerhetskopiera och återställa din konversationshistorik måste du använda alternativet "*Data Backup*". Detta genererar en fullständig säkerhetskopia av ditt konto, som lagras lokalt på din telefon. Du måste överföra denna säkerhetskopia till din nya enhet och använda ditt lösenord (och eventuellt din passphrase) för att återställa hela ditt konto.



Eftersom den här säkerhetskopian bara är lokal måste den regelbundet kopieras till externa medier. Annars är det omöjligt att återställa den om enheten försvinner. Den här metoden lämpar sig därför bäst för en planerad överföring från en enhet till en annan, snarare än för nödsituationer.



Observera: "*Data Backup*" fungerar bara om du använder samma operativsystem. Du kommer inte att kunna använda den för att till exempel migrera från en Samsung till en iPhone.



## Anpassa din Threema-profil



I det övre vänstra hörnet av Interface klickar du på din profilbild och väljer sedan "*Min profil*".



![Image](assets/fr/22.webp)



Här kan du anpassa din profil: lägga till ett foto, välja vem som kan se den eller visa din Threema-inloggning.



![Image](assets/fr/23.webp)



## Synkronisera PC-programvara



Om du vill komma åt dina konversationer på din dator kan du synkronisera ditt Threema-konto med den dedikerade programvaran. Ladda ner programvaran för ditt operativsystem [från den officiella webbplatsen] (https://threema.ch/en/download).



![Image](assets/fr/24.webp)



På din telefon klickar du på de tre prickarna uppe till höger och öppnar sedan menyn "*Threema 2.0 for Desktop*".



![Image](assets/fr/25.webp)



Klicka på "*Add device*" och använd sedan din telefon för att skanna QR-koden som visas av programvaran på din dator.



![Image](assets/fr/26.webp)



För att bekräfta synkroniseringen klickar du på den emoji-grupp som visas i programvaran.



![Image](assets/fr/27.webp)



Logga in på din dator med ditt lösenord.



![Image](assets/fr/28.webp)



Förutom mobilapplikationen kan du nu komma åt ditt Threema-konto direkt från din dator.



![Image](assets/fr/29.webp)



## Skicka meddelanden med Threema



Nu när allt är korrekt inställt kan du börja kommunicera. Klicka på knappen "*Starta chatt*".



![Image](assets/fr/30.webp)



Välj "*Ny kontakt*".



![Image](assets/fr/31.webp)



Ange eller skanna din korrespondents "*Threema ID*".



![Image](assets/fr/32.webp)



Klicka på meddelandeikonen.



![Image](assets/fr/33.webp)



Skicka ett första meddelande till din korrespondent.



![Image](assets/fr/34.webp)



När din korrespondent svarar upprättas förbindelsen och du kan se hans eller hennes namn och profilbild. Du kan sedan skicka Exchange-meddelanden, multimediafiler och till och med ringa samtal.



![Image](assets/fr/35.webp)



Grattis, du har nu kommit igång med att använda Threema messaging, ett bra alternativ till WathsApp! Om du tyckte att den här handledningen var användbar skulle jag vara mycket tacksam om du lämnar en Green-tumme nedan. Du får gärna dela denna handledning på dina sociala nätverk. Tack så mycket!



Jag rekommenderar också den här andra handledningen, där jag introducerar dig till Proton Mail, ett mycket mer integritetsvänligt alternativ till Gmail :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2