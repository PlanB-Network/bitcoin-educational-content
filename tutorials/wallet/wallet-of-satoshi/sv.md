---
name: Wallet of Satoshi
description: Den enklaste depån Wallet för att komma igång
---
![cover](assets/cover.webp)

_Den här handledningen skrevs av_ [Bitcoin Campus] (https://linktr.ee/bitcoincampus_)


## Ladda ner, konfigurera och använda Wallet eller Satoshi


Wallet av Satoshi är en Lightning Network Wallet, custodial, och mycket enkel att använda.

I kursen [BTC105 - Finding Now] (https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5) används den för att ange Redeem Lightning Network vouchers.


**Kom alltid ihåg**: _inte dina nycklar, inte dina mynt_


Förvaringsplånböcker tillåter inte användare full kontroll över sina medel. De rekommenderas normalt inte, förutom för nybörjare. WoS bör användas som en övergångs-Wallet eller för att hålla fickpengar, inte för långsiktig fondackumulering.


---

Wallet of Satoshi (WoS) är en depåprodukt, men den har ett visst rykte. Vi kan rimligen vända oss till ett verktyg som WoS, till exempel för att öka vår förmåga att ta emot likviditet. Vi delegerar tillfälligt till WoS det "smutsiga arbetet" att hantera likviditeten i kanalerna åt oss. När ett visst belopp har uppnåtts kommer vi att tömma WoS On-Chain till vår icke-frihetsberövande Wallet.


**WARNING⚠️: Vi rekommenderar att du läser hela handledningen innan du fortsätter**


### Nedladdning av Wallet av Satoshi


Gå till Play Store och ladda ner WoS


![image](assets/it/01.webp)


**WoS laddas endast ner från officiella butiker. Om enhetens operativsystem är programmerat, innan WoS öppnas, finns det en verifieringsdel av operativsystemet självt. Efter verifieringsfasen väljer du** _Open_.


![image](assets/it/02.webp)


Wallet av Satoshi öppnas med följande skärm, och det är nödvändigt att klicka på _Start_


![image](assets/it/03.webp)


### Registrera ett konto för WoS


Vid denna tidpunkt är Wallet redan i drift, men för större säkerhet fortsätter vi med att ställa in en inloggning: den kommer att behövas för att återställa medel i händelse av funktionsfel eller förlust av enheten. Välj därför menyn längst upp till vänster.


![image](assets/it/04.webp)


Hela menyfönstret öppnas, där du endast måste ställa in valutan (Wallet av Satoshi presenterar som standard US-dollar som referensvaluta) och temafärgen (ljus/mörk), enligt smak. Använd inte de andra kommandona.


Eftersom WoS är ett förvaringsverktyg kan vi inte säkerhetskopiera Wallet med Mnemonic frasen, men vi kan göra det möjligt för WoS att återfå våra medel, i händelse av förlust eller icke-användning av den mobila enheten, genom att klicka på _Login/Register_

Ett fönster visas där vi uppmanas att ange ett e-postmeddelande Address. Det kan vara **en Proton-mail** (rekommenderas), men den måste vara funktionell, eftersom den kommer att göra det möjligt för oss att återfå pengarna i Wallet i händelse av förlust/stöld eller skada på mobiltelefonen.


![image](assets/it/08.webp)


Wallet från Satoshi har skickat ett meddelande till den angivna e-postinkorgen.


![image](assets/it/09.webp)


I brevlådan hittar vi två ord, som vi måste skriva in, skriva om dem, i det utrymme som tillhandahålls av appen.


- aktivera inte översättaren: orden är och måste förbli på **engelska**
- skriva om de två orden med hänsyn till versaler/gemener


![image](assets/it/10.webp)


När du har transkriberat de två orden klickar du på _OK_.


![image](assets/it/11.webp)


Resultatet bör vara en bild som visas högst upp, med bocksymbolen för verifiering.


![image](assets/it/12.webp)


i inställningsavsnittet visar det röda fältet _Login/Register_ nu användarens e-post Address.


![image](assets/it/13.webp)


### Mottagande av betalningar


För att ta emot på WoS, klicka på _Receive_ och en rad kommandon kommer att visas.


![image](assets/it/14.webp)


Du kan få


- via LN-Address **a**
- via LN, genom att ställa in Invoice **b**
- on chain (WoS stöder Bitcoin-nätverket men med betalda ubåtsbyten) **c**
- genom att skanna QR-koden på en LNurl-p **d**


![image](assets/it/15.webp)


### Skapa en Invoice


Klicka på _Receive_ och välj kommandot med symbolen Lightning Network.


![image](assets/it/16.webp)


Menyn för att skapa en Invoice visas, där vi klickar på _Add Amount_ för att skriva det exakta beloppet och lägga till en beskrivning, i det här exemplet "Min första Invoice".


![image](assets/it/17.webp)


Med tangentbordet ställer vi in beloppet.


![image](assets/it/18.webp)


för att sedan få betalt Invoice. Den mottagna betalningen ser ut så här:


![image](assets/it/19.webp)


### Avhämtning från POS


Wallet av Satoshi har en standardfunktion, vilket gör den särskilt lämplig för handlare: POS. Låt oss se hur du aktiverar den.


Välj menyn längst upp till höger på huvudskärmen.


![image](assets/it/20.webp)


Välj sedan _Point of Sale_.


![image](assets/it/21.webp)


Med den senaste versionen av WoS, se till att välja _Keypad_.


![image](assets/it/22.webp)

och skriv sedan in beloppet på knappsatsen, i exemplet som följer lika med 10 cent / 118 Sats. Lägg till en beskrivning för insamlingen, i det här fallet "min andra med POS". En stor Green-knapp tänds, och den ska klickas på

![image](assets/it/23.webp)


till generate Invoice och visa den - till exempel - för en kund.


![image](assets/it/24.webp)


Denna betalning är också inkasserad!


![image](assets/it/25.webp)


### Skicka betalningar


Enkelhet är en styrka hos WoS huvudskärm. För att betala en Invoice, klicka på _Send_


![image](assets/it/26.webp)


Vid första användningen ber WoS om tillstånd för att komma åt kameran


![image](assets/it/27.webp)


Från detta ögonblick aktiveras kameran


![image](assets/it/28.webp)


Med Invoice som ram ser vi att en betalning på 210 Sats har begärts. En beskrivning läses också, om beställaren har angett en sådan. Denna skärm är sammanfattningen och också en begäran om bekräftelse: WoS "ber om auktorisation" för att skicka betalningen, vilket beviljas genom att klicka på Green _Send_-knappen


![image](assets/it/29.webp)


När betalningen når sin destination meddelar WoS detta med denna skärm


![image](assets/it/30.webp)


Om du klickar på _Historik_ (precis under saldot) på huvudskärmen visas en lista över transaktioner


![image](assets/it/31.webp)


#### Återställning av WoS-kontot


Nu ska vi se hur man installerar WoS på en ny enhet; detta kommer också att vara användbart vid stöld, förlust eller oförmåga att använda mobiltelefonen som Wallet tidigare installerades på. När du har installerat om måste du göra om kontoregistreringsproceduren som just förklarats, med en enda variant: i slutet av begäran om att logga in med den tidigare inställda e-postadressen kommer WoS att se ut så här:


![image](assets/it/33.webp)


Ett meddelande varnar oss för att ett e-postmeddelande har skickats med proceduren för att återaktivera kontot. Du måste öppna din e-postinkorg.


** VIKTIGT**: öppna e-postmeddelandet från en dator eller i alla fall från en annan enhet än den som du håller på att återställa WoS-kontot på. I inkorgen hittar vi ett meddelande som visar oss en QR-kod för att rama in


![image](assets/it/34.webp)


När QR-koden är inramad kommer det återställda kontot att visas på WoS huvudsida, med saldo och historik.