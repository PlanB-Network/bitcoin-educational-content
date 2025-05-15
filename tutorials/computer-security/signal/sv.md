---
name: Signal
description: Uttryck dig fritt
---
![cover](assets/cover.webp)



Signal är en krypterad meddelandeapplikation som är utformad för att erbjuda god sekretess som standard. Varje meddelande, samtal och fil skyddas av Signal-protokollet, som är erkänt som ett av de mest robusta meddelandeprotokollen. Det återanvänds av många andra applikationer, inklusive WathsApp, Facebook Messenger, Skype och Google Messages för RCS-kommunikation.



Signal lanserades 2014 av Moxie Marlinspike (pseudonym) och utvecklas sedan 2018 av Signal Foundation, en ideell organisation som skapats med stöd av Brian Acton (medgrundare av WhatsApp).



![Image](assets/fr/01.webp)



Jämfört med WhatsApp utmärker sig Signal genom sin transparens: applikationens kod, både på klient- och serversidan, är helt öppen källkod. Detta gör det möjligt för vem som helst att granska den, och i synnerhet att kontrollera att kryptering tillämpas som utlovat.



Signal förlitar sig dock på användningen av ett telefonnummer, vilket är dess största svaghet när det gäller anonymitet jämfört med andra lösningar. Trots detta är applikationen enligt min mening en av de mest tillförlitliga när det gäller säkerhet och sekretess, tack vare sin helt öppna arkitektur och ett allmänt antaget krypteringsprotokoll, och därför testad och granskad, till skillnad från andra mer marginella applikationer.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| **Signal**           | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end-kryptering*




## Installera Signal-applikationen



Signal är tillgänglig på alla plattformar. Du kan ladda ner programmet direkt från din telefons programbutik:




- [Google Play] (https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms);
- [App Store] (https://apps.apple.com/us/app/signal-private-messenger/id874139669);



På Android är det också möjligt att [installera via APK] (https://github.com/signalapp/Signal-Android/releases).



I den här handledningen koncentrerar vi oss på mobilversionen, men observera att [skrivbordsversioner också finns tillgängliga](https://signal.org/fr/download/) (MacOS, Linux och Windows). Du måste dock först konfigurera mobilapplikationen innan du kan synkronisera ditt konto med skrivbordsversionen.



## Skapa ett konto på Signal



När du startar programmet för första gången klickar du på knappen "*Continue*".



![Image](assets/fr/02.webp)



Ange ditt telefonnummer och klicka sedan på "*Nästa*".



![Image](assets/fr/03.webp)



En verifieringskod kommer att skickas till dig via SMS. Ange denna kod i Signal-applikationen.



![Image](assets/fr/04.webp)



Välj en PIN-kod för att säkra ditt Signal-konto. Koden krypterar dina data och kan användas för att återställa åtkomsten till ditt konto om du förlorar din enhet. Det är därför viktigt att du väljer en robust PIN-kod som är så lång och slumpmässig som möjligt och att du sparar den på ett tillförlitligt sätt.



![Image](assets/fr/05.webp)



Bekräfta PIN-koden en gång till.



![Image](assets/fr/06.webp)



Du kan nu anpassa din användarprofil. Välj ett foto, ange ditt namn eller ett smeknamn. I det här skedet kan du också definiera vem som kan hitta dig på Signal via ditt nummer. Välj "*Alla*" om du vill vara synlig eller "*Ingen*" om du vill vara ospårbar via telefonnumret (du kan då bara läggas till med ditt "*Användarnamn*"). När du har gjort dina val klickar du på "*Nästa*".



![Image](assets/fr/07.webp)



Du är nu ansluten till Signal och redo att skicka Exchange-meddelanden.



![Image](assets/fr/08.webp)



## Konfigurera ditt Signal-konto



Klicka på ditt profilfoto i det övre vänstra hörnet för att komma till applikationsinställningarna.



![Image](assets/fr/09.webp)



I menyn "*Account*" kan du hantera dina profilinställningar. Jag råder dig att behålla standardinställningarna. Du kan också aktivera alternativet "*Registration Lock*", som skyddar ditt konto mot vissa typer av attacker. Den här menyn innehåller också de alternativ du behöver för att överföra ditt konto till en ny enhet.



![Image](assets/fr/10.webp)



Om du klickar på din profilbild i inställningarna igen kommer du till alternativen för att anpassa din profil. Jag rekommenderar att du anger ett "*användarnamn*": detta gör att du kan komma i kontakt med andra människor utan att avslöja ditt telefonnummer.



![Image](assets/fr/11.webp)



Genom att välja "*QR-kod eller länk*" får du den information du behöver för att dela med dig till någon som vill lägga till dig i Signal.



![Image](assets/fr/12.webp)



Menyn "*Privacy*" är särskilt viktig. Här hittar du alternativ för att kontrollera synligheten av ditt nummer, hanteringen av dina meddelanden med dina kontakter samt olika behörigheter som beviljas i applikationen.



![Image](assets/fr/13.webp)



Utforska gärna menyerna "*Avseende*", "*Chatt*" och "*Aviseringar*" för att skräddarsy Interface och programmets funktion efter dina personliga behov.



## Anslut skrivbordsapplikation



För att ansluta skrivbordsprogrammet börjar du med att installera programvaran på din dator (se den första delen av denna handledning). Gå sedan till Inställningar på din telefon och öppna avsnittet "*Länkade enheter*".



![Image](assets/fr/14.webp)



Klicka på knappen "*Länk en ny enhet*".



![Image](assets/fr/15.webp)



Starta programmet på din dator och skanna sedan QR-koden som visas på skärmen med din telefon. Om du vill importera dina konversationer väljer du alternativet "*Överför meddelandehistorik*".



![Image](assets/fr/16.webp)



Dina enheter är nu helt synkroniserade.



![Image](assets/fr/17.webp)



## Skicka meddelanden med Signal



För att kommunicera med någon på Signal måste du först lägga till dem som en kontakt. Det finns flera alternativ: du kan lägga till dem via deras telefonnummer (om personen har aktiverat alternativet att hittas på detta sätt) eller använda deras Signal-ID.



Klicka på pennikonen i det nedre högra hörnet av Interface.



![Image](assets/fr/18.webp)



I mitt fall vill jag lägga till personen efter användarnamn. Så jag klickar på "*Find by username*".



![Image](assets/fr/19.webp)



Du kan sedan antingen klistra in dess inloggning eller skanna dess QR-kod.



![Image](assets/fr/20.webp)



Skicka ett meddelande till honom för att etablera kontakt.



![Image](assets/fr/21.webp)



Konversationen kommer då att visas på startsidan. Om personen accepterar din kontaktbegäran ser du dennes namn och profilbild.



![Image](assets/fr/22.webp)



Grattis, du har nu kommit igång med att använda Signal-meddelanden, ett bra alternativ till WathsApp! Om du tyckte att den här handledningen var användbar skulle jag vara mycket tacksam om du lämnar en Green-tumme nedan. Känn dig fri att dela denna handledning på dina sociala nätverk. Tack så mycket!



Jag rekommenderar också den här andra handledningen, där jag introducerar dig till Proton Mail, ett mycket mer integritetsvänligt alternativ till Gmail :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2