---
name: Breez - POS
description: Breez gör det enkelt att samla in bitcoinbetalningar för ditt företag.
---

![cover](assets/cover.webp)



Sedan covid-19-pandemin har kontaktlösa digitala betalningar blivit vanliga, även i de minsta butikerna. Under denna period har många företag upptäckt hur praktiskt det är med bitcoin cash-lösningar som gör det möjligt för dem att ta emot betalningar från hela världen. Dessa lösningar är dock ibland svåra att använda eller olämpliga för små företag. I den här handledningen tittar vi på Breez betalterminal, en lösning som sticker ut för sin användarvänlighet, samtidigt som den ger dig total kontroll över hanteringen av dina bitcoins.



## Installera Breez POS



Breez POS är en självförvaltande tjänst som tillhandahålls av Breez wallet. Syftet med denna tjänst är att göra det möjligt för handlare att samla in betalningar via Bitcoin samtidigt som de behåller ett enkelt gränssnitt, mycket likt de olika Lightning-plånböckerna. Breez POS finns tillgängligt på nedladdningsplattformarna [Google Play Store](https://play.google.com/store/apps/details?id=com.breez.client) (Android) och [App Store](https://apps.apple.com/app/breez-lightning-client-pos/id1463604142) (iOS).



![download](assets/fr/01.webp)



![setup](assets/fr/12.webp)



⚠️ Det är viktigt att notera att dessa applikationer fortfarande är under utveckling och att det kan förekomma vissa fel i användningen av funktionerna. Vi rekommenderar måttlig användning.



Med denna applikation ger Breez dig fullständig kontroll över nätverkskonfigurationer och avgiftsinställningar, samtidigt som du garanterar din suveränitet i hanteringen av dina bitcoins.



Du kan utforska de olika Breez wallet-alternativen genom att följa vår handledning nedan. Detta steg hjälper dig att bättre förstå ekosystemet för försäljningsställen och anta bästa praxis för att effektivt säkra bitcoins som är associerade med din seed.



https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## Använda Breez POS



I den här handledningen fokuserar vi på avsnittet "*Point-of-Sale*" för att hjälpa dig att förstå hur du integrerar det som ett betalningsmedel i ditt företag.



Försäljningsstället är en integrerad del av Breez-portföljen och förlitar sig främst på Lightning Network för att samla in betalningar.



I menyn "*Point of Sale*" har du ett direkt gränssnitt för att ta emot betalningar. Det är indelat i två delar:



### Direktdebitering



Den första delen är tangentbordet för direktdebitering. Det här gränssnittet är praktiskt för att samla in en betalning i sin helhet när du känner till dina kunders totala inköp, eller när du inte behöver en fast produktkatalog i ditt företag (t.ex. frilanstjänster).



![keyboard](assets/fr/02.webp)



För att använda Breez POS för första gången måste du betala över 2 500 satoshis (cirka 3 euro enligt dagens växelkurs). Detta belopp, som endast betalas vid din första utbetalning, motsvarar kostnaden för att skapa en betalningskanal så att du kan kommunicera med andra Lightning Network-noder och skicka och ta emot satoshis.



![channel_fee](assets/fr/03.webp)


### Produktkatalog



Den andra delen är produktkatalogen. Det här gränssnittet är perfekt när du har en produktkatalog med fördefinierade priser. Här kan du förkonfigurera dina produkter och sedan använda dem till generate-fakturor för att förbättra spårbarheten för dina kassakvitton.



![items](assets/fr/04.webp)



Du kan manuellt konfigurera varje artikel från detta gränssnitt genom att klicka på knappen "**Plus**" och sedan definiera namn, pris och en identifierare för denna artikel.



![add_items](assets/fr/05.webp)



Du kan sedan lägga till den och definiera dess kvantitet för att samla in den tillhörande betalningen.



När din katalog är ganska stor kan det bli komplicerat att lägga till dina produkter en efter en. För detta ändamål kan du i avsnittet **Preferences > Point of Sale Settings**, från menyn "Artikelförteckning", automatiskt importera och exportera din artikelförteckning från CSV-filer.



![import](assets/fr/07.webp)



I samma avsnitt kan du definiera giltighetstiden för dina Lightning-fakturor. Från och med nu har dina kunder `N` sekunder på sig att betala för alla dina fakturor, annars måste du skapa en ny Lightning-faktura.



![invoice_time](assets/fr/08.webp)



Som chef kan du stärka säkerheten för dina bitcoins genom att lägga till ett lösenord som kommer att krävas för alla utgående betalningar från din wallet. Den här funktionen är särskilt användbar när du inte är den enda som hanterar ditt uttag.



![manager](assets/fr/09.webp)



I menyn **Transactions** hittar du en lista över alla betalningar som du har samlat in. Du kan också filtrera resultaten för en viss period genom att klicka på knappen **Calendar**.



![transactions](assets/fr/10.webp)



Du kan också se en daglig sammanfattning av din försäljning och det totala beloppet som samlats in genom att klicka på knappen **Document**.



![summary](assets/fr/11.webp)



Du har nu en fullständig förståelse för den kassa som erbjuds av Breez-applikationen för sömlös integrering av Bitcoin i ditt företag. Om du tyckte att denna handledning var användbar rekommenderar vi vår handledning om be-BOP, en e-handelsplattform som låter dig ta emot betalningar i bitcoins och tjäna pengar på ditt företag.



https://planb.academy/tutorials/business/point-of-sale/be-bop-d8c40a3b-9090-48e7-9ba7-235d0c17e5fa