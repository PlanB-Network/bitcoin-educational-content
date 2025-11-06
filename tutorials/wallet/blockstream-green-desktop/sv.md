---
name: Blockstream Green - Skrivbord
description: Använda Green Wallet på din dator
---
![cover](assets/cover.webp)


I den här handledningen utforskar vi hur du använder Blockstream Green-programvaran på din dator för att hantera en säker Wallet på en Hardware Wallet. När du använder en Hardware Wallet är det viktigt att använda programvara på din dator för att hantera Wallet. Denna hanteringsprogramvara har ingen åtkomst till privata nycklar; den används endast för att konsultera ditt Wallet-saldo, generate-mottagningsadresser och för att bygga och distribuera transaktioner som ska signeras av Hardware Wallet. Green är bara en av de många lösningar som finns för att hantera din Bitcoin Hardware Wallet.


År 2024 är Blockstream Green endast kompatibel med Ledger Nano S (gammal version), Ledger Nano X, Trezor One, Trezor T och Blockstream Jade-enheter.


## Introduktion av Blockstream Green


Blockstream Green är en mjukvaruapplikation som finns tillgänglig på mobil och dator. Denna Wallet var tidigare känd som Green Address och blev ett Blockstream-projekt efter förvärvet 2016.


Green är en mycket lättanvänd applikation, vilket gör den särskilt lämplig för nybörjare. Den erbjuder olika funktioner, t.ex. hantering av Hot-plånböcker, hårdvaruplånböcker samt plånböcker på Liquid Sidechain. Du kan också använda den för att konfigurera en Watch-only wallet.


![GREEN-DESKTOP](assets/fr/01.webp)


I den här handledningen koncentrerar vi oss enbart på att använda programvaran på datorn. För att utforska andra användningsområden för Green, se våra andra dedikerade handledningar:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

https://planb.network/tutorials/wallet/mobile/blockstream-green-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

## Installera och konfigurera Blockstream Green-programvaran


Börja med att installera programvaran Blockstream Green på din dator. Gå till [den officiella webbplatsen] (https://blockstream.com/Green/) och klicka på knappen "*Download Now*". Följ sedan installationsprocessen enligt ditt operativsystem.


![GREEN-DESKTOP](assets/fr/02.webp)


Starta programmet och kryssa sedan i rutan "Jag accepterar villkoren...*".


![GREEN-DESKTOP](assets/fr/03.webp)


När du öppnar Green för första gången visas startskärmen utan en konfigurerad Wallet. Om du senare skapar eller importerar plånböcker kommer de att visas i denna Interface. Innan du går vidare med att skapa en Wallet rekommenderar jag att du justerar programmets inställningar så att de passar dina behov. Klicka på ikonen Settings (Inställningar) i det nedre vänstra hörnet.


![GREEN-DESKTOP](assets/fr/04.webp)


I menyn "*General*" kan du ändra programvarans språk och aktivera experimentella funktioner om du så önskar.


![GREEN-DESKTOP](assets/fr/05.webp)


I menyn "*Nätverk*" kan du aktivera anslutning via Tor, ett nätverk som krypterar alla dina anslutningar och gör det svårt att spåra dina aktiviteter. Även om det här alternativet kan göra programmet något långsammare rekommenderas det starkt för att skydda din integritet, särskilt om du inte använder din egen kompletta nod.


![GREEN-DESKTOP](assets/fr/06.webp)


För användare som har en egen komplett nod erbjuder Green möjligheten att ansluta till den via en Electrum-server, vilket garanterar total kontroll över Bitcoin:s nätverksinformation och transaktionsspridning. För att göra detta klickar du på menyn "*Custom servers and validation*" och anger sedan dina Electrum-serveruppgifter.


![GREEN-DESKTOP](assets/fr/07.webp)


En annan alternativ funktion är alternativet "*SPV Verification*", som gör att du kan verifiera vissa Blockchain-data direkt och därmed minska behovet av att lita på Blockstreams standardnod, även om den här metoden inte ger alla garantier som en Full node. Det här alternativet finns också i menyn "*Custom servers and validation*".


![GREEN-DESKTOP](assets/fr/08.webp)


När du har justerat dessa parametrar efter dina behov kan du lämna denna Interface.


## Importera en Bitcoin Wallet på Blockstream Green


Du är nu redo att importera din Bitcoin Wallet. Klicka på knappen "**Gå igång**".


![GREEN-DESKTOP](assets/fr/09.webp)


Du kan välja mellan att skapa en lokal Software Wallet eller att hantera en Cold Wallet via en Hardware Wallet. I den här handledningen koncentrerar vi oss på att hantera en Hardware Wallet, så du måste välja alternativet "*På Hardware Wallet*".


Med alternativet "*Watch-only*" kan du importera en utökad publik nyckel (`xpub`) för att se Wallet-transaktioner utan att kunna spendera de tillhörande pengarna.


![GREEN-DESKTOP](assets/fr/10.webp)


Om du använder en Jade, klicka på motsvarande knapp. Annars väljer du "*Connect a different Hardware Device*". I mitt fall använder jag en Ledger Nano S. För Ledger-användare, se till att du installerar programmet "*Bitcoin Legacy*" på din Hardware Wallet, eftersom Green endast stöder denna version.


![GREEN-DESKTOP](assets/fr/11.webp)


Anslut din Hardware Wallet till datorn och välj Green.


![GREEN-DESKTOP](assets/fr/12.webp)


Vänta tills Green har importerat din Wallet-information, varefter du kan komma åt den.


![GREEN-DESKTOP](assets/fr/13.webp)


I det här läget finns det två möjliga scenarier. Om du har använt din Hardware Wallet tidigare bör du se ditt konto visas i programvaran. Men om du, som jag, just har initialiserat din Hardware Wallet genom att generera en Mnemonic-fras utan att ha använt den ännu, måste du skapa ett konto. Klicka på "*Create Account*".


![GREEN-DESKTOP](assets/fr/14.webp)


Välj "*Standard*" om du vill använda en klassisk Wallet.


![GREEN-DESKTOP](assets/fr/15.webp)


Du har nu tillgång till ditt konto.


![GREEN-DESKTOP](assets/fr/16.webp)


## Använda en Hardware Wallet med Blockstream Green


Nu när din Bitcoin Wallet är konfigurerad är du redo att ta emot din första Sats! Klicka bara på knappen "*Receive*".


![GREEN-DESKTOP](assets/fr/17.webp)


Klicka på knappen "*Copy Address*" för att kopiera Address eller skanna dess QR-kod.


![GREEN-DESKTOP](assets/fr/18.webp)


När transaktionen har sänts ut i nätverket kommer den att visas i din Wallet. Vänta tills du har fått tillräckligt många bekräftelser för att anse att transaktionen är oföränderlig.


![GREEN-DESKTOP](assets/fr/19.webp)


Med bitcoins i din Wallet är du nu redo att skicka dem. Klicka på "*Sänd*"-knappen.


![GREEN-DESKTOP](assets/fr/20.webp)


På nästa sida anger du mottagarens Address. Du kan ange den manuellt eller skanna en QR-kod med din webbkamera.


![GREEN-DESKTOP](assets/fr/21.webp)


Välj betalningsbelopp.


![GREEN-DESKTOP](assets/fr/22.webp)


Längst ner på skärmen kan du välja avgiftssats för den här transaktionen. Du kan välja att följa programmets rekommendationer eller anpassa dina avgifter. Ju högre avgift i förhållande till andra väntande transaktioner, desto snabbare kommer din transaktion att behandlas. För information om avgiftsmarknaden, besök [Mempool.space](https://Mempool.space/) i avsnittet "*Transaktionsavgifter*".


![GREEN-DESKTOP](assets/fr/23.webp)


Om du vill välja specifikt vilka UTXO som ska användas i din transaktion klickar du på knappen "*Manuellt myntval*".


![GREEN-DESKTOP](assets/fr/24.webp)


Kontrollera dina transaktionsparametrar och om allt är som du förväntar dig, klicka på "*Nästa*".


![GREEN-DESKTOP](assets/fr/25.webp)


Dubbelkolla att Address, belopp och avgifter är korrekta och klicka sedan på "*Bekräfta transaktion*".


![GREEN-DESKTOP](assets/fr/26.webp)


Kontrollera att alla transaktionsparametrar är korrekta på din Hardware Wallet-skärm och signera sedan transaktionen med den.


![GREEN-DESKTOP](assets/fr/27.webp)


När transaktionen har signerats från Hardware Wallet, sänder Green den automatiskt till Bitcoin-nätverket. Din transaktion kommer sedan att visas på din Bitcoin Wallet instrumentpanel i väntan på bekräftelse.


![GREEN-DESKTOP](assets/fr/28.webp)


Nu vet du hur du enkelt kan konfigurera Blockstream Green för att hantera din Bitcoin Wallet på en Hardware Wallet.


Om du tyckte att den här handledningen var användbar skulle jag vara tacksam om du lämnar en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också att du kollar in den här andra omfattande handledningen om Blockstream Green-mobilappen för att ställa in en Hot Wallet:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143
