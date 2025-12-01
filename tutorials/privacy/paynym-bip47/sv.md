---
name: BIP47 - PayNym
description: Använd en återanvändbar betalkod på Ashigaru
---
![cover](assets/cover.webp)



Det värsta integritetsmisstaget du kan göra på Bitcoin är att återanvända adresser. Varje gång samma adress tar emot flera betalningar länkas dessa transaktioner samman, vilket ger världen en karta över dina transaktioner. Det rekommenderas därför starkt att du alltid använder generate för att skapa en unik adress för varje kvitto. Men för vissa Bitcoin-applikationer är detta inte en enkel sak.



BIP47, som föreslogs av Justus Ranvier 2015, ger ett elegant svar på detta problem. Den introducerar konceptet **återanvändbar betalningskod**: en unik identifierare som gör det möjligt att ta emot ett praktiskt taget obegränsat antal bitcoinbetalningar i kedjan utan att någonsin återanvända en adress. Tack vare en kryptografisk mekanism som bygger på ett ECDH-utbyte (*Diffie-Hellman på elliptiska kurvor*) resulterar varje betalning till samma kod i en tom adress, som är specifik för förhållandet mellan avsändare och mottagare.



![Image](assets/fr/01.webp)



Denna BIP47-princip tillämpas i synnerhet av **PayNym**, det system som ursprungligen utvecklades av Samourai Wallet och som nu har tagits över av Ashigaru. I den här handledningen tittar vi på hur du aktiverar ditt PayNym, utbyter betalkoder med en korrespondent och utför transaktioner utan att återanvända en adress.



Jag kommer inte att gå in på den detaljerade driften av BIP47 här. Om du vill fördjupa dig i ämnet hänvisar jag till kapitel 6.6 i min BTC 204-utbildningskurs.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Förkunskapskrav



För att följa denna handledning behöver du bara en wallet på Ashigaru-appen. Om du inte vet hur du laddar ner, verifierar, installerar applikationen eller skapar en wallet rekommenderar jag att du först läser denna handledning:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Begär PayNym



Det första steget är att göra anspråk på ditt PayNym. Denna operation behöver endast utföras en gång per wallet. Den associerar din BIP47-betalningskod som härrör från din seed (`PM...`) med en unik identifierare som är specifik för PayNym-implementeringen. Denna kortare, mer läsbara identifierare kan sedan överföras till dina korrespondenter för att underlätta utbyten, utan att du behöver dela den långa, fullständiga BIP47-koden.



För att göra det, klicka på din PayNym-bild längst upp till vänster i gränssnittet och sedan på din betalningskod `PM...`.



![Image](assets/fr/02.webp)



Klicka sedan på de tre små prickarna i det övre högra hörnet och välj `Claim PayNym`.



![Image](assets/fr/03.webp)



Bekräfta genom att klicka på knappen `CLAIM YOUR PAYNYM`.



![Image](assets/fr/04.webp)



Uppdatera sidan: ditt PayNym-ID visas nu under din bild, precis ovanför din BIP47-betalkod.



![Image](assets/fr/05.webp)



Ditt PayNym är nu aktivt och redo att användas för dina första BIP47-transaktioner.



## Anslut till en kontakt



Det finns två typer av anslutning mellan PayNym: **följa** och **ansluta**. "Follow"-funktionen är helt kostnadsfri. Den upprättar en länk mellan två PayNym genom Soroban, ett Tor-baserat krypterat kommunikationsprotokoll som utvecklats av Samourai-teamet och antagits av Ashigaru. Denna länk gör det möjligt för två användare som följer varandra att utbyta information privat, i synnerhet för att samordna samarbetstransaktioner som Stowaway eller StonewallX2, som vi kommer att titta på i en annan handledning. Detta steg är specifikt för PayNym och är inte en del av BIP47-protokollet.



![Image](assets/fr/06.webp)



Anslutningsoperationen (`connect`), å andra sidan, kräver en on-chain-transaktion. Den består i att utföra en aviseringstransaktion enligt definitionen i BIP47. Denna Bitcoin-transaktion innehåller metadata i en `OP_RETURN`-utgång, som upprättar en krypterad kommunikationskanal mellan betalaren och mottagaren. Från denna kanal kommer betalaren att kunna generate unika mottagaradresser för varje betalning, och mottagaren kommer att meddelas om dessa betalningar och kommer att kunna generate de privata nycklar som är associerade med adresserna för att spendera dessa medel senare.



Denna aviseringstransaktion har en kostnad: avgiften mining och 546 sats som skickas till mottagarens aviseringsadress för att signalera anslutningen. När förbindelsen har upprättats kan ett nästan oändligt antal betalningar göras via BIP47.



I ett nötskal:




- follow": gratis, upprättar krypterad kommunikation via Soroban, användbar för Ashigarus samarbetsverktyg;
- `Connect`: avgiftsbelagd, utför aviseringstransaktionen BIP47 för att aktivera kanalen mellan betalaren och mottagaren.



För att interagera med ett PayNym måste du först *följa* det. Detta är det första steget innan du upprättar en BIP47-anslutning. Låt oss säga att du vill skicka återkommande betalningar till PayNym `+instinctiveoffer10`.



Gå till din PayNym-sida på Ashigaru och klicka sedan på "+"-knappen längst ner till höger i gränssnittet.



![Image](assets/fr/07.webp)



Du kan sedan antingen klistra in mottagarens fullständiga betalkod eller skanna deras QR-kod.



![Image](assets/fr/08.webp)



Om du bara har hans PayNym-ID, gå till [Paynym.rs] (https://paynym.rs/) för att hitta QR-koden som är kopplad till hans betalningskod.



![Image](assets/fr/09.webp)



När du har skannat QR-koden klickar du på knappen `FOLLOW` för att följa PayNym.



![Image](assets/fr/10.webp)



Åtgärden `FOLLOW` är tillräcklig för samarbetstransaktioner (*cahoots*). För att skicka BIP47-betalningar måste du dock upprätta en anslutning: klicka på `CONNECT` för att utföra meddelandetransaktionen.



![Image](assets/fr/11.webp)



Transaktionsmeddelandet sänds sedan ut i nätverket. Vänta tills den har bekräftats minst en gång innan du gör din första betalning.



![Image](assets/fr/12.webp)



## Gör en BIP47-betalning



Du är nu ansluten till mottagaren och kan skicka en betalning till en unik adress, som automatiskt genereras med hjälp av BIP47-protokollet, utan någon föregående utväxling med mottagaren.



På PayNyms huvudsida klickar du på den kontakt som du vill skicka en betalning till.



![Image](assets/fr/13.webp)



Klicka på pilikonen längst upp till höger i gränssnittet.



![Image](assets/fr/14.webp)



Ange det belopp som ska skickas. Du behöver inte ange någon mottagaradress, den kommer automatiskt att tas fram med hjälp av BIP47-protokollet.



![Image](assets/fr/15.webp)



Kontrollera noggrant transaktionsdetaljerna, inklusive avgifter, och dra sedan den gröna pilen längst ned på skärmen för att signera och sända transaktionen.



![Image](assets/fr/16.webp)



Transaktionen har skickats.



![Image](assets/fr/17.webp)



I det här exemplet gjordes betalningen till en annan av mina PayNym-plånböcker. Jag kan därför se att den har anlänt till min andra Ashigaru wallet, utan att någon adress har bytts ut manuellt: endast PayNym-identifieraren användes.



![Image](assets/fr/18.webp)



Du vet nu hur man använder BIP47 återanvändbara betalkoder tack vare PayNym-implementeringen i Ashigaru-applikationen. Du kan nu dela denna betalningskod med alla som vill skicka betalningar till dig (särskilt återkommande betalningar). Du kan också publicera ditt PayNym-ID på din webbplats eller i sociala nätverk för att ta emot donationer.



För att fördjupa dina kunskaper om det här protokollet, förstå i detalj hur det fungerar och vad det innebär för sekretessen, rekommenderar jag starkt att du går min BTC 204-kurs:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c