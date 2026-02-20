---
name: Matrix
description: En guide för att förstå, konfigurera och använda Matrix, den säkra, öppna och decentraliserade kommunikationsplattformen.
---

![cover](assets/cover.webp)



## Vad är Matrix?



Matrix är ett **decentraliserat kommunikationsprotokoll** som är utformat för att möjliggöra utbyte av meddelanden, filer och ljud-/videosamtal mellan användare och applikationer, utan att vara beroende av ett centralt företag. Till skillnad från traditionella meddelandeplattformar är Matrix en **öppen infrastruktur**, jämförbar med e-post: vem som helst kan välja en server eller driva den själv, samtidigt som man behåller möjligheten att utbyta med resten av nätverket.



Matrix kännetecknas av tre grundläggande principer:



### Ett protokoll, inte en applikation



Matrix är inte en applikation som WhatsApp eller Telegram.


Det är ett standardiserat språk som många applikationer kan använda.


Med andra ord ger ett brett utbud av Element-programvara, FluffyChat, Cinny, Nheko och andra, tillgång till samma Matrix-nätverk.



Detta garanterar total frihet: byte av applikation utan förlust av kontakter, mångfald av gränssnitt, oberoende av en enda leverantör.



![capture](assets/fr/03.webp)



### Ett decentraliserat, federerat nätverk



Matrix struktur är baserad på **federation**, en modell där flera oberoende servrar samarbetar med varandra.


Varje server (kallad _homeserver_) kan vara värd för användare, chattrum och synkronisera meddelanden med andra servrar i nätverket.


Således :





- ingen enskild enhet kontrollerar hela systemet;
- en server kan försvinna utan att det påverkar resten av nätverket;
- varje organisation eller individ kan hantera sitt eget utrymme.



Denna modell säkerställer **hög motståndskraft** och återspeglar värdena för teknisk suveränitet.



![capture](assets/fr/03.webp)



### Ett säkert, krypterat system



Matrix har stöd för **end-to-end-kryptering (E2EE)** för privata utbyten och krypterade grupper.


Meddelanden kan bara läsas av deltagarna, inte av mellanliggande servrar.


Detta tillvägagångssätt gör det möjligt att kommunicera utan att exponera innehållet i utbytena för en tredje part, samtidigt som protokollets transparens och möjligheten att hosta en egen server bibehålls.



![capture](assets/fr/05.webp)



### Unik interoperabilitet



En av Matrix stora tillgångar är dess förmåga att fungera som en **brygga mellan olika kommunikationssystem**. Tack vare _bryggor_ är det möjligt att ansluta :





- Telegram
- WhatsApp
- Signal
- Budbärare
- Slack
- Discord
- IRC, XMPP, etc.



Detta gör det möjligt att förena communities som är utspridda på flera plattformar, samtidigt som man behåller kontrollen över infrastrukturen.



![capture](assets/fr/06.webp)



## Hur fungerar Matrix?



I detta avsnitt presenteras Matrix-nätverkets interna struktur för att förstå hur användare, servrar och applikationer samverkar inom detta decentraliserade ekosystem. Matrix bygger på tre viktiga element: _hemservrar_, identiteter och _klienter_ som används för att kommunicera.



### Servrar: homeservers



Matrix körs på oberoende servrar som kallas _homeservers_.


Varje hemserver hanterar :





- de användarkonton som den är värd för,
- privata samtal och lounger som dessa användare deltar i,
- synkronisering med andra nätverksservrar.



Alla homeservers som är anslutna till Matrix-nätverket utbyter automatiskt meddelanden och händelser från gemensamma vardagsrum. Det kan till exempel vara





- en användare som är registrerad på server A kan chatta med en användare på server B,
- en salong kan vara spridd över dussintals servrar,
- ingen har kontroll över en salong eller ett samhälle som helhet.



Denna modell är mycket motståndskraftig och gör det möjligt för varje organisation eller individ att hantera sin egen infrastruktur.



### Matrisidentifierare



Varje användare har en unik identifierare, kallad **MXID** (_Matrix ID_), som ser ut som en adress:



```bash
@nomdutilisateur:serveur.xyz
```



Den består av :





- ett användarnamn, föregånget av **@**
- namnet på den server där kontot skapades, föregånget av **:**



Exempel på detta:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



Denna identifierare möjliggör kommunikation med alla andra Matrix-användare, oavsett ursprungsserver.



### Matrisklienter (applikationer)



För att använda Matrix måste du ansluta dig till ett program som heter **client Matrix**.



De mest kända är :





- Element (webb, mobil, skrivbord)
- FluffyChat (mobil)
- Cinny (minimalistisk webb/skrivbord)
- Nheko (skrivbord)



Dessa applikationer är endast gränssnitt för :





- för att visa meddelanden,
- skicka text, bilder eller filer,
- gå med i eller skapa mässor,
- ringa ljud- och videosamtal.



Alla applikationer kommunicerar med servrarna via samma standardiserade protokoll.



### Rum och privata meddelanden (DM)



I Matrix sker utbyten i **rum** :





- ett rum kan vara offentligt eller privat
- kan rymma två personer eller tusentals
- den kan delas mellan flera servrar
- den har en unik identifierare som börjar med **!**



Privata meddelanden är helt enkelt chattrum med två deltagare, ofta kallade **DM (Direct Messages)**.



Salongssynkroniseringen sker i realtid mellan deltagande servrar, vilket säkerställer en sömlös upplevelse samtidigt som decentraliseringen upprätthålls.



## Varför använda Matrix?



Matrix är inte bara ett alternativ till centraliserade meddelandesystem: det är en teknik som uppfyller verkliga behov när det gäller digital suveränitet, säkerhet och interoperabilitet. Det finns många skäl till att allt fler människor, företag och institutioner väljer det här protokollet för att kommunicera.



### Återta kontrollen över din kommunikation



De flesta meddelandeplattformar fungerar enligt en centraliserad modell: en enda aktör kontrollerar servrar, åtkomst, data och användningsregler. Denna modell innebär ett totalt beroende av leverantören.


Matrix har ett annat tillvägagångssätt.


Vem som helst kan välja var man vill ha sitt konto, eller till och med använda sin egen server. Ingen enhet har möjlighet att blockera en användare, kräva inträngande identifiering eller införa en policyförändring.


Denna arkitektur ger autonomi tillbaka till både individer och organisationer. Kommunikationen bygger inte längre på förtroende för ett företag, utan på ett öppet, dokumenterat och verifierbart protokoll.



### Säker, krypterad kommunikation



Matrix stöder end-to-end-kryptering för privata konversationer och grupper. Denna mekanism säkerställer att endast deltagare kan läsa meddelanden, även om de passerar genom tredjepartsservrar i federationen.



Protokollet använder Megolm/Olm-algoritmen, som är särskilt utformad för att ge stark säkerhet i distribuerade miljöer med flera enheter.



Detta gör det möjligt att :





- skydda känsliga konversationer,
- förhindra obehörig åtkomst (även från värdservern),
- upprätthålla konfidentialitet på lång sikt.



Kryptering är inte ett alternativ: det är en kärnkomponent i protokollet.



### Inte längre beroende av en enda applikation



Matrix är inte en applikation, utan ett protokoll.



Denna mångfald av kunder garanterar :





- ett val anpassat till individuella behov,
- möjligheten att använda Matrix på alla typer av enheter,
- inget beroende av en enda programvara.



Om en kund är olämplig eller upphör att underhållas väljer du helt enkelt en annan: kontot fortsätter att fungera normalt.



### Federering och sammankoppling av olika samhällen



Federation gör det möjligt för olika servrar att arbeta tillsammans samtidigt som de hanteras oberoende av varandra.


Således :





- en organisation kan hantera sin egen hemserver,
- individer kan ansluta sig till offentliga servrar,
- alla kan kommunicera med varandra som om de befann sig på samma plattform.



Denna flexibilitet gör det möjligt att skapa kommunikationsutrymmen som är anpassade till alla behov: team, föreningar, samhällen, institutioner eller projekt med öppen källkod.



Matrix är särskilt populär i tekniska kretsar, aktivistkollektiv, forskare, regeringar och i allt högre grad i Bitcoin-samhällen.



### Unik interoperabilitet i meddelandelandskapet



En av Matrix stora tillgångar är dess förmåga att **förlänga** börserna tack vare broar som kan länka samman :





- WhatsApp
- Telegram
- Signal
- Slack
- Discord
- IRC
- XMPP
- och många andra plattformar



Matrix blir därmed ett sammanhållande lager för kommunikation som för samman flera grupper som är utspridda över olika applikationer.



Denna interoperabilitet minskar fragmenteringen och förenklar samarbetet.



### Ett fritt, öppet och hållbart protokoll



Matrix-protokollet har helt öppen källkod och utvecklas på ett transparent sätt.


Detta garanterar flera fördelar:





- en kontinuerlig utveckling av standarden,
- möjlighet för vem som helst att kontrollera koden,
- oberoende av kommersiella eller politiska förändringar,
- långsiktig motståndskraft.



Till skillnad från proprietära meddelandesystem är framtiden för Matrix inte beroende av ett enda företag, utan av en global gemenskap och en öppen standard.



## Hur skapar jag ett Matrix-konto?



Det är enkelt att skapa ett Matrix-konto och det krävs inga tekniska kunskaper. Användare kan ansluta sig till en befintlig server, skapa en inloggning och börja chatta omedelbart. I detta avsnitt beskrivs de viktigaste stegen.



### Välj en server (offentlig eller privat)



Matrix är ett federerat nätverk: det finns ett stort antal servrar (hemservrar) som hanteras av olika organisationer, grupper eller enskilda personer. Valet av server avgör bara _var_ kontot finns, men förhindrar inte kommunikation med hela nätverket.


**Två alternativ är tillgängliga: **



### - Använd en offentlig server



Detta är den enklaste lösningen.


Exempel på populära servrar:





- _matrix.org_ (den mest kända)
- _envs.net_ _envs.net
- tematiska gemenskapsservrar (teknik, integritet, öppen källkod ...)



Dessa servrar är lämpliga för nybörjare som vill registrera sig snabbt.



### - Använd en privat server



Idealisk för :





- en organisation,
- en familj,
- ett projekt med öppen källkod,
- ett arbetslag,
- eller för suverän, självhanterad användning.



I det här fallet måste någon administrera servern (Synapse, Dendrite, Conduit...).


Oavsett vilken server du väljer kan användarna prata med varandra tack vare federation.



### Skapa ett konto steg för steg



Eftersom Matrix är ett öppet protokoll kan det användas av flera olika applikationer.


Som beskrivits ovan erbjuder de olika gränssnitt och funktioner beroende på kraven:





- Element**: den mest kompletta klienten, tillgänglig på alla plattformar.
- FluffyChat**: enkel, modern och perfekt för mobiler.
- Nheko**: lättviktig, ergonomisk klient för persondatorer.
- SchildiChat**: Element-variant med ergonomiska förbättringar.
- NeoChat**: integrerat i KDE:s ekosystem.



Valet av klient har ingen inverkan på kontot: alla fungerar med alla Matrix-server.



### Klassiska steg :





- Öppna den valda applikationen. I vårt fall gör vi detta med [Element](app.element.io).
- Välj "Skapa ett konto".



![cover-kali](assets/fr/10.webp)



För enkelhetens skull kan du skapa ett Matrix-konto med hjälp av **Google, Facebook, Apple, GitHub eller GitLab**. Dessa tjänster vet bara att deras konto har använts för att få åtkomst till Matrix: detta kallas en **social anslutning**.



För större sekretess kan du också registrera dig manuellt genom att välja ett **användarnamn**, ett **lösenord** och en **e-postadress**.



Beroende på vilken server som väljs kan en **captcha** krävas, liksom godkännande av **användarvillkoren**.



När registreringen har validerats skickas ett e-postmeddelande med en bekräftelse.


Klicka bara på länken för att aktivera ditt konto och få tillgång till webbapplikationen (Element) för att delta i dina första Matrix-konversationer.



![cover-kali](assets/fr/11.webp)



Du har nu ett konto och använder webbversionen av Element.



## Lägg till din första kontakt



För att kommunicera med någon på Matrix behöver du bara känna till deras fullständiga identifierare, som kallas **Matrix ID**.



Exempel:



`@alice:matrix.org @bened:monserveur.bj`



### Lägg till en kontakt



För att bjuda in vänner till din gruppchatt klickar du på cirkeln "i" i det övre högra hörnet. Då öppnas den högra panelen. Klicka på "People" för att visa listan över medlemmar i det här rummet: ni bör vara de enda som är närvarande just nu.



![cover-kali](assets/fr/12.webp)



Klicka på "Bjud in till det här rummet" högst upp i personlistan så öppnas en fråga där du kan bjuda in dina vänner att ansluta sig till dig i Matrix. Om de redan är inloggade i Matrix anger du deras Matrix-ID. Om de inte är det, ange deras e-postadress så kommer de att bjudas in att ansluta sig till oss.



Det finns inget "vän"-system: en kontakt är helt enkelt en person med vilken en konversation har inletts.



![cover-kali](assets/fr/13.webp)



Den person som du har bjudit in kan antingen acceptera eller avböja inbjudan. Om de accepterar bör du se dem gå med i rummet. Ju fler desto bättre!



![cover-kali](assets/fr/14.webp)



### Konfigurera din egen server



Matrix kommer verkligen till sin rätt när den används tillsammans med en personlig server.


Genom att distribuera din egen hemserver kan du :





- behålla fullständig kontroll över data,
- definiera sina egna regler för användning,
- vara värd för flera konton (vänner, team, community),
- och säkerställa maximal motståndskraft i händelse av restriktioner eller censur.



**Tillgängliga lösningar:**





- Synapse**: den historiska och mest kompletta implementationen.
- Dendrite**: Lättare, kraftfullare och utformad för protokollets framtid.
- Conduit**: en minimalistisk variant som är lätt att driftsätta.



**Förkunskaper:**





- ett domännamn,
- en maskin eller en VPS,
- minimikunskaper i systemadministration.



Även om det krävs en del konfigurering gör hanteringen av din egen server Matrix till ett suveränt och hållbart verktyg.



### Delta i dina första mässor



Matrix förlitar sig mycket på _rooms_ (vardagsrum).


Det finns offentliga, privata, kommunala, tekniska, lokala och internationella mässor.



**Tre sätt att gå med i en salong:**



1. **via en inbjudningslänk** (ofta i form av en URL med namnet `matrix.to`).


2. **Söker efter salongens namn** i ansökan.


3. **Genom att ange hela showens ID**, t.ex. :


`#bitcoin:matrix.org`


`#communauté-bénin:monsrv.bj`



När du har anslutit dig till chattrummet fungerar det som en klassisk nyhetsgrupp, med historik, kryptering, filer, reaktioner och audio-/videosamtal, beroende på vilken klient som används.



![capture](assets/fr/09.webp)



## Att gå vidare



När du har lärt dig grunderna erbjuder Matrix en mängd avancerade möjligheter. Oavsett om du vill ansluta andra meddelandesystem, vara värd för din egen server eller organisera en gemenskap, är ekosystemet mycket rikt.



### Broar (WhatsApp, Telegram, Signal, etc.)



En brygga kopplar Matrix till andra meddelandesystem.


Med den kan du skicka och ta emot meddelanden från :





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Discord
- Slack**
- IRC** (IRC)
- och många andra



### Vad broar kan göra





- Samla alla dina konversationer i Matrix
- Tillhandahålla ett öppet gränssnitt för interaktion med proprietära tjänster
- Hantera en community med flera plattformar från en enda plats



Vissa broar är officiella, andra är lokalt förankrade.


Beroende på avdelning kan de kräva :





- en personlig server,
- en ytterligare konfiguration,
- eller användning av en befintlig offentlig bro.



### Använda Matrix för en Bitcoin-organisation, ett samhälle eller ett projekt



Matrix är inte bara ett personligt verktyg.


Den kan användas för att strukturera arbetsgrupper, organisera lokala samhällen eller hantera projektkommunikation.



**Exempel på användning:**





- Gemenskaper för öppen källkod
- Bitcoin och ekosystemprojekt med blixtar
- Student- eller utvecklargrupper
- Medborgarorganisationer
- Oberoende medier
- Lokala grupper och föreningar



**Varför är det här intressant?





- verktyg med 100% öppen källkod**
- Suverän och decentraliserad** kommunikation
- Utrymmen organiserade i **lounger**, **undergrupper**, **privata lounger**, etc.
- Integrera med Nextcloud, GitLab, Mattermost eller anpassade bots
- Finjusterad hantering av behörigheter och moderering



Matrix blir då en kommunikationsbärare för alla strukturer som vill vara oberoende av de stora centraliserade plattformarna.



## Slutsats



Matrix är en modern, öppen och säker lösning för realtidskommunikation som erbjuder ett decentraliserat alternativ till traditionella plattformar. Tack vare den federerade arkitekturen och de avancerade krypteringsprotokollen kan användarna behålla kontrollen över sina data samtidigt som de får en smidig och interoperabel upplevelse. Oavsett om det gäller privat, professionellt eller samhälleligt bruk erbjuder Matrix ett robust och skalbart ramverk för att bygga kommunikationsmiljöer som är anpassade till dagens behov.



Om du vill veta mer och upptäcka alla funktioner som Matrix erbjuder kan du läsa den officiella dokumentationen som finns här :


[https://matrix.org/docs/](https://matrix.org/docs/)