---
name: Olvid
description: Privat meddelandehantering för alla
---
![cover](assets/cover.webp)



Olvid är en fransk applikation för snabbmeddelanden som lanserades 2019 och som är utformad för att erbjuda en hög säkerhetsnivå utan att kompromissa med integriteten. Till skillnad från WhatsApp eller Signal ber Olvid inte om några personuppgifter vid registrering: inget telefonnummer, ingen e-post, ingenting. Identifiering mellan användare baseras på en Exchange-nyckel, utan katalogserver eller delad Address-bok.



Alla meddelanden krypteras från början till slut med hjälp av ett originalkryptografiskt protokoll, som är utformat för att skydda även metadata: ingen vet vem du pratar med eller när. Klientkoden är öppen källkod, men den centrala servern som används för att dirigera krypterade meddelanden är fortfarande proprietär och finns på AWS.


Olvids säkerhetsmodell bygger på en nyckelprincip: den fullständiga avsaknaden av betrodda tredje parter vid upprättandet av digitala identiteter. Till skillnad från de flesta krypterade budbärare som förlitar sig på en centraliserad katalog för att hantera användaridentiteter, är Olvid inte beroende av någon centraliserad infrastruktur för att säkerställa kommunikationens integritet. Denna arkitektur eliminerar de risker som är förknippade med katalogkompromisser.


Olvid använder dock en central server för distribution av meddelanden, som är strikt begränsad till en logistisk roll: den hanterar den asynkrona överföringen av krypterade meddelanden. Denna server spelar ingen roll i krypteringsprocessen, känner varken till användarnas verkliga identiteter eller innehållet eller metadata i meddelandena (förutom mottagarens publika nyckel, som är nödvändig för routning). Den kan därför betraktas som fientlig som standard utan att systemets övergripande säkerhet äventyras. Även om den skulle komprometteras skulle den inte ge någon tillgång till meddelandets innehåll. Olvid förutsätter således centralisering för leverans av meddelanden (för effektivitet och tjänstekvalitet), samtidigt som det garanterar säkerhet som är oberoende av denna infrastruktur.



Olvid erbjuder en gratisversion och en abonnemangsversion för 4,99 euro per månad. Den kostnadsfria versionen erbjuder full funktionalitet, med undantag för att ringa ljud- och videosamtal (även om det är möjligt att ta emot dem), och tillåter inte kontosynkronisering mellan flera enheter. Så om du planerar att använda din smartphone uteslutande och inte behöver ringa samtal är Olvid en utmärkt lösning.



Olvid är certifierat av ANSSI (den franska cybersäkerhetsmyndigheten). Denna applikation är ett utmärkt alternativ till traditionella meddelandetjänster (WhatsApp, Facebook Messenger, WeChat ...) för dem som söker integritet samtidigt som de behåller enkelheten i användningen.


| Application          | E2EE 1:1      | E2EE groups   | Anonymous registration | Open-source client license | Open-source server license | Decentralized server | Year of creation |
| -------------------- | ------------- | ------------- | ---------------------- | -------------------------- | -------------------------- | -------------------- | ---------------- |
| WhatsApp             | ✅             | ✅             | ❌                      | ❌                          | ❌                          | ❌                    | 2009             |
| WeChat               | ❌             | ❌             | ❌                      | ❌                          | ❌                          | ❌                    | 2011             |
| Facebook Messenger   | ✅             | 🟡 (optional) | ❌                      | ❌                          | ❌                          | ❌                    | 2011             |
| Telegram             | 🟡 (optional) | ❌             | 🟡                     | ✅                          | ❌                          | ❌                    | 2013             |
| LINE                 | ✅             | ✅             | ❌                      | ❌                          | ❌                          | ❌                    | 2011             |
| Signal               | ✅             | ✅             | ❌                      | ✅                          | ✅                          | ❌                    | 2014             |
| Threema              | ✅             | ✅             | ✅                      | ✅                          | ❌                          | ❌                    | 2012             |
| Element (Matrix)     | ✅             | ✅             | ✅                      | ✅                          | ✅                          | 🟡 (federated)       | 2016             |
| Delta Chat           | ✅             | ✅             | ✅                      | ✅                          | N/A                        | 🟡 (via email)       | 2017             |
| Conversations (XMPP) | ✅             | ✅             | ✅                      | ✅                          | ✅                          | 🟡 (federated)       | 2014             |
| Session              | ✅             | ✅             | ✅                      | ✅                          | ✅                          | ✅                    | 2020             |
| SimpleX              | ✅             | ✅             | ✅                      | ✅                          | ✅                          | ✅                    | 2021             |
| **Olvid**            | **✅**         | **✅**         | **✅**                  | **✅**                      | **❌**                      | 🟡(no directory)     | **2019**         |
| Keet                 | ✅             | ✅             | ✅                      | ❌                          | N/A                        | ✅                    | 2022             |
| Jami                 | ✅             | ✅             | ✅                      | ✅                          | N/A                        | ✅                    | 2005             |
| Briar                | ✅             | ✅             | ✅                      | ✅                          | N/A                        | ✅                    | 2018             |
| Tox                  | ✅             | ✅             | ✅                      | ✅                          | N/A                        | ✅                    | 2013             |

*E2EE = End-to-end-kryptering*



## Installera Olvid-applikationen



Olvid finns tillgänglig på alla plattformar. Du kan ladda ner applikationen direkt från din telefons appbutik:




- [Google Play] (https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store] (https://apps.apple.com/app/olvid/id1414865219);



På Android är det också möjligt att [installera via APK] (https://www.olvid.io/download/).



I den här handledningen koncentrerar vi oss på mobilversionen, men observera att [datorversioner också finns tillgängliga](https://www.olvid.io/download/) (MacOS, Linux och Windows). Om du väljer betalversionen kommer du att kunna synkronisera ditt konto på flera enheter.



![Image](assets/fr/01.webp)



## Skapa ett konto på Olvid



När du startar programmet för första gången klickar du på knappen "*Jag är en ny användare*".



![Image](assets/fr/02.webp)



Välj ett smeknamn eller ange ditt för- och efternamn.



![Image](assets/fr/03.webp)



Lägg till ett profilfoto.



![Image](assets/fr/04.webp)



Ditt konto är nu skapat.



![Image](assets/fr/05.webp)



För att förhindra förlust av åtkomst till ditt Olvid-konto rekommenderar vi att du ställer in automatiska säkerhetskopior. För att göra detta, öppna inställningarna genom att klicka på de tre prickarna längst upp till höger i Interface och välj sedan "*Inställningar*".


⚠️ **Varning**: Sedan Olvid version 3.7 har proceduren för säkerhetskopiering av dina profiler och kontakter ersatts av en ny. Denna handledning presenterar fortfarande den gamla versionen. Du kan upptäcka den nya versionen på deras FAQ: [💾 Säkerhetskopiera dina profiler](https://www.olvid.io/faq/sauvegarder-vos-profils/)


![Image](assets/fr/06.webp)



Gå till menyn "*Spara nycklar och kontakter*".



![Image](assets/fr/07.webp)



Klicka sedan på "*generate en säkerhetskopieringsnyckel*". Den här nyckeln krypterar dina säkerhetskopior. Om du behöver återställa ditt konto på en annan enhet och inte längre har tillgång till det, behöver du både en säkerhetskopia och den här nyckeln för att dekryptera den.



![Image](assets/fr/08.webp)



Förvara denna nyckel på en säker plats. Du kan också göra en papperskopia.



![Image](assets/fr/09.webp)



Du kan sedan välja att skapa en lokal säkerhetskopia eller en automatisk säkerhetskopia på en molntjänst. Det andra alternativet rekommenderas starkt för att garantera tillgång till ditt Olvid-konto under alla omständigheter, även om du tappar bort din telefon.



![Image](assets/fr/10.webp)



Kontrollera att alternativet "*Enable automatic backup*" är markerat.



![Image](assets/fr/11.webp)



Du kan också utforska de andra inställningarna som finns tillgängliga för att anpassa programmet efter dina behov.



![Image](assets/fr/12.webp)



## Skicka meddelanden med Olvid



För att du ska kunna skicka meddelanden måste du först lägga till kontakter. Klicka på den blå "*+*"-knappen på startsidan.



![Image](assets/fr/13.webp)



Olvid visar då ditt användar-ID. Det kan du sedan skicka vidare till de personer som du vill kommunicera med, så att de kan lägga till dig som kontakt.



För att lägga till en person skannar du dennes ID med kameran eller klistrar in det manuellt genom att klicka på de tre små prickarna i det övre högra hörnet.



![Image](assets/fr/14.webp)



När ID-kortet har skannats kan du antingen be din kontaktperson att skanna den QR-kod som visas eller skicka en begäran om fjärranslutning genom att klicka på "*Fjärranslutning*".



![Image](assets/fr/15.webp)



Förbindelsen är nu upprättad.



![Image](assets/fr/16.webp)



Du kan nu börja utbyta meddelanden och annat innehåll med din korrespondent!



![Image](assets/fr/17.webp)



Från startsidan hittar du alla dina konversationer.



![Image](assets/fr/18.webp)



Den andra fliken innehåller alla dina kontakter.



![Image](assets/fr/19.webp)



Du kan också skapa gruppdiskussioner.



![Image](assets/fr/20.webp)



Grattis, du har nu kommit igång med att använda Olvid messaging, ett bra alternativ till WathsApp! Om du tyckte att den här handledningen var användbar skulle jag vara mycket tacksam om du lämnar en Green-tumme nedan. Känn dig fri att dela denna handledning på dina sociala nätverk. Tack så mycket!



Jag rekommenderar också den här andra handledningen, där jag introducerar dig till Proton Mail, ett mycket mer integritetsvänligt alternativ till Gmail :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2