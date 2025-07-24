---
name: Blockstream Green - Endast för bevakning
description: Watch-only wallet-konfiguration
---
![cover](assets/cover.webp)


I den här handledningen kommer du att upptäcka hur du enkelt kan ställa in en "watch-only" Wallet på mobilen med hjälp av Blockstream Green-applikationen.


## Vad är en Watch-only wallet?


En skrivskyddad Wallet, eller "Watch-only wallet", är en typ av programvara som är utformad så att användaren kan observera transaktioner som är associerade med en eller flera specifika publika Bitcoin-nycklar utan att ha tillgång till motsvarande privata nycklar.


Denna typ av applikation lagrar endast de data som behövs för att övervaka en Bitcoin Wallet, särskilt för att se dess saldo och transaktionshistorik, men den har ingen tillgång till privata nycklar. Som ett resultat är det omöjligt att spendera Bitcoins som innehas av Wallet på applikationen som endast övervakar.


![GREEN-WATCH-ONLY](assets/fr/01.webp)


Watch-only används i allmänhet tillsammans med en Hardware Wallet. Detta gör att Wallet:s privata nycklar kan lagras säkert, på hårdvara som inte är ansluten till Internet och som har en mycket liten attackyta, vilket isolerar de privata nycklarna från potentiellt sårbara miljöer. Watch-only-applikationen, å andra sidan, lagrar endast den utökade publika nyckeln (`xpub`, `zpub`, etc.) för Bitcoin Wallet. Denna överordnade nyckel kan inte användas för att hitta de tillhörande privata nycklarna och kan därför inte användas för att spendera Bitcoins. Den gör det dock möjligt att härleda barns publika nycklar och mottagaradresser. Tack vare Hardware Wallet:s kunskap om säkra Wallet-adresser kan watch-only-applikationen spåra dessa transaktioner i Bitcoin-nätverket, vilket gör det möjligt för användaren att övervaka sitt saldo och generate nya mottagningsadresser utan att behöva ansluta sin Hardware Wallet varje gång.


I den här handledningen vill jag introducera dig till en av de mest populära mobila Wallet-lösningarna för endast klockor: **Blockstream Green**.


![GREEN-WATCH-ONLY](assets/fr/02.webp)


## Vi presenterar Blockstream Green


Blockstream Green är en mjukvaruapplikation som finns tillgänglig på mobil och dator. Tidigare känd som Green Address, blev denna Wallet ett Blockstream-projekt efter förvärvet 2016.


Green är en mycket lättanvänd applikation, vilket gör den särskilt lämplig för nybörjare. Den erbjuder en rad olika funktioner, t.ex. hantering av Hot-plånböcker, hårdvaruplånböcker och Liquid Sidechain-plånböcker.


I den här handledningen koncentrerar vi oss enbart på att skapa en Watch-only wallet. För att utforska andra användningsområden för Green, se våra andra dedikerade handledningar:


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143

## Installera och konfigurera Blockstream Green-applikationen


Det första steget är naturligtvis att ladda ner Green-applikationen. Gå till din applikationsbutik:



- [För Android] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN-WATCH-ONLY](assets/fr/03.webp)


För Android-användare kan du också installera applikationen via filen `.apk` [tillgänglig på Blockstreams GitHub] (https://github.com/Blockstream/green_android/releases).


![GREEN-WATCH-ONLY](assets/fr/04.webp)


Starta programmet och kryssa sedan i rutan "Jag accepterar villkoren...*".


![GREEN-WATCH-ONLY](assets/fr/05.webp)


När du öppnar Green för första gången visas startskärmen utan en konfigurerad Wallet. Senare, om du skapar eller importerar plånböcker, kommer de att visas i denna Interface. Innan du fortsätter att skapa en Wallet rekommenderar jag att du justerar applikationsinställningarna så att de passar dina behov. Klicka på "Applikationsinställningar".


![GREEN-WATCH-ONLY](assets/fr/06.webp)


Alternativet "*Enhanced Privacy*", som endast finns tillgängligt på Android, förbättrar integriteten genom att inaktivera skärmdumpar och dölja förhandsvisningar av applikationer. Det låser också automatiskt åtkomsten till applikationer så snart telefonen låses, vilket gör det svårare att komma åt dina data.


![GREEN-WATCH-ONLY](assets/fr/07.webp)


För den som vill stärka sin integritet erbjuder applikationen möjligheten att roota sin trafik via Tor, ett nätverk som krypterar alla dina anslutningar och gör dina aktiviteter svåra att spåra. Även om det här alternativet kan göra applikationen något långsammare rekommenderas det starkt för att skydda din integritet, särskilt om du inte använder din egen kompletta nod.


![GREEN-WATCH-ONLY](assets/fr/08.webp)


För användare som har en egen komplett nod erbjuder Green Wallet möjligheten att ansluta till den via en Electrum-server, vilket garanterar total kontroll över Bitcoin nätverksinformation och distribution av transaktioner.


![GREEN-WATCH-ONLY](assets/fr/09.webp)


En annan alternativ funktion är alternativet "*SPV Verification*", som gör att du kan verifiera vissa Blockchain-data direkt och därmed minska behovet av att lita på Blockstreams standardnod, även om den här metoden inte ger alla garantier som en Full node.


![GREEN-WATCH-ONLY](assets/fr/10.webp)


När du har anpassat dessa inställningar till dina behov klickar du på knappen "*Save*" och startar om programmet.


![GREEN-WATCH-ONLY](assets/fr/11.webp)


## Skapa en Watch-only wallet på Blockstream Green


Du är nu redo att skapa en Watch-only wallet. Klicka på knappen "*Get Started*".


![GREEN-WATCH-ONLY](assets/fr/12.webp)


Du kommer att kunna välja mellan flera typer av Wallet. För denna handledning vill vi skapa en Watch-only wallet, så klicka på motsvarande knapp.


![GREEN-WATCH-ONLY](assets/fr/13.webp)


Välj alternativet "Enkel signatur".


![GREEN-WATCH-ONLY](assets/fr/14.webp)


Välj sedan "*Bitcoin*". För min del gör jag den här handledningen på en Testnet Wallet, men proceduren förblir identisk på Mainnet.


![GREEN-WATCH-ONLY](assets/fr/15.webp)


Du kommer att bli ombedd att ange antingen en utökad publik nyckel (`xpub`, `zpub`, etc.) eller en output script descriptor.


![GREEN-WATCH-ONLY](assets/fr/16.webp)


Du måste därför hämta denna information från den Wallet som du vill spåra via din Watch-only wallet. Den utökade publika nyckeln är inte känslig ur säkerhetssynpunkt, eftersom den inte ger tillgång till privata nycklar, men den är känslig för din integritet, eftersom den avslöjar alla dina publika nycklar och därmed alla dina Bitcoin-transaktioner.


Låt oss säga att du använder Sparrow wallet för att hantera din Wallet på en Hardware Wallet, du hittar denna information i avsnittet "*Inställningar*". Hur du hittar den här informationen beror på vilken programvara för Wallet-hantering du använder, men den finns vanligtvis i inställningarna.


![GREEN-WATCH-ONLY](assets/fr/17.webp)


Kopiera din utökade publika nyckel och ange den i Green-programmet och klicka sedan på "Connect".


![GREEN-WATCH-ONLY](assets/fr/18.webp)


Du kommer då att kunna se saldot som är kopplat till den här nyckeln samt transaktionshistoriken.


![GREEN-WATCH-ONLY](assets/fr/19.webp)


Genom att klicka på "*Receive*" kan du generate en ta emot Address för att ta emot bitcoins på din Hardware Wallet. Jag skulle dock avråda från att använda detta alternativ utan att först kontrollera på Hardware Wallet-skärmen att den har den privata nyckeln som är associerad med den genererade Address, innan du använder den för att låsa bitcoins. Detta är en bra praxis att följa.


![GREEN-WATCH-ONLY](assets/fr/20.webp)


Med alternativet "*Balayer*" kan du manuellt ange en privat nyckel för att spendera pengar direkt från din Green-applikation. Förutom i mycket specifika fall rekommenderar jag inte att du använder den här funktionen, eftersom det kräver att du avslöjar din privata nyckel på en telefon, som är mycket mer sårbar för datorattacker än din Hardware Wallet.


![GREEN-WATCH-ONLY](assets/fr/21.webp)


Så nu vet du hur du enkelt ställer in en Watch-only wallet på din smartphone! Det är ett praktiskt verktyg för att övervaka en Wallet på en Hardware Wallet utan att behöva ansluta och låsa upp den varje gång.


Om du tyckte att den här handledningen var användbar skulle jag vara tacksam om du lämnar en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också att du kollar in den här andra omfattande handledningen om Blockstream Green-applikationen för att ställa in en Hot Wallet:


https://planb.network/tutorials/wallet/mobile/blockstream-green-e84edaa9-fb65-48c1-a357-8a5f27996143