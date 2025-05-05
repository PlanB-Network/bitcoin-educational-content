---
name: Portal
description: Konfigurera och använda TwentyTwo-Devices Hardware Wallet Portal
---
![cover](assets/cover.webp)


Portal är en Bitcoin Hardware Wallet designad av TwentyTwo Devices, ett företag som specialiserar sig på att skapa hårdvaruplånböcker med öppen källkod för bitcoiners. TwentyTwo Devices grundades av Alekos Filini, skaparen av Magical Bitcoin-projektet ([hädanefter kallat BDK](https://github.com/bitcoindevkit)) och har arbetat för Blockstream och BHB Network, och har som mål att fokusera på användarautonomi, enkelhet och säkerhet.


Det som skiljer Portal från andra hårdvaruplånböcker på marknaden är dess inbyggda integration med smartphones. Den fungerar utan kablar eller batterier. Den använder NFC-teknik för att driva sig själv och kommunicera med alla kompatibla mobila Wallet. Den spännande designen är utformad för ergonomisk användning. Den runda delen placeras på baksidan av smarttelefonen för att avslöja en skärm där du kan kontrollera detaljerna i dina transaktioner innan du signerar dem med den dedikerade knappen.


![Image](assets/fr/01.webp)


Portalen, som är helt öppen källkod, är baserad på firmware skriven i Rust och använder BDK (Bitcoin Dev Kit) för nyckel- och transaktionshantering. Den säljs för €89 [på den officiella webbplatsen] (https://store.twenty-two.xyz/products/portal-hardware-Wallet).


I skrivande stund är portalen kompatibel med applikationerna Nunchuk och Bitcoin Keeper. I denna handledning kommer vi att konfigurera den med Nunchuk.


## Uppackning


När du får din portal ska du kontrollera att lådan och etiketten som förseglar den är i gott skick. På insidan hittar du din portal i en förseglad påse.


Se till att Seal är intakt för att bekräfta att påsen inte har öppnats. Det unika numret som visas med stora bokstäver på påsen ska motsvara det som står skrivet i svart under den blå Seal, det som står på etiketten på lådan och det som visas på skärmen när du startar för första gången.


![Image](assets/fr/02.webp)


## Installation av Nunchuk


För att hantera Wallet på portalen kommer vi att använda Nunchuk-applikationen. Ladda ner applikationen från [Google Play Store] (https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store] (https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) eller direkt via dess [fil `.apk`] (https://github.com/nunchuk-io/nunchuk-android/releases).


![Image](assets/fr/03.webp)


Om du använder Nunchuk för första gången kommer programmet att uppmana dig att skapa ett konto. I den här handledningen är det inte nödvändigt att skapa ett konto. Välj "*Fortsätt som gäst*" för att fortsätta utan konto.


![Image](assets/fr/04.webp)


## Konfiguration av portalen


På startskärmen för Nunchuk klickar du på "*NFC*"-logotypen längst upp på skärmen.


![Image](assets/fr/05.webp)


Placera din Portal på baksidan av din smartphone för att aktivera den.


![Image](assets/fr/06.webp)


Nunchuk kommer att känna igen din portal. Klicka sedan på "*Continue*".


![Image](assets/fr/07.webp)


För att skapa en ny Wallet, välj "*generate seed on Portal*" och klicka sedan på "*Continue*".


![Image](assets/fr/08.webp)


Du kan välja mellan en Mnemonic-fras på 12 eller 24 ord. De båda alternativen ger samma säkerhet, så du kan välja det som är enklast att spara, dvs. 12 ord.


![Image](assets/fr/09.webp)


Du kommer sedan att bli ombedd att välja ett lösenord. Lösenordet låser upp din portal. Det ger därför skydd mot obehörig fysisk åtkomst. Detta lösenord är inte involverat i härledningen av din Wallet:s kryptografiska nycklar. Så även utan tillgång till detta lösenord kan du få tillgång till dina bitcoins om du har din Mnemonic-fras på 12 eller 24 ord. Det är tillrådligt att välja ett lösenord som är så slumpmässigt som möjligt och tillräckligt långt. Se till att du sparar detta lösenord på en annan plats än där din portal lagras (t.ex. i en lösenordshanterare).


![Image](assets/fr/10.webp)


Din portal kommer att visa din Mnemonic-fras på 12 ord. Denna Mnemonic ger dig full, obegränsad tillgång till alla dina bitcoins. Alla som har tillgång till denna fras kan stjäla dina pengar, även utan fysisk tillgång till din portal.


Den 12-ordiga frasen återställer åtkomsten till dina bitcoins i händelse av förlust, stöld eller brott på din portal. Det är därför mycket viktigt att spara den noggrant och förvara den på en säker plats.


Du kan gravera den på ett papper, eller för extra säkerhet rekommenderar jag att du graverar den på en bas av rostfritt stål för att skydda den mot brand, översvämning eller kollaps.


För mer information om det rätta sättet att spara och hantera din Mnemonic-fras rekommenderar jag starkt att du följer den här andra handledningen, särskilt om du är nybörjare:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

du får naturligtvis aldrig dela med dig av dessa ord på Internet, vilket jag gör i den här handledningen. Detta prov Wallet kommer endast att användas på Testnet och kommer att raderas i slutet av handledningen.**_


Tryck hårt på knappen på din Portal för att gå vidare till nästa ord. Se till att placera hela fingret på knappen och håll trycket i några sekunder, så att interaktionen upptäcks korrekt.


![Image](assets/fr/11.webp)


Din portal kommer då att bekräfta det lösenord som du angav i Nunchuk.


![Image](assets/fr/12.webp)


Du är nu klar med att konfigurera din portal och skapa din Mnemonic-fras!


![Image](assets/fr/13.webp)


## Bitcoin Wallet konfiguration


Klicka på "*Continue*" på Nunchuk samtidigt som du håller din Portal mot baksidan av telefonen.


![Image](assets/fr/14.webp)


I den här handledningen kommer jag att konfigurera en Wallet med enkelsigg, så jag väljer det här alternativet.


![Image](assets/fr/15.webp)


Använd standardkontot, dvs. det första kontot i Wallet (nummer 0). Nunchuk kommer sedan att be dig bekräfta ditt portallösenord för att låsa upp den.


![Image](assets/fr/16.webp)


På portalen bekräftar du exporten av din xpub till Nunchuk. Detta gör att du kan hantera Wallet från din smartphone utan att kunna spendera bitcoins utan portalen. Tryck på knappen för att bekräfta.


Observera att den härledningsväg som anges i ditt fall kommer att skilja sig från min, eftersom denna handledning utförs på Testnet.


![Image](assets/fr/17.webp)


Namnge din Wallet, till exempel "*Portal*", och klicka sedan på "*Fortsätt*".


![Image](assets/fr/18.webp)


Nunchuk ger dig sedan din Descriptor. Det är en bra idé att göra en säkerhetskopia. Även om Descriptor inte tillåter dig att spendera bitcoins, tillåter den dig att spåra härledningsvägarna för dina nycklar från din Mnemonic-fras i händelse av Wallet-återställning. Förvara den på en säker plats, för även om läckage inte utgör ett säkerhetsproblem, utgör det en sekretessfråga.


Klicka på "*Done*".


![Image](assets/fr/19.webp)


Du måste nu generate de publika nycklarna för din Bitcoin Wallet. För att göra detta klickar du på knappen "*Create new Wallet*".


![Image](assets/fr/20.webp)


Klicka igen på "*Skapa ny Wallet*". Välj sedan alternativet "*Skapa en ny Wallet med hjälp av befintliga nycklar*".


![Image](assets/fr/21.webp)


Välj ett namn för din Wallet och klicka på "*Fortsätt*".


![Image](assets/fr/22.webp)


Välj din portal som signeringsenhet för den nya nyckeluppsättningen och klicka sedan på "*Continue*".


![Image](assets/fr/23.webp)


Om allt är till belåtenhet validerar du skapelsen.


![Image](assets/fr/24.webp)


Du kan sedan spara din Wallet-konfigurationsfil. Den här filen innehåller endast dina publika nycklar, vilket innebär att även om någon kommer åt den kommer de inte att kunna stjäla dina bitcoins. De kommer dock att kunna spåra alla dina transaktioner. Den här filen utgör därför endast en risk för din integritet. I vissa fall kan den vara oumbärlig för att återfå dina Wallet.


![Image](assets/fr/25.webp)


Och det är allt som behövs!


![Image](assets/fr/26.webp)


## Hur kan jag ta emot bitcoins med Portal?


För att ta emot bitcoins, välj din Wallet.


![Image](assets/fr/27.webp)


Innan du använder den genererade Address ska du kontrollera den på Portal-skärmen. För att göra detta, klicka på "*Receive*".


![Image](assets/fr/28.webp)


Klicka på de tre prickarna och välj sedan "*Verifiera Address via PORTAL*". Ange sedan ditt lösenord.


![Image](assets/fr/29.webp)


Placera din Portal på baksidan av telefonen och bekräfta sedan genom att trycka på knappen.


![Image](assets/fr/30.webp)


Kontrollera att den Address som visas på portalen stämmer överens med den som finns på din Nunchuk och bekräfta sedan genom att trycka på knappen igen. Om adresserna är identiska kan du ge denna Address till betalaren.


![Image](assets/fr/31.webp)


När betalarens transaktion har sänts ser du den på din Wallet.


![Image](assets/fr/32.webp)


Klicka på "*Visa hörn*".


![Image](assets/fr/33.webp)


Välj din nya UTXO.


![Image](assets/fr/34.webp)


Klicka på "*+*" bredvid "*Tags*" för att lägga till en tagg till din UTXO. Detta är en bra praxis, eftersom det hjälper dig att komma ihåg var dina mynt kommer ifrån och optimerar din integritet när du spenderar i framtiden.


![Image](assets/fr/35.webp)


Välj en befintlig tagg eller skapa en ny och klicka sedan på "*Spara*". Du kan också skapa "*samlingar*" för att organisera dina delar på ett mer strukturerat sätt.


![Image](assets/fr/36.webp)


## Hur skickar jag bitcoins med hjälp av Portal?


Nu när du har bitcoins i din Wallet kan du också skicka dem. För att göra det klickar du på den Wallet du vill ha.


![Image](assets/fr/37.webp)


Klicka på knappen "*Sänd*".


![Image](assets/fr/38.webp)


Välj det belopp som ska skickas och klicka sedan på "*Fortsätt*".


![Image](assets/fr/39.webp)


Lägg till en "*not*" i din framtida transaktion för att påminna dig om dess syfte.


![Image](assets/fr/40.webp)


Ange sedan mottagarens Address i det fält som finns. Du kan också skanna en Address som är kodad som en QR-kod genom att klicka på ikonen längst upp till höger på skärmen. Klicka sedan på knappen "*Create Transaction*".


![Image](assets/fr/41.webp)


Kontrollera dina transaktionsuppgifter och klicka sedan på knappen "*Signera*" bredvid din portal och ange ditt lösenord.


![Image](assets/fr/42.webp)


Placera din Portal på baksidan av din telefon. Kontrollera att mottagarens Address och beloppet är korrekta. Om så är fallet, tryck på knappen för att fortsätta.


![Image](assets/fr/43.webp)


Kontrollera att transaktionsavgiften är korrekt och tryck sedan på knappen igen för att signera transaktionen.


![Image](assets/fr/44.webp)


Din transaktion har undertecknats. Du kan kontrollera detaljerna en sista gång på Nunchuk och sedan klicka på knappen "*Broadcast transaction*" för att sända den på Bitcoin-nätverket.


![Image](assets/fr/45.webp)


Din transaktion väntar nu på bekräftelse.


![Image](assets/fr/46.webp)


Grattis, du har nu fått kläm på hur du använder Portal! Om du tyckte att denna handledning var användbar skulle jag vara tacksam om du lämnade en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!


Om du vill veta mer kan du ta en titt på vår kompletta utbildning om hur HD-plånböcker fungerar:


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f