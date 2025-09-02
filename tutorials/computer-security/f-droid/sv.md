---
name: F-Cold
description: Katalogen över applikationer med fri och öppen källkod.
---

![cover](assets/cover.webp)



I den digitala tidsåldern arbetar stora företag och institutioner för att göra Internet mer centraliserat, lägga kontrollen över det i sina egna händer och därmed hindra alla användares integritet och frihet. Detta är inte en utopi, det händer redan. Som bitcoiner är decentralisering, respekt för integritet och individuella friheter principer som du håller kära, särskilt i de verktyg du använder dagligen. Android, till skillnad från iOS, har i flera år tillåtit flera appbutiker att samexistera inom sitt ekosystem, vilket ger dig friheten att hitta och installera appar från dina favoritkällor.



I den här handledningen kommer vi att titta på F-droid, en applikationskatalog som representerar ett alternativ till applikationsbutiker som Google Play Store och Microsoft Store.



## Komma igång med F-Droid



F-Droid är en applikations- och verktygsbutik som låter dig installera gratis applikationer med öppen källkod på Android-plattformen. F-droid är i sig ett projekt med öppen källkod som startades 2010 av Ciaran Gultnieks och flera andra bidragsgivare. Huvudsyftet med projektet är att göra applikationer med öppen källkod tillgängliga och att göra det möjligt för initiativtagare till projekt med öppen källkod att hitta en plattform där de kan publicera sina verktyg utan att behöva hänvisa till Google Play Store.



Tyvärr är F-Droid inte en applikation som är tillgänglig på iOS och innehåller många verktyg som är utformade för Android-system.



Du kan ladda ner F-droid från [den officiella webbplatsen] (https://f-droid.org/) i APK-format och installera det manuellt på din Android-telefon.



![download](assets/fr/02.webp)



På Android, se till att du ger installationsbehörighet för webbläsaren från vilken du hämtade F-Droid.



När installationen är klar kommer F-Droid att starta en uppdatering av Open Source-applikationskatalogerna för att berika applikationerna i butiken.



![repositories](assets/fr/03.webp)



Du kan nu installera applikationer på din telefon utan att gå via Google Play Store.



## Bokhandeln F-Droid



I Application Store hittar du flera olika kategorier av applikationer som passar dina behov. På fliken **Categories** hittar du över 20 typer av applikationer, från webbläsare till fritextredigerare, och alla kräver så lite information som möjligt från din sida.



Vill du installera en specifik applikation? Klicka på knappen **Sök** och ange sedan namnet på det program du letar efter.



![search](assets/fr/04.webp)



F-Droid ger omfattande information om varje applikation som du vill installera.



Genom att klicka på applikationen hittar du bland annat:




- Funktioner och ändringar som lagts till i den senast tillgängliga versionen
- En detaljerad beskrivning av applikationen, dess funktioner, skälen till att använda den och Open Source-communityn bakom projektet.



![features](assets/fr/05.webp)





- Den licens som används av projektet, länkar till källkoden och till problem som uppstått vid användning av applikationen
- Behörigheter som krävs av applikationen



![permissions](assets/fr/06.webp)



Läs mer i vår Thunderbird-handledning:



https://planb.network/tutorials/computer-security/communication/thunderbird-91d02325-0361-4641-b152-8975890284a8

F-Droid ger dig all information du behöver för att avgöra om användningen av en applikation skyddar dina data och förbättrar din integritet. Skanna alla applikationer som du vill använda och klicka sedan på **Install**-knappen för att ladda ner och installera din applikation.


Ge F-Droid installationsrättigheter genom att aktivera alternativet i dina inställningar.



![settings](assets/fr/07.webp)



## Exchange dina applikationer



F-Droid uppmuntrar öppen källkod och bidrag från samhället, särskilt via dess **Near By** Exchange-alternativ. Anslut till användarna runt omkring dig via:




- Bluetooth-detektering;
- Samma Wi-Fi-nätverk;
- QR-kod eller IP:PORT Address för att komma in i din webbläsare.



Med det här alternativet kan du dela och ta emot applikationer som är installerade på din Android-telefon med vänner och familj i bara några steg.



![swap](assets/fr/08.webp)



## Uppdateringar



På fliken **Update** kan du se listan över tillgängliga uppdateringar och se till att du också läser informationen om nya versioner av varje program för att ta reda på eventuella större ändringar i den version du använder.



![updates](assets/fr/09.webp)



Du kan också uppdatera listan över tillgängliga program genom att uppdatera sidan (scrolla nedåt).



## Lägg till dina egna applikationer



F-Droid är ett Open Source-projekt som uppmuntrar bidrag till applikationer som prioriterar användarnas integritet. Du kan lägga till din egen Android-mobilapp i butiken genom bidrag till F-Droid GitLab-källkoden.



Din applikation måste vara öppen källkod, med källkoden offentligt tillgänglig på till exempel GitHub eller GitLab.


Du måste sedan förbereda en YAML-fil (metadata) som beskriver din applikation, inklusive all information och alla behörigheter som krävs för dess användning, enligt [metadatamallen] (https://f-droid.org/docs/Build_Metadata_Reference/) som föreslagits av F-Droid.



I avsnittet **Developers** i [dokumentationen](https://f-droid.org/en/docs/) hittar du alla resurser du behöver för att publicera och underhålla dina applikationer på F-Droid.



### Integritet och säkerhet



Att lägga in en applikation i öppen källkod är ofta synonymt med ökad säkerhet, men också med betydande risker. Hur kan du se till att det inte finns några skadliga ändringar i källkoden för en applikation som finns tillgänglig på F-Droid?



F-Droid kompilerar applikationer på sina egna servrar, baserat på den officiella källkoden och kompileringsanvisningarna. Varje publicerad applikation byggs om och verifieras för att säkerställa att den inte har äventyrats. Detta säkerställer att APK som erbjuds är trogen mot källkoden som publiceras av utvecklarna. Dessutom är varje applikation som installeras via F-Droid digitalt signerad, och sedan jämförs signaturfingeravtrycket med det som meddelats av applikationens utvecklare på den officiella webbplatsen eller på Git-arkivet.



Om du gillade den här handledningen kan du läsa mer om vår kurs i IT-säkerhet och datahantering:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1