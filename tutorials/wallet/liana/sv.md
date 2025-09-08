---
name: Liana
description: Konfigurera och använda en Wallet på Liana
---
![cover](assets/cover.webp)


![video](https://youtu.be/rTId6hfiRm0)


I den här handledningen förklarar vi steg för steg hur du använder Liana-applikationen på en dator. Du får bland annat lära dig hur du skapar en automatiserad successionsplan, tar emot och skickar bitcoins i normala situationer och hämtar medel från en befintlig Wallet efter en viss period.


I januari 2025 var de hårdvaruplånböcker som var kompatibla med Liana: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Spectre DIY.


Om du vill återfå pengar från en befintlig Liana Wallet, läs presentationen nedan och gå direkt till avsnittet "Återfå bitcoins".


## Introduktion av Liana programvara


Liana är ett mjukvarupaket med öppen källkod som är utformat för att skapa och hantera avancerade plånböcker, särskilt som en del av ett automatiserat arvssystem eller en robust säkerhetskopieringsmekanism. Projektet har utvecklats sedan 2022 av Wizardsardine, ett företag som grundades av Kévin Loaec och Antoine Poinsot. På den officiella webbplatsen presenteras Liana som "en enkel Wallet för personlig kurering, med återställnings- och arvsfunktioner". Programvaran körs på datorer - Linux, MacOS, Windows - och dess (öppna) källkod finns tillgänglig [på GitHub] (https://github.com/wizardsardine/Liana).


Liana bygger på Bitcoin:s programmerbarhet för att skapa en avancerad Wallet. I synnerhet utnyttjar den tidslås (*timelocks*), som gör det möjligt att spendera pengar först när en viss tidsperiod har gått, och som är involverade i återvinningen av Bitcoins. En Liana Wallet består således av flera utgiftsvägar:




- En huvudutgiftsväg som alltid är tillgänglig;
- Minst en återställningsväg, som blir tillgänglig efter en viss tid.


Diagrammet nedan illustrerar hur en Wallet med två utgiftsvägar fungerar:


![Schéma explicatif](assets/fr/01.webp)


Med denna funktion kan du ställa in olika konfigurationer, inklusive :




- En successionsplan (eller arvsplan) som gör det möjligt för arvingar att återfå medel om användaren skulle avlida. För mer information om detta ämne rekommenderar vi att du läser [del 4](https://planb.network/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f/233c88d3-2e8e-5eba-ac06-efe67a209038) i BTC102-kursen.
- En förstärkt backup med återställningstid, vilket ger användaren möjlighet att använda sin Wallet utan att behöva behålla motsvarande hemliga fras och riskera att den blir stulen, till exempel vid ett inbrott.
- Ett skyddsnät för personer som börjar med Bitcoin: de kommer att hantera sina egna Wallet, och deras "förmyndare" (till exempel en släkting) kommer att förbehålla sig rätten att återfå sina medel efter en viss period.
- Ett flerpartssignaturprogram (*Multisig*) med reducerade krav över tiden för att klara av att en eller flera av deltagarna försvinner, t.ex. ett företags delägare.


Den stora styrkan med Liana är att den introducerar ett standardiserat sätt att garantera återvinning av medel i händelse av förlust av huvudnyckeln, som används för löpande utgifter. Detta utgör en enorm innovation för ren förvaring av medel, vilket är förenat med risker, särskilt om du inte är välinformerad om ämnet. Liana kan därför uppmuntra även de mest riskbenägna användarna att sluta använda ett förvaringsinstitut (t.ex. en Exchange-plattform) för att hålla sina medel och återfå Ownership av sina pengar, i enlighet med Bitcoin:s Cypherpunk-etos.


Naturligtvis har Liana sina nackdelar. Den första är att du måste uppdatera din Wallet regelbundet genom att göra en transaktion på Bitcoin Blockchain. Detta kan vara besvärligt (beroende på hur ofta du använder programvaran) och kostsamt (beroende på avgiftsnivån vid den aktuella tidpunkten), men det är priset du betalar för extra säkerhet.


En annan negativ punkt kan vara sekretessen. När du involverar en annan person i konfigurationen får han eller hon kännedom om alla dina adresser och kan därför övervaka din aktivitet. Detta är dock inget problem om du väljer en förstärkt backup eller en successionsplan där din arvinge inte har någon omedelbar kännedom om Wallet:ans detaljer.


## Förberedelser


I den här handledningen ska vi upprätta en successionsplan. Vi kommer att använda :




- En Ledger Nano S Plus, för vardagliga utgifter;


https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4


- En Blockstream Jade som används för att återkräva medel;


https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3


- Två lagringsmedia (USB-minnen) för att lagra Wallet-descriptorn;
- Ett successionsbrev som innehåller instruktioner för att återkräva medlen;
- En numrerad förseglad påse, för att säkerställa att återvinningsanordningen (Jade) inte har använts.


## Installation och konfiguration


Besök den officiella Wizardsardine-webbplatsen och ladda ner Liana på https://wizardsardine.com/Liana/. Du kan också ladda ner den senaste versionen [från GitHub-arkivet] (https://github.com/wizardsardine/Liana/releases), där du kan kontrollera programvarans äkthet. Den version som används i denna handledning är 0.9.


![Télécharger Liana](assets/fr/02.webp)


För att ta reda på hur du manuellt verifierar programvarans äkthet och integritet före installationen rekommenderar vi att du läser den här handledningen :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Installera programvaran på din maskin och starta den. Välj alternativet "*Create a new Liana Wallet*" för att konfigurera din Wallet.


![Accueil Liana](assets/fr/03.webp)


Välj din Wallet-typ. Om du vill skapa en förbättrad säkerhetskopia med återställningstid kan du välja alternativet "*Bygg din egen*" och välja standardschemat. Detta kommer att fungera på ungefär samma sätt, förutom att du inte behöver behålla Hardware Wallet-återställningsfrasen.


Vi bortser här från fallet med *Expanderande Multisig*, som skapar en mer komplex konfiguration.


I den här handledningen använder vi oss av enkel nedärvning.


![Choisir type de portefeuille](assets/fr/04.webp)


En kort förklaring följer nedan.


![Rapide explication](assets/fr/05.webp)


När du har läst förklaringen kommer du att kunna ställa in nycklarna till din Liana Wallet. Detta är ett viktigt steg eftersom det avgör hur mycket du kan spendera på ditt konto.


![Configurer clés](assets/fr/06.webp)


Först och främst kan du i menyn "Advanced Settings" välja "descriptor type", dvs. det sätt på vilket Contract ska skrivas på kedjan. Du kan välja mellan två typer: P2WSH (SegWit) eller Taproot. I båda fallen kommer semantiken för utgiftsvillkoren att vara densamma. Medan P2WSH gör Contract lättare att förstå, är Taproot överlägsen eftersom den döljer oanvända villkor och sparar kostnader vid hämtning.


Detta val är frivilligt: om du är osäker, lämna standardalternativet (P2WSH i fallet med version 0.9, men detta kan komma att ändras).


![Choisir le type de descripteur](assets/fr/07.webp)


Därefter konfigurerar du din primära nyckel (*primary key*). Denna nyckel (eller snarare denna uppsättning nycklar) kommer att användas för den aktuella utgiften av medel, som inte är föremål för några tidsvillkor. Genom att klicka på "*Set*" kan du välja motsvarande *signing device*. I vårt fall har vi valt Ledger Nano S Plus Hardware Wallet.


Tillåt delning av den utökade publika nyckeln från enheten. Ge nyckeln ett meningsfullt namn (i det här fallet "Nano S+"). Observera att alla program som är installerade på enheten kommer att fortsätta att fungera normalt.


![Configurer clé principale](assets/fr/08.webp)


Därefter ställer du in återbetalningsfördröjningen, dvs. den tid efter vilken pengarna kan användas av *arvsnyckeln*. Denna fördröjning definieras i termer av block, där varje block separeras med i genomsnitt 10 minuter. Den kan variera från 10 minuter (1 block) till cirka 15 månader (65 535 block). Denna övre gräns är en begränsning av Bitcoin-protokollet, eftersom låsningstiden är kodad på 16 bitar.


Om inte särskilda omständigheter föreligger bör du välja den längsta ledtiden: 15 månader eller 65 535 block. Detta kommer att spara dig kostnader. Vi rekommenderar dock att du utför uppdateringsproceduren (som beskrivs i avsnittet "Uppdatering av Wallet") en gång om året, alltid vid samma tid på året, för att "ritualisera" denna praxis och undvika att glömma.


Här har vi ställt in en återställningstid på en timme (6 block) för att utföra våra tester.


![Configurer temps de verrouillage](assets/fr/09.webp)


Slutligen, skapa en nyckel till ditt dödsbo. Denna nyckel (eller snarare uppsättning nycklar) kommer att användas för att återfå medel om du skulle försvinna. Klicka på "*Set*", välj signeringsenhet och validera delningen av den utökade offentliga nyckeln på den.


För denna handledning har vi valt Jade. Ge nyckeln ett stämningsfullt namn (här "Jade"). Precis som med den första enheten kommer konventionella konton att fortsätta att fungera.


![Configurer clé de succession](assets/fr/10.webp)


När alla dessa åtgärder har utförts, kontrollera att allt är i sin ordning och klicka på "*Continue*" för att bekräfta dina val.


![Confirmer clés](assets/fr/11.webp)


Nästa steg är att spara din Wallet descriptor. Det här är den information du behöver för att hitta pengarna på ditt konto. Till skillnad från frasen Mnemonic tillåter inte deskriptorn dig att spendera pengar, så att avslöja den kommer bara att utgöra ett sekretessproblem (personen kommer att känna till alla dina transaktioner).


Spara två kopior av deskriptorn på elektroniska medier, t.ex. USB-minnen. Se till att du också skriver ut två kopior på papper, så att du kan komma åt dem om det elektroniska mediet skulle skadas. Varje säkerhetskopia måste vara kopplad till en signeringsenhet.


![Sauvegarder descripteur](assets/fr/12.webp)


Vår deskriptor (som analyseras i slutet av handledningen) är som följer:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


Det sista steget i den inledande Wallet-konfigurationen är att verifiera deskriptorn i var och en av de hårdvaruplånböcker som fungerar som signaturenheter.


![Enregistrer descripteur](assets/fr/13.webp)


Gör samma sak för varje signeringsenhet. Du måste kontrollera och bekräfta att deskriptorn har lagts till i varje Hardware Wallet.


![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)


Din Wallet-information är nu registrerad och det enda som återstår är att konfigurera hur du vill ansluta till Bitcoin-nätverket. Du kan välja att använda din egen nod (lokal eller fjärrstyrd) eller använda WizardSardines infrastruktur. I det senare fallet måste du länka ett Address-e-postmeddelande till din Wallet, vilket gör att du kan hämta deskriptorn. WizardSardine kommer att ha tillgång till alla dina transaktioner. Det första alternativet föreslås därför.


![Sélectionner connexion réseau](assets/fr/15.webp)


Vi har valt att använda vår egen nod. Du kan använda en befintlig nod eller installera en *pruned node* på din maskin. Om du inte har tillgång till någon annan nod, installera din egen nod på din maskin, vilket bör ta lite tid (i storleksordningen flera dagar).


![Choisir type de nœud](assets/fr/16.webp)


För denna handledning har vi använt en befintlig (offentlig) Electrum-server. Men var försiktig! Den hade tillgång till all vår aktivitet med Liana Wallet. Så använd din egen nod om du vill skydda din integritet.


![Connexion serveur Electrum public](assets/fr/17.webp)


När nodkonfigurationen är klar öppnas huvudskärmen och visar din nyss skapade Liana Wallet.


Passa på att förvara återvinningsenheten på ett säkert ställe. Den bör förvaras på en strategisk plats, så att den kan hittas av dina arvingar om du skulle avlida.


För extra säkerhet kan du lägga de komponenter som används för återställning i en förseglad påse (*tamper-evident bag*) och skriva ner serienumret någonstans. På så sätt försäkrar du dig om att ingen har kommit åt den och att din enhet fortfarande är giltig.


I vårt exempel har vi monterat följande Elements:




- Blockstream Jade som signaturenhet för dödsboet;
- En USB-kabel för anslutning och laddning av enheten;
- En pappersbackup av meningen i händelse av funktionsfel eller skada på enheten (observera att mediet också kan vara av metall och därför skyddat från Elements, som t.ex. är fallet med Cryptosteel-kapslar);
- USB-nyckeln som innehåller Wallet-descriptorn ;
- En pappersbackup av descriptorn, i händelse av fel eller skada på USB-minnet (denna backup har inte fotograferats här);
- Ett successionsbrev som beskriver de åtgärder som ska vidtas för att återfå medlen.


![Éléments de récupération](assets/fr/18.webp)


Och vi lägger dessa föremål under Seal!


![Sachet scellé récupération](assets/fr/19.webp)


## Mottagande av medel


Liana:s huvudskärm visar ditt saldo och de transaktioner (tidigare och aktuella) som är kopplade till din Wallet. I vårt fall är saldot noll, vilket är normalt.


![Écran principal](assets/fr/20.webp)


För att ta emot pengar, gå till fliken "*Receive*" och klicka på "*generate Address*". En ny Address ska visas på din skärm. Den är längre än i vanliga plånböcker: det är en Address som är kopplad till en fristående Contract (P2WSH eller Taproot).


![Générer nouvelle adresse](assets/fr/21.webp)


Du måste verifiera denna Address på din Hardware Wallet genom att klicka på "*Verifiera på hårdvaruenhet*".


![Vérifier adresse portefeuille matériel](assets/fr/22.webp)


När pengarna har skickats visas transaktionen på huvudskärmen (först som obekräftad, sedan som bekräftad). Här har vi skickat 50 000 satoshis (drygt 50 dollar vid överföringstillfället) för det här testet. Det säger sig självt att det belopp som överförs i ditt fall måste vara en storleksordning högre än detta värde på grund av transaktionsavgifter.


![Vérifier solde](assets/fr/23.webp)


Du kan kontrollera utgångsstatus för dina medel genom att gå till fliken "*Coins*". Den här fliken visar de olika mynten (UTXO) i din Wallet. Här kan vi se att det 50 000 satoshis-mynt som skapades av vår transaktion löper ut samma dag (en timmes tid).


![Obtenir informations pièce](assets/fr/24.webp)


För att bättre förstå UTXO:s representationsmodell som används i Bitcoin kan du läsa den första delen av kursen om sekretess i Bitcoin skriven av Loïc Morel :


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Löpande utgifter


Löpande utgifter är den normala situationen för att använda Liana. Att skicka bitcoins med huvudnyckeln fungerar som i alla klassiska Bitcoin-plånböcker som Electrum eller Sparrow.


För att göra en debitering går du till fliken "*Send*" och anger den viktigaste informationen: mottagarens BTC Address, beloppet som ska skickas och önskad debiteringssats. En beskrivning (som sparas lokalt) kan också läggas till för din personliga bekvämlighet. I vårt exempel skickade vi 10 000 satoshis till en viss Bob, för en debiteringsgrad på 4 sat/ov, eller 0,67 USD vid transaktionstillfället.


Liana erbjuder också "myntkontroll": du anger vilket mynt (UTXO) du vill spendera. Här har vi valt det tidigare skapade myntet på 50 000 satoshis.


![Envoyer fonds clé principale](assets/fr/25.webp)


Signera sedan transaktionen med din signaturenhet som är kopplad till huvudnyckeln genom att klicka på "*Signera*". Du måste verifiera och bekräfta transaktionen på din Hardware Wallet. Här har vi använt Nano S Plus för att signera transaktionen.


![Signer transaction clé principale](assets/fr/26.webp)


Slutligen sänder du transaktionen över nätverket genom att klicka på "*Broadcast*". Observera att om du skickar pengar återställs återhämtningstiden för använda mynt.


![Diffuser transaction clé principale](assets/fr/27.webp)


Transaktionen kommer att visas på huvudskärmen och ditt saldo kommer att uppdateras.


![Solde après dépense](assets/fr/28.webp)


## Uppdatering av portföljen


Som förklarats ovan kräver Liana Wallet att du uppdaterar dina medel regelbundet genom att utföra en transaktion på Blockchain. Om du inte gör det kan dina medel återställas av din arvinge (eller av din andra enhet om det gäller en förbättrad säkerhetskopia). Den här situationen är inte extremt farlig, men den motverkar syftet med att inrätta den här mekanismen: att behålla kontrollen över dina bitcoins utan att behöva vända dig till en betrodd tredje part, samtidigt som du drar nytta av ett skyddsnät.


En varning visas innan dina medel (eller en del av dem) löper ut och kan spenderas med återställningsnyckeln. Det kommer att indikera att din "återhämtningsväg" (*återhämtningsväg*) snart kommer att vara tillgänglig. Med tanke på den korta återhämtningstiden (en timme) visas detta meddelande direkt i vårt fall.


![Avertissement chemin récupération](assets/fr/29.webp)


När tidsfristen närmar sig kommer en knapp att visas som uppmanar dig att uppdatera de berörda medlen.


![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)


För att uppdatera dina mynt går du till fliken "*Mynt*" och klickar på "*Aktualisera mynt*" i motsvarande myntruta. Om du har flera mynt bör du uppdatera dem ett i taget och med relativt korta intervall, av sekretesskäl. För att hålla kostnaderna nere kan du konsolidera dina medel genom att skicka hela Wallet till en ny mottagande Address, men detta kommer att påverka din sekretess.


![Actualiser pièce](assets/fr/31.webp)


Ange önskad avgiftssats för transaktionen. Eftersom det här är en överföring till dig själv kan du ställa in en ganska låg avgiftssats, särskilt om du gör det flera dagar före utgången.


![Transfert à soi-même](assets/fr/32.webp)


Transaktionen (märkt "*self-transfer*") kommer endast att vara synlig på fliken "*Transactions*".


![Transactions après auto-transfert](assets/fr/33.webp)


När det har bekräftats är ditt mynt säkert! Du kan vila lugnt fram till nästa utgångsdatum.


## Bitcoin återvinning


När du återställer medel från Liana Wallet kan du ställas inför en av två situationer. Du kanske har tillgång till den dator där programvaran är installerad, och i så fall behöver du bara öppna den (vilket kommer att ske när det gäller den förbättrade säkerhetskopieringsmodellen). Men du kanske inte har tillgång till den här datorn, så vi börjar från början här. Observera att återställningsproceduren är densamma i båda fallen.


För att komma igång, ladda ner Liana från [den officiella Wizardsardine-webbplatsen](https://wizardsardine.com/Liana/), eller från [GitHub-arkivet](https://github.com/wizardsardine/Liana/releases), där du kan kontrollera programvarans äkthet. Installera programvaran och kör den. Den version som används i vårt fall är 0.9, så det visuella kan ha ändrats. På välkomstskärmen väljer du alternativet "Add an existing Liana Wallet" (Lägg till en befintlig Liana Wallet).


![Ajouter portefeuille existant](assets/fr/34.webp)


Konfigurera hur du vill ansluta till nätverket. Du kan välja att använda din egen nod (lokal eller fjärrstyrd) eller använda WizardSardines infrastruktur. I det senare fallet behöver du e-postadressen Address som används av Wallet-skaparen, så att fonderna kan lokaliseras automatiskt. Om du inte har den här informationen väljer du det första alternativet.


![Sélectionner connexion réseau](assets/fr/35.webp)


Om du använder din egen nod importerar du Wallet-descriptorn. Det här är en teknisk beskrivning av kontot som gör att du kan hämta ut de medel som finns på det. I vårt fall är det följande information:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


![Importer descripteur](assets/fr/36.webp)


Liana ber dig sedan att ange en Mnemonic-fras. Om du har en fungerande signaturenhet (Hardware Wallet) hoppar du över den här delen. Om din enhet saknas eller är skadad, men du har motsvarande 12 eller 24 ord, kan du fortfarande använda det här alternativet. För att vara på den säkra sidan (om beloppet som ska återställas är högt) föreslår vi ändå att du skaffar en ny Hardware Wallet och använder Mnemonic för att återställa nycklarna på den.


I vårt fall använder vi Blockstream Jade Hardware Wallet som en återställningsenhet och väljer att hoppa över ("*Skip*") detta steg.


![Passer phrase mnémotechnique](assets/fr/37.webp)


Kontrollera och spara descriptorn i din signeringsenhet genom att välja den på skärmen. Om din Hardware Wallet inte visas, kontrollera att den är ansluten och upplåst. Kontrollera och bekräfta att denna information har lagts till i din enhet.


![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)


Konfigurera din nod. Du kan använda en befintlig nod eller installera en *pruned node* på din maskin. I vårt fall har vi använt en befintlig nod.


![Choisir type de nœud](assets/fr/39.webp)


För denna handledning använde vi en offentlig Electrum-server. Den hade dock tillgång till all vår aktivitet med Liana Wallet. Om du vill skydda din integritet är det bättre att du använder din egen nod.


![Connexion serveur Electrum public](assets/fr/17.webp)


När du har konfigurerat din nod kommer du till huvudskärmen i Wallet, där du kan se saldot och tidigare transaktioner som är kopplade till kontot. Du kan även se om det går att hämta ut pengar. Här ser vi att ett mynt kan hämtas.


![Accueil Liana récupération](assets/fr/40.webp)


För att återfå pengarna i Wallet, gå till Inställningar ("*Inställningar*") längst ned till vänster och klicka på "*Återvinning*".


![Récupération dans paramètres](assets/fr/41.webp)


Spendera myntet i Wallet genom att kryssa i lämplig ruta. Ange den BTC Address som du vill skicka pengarna till, samt transaktionsavgiftssatsen. Klicka sedan på "*Nästa*".


![Récupération des pièces](assets/fr/42.webp)


Signera transaktionen genom att klicka på "*Signera*" och validera transaktionen på din Hardware Wallet.


![Signer transaction clé de récupération](assets/fr/43.webp)


Sänd den sedan över nätverket genom att klicka på "*Broadcast*".


![Diffuser transaction clé de récupération](assets/fr/44.webp)


Transaktionen bör visas på huvudskärmen. När den har bekräftats är återställningen klar!


![Écran principal après récupération](assets/fr/45.webp)


## Bonus: analys av deskriptorer


Deskriptorn är en mänskligt läsbar teckensträng som uttömmande beskriver en uppsättning adresser. Den kombinerar ett antal väsentliga delar av information för att hämta delar (UTXO) av en avancerad Wallet. Sättet som deskriptorn skrivs på är baserat på [Miniscript syntax] (https://bitbox.swiss/blog/understanding-Bitcoin-miniscript-part-2/), det skriptspråk som utvecklades av Andrew Poelstra, Pieter Wuille och Sanket Kanjalkar 2019.


För att bättre förstå varför denna teckensträng är viktig, låt oss analysera deskriptorn i vårt exempel, som är :


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


Följande information kan utläsas ur denna deskriptor:




- `wsh` (förkortning för *vittnesmanus Hash*): Detta är den typ av transaktionsutdata som skapas. Om vi hade valt att använda Taproot skulle identifieraren ha varit `tr`.
- `eller_d`: Detta är en logisk operator som anger att *ett av följande två* villkor måste vara uppfyllda för att utlägget ska godkännas (`_d` anger en särskild syntax).
- `pk` (förkortning för *public key*): Denna operator kontrollerar en given signatur mot följande offentliga nyckel och ger svaret som ett booleskt värde (TRUE eller FALSE).
- `[3689a8e7/48'/0'/0'/2']`: Detta element innehåller *fingeravtrycket* av huvudnyckeln för den huvudsakliga Hardware Wallet (i detta fall Nano S Plus) och härledningsvägen till den länkade utökade privata nyckeln (från vilken alla andra privata nycklar härleds).
- `xpub6FKY ... WQa`: Detta är den utökade publika nyckeln som är kopplad till huvud-Hardware Wallet (här Nano S Plus)
- `/<0;1>/*`: Detta är härledningsvägarna för att erhålla enkla nycklar och adresser: `0` för mottagning, `1` för interna operationer (*ändring*), med ett "jokertecken" (`*`) som möjliggör sekventiell härledning av flera adresser på ett konfigurerbart sätt, liknande "gap limit"-hanteringen i klassisk Wallet-programvara.
- och_v`: Detta är en logisk operator som anger att *följande två* villkor måste vara uppfyllda för att utlägget ska accepteras (`_v` anger en viss syntax).
- `v:pkh` (förkortning för *verifiera: offentlig nyckel Hash*): Denna operator verifierar en given signatur och publik nyckel mot den publika nyckeln Hash (*Hash*) som följer. Detta är i princip samma kontroll som för P2PKH- och P2WPKH-skript.
- `[42e629dd/48'/0'/0'/2']`: Detta är samma element som ovan (bestående av spårningen och härledningsvägen), förutom att spårningen av huvudnyckeln för hårdvaruåterställningen Wallet (i detta fall Jade) anges.
- `xpub6DpQ ... WQd`: Detta är den utökade publika nyckeln som är kopplad till hårdvaruåterställningen Wallet (här Jade).
- `older(6)` : Denna operator kontrollerar att den transaktionsutskrift som skapas måste ha en ålder som är strikt större än 6 block för att kunna användas.


Den sista dataposten (`8alrve5h`) är deskriptorns kontrollsumma och motsvarar Wallet-identifieraren.


De skript som skapas av denna Wallet kommer att ha följande form:


```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```


Eftersom säkerheten för din Bitcoin Wallet också beror på din förståelse för hur den fungerar, föreslår jag att du studerar mekanismerna för deterministiska och hierarkiska plånböcker på djupet genom att gå den här kostnadsfria kursen om Plan ₿ Network :


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f