namn: NOSTR

beskrivning: Upptäck och börja använda NOSTR
---

# Hur man använder Nostr år 2023: En guide för nybörjare

Vid slutet av denna guide kommer du att förstå vad Nostr är, du kommer att ha skapat ett konto och du kommer att kunna använda det.

![En ny utmanare har anlänt](assets/1.jpeg)

## Vad är Nostr?

Nostr är en protokoll som har förmågan att ersätta Twitter, Telegram och andra sociala medier. Det är ett enkelt öppet protokoll som kan skapa en globalt motståndskraftig social nätverk en gång för alla.

## Hur fungerar det?

Nostr bygger på tre komponenter: nyckelpar, klienter och reläer.

Varje användare har en eller flera identiteter, varje identitet bestäms av ett kryptografiskt nyckelpar.

För att få tillgång till nätverket måste du använda en klientprogramvara och ansluta till reläer för att ta emot och skicka innehåll.

![Nyckelsystem](assets/2.jpeg)

## 1. Kryptografiska nycklar

Till skillnad från Facebook eller Twitter där användaren måste ange en e-postadress och massor av information till ett privat företag, fungerar Nostr utan en central myndighet. Användaren genererar ett kryptografiskt nyckelpar, en hemlig nyckel (även kallad privat nyckel) och en offentlig nyckel.

Den hemliga nyckeln, nsec, som bara användaren känner till, används för autentisering och publicering av innehåll.

Den offentliga nyckeln, npub, är en unik identifierare som allt innehåll som publiceras av en användare är kopplat till. Din offentliga nyckel är en slags användarnamn som gör att andra användare kan hitta dig och prenumerera på ditt Nostr-flöde.

## 2. Klienter

Klienter är programvaror som gör det möjligt att interagera med Nostr. De främsta klienterna är:

> iOS: damus
> Android: amethyst
> Web: iris.to; snort.social; astral.ninja

Klienterna gör det möjligt för en användare att generera ett nytt nyckelpar (motsvarande att skapa ett konto) eller att autentisera sig med ett befintligt nyckelpar.

## 3. Reläer

Reläerna är enkla servrar som du kan överge när som helst om du inte gillar det innehåll de skickar till dig. Du kan också köra din egen relä om du vill.

> 💡 Proffstips: Betalda reläer är vanligtvis effektivare för att filtrera skräppost och oönskat innehåll.

# Guide

Nu vet du tillräckligt om Nostr för att komma igång och skapa din första identitet på detta protokoll.

För denna guide kommer vi att använda iris.to (https://iris.to/) eftersom denna webbklient fungerar på alla plattformar.

## Steg 1: Generera nycklar
ris kommer att skapa en nyckelspel åt dig utan att du behöver göra något mer än att ange ett namn (verkligt eller fiktivt) för din profil. Klicka sedan på GO och det är klart!
![Huvudmeny](assets/3.jpeg)

> ⚠️ Observera! Du måste hålla reda på dina nycklar om du vill kunna komma åt din profil igen efter att din session har avslutats. Jag kommer att visa dig hur i slutet av den här guiden.

## Steg 2: Publicera innehåll

För att publicera innehåll är det lika enkelt och intuitivt som att skriva några ord i publiceringsfältet.

![Publicering](assets/4.jpeg)

Det är klart! Du har publicerat ditt första inlägg på Nostr.

![Inlägg](assets/5.jpeg)

## Steg 3: Hitta en vän

Hitta mig på Nostr och var aldrig ensam igen. Jag prenumererar tillbaka på alla som prenumererar på mitt flöde. För att göra detta behöver du bara ange min publika nyckel

npub1hartx53w6t3q5wv9xdqdwrk7h6r5866t8u775q0304zedpn5zgssasp7d3 i sökfältet.

![Min profil](assets/6.jpeg)

Klicka på "follow" och inom några dagar kommer jag också att prenumerera på ditt flöde. Vi kommer att vara vänner. Jag ser också fram emot att läsa ditt meddelande om du vill skicka ett.

Slutligen, se också till att prenumerera på Agora256-flödet för att få en notis varje gång vi publicerar något nytt: npub1ag0rawstycy7nanuc6sz4v287rneen2yapcq3fd06972f8ncrhzqx

## Steg 4: Anpassa din profil

Det finns fortfarande lite arbete kvar för att anpassa din profil. För att göra detta, klicka på avatarbilden som Iris har genererat åt dig i det övre högra hörnet av skärmen och klicka sedan på "edit profil".

![Profil](assets/7.jpeg)

Du behöver bara ange var Iris kan hitta din profilbild och banner på internet. Jag rekommenderar att du själv hostar ditt innehåll: skydda det som är ditt.

![Annat alternativ](assets/8.jpeg)

Om du föredrar kan du också ladda upp bilder som kommer att lagras åt dig av Iris på nostr.build, en gratis tjänst för visuellt innehållshosting för Nostr.

Som du kan se kan du också konfigurera din klient för att kunna ta emot och skicka sats. På så sätt kan du belöna författare till innehåll du gillar eller ännu bättre, samla sats själv för det fantastiska innehåll du kommer att publicera.

## Steg 5: Säkerhetskopiera nyckelparet

Detta steg är avgörande om du vill behålla åtkomsten till din profil efter att du har loggat ut från klienten eller om din session har löpt ut.
Först, klicka på "inställningar" -ikonen som representeras av en kugghjul
![Inställningar](assets/9.jpeg)

Sedan, kopiera och klistra in dina npub, npub hex, nsec och nsec hex en efter en i en textfil som du håller säker. Jag rekommenderar att du krypterar denna fil om du vet hur man gör det.

![Nyckel](assets/10.jpeg)

> ⚠️ Observera varningen som iris ger dig. Du kan dela din publika nyckel utan oro, men det är en helt annan sak med din privata nyckel. Den som har den kan få tillgång till ditt konto.

## Slutsats

Nu har du, lilla struts, tagit dina första steg på Nostr. Nu måste du lära dig att springa som en blixt. Vi kommer snart att publicera guider som visar dig hur du hanterar dina nycklar och hur du integrerar belysning i din Nostr-upplevelse med hjälp av getalby.