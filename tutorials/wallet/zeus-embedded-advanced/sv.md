---
name: Zeus Embedded - Avancerad
description: Flernoder självförvarad Lightning-plånbok
---

![Zeus](assets/cover.webp)


## Introduktion till ZEUS Wallet


ZEUS är en mobil Bitcoin Wallet och nodhanteringsapp med full funktionalitet för en Bitcoin lightning Wallet som gör Bitcoin-betalningar enkla, ger användarna fullständig kontroll över sina finanser och låter mer avancerade användare hantera sina Lightning-noder från handflatan.


### Vem är ZEUS till för?

För närvarande är ZEUS för personer som kör sina egna hem- / företagsnoder [Lightning Network Daemon (LND)](https://lightning.engineering/) eller [Core Lightning (CLN)](https://blockstream.com/lightning/) och hanterar dem på distans via Zeus.


Handlare som använder [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) eller [Alby](https://getalby.com/) (eller något annat LNDhub-konto) kan också ansluta till, använda och hantera sina noder / konton via ZEUS.


[Från och med v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/) kommer ZEUS att börja tillgodose genomsnittliga användare som bara vill ha ett enkelt sätt att göra snabba och billiga bitcoin-betalningar från sin mobila enhet, med en [inbyggd mobil Lightning-nod](https://docs.zeusln.app/category/embedded-node) med en integrerad [Lightning-tjänsteleverantör (LSP)](https://docs.zeusln.app/lsp/intro).


### Viktiga Zeus-resurser:


- Zeus officiella webbsida - [https://zeusln.app/](https://zeusln.app/)
- Zeus Documentation - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Zeus Github-repository](https://github.com/ZeusLN/zeus)
- [Zeus Telegram-supportgrupp](https://t.me/ZeusLN)
- [Zeus på NOSTR](https://iris.to/zeus@zeusln.app)
- [Zeus Bloggmeddelanden](https://blog.zeusln.com)


### Zeus funktioner

#### Allmänna egenskaper:


- Självförvaltande, endast Bitcoin och Lightning Wallet
- Inga behandlingsavgifter, ingen KYC
- Helt öppen källkod (APGLv3)
- Stöd för flera noder/konton (du kan hantera dina egna hemnoder, köra inbäddade LND-noder, ansluta till flera LNDhub-konton)
- Lättanvänd aktivitetsmeny
- PIN- eller passphrase-kryptering, sekretessläge - dölj dina känsliga uppgifter
- Kontaktbok, multitema, multispråk


#### Tekniska egenskaper


- Anslut via Tor
- Fullständigt stöd för LNURL (betalning, uttag, autentisering, kanal), skicka till Lightning-adresser
- Detaljerad hantering av belysningskanaler, MPP/AMP-stöd, Keysend, hantering av routningsavgifter
- Replace-by-fee (RBF) och Barn betalar för förälder (CPFP) stöd
- NFC-betalningar och -förfrågningar, Signera och verifiera meddelanden
- Stöd för SegWit och Taproot
- Enkla Taproot-kanaler
- Självförvaltande blixtadresser (@zeuspay.com)
- Point of Sale by Square (snart öppen PoS)


### Guider och videohandledning

För att kunna använda Zeus och hantera Lightning-kanaler, likviditet, avgifter etc, är det bättre att först läsa några viktiga guider om Lightning Network.


#### Guider:


- [LND - Lightning Network Daemon-dokumentation](https://docs.lightning.engineering/)
- [CLN - Core Lightning-dokumentation](https://lightning.readthedocs.io/index.html)
- [Lightning-guide för nybörjare](https://bitcoiner.guide/lightning/) – av Bitcoin Q&A
- [Lightning Node-hantering](https://www.lightningnode.info/) – av openoms
- [Lightning-nätverket och flygplatsanalogin](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Hantering av Lightning Node-likviditet](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Underhåll av Lightning-nod](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Videohandledning av BTC-sessioner


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## En genomgångsguide för hur du börjar använda Zeus LN inbäddad nod på din mobila enhet


![Image](assets/en/01.webp)


Jag tillägnar denna guide till alla de nya Lightning Network (LN) -användare som vill börja en ny suverän resa med hjälp av en självförvarad nod Wallet på sina mobila enheter.


Låt oss överväga att du redan passerar genom all den överflöd av förvarings LN plånböcker, men du är inte redo ännu att börja köra en PUBLIC-routing LN-nod, du vill bara stapla mer Sats över LN på ett mer självförvaltande sätt och göra dina regelbundna betalningar över LN.


Här kommer Zeus, med början i [version v0.8.0 som tillkännagavs på deras blogg](https://blog.zeusln.com/new-release-zeus-v0-8-0/), som nu erbjuder en inbyggd LND-nod i appen. Fram till nu var Zeus en app för hantering av fjärrnoder + LNDhub-konton. Men nu… noden är i telefonen!


![Image](assets/en/02.webp)


### Snabb sammanfattning av huvudfunktionerna för Zeus Node:



- **Privat LND-nod** - Det innebär att denna nod INTE kommer att göra offentlig routing av andras betalningar genom din nod. Noden och kanalerna är oannonserade (privata, inte synliga på den offentliga LN-grafen). Att ta emot och göra betalningar kommer att göras genom dina anslutna LSP-kollegor. KOM IHÅG: Zeus Embedded Node kommer INTE att göra offentlig routing!
- **Ihållande LND-tjänst** - användaren kan aktivera den här funktionen och hålla LND-tjänsten aktiv kontinuerligt som vilken vanlig LN-nod som helst. Appen behöver inte vara öppen, den beständiga tjänsten kommer att hålla all kommunikation online.
-   **Neutrino-blockfilter** - block-synkronisering görs med [blockfilter och Neutrino-protokollet](https://bitcoinops.org/en/topics/compact-block-filters/) (utan någon information om våra användares on-chain-medel). Påminnelse: för internetanslutningar med hög latens / långsam hastighet kan denna Neutrino-baserade block-synkronisering ibland misslyckas. Att försöka byta till en närliggande Neutrino-server kan hjälpa till att återställa synkroniseringen. Utan denna synkronisering kan din LND-nod inte starta!
- **Enkla Taproot-kanaler** - När dessa kanaler stängs får användarna lägre avgifter och mer integritet eftersom de ser ut som alla andra Taproot-utgifter när de undersöker sitt On-Chain-avtryck.
- Integrerad **LSP** - Olympus är den nya LSP-noden för Zeus. Användare kan ta emot Sats över LN direkt, utan att tidigare ha satt upp LN-kanaler. De måste helt enkelt skapa en LN Invoice och betala från vilken annan LN Wallet som helst, med Zeus 0-conf-kanaltjänst. Läs mer om Zeus LSP här. LSP ger också ökad integritet till våra användare genom att förse dem med inplastade fakturor som döljer deras noders publika nycklar från betalare.
- **Kontaktbok** - du kan spara kontakter manuellt eller importera från NOSTR, så att du enkelt kan skicka betalningar till dina vanliga destinationer.
- Fullt stöd för LNURL, LN Address skicka och ta emot - nu kan du konfigurera din egen självförvaltande LN Address med @zeuspay.com. Påminnelse: Du kan också använda Zeus för LN-autentisering på webbplatser där du kan logga in med en LN-autentisering. Är mycket praktiskt.
- **Point of Sale** - Nu kan handlare skapa egna produkter och sälja direkt från Zeus, med integrerad PoS. Innehåller för närvarande grundläggande behov men kommer i framtiden att innehålla utökade funktioner.
- **LND-loggar** - användaren kan läsa LND:s serviceloggar i realtid och använda dem för att felsöka eventuella problem (främst dåliga anslutningar)
- Automatiserade säkerhetskopior - LN-nodkanalerna säkerhetskopieras automatiskt på Olympus-servern. Den här automatiska säkerhetskopian är krypterad med din nod Wallet seed (utan seed är den helt värdelös). Användaren kan också exportera manuellt en SCB (statisk kanalbackup) för katastrofåterställning.


### Så här kommer du igång med Zeus LN-nod (LND inbäddad)


I den här guiden kommer jag endast att tala om den inbyggda LND-noden, och inte om de andra sätten att använda denna fantastiska app (hantering av fjärrnoder och LNDhub-konton). För de andra typerna av anslutningar, vänligen se [Zeus-dokumentsidan](https://docs.zeusln.app/category/getting-started), som är mycket väl förklarad och inte kräver en separat guide.


#### STEG 1 - INLEDANDE INSTÄLLNING


På grund av att Zeus är en full LND-nod kommer jag att ha några initiala rekommendationer:



- Använd inte en gammal enhet, det kan påverka användningen av denna kraftfulla app. Speciellt under synkroniseringsperioden kan appen använda CPU och RAM intensivt. Avsaknaden av dessa kan till och med göra det omöjligt att använda Zeus-appen.
- Använd minst Android 11 som mobilt operativsystem och uppdatera så mycket som möjligt. För iOS samma sak, försök att använda en mycket högre version av OS.
- Du behöver minst 1 GB diskutrymme för datalagringen. Med tiden kan det bli mer, men det finns en funktion för att komprimera databasen till en nivå på MB.
- Det finns INGET behov av att använda Zeus med Tor eller Orbot-tjänsten. Vänligen komplicera inte saker mer än vad som är nödvändigt. Tor i det här fallet kommer inte att erbjuda dig mer integritet utan bara göra saker värre för den första synkroniseringen. Var också försiktig med vilka VPN: er du använder den och kontrollera latensen för anslutningen till Neutrino-servrar. Tänk på att Neutrino blockfilter inte läcker eller spårar din enhets identitet, bara serverar block. LN-trafiken är också bakom en LSP med privata kanaler så mycket få information är ute, det finns ingen anledning att flippa ut om integritet.
-   Ha tålamod för den initiala synkroniseringen, det kan ta flera minuter. Försök vara ansluten till en bredbandsanslutning med låg latens. Om du kör din egen Bitcoin-nod, [kan du aktivera neutrino-tjänsten](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core) och ansluta din Zeus till din egen nod, även med det interna LAN:et, så att du får maximal hastighet.


När du har ställt in anslutningstypen "Inbäddad nod" kommer appen att börja synkronisera ett tag. Vänta tålmodigt tills den delen är klar och gå sedan in på huvudinställningssidan.


![Image](assets/en/03.webp)


Låt oss kortfattat gå in på varje avsnitt i Inställningar och förstå några av de viktigaste funktionerna innan du börjar använda Zeus:


**A - INSTÄLLNINGAR**


Det här är ett avsnitt med allmänna inställningar för hela appen


**1 - Lightning Service Provider (LSP)**


Här presenteras två LSP-tjänster:



- _Just in time channels_ - när du inte har någon kanal öppen eller inkommande likviditet tillgänglig kommer tjänsten, om den är aktiverad, att öppna en kanal i farten åt dig. Det här alternativet kan avaktiveras om du inte vill öppna fler kanaler av den här typen.
- _Begära kanaler i förväg_ - du kan köpa inkommande kanaler från Olympus LSP direkt i appen med flera alternativ och belopp (för inkommande och utgående).


LSP hjälper användare att ansluta till Lightning-nätverket genom att öppna betalningskanaler till deras noder. [Läs mer om LSP här](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS har en ny integrerad LSP kallad [OLYMPUS by ZEUS](https://mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), som är tillgänglig för alla användare som använder den nya inbäddade noden.


I det här avsnittet är Olympus LSP (https://0conf.lnolymp.us) som standard, men snart kan du också ställa in en annan 0conf LSP som stöder detta protokoll.


_Håll i minnet:_

när du öppnar en kanal med Olympus LSP med hjälp av de inslagna LN-fakturorna får du också en 100k inkommande likviditet! Detta är ett riktigt bra alternativ om du behöver ta emot mer Sats direkt

_Exempel: du sätter in 400k Sats för att öppna en LSP-kanal, då öppnar LSP:n en kanal med 500k Sats kapacitet mot din Zeus-nod och skjuter de 400k Sats du sätter in mot din sida

_"Inkommande likviditet" = mer "utrymme" i din kanal för att ta emot


I framtiden hoppas vi att vi kan ha många andra LSP som kan integreras i Zeus och använda alternativt var och en. Det är bara en tidsfråga innan nya LSP:er kommer att anta en öppen standard för den här typen av 0conf-kanaler.


Om du inte vill öppna nya kanaler "on the fly" kan du avaktivera det här alternativet.


I samma avsnitt har du också möjlighet att välja "begära enkla Taproot-kanaler" när LSP:n öppnar en kanal mot din Zeus-nod. Dessa enkla Taproot-kanaler erbjuder bättre On-Chain-integritet och lägre avgifter vid kanalstängning. Det finns bara två anledningar till att du inte skulle vilja använda dem:



- De är nya, och det kan fortfarande finnas buggar i LND när de används.
- Din motpart stöder dem inte. Även LND-noder måste uttryckligen välja att använda dem, för tillfället.


**2 - Betalningsinställningar**


Den här funktionen ger dig möjlighet att ställa in dina egna önskade avgifter för betalningar, över LN eller onchain. Du får också möjlighet att öka eller minska timeouten för dina fakturor.


Om några av dina LN-betalningar misslyckas kan du höja avgiften för att hitta en bättre rutt. Även om du gör onchain txs kan du ställa in en specifik avgift så att din tx inte kan fastna i Mempool under lång tid, i händelse av höga avgiftsperioder.


**3 - Inställningar för fakturor**


I detta avsnitt finns några alternativ till generate-fakturor:



- Ställ in ett standardmemo som ska visas i Invoice eller generate
- Utgångstid i sekunder, om du vill ha en specifik tid, längre eller kortare för att din Invoice ska betalas
- Inkludera rutttips - ge information för att hitta icke-annonserade, eller privata, kanaler. Detta gör det möjligt att dirigera betalningar till noder som inte är allmänt synliga i nätverket. En routing hint ger en partiell rutt mellan mottagarens privata nod och en publik nod. Denna routing hint inkluderas sedan i den Invoice som genereras av mottagaren och tillhandahålls betalaren. Jag föreslår att den är aktiverad som standard, annars kan inkommande betalningar misslyckas (ingen rutt hittad).
- AMP Invoice - Atomic Multi-path Payments är en ny typ av blixtbetalningar som implementeras av LND som gör det möjligt att ta emot Sats utan en specifik Invoice, med hjälp av [Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-Keysend). Är praktiskt taget en statisk betalningskod. [Läs mer här](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Show custom preimage field - använd detta alternativ endast i mycket specifika fall när du verkligen vill använda anpassade fält i förbilden. [Läs mer här](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Ett annat alternativ i detta avsnitt är hur du ställer in vilken typ av onchain Address du vill använda: SegWit nästlad, SegWit, Taproot.


![Image](assets/en/04.webp)


Klicka på den övre hjulknappen så visas en popup-skärm där du kan välja önskad typ av Address. När du har ställt in det, nästa gång du trycker på mottagningsknappen för onchain, kommer det att generate den valda Address-typen. Du kan ändra det när som helst.


**4 - Inställningar för kanaler**


I det här avsnittet förinställer du vissa funktioner för öppningskanaler, t.ex:



- antal bekräftelser
- Meddela kanal (som standard är av), vilket innebär att det kommer att vara oannonserade kanaler
- Enkla Taproot-kanaler
- Visa inköpsknapp för kanal


**5 - Inställningar för sekretess**


Här hittar du några grundläggande inställningar för att öka integriteten med Zeus-appen:



- Block explorer för att öppna tx-detaljer (Mempool.space, blockstream.info eller anpassad personlig)
- Läs urklipp - slå på/av om du vill att Zeus ska läsa urklippet på din enhet
- Lurker-läge - på/av-växling om du vill dölja specifik känslig information från din Zeus-app. Är ett bra alternativ när du gör demos eller skärmdumpar.
- Mempool avgiftsförslag - aktivera detta alternativ om du vill använda rekommenderade avgiftsnivåer från [Mempool.space](https://Mempool.space/)


**6 - Säkerhet**


I det här avsnittet finns det bara två alternativ för att säkra appen vid öppning: ange ett lösenord eller en PIN-kod.


När du har angett en PIN-kod för att öppna appen kan du också ange en "överfalls-PIN-kod". Denna hemliga extra PIN-kod kommer ENDAST att användas i en nödsituation, om du är hotad. Om du sätter den här PIN-koden kommer konfigurationen att raderas helt och hållet. Så det är bäst att du håller dina säkerhetskopior uppdaterade. Automatiska säkerhetskopior är PÅ som standard, men det är bra att ha dina egna säkerhetskopior också, utanför enheten.


**7 - Valuta**


Aktivera eller inaktivera alternativet att visa en fiat-valutakonvertering i Zeus-appens användning. För närvarande stöds över 30 globala fiatvalutor.


**8 - Språk **


Du kan växla mellan flera olika översättningsspråk, som granskats av Zeus community med modersmålstalare.


**9 - Display **


I det här avsnittet kan du anpassa din Zeus-display genom att välja olika färgteman, standardskärm (knappsats eller balans), visa ditt nodalias, aktivera stora knappsatser och visa fler decimaler.


**10 - Försäljningsställe**


Detta är en speciell funktion för att aktivera / inaktivera ett integrerat PoS-system i Zeus. Du kan köra en fristående PoS eller länkad till ett Square PoS-system. För närvarande stöder grundläggande funktioner som en PoS, men tillräckligt för en bra start och kan hjälpa de små handlarna (barer / restauranger, livsmedelsbutiker) att börja acceptera BTC på ett inbyggt sätt.


I de här inställningarna hittar du olika alternativ för att konfigurera din PoS:



- Typ av bekräftelse på betalning: Endast LN, 0-conf, 1-conf
- Aktivera/avaktivera dricks för anställda som sköter kassan
- Visa/dölj knappsats
- Skatteprocent som ska tillämpas på biljetten
- Skapa produkter och produktkategorier
- En enkel lista över alla försäljningar


Här är en live demo video om hur du använder Zeus PoS:


**B - Reserv Wallet**


Den inbäddade noden i ZEUS är baserad på LND och använder [aezeed seed format](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Detta skiljer sig från det typiska [BIP39-formatet](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) som du ser i de flesta Bitcoin-plånböcker, även om det kan tyckas vara liknande. Aezeed innehåller lite extra data inklusive födelsedatum för Wallet som hjälper omskanningar under återhämtningen att ske mer effektivt.


Nyckelformatet aezeed bör vara kompatibelt med följande mobila plånböcker: Blixt, BlueWallet och Breez. Observera att enbart seed kommer att vara otillräckligt för att återställa alla dina saldon om du har öppna eller väntande stängningskanaler!


Läs mer om säkerhetskopiering och återställning på [Zeus Docs page](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


RÅD OM STRÖMFÖRSÖRJNING: När du sparar din seed, spara även nodens pubkey! Ibland är det bra att ha den till hands, tillsammans med din seed och SCB (Static Channels Backup) om du behöver verifiera återställningen.


SCB är endast nödvändigt om du har LN-kanaler öppna. Om du bara har onchain-fonder är det inte nödvändigt.


Om du ser att efter en lång tid fortfarande inte visar den gamla historiken txs, gå till Inbäddad nod - Peers och inaktivera alternativet att använda listan över valda peers (som standard är btcd.lnolymp.us). Det kommer att utlösa en omstart och kommer att ansluta till den första tillgängliga neutrino-noden med ett bättre tidssvar. Eller använd de nedan nämnda andra välkända neutrino-peers.


Om du vill se fler återställningsalternativ för en LND-nod, [läs min tidigare guide](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), där du kan hitta stegen för hur du importerar en aezeed seed till Sparrow wallet eller andra metoder.


**C - Inbäddad nod**


I det här avsnittet hittar du några grundläggande verktyg för att hantera den integrerade noden:



- _Disaster Recovery_ - Automatiserade och manuella säkerhetskopior för LN-kanalerna. Läs mer om hur du använder den här funktionen på Zeus Docs-sidan.
- _Express Graph Sync_ - Zeus app laddar ner LN skvallerdatagrammet från en dedikerad server för snabbare och bättre synkronisering, och erbjuder bästa betalningsvägar. Du kan också välja att rensa tidigare grafdata vid uppstart.
- _Peers_ - avsnitt för att hantera neutrino-peers och 0-conf-peers. Om du har problem med den första synkroniseringen, kanaler som inte kommer online, beror det på att din enhet har hög latens med den konfigurerade neutrino-peeren. Försök att byta från listan över föredragna peers eller lägg till din specifika peer som du vet att den har bättre latens för synkronisering. Välkända neutrino-servrar är:



 - btcd1.lnolymp.us | btcd2.lnolymp.us - för USA-regionen
 - sg.lnolymp.us - för Asien-regionen
 - btcd-Mainnet.lightning.computer - för USA-regionen
 - uswest.blixtwallet.com (Seattle) - för regionen USA
 - europe.blixtwallet.com (Tyskland) - för EU-regionen
 - asia.blixtwallet.com - för Asien-regionen
 - node.eldamar.icu - för region i USA
 - noad.sathoarder.com - för USA-regionen
 - bb1.breez.technology | bb2.breez.technology - för USA-regionen
 - neutrino.shock.network - region USA



- _LND logs_ - mycket användbart verktyg för att felsöka dina LN nodproblem och kontrollera på djupet vad som händer på en mer teknisk nivå.
- _Avancerade inställningar_ - fler verktyg för att styra användningen av din LND-nod:



 - _Pathfinding mode_ - bimodal eller apriori, sätt att hitta en bättre rutt för dina LN-betalningar och även återställa den tidigare ruttinformationen. Läs gärna dessa mycket bra guider om pathfinding: [Pathfinding](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - av Docs Lightning Engineering och [LN Payment Pathfinding](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - av Voltage
 - _Persistent LND_ - aktivera det här läget om du vill att LND-tjänsten ska köras kontinuerligt i bakgrunden och hålla din nod online 24/7. Detta är mycket användbart om du använder Zeus som en PoS i en liten butik eller om du får många LN-tips via LN Address.
 - _Rescan wallet_ - det här alternativet kommer vid omstart att utlösa en fullständig skanning av alla tx:er i kedjan i din Wallet. Aktivera det endast om du saknar några tx:er i din Wallet. Omskanningsuppgiften kommer att ta tid, flera minuter, så ha tålamod och kontrollera alltid loggarna för att se mer information om framstegen.
 - _Compact Database_ - det här alternativet är mycket användbart om din Zeus-app tar upp mycket utrymme på enheten (se appdetaljer i enhetens inställningar). Om du har mycket aktivitet med Zeus skulle jag rekommendera att du gör denna komprimering oftare. När du ser att du har mer än 1-1,5 GB data för Zeus-appen, gör komprimeringen. Det kommer att starta om och ta lite tid, så ha tålamod.
 - _Delete Neutrino files_ - det här alternativet för att radera neutrino-filerna (med en omstart) kommer att minska datalagringsanvändningen mycket. Minskad dataanvändning har också en stor inverkan på batterianvändningen, vilket minskar batterianvändningen, särskilt om du använder Zeus i persistent läge.


**D - Info om noden**


I det här avsnittet hittar du mer information om statusen för din Zeus-nod som:



- Alias - kort nod-ID
- Public Key - den fullständiga offentliga nyckeln för din nod som krävs för att andra noder ska hitta vägen till din nod. Kom ihåg att denna publika nyckel INTE är synlig på de vanliga LN-utforskarna (Mempool, Amboss, 1ML etc.). Denna publika nyckel kan ENDAST nås via dina anslutna LN-peers och kanaler.
- LN implementeringsversion
- Zeus app version
- Synkroniserad med kedja och Synkroniserad med grafstatus - mycket viktiga statusar som visar rätt status för din nod. Om dessa två inte visar "true" betyder det att din nod fortfarande synkroniserar eller har problem med synkroniseringen. Så vi föreslår att du tittar i dina LND-loggar eller väntar lite längre.
- Blockhöjd och Hash - visar det senaste blocket och Hash som din nod såg och synkroniserade.


**E - Information om nätverket**


I det här avsnittet visas mer information om den allmänna statusen för Lightning Network, som hämtats från synkroniseringsdata för grafen: antal tillgängliga publika kanaler, antal noder, antal zombiekanaler (offline eller döda), grafdiameter, genomsnittlig och maximal grad för grafen.


Dessa informationsdata kan vara användbara för felsökning eller bara användas för statistik.


**F - Blixt Address**


I det här avsnittet kan användaren ställa in sin egen självförvarare LN Address @zeuspay.com.


ZEUS PAY utnyttjar användargenererade preimage-hashar, HODL-fakturor och Zaplockers Nostr-attesteringssystem för att tillåta användare som kanske inte är online 24/7 att ta emot betalningar till en statisk blixt Address. Användare behöver bara logga in på sina ZEUS-plånböcker inom 24 timmar för att göra anspråk på betalningarna, annars kommer de att returneras till avsändaren.


Om du aktiverar "persistent mode" kommer alla betalningar till din LN Address att tas emot direkt.


Läs mer om hur [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) betalningar fungerar och mer om [ZeusPay-avgifter här](https://docs.zeusln.app/lightning-Address/fees).


**G - Onchain-adresser**


I det här avsnittet kan du konsultera dina genererade onchain-adresser för en bättre myntkontroll


**H - Kontakter**


En ny kontaktbok introducerades i Zeus v 0.8.0 som du kan använda för att snabbt skicka betalningar till dina vänner och familj, även med möjlighet att importera dina kontakter från Nostr.


Ange bara din Nostr npub eller mänskligt läsbara NIP-05 Address, så kommer ZEUS att fråga Nostr efter alla dina kontakter. Därifrån kan du skicka en snabb betalning till en kontakt, eller importera alla eller utvalda kontakter till din lokala kontaktbok./<


Här följer en kort video om hur du konfigurerar och använder dina Zeus-kontakter:


**I - Verktyg**


Här har vi olika underavdelningar med fler verktyg:



- _Accounts_ - här kan du importera externa konton/plånböcker, Cold-plånböcker, Hot-plånböcker, för att kontrollera eller använda som extern finansieringskälla för dina Zeus-nodkanaler. Den här funktionen är fortfarande experimentell.
- _Speed up transaction_ - Den här funktionen kan vara till hjälp när du har en fastnad tx till Mempool och vill höja avgiften. Du måste ange tx-utgången från tx-detaljer och välja önskad ny avgift som du vill använda. Måste vara högre än den tidigare och kräver att du har mer pengar tillgängliga i din onchain Wallet.


![Image](assets/en/05.webp)


Du måste gå till din väntande tx och kopiera txid outpoint. Kom sedan till det här avsnittet och klistra in det och välj sedan den nya avgiften du vill använda för att stöta på den. Det kommer att dyka upp en ny skärm med rekommenderade avgifter i det ögonblicket, eller så kan du ställa in en anpassad. Kom ihåg MÅSTE vara högre än den tidigare.


Är alltid bättre att hålla en UTXO med högst 100k Sats i din Zeus onchain Wallet, för att kunna använda den för att stöta på avgifter när det är nödvändigt.



- _Signera eller verifiera_ - Med den här funktionen kan du signera ett specifikt meddelande med dina Wallet-nycklar. Den kan också användas för att verifiera ett meddelande för att bevisa att det kommer från en viss Wallet-nyckel.
- _Currency converter_ - ett enkelt verktyg för att beräkna kursomvandlingen mellan BTC och andra fiatvalutor.


**J - Merchandise och support**


Här hittar du mer information och länkar om Zeus, webbutik, sponsorer, sociala medier.


**K - Hjälp**


I det här sista avsnittet hittar du länkar till Zeus dokumentationssida, Github-problem (om du vill skicka en bugg eller begäran direkt till apputvecklare), e-postsupport.



### STEG 2 - BÖRJA ANVÄNDA ZEUS-NODEN



Kom ihåg att Zeus huvudsakligen ska användas som en LN Wallet, för enkla och snabba betalningar över LN. Visst, det innehåller också en Wallet på kedjan, men den ska användas uteslutande för att öppna / stänga LN-kanaler och inte för regelbundna betalningar av ett kaffe.


Läs gärna min andra guide om [hur du blir din egen bank med hjälp av de 3 nivåerna i Stash](https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


I det här ögonblicket har användaren två sätt att börja använda Zeus:



- Direkt över LN, med 0-conf-kanalen från Olympus LSP
- Gör först en insättning i onchain Wallet och öppna sedan en normal LN-kanal med den peer du önskar.


#### Metod A - Använda Olympus LSP


Detta är ett mycket enkelt och rakt sätt att ta ombord en ny LN-användare med Zeus. Det kan vara en helt ny Bitcoin-användare som inte har någon Sats alls, ombord av en vän, eller en ny handlare som börjar med sin första LN-betalning.


Som standard kommer Zeus att använda sin egen LSP, Olympus. Men senare kan du även byta till andra LSP:er som stöder detta 0-conf-protokoll för att öppna kanaler.


Genom att helt enkelt skapa en Invoice på din Zeus (ange beloppet och klicka på "begär" -knappen) kommer du att kunna ta emot dessa Sats direkt.


Den Invoice du generate kommer att vara [wrapped](https://docs.zeusln.app/lsp/wrapped-invoices) och du kommer att presenteras med de avgifter som är förknippade med tjänsten om de betalas. Denna inplastade Invoice innehåller rutttips mot din Zeus-nod, så att LSP kan hitta din nya nod och öppna en kanal med de nya medel du sätter in.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


För att få en LN-kanal från LSP med de medel du vill ta emot första gången måste denna Invoice betalas från en annan LN Wallet och vänta några ögonblick tills LSP öppnar kanalen mot din Zeus-nod, drar av avgiften och skjuter det återstående beloppet av betalningen på din sida av kanalen.


Allt du behöver göra är att betala Invoice som genererats för dig i ZEUS med en annan blixt Wallet, och din kanal öppnas omedelbart. [Vänligen se Zeus LSP-avgifter](https://docs.zeusln.app/lsp/fees).


En annan fördel med att betala för en kanal är nollavgiftsrouting. Det innebär att när du dirigerar betalningar medför det första hoppet genom OLYMPUS by ZEUS inga dirigeringsavgifter. Observera att hopp bortom OLYMPUS by ZEUS fortfarande kommer att debitera dig.


När kanalen är klar klickar du på den högra knappen längst ned på skärmen, som visar Zeus-kanalerna.


![Image](assets/en/08.webp)


Och du kommer att se en kanal som den här, som visar din sida av kanalbalansen:


![Image](assets/en/09.webp)


Ju mer du spenderar från den här kanalen, desto mer inkommande likviditet kommer du att ha. Ju mer Sats du får in i den här kanalen, desto mindre inkommande likviditetsutrymme kommer du att ha.


Här är en enkel visuell demonstration (av Rene Pickhardt) om hur LN-kanaler fungerar:


I det här ögonblicket, med tanke på demo-skärmen för kanaler, klicka på kanalnamnet så får du mer information om det.


Du har en enda kanal med Olympus, med en total kapacitet på 490 000 Sats, med en balans på 378k Sats på din sida och 88k Sats på Olympus sida. Det innebär att du kan ta emot maximalt 88k Sats mer i samma kanal.


Om du behöver ta emot mer än 88k Sats (den tillgängliga inkommande likviditeten i det här fallet), låt oss säga ytterligare 500k Sats, genom att helt enkelt skapa en ny LN Invoice med det beloppet, kommer att utlösa en ny kanalbegäran till Olympus LSP. Så du kommer att få en 2:a kanal.


För att undvika att betala mer avgifter för att öppna flera kanaler rekommenderas det därför att öppna en större kanal första gången, låt oss säga 1-2M Sats. När den är öppen kan du byta ut till onchain-del av dessa Sats, låt oss säga 50%, med hjälp av någon extern swaptjänst som beskrivs i den här guiden.


När du har bytt ut från den kanalen, låt oss säga 50% och få tillbaka Sats till din egen Zeus onchain Wallet, är du redo att gå vidare till nästa metod för att öppna en ny kanal - från onchain-balans.


#### Metod B - Använda ditt onchain-saldo


Med den här metoden kan du öppna kanaler mot vilken annan LN-nod som helst, inklusive samma Olympus LSP. Men om du redan har en kanal med Olympus rekommenderas att du också har det med en annan nod, för mer tillförlitlighet och kan också använda MPP (multi-part payment).


![Image](assets/en/10.webp)


Ovan är ett exempel på betalning av en LN Invoice med MPP. Som du kan se längst ned på skärmen har du "inställningar" och öppnar en rullgardinsmeny med mer information om den betalning du håller på att göra. På den skärmen, om du har minst 2 kanaler öppna, kommer MPP-funktionen att vara PÅ som standard. Du kan också aktivera AMP (atomic multi-path) och ställa in specifika delar du vill ha. Det här är en kraftfull funktion!


För en privat nod som Zeus skulle jag rekommendera att ha 2-3 bra kanaler (max 4-5), med bra LSP:er och bra likviditet för att täcka alla dina behov av att betala eller ta emot Sats över LN. [Se mer råd om likviditet för LN-noden i den här guiden](/nodes/managing-lightning-node-liquidity-en.html). Även här en annan [allmän guide om LN likviditet](https://Bitcoin.design/guide/how-it-works/liquidity/) från Bitcoin Design team.


Att välja rätt peers, jag vet, är inte en lätt uppgift, inte ens för erfarna användare. [Så jag ska ge dig några alternativ att börja med](https://github.com/ZeusLN/zeus/discussions/2265), det här är peer-noder som jag testade själv med Zeus (jag försökte ansluta endast till LND-noder för att undvika inkompatibilitetsproblem)


Här finns också en lista över vouched node peers för Zeus. Om du känner till bra sådana är du välkommen att lägga till dem i den listan.


Du kan öppna en kanal i Zeus genom att gå till vyn Channels genom att klicka på kanalikonen i det nedre högra hörnet av huvudvyn och sedan trycka på ikonen + i det övre högra hörnet.


![Image](assets/en/11.webp)


Om du vill öppna en kanal med en specifik nod klickar du på (A) i övre hörnet för att skanna nodens QR-nodID (på Mempool, Amboss, 1ML kan du få den QR) och alla peer-detaljer kommer att fyllas i.


PÅMINNELSE:


- Zeus inbäddade nod använder inte Tor-tjänsten! Så försök inte att öppna kanaler med noder som är under Tor! Du gör mer skada på dig själv än att lägga till mer integritet. Tor för LN erbjuder inte mer integritet utan ger mer problem.
- välj klokt dina kamrater, bättre vara bra LSP: er, bra routingnoder, inte slumpmässiga pleb-noder som kan stänga dina kanaler och inte kan erbjuda god likviditet. [Här skrev jag en dedikerad guide](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) om likviditet och exempel på noder.


Om du klickar direkt på knappen "Öppna kanal till Olympus" kommer du att fylla i de obligatoriska fälten för att öppna en kanal till [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


Till skillnad från betalda LSP-kanaler kommer din kanal att kräva On-Chain-bekräftelse med hjälp av dina onchain-medel (du kan välja från dina UTXO:er i vyn för öppen kanal); den öppnas inte direkt. Kontrollera först de faktiska Mempool-avgifterna och justera dem i enlighet med detta, beroende på hur snabbt du vill öppna kanalen.


Innan du trycker på knappen för att öppna kanalen, skjut ner de avancerade alternativen:


![Image](assets/en/12.webp)


Du måste också se till att kanalen är oannonserad (privat). Som standard är alternativet avaktiverat för aviserade kanaler. Det här alternativet rekommenderas inte att aktiveras för Zeus inbäddade nod, det är endast användbart när du använder Zeus med din fjärrnod, som en offentlig routingnod.


Till skillnad från betalda LSP-kanaler kommer du inte att dra nytta av nollavgiftsrouting genom att öppna kanaler med den här metoden.


Och klart, klicka bara på knappen "Open Channel", vänta på att tx ska bekräftas av gruvarbetarna. När kanalen är öppen kan du göra transaktioner som du vill med Sats från dina kanaler.


Tänk på att dessa kanaler kommer att ha all balans på DIN sida, så du kommer inte att ha inkommande likviditet. Som jag sa tidigare, byt ut eller spendera lite Sats på att köpa saker över LN för att "skapa mer utrymme" för att ta emot.


Tänk på dina LN-kanaler som ett glas vatten. Du häller lite vatten (Sats) i ett tomt glas (din kanal) tills du fyller upp det. Du kan inte hälla upp mer vatten förrän du har druckit lite (spenderat/bytt ut). När glaset är nästan tomt häller du mer vatten (Sats) i det genom att använda en swap in. [Läs mer om externa bytestjänster här](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


Det finns också andra LSP-tjänster som säljer dig inkommande kanaler: LNBig eller Bitrefill. Jag tror att det finns fler tjänster som dessa men kan inte komma ihåg dem just nu.


Så om du behöver praktiskt taget en tom LN-kanal (balansen är 100% på peer-sidan från början), för att ta emot fler betalningar än du kan hantera på dina befintliga fyllda kanaler, kan detta vara ett mycket bra alternativ. Du betalar en specifik avgift för att öppna dessa kanaler och du får gott om inkommande utrymme.



## TIPS OCH TRICKS


### Reservgränser för inkommande


Just nu, på grund av vissa LN-kodbegränsningar, är det inte möjligt att få exakt hur mycket som visas i "Inbound". Tänk alltid på att du bör göra dina fakturor med ett något mindre belopp, respektive beloppet för "Channel Local Reserve".


![Image](assets/en/13.webp)


Som du kan se i ovanstående bild visar "inkommande" att jag fortfarande kan ta emot 5101 Sats, men i själva verket är det omöjligt att ta emot mer i det här ögonblicket. Och du kan observera att det är samma belopp som den "Lokala reserven".


Så kom ihåg att när du gör fakturor att ta emot, ta också en titt på dina kanalers likviditet och dra av den lokala reserven från det beloppet, om du vill pressa till gränserna för fordringsbeloppet.


### Snabba råd till nya användare som börjar använda Zeus node:



- Utnyttja dina nya kanaler på rätt sätt.


Om du till exempel vet att du om en vecka kommer att få låt oss säga 1 miljon Sats, öppna en 2 miljoner Sats-kanal och swappa ut till onchain Wallet eller till ett annat (tillfälligt) depå LN-konto 50-60% av din utgående likviditet. Var alltid beredd med mer likviditet. När du behöver mer likviditet tillbaka i dina Zeus-kanaler kan du flytta tillbaka den från depåkontona.


Om du vet att du kommer att skicka låt oss säga 500k Sats/vecka, öppna då en 1M Sats kanal. På så sätt kommer du fortfarande att ha en reserv tills du fyller upp den igen.



- Om du är en handlare och du alltid kommer att få mer än du spenderar regelbundet, köp en dedikerad inkommande kanal. Är det billigaste sättet. Du betalar en minimal avgift och du får en "tom" kanal.



- Öppna inte små meningslösa kanaler på 50-100-300-500k Sats. Du kommer att fylla dem inom några dagar, även om du bara använder dem för zaps. Öppna större och olika, INTE bara en kanal.


När du har öppnat en större kanal kan du alltid använda externa ubåtsswappar för att flytta Sats till dina onchain-plånböcker (inklusive tillbaka till Zeus onchain). Att hålla en balans mellan in- och utlikviditet är bra och du kan också "återanvända" dessa Sats för att öppna fler kanaler om du vill.


### Inplastad Invoice


Om du vill lägga till mer integritet när du tar emot, kan du använda metoden "wrapped Invoice". Påminnelse: För att kunna göra detta behöver du en kanal med Olympus LSP. Inslagna fakturor kommer att "dölja" slutdestinationen (din Zeus-nod) och visa din LSP-nod som destination för betalaren.


För att få en inplastad Invoice, gå till huvudknappsatsskärmen, sätt beloppet och tryck på begäran. Kommer att visa en normal QR-kod för din Invoice. Klicka nu på den övre högra "X" -knappen så kommer du att omdirigeras till fler alternativ för Invoice.


![Image](assets/en/14.webp)


Nu måste du aktivera det alternativet ovanpå "Aktivera LSP" och trycka på knappen "Skapa Invoice". Det alternativet kommer att skapa den inslagna Invoice och kom ihåg, kommer att ta ut en liten avgift.


### Fakturor med vägbeskrivningar


Detta är en mycket användbar funktion om du vill hantera flera inkommande kanalers likviditet. I praktiken kan du ange till vilken inkommande kanal du vill ta emot Sats från en Invoice.


Den här funktionen kan också användas för cirkulär rebalansering, när du vill flytta likviditet från en fylld kanal till en annan tömd.


Hur skapar man en Invoice med rutttips?



- På huvudskärmen, skjut LN-lådan åt höger och klicka på "Receive"
- I inställningarna för Invoice går du till den nedre delen och aktiverar knappen "Insert route hints" och väljer sedan fliken "Custom". En skärm med alla dina tillgängliga kanaler öppnas. Välj den som du vill ta emot.
- Fyll i alla övriga uppgifter för Invoice, belopp, memo etc och klicka på "skapa Invoice".
- Genom att betala den Invoice kommer Sats att föras in i den angivna kanalen.


Om du vill betala den Invoice till dig själv (cirkulär ombalansering), när du betalar den från samma Zeus-nod, väljer du i betalningsskärmen den utgående kanal (en med mer likviditet) som du vill använda för att skicka betalningen.


### Betala med Keysend


Keysend är en mycket underskattad LN-funktion och användare bör använda den oftare.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-Keysend) gör det möjligt för användare i Lightning Network att skicka betalningar till andra , direkt till deras publika nyckel, så länge deras nod har publika kanaler och har Keysend aktiverat. Keysend kräver inte att betalningsmottagaren utfärdar en Invoice.


Så hur kan du göra det med Zeus?


Skanna eller kopiera helt enkelt destinationens nodeID (eller använd Zeus-kontakter för att spara dina vanliga destinationsnoder som kontakter) och klicka sedan på "Skicka"-knappen från Zeus huvudskärm. På den skärmen klistrar du sedan in nodID eller väljer från dina kontakter.


Ange beloppet för Sats, ett meddelande om det behövs (ja, du kan också använda det som en hemlig chatt över LN) och klicka på "Skicka" -knappen. Nu är det klart!


![Image](assets/en/15.webp)


Om du har en direktkanal med destinationspartnern tillkommer INGA avgifter.


Om du inte har en direktkanal med destinationspeeren kommer Keysend-betalningen att betala avgifterna som en vanlig LN Invoice-betalning, dirigerad på en reguljär väg som alla andra betalningar. Kom bara ihåg att det inte kommer att finnas några spår som en LN Invoice.


## Sammanflätning


Jag rekommenderar att du läser uppföljningsguiden [Avancerad användning av Zeus](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) med fler instruktioner och användningsfall.


Och... det är allt! Från och med nu använder du bara Zeus Node som en vanlig BTC/LN Wallet på din mobil. Användargränssnittet är ganska rakt fram och lätt att använda, intuitivt för alla typer av användare, jag tror inte att jag behöver ange mer detaljer om hur man gör och tar emot betalningar.


Sammanfattningsvis är här en jämförelse av sekretessdiagram :


![Image](assets/en/16.webp)
