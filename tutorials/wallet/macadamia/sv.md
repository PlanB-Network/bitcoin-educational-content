---
name: Macadamia Wallet
description: Cashu mobile wallet för anonyma och omedelbara BTC-betalningar
---

![cover](assets/cover.webp)



Macadamia Wallet är en iOS-mobil wallet som implementerar Cashu-protokollet, ett Chaumian ecash-system som möjliggör helt anonyma Bitcoin-betalningar. Tack vare blinda signaturer kan ingen observatör koppla dina insättningar till dina utgifter, vilket ger en sekretess som liknar fysiska kontanter.



I den här handledningen tittar vi på hur du installerar och konfigurerar Macadamia, utför dina första Cashu-transaktioner (Mint, Send, Receive, Melt) och hanterar flera mints för att säkra dina pengar.



## Vad är Macadamia Wallet?



### Cashu-protokollet



Cashu använder blinda signaturer som uppfanns av David Chaum: du sätter in bitcoins på en "mint"-server, som utfärdar motsvarande tokens i satoshis. Myntverket signerar dessa tokens utan att se deras innehåll, vilket gör det omöjligt att länka en token till en användare. Utbyten är off-chain, peer-to-peer och helt ogenomskinliga - inte ens myntverket kan spåra vem som betalar vem.



Macadamia är ett wallet iOS med öppen källkod som utvecklats i Swift/SwiftUI. Den fungerar utan konto eller KYC, dina tokens lagras lokalt och skyddas av en seed-fras. Koden är granskningsbar på GitHub och tokens är kompatibla med andra Cashu-plånböcker (Minibits, Cashu.me).



### Förvaltningsmodell och kompromiss



**Viktigt**: Cashu fungerar enligt en förvaringsmodell. Tokens är löften om att betala (IOU) som backas upp av myntverkets Bitcoin reserver. Om myntverket försvinner förlorar dina tokens sitt värde. Detta är kompromissen för maximal sekretess.



Använd Macadamia som en fysisk wallet: endast små mängder. Sprid dina medel över flera mints för att späda ut risken.



## Huvudsakliga egenskaper



Macadamia implementerar de fyra grundläggande operationerna i Cashu-protokollet. **Mint** omvandlar dina satoshis till tokens via en Lightning-faktura. **Send** låter dig skicka tokens kostnadsfritt via QR-kod eller länk, helt off-chain. **Receive** låter dig ta emot tokens eller generate en Lightning-faktura. **Melt** betalar en Lightning-faktura genom att förstöra dina tokens.



wallet stöder hanteringen av flera myntverk samtidigt. Du kan byta tokens mellan olika mints via Lightning.



## Plattformar som stöds



Macadamia är endast tillgänglig på iOS 17 eller högre för iPhone och iPad. Den inbyggda Swift/SwiftUI-applikationen erbjuder optimal integration med Apples ekosystem.



Cashu-protokollet garanterar interoperabilitet mellan plånböcker. Du kan återställa din seed-fras i andra applikationer som Minibits på Android eller Nutstash på datorn.



Den aktuella versionen distribueras via TestFlight. Använd endast små mängder med denna betaversion.



## Installation



Macadamia är för närvarande tillgängligt via TestFlight, Apples betatestprogram. Så här installerar du det:



### Installation via TestFlight



**Steg 1: Ladda ner TestFlight**



Om du inte redan har TestFlight-appen på din enhet kan du söka efter "TestFlight" i App Store och installera den. TestFlight är Apples officiella applikation för att testa betaversioner av iOS-applikationer.



**Steg 2: Gå med i Macadamia beta-program** (på franska)



När TestFlight är installerat, följ denna inbjudningslänk från din iPhone eller iPad: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



Länken kommer automatiskt att öppna TestFlight och erbjuda dig att installera Macadamia Wallet. Tryck på "Acceptera" och sedan på "Installera" för att starta nedladdningen. Programmet väger cirka tio megabyte och tar bara några sekunder att installera.



![Installation TestFlight](assets/fr/01.webp)



### Viktig information om betaversioner



Macadamia är fortfarande i den aktiva utvecklingsfasen. TestFlight-versioner uppdateras ofta och kan innehålla nya funktioner eller korrigera buggar. Som med alla betaversioner kan dock fel uppstå. **Vi rekommenderar starkt att du endast använder små mängder**, som du accepterar kan gå förlorade i händelse av ett tekniskt problem.



Macadamia samlar inte in några användardata enligt den sekretesspolicy som visas. Var noga med att kontrollera att utvecklaren är cypherbase UG när du installerar.



## Inledande konfiguration



Vid första lanseringen genererar Macadamia en BIP-39 mening med 12 ord. Skriv ner dem på ett säkert ställe - aldrig som en skärmdump. Dessa ord gör att du kan återskapa din wallet och spendera dina tokens.



![Configuration initiale](assets/fr/02.webp)



Följ de fyra stegen: välkommen, acceptera villkoren, spara seed-meningen och slutlig bekräftelse.



![Interface principale](assets/fr/03.webp)



När konfigurationen är klar presenterar Macadamia tre huvudflikar. **Wallet** visar ditt saldo och din transaktionshistorik. **Mints** låter dig hantera dina Cashu-servrar. **Settings** ger tillgång till inställningar och din seed-fras.



![Ajout d'un mint](assets/fr/04.webp)



Du måste nu konfigurera en mint, dvs. en Cashu-server som kommer att utfärda dina tokens. Gå till fliken "Mints", tryck på "Add new Mint URL" och ange adressen till din valda mint (t.ex. mint.cubabitcoin.org). Kolla in bitcoinmints.com eller cashu.space för välrenommerade offentliga myntverk. Validera endast mints vars rykte du har kontrollerat, eftersom de kommer att ha vårdnaden om dina satoshis.



## Daglig användning



### Skapande av nya tokens (Mint)



För att mata din wallet Macadamia med ecash måste du utföra en "Mint" -operation (för att skapa tokens). Tryck på "Receive" och välj sedan alternativet "Lightning". Ange önskat belopp (t.ex. 1000 sats), välj den mynta som ska användas och generate sedan Lightning-fakturan.



![Opération Mint](assets/fr/05.webp)



Betala den genererade Lightning-fakturan med din vanliga wallet (Phoenix, Zeus, BlueWallet).



![Confirmation Mint](assets/fr/06.webp)



Cashu-tokens visas direkt i ditt saldo efter betalning.



### Skicka polletter



För att skicka Cashu-tokens till en annan användare, tryck på knappen "Send" på huvudskärmen och välj sedan "Ecash". Ange beloppet som ska skickas (t.ex. 50 sats) och lägg till ett beskrivande memo om det behövs.



![Envoi Ecash](assets/fr/07.webp)



Dela QR-koden eller den genererade texten via iMessage, Signal eller Telegram. Mottagaren gör anspråk på pengarna direkt och kostnadsfritt.



### Ta emot polletter



För att ta emot Cashu-tokens som skickats av en annan användare, tryck på "Receive" och välj sedan "Ecash". Skanna token QR-koden eller klistra in token-länken som du fick.



![Réception Ecash](assets/fr/08.webp)



Tryck på "Redeem" för att hämta token.



### Betalningar för blixtnedslag (smältning)



För att betala en Lightning-faktura med dina Cashu-tokens, tryck på "Skicka" och välj sedan "Lightning". Klistra in en BOLT11-faktura som du vill betala.



![Paiement Lightning](assets/fr/11.webp)



Myntverket förstör dina tokens och verkställer Lightning-betalningen. Så du kan betala för alla Lightning-tjänster samtidigt som du bevarar din anonymitet.



### Byte mellan myntverk



När du får polletter från ett myntverk som du inte har konfigurerat erbjuder Macadamia dig flera alternativ för att hantera dessa polletter.



![Swap inter-mints](assets/fr/09.webp)



Lägg till det nya myntverket eller byt ut polletterna till ett befintligt myntverk. Vid bytet används Lightning som en bro för att överföra dina pengar anonymt.



### Avancerad multiminthantering



Macadamia erbjuder sofistikerade verktyg för att hantera flera mints samtidigt och strategiskt fördela dina medel.



![Gestion multi-mints](assets/fr/10.webp)



"Distribute Funds" fördelar automatiskt ditt saldo enligt procentandelar (t.ex. 50/50). "Transfer" tillåter manuella överföringar mellan myntverk för att diversifiera dina risker.



## Fördelar och begränsningar



**Höjdpunkter** :





- Maximal sekretess**: Transaktioner som inte kan spåras, inte ens av myntverket. Inga metadata i blockkedjan, spårlösa peer-to-peer-utbyten.
- Snabbt och gratis**: Kostnadsfria direktöverföringar inom ett minutintervall, perfekt för mikrobetalningar.
- Interoperabilitet**: standardiserade Cashu-tokens för användning med andra kompatibla plånböcker (Minibits, Nutstash).
- Enkelhet**: Interface iOS native är tillgängligt för nybörjare samtidigt som det är granskningsbart (öppen källkod).



**Begränsningar** :





- Förvaringsmodell**: mint trust krävs. Om ett myntverk försvinner förlorar dina polletter sitt värde.
- endast iOS**: Ingen Android/desktop-version. Cashu-interoperabilitet möjliggör åtkomst via andra plånböcker, men den optimala upplevelsen förblir iOS.
- Myntberoende**: Mint offline = kan inte utföra transaktioner som kräver dess ingripande (Mint, Melt).
- Framväxande teknik** : Aktiv utveckling, möjliga buggar, standarder under utveckling.



## Bästa praxis





- Diversifiera dina mints**: Sprid ut dina marker på flera välrenommerade myntverk för att minska risken.
- Begränsa belopp**: Använd Macadamia som en fysisk wallet för dagliga betalningar, inte som ett kassaskåp.
- Säkra din seed**: Förvara din 12-ordsfras på papper på en säker plats. Testa restaureringen då och då.
- Kontrollera mints**: Konsultera cashu.space och community-forum innan du lägger till en myntautomat. Välj de som har bra drifttid och ett gott rykte.
- VPN eller Tor**: Dölj din IP med VPN/Tor för att maximera integriteten i nätverket.
- Gå med i gemenskapen**: Telegram/Discord Cashu-grupper för uppdateringar, rekommendationer och bästa praxis.



## Slutsats



Macadamia Wallet ger egenskaperna hos fysiska kontanter till digitala Bitcoin. Genom att kombinera Chaum och Lightning blinda signaturer erbjuder den en elegant lösning för transaktionssekretess. Dess inbyggda iOS-gränssnitt gör sofistikerad kryptografisk teknik tillgänglig samtidigt som den förblir öppen källkod och interoperabel med Cashu-ekosystemet.



Depåmodellen kräver vaksamhet och god säkerhetspraxis. Rätt använd blir Macadamia ett ovärderligt verktyg för vardagliga betalningar som kräver anonymitet, som komplement till plånböcker för sparande utan depå.



## Resurser



### Officiell dokumentation




- Officiell webbplats: [macadamia.cash](https://macadamia.cash)
- Macadamia FAQ: [macadamia.cash/faq](https://macadamia.cash/faq)
- GitHub källkod: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Cashu-dokumentation




- Teknisk dokumentation: [docs.cashu.space](https://docs.cashu.space)
- Lista över offentliga myntverk: [bitcoinmints.com](https://bitcoinmints.com)
- Officiell webbplats för protokollet: [cashu.space](https://cashu.space)



### Gemenskap




- Telegram Cashu-grupp: [t.me/cashu_ecash] (https://t.me/cashu_ecash)