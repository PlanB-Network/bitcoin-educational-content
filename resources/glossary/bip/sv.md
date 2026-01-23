---
term: BIP
definition: Bitcoin Improvement Proposal. Formell process som gör det möjligt för communityn att föreslå, diskutera och dokumentera förbättringar av Bitcoin-protokollet.
---

Akronym för "Bitcoin Improvement Proposal" (Bitcoin-förbättringsförslag) Ett Bitcoin Improvement Proposal (BIP) är en formell process för att föreslå och dokumentera förbättringar och ändringar av Bitcoin-protokollet och dess standarder. Eftersom Bitcoin inte har någon central enhet som beslutar om uppdateringar gör BIP:er det möjligt för communityn att föreslå, diskutera och implementera förbättringar på ett strukturerat och transparent sätt. Varje BIP beskriver målen för den föreslagna förbättringen, motiveringarna, potentiella effekter på kompatibiliteten samt fördelar och nackdelar. BIP:er kan skrivas av alla medlemmar i communityn, men måste godkännas av andra utvecklare och de redaktörer som underhåller Bitcoin Core GitHub-databasen: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun och Ruben Somsen. Det är dock viktigt att förstå att dessa personers roll i redigeringen av BIP:er inte innebär att de kontrollerar Bitcoin. Om någon föreslår en förbättring som inte accepteras inom det formella BIP-ramverket kan de fortfarande presentera den direkt för Bitcoin-gemenskapen eller till och med skapa en Fork inklusive deras modifiering. Fördelen med BIP-processen ligger i dess formalitet och centralisering, vilket underlättar debatt för att undvika uppdelning bland Bitcoin-användare, som försöker implementera uppdateringar på ett samförståndsmässigt sätt. I slutändan är det principen om ekonomisk majoritet som avgör maktdynamiken inom protokollet.


BIP delas in i tre huvudkategorier:


- **BIP:er för standardiseringsspår**: Gäller ändringar som direkt påverkar Bitcoin-implementeringar, t.ex. valideringsregler för transaktioner och block;
- Informativa **BIP**: Ger information eller rekommendationer utan att föreslå direkta ändringar av protokollet;
- Processa BIP:er: Beskriv förändringar i rutinerna kring Bitcoin, t.ex. styrningsprocesser.


Standards Track och Informational BIPs klassificeras också av "Layer":


- **Samförstånd Layer**: BIP i denna Layer gäller konsensusreglerna i Bitcoin, t.ex. ändringar av block- eller transaktionsvalideringsreglerna. Dessa förslag kan vara antingen Soft-forkar (bakåtkompatibla modifieringar) eller Hard-forkar (icke-bakåtkompatibla modifieringar). Exempelvis tillhör BIP:erna för SegWit och Taproot denna kategori;
- **Peer-tjänster**: Denna Layer avser driften av Bitcoin-nodnätverket, det vill säga hur noder hittar och kommunicerar med varandra på Internet.
- **API/RPC**: BIP:erna i denna Layer gäller gränssnitt för applikationsprogrammering (API) och fjärrproceduranrop (RPC) som gör det möjligt för Bitcoin-programvara att interagera med noder;
- Tillämpningar Layer: Denna Layer avser applikationer som är byggda ovanpå Bitcoin. BIP:erna i denna kategori handlar vanligtvis om modifieringar på nivån för Bitcoin Wallet-standarder.


Processen med att skicka in en BIP börjar med konceptualisering och diskussion av idén på e-postlistan *Bitcoin-dev*. Om idén är lovande skriver författaren ett utkast till en BIP enligt ett specifikt format och skickar in det via en Pull Request på Core GitHub-arkivet. Redaktörerna granskar detta förslag för att verifiera att det uppfyller alla kriterier. BIP:en måste vara tekniskt genomförbar, gynna protokollet, följa den formatering som krävs och vara i enlighet med Bitcoin:s filosofi. Om BIP:en uppfyller dessa villkor integreras den officiellt i GitHub-arkivet för BIP:ar. Den tilldelas sedan ett nummer. Detta nummer bestäms i allmänhet av redaktören, ofta Luke Dashjr, och tilldelas logiskt: BIP:ar som handlar om liknande ämnen får ofta nummer i följd.


BIP:erna går sedan igenom olika statusar under sin livscykel. Den aktuella statusen anges i rubriken för varje BIP:


- Utkast: Förslaget befinner sig fortfarande i berednings- och debattfasen;
- Föreslås: BIP:en anses vara komplett och redo för granskning av samhället;
- Uppskjuten: BIP:en läggs på is av mästaren eller en redaktör för att tas upp senare;
- Avvisad: En BIP klassificeras som avvisad om den inte har visat någon aktivitet på 3 år. Dess författare kan välja att återuppta den senare, vilket skulle göra det möjligt för den att återgå till statusen utkast;
- Återkallad: BIP:en har dragits tillbaka av dess författare;
- Slutlig: BIP accepteras och implementeras i stor utsträckning på Bitcoin;
- Aktiv: Endast för process-BIP:er tilldelas denna status när ett visst samförstånd har uppnåtts;
- Ersatt/föråldrad: BIP är inte längre tillämpligt eller har ersatts av ett nyare förslag som gör det överflödigt.





