---
name: Tiankii
description: Lightning-svit med verktyg för återförsäljare och konsumenter
---

![cover](assets/cover.webp)



I Bitcoin-ekosystemet är det fortfarande en stor utmaning för företag och privatpersoner att ta emot betalningar i realtid. Traditionella lösningar kräver ofta avancerad teknisk kunskap, en komplex infrastruktur att underhålla eller att medel hålls av mellanhänder. Denna situation håller tillbaka massanvändningen av Bitcoin som en vardagsvaluta, trots löftet om Lightning Network:s tekniska framsteg.



Tiankii, ett salvadoranskt företag som föddes 2021, svarar på detta problem genom att erbjuda en tillgänglig, modulär Bitcoin-infrastruktur. I stället för att tvinga fram ett slutet ekosystem erbjuder Tiankii en uppsättning sammankopplade verktyg som gör det möjligt för vem som helst att integrera Bitcoin Lightning i sin verksamhet utan att offra kontrollen över sina medel.



## Vad är Tiankii?



### Ursprung och filosofi



Tiankii - en Nahuatl-term som betyder "utomhusmarknad tillgänglig för alla" - är El Salvadors första startupbolag som till 100% består av Bitcoin. Företaget grundades av Darvin Otero efter att Bitcoin antagits som landets lagliga betalningsmedel och har som mål att omvandla Bitcoin från en värdebevarare till en transaktionsbar valuta för vardagliga inköp. Till skillnad från depåplattformar använder Tiankii ett icke-depåbaserat tillvägagångssätt där användarna behåller kontrollen över sina medel och infrastrukturen endast fungerar som en teknisk mellanhand.



### Teknisk arkitektur



Tiankii är positionerat som en leverantör av Bitcoin-as-a-Service-infrastruktur baserad på Lightning Network. Denna andra lager-teknik möjliggör nästan omedelbara transaktioner med försumbara kostnader, vilket gör mikrobetalningar och vardagliga inköp möjliga.



Arkitekturen bygger på tre pelare:



**Blixtar först**: Systematiskt gynna Lightning-nätverket för dess hastighet och lägre kostnader, samtidigt som on-chain-transaktionsstöd för stora belopp behålls.



**Öppna standarder**: Användning av LNURL för att automatisera betalningsförfrågningar, Lightning Address för läsbara e-post-ID och Bolt Card för interoperabla NFC-betalningar.



**wallet-agnostisk modularitet**: Möjlighet att ansluta olika Lightning-portföljer (LNbits, Blink, BlueWallet) eller din egen nod, vilket ger maximal flexibilitet beroende på vilken nivå av expertis och självständighet som krävs.



## Tiankii ekosystemverktyg



### Bitcoin POS - Betalningsterminal i butik



Applikationen förvandlar smarttelefonen eller surfplattan till en Lightning-terminal. Handlaren anger beloppet i lokal valuta och appen genererar en Lightning QR-kod eller accepterar ett Bolt-kort. Transaktionerna krediteras omedelbart utan provision, med automatisk konvertering i över 150 valutor, drickshantering och försäljningshistorik.



### Merchant Dashboard - enhetlig försäljningshantering



Interface web centraliserad för att ansluta sina wallet Lightning, spåra transaktioner i realtid, utfärda fakturor och generate redovisningsrapporter. Plattformen samlar alla kanaler: betalningar i butik (POS), onlineförsäljning (plug-ins för e-handel) eller API-integrationer. Betalningarna sammanstrålar på den valda wallet.



### Bitcoin Kontaktlöst kort (Bolt-kort)



NFC Bolt-kortet representerar Tiankiis stora innovation för att demokratisera Bitcoin för allmänheten. Det fungerar som ett kontaktlöst bankkort och låter dig betala för Bitcoin Lightning-inköp genom att helt enkelt trycka på en kompatibel terminal.



Till skillnad från traditionella depålösningar följer detta kort en öppen standard som garanterar interoperabilitet. Användarna kan koppla kortet till sin egen wallet via IBI-applikationen och på så sätt behålla sina privata nycklar och full kontroll över de tillhörande medlen. Betalningen tar bara en sekund, utan att man behöver ta fram sin smartphone eller ha en aktiv internetanslutning vid betalningstillfället.



Denna lösning är särskilt inkluderande för personer som inte är bekanta med smartphones och erbjuder en tillgänglig inkörsport till Bitcoin-ekonomin.



### IBI-app - Interface enskilda Bitcoin



IBI-applikationen (Individual Bitcoin Interface) är utformad för personer som vill använda Bitcoin Lightning dagligen. Dess främsta fördel ligger i genereringen av en personlig Address Lightning, en betalningsidentifierare som kan läsas i e-postformat (exempel: alice@ibi.me).



Denna identifierare förenklar mottagandet av betalningar drastiskt: du behöver inte generate en ny faktura för varje transaktion, avsändaren kan helt enkelt ange Lightning-adressen. I gränssnittet kan du också hantera ditt Bolt-kort (aktivering, avaktivering, utgiftsgränser), ansluta olika Lightning-plånböcker och göra betalningar genom att skanna QR-koder.



### Plugins för e-handel



Färdiga integrationer för WooCommerce, Shopify och Cloudbeds. Installeras på några minuter för att lägga till Bitcoin Lightning i kassan. Fördelar: ingen provision (jämfört med 2-3 % för kreditkort), omedelbar avveckling, tillgång över hela världen, eliminering av återbetalningar. Betalningar anländer direkt till handlarens anslutna wallet.



### Bitcoin API och verktyg för utvecklare



Tiankiis SDK gör det möjligt att integrera Bitcoin Lightning i befintliga applikationer utan att behöva underhålla en egen nod. API hanterar fakturaskapande, betalningsverifiering och massutskick via en robust infrastruktur på Google Cloud. Command Center kompletterar erbjudandet för organisationer med Address Lightning på anpassade domäner, bulkbetalningar och centraliserad hantering av NFC-terminaler och kort.



## Installation och första steg



### Viktiga förutsättningar



Att använda Tiankii kräver inga komplicerade tekniska förutsättningar. Applikationerna fungerar via en webbläsare på en smartphone, surfplatta eller dator. Ingen egen installation av applikationen krävs: allt du behöver är internetåtkomst och en ny webbläsare för att komma åt IBI eller Merchant Dashboard.



**För privata användare (IBI App)**: Ingen tidigare wallet Lightning krävs. När du skapar ditt konto konfigurerar Tiankii automatiskt en fungerande Address Lightning via [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html), en nodlös implementering som använder Liquid-nätverket i bakgrunden. Du kan omedelbart ta emot och skicka betalningar utan någon teknisk konfiguration. Denna lösning förenklar drastiskt åtkomsten för nybörjare, samtidigt som den förblir självförsvarande.



**För handlare (Merchant Dashboard)** : Anslutningen av en befintlig wallet Lightning är obligatorisk för att använda Point of Sale-terminaler och ta emot betalningar. Tiankii stöder många lösningar: mobila plånböcker (Blink, Strike), lösningar med egen värd (LNbits, LND/CLN-nod) eller webbplånböcker (Alby). Detaljerade anslutningsguider finns tillgängliga i avsnittet Resurser i denna handledning.



### För privatkunder: IBI App



**Skapande av konto



Gå till accounts.ibi.me för att skapa ditt konto. På den här sidan kan du välja mellan två kontotyper: "Personal Use" för privat bruk eller "Business Use" för kommersiellt bruk. Välj "Personal Use" för att få tillgång till verktygen för att ta emot och skicka betalningar i Bitcoin.



![Choix du type de compte](assets/fr/01.webp)



När du har valt "Personal Use" kommer du automatiskt att omdirigeras till go.ibi.me för att slutföra din registrering. Detta kan göras via e-post, telefonnummer eller med hjälp av ditt Google-, Microsoft- eller Twitter-konto. När du har skapat ditt konto kan du omedelbart komma åt ditt IBI-gränssnitt, med din Lightning Address redan i drift.



![Création du compte](assets/fr/02.webp)



**Interface huvud**



IBI-gränssnittet visar ditt saldo i satoshis och lokal valuta (USD). Tre knappar gör det möjligt för dig att interagera: "Receive" för att ta emot betalningar, "Scan" för att skanna en QR-kod och "Send" för att skicka satoshis.



![Interface IBI](assets/fr/03.webp)



**Motta betalning**



För att ta emot satoshis, tryck på "Receive". Programmet genererar automatiskt en QR-kod och visar din personliga Address Lightning (nom@ibi.me format). Dela den här adressen eller QR-koden med avsändaren: pengarna kommer direkt in på ditt IBI-konto.



![Réception avec Lightning Address](assets/fr/04.webp)



När ditt saldo har krediterats kan du använda dessa satoshis för att göra betalningar.



**Skicka en betalning**



För att skicka satoshis, tryck på "Skicka". Du kan antingen skanna en Lightning QR-kod eller direkt ange en Lightning Address-destination.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



Ange önskat belopp i satoshis, kontrollera motsvarande belopp i lokal valuta och bekräfta sedan betalningen.



![Confirmation du montant](assets/fr/07.webp)



Ett meddelande bekräftar sändningen med uppgifter om belopp, transaktionsavgift och mottagare.



![Paiement réussi](assets/fr/08.webp)



**Kontohantering



I Inställningar kan du hantera dina Bitcoin NFC-kort (Bolt-kort). I gränssnittet kan du aktivera, avaktivera eller ställa in utgiftsgränser för dina kort.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### För handlare: Dashboard för handlare och POS



**Skapande av företagskonto



Gå till accounts.ibi.me för att skapa ditt konto. Välj "Business Use" för att få tillgång till verktyg för handlare. Den här typen av konto ger tillgång till Merchant Dashboard och terminaler för försäljningsställen.



När du har valt "Business Use" kommer du automatiskt att omdirigeras till Merchant Dashboard (pay.tiankii.com). Detta tar dig till gränssnittet för affärshantering med intäktsspårning, transaktioner och betalningsverktyg. För att börja ta emot betalningar måste du först ansluta din wallet Lightning genom att klicka på länken högst upp på sidan (se pilen på bilden).



![Dashboard marchand](assets/fr/11.webp)



**wallet Blixt** anslutning



Avgörande steg för att aktivera din försäljningspunkt: anslut din wallet Lightning för att ta emot betalningar. Gränssnittet erbjuder flera anslutningsalternativ. Observera att vissa alternativ (Bitcoin Onchain och Lightning Network) fortfarande är under utveckling och visas i grått i gränssnittet.



![Options de connexion wallet](assets/fr/12.webp)



I den här handledningen använder vi Lightning Address-anslutningen, kompatibel med Chivo, Blink Wallet och Strike. Ange din Lightning Address (nom@domaine.com-format), till exempel från LN Markets, Alby eller någon annan kompatibel leverantör.



![Saisie de la Lightning Address](assets/fr/13.webp)



När du har loggat in är ditt konto i drift. Du kan nu komma åt kassan eller gå tillbaka till instrumentpanelen för att konfigurera andra inställningar.



![Connexion réussie](assets/fr/14.webp)



*betalningslänkar** *betalningslänkar



Via menyn "Payment Tools" får du tillgång till "Payment Request", där du kan skapa och hantera betalningslänkar. Den här funktionen är användbar för att skapa personliga betalningslänkar som ska skickas via e-post eller meddelande: donationer, enstaka betalningar, flera betalningar eller till och med betalväggar för att skydda innehåll. Du kan skapa olika typer av länkar för att passa dina affärsbehov.



![Liens de paiement](assets/fr/15.webp)



**Konfiguration av säljterminalen**



För att acceptera betalningar i butik, gå till menyn "Försäljningsterminal" från "Betalningsverktyg". I det här avsnittet kan du skapa och hantera dina POS-terminaler (antalet terminaler beror på din plan, se Freemium vs. Business-planer nedan). Klicka på "Öppna" för att öppna POS-gränssnittet i din webbläsare.



![Gestion des terminaux](assets/fr/16.webp)




**Generera en försäljning**



Kassaterminalen visar en numerisk knappsats för inmatning av försäljningsbeloppet. Ange beloppet i din lokala valuta (t.ex. 500 sats motsvarar 630,74 ARS) och tryck sedan på "OK" för att bekräfta.



![Saisie du montant](assets/fr/17.webp)



Applikationen genererar omedelbart en Lightning QR-kod och en Lightning Address för betalning. Kunderna kan skanna QR-koden med sin wallet eller använda sitt Bolt-kort på en NFC-terminal.



![QR code de paiement](assets/fr/18.webp)



Så snart betalningen har tagits emot visas en bekräftelseskärm som visar det mottagna beloppet i lokal valuta och satoshis. Du kan skicka ett kvitto via e-post, skriva ut biljetten eller starta en ny försäljning omedelbart.



![Paiement encaissé](assets/fr/19.webp)



**Övervakning och styrning**



Alla transaktioner registreras i din Merchant Dashboard. Du har fullständig spårning av intäkter per period, totalt antal försäljningar och detaljerad historik för din redovisning.



I gränssnittet Inställningar finns flera flikar för konfiguration. På fliken "Allmänna inställningar" kan du hantera din säljarprofil och dina aviseringar. På fliken "Användare" kan du lägga till och hantera åtkomst till Merchant Dashboard för ditt team (hantering av flera användare enligt din plan). Fliken "Development Workspace" ger tillgång till API-nycklar för avancerade integrationer, medan "Subscription" låter dig hantera din prenumeration.



![Paramètres du compte marchand](assets/fr/20.webp)



**Freemium vs affärsplaner



Tiankii erbjuder två paket för Merchant Dashboard. **Freemium**-planen (gratis) är lämplig för nystartade företag med begränsningar: ett enda försäljningsställe, en enda användare, månadsvolym begränsad till 1 000 USD och ingen tillgång till e-handelskopplingar. Planen **Business** (0,5% avgift per transaktion) erbjuder obegränsat antal terminaler, obegränsat antal användare, obegränsad volym, tillgång till WooCommerce/Shopify/Cloudbeds-plugins och exklusiva WhatsApp-meddelanden.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## Fördelar och begränsningar



### Höjdpunkter



**Självförvaltande**: Du behåller dina privata nycklar och full kontroll över dina medel. Ingen risk för frysning av konton eller konkurs för tredjepartsplattform.



**Enkelhet**: Lightning Address som en e-postadress, NFC-betalningar med en enkel tryckning, intuitivt gränssnitt utan krav på teknisk expertis.



** Komplett ekosystem**: Verktyg för alla profiler (privatpersoner, återförsäljare, utvecklare) med modulära integrationer för att passa dina behov.



**Professionell efterlevnad**: Säker molnhosting, efterlevnad av PCI-DSS, efterlevnad av salvadoranska bestämmelser.



### Begränsningar



**Blixtnedslagsbegränsningar**: Kräver permanent wallet-anslutning, likviditetshantering för stora volymer, risk för misslyckande om mottagaren är offline. Tiankii mildrar dessa aspekter med integrerade LSP:er.



**SaaS-beroende**: Om Tiankii inte är tillgängligt är det tillfälligt omöjligt att generera fakturor (dina medel förblir säkra).



**Sekretess**: Tiankii kan observera metadata för transaktioner (belopp, datum). Mindre privat än en självhostad lösning som BTCPay Server.



## Slutsats



Tiankii illustrerar hur en väl utformad infrastruktur kan undanröja de tekniska hinder som står i vägen för en massanvändning av Bitcoin som vardagsvaluta. Genom att kombinera kraften i Lightning Network med ett icke-frihetsberövande tillvägagångssätt och tillgängliga verktyg erbjuder ekosystemet en balanserad väg mellan finansiell suveränitet och användarvänlighet.



För handlare innebär Tiankii en möjlighet att drastiskt minska transaktionskostnaderna och samtidigt få tillgång till en ny kundbas. För konsumenterna innebär Lightning Address och NFC-kort att Bitcoin förvandlas till en praktisk valuta utan teknisk komplexitet.



Även om ett utbrett införande av Bitcoin fortfarande är en utmaning som kräver utbildning och tid, visar infrastrukturer som Tiankii att de tekniska verktygen redan finns. Uppdraget att förenkla Bitcoin-betalningar är inte längre en avlägsen vision, utan en verklighet som är tillgänglig för alla som är villiga att ta steget.



## Resurser



### Officiell dokumentation




- [Tiankiis officiella webbplats](https://tiankii.com)
- [Tiankii Hjälpcenter](https://help.tiankii.com)
- [IBI-ansökan](https://go.ibi.me)
- [Instrumentpanel för handlare](https://pay.tiankii.com)
- [Kommandocentral](https://cc.ibi.me)



### Wallet anslutningsguider




- [Anslut LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Connect BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Anslut Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### Gemenskap




- [Lightning Network Plus](https://lightningnetwork.plus) - Utbildningsresurs för blixtar
- [Bitcoin Beach](https://www.bitcoinbeach.com) - Salvadorianskt initiativ för cirkulär ekonomi Bitcoin



### Relaterade verktyg




- [Blink Wallet](https://blink.sv) - Wallet Lightning-kompatibel rekommenderas
- [LNbits](https://lnbits.com) - Självhanterad wallet-lösning
- [Standard Bolt-kort](https://github.com/boltcard) - Tekniska specifikationer för NFC-kort