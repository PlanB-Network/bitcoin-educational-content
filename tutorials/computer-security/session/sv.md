---
name: Session
description: Skicka krypterade meddelanden, inte metadata
---
![cover](assets/cover.webp)



Session är en krypterad meddelandeapplikation som skapades 2020 och som är utformad för att erbjuda en högre grad av sekretess än traditionella meddelanden. Den utvecklades först av *Oxen Privacy Tech Foundation* och sedan av *Session Technology Foundation*.



Session har några intressanta tekniska funktioner: end-to-end-kryptering av meddelanden, ett decentraliserat nätverk som är organiserat för att garantera tillgänglighet och redundans samt Tor-inspirerad onion routing. Till skillnad från WathsApp eller Signal, som kräver ett telefonnummer för registrering, ber Session inte om någon personlig information (inget nummer, ingen e-post, bara ett par kryptografiska nycklar).



Med Session kan du skicka meddelanden, filer, röstmeddelanden, ljudsamtal samt grupper på upp till 100 medlemmar (och communities utöver det), samtidigt som du minimerar läckage av metadata.



![Image](assets/fr/01.webp)



Session vänder sig framför allt till användare som prioriterar konfidentialitet högt. Denna meddelandetjänst utgör ett seriöst alternativ till WhatsApp, med en arkitektur som är utformad för att motstå moderna övervakningsmodeller.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end-kryptering*



## Installera Session-applikationen



Session är tillgänglig på alla plattformar. Du kan ladda ner applikationen direkt från din telefons applikationsbutik:




- [Google Play] (https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store] (https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid] (https://fdroid.getsession.org/).



På Android är det också möjligt att [installera via APK] (https://github.com/session-foundation/session-android/releases).



I den här handledningen koncentrerar vi oss på mobilversionen, men observera att [datorversioner också finns tillgängliga](https://getsession.org/download) (MacOS, Linux och Windows). Senare kommer vi att titta på hur man synkroniserar ett konto mellan flera enheter.



## Skapa ett konto på Session



Vid första lanseringen klickar du på "*Create account*".



![Image](assets/fr/02.webp)



Välj ett visningsnamn för din profil. Det kan vara en pseudonym eller ditt riktiga namn.



![Image](assets/fr/03.webp)



Du måste sedan välja mellan två olika sätt att hantera meddelanden:





- Snabbläge ("*Firebase Cloud Messaging/Apple Push Notification Service*")**: gör att du kan ta emot meddelanden i nära realtid tack vare de meddelandetjänster som tillhandahålls av Google eller Apple (beroende på ditt system). För att detta ska fungera överförs din IP Address och ett unikt meddelande-ID till Google eller Apple, och sessionskontots ID registreras också på en STF-server (via Tor). Detta läge innebär (visserligen minimal) exponering av metadata, men äventyrar inte meddelandets innehåll eller kontakter och gör det inte möjligt att spåra din faktiska aktivitet. Detta läge är därför mer effektivt när det gäller respons, men är beroende av en centraliserad infrastruktur och är något mindre effektivt när det gäller konfidentialitet.





- Långsamt läge (*background polling*)**: Session-applikationen förblir aktiv i bakgrunden och pollar regelbundet nätverket efter nya meddelanden. Detta tillvägagångssätt garanterar större sekretess än det första, eftersom inga data överförs till tredjepartsservrar; varken Google, Apple eller STF:s servrar får någon information. Å andra sidan har detta läge två nackdelar: meddelanden kan försenas (upp till flera minuter) och energiförbrukningen är i allmänhet högre på grund av applikationsaktivitet i bakgrunden.



![Image](assets/fr/04.webp)



Du är nu ansluten till Session-programmet och kan börja utbyta meddelanden.



![Image](assets/fr/05.webp)



## Spara ditt Session-konto



Det första du bör göra innan du börjar använda Session är att spara ditt konto så att du kan återställa det om du tappar bort din enhet. Det gör du genom att klicka på knappen "*Fortsätt*" bredvid "*Spara ditt återställningslösenord*".



![Image](assets/fr/06.webp)



Session kommer då att visa en Mnemonic-fras. Kopiera den noggrant och förvara den på en säker plats. Den här frasen ger dig full åtkomst till ditt Session-konto, så det är viktigt att du inte avslöjar den. Du kommer att behöva den för att komma åt ditt konto på en annan enhet, särskilt om din nuvarande telefon försvinner eller byts ut.



![Image](assets/fr/07.webp)



Den här frasen fungerar på samma sätt som Mnemonic-fraserna som används i Bitcoin-plånböcker. Jag rekommenderar därför att du läser den här andra handledningen, där jag förklarar de bästa metoderna för att spara en Mnemonic-fras:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Vänligen notera**: Till skillnad från Mnemonic-fraserna som används på Bitcoin-plånböcker, på Session, ** måste du absolut spara varje ord i sin helhet**. De första 4 bokstäverna räcker inte!



## Konfigurera Session-applikationen



För att komma åt programinställningarna klickar du på ditt profilfoto längst upp till vänster i Interface. Det är här du kan lägga till ett profilfoto.



![Image](assets/fr/08.webp)



I menyn "*Privacy*" kan du aktivera eller inaktivera olika funktioner (se upp, vissa kan avslöja din IP Address). Jag rekommenderar också att du aktiverar alternativet "*Lock App*", som kräver autentisering för att komma åt applikationen.



![Image](assets/fr/09.webp)



I menyn "*Notification*" kan du välja mellan "*Fast Mode*" och "*Slow Mode*" (se tidigare delar av handledningen). Du kan också anpassa aviseringarna så att de passar dina önskemål.



![Image](assets/fr/10.webp)



Slutligen kan du gå till menyn "*Appearance*" för att anpassa Interface efter din smak. I menyn "*Recovery Password*" kan du hämta din Mnemonic-fras om du vill göra en ny säkerhetskopia.



![Image](assets/fr/11.webp)



## Skicka meddelanden med Session



För att kontakta andra personer, klicka på "*+*"-knappen på startsidan.



![Image](assets/fr/12.webp)



Flera alternativ finns tillgängliga. Om du vill skapa eller gå med i en grupp väljer du "*Create Group*" eller "*Join Community*".



![Image](assets/fr/13.webp)



Om du vill att någon ska lägga till dig som kontakt kan du be dem att skanna ditt sessions-ID som en QR-kod.



![Image](assets/fr/14.webp)



Om du vill skicka din inloggning på distans klickar du på "*Invitera en vän*". Du kan då kopiera ditt sessions-ID och skicka det via en annan kommunikationskanal. Du kan också hämta denna information genom att klicka på din profilbild från startsidan.



![Image](assets/fr/15.webp)



Om du har en annan persons sessions-ID och vill lägga till det klickar du på "*Nytt meddelande*".



![Image](assets/fr/16.webp)



Du kan sedan klistra in dess identifierare i text, eller skanna den direkt om du har den som en QR-kod.



![Image](assets/fr/17.webp)



Skicka sedan ett första meddelande till den här personen.



![Image](assets/fr/18.webp)



Så snart personen accepterar din begäran ser du hans eller hennes användarnamn och du kan chatta fritt med honom eller henne.



![Image](assets/fr/19.webp)



## Synkronisera programvara för skrivbord



För att synkronisera ditt konto på din dator måste du installera programvaran. [Ladda ner den från den officiella webbplatsen](https://getsession.org/download). Jag råder dig att kontrollera dess äkthet och integritet innan du installerar den.



![Image](assets/fr/20.webp)



Vid första öppningen klickar du på "*Jag har ett konto*".



![Image](assets/fr/21.webp)



Ange din Mnemonic-fras och se till att lämna ett mellanslag mellan varje ord.



![Image](assets/fr/22.webp)



Du kan nu komma åt dina konversationer från din dator.



![Image](assets/fr/23.webp)



Grattis, du har nu lärt dig att använda Session messaging, ett utmärkt alternativ till WathsApp!



Jag rekommenderar också den här andra handledningen, där jag presenterar Threema, ett annat intressant alternativ för din meddelandeprogram:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74