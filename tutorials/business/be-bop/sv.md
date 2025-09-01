---
name: be-BOP
description: Praktisk guide till hur du tjänar pengar på ditt företag med be-BOP
---

![cover-bebop](assets/cover.webp)



**be-BOP** är en e-handelsplattform som är utformad för entreprenörer som vill sälja online och offline, helt självständigt, och samtidigt ta emot betalningar i Bitcoin, via ett bankkonto och i kontanter. Lösningen är också användbar för alla typer av organisationer som vill samla in donationer eller tjäna pengar på sina olika aktiviteter.



Lösningen är enkel, lätt och autonom. Den gör det möjligt att skapa en onlinebutik, även i en miljö där traditionella finansiella tjänster är begränsade eller saknas. **be-BOP** har utformats för att fungera effektivt med eller utan tillgång till banker, med Bitcoin som betalningsinfrastruktur.



I den här handledningen kommer vi att ta dig steg för steg genom:





- Skapa din första webbutik med **be-BOP**
- Anpassa ditt skyltfönster och dina produkter
- Konfigurera tillgängliga betalningsmetoder
- Förstå de bästa metoderna för att sälja effektivt online med **be-BOP**



Denna handledning kräver inga avancerade tekniska färdigheter. Den vänder sig till utvecklare samt hantverkare, handlare, kooperativ eller entreprenörer som vill börja med digital handel på ett suveränt och motståndskraftigt sätt.



## Förutsättningar för att installera be-BOP på din egen server



Innan du börjar installera be-BOP ska du se till att du har följande tekniska infrastruktur. Dessa Elements är nödvändiga för att plattformen ska fungera korrekt:



### S3-kompatibel lagring



be-BOP använder ett lagringssystem för att hantera filer (t.ex. produktbilder). Detta kräver tillgång till en S3-tjänst, till exempel:





- [MinIO](https://min.io/) självhanterande
- Amazon S3 (AWS)
- Scaleway Objektlagring



Du måste konfigurera en bucket och ange följande information:





- S3_BUCKET**: namn på skopan
- S3_ENDPOINT_URL**: länk till din S3-tjänst
- S3_KEY_ID** och S3_KEY_SECRET: dina åtkomstkoder
- S3_REGION**: regionen för din S3-tjänst



### MongoDB-databas i ReplicaSet-läge



be-BOP använder MongoDB för att lagra butiks-, användar-, produkt- och annan data.



Du har två alternativ:





- Installera MongoDB lokalt med **ReplicaSet-läge aktiverat**
- Använd en onlinetjänst som **MongoDB Atlas**



Du kommer att behöva följande variabler:





- MONGODB_URL**: databasanslutning Address
- MONGODB_DB**: databasens namn



## Node.js-miljö



be-BOP fungerar med Node.js. Se till att du har **Node.js** version 18 eller högre och **Corepack** aktiverat (behövs för att hantera pakethanterare som pnpm). Kommandot som ska köras är `corepack enable`



### Git LFS installerat



Vissa resurser (t.ex. stora bilder) hanteras via Git LFS (Large File Storage). Se till att du har Git LFS installerat på din maskin med kommandot `git lfs install`. När dessa förutsättningar är på plats är du redo att gå vidare till nästa steg: ladda ner och konfigurera be-BOP.



**En teknisk guide till programvarudistribution finns tillgänglig i en separat handledning.



## Skapa ett Super-Admin-konto



Den allra första gången be-BOP lanseras skapas ett **Super Admin**-konto. Det här kontot har alla behörigheter som krävs för att hantera backoffice-funktioner. Följ dessa steg för att skapa ett konto:





- Gå till `dinwebbplats/admin/login`
- Skapa ett superadmin-konto med en säker inloggning och ett säkert lösenord



Detta konto ger dig tillgång till alla backoffice-funktioner. När du har skapat kontot kan du logga in genom att ange ditt användarnamn och lösenord.



![login](assets/fr/001.webp)



## Konfiguration och säkerhet för backoffice



Innan du konfigurerar din Interface-backofficeanslutning måste du skapa en unik Hash. Detta ger skydd mot illvilliga aktörer som försöker stjäla anslutningslänken till din Interface-administratör.



För att skapa Hash, gå till `/admin/Settings`. I avsnittet för säkerhet (t.ex. "Admin Hash") definierar du en unik sträng (Hash). När du har registrerat dig kommer webbadressen till backoffice att ändras (t.ex. `/admin-yourhash/login`) för att begränsa åtkomsten för obehöriga personer.



![hash-login](assets/fr/002.webp)



2.2. Aktivera underhållsläge (om nödvändigt)



Fortfarande i /admin/Inställningar, (Inställningar > Allmänt via Interface grafik) kontrollera alternativet "aktivera underhållsläge" längst ner på sidan.



![maintenance-mode](assets/fr/003.webp)



Om det behövs kan du ange en lista med auktoriserade IPv4-adresser (separerade med kommatecken) för att möjliggöra åtkomst till front office under underhåll. Backoffice förblir tillgängligt för administratörer.



![ip-bebop](assets/fr/004.webp)



## Inställningar för kommunikation



För att be-BOP ska kunna skicka meddelanden (t.ex. för beställningar, registreringar eller systemmeddelanden) måste du konfigurera minst en kommunikationsmetod. Två alternativ finns tillgängliga: e-post (SMTP) eller Nostr.



### SMTP-konfiguration (e-post)



be-BOP kan skicka e-post via en SMTP-server. Du behöver giltiga SMTP-referenser, som ofta tillhandahålls av en e-posttjänst (t.ex. Mailgun, Gmail etc.).



Här är vad du behöver veta:



SMTP_HOST: SMTP-server Address (t.ex. smtp.mailgun.org)



SMTP_PORT: den port som ska användas (ofta 587 eller 465)



SMTP_USER: ditt användarnamn (vanligtvis ett e-postmeddelande Address)



SMTP_PASSWORD: ditt lösenord eller din API-nyckel



SMTP_FROM: det e-postmeddelande Address som kommer att visas som avsändare




### Nostr-konfiguration



be-BOP gör att du kan skicka meddelanden via Nostr-protokollet, en decentraliserad meddelandeinfrastruktur. För att göra detta måste du generate eller Supply en Nostr privat nyckel (NSEC). Du kan generate denna nyckel direkt via be-BOP:s Interface, i avsnittet som är dedikerat till Nostr. När dessa Elements är korrekt konfigurerade kommer be-BOP automatiskt att kunna skicka meddelanden och varningar till dina användare.



## Kompatibla betalningsmetoder



be-BOP är kompatibelt med flera betalningslösningar, vilket gör att du kan erbjuda dina kunder större flexibilitet. Här är vad du behöver för att ställa in den betalningsmetod som passar dig bäst.



### Bitcoin Onchain



med be-BOP kan du ta emot Bitcoin-betalningar direkt på Blockchain (On-Chain), enkelt och säkert.



**Konfigurationssteg:**





- Gå till menyn **Payment Settings** (Betalningsinställningar)
- Klicka på **Bitcoin Nodeless** för att komma åt On-Chain betalningsparametrar.
- Fyll i följande fält:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Tips:** För att få din utökade publika nyckel (Zpub) kan du konsultera de avancerade inställningarna för din Bitcoin Wallet (Sparrow wallet, BlueWallet, Specter, etc.). Se till att din Wallet är **inte skrivskyddad** om du avser att använda transaktionshistorik.



### Lightning Network



be-BOP kan också acceptera omedelbara Bitcoin-betalningar tack vare Lightning Network. Två konfigurationsalternativ är för närvarande tillgängliga:



**Phoenixd**



Gå till menyn `Betalningsinställningar`, klicka på `Phoenixd`



![phoenixd](assets/fr/006.webp)



Du måste sedan ange **lösenordet eller token-autentiseringen** som ansluter dig till din Phoenixd-instans, en backend som utvecklats av Acinq som låter dig hantera Lightning-betalningar med din egen nod, men utan komplexiteten i att hantera betalningskanaler.



**Swiss Bitcoin Betalning**



Om du inte vill hantera en Lightning-nod själv är **Swiss Bitcoin Pay** en färdig lösning som är enkel att använda och konfigurera och som är perfekt för att börja acceptera Lightning-betalningar utan en komplex infrastruktur.



Konfigurationssteg:





- I menyn "Betalningsinställningar" klickar du på `Swiss Bitcoin Pay`
- Logga in på ditt schweiziska Bitcoin Pay-konto (eller skapa ett om du inte redan har ett).
- Ange API-nyckeln som tillhandahålls av Swiss Bitcoin Pay och klicka sedan på "Spara"



När be-BOP har konfigurerats kommer det automatiskt att skicka generate Lightning-fakturor till dina kunder, och du kommer att ta emot betalningar direkt till ditt schweiziska Bitcoin Pay-konto. Den här lösningen är perfekt för användare som vill undvika den tekniska komplexiteten med en personlig nod och samtidigt ta emot snabba betalningar till låg kostnad.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Förutom Bitcoin kan du med be-BOP också ta emot kontantbetalningar via PayPal, en välkänd och allmänt använd internationell lösning.



Konfigurationssteg:





- Gå till menyn "Betalningsinställningar
- Klicka på `PayPal
- I ditt Paypal-konto (utvecklarsektionen) anger du `Client ID` och `Secret`
- Välj den valuta du vill ha (t.ex. **USD**, **EUR**, **XOF**, etc.)
- Klicka på `Spara



![paypal](assets/fr/008.webp)



**Du måste ha ett PayPal-företagskonto för att kunna använda generate för dessa identifierare. Du kan få dem via [developer]-portalen (https://developer.paypal.com)



### SumUp



Programvaran integrerar nu betalningslösningen **SumUp**, vilket gör att du kan ta emot kreditkortsbetalningar på ett enkelt, säkert och effektivt sätt. För att dra nytta av denna funktionalitet krävs en inledande konfiguration. Här är stegen som ska följas, numrerade för en tydlig och progressiv implementering:





- Börja med att ange din **API-nyckel**, en konfidentiell nyckel som tillhandahålls av SumUp när du skapade ditt utvecklarkonto. Den upprättar en säker anslutning mellan ditt SumUp-konto och programvaran.
- Fyll i fältet `Merchant Code` med den unika kod som identifierar ditt företag inom SumUp-plattformen. Denna kod är nödvändig för att kunna koppla transaktioner till ditt företag.
- I fältet "Currency" väljer du den huvudvaluta som du använder för dina transaktioner (t.ex. **EUR**, **USD**, **CDF**, etc.).
- När alla fält har fyllts i korrekt klickar du på knappen "Spara" för att spara dina inställningar. Systemet kommer sedan att upprätta länken till ditt SumUp-konto och din programvara är redo att ta emot betalningar.



![payment-sumup](assets/fr/009.webp)



Efter denna konfiguration kommer **SumUp**-integrationen att vara aktiv och i drift, så att du snabbt kan ta ut pengar och spåra dina transaktioner direkt från programvaran.



### Randig



be-BOP erbjuder också full integration med **Stripe**, en av de mest populära betalningsplattformarna online. Med Stripe kan du ta emot betalningar online via kreditkort, digital Wallet och flera andra betalningsmetoder. Så här aktiverar du det:





- Ange den **hemliga nyckel** som anges i Stripe-panelen.
- Fyll i fältet **Public Key**, som också tillhandahålls av Stripe.
- Välj **huvudvaluta**.
- Spara konfigurationen och klicka sedan på `Save`.



![payment-stripe](assets/fr/010.webp)



⚠️ **Observera:** Det är viktigt att känna till det momssystem som gäller för din verksamhet (t.ex.: försäljning med moms i säljarens land, undantag enligt motivering eller försäljning till momssatsen i köparens land) för att korrekt kunna konfigurera faktureringsalternativen i **be-BOP**.



## Konfiguration av valuta



**be-BOP** erbjuder avancerad valutahantering och är anpassat till miljöer med flera valutor och specifika redovisningskrav. För att säkerställa konsekvens i finansiella transaktioner och rapportering är det viktigt att korrekt konfigurera de olika valutorna som används i systemet. Här följer de steg som ska följas för denna konfiguration:





- Välj **huvudvaluta** (`Huvudvaluta`)
- Välj `Sekundär valuta
- Definiera **referensvaluta** (`Prisreferensvaluta`)
- Ange "Redovisningsvaluta



När alla valutor har konfigurerats på rätt sätt säkerställer programvaran automatisk och korrekt konvertering av transaktioner i flera valutor, samtidigt som den upprätthåller en strikt redovisningskonsistens.



![settings-currencies](assets/fr/011.webp)



## Konfiguration av åtkomst till återställning via e-post eller Nostr



Fortfarande i `/admin/settings`, via **ARM**-modulen, ska du se till att superadmin-kontot innehåller en **email Address** eller en **recovery pub**, vilket underlättar proceduren om du glömmer ditt lösenord.



![settings-users](assets/fr/012.webp)



## Språkinställningar



Programvaran kan användas på flera språk för att anpassa sig till en internationell publik och förbättra användarupplevelsen. För att aktivera den flerspråkiga funktionen är det viktigt att konfigurera de tillgängliga språken och definiera ett **standardspråk**.



![settings-languages](assets/fr/13.webp)



## Interface och Identity-konfiguration i be-BOP



**be-BOP** ger designers alla verktyg de behöver för att designa en webbplats. Det första steget är att öppna avsnittet `/Admin > Merch > Layout` i inställningarna. Börja med att konfigurera **Top Bar**, **Navbar** och **Footer**.



### Le Top Bar



Med konfigurationen **Top Bar** kan du anpassa din programvaras visuella identitet genom att visa viktig information direkt på första raden i Interface. Detta förstärker varumärkesigenkänningen och ger ett tydligt sammanhang för användarna.



#### Konfigurationssteg:





- I fältet "Varumärke" anger du namnet på ditt företag, din organisation eller din produkt. Detta namn kommer att visas högst upp på Interface och kommer att representera din huvudsakliga visuella identitet.
- Ange webbplatsens titel**: den valda titeln bör sammanfatta syftet med plattformen. Denna titel kan visas i sidhuvudet eller i webbläsarfliken.
- Add Website description**: här kan du skriva en kort beskrivning av ditt initiativ. Beskrivningen hjälper användarna att sätta verktyget i ett sammanhang och kan även användas för SEO-ändamål.



När denna information har matats in kommer **Top Bar** att visa en tydlig, professionell och sammanhängande presentation av din lösning.



#### Länkar i det övre fältet



I Top Bars avsnitt "Länkar" kan du lägga till genvägar till viktiga sidor i din applikation eller på externa webbplatser. Dessa länkar visas direkt i Top Bar och ger dina användare snabb och strukturerad åtkomst.



#### Konfigurationssteg:





- Ange länknamn (Text)**: i fältet "Text" anger du namnet eller etiketten på länken så som den kommer att visas (t.ex. Hem, Kontakt, Hjälp...).
- Ange länk Address (Url)**: i fältet `Url` anger du hela Address för målsidan (intern eller extern).
- Lägg till andra länkar vid behov**: på varje konfigurationsrad kan du lägga till en ytterligare länk med hjälp av fälten "Text" och "URL".
- Spara länkar**: När alla länkar har angetts klickar du på knappen "Add top bar link" för att spara dem.



Med den här konfigurationen kan du erbjuda tydlig, smidig och tillgänglig navigering genom de olika delarna av din webbplats eller till kompletterande resurser.



![settings-topbar](assets/fr/014.webp)



### La Nav Bar



I avsnittet **Navbar** kan du konfigurera be-BOP:s huvudmeny för navigering, som vanligtvis finns på sidan eller överst i Interface. Denna meny vägleder användarna till applikationens olika sidor och funktioner. Konfigurationen av länkarna är enkel och intuitiv. Så här fungerar det:





- Ange länknamn (`Text`)**: På konfigurationsraden börjar du med att fylla i fältet `Text`. Detta motsvarar namnet på den länk som visas i navigeringsfältet (exempel: *Dashboard*, *Users*, *Settings*...).
- Ange länkens Address (`Url`)**: bredvid fältet `Text` hittar du fältet `Url`. I det här fältet anger du Address för den sida som länken ska omdirigera till. Detta kan vara en intern rutt eller en länk till en extern sida.
- Lägg till flera länkar om det behövs**: under den första raden finns nya fält för "Text" och "URL" där du kan lägga till så många länkar som behövs. Varje rad representerar ytterligare en navigeringslänk.
- Spara länkar**: När du har angett alla Elements klickar du på knappen "Lägg till länk i navigeringsfältet" för att spara och visa resultaten i navigeringsfältet.



Denna konfiguration gör det möjligt att på ett effektivt sätt strukturera åtkomsten till olika delar av programvaran, vilket förbättrar ergonomin och användarupplevelsen.



![navbar](assets/fr/015.webp)



### Sidfoten



I avsnittet **Footer** kan du anpassa sidfoten i din programvara och lägga till användbar information eller länkar. Innan du konfigurerar länkarna ska du börja med att aktivera ett visst alternativ:





- Aktivera visning av etiketten "Powered by be-BOP"**: aktivera knappen `Display Powered by be-BOP` för att visa denna etikett i sidfoten.
- Ange namnet på länken (`Text`)**: fyll i fältet `Text`, som motsvarar länkens ordalydelse i sidfoten (exempel: *Villkor*, *Privacy*, *Kontakt*...).
- Ange länkens Address (`Url`)**: i fältet `Url` anger du målsidans Address (intern eller extern).
- Lägg till fler länkar om det behövs**: använd de extra raderna för att skapa så många länkar som du vill.
- Spara länkar**: klicka på knappen "Add footer link" för att spara länkar.



![footer](assets/fr/016.webp)



### Visuell personalisering



**⚠️ Glöm inte att ställa in logotyperna för de ljusa och mörka teman, samt favicon, via** `Admin > Merch > Pictures`.



Så här anpassar du utseendet och känslan på din webbplats:



#### Gå till avsnittet Bilder



Meny `Admin` > `Merch` > `Bilder`.



#### Lägg till en ny bild



Klicka på `Ny bild`.



#### Välj en lokal fil



Klicka på `Choose Files` och välj sedan en bild från din Hard-disk.



#### Välj den fil som ska importeras



Dubbelklicka på den bild som ska importeras (ljus logotyp, mörk logotyp eller favicon).



#### Namnge bilden



Fyll i fältet `Bildens namn`.



#### Lägg till bild



Klicka på "Lägg till" för att slutföra importen.



![pictures](assets/fr/017.webp)



### Inställning av säljaridentitet



#### Inställningar för identitet



I det här avsnittet, som nås via `Admin > Identity` (eller `Settings > Identity`), kan du konfigurera företagets administrativa och juridiska information.



#### Juridisk information





- Företagsnamn**: officiellt företagsnamn.
- Företagsidentifikation**: juridisk identifikation eller registreringsnummer (RCCM, SIRET...).



#### Företag Address





- Street**: postnummer Address (gata, nummer ...).
- Land**: land.
- Delstat**: provins eller region.
- Stad**: stad.
- Postnummer**: postnummer.



#### Kontaktuppgifter





- E-post**: professionell e-post Address.
- Phone**: företagets telefonnummer.



#### Bankkonto





- Kontohavarens namn**: Kontohavarens namn.
- Kontohavare Address**: innehavarens Address.
- IBAN**: Internationellt bankkontonummer.
- BIC**: SWIFT/BIC-kod.



![bank-account](assets/fr/019.webp)



#### Fakturering





- Klicka på "Fyll i information om huvudbutiken" för att fylla i uppgifterna.
- Information om utställaren**: fält för juridisk information/skatteinformation som visas på fakturor.
- Klicka på `Uppdatera` för att spara ändringarna.



**Du kan också ange ytterligare information som ska visas på Invoice, beroende på dina behov.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Fysisk butik Address



För de som har en fysisk butik, lägg till en specifik fullständig Address i `Admin > Settings > Identity` eller ett dedikerat avsnitt. Detta gör att den kan visas på officiella dokument och i sidfoten vid behov.



![seller-id](assets/fr/021.webp)



## Produkthantering



### Skapa en ny produkt



Gå till `Admin > Merch > Products` för att lägga till eller ändra en produkt. Fyll i följande fält:



#### Grundläggande information





- Produktnamn**: Produktens namn (t.ex. *BOP T-shirt limited edition*).
- Slug**: URL-identifierare utan mellanslag (t.ex. `tshirt-bop-edition-limitee`).
- Alias** *(valfritt)*: användbart för att snabbt lägga till i korgen via ett särskilt fält.



![product-config](assets/fr/028.webp)



#### Prissättning





- Prisbelopp**: produktpris (t.ex. "25,00").
- Prisvaluta**: valuta (EUR, USD, BTC, etc.).
- Specialprodukter**:
  - detta är en gratis produkt.
  - detta är en betala-vad-du-vill-produkt.



#### Produktalternativ





- Enkel produkt (`standalone`)**: endast ett tillägg möjligt per beställning (t.ex. donation, inträdesbiljett).
- Produkt med variationer**:
  - Kolla inte "Standalone".
  - Markera `Produkten har lätta variationer (ingen lagerskillnad)`.
  - Lägg till:
    - Namn** (t.ex. *Storlek*),
    - Värden** (t.ex.: S, M, L, XL),
    - Prisskillnader** om tillämpligt (t.ex.: `+2 USD` för XL).



![product-details](assets/fr/029.webp)



## Lagerhantering



### Avancerade alternativ när du skapar en produkt (lager, leverans, biljetter etc.)



#### Produkt med begränsat lager



Om din produkt inte finns tillgänglig i obegränsade kvantiteter, markera `Produkten har ett begränsat lager`. Detta aktiverar automatisk spårning av återstående kvantiteter. När denna ruta är markerad visas ett fält för att ange **tillgängligt lager**.



Systemet hanterar:





- Reserverat lager** → produkter i korgar som ännu inte har betalats
- Sålt lager** → redan köpta produkter



**Reservationstid för korg**: När en kund lägger till en produkt i sin varukorg "reserveras" den under en begränsad tid. Du kan ändra den här tiden i: `Admin > Konfig > Korgreservation` (värde i minuter)



#### Produkt som ska levereras?



Markera `Produkten har en fysisk komponent som kommer att skickas till kundens Address`. Detta är användbart för alla produkter som ska skickas fysiskt (böcker, t-shirts, etc.)



#### Andra alternativ





- Ticket**: kryssa i om produkten är en biljett till ett evenemang
- Bokning**: kontrollera om detta är en bokningsplats (t.ex.: session, möte)



![product-options](assets/fr/030.webp)



### Inställningar för åtgärder (nederst)



Detta avsnitt bestämmer **var** och **hur** produkten kan ses och köpas:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Markera endast de kanaler som du vill använda.



## Skapande och anpassning av CMS-sidor och widgets



### Obligatoriska CMS-sidor



Gå till `Admin > Merch > CMS`. Du kommer att se en lista över befintliga sidor och kan lägga till nya med **Lägg till CMS-sida**.



CMS-sidor är viktiga för:





- Informera dina besökare (t.ex. användarvillkor)
- Följa lagen (t.ex. integritetspolicy)
- Förklara vissa funktioner i butiken (t.ex. IP-kollektion, 0% moms)



Du kan lägga till andra sidor efter behov:





- Om oss / Vilka vi är
- Stöd oss / Donationer
- VANLIGA FRÅGOR
- Kontakt
- etc.



**Tips: Klicka på varje länk eller ikon för att ändra **innehåll**, **titel** eller **seo synlighet** för varje sida.



### Layout och grafik Elements



Gå till: administratör > Merch > Layout. Du kan anpassa den visuella Elements på din webbplats:



![product-options](assets/fr/032.webp)



#### Översta baren





- Ändra eller ta bort länkar (EX: HOME, ABOUT US,...)
- Navigering mellan viktiga delar av webbplatsen



#### Navbar (huvudnavigeringsfält)





- Finns i det grå området under det övre fältet
- Innehåller snabb åtkomst till: `Config`, `Payment Settings`, `Transaction`, `Node Management`, `Widgets`, etc.
- Endast styrelseledamöter



#### Sidfot





- Kan redigeras från `Admin > Merch > Layout`
- Innehåller: kontaktinformation, användbara länkar, juridiska meddelanden...



#### Anpassa bilderna



Gå till: `Admin > Merch > Bilder`



Du kan:





- Ändra **huvudsaklig logotyp**
- Ändra eller lägg till layout **bilder**



#### Beskrivning av webbplatsen



Den kan också ändras i `Pictures` och gör att du kan visa en **sammanfattning eller slogan** i sidhuvudet eller sidfoten, beroende på tema.



**Anmärkning:** Detta gör att du kan anpassa utseendet till din varumärkesidentitet (utbildning, kommersiellt eller samhälle).



### Integrera widgetar i CMS-sidor



Widgets** berikar dina CMS-sidor med dynamiska eller visuella Elements.



#### Skapande av widgetar



Gå till: `Admin > Widgets`



Exempel på tillgängliga widgets:





- Utmaningar**: utmaningar eller uppdrag
- Taggar**: kategorier eller nyckelord
- Sliders**: bildkaruseller
- Specifikationer**: Specifikationer tabeller
- Formulär**: formulär (kontakt, feedback, etc.)
- Nedräkningar**: timers
- Gallerier**: bildgallerier
- Ledartavlor**: användarnas ranking



![widgets](assets/fr/033.webp)



#### Integrering i CMS-sidor



Använd **shortcodes** i innehållet på dina CMS-sidor:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Aktuella parametrar**:





- `slug`: unik widgetidentifierare
- `display=img-1`: produktspecifik bild
- `width`, `height`, `fit`: bilddimensioner och stil
- autoplay=3000`: tid i ms mellan två bilder



**Fördelar**:





- Lätt att infoga (kopiera och klistra in)
- Dynamisk: alla ändringar av widgeten återspeglas automatiskt
- Ingen utvecklare krävs



## Orderhantering och rapportering



### Spårning av order



För att se och hantera tidigare beställningar, gå till: `Admin > Transaktion > Order`



Här hittar du en **fullständig lista över beställningar** som gjorts på din webbplats.



![orders](assets/fr/034.webp)



#### Visualisering och sökning



Med Interface kan du söka och filtrera order enligt flera kriterier:





- ordernummer: ordernummer
- produktalias: identifiering eller namn på produkten
- payment Mean": betalningsmetod som används (kort, krypto, etc.)
- e-post: kundens e-postadress



Dessa filter underlättar snabba sökningar och målinriktad hantering.



#### Detaljer om varje order



Genom att klicka på en order kan du få tillgång till en komplett fil som innehåller:





- Beställda produkter
- Information till kunder
- Leverans Address (om tillämpligt)
- Eventuella anteckningar som är kopplade till ordern



#### Möjliga åtgärder på en order



Du kan:





- Bekräfta ordern (om den är under behandling)
- Avbeställa en order (i händelse av problem eller kundförfrågan)
- Lägg till **etiketter** (för intern organisation)
- Konsultera / lägg till **interna anteckningar**



**Anmärkning:** Detta avsnitt är viktigt för god logistik och kundrelationer.



### Rapportering och export



För att få tillgång till försäljnings- och betalningsstatistik:


administratör > Inställningar > Rapportering



![reporting](assets/fr/035.webp)



Här hittar du en översikt över din verksamhet i form av **månads- och årsrapporter**.



#### Rapportera innehåll



Rapporterna är indelade i avsnitt:





- Order Detail**: antal order, status (bekräftad, avbokad, pågående), utveckling
- Produktdetaljer**: sålda produkter, kvantiteter, populära produkter
- Payment Detail**: inkasserade belopp, uppdelning per betalningsmetod



#### Export av data



Varje avsnitt innehåller en **Export CSV**-knapp, som gör att du kan:





- Ladda ner data i CSV-format
- Öppna dem i Excel, Google Sheets etc.
- Arkivering för administrativ eller redovisningsmässig användning
- Använd dem för interna rapporter



**Perfekt för resultatuppföljning, redovisning och presentationer.



## Konfiguration av Nostr Messaging (tillval)



![nostr-config](assets/fr/036.webp)



Plattformen stöder **Nostr**-protokollet för vissa avancerade funktioner:





- Decentraliserade meddelanden
- Logga in utan lösenord
- Interface ljusstyrning



### Generera och lägga till den privata nyckeln för Nostr



Gå till:


admin > Node Management > Nostr





- Klicka på **Create nsec** om du inte redan har en.
- Systemet kan generate det automatiskt.
- Alternativt kan du använda en befintlig nyckel (t.ex. från Damus eller Amethyst).



Nästa:





- Kopiera `nsec`-nyckeln
- Lägg till den i filen `.env.local` (eller `.env`): ```env NOSTR_PRIVATE_KEY=DinNsecIciKey



### Funktioner aktiverade med Nostr



När konfigurationen är klar finns flera funktioner tillgängliga:



**Notifieringar via Nostr**





- Skicka aviseringar om order, betalningar eller systemhändelser
- För administratörer eller användare



**Interface lätt administration**





- Tillgänglig via en Nostr-klient
- Möjliggör snabb, mobilvänlig hantering



**Uppkoppling utan lösenord**





- Inloggning via säker länk (skickas via Nostr)
- Ökad användarsäkerhet och smidighet



## Anpassning av design och tema



För att anpassa utseendet på din butik till din grafiska charter, gå till: `Admin > Merch > Tema`



Här hittar du alla alternativ för att **skapa** och **konfigurera** ett anpassat tema.



### Skapa ett tema



![theme](assets/fr/037.webp)



När du skapar eller ändrar ett tema kan du definiera:





- Färger**: för knappar, bakgrunder, text, länkar etc.
- Typsnitt**: val av typsnitt för rubriker, stycken, menyer
- Grafiska stilar**: ramar, marginaler, avstånd, blockformer



### Anpassningsbara sektioner



Varje del av anläggningen kan justeras oberoende av varandra:





- Header**: övre navigeringsfältet
- Body**: huvudinnehåll
- Sidfot**: längst ner på sidan



**Anmärkning:** Denna detaljnivå säkerställer överensstämmelse mellan webbplatsens visuella element och ditt varumärkes identitet.



### Aktivering av tema



När temat är konfigurerat:





- Klicka på **Spara**
- Aktivera det som butikens **huvudtema**



**Det aktiva temat är det som kommer att vara synligt för besökare.



## Konfigurera e-postmallar



Med plattformen kan du anpassa de e-postmeddelanden som skickas automatiskt till användarna. Gå till: `Admin > Inställningar > Mallar`



![emails-templates](assets/fr/038.webp)



### Skapa / redigera mallar



Varje e-postmeddelande (orderbekräftelse, glömt lösenord etc.) har:





- Ämne**: ämnet för e-postmeddelandet (t.ex. "Din order har validerats")
- HTML-kod**: HTML-innehåll som visas i e-postmeddelandet



**Du kan infoga text, bilder, länkar etc. efter behov.



### Använda dynamiska variabler



För att göra e-postmeddelanden dynamiska kan du infoga variabler som:





- `{orderNumber}}`: ersätts av det faktiska ordernumret
- röstlänk: länk till Invoice
- `{webbplatslänk}}`: URL till din webbplats



**Note:** dessa taggar ersätts automatiskt när de skickas.



### Avancerade tips





- Skapa e-postmeddelanden som är **responsiva** så att de är lätta att läsa på mobila enheter
- Lägg till **handlingsknappar** (betala, ladda ner, spåra order)
- Testa dina e-postmeddelanden genom att skicka dem till dig själv innan du publicerar dem



## Konfigurera specifika taggar och widgets



### Hantering av taggar



Taggar kan användas för att strukturera och berika ditt innehåll. För att komma åt dem: `Admin > Widgets > Taggar`



![tags-config](assets/fr/039.webp)



### Skapa en tagg



Fyll i följande fält:





- Taggens namn**: taggens namn visas
- Slug**: unik identifierare (inga mellanslag eller accenter)
- Taggfamilj**: grupperar taggar efter kategori



![targsconfig](assets/fr/040.webp)



#### Tillgängliga familjer:





- creators": författare eller producenter
- detaljister: försäljare eller försäljningsställen
- tidsmässigt: perioder eller datum
- händelser: associerade händelser



### Valfria fält



Dessa fält kan användas för att berika en tagg som om den vore en innehållssida:





- Titel
- Undertitel
- Kort** innehåll
- Fullständigt innehåll** (på franska)
- CTA** (åtgärdsknappar)



### Använda taggar



Etiketter kan vara:





- Fördelat till produkter
- Integreras i CMS-sidor med en tagg: [Tagg=slug?display=var-1]



## Konfiguration av nedladdningsbara filer



För att erbjuda nedladdningsbara dokument till dina kunder: `Admin > Merch > Files`



### Lägga till en fil



1. Klicka på **Ny fil**


2. Informera:




   - Filnamn** (t.ex. *Installationsguide*)
   - Fil att ladda upp** (PDF, bild, Word...)



**Note:** när den har lagts till genererar plattformen automatiskt en **permanent länk**.



### Använda länken



Denna länk kan sedan sättas in i:





- CMS**-sida (som textlänk eller knapp)
- En **e-postklient** (via en mall)
- Ett **produktblad** (t.ex. nedladdning av bruksanvisning)



Det är perfekt för att tillhandahålla *användarhandböcker, tekniska guider, produktblad ...* utan behov av extern hosting.



## Nostr-bot



Plattformen erbjuder avancerad integration med **Nostr**-protokollet via en automatiserad bot.



Gå till: nodhantering > Nostr



### Huvudsakliga egenskaper



#### Hantering av reläer





- Lägg till eller ta bort **reläer** som används av boten
- Optimera **räckvidden** och **tillförlitligheten** för skickade meddelanden



#### Automatiskt introduktionsmeddelande





- Aktivera ett automatiskt meddelande vid **första användarinteraktionen**
- Idealisk för:
  - Presentera din tjänst
  - Skicka en användbar länk (t.ex. FAQ, kontakt, beställning)



#### Certifiering av din `npub





- Lägg till en **logotyp** och ett **offentligt namn**
- Länk till en **verifierad webbdomän**
- Förbättrar trovärdigheten och igenkänningen av din Nostr-identitet



### Användningsfall för Nostr-bot





- Skickar **orderbekräftelser** till dig
- Automatisk respons på **händelser (t.ex. ny order)**
- Skapa en **decentraliserad kundinteraktion**



## Överbelastning av översättningsetiketter



be-BOP är flerspråkig (FR, EN, ES...), men du kan anpassa översättningarna efter dina behov.



För att göra detta, gå till: `Inställningar > Språk`



### Laddning och redigering



Översättningsfilerna är i JSON-format. Du kan:





- Ladda ner** språkfiler
- Ändra** befintliga texter
- Lägg till** dina egna översättningar



Länk till originalfiler:


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Exempel:** ersätt `Add to cart` med `Ajouter au panier` eller `Acheter`.



## Lagarbete och försäljningsställen (POS)



### Hantering av användar- och åtkomsträttigheter



#### Skapa roller



Gå till: administratör > Inställningar > ARM



Klicka på **Create a role** för att skapa en roll (t.ex. `Super Admin`, `POS`, `Ticket checker`).



Varje roll innehåller:





- skrivbehörighet**: skrivbehörighet
- läsbehörighet**: läsbehörighet
- förbjudet tillträde**: sektioner interdites



#### Skapande av användare



I samma meny `Admin > Inställningar > ARM` lägger du till en användare med:





- logga in
- alias
- återställning av e-post
- (valfritt) `recovery npub` för anslutning via Nostr



Tilldela en tidigare definierad roll.



![pos-users](assets/fr/045.webp)



Skrivskyddade** användare ser menyerna i *italic* och kan inte ändra innehållet.



## Konfiguration av försäljningsställen (POS)



### Tilldela POS-rollen



För att ge en användare tillgång till POS, tilldela rollen `Point of Sale (POS)` i: administratör > Konfig > ARM



Han kan ansluta via den säkra URL:en: `/pos` eller `/pos/touch`



### POS-specifika funktioner



Be-BOP erbjuder en Interface för fysisk försäljning (butik, evenemang etc.).



#### Snabbt tillägg via alias



I `/cart` finns ett fält där du kan lägga till en produkt:





- Genom att skanna en **streckkod** (ISBN, EAN13)
- Genom att ange ett **produktalias** manuellt



**Obs:** produkten läggs automatiskt i varukorgen.



#### Betalningsmedel



POS stöder:





- Arter
- Kreditkort
- Lightning Network (krypto)
- Andra enligt konfiguration



Två avancerade alternativ finns tillgängliga:





- Momsbefrielse**: tillämplig på motivering (icke-statliga organisationer, utlänningar...)
- Presentrabatt**: exceptionell rabatt med obligatorisk kommentar



#### Visning på klientsidan



URL:en `/pos/session` är avsedd för en **sekundär skärm** (HDMI, surfplatta...):



Poster:





- Produkter under tillverkning
- Totalt belopp
- Betalningsmetod
- Rabatter tillämpas



**Note:** kunden följer ordern live, medan säljaren registrerar den på `/pos`.



### POS-sammanfattning



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Tack för att du följer denna handledning noggrant.