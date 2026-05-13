---
name: Voltz
description: Allt-i-ett Lightning wallet för ditt företag.
---

![cover](assets/cover.webp)



Idén till Voltz-plattformen kom från en grupp bitcoinare som ville tillhandahålla sin egen bitcoin wallet-tjänst. Resultatet blev en komplett infrastruktur för att ta emot bitcoin i detaljhandeln. I den här guiden tar vi dig med på en rundtur i Voltz och de möjligheter till bitcoinintegration som plattformen har att erbjuda.



## Att komma igång med Voltz



Utöver att vara en depåbaserad Lightning wallet som låter dig skicka, ta emot och betala dagligen, är Voltz en komplett plattform som tillhandahåller många tillägg för att integrera bitcoin som en försäljningsplats eller marknadsplats i ditt företag.



Gå till [Voltz]-plattformen (https://www.lnvoltz.xyz/en) och skapa ett konto genom att klicka på knappen "Try now".



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ Det är viktigt att ange ett starkt alfanumeriskt lösenord för att öka dina chanser mot brute-force-attacker, och kontrollera att du verkligen är på Voltz officiella webbplats för att fylla i dina inloggningsuppgifter för att skydda dig mot nätfiske.



Voltz gränssnitt är mycket likt det i LnBits plattform.



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz är i själva verket byggd på en LnBits-server; kolla in vår handledning för att lära dig hur du monterar dina egna LnBits-servrar och bygger dina lösningar på dem.



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

Plattformen gör att du effektivt kan hantera flera portföljer. När du registrerar dig har du som standard automatiskt en Lightning-portfölj. Du kan dock lägga till andra portföljer.



![wallets](assets/fr/03.webp)



### Bärbarhet



Voltz är inte begränsat till ett webbgränssnitt: i avsnittet **Mobile Access** kan du ansluta din aktiva Voltz wallet till applikationer som Zeus eller Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

För att göra detta måste du installera och aktivera tillägget **LndHub** på plattformen.



![lndhub](assets/fr/04.webp)



Välj din aktiva Voltz-portfölj och, beroende på vilka rättigheter du vill bevilja, skanna lämplig QR-kod.




- Med QR-koden för fakturor kan du bara läsa din portföljhistorik och generate nya fakturor.
- Med QR-koden för administratörer kan du se historik, generate-fakturor och även betala blixtfakturor.



![qrs](assets/fr/05.webp)



I den här handledningen ansluter vi vår Voltz wallet till Blue Wallet-applikationen.



![connect](assets/fr/06.webp)



När vår portfölj är ansluten kommer alla åtgärder som utförs att synkroniseras mellan Blue Wallet och Voltz. Till exempel, när du generate en faktura på Blue Wallet, har du också en historik på Voltz.



![sync](assets/fr/07.webp)



I avsnittet **Portföljkonfiguration** hittar du minimala parametrar som anpassning av portföljnamnet och den valuta som du vill ta emot dina betalningar i.



![config](assets/fr/08.webp)



### Tillägg



En av de speciella egenskaperna hos Voltz-plattformen är dess modularitet, så att du kan aktivera de tillägg du behöver. Listan över tillägg finns i menyn **Extensions**.



![extensions](assets/fr/09.webp)



Bland dessa tillägg finns TPoS, en kassaterminal som du kan använda för att hålla en inventering och ta emot betalningar från dina kunder.



![tpos](assets/fr/10.webp)



Från Point of Sale-terminalen kan du :




- Få en webbsida som du kan dela med dina kunder och partners;
- Hantera produktinventering;
- Generera Lightning-fakturor;
- Kontanta betalningar via Bolt-kort.



Tillägget finns som en gratisversion och som en betalversion för mer avancerade funktioner. För att skapa en POS-terminal, klicka på knappen **Öppna** under tilläggets logotyp och klicka sedan på **Ny POS**.



![new_tpos](assets/fr/11.webp)



Ange namnet på ditt försäljningsställe och anslut sedan Voltz wallet till terminalen för att ta emot betalningar. Du kan aktivera dricks genom att markera rutan **Activate gratuities**. Aktivera även alternativet för fakturautskrift om du vill utfärda kvitton till dina kunder (den här funktionen är fortfarande under utveckling, så det kan förekomma fel).



Kassaterminalen innehåller också skattekonfigurering när du vill tillämpa ditt lands skatt direkt på dina produkter.



![tpos](assets/fr/12.webp)



När din POS-terminal har skapats kan du lägga till förkonfigurerade produkter och tjänster för att säkerställa en smidig betalnings- och bokföringsupplevelse för dig och dina kunder.



![product](assets/fr/13.webp)



Skapa dina produkter genom att definiera deras namn, lägga till en bild och ange ett försäljningspris.  Du kan kategorisera dina produkter för enklare spårning. Du kan tillämpa skatter direkt på en specifik produkt. Om produkten inte har någon skatt kommer den skatt som konfigurerats när du skapade kassaterminalen att tillämpas automatiskt.



![products](assets/fr/14.webp)



Du kan automatiskt importera din produktlista från ett JSON-format genom att klicka på knappen **Import/Export**.



![exports](assets/fr/15.webp)



Gå till kassan via länken genom att klicka på ikonen **Ny flik**, eller dela din POS-plattform via QR-kod med dina kunder genom att klicka på ikonen **QR-kod**.



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



Dina kunder kan titta i din katalog och göra sina betalningar från det här gränssnittet.



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



I gruppen av tillgängliga tillägg hittar du också verktyg som ** Invoice** och ** Betalningslänk**-tillägg, som låter dig generate-fakturor med specifika produkter för att samla in isolerade betalningar utan att gå igenom POS-terminalen.



## Håll koll på dina betalningar



I menyn **Payments** ger Voltz dig en överblick över betalningar till dina olika portföljer.


Du kan följa dina betalningar genom att :




- Status.
- Etiketten: till exempel **TPOS** för betalningar på försäljningsstället och **lnhub** via mobilanslutningen i Zeus- och Blue Wallet-plånböckerna.
- Samlingsportföljen.
- Summa inkommande och utgående betalningar.
- En väldefinierad period.



![payments](assets/fr/22.webp)



## Fler alternativ



Voltz är också en infrastruktur som du kan bygga dina egna lösningar på. I avsnittet **Extensions** hittar du en guide för att utveckla dina egna tillägg inom Voltz och LnBits ekosystem.



![build](assets/fr/23.webp)



Om du vill utveckla lösningar utanför ekosystemet men ändå använda deras infrastruktur, hittar du i avsnittet **URL of node** API-nycklar och dokumentationsinformation med ett exempel på vad du kan göra med dessa data.



Du kan skapa Lightning-fakturor från dina applikationer med hjälp av Voltz wallet, betala Lightning-fakturor, avkoda och verifiera fakturor.



![keys](assets/fr/24.webp)



Du har nu en bra förståelse för Voltz. Om du gillade den här handledningen är vi säkra på att du kommer att lära dig mer om de bästa metoderna och verktygen för att integrera bitcoin i ditt företag med vår kurs: Bitcoin för företag.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a