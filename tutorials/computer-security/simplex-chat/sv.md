---
name: SimpleX Chatt
description: Den första brevlådan utan användar-ID
---
![cover](assets/cover.webp)



SimpleX lanserades 2021 och är en gratis applikation för snabbmeddelanden med en radikalt annorlunda inställning till integritet. Till skillnad från WhatsApp, Signal och andra centraliserade meddelandetjänster står SimpleX ut för sin användarhantering: det finns inga användaridentifierare, pseudonymer, nummer eller synliga offentliga nycklar. Denna totala avsaknad av identifierare gör det praktiskt taget omöjligt att korrelera användare, vilket garanterar en hög integritetsnivå.



Till skillnad från de flesta applikationer som kräver ett konto eller telefonnummer låter SimpleX dig inleda konversationer genom att dela en länk eller en kortlivad QR-kod. Varje länk skapar en unik krypterad kanal och kontakter kan inte hitta eller kontakta avsändaren på nytt utan en uttrycklig Exchange. Meddelandena är krypterade från början till slut och passerar genom reläservrar som raderar dem efter att de skickats och som varken ser avsändaren, mottagaren eller deras nycklar.



![Image](assets/fr/01.webp)



Nätverksarkitekturen är helt decentraliserad och utan federation: servrarna känner inte varandra, de har ingen global katalog och de är inte värd för några användarprofiler. Ännu bättre är att varje användare kan distribuera och använda sin egen reläserver, samtidigt som den förblir kompatibel med dem i det offentliga nätverket.



SimpleX är helt öppen källkod (klienter, protokoll och servrar) och finns tillgänglig på Android, iOS, Linux, Windows och macOS. Den lokala lagringen är krypterad och portabel, så du kan överföra en profil från en enhet till en annan utan att förlita dig på en centraliserad server.



SimpleX integrerar alla de klassiska funktionerna i meddelandeprogram. Ergonomin är dock inte lika smidig som i WhatsApp eller Signal. Det kan också vara mer restriktivt att använda, särskilt när man lägger till kontakter. Så enligt min mening är det ett relevant alternativ till WhatsApp eller Signal för användare som sätter sekretess i centrum för sina prioriteringar, och som av den anledningen är beredda att göra några eftergifter när det gäller den dagliga användarkomforten.



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



## Installera SimpleX Chat-applikationen



SimpleX Chat är tillgänglig på alla plattformar. Du kan ladda ner applikationen direkt från din telefons appbutik:




- [Google Play] (https://play.google.com/store/apps/details?id=chat.simplex.app);
- [App Store] (https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084);
- [F-Droid] (https://simplex.chat/fdroid/).



På Android är det också möjligt att [installera via APK] (https://github.com/simplex-chat/simplex-chat/releases).



I den här handledningen koncentrerar vi oss på mobilversionen, men observera att [skrivbordsversioner också finns tillgängliga](https://simplex.chat/downloads/) (MacOS, Linux och Windows). Det är möjligt att länka skrivbordsversionen till en befintlig mobil användarprofil, men för att denna synkronisering ska fungera måste båda enheterna vara anslutna till samma lokala nätverk.



![Image](assets/fr/02.webp)



## Skapa ett konto på SimpleX Chat



När du först startar programmet klickar du på knappen "*Create your profile*".



![Image](assets/fr/03.webp)



Välj ett användarnamn, som kan vara ditt riktiga namn eller en pseudonym, och klicka sedan på "*Create*".



![Image](assets/fr/04.webp)



Därefter ställer du in hur ofta programmet ska söka efter nya meddelanden. Om telefonens batteritid inte är något problem kan du välja "*Instant*" för att få meddelanden i realtid. Om du vill spara batteri och förhindra att applikationen körs i bakgrunden väljer du "*När appen körs*": du får då bara meddelanden när applikationen är öppen. En möjlig kompromiss är att välja en periodisk kontroll var 10:e minut.



När du har gjort ditt val klickar du på "*Use chat*".



![Image](assets/fr/05.webp)



Du är nu ansluten till SimpleX Chat och redo att börja chatta.



![Image](assets/fr/06.webp)



## Konfigurera SimpleX Chat



Först och främst kommer du åt inställningarna genom att klicka på din profilbild i det nedre högra hörnet och sedan på "*Inställningar*".



![Image](assets/fr/07.webp)



Standardinställningarna är i allmänhet lämpliga för de flesta användare. Jag rekommenderar dock att du går till menyn "*Databas passphrase & export*". Det är här du kan exportera din SimpleX-kontodatabas för säkerhetskopieringsändamål.



Du kan också ändra den passphrase som används för att kryptera databasen. Som standard genereras den slumpmässigt och lagras lokalt på din enhet. Om du föredrar det kan du definiera din egen passphrase och ta bort den lokala passphrase-säkerhetskopian: du måste då ange den manuellt varje gång du öppnar programmet, liksom när du migrerar till en annan enhet.



**Observera**: Om du väljer det här alternativet kommer förlusten av passphrase att leda till permanent förlust av alla dina SimpleX-profiler och meddelanden.



![Image](assets/fr/08.webp)



Jag rekommenderar också att du går till menyn "*Privacy & security*", där du kan aktivera alternativet "*SimpleX Lock*". Detta skyddar åtkomsten till applikationen med en låskod.



![Image](assets/fr/09.webp)



Slutligen kan du i menyerna "*Notifications*" och "*Appearance*" anpassa SimpleX Chat efter dina önskemål.



![Image](assets/fr/10.webp)



## Skicka meddelanden med SimpleX Chat



För att få kontakt med en annan person på SimpleX har du två alternativ:




- Använd en länk för engångsbruk;
- Använd en återanvändbar statisk Address.



En statisk Address gör det möjligt för alla som känner till den att kontakta dig på SimpleX. Det är en persistent Address som kan användas flera gånger, av olika personer, utan tidsbegränsning. Det är denna beständighet som gör den mer sårbar för skräppost. Till skillnad från andra meddelandeprogram räcker det dock med att radera SimpleX Address för att stoppa all skräppost, utan att påverka befintliga konversationer. Faktum är att denna Address endast används för att upprätta den första anslutningen och inte längre behövs när Exchange har börjat.



Engångslänkar kan å andra sidan bara användas en gång, av vilken användare som helst. När en kontakt använder den blir länken ogiltig. Du måste generate en ny för varje ny anslutning.



### Med statisk Address



Om du vill använda Address klickar du på din profilbild längst ned till vänster på Interface och väljer sedan "*Create SimpleX Address*". Klicka sedan på "*Create SimpleX Address*" igen.



![Image](assets/fr/11.webp)



Din återanvändbara Address har nu skapats. Du kan dela den med personer som vill komma i kontakt med dig, antingen genom att visa dem QR-koden eller genom att skicka länken till dem.



![Image](assets/fr/12.webp)



Klicka på knappen "*Address-inställningar*". Här kan du konfigurera de behörigheter som är kopplade till din Address. Alternativet "*Dela med kontakter*" gör din Address synlig på din SimpleX-profil. Dina kontakter kan då ta del av den och vidarebefordra den till andra personer som vill kontakta dig.



Alternativet "*Auto-accept*" accepterar automatiskt inkommande anslutningar via din Address. Det innebär att alla som har din Address kan se din profil och skicka ett meddelande till dig, såvida du inte aktiverar alternativet "*Acceptera inkognito*". Detta döljer ditt namn och profilfoto när en ny anslutning görs och ersätter dem med en slumpmässig pseudonym, som är olika för varje samtalspartner.



![Image](assets/fr/13.webp)



### Med återanvändbar länk



Det andra sättet att få kontakt med en person är att skapa en engångslänk. För att göra detta klickar du på pennikonen i det nedre högra hörnet av Interface och väljer sedan "*skapa engångslänk*".



Om din kontakt har skickat en länk till dig, klicka på "*Scan / Paste link*" för att scanna eller klistra in den.



![Image](assets/fr/14.webp)



SimpleX genererar sedan en länk för engångsbruk. Du kan vidarebefordra den till din kontakt på valfritt sätt: fysisk Exchange, andra meddelanden, etc.



![Image](assets/fr/15.webp)



Du kan också välja vilken profil som ska kopplas till denna inbjudningslänk. För att göra det klickar du på din profil precis under QR-koden. Du kommer då att kunna :




- välj en av dina befintliga profiler (vi kommer att se hur du skapar flera profiler i nästa avsnitt);
- eller välj läget "*Inkognito*", som döljer ditt namn och profilfoto med en slumpmässigt genererad pseudonym för din korrespondent.



Här väljer jag läget "*Inkognito*".



![Image](assets/fr/16.webp)



Min kontakt använde länken. För sin del aktiverade han inte läget "*Inkognito*", vilket är anledningen till att jag ser hans profilnamn "*Bob*". Å andra sidan ser Bob inte mitt riktiga namn "*Loïc Morel*", utan en slumpmässig pseudonym, i det här fallet "*RealSynergy*".



![Image](assets/fr/17.webp)



Jag skulle kunna börja chatta direkt, men först vill jag kontrollera att jag pratar med Bob och inte med någon illasinnad person som kan ha snappat upp länken eller utfört en MITM-attack.



För att göra detta ska vi kontrollera vår säkerhetslänk **utanför applikationen**. Detta är viktigt, för i händelse av en MITM-attack skulle den interna verifieringen äventyras. Så använd ett annat säkert meddelandesystem, eller ännu bättre, kontrollera koderna personligen.



I chatten klickar du på Bobs foto och sedan på "*Verifiera säkerhetskod*". Bob måste göra samma sak på sin sida.



![Image](assets/fr/18.webp)



Om du arbetar på distans kan du jämföra koderna på ett annat säkert meddelandesystem (de måste vara identiska). Eller ännu bättre, om ni kan träffas ansikte mot ansikte, skanna din kontakts QR-kod genom att klicka på "*Skanna kod*".



![Image](assets/fr/19.webp)



Om verifieringen lyckas visas en sköldikon med en bockmarkering bredvid din kontakts namn. Detta är din försäkran om att du utbyter information med Bob. Om verifieringen inte lyckas visas meddelandet "*Inkorrekt säkerhetskod!*".



![Image](assets/fr/20.webp)



Du kan nu fritt Exchange meddelanden, samtal och filer med Bob, beroende på vilka behörigheter du har ställt in för den här konversationen.



## Anpassa dina SimpleX Chat-profiler



En av SimpleX mest kraftfulla funktioner är möjligheten att hantera flera helt separata användarprofiler, som alla är tillgängliga från samma lokala konto. Detta gör att du kan separera dina olika identiteter på ett snyggt sätt, utan att komplicera meddelandehanteringen.



Du kan till exempel skapa :




- En profil med ditt riktiga namn och ett riktigt foto för dina professionella utbyten;
- En profil med ditt riktiga namn och ett roligt foto för dina familjeutbyten;
- En profil med ett falskt foto och en pseudonym för dina personliga konversationer;
- En annan pseudonym profil för att chatta med främlingar.



Det är vad vi ska göra här. Jag börjar med att konfigurera min huvudprofil, den som är kopplad till min riktiga identitet. För att göra detta klickar jag på mitt profilfoto i det nedre högra hörnet och sedan på mitt användarnamn.



![Image](assets/fr/21.webp)



Jag klickar sedan på min profilbild för att ändra den och lägga till en ny.



![Image](assets/fr/22.webp)



Om du vill lägga till andra profiler klickar du på menyn "*Dina chattprofiler*".



![Image](assets/fr/23.webp)



Här ser du alla dina profiler. Klicka på "*Lägg till profil*" för att skapa en ny.



![Image](assets/fr/24.webp)



Välj sedan information för din nya profil: namn, foto osv. Här använder jag en pseudonym och en annan bild för att dölja min verkliga identitet i vissa utbyten.



![Image](assets/fr/25.webp)



Genom att hålla fingret nere på en profil kan du dölja den. Då blir den osynlig i applikationen, tillsammans med alla tillhörande konversationer. Du kan också välja att "*Mute*" den för att sluta ta emot aviseringar.



![Image](assets/fr/26.webp)



När du har skapat dina profiler kan du hantera dem självständigt. Från startsidan väljer du helt enkelt den aktiva profil som ska visas.



![Image](assets/fr/27.webp)



När du skapar en inbjudningslänk eller statisk Address kan du nu välja vilken profil som ska associeras med den. Om jag till exempel väljer profilen "*Satoshi Nakamoto*" för att generate en länk och skickar den till Alice, kommer hon bara att se min pseudonyma identitet "*Satoshi Nakamoto*", utan att någonsin känna till min riktiga identitet "*Loïc Morel*". Omvänt, om jag ger henne en länk från min riktiga profil, har hon inget sätt att länka till min pseudonyma profil.



![Image](assets/fr/28.webp)



Grattis, nu har du fått koll på SimpleX messaging, ett utmärkt alternativ till WathsApp!



Jag rekommenderar också den här andra handledningen, där jag presenterar Threema, ett annat intressant alternativ för din meddelandeprogram:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74