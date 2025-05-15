---
name: NOSTR

description: Upptäck och börja använda NOSTR
---

I slutet av den här guiden kommer du att förstå vad Nostr är, du kommer att ha skapat ett konto och du kommer att kunna använda det.


![A new challenger has arrived](assets/1.webp)


## Vad är Nostr?


Nostr är ett protokoll som har kraften att ersätta Twitter, Telegram och andra sociala medieplattformar. Det är ett enkelt öppet protokoll som kan skapa ett globalt resistent socialt nätverk en gång för alla.


## Hur fungerar det?


Nostr bygger på tre komponenter: nyckelpar, klienter och reläer.


Varje användare har en eller flera identiteter, och varje identitet bestäms av ett kryptografiskt nyckelpar.


För att få tillgång till nätverket måste du använda klientprogramvara och ansluta till reläer för att ta emot och sända innehåll.


![Key system](assets/2.webp)


## 1. Kryptografiska nycklar


Till skillnad från Facebook eller Twitter, där användarna måste uppge en e-postadress Address och en mängd information till ett privat företag, fungerar Nostr utan en central myndighet. Användare generate ett kryptografiskt nyckelpar, en hemlig nyckel (även känd som en privat nyckel) och en offentlig nyckel.


Den hemliga nyckeln, nsec, som endast användaren känner till, används för autentisering och publicering av innehåll.


Den publika nyckeln, npub, är en unik identifierare som allt innehåll som publiceras av en användare är kopplat till. Din publika nyckel är som ett användarnamn som gör det möjligt för andra användare att hitta dig och prenumerera på ditt Nostr-flöde.


## 2. Kunder


Klienter är programvara som tillåter interaktion med Nostr. De viktigaste klienterna är:



- iOS: damus
- Android: ametist
- Webb: iris.to; snort.social; astral.ninja


Klienter tillåter användare att generate ett nytt nyckelpar (motsvarande att skapa ett konto) eller autentisera sig med ett befintligt nyckelpar.


## 3. Reläer


Reläer är förenklade servrar som du kan överge när som helst om du inte gillar innehållet de levererar till dig. Du kan också köra ditt eget relä om du vill.


💡 **Proffstips:** Betalda reläer är i allmänhet mer effektiva när det gäller att filtrera skräppost och oönskat innehåll.


### Guide


Nu vet du tillräckligt om Nostr för att komma igång och skapa din första identitet på detta protokoll.


I den här guiden kommer vi att använda iris.to (https://iris.to/) eftersom den här webbklienten fungerar på alla plattformar.


## Steg 1: Generera nycklar


ris skapar en uppsättning nycklar åt dig utan att du behöver göra något mer än att ange ett namn (verkligt eller fiktivt) för din profil. Klicka sedan på GO och du är klar!


![Main menu](assets/3.webp)


⚠️ **Attention!** Du måste hålla reda på dina nycklar om du vill kunna komma åt din profil igen när din session har stängts. Jag kommer att visa dig hur du gör det i slutet av den här guiden.


## Steg 2: Publicera innehåll


För att publicera innehåll är det lika enkelt och intuitivt som att skriva några ord i publiceringsfältet.


![Publication](assets/4.webp)


Nu är du igång! Du har publicerat din första notis på Nostr.


![Post](assets/5.webp)


## Steg 3: Hitta en vän


Hitta mig på Nostr och var aldrig ensam igen. Jag kommer att prenumerera tillbaka till alla som prenumererar på mitt flöde. För att göra detta, ange bara min publika nyckel


npub1hartx53w6t3q5wv9xdqdwrk7h6r5866t8u775q0304zedpn5zgssasp7d3 i sökfältet.


![My profile](assets/6.webp)


Klicka på "följ" och om högst några dagar kommer jag också att prenumerera på ditt flöde. Vi kommer att vara vänner. Jag kommer också gärna att läsa ditt meddelande om du vill skriva ett till mig.


Slutligen, se till att du också prenumererar på Agora256:s flöde för att få ett meddelande varje gång vi publicerar något nytt: npub1ag0rawstycy7nanuc6sz4v287rneen2yapcq3fd06972f8ncrhzqx


## Steg 4: Anpassa din profil


Du har fortfarande en del kvar att göra för att anpassa din profil. För att göra detta klickar du på den avatar som iris automatiskt genererade åt dig i det övre högra hörnet av skärmen och klickar sedan på "redigera profil".


![Profile](assets/7.webp)


Allt du behöver göra nu är att tala om för iris var du hittar din bild och profilbanner på internet. Jag rekommenderar att du hostar ditt eget innehåll: skydda det som är ditt.


![Another option](assets/8.webp)


Om du föredrar det kan du också ladda upp bilder, de kommer att lagras åt dig av iris på nostr.build, en gratis hosting-tjänst för visuellt innehåll för Nostr.


Som du ser kan du också konfigurera din klient så att den kan ta emot och skicka Sats. På så sätt kan du belöna författarna till innehåll som du gillar eller, ännu bättre, samla Sats för det fantastiska innehåll som du kommer att publicera.


## Steg 5: Säkerhetskopiera nyckelparet


Detta steg är viktigt om du vill behålla åtkomsten till din profil när du har loggat ut från klienten eller när din session har löpt ut.

Klicka först på ikonen "inställningar" som representeras av en kugghjul

![Setting](assets/9.webp)


Kopiera och klistra sedan in en efter en av dina npub, npub hex, nsec och nsec hex i en textfil som du kommer att hålla säker. Jag rekommenderar att du krypterar den här filen om du vet hur man gör det.


![Key](assets/10.webp)


⚠️ **Notera varningen som iris ger dig:** Du kan dela din publika nyckel utan rädsla, men det är en annan sak med din privata nyckel. Den som har den senare kommer att kunna komma åt ditt konto.


## Slutsats


Så där ja, lilla struts, nu har du tagit dina första steg på Nostr. Nu måste du lära dig att springa med blixtens hastighet. Vi kommer snart att publicera guider som visar dig hur du hanterar dina nycklar och hur du integrerar blixtar i din Nostr-upplevelse med hjälp av getalby.