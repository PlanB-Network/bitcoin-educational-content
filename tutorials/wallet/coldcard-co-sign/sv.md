---
name: COLDCARD - Medsignera
description: Upptäck Co-Sign-funktionen och använd den på ditt COLDCARD
---

![cover](assets/cover.webp)


*OBS: Denna handledning riktar sig till personer som redan har viss erfarenhet av multisignaturplånböcker, Coinkite-enheter och programvara som Sparrow wallet eller Nunchuk.*



![video](https://youtu.be/MjMPDUWWegw)




**Varför ColdCard Co-Sign?



Med den här funktionen kan du lägga till **utgiftsvillkor** till din ColdCard-enhet (Q eller Mk4) på samma sätt som en hårdvarusäkerhetsmodul (HSM), för att skydda dina pengar samtidigt som du behåller betydande flexibilitet och kontroll över dem.



Utgiftsvillkor kan till exempel vara:





- Gränser för magnitud**: Begränsa mängden bitcoins du kan spendera i en enda transaktion.
- Velocity limits:** bestämmer hur många transaktioner du kan genomföra per tidsenhet (per timme, dag, vecka etc.), vilket kräver ett minsta antal block mellan dem.
- Förhandsgodkända adresser:** Tillåt endast att bitcoins skickas till förhandsgodkända adresser.
- Tvåfaktorsautentisering:** Kräver bekräftelse från en mobil 2FA-applikation från tredje part (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) på en NFC-aktiverad smartphone/surfplatta med internetåtkomst.



**Hur det fungerar



Genom att lägga till en andra seed till din ColdCard Mk4- eller Q-enhet, kallad "Spending Policy Key", som vi kommer att hänvisa till i hela denna handledning som "C Key".


Förutom denna ytterligare seed kommer du att bli ombedd att Supply minst en ytterligare nyckel (XPUB), som vi kallar en "Backup Key", för att skapa en Wallet Multisig 2-on-N.



Sammanfattningsvis ska vi skapa en Wallet Multisig, och din ColdCard-enhet kommer att innehålla två av de privata nycklar som behövs för att spendera pengarna, enhetens seed-master och "Spending Policy Key".



Varje gång "C Key" ombeds att signera gäller de angivna utgiftsvillkoren och ColdCard signerar endast om transaktionen uppfyller villkoren.



Om du vill avstå från dessa utgiftsvillkor kan du göra det:




- genom att signera med en av reservnycklarna och seed-handen, eller 2 reservnycklar beroende på storleken på din Multisig.
- genom att ange "Spending Policy Key" eller "C Key" i menyn "Co-Sign". **Den senare kan inte användas direkt på enheten, eftersom vem som helst annars skulle kunna avbryta de utgiftsvillkor som har konfigurerats




## Konfigurering av ColdCard Co-Sign



![video](https://youtu.be/MjMPDUWWegw)



### 1- Aktivera funktionalitet



Kontrollera först och främst att din enhet har minst den senaste firmwareversionen:




- Mk4: v5.4.2
- Q: v1.3.2Q




På din Mk4 eller ColdCardQ går du till *Avancerade verktyg > ColdCard Co-Signing*.



![Co-Sign](assets/fr/01.webp)



*I följande handledning kommer skärmdumpar att tas på en ColdCardQ för enkelhetens skull, men stegen och menyerna är identiska mellan Mk4 och Q.*



En sammanfattning av funktionaliteten visas.


Den terminologi som används för att beteckna nycklarna, och som vi kommer att använda igen i den 2-mot-3-multisignatur Wallet som vi ska skapa, är följande:



Nyckel A = Coldcard master seed


Nyckel B = Säkerhetsknapp


Nyckel C = Nyckel för utgiftspolicy



Klicka på **"ENTER"**.



![Co-Sign](assets/fr/02.webp)



Nästa steg är att bestämma vilken privat nyckel som ska fungera som "Spending Policy Key" eller "Key C".



Vi kan se att vi har flera alternativ öppna för oss:





- Eller tryck på **"ENTER"** för att generate en ny seed mening med 12 ord.





- Klicka antingen på **"(1)"** för att importera en befintlig 12-ords seed, eller välj **"(2)"** för att importera en befintlig 24-ords seed.





- Eller tryck **"(6)"** för att importera en seed från din enhets valv.



För denna handledning har vi beslutat att importera en befintlig seed med 12 ord genom att trycka på **"(1)"**. Detta kan vara vilken seed BIP39 som helst som du redan äger, och som du uppenbarligen har en säkerhetskopia för.



Använd ditt tangentbord för att ange de 12 orden i din seed. I det här exemplet väljer vi seed:s giltiga fras biff x 12. Tryck sedan på **"ENTER"**.


*OBS: Om du inte har en säkerhetskopia av denna seed kommer du inte längre att kunna ändra inställningarna för "Co-Sign" på din enhet för att ändra dina utgiftsvillkor*



Funktionen "Co-Sign" är nu aktiverad på enheten. Därefter måste vi välja våra utgiftsvillkor och sedan slutföra skapandet av Wallet med flera signaturer.



![Co-Sign](assets/fr/03.webp)



### 2- Välj utgiftsvillkor eller "*utgiftspolitik*"



Här anger vi de utgiftsvillkor som måste uppfyllas när **"C Key"** eller **"Spending Policy Key**" signerar en transaktion.



I menyn **"Co-Signing"** klickar du på **"Spending Policy**".



Du kan sedan välja den maximala magnituden, dvs. det maximala antalet satoshis som kan spenderas i en enda transaktion.



I det här exemplet väljer vi en maximal magnitud på **21212** satoshis. Klicka på **"ENTER"** för att bekräfta.




![Co-Sign](assets/fr/04.webp)



Vi väljer sedan att ställa in den maximala hastigheten, dvs. det antal transaktioner som enheten ska kunna signera per tidsenhet. I den här handledningen väljer vi obegränsad hastighet, dvs. ingen begränsning av antalet transaktioner.




![Co-Sign](assets/fr/05.webp)



### 3- Skapa Wallet Multisig 2-mot-N



Vi måste fortfarande välja den tredje nyckeln för vår Wallet Multisig, dvs. **"Backup Key"** (Nyckel B), utöver enhetens **master seed** (Nyckel A) och **"Spending Policy Key"** (Nyckel C).



Vår "B-nyckel" måste importeras antingen via SD-kort eller via QR-kod i fallet med ColdCardQ.


För att göra detta behöver vi en andra ColdCard Mk4 eller Q-enhet, på vilken vår "Key B" används.



På den här andra enheten som innehåller din ** "Backup Key"**, säg en ColdCard Mk4 för detta exempel, gå från huvudmenyn till ** "Inställningar"**, sedan ** "Multisig Wallet"** och slutligen ** "Export Xpub"**.


(Om din andra enhet är en ColdCardQ har du naturligtvis möjlighet att exportera din Xpub via QR-kod).





![Co-Sign](assets/fr/06.webp)





På nästa skärm sätter du i ett SD-kort och klickar på knappen **"validate"** längst ned till höger. Klicka sedan på **"(1)"** för att spara filen på SD-kortet.



Filen innehåller fingeravtrycket för den publika nyckeln (*fingerprint*) i sitt namn och har formen `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Sätt sedan in SD-kortet i den "ursprungliga" ColdCardQ för att importera vår "Backup Key" (nyckel B).


I menyn "ColdCard Co-Signing" väljer du "Build 2-of-N", sedan klickar du på **"ENTER"** på nästa skärm och sedan igen **"ENTER"** för att importera "Backup Key" från SD-kortet.



![Co-Sign](assets/fr/08.webp)



På nästa skärm lämnar du "Account Number" tomt (om du inte vet exakt vad du gör) och klickar på **"ENTER"** igen.



![Co-Sign](assets/fr/09.webp)



Äntligen är vi redo att använda vår nya Wallet Multisig 2-sur-3, som är sammansatt enligt följande:



Nyckel A= Coldcard Q master seed


Nyckel B= Backup-nyckel (just importerad från en andra Coldcard-enhet)


Nyckel C= Spending Policy Key (om den används för att signera, inför fördefinierade utgiftsvillkor)



## Signera tillsammans med Sparrow wallet



Om det behövs kan du läsa igenom handledningarna nedan för att bekanta dig med Sparrow wallet-programvaran:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Export Wallet Multisig 2-sur-3 till Sparrow wallet



Vi behöver nu exportera våra Wallet Multisig till Sparrow så att vi kan placera våra första satoshis där.



Från huvudmenyn i din ColdCardQ väljer du **"Inställningar"** och sedan **"Multisig Plånböcker"**.


Uppsättningen av Multisig plånböcker som är kända för ditt ColdCard visas nu, med antalet nycklar som är inblandade här "2/3" (2-sur3). Välj Multisig **"ColdCard Co-Sign"** som vi just har skapat och klicka sedan på **"ColdCard Export"**.



![Co-Sign](assets/fr/10.webp)




Slutligen väljer du den metod som gör att du kan exportera Wallet till Sparrow. I vårt fall väljer vi SD-kort och klickar på **"(1)"** efter att ha satt in ett SD-kort i enhetens kortplats A.



![Co-Sign](assets/fr/11.webp)



I Sparrow wallet väljer du sedan "Importera Wallet".



![Co-Sign](assets/fr/12.webp)



Klicka sedan på **"Importera fil"**. Välj sedan filen **"export-Coldcard_Co-sign.txt"** på ditt SD-kort.



![Co-Sign](assets/fr/13.webp)



Ge din Wallet ett namn som den kommer att visas i Sparrow, och välj ett lösenord för att kryptera din Wallet (eller inte).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Vi är nu redo att ta emot våra första satoshis och testa de utgiftsvillkor som vi har tillämpat på vår Wallet.



![Co-Sign](assets/fr/16.webp)



### 2- Testa fördefinierade utgiftspolicyer



Som en påminnelse hade vi beslutat om en maximal magnitud på 21212 satoshis för vår Wallet Multisig. Detta innebar att varje gång Spending Policiy Key (Key C) signerade en transaktion, skulle den senare endast vara giltig om det spenderade beloppet var mindre än eller lika med 21212 satoshis.



Låt oss testa det.


Låt oss först klicka på fliken "Receive" i Sparrow och släppa några Satss på Wallet, som vi kommer att använda under hela denna handledning.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



Låt oss sedan försöka spendera mer än de 21212 tillåtna satoshierna genom att simulera en transaktion på 50 000 Sats.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Efter att ha skannat QR-koden som representerar den *osignerade* transaktionen med vår ColdCardQ för att importera transaktionen, är detta vad vi visas på skärmen. Ett varningsmeddelande talar om för oss att utgiftsvillkoren inte har uppfyllts. Om vi ändå signerar transaktionen kommer endast en av de två nycklarna (seed-mastern på enheten, men inte "Key C") att signera.




![Co-Sign](assets/fr/23.webp)



Här, efter att ha importerat vår transaktion till Sparrow, kan vi se att endast en av signaturerna har använts för transaktionen.



![Co-Sign](assets/fr/24.webp)




Låt oss nu upprepa experimentet, men för en transaktion på 21 000 satoshis, dvs. mindre än den maximala magnituden (21212 Sats) som vi satte för denna Wallet.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Låt oss försöka signera denna transaktion med vår ColdCardQ.



Inga problem den här gången, inget varningsmeddelande visas och när vi importerar den signerade transaktionen till Sparrow wallet har den här gången de två signaturerna använts, vilket gör transaktionen giltig och redo för distribution.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Signera tillsammans med Nunchuk



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Web 2FA & Vitlistade adresser



I det här stycket använder vi vår Wallet Multisig Co-Sign med Nunchuk och passar på att tillämpa nya utgiftsvillkor för att se hur det går.



Gå till *Avancerade verktyg > ColdCard Co-Signing*.


Vi ombeds att ange vår "Spending Policy Key" för att komma till menyn där vi kan ändra utgiftsvillkoren. I vårt fall anger vi 12 x "nötkött".



Vi har beslutat att hålla en magnitud på 21212 Sats och en maximal "Limit Velocity" av praktiska skäl relaterade till denna handledning. Å andra sidan kommer vi att använda menyn **"Whitelist Addresses"** för att införa de adresser som våra medel kan spenderas på.




![Co-Sign](assets/fr/31.webp)




Skanna QR-koderna som hör till de adresser (vi väljer 2) som du vill lägga till i din vitlista och klicka sedan på **"ENTER"**. Efter att ha validerat dina adresser genom att trycka på **"ENTER"** successivt ser vi att begränsningar av Magnitude- och mottagaradresser har tillämpats.



![Co-Sign](assets/fr/32.webp)



För att få en fullständig bild av de möjligheter som "Co-Sign" erbjuder ska vi slutligen aktivera alternativet "Web 2FA".


Med den här funktionen kan du använda en TOTP RFC-6238-kompatibel applikation som Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / eller Aegis Authenticator, för att lägga till en extra Layer av säkerhet.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

Konkret innebär det att innan du signerar en transaktion måste du föra din NFC-aktiverade, internetanslutna enhet nära ditt Coldcard. Då kommer du automatiskt till en webbsida på coldcard.com där du ombeds att ange den sexsiffriga koden för din applikation. Om du anger rätt kod kommer webbsidan att visa dig antingen en QR-kod att skanna för ColdCardQ, eller en 8-siffrig kod att ange på din Mk4, för att ge din enhet behörighet att signera.





![Co-Sign](assets/fr/33.webp)



När du har skannat QR-koden som visas i din applikation för dubbel autentisering och lagt till ditt ColdCard Co-Sign-konto (CCC) kommer du att bli ombedd att verifiera att allt är i sin ordning genom att ange din 2FA-kod.



Skriv in ditt ColdCard på baksidan av din NFC-enhet.



![Co-Sign](assets/fr/34.webp)



På den webbsida som öppnas anger du 2FA-koden för din favoritapplikation. Skanna sedan QR-koden som visas med din ColdCardQ (eller ange den 8-siffriga koden som visas i din Mk4).



![Co-Sign](assets/fr/35.webp)




Vi har nu infört en begränsning av magnitud (21212 Sats), destinationsadresser och dubbel autentisering.



![Co-Sign](assets/fr/36.webp)



### 2- Export Wallet Multisig 2-mot-3 till Nunchuk



Låt oss exportera Wallet Multisig 2-mot-3 till Nunchuk den här gången, som vi gjorde med Sparrow tidigare.


Gå till *Inställningar > Multisig Plånböcker > 2/3: ColdCard Co-sign > ColdCard Export*.



![Co-Sign](assets/fr/10.webp)



Den här gången väljer du NFC-alternativet för export genom att klicka på ColdcardQ-knappen med samma namn **"NFC"**.



![Co-Sign](assets/fr/37.webp)



Om du öppnar programmet för första gången i Nunchuk klickar du på **"Återställ befintlig Wallet"**.



![Co-Sign](assets/fr/38.webp)



Om du redan har en Wallet i programmet klickar du på **"+"** längst upp till höger och sedan på **"Återställ befintlig Wallet"**.



![Co-Sign](assets/fr/39.webp)




Välj sedan ** "Återställ Wallet från COLDCARD"** sedan ** "Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Slutligen trycker du på baksidan av din smartphone mot skärmen på din ColdCardQ för att importera Wallet via NFC.



![Co-Sign](assets/fr/41.webp)



Vårt konto och de satoshis som tidigare satts in via Sparrow wallet är tillbaka.



![Co-Sign](assets/fr/42.webp)



### 3- Testa fördefinierade utgiftspolicyer



Låt oss nu försöka göra en transaktion som bryter mot de två utgiftsvillkor vi har ställt. ** Vi försöker spendera mer än 21212 Sats till en Address som inte har godkänts.** Låt oss försöka skicka 22 222 Sats till en slumpmässig Address.



![Co-Sign](assets/fr/43.webp)



När transaktionen har skapats klickar du på de tre små prickarna i det övre högra hörnet för att exportera den till ditt ColdCard.



![Co-Sign](assets/fr/44.webp)



Välj sedan **"Exportera via BBQR"** och skanna QR-koden som visas med din ColdCardQ.



![Co-Sign](assets/fr/45.webp)



Ditt ColdcardQ visar sedan en varning som, när du skrollar längst ned på skärmen, klargör att transaktionen bryter mot utgiftsvillkoren, som förväntat.



**Observera att enheten inte berättar vilka utgiftsvillkor som är inblandade, för att förhindra att en potentiell angripare försöker kringgå begränsningarna.**




![Co-Sign](assets/fr/46.webp)



Om du fortfarande validerar genom att trycka på **"ENTER"** visas QR-koden som representerar den signerade transaktionen. Om du importerar den med Nunchuk kan du se att endast en signatur har använts.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Låt oss utföra exakt samma operation, men den här gången med en transaktion som respekterar magnitudgränsen (21212 Sats) och spenderar satoshis till en av de två adresser som vi har förkonfigurerat.



Vi skickar Nunchuk 12121 Sats till en av våra 2 adresser. Sedan exporterar vi transaktionen till vårt ColdCard som vi tidigare gjort.



![Co-Sign](assets/fr/49.webp)




Efter att ha importerat den osignerade transaktionen till vår ColdCardQ, låt oss se vad vi visas den här gången.



En varning är alltid närvarande, men den här gången, när vi rullar längst ner på skärmen, ser vi att det handlar om att validera transaktionen via 2FA. Enheten ber oss att föra vårt ColdcardQ nära vår internetanslutna NFC-terminal (smartphone eller surfplatta), vilket vi gör.



![Co-Sign](assets/fr/50.webp)



En webbsida öppnas på vår smartphone där vi uppmanas att ange vår 2FA-kod, vilket vi gör tack vare Proton Authenticator.



![Co-Sign](assets/fr/51.webp)





Skanna sedan QR-koden som visas på webbsidan för att ge ditt ColdCard behörighet att signera transaktionen.


Transaktionen är nu signerad av de två nycklarna och därmed giltig.



Om "Push Tx" är aktiverat på din ColdCardQ kan du sända transaktionen direkt till nätverket med en enkel tryckning på baksidan av din smartphone.



![Co-Sign](assets/fr/52.webp)




Om du inte har "Push tx" aktiverat kan du trycka på "QR"-knappen på ditt ColdCardQ för att visa den signerade transaktionen som en QR-kod och importera den till Nunchuk på samma sätt som i föregående exempel.



![Co-Sign](assets/fr/53.webp)



Den här gången ser vi att 2 signaturer har använts, så transaktionen är redo att sändas ut i Bitcoin-nätverket.



![Co-Sign](assets/fr/54.webp)




Vi har kommit till slutet av denna handledning, som ger dig en översikt över de möjligheter som erbjuds av Co-Sign-funktionen som är integrerad i Coinkites ColdCardQ- och Mk4-enheter, samt dess användning via plånböcker som Sparrow och Nunchuk.