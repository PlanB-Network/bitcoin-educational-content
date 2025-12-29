---
name: Alby

description: Webbläsartillägg för Bitcoin och Lightning Network
---

![cover](assets/cover.webp)




Att göra betalningar allt enklare med bitcoin är den utmaning som många företag i sektorn står inför. Alby sticker ut från mängden med sitt Alby wallet-tillägg för webbläsare. Detta tillägg syftar till att sätta upp ett flytande ramverk som automatiskt upptäcker adresser och låter dig göra friktionsfria bitcoinbetalningar. I denna handledning upptäcker vi Alby-tillägget och testar hur det underlättar betalningar från webbläsaren.




![video](https://youtu.be/nd5fX2vHuDw)




## Alby förlängning



Alby-tillägget är ett verktyg som gör det möjligt för din webbläsare att enkelt och säkert interagera med Bitcoin-nätverket och dess Lightning Network-lager. Det kännetecknas av tre aspekter:




- Lightning Network wallet: Länka din Alby-nod eller ditt Alby-konto för att skicka och ta emot bitcoin snabbt och billigt via Lightning Network-lagret.
- Vätskebetalningar via webben: Det eliminerar behovet av att skanna QR-koder eller växla mellan applikationer för bitcoinbetalningar på webbplatser som stöder Lightning. Det möjliggör smidiga transaktioner med ett enda klick, eller utan bekräftelse om du har satt en budget.
- En Nostr-hanterare: Tillägget hanterar dina Nostr-nycklar, vilket gör det enkelt att ansluta och interagera med Nostr-applikationer som fungerar som en säker undertecknare utan att exponera din privata nyckel för varje plattform.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Anslut till förlängningen



I den här handledningen kommer vi att använda tillägget Alby i webbläsaren Firefox under ett Ubuntu-operativsystem. Det är dock också tillgängligt på Windows och med webbläsare som Chrome.



Du kan lägga till Alby-tillägget i din webbläsare genom att besöka [Firefox]-tilläggsbutiken (https://addons.mozilla.org/fr/firefox/addon/alby/) eller [Chrome]-tilläggsbutiken (https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ Det är viktigt att kontrollera att författaren till tillägget verkligen är det officiella Alby-kontot, för att undvika någon form av piratkopiering eller stöld av dina bitcoins.



Lägg till tillägget i din webbläsare genom att klicka på knappen till höger.


Ge de nödvändiga behörigheterna för att installera och använda tillägget och fäst sedan tillägget i verktygsfältet så att det är lätt att hämta.



![pin](assets/fr/03.webp)



Du bör också definiera en upplåsningskod (mycket viktigt), som garanterar säker åtkomst till din Lightning wallet från din webbläsare. Vi föreslår att du anger ett starkt alfanumeriskt lösenord.



ℹ️ Spara lösenordet på en säker plats så att du kan komma åt det om du glömmer det, eftersom det kan ändras men inte återställas.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby visar sin anpassningsförmåga genom att erbjuda dig två val:




- Fortsätt med ett Alby-konto om du vill njuta av applikationerna samtidigt som du behåller kontrollen över dina bitcoins.
- Anslut din egen wallet- eller Lightning-nod om du redan har en som stöds av tillägget.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


I den här handledningen väljer vi att fortsätta med Alby-kontot för att dra nytta av funktionerna i Alby-ekosystemet.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Logga in på ditt Alby-konto, eller skapa ett om du inte har något ännu.



![signup](assets/fr/05.webp)



## Gör dina första betalningar



När du är inloggad kan du klicka på tillägget Alby i verktygsfältet för att komma åt din portfölj.



![buzzin](assets/fr/06.webp)



När du har skapat ditt Alby-konto måste du ansluta det till en wallet för att kunna spendera satoshis. För att länka bitcoin wallet till ditt Alby-konto föreslår vi att du använder en Alby Hub-nod, som du antingen kan installera på din dator eller prenumerera på en plan som erbjuds av Alby.



![hubplan](assets/fr/13.webp)




I den här handledningen stöds vårt Alby-konto av en lokal installation på vår maskin.


För att bygga din egen Alby-nod rekommenderar vi vår Alby Hub-handledning.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Med den här noden kan du skapa självförvaltande Lightning-portföljer och effektivt hantera dina Lightning-kanaler för att skicka och ta emot satoshis.



![channels](assets/fr/14.webp)



Öppna mottagningskanaler som definierar det totala antalet satoshis du kan ta emot.



![receivechanal](assets/fr/15.webp)



Öppna sändningskanaler genom att blockera satoshis på en bitcoin onchain-adress. De satoshis som du har blockerat definierar det totala antalet satoshis som du kan spendera.



![spend](assets/fr/16.webp)



Du kan nu skicka och ta emot satoshis via tillägget Alby.



![exchange](assets/fr/08.webp)



Från och med nu kan Alby-tillägget upptäcka Lightning-adresser och fakturor som finns på de webbsidor du besöker, och kommer att föreslå att du betalar dem i bitcoin eller Lightning direkt från ditt tillägg.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Säkra återställningsnycklar med huvudnyckeln



Huvudnyckeln som erbjuds av Alby-tillägget fungerar som ett skyddande överlägg som gör att du kan kommunicera säkert med det huvudsakliga Bitcoin-nätverkslagret (Onchain), Nostr-systemet och gör att du kan aktivera Lightning-anslutningen med Nostr-applikationer.



![masterKey](assets/fr/11.webp)



Denna huvudnyckel består av 12 ord som liknar din återställningsfras. Vi rekommenderar därför att du förvarar den på ett säkert sätt så att du alltid kan komma åt den.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Du kan nu uppleva friktionsfria bitcoin- och Lightning-betalningar med tillägget Alby. Om du gillade den här handledningen rekommenderar vi vår Alby Hub-handledning för att sätta upp din egen Alby-nod och kontrollera alla aspekter av dina Alby-plånböcker från ett smidigt och kraftfullt gränssnitt.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a