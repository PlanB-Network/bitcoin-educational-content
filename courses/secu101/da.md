---
name: Informationssikkerhed og databehandling
goal: Opdater adgangskode- og persondatahåndtering. Opret en sikkerhedskopi, beskyt mod hackere og øg bevidstheden om masseovervågning.
objectives:
  - Opdatering af persondatahåndtering og værktøjer, der forbedrer din sikkerhed.
  - Implementering af en sikker og brugervenlig adgangskodeadministrator.
  - Implementering af to-faktor-godkendelse for at styrke sikkerheden og minimere risikoen for hacking.
---

# En rejse mod beskyttelse af dine data

Velkommen alle sammen til dette uddannelsesprogram dedikeret til digital sikkerhed. Denne træning er designet til at være tilgængelig for alle, så der kræves ingen forudgående viden om datalogi. Vores primære mål er at give dig den viden og de færdigheder, der er nødvendige for at navigere i den digitale verden mere sikkert og privat.

Dette vil involvere implementeringen af flere værktøjer såsom en sikker e-mail-tjeneste, et værktøj til bedre håndtering af dine adgangskoder og forskellige software til sikring af dine onlineaktiviteter.

I denne træning sigter vi ikke mod at gøre dig til ekspert, anonym eller uigennemtrængelig, da dette er umuligt. I stedet tilbyder vi dig nogle enkle og tilgængelige løsninger for at begynde at ændre dine onlinevaner og genvinde kontrollen over din digitale suverænitet.

Bidragyderhold:
Muriel; design
Rogzy Noury & Fabian; produktion
Théo; bidrag

+++

# Introduktion

## Kursusintroduktion

![introduktion](https://youtu.be/DqLf72XBJUg)

### Mål: Opdater dine sikkerhedsfærdigheder!

Velkommen alle sammen til dette uddannelsesprogram dedikeret til digital sikkerhed. Denne træning er designet til at være tilgængelig for alle, så der kræves ingen forudgående viden om datalogi. Vores primære mål er at give dig den viden og de færdigheder, der er nødvendige for at navigere i den digitale verden mere sikkert og privat.

Dette vil involvere implementeringen af flere værktøjer såsom en sikker e-mail-tjeneste, et værktøj til bedre håndtering af dine adgangskoder og forskellige software til sikring af dine onlineaktiviteter.

Denne træning er et fælles projekt mellem tre af vores professorer:

- Renaud Lifchitz, cybersikkerhedsekspert
- Théo Pantamis, ph.d. i anvendt matematik
- Rogzy, CEO for DécouvreBitcoin

Din digitale hygiejne er afgørende i en stadig mere digital verden. På trods af den konstante stigning i hacking og masseovervågning er det ikke for sent at tage det første skridt og beskytte dig selv.
I denne træning sigter vi ikke mod at gøre dig til ekspert, anonym eller uigennemtrængelig, da dette er umuligt. I stedet tilbyder vi dig nogle enkle og tilgængelige løsninger, som alle kan begynde at ændre dine onlinevaner og genvinde kontrollen over din digitale suverænitet.
Hvis du leder efter mere avancerede færdigheder inden for emnet, er vores ressourcer, tutorials eller andre cybersikkerhedstræninger her for dig. I mellemtiden får du her en kort oversigt over vores program for de næste par timer sammen.

### Sektion 1: Alt hvad du behøver at vide om online browsing

- Kapitel 1 - Online browsing
- Kapitel 2 - Brug af internettet sikkert

For at starte vil vi diskutere vigtigheden af at vælge en webbrowser og dens betydning for sikkerheden. Derefter vil vi udforske specifikationerne ved browsere, især med hensyn til cookiehåndtering. Vi vil også se, hvordan man sikrer en mere sikker og anonym browsingoplevelse ved hjælp af værktøjer som TOR. Derefter vil vi fokusere på brugen af VPN'er til at forbedre beskyttelsen af dine data. Til sidst vil vi afslutte med anbefalinger til sikker brug af WiFi-forbindelser.

### Sektion 2: Bedste praksis for computerbrug

- Kapitel 3 - Computerbrug
- Kapitel 4 - Hacking og backuphåndtering
I denne sektion vil vi dække tre nøgleområder inden for computer sikkerhed. Først vil vi udforske forskellige operativsystemer: Mac, PC og Linux og fremhæve deres specifikke egenskaber og styrker. Derefter vil vi dykke ned i metoder til effektivt at beskytte mod hacking forsøg og styrke sikkerheden på dine enheder. Til sidst vil vi understrege vigtigheden af regelmæssigt at beskytte og sikkerhedskopiere dine data for at forhindre tab eller ransomware.
### Sektion 3: Implementering af løsninger

- Kapitel 6 - Håndtering af e-mails
- Kapitel 7 - Adgangskodehåndtering
- Kapitel 8 - To-faktor autentifikation

I denne praktiske tredje sektion vil vi gå videre til implementeringen af dine konkrete løsninger.

Først vil vi se, hvordan du beskytter din e-mail-indbakke, som er afgørende for dine kommunikationer og ofte er mål for hackere. Derefter vil vi introducere dig til en adgangskodehåndterer: en praktisk løsning til ikke længere at glemme eller blande dine adgangskoder, samtidig med at de holdes sikre. Til sidst vil vi diskutere en ekstra sikkerhedsforanstaltning, to-faktor autentifikation, som tilføjer et ekstra lag af beskyttelse til dine konti. Alt vil blive forklaret klart og tilgængeligt.

### Bonussektion: Interview med Pantamis og Renaud

# Alt hvad du behøver at vide om online browsing

## 1. Online browsing

![online browsing](https://youtu.be/BEK7vGnkO64)

Når du browser på internettet, er det vigtigt at undgå visse almindelige fejl for at bevare din online sikkerhed. Her er nogle tips til at undgå dem:

### Vær forsigtig med software downloads:

Det anbefales at downloade software fra udgiverens officielle hjemmeside i stedet for generiske sider.
Eksempel: Brug www.signal/download i stedet for www.logicieltelechargement.fr/signal.

Det er også tilrådeligt at prioritere open-source software, da de ofte er sikrere og fri for skadelig software. Open-source software er software, hvis kildekode er kendt og tilgængelig for alle. Dette tillader verifikation, blandt andet for at sikre, at der ikke er skjult adgang til at stjæle dine personlige data.

> Bonus: Open-source software er ofte gratis! Dette universitet er 100% open source, så du kan også tjekke vores kode på vores GitHub.

### Håndtering af cookies: Fejl og bedste praksis

Cookies er filer, der oprettes af hjemmesider for at gemme information på din enhed. Mens nogle sider kræver disse cookies for at fungere korrekt, kan de også udnyttes af tredjeparts sider, især til reklame sporing. I overensstemmelse med regulativer som GDPR er det muligt - og anbefalet - at afvise tredjeparts sporende cookies, samtidig med at man accepterer dem, der er nødvendige for hjemmesidens korrekte funktion. Efter hvert besøg på en hjemmeside er det klogt at slette de tilknyttede cookies, enten manuelt eller gennem en udvidelse eller et specifikt program. Nogle browsere tilbyder endda muligheden for selektivt at slette cookies. På trods af disse forholdsregler er det afgørende at forstå, at informationen indsamlet af forskellige sider kan forblive forbundet, derfor er det vigtigt at finde en balance mellem bekvemmelighed og sikkerhed.

> Bemærk: Begræns også antallet af udvidelser installeret i din browser for at undgå potentielle sikkerheds- og ydelsesproblemer.

### Webbrowsere: valg, sikkerhed

Der er to store familier af browsere: dem baseret på Chrome og dem baseret på Firefox.
Selvom begge familier tilbyder et lignende niveau af sikkerhed, anbefales det at undgå Google Chrome-browseren på grund af dens trackere. Lettere alternativer til Chrome, som f.eks. Chromium eller Brave, kan foretrækkes. Brave anbefales især for sin indbyggede reklameblokerer. Det kan være nødvendigt at bruge flere browsere for at få adgang til visse hjemmesider.

### Privat browsing, TOR og andre alternativer til mere sikker og anonym browsing
Privat browsing, selvom det ikke skjuler browsing fra din internetudbyder, giver dig mulighed for ikke at efterlade lokale spor på din computer. Cookies slettes automatisk ved afslutningen af hver session, hvilket giver dig mulighed for at acceptere alle cookies uden at blive sporet. Privat browsing kan være nyttigt, når du køber online-tjenester, da hjemmesider sporer vores søgevaner og justerer priserne derefter. Det er dog vigtigt at bemærke, at privat browsing anbefales til midlertidige og specifikke sessioner, ikke til generel internetbrowsing.
Et mere avanceret alternativ er TOR (The Onion Router) netværket, som tilbyder anonymitet ved at skjule brugerens IP-adresse og tillade adgang til Darknet. TOR Browser er en browser specielt designet til at bruge TOR-netværket. Den giver dig mulighed for at besøge både konventionelle hjemmesider og .onion-hjemmesider, som typisk drives af enkeltpersoner og kan være af ulovlig karakter.

TOR er lovligt og bruges af journalister, frihedsaktivister og andre, der ønsker at undgå censur i autoritære lande. Det er dog vigtigt at forstå, at TOR ikke sikrer de besøgte hjemmesider eller computeren selv. Derudover kan brug af TOR sænke internetforbindelsen, da data passerer gennem tre andre personers computere, før det når sin destination. Det er også vigtigt at bemærke, at TOR ikke er en narresikker løsning, der garanterer 100% anonymitet, og det bør ikke bruges til ulovlige aktiviteter.

### BRAVE

**_Tutorial under construction, to contribute or add it, you can go through GitHub_**

## 2. VPN og internetforbindelse

![vpn and internet connection](https://youtu.be/oRO7sGexvzo)

### VPN'er

Beskyttelse af din internetforbindelse er en afgørende del af online-sikkerhed, og brug af virtuelle private netværk (VPN'er) er en effektiv metode til at forbedre denne sikkerhed, både for virksomheder og individuelle brugere.

"VPN'er er værktøjer, der krypterer data, der sendes over internettet, hvilket gør forbindelsen mere sikker. I en professionel sammenhæng giver VPN'er medarbejdere mulighed for sikkert at få adgang til virksomhedens interne netværk eksternt. De udvekslede data er krypteret, hvilket gør det meget sværere for tredjeparter at opsnappe dem. Ud over at sikre adgangen til et internt netværk kan brug af en VPN tillade en bruger at rute deres internetforbindelse gennem virksomhedens interne netværk og dermed give indtryk af, at deres forbindelse kommer fra virksomheden. Dette kan være særligt nyttigt for at få adgang til online-tjenester, der er geografisk begrænsede.

### Typer af VPN'er

Der er to hovedtyper af VPN'er: virksomheds-VPN'er og forbruger-VPN'er, som f.eks. NordVPN. Virksomheds-VPN'er er normalt dyrere og mere komplekse, mens forbruger-VPN'er generelt er mere tilgængelige og brugervenlige. For eksempel giver NordVPN brugere mulighed for at oprette forbindelse til internettet gennem en server placeret i et andet land, hvilket kan omgå geografiske begrænsninger.

Brug af en forbruger-VPN garanterer dog ikke fuldstændig anonymitet. Mange VPN-udbydere opbevarer oplysninger om deres brugere, hvilket potentielt kan kompromittere deres anonymitet. Selvom VPN'er kan være nyttige til at forbedre online-sikkerheden, er de ikke en universel løsning. De er effektive til visse specifikke formål, såsom at få adgang til geografisk begrænsede tjenester eller forbedre sikkerheden under rejser, men de garanterer ikke total sikkerhed. Når du vælger en VPN, er det vigtigt at prioritere pålidelighed og teknisk ekspertise frem for popularitet. VPN-udbydere, der indsamler færrest personlige oplysninger, er generelt de sikreste. Tjenester som iVPN og Mullvad indsamler ikke personlige oplysninger og tillader endda betaling med Bitcoin for øget privatliv.
Endelig kan en VPN også bruges til at blokere online reklamer og give en mere behagelig og sikker browsingoplevelse. Det er dog vigtigt at lave sin egen research for at finde den VPN, der bedst passer til ens specifikke behov. Det anbefales at bruge en VPN for at forbedre sikkerheden, selv når man browser på internettet derhjemme. Dette hjælper med at sikre et højere niveau af sikkerhed for udvekslet data online. Sørg også for at kontrollere URL'er og den lille hængelås i adresselinjen for at bekræfte, at du er på den side, du har til hensigt at besøge.
### HTTPS og offentlige Wi-Fi-netværk

Når det kommer til online sikkerhed, er det vigtigt at forstå, at 4G generelt er mere sikkert end offentlige Wi-Fi-netværk. Dog kan brugen af 4G hurtigt opbruge din mobildata. HTTPS-protokollen er blevet standarden for at kryptere data på hjemmesider. Den sikrer, at data, der udveksles mellem brugeren og hjemmesiden, er sikker. Det er derfor afgørende at verificere, at den side, du besøger, bruger HTTPS-protokollen.

I Den Europæiske Union reguleres databeskyttelse af den Generelle Databeskyttelsesforordning (GDPR). Det er derfor sikrere at bruge europæiske Wi-Fi-adgangspunktsudbydere, såsom SNCF, der ikke videresælger brugerens forbindelsesdata. Dog garanterer det blot, at en side viser en hængelås, ikke dens autenticitet. Det er vigtigt at verificere sidens offentlige nøgle ved hjælp af et certifikatsystem for at bekræfte dens autenticitet. Selvom datakryptering forhindrer tredjeparter i at opsnappe udvekslede data, er det stadig muligt for en ondsindet person at udgive sig som siden og overføre data i klartekst.

For at undgå online svindel er det afgørende at verificere identiteten af den side, du browser på, især ved at kontrollere udvidelsen og domænenavnet. Vær også opmærksom på svindlere, der bruger lignende bogstaver i URL'er for at narre brugere.

Sammenfattende kan brugen af en VPN markant forbedre online sikkerhed, både for virksomheder og individuelle brugere. Desuden kan gode browsingvaner bidrage til bedre digital hygiejne. I næste del af denne kursus vil vi adressere computer sikkerhed, herunder opdateringer, antivirus og adgangskodehåndtering.

### Vejledning: IVPN

**_Vejledning under konstruktion, for at bidrage eller tilføje den, kan du gå gennem GitHub_**

# Bedste praksis for computerbrug

## Computerbrug

![computerbrug](https://youtu.be/lzJr5CIulSU)

Sikkerheden på vores computere er en stor bekymring i dagens digitale verden. I dag vil vi adressere tre nøglepunkter:

- Valg af computer
- Opdateringer og antivirus til optimal sikkerhed
- Bedste praksis for sikkerhed af din computer og data.

### Valg af computer og operativsystem

Hvad angår valg af computer, er der ingen væsentlig forskel i sikkerhed mellem gamle og nye computere. Dog er der sikkerhedsforskelle mellem operativsystemer: Windows, Linux og Mac.
Hvad angår Windows, anbefales det ikke at bruge en administrator-konto til daglig brug, men derimod at oprette to separate konti: en administrator-konto og en konto til daglig brug. Windows er ofte mere udsat for malware på grund af det store antal brugere og nemheden ved at skifte fra bruger til administrator. På den anden side er trusler mindre almindelige på Linux og Mac.

Valget af operativsystem bør baseres på dine behov og præferencer. Linux-systemer er blevet betydeligt udviklet i de seneste år og er blevet mere og mere brugervenlige. Ubuntu er et interessant alternativ for begyndere med et brugervenligt grafisk interface. Det er muligt at partitionere en computer for at eksperimentere med Linux og samtidig beholde Windows, men dette kan være komplekst. Det er ofte at foretrække at have en dedikeret computer, en virtuel maskine eller en USB-nøgle til at teste Linux eller Ubuntu.

### Softwareopdateringer

Hvad angår opdateringer er reglen simpel: **regelmæssig opdatering af operativsystemet og applikationer er afgørende.**
På Windows 10 er opdateringer næsten kontinuerlige, og det er afgørende ikke at blokere eller forsinke dem. Hvert år identificeres omkring 15.000 sårbarheder, hvilket understreger vigtigheden af at holde softwaren opdateret for at beskytte mod vira. Generelt slutter software-support mellem 3 og 5 år efter udgivelsen, så det er nødvendigt at opgradere til en nyere version for at fortsætte med at nyde godt af sikkerheden.
Reglen gælder næsten al software. Opdateringer er faktisk ikke beregnet til at gøre din maskine forældet eller langsom, men til at beskytte den mod nye trusler. Nogle opdateringer betragtes endda som store, og uden dem er din computer i alvorlig risiko for udnyttelse.

For at give dig et konkret eksempel på en fejl: sprækket software, der ikke kan opdateres, udgør en dobbelt potentiel trussel. Ankomsten af en virus under den ulovlige download fra et mistænkeligt websted og en usikker brug mod nye former for angreb.

### Antivirus

- Har du brug for et antivirusprogram? JA
- Skal du betale? Det afhænger!

Valget og implementeringen af et antivirusprogram er vigtigt. Windows Defender, det indbyggede antivirusprogram i Windows, er en sikker og effektiv løsning. Som en gratis løsning er det ekstremt godt og meget bedre end mange gratis løsninger, der findes online. Man skal faktisk udvise forsigtighed med antivirusprogrammer, der downloades fra internettet, da de kan være ondsindede eller forældede.
For dem, der ønsker at investere i et betalt antivirusprogram, anbefales det at vælge et antivirusprogram, der intelligent analyserer ukendte og nye trusler, som f.eks. Kaspersky. Opdateringer af antivirusprogrammet er afgørende for at beskytte mod nye trusler.

> Bemærk: Linux og Mac har ofte ikke brug for antivirusprogrammer takket være deres system til adskillelse af brugerrettigheder.

Endelig er her nogle gode praksisser for sikkerheden af din computer og data. Det er vigtigt at vælge et effektivt og brugervenligt antivirusprogram. Det er også afgørende at følge gode praksisser på din computer, f.eks. ikke at indsætte ukendte eller mistænkelige USB-nøgler. Disse USB-nøgler kan indeholde ondsindede programmer, der automatisk kan starte ved indsættelse. Efterfølgende kontrol af USB-nøglen vil være nytteløs, når den først er blevet indsat. Nogle virksomheder er blevet ofre for hacking på grund af USB-nøgler, der er blevet efterladt uforsigtigt på tilgængelige områder, f.eks. en parkeringsplads.

Behandl din computer, som du ville behandle dit hjem: vær opmærksom, opdater regelmæssigt, slet unødvendige filer og brug en stærk adgangskode til sikkerhed. Det er afgørende at kryptere data på bærbare computere og smartphones for at forhindre tyveri eller datatab. BitLocker til Windows, LUKS til Linux og den indbyggede mulighed til Mac er løsninger til datakryptering. Det anbefales at aktivere datakryptering uden tøven og skrive adgangskoden ned på et stykke papir, der opbevares et sikkert sted.

Konklusionen er, at det er afgørende at vælge et operativsystem, der passer til dine behov, og regelmæssigt opdatere det samt de installerede applikationer. Det er også afgørende at bruge et effektivt og brugervenligt antivirusprogram og følge gode praksisser for sikkerheden af din computer og data.

### Vejledning: Ubuntu

**_Vejledning under udarbejdelse, for at bidrage eller tilføje den kan du gå gennem GitHub_**

## Hacking og backup-styring: Beskyttelse af dine data

![hacking og backup-styring](https://youtu.be/CJDjWPV3PeU)

### Hvordan angriber hackere?

For at beskytte dig selv godt er det vigtigt at forstå, hvordan hackere forsøger at infiltrere din computer. Vira opstår nemlig sjældent ud af ingenting, men er snarere konsekvensen af vores handlinger, selvom det er uforvarende!

Som en generel regel kommer vira, fordi du har tilladt din computer at invitere dem ind i dit hjem. Dette kan visualiseres ved at downloade mistænkelig software, en kompromitteret torrent-fil eller simpelthen ved at klikke på linket i en svigagtig e-mail!

### Phishing, vær opmærksom på svigagtige e-mails:
Opmærksomhed! E-mails er den første angrebsvektor, her er nogle tips:
- Vær opmærksom på phishing-forsøg, der sigter mod at udtrække følsomme oplysninger som dine legitimationsoplysninger og adgangskoder. Undgå at klikke på mistænkelige links og del ikke dine personlige oplysninger, uden at have verificeret afsenderens legitimitet.
- Vær forsigtig med e-mail-vedhæftede filer og billeder:
  E-mail-vedhæftede filer og billeder kan indeholde malware. Download eller åbn ikke vedhæftede filer fra ukendte eller mistænkelige afsendere, og sørg for, at dit antivirusprogram er opdateret.

Den gyldne regel her er at kontrollere afsenderens fulde navn samt e-mailens oprindelse. Hvis du er i tvivl, så slet den!

### Ransomware og typer af cyberangreb:

Ransomware er en type ondsindet software, der krypterer brugerdata og kræver en løsesum for at dekryptere det. Denne type angreb bliver stadig mere almindelig og kan være meget problematisk for en virksomhed eller enkeltperson. For at beskytte dig selv er det afgørende at oprette sikkerhedskopier af de mest følsomme filer! Dette vil ikke stoppe ransomwaren, men det vil tillade dig at ignorere den.

Lav regelmæssige sikkerhedskopier af dine vigtige data til en ekstern lagringsenhed eller en sikker online lagringstjeneste. På den måde kan du, i tilfælde af et cyberangreb eller hardwarefejl, gendanne dine data uden at miste vigtige oplysninger.

En simpel løsning:

- Køb en ekstern harddisk og kopier dine data over på den. Frakobl den og opbevar den et sikkert sted i huset. (Hvis du gør dette to gange og opbevarer en af ​​harddiskene et andet sted, hjælper det med at beskytte mod potentielle brande.)

- Opret en "cloud" sikkerhedskopi ved hjælp af ProtonMail Drive, Sync eller endda Google Drive. Upload blot dine følsomme data til denne online vært. Vær dog opmærksom på, at dine data potentielt er på internettet og opbevares af en betroet tredjepart.

### Skal du betale hackerne?

NEJ, det anbefales generelt ikke at betale hackere i tilfælde af ransomware eller andre typer angreb. Betaling af løsesum garanterer ikke gendannelse af dine data og kan opmuntre cyberkriminelle til at fortsætte deres ondsindede aktiviteter. Prioriter i stedet forebyggelse og regelmæssig sikkerhedskopiering af dine data for at beskytte dig selv.

Hvis du opdager en virus på din computer, skal du afbryde internetforbindelsen, udføre en fuld antivirus-scanning og slette inficerede filer. Opdater derefter din software og dit operativsystem og skift dine adgangskoder for at forhindre yderligere indtrængen.

# Implementering af løsninger.

## Håndtering af e-mailkonti

![e-mailkontohåndtering](https://youtu.be/WjqH882f4cY)

## Opsætning af en ny e-mailkonto!

E-mailkontoen er det centrale punkt for din online aktivitet: Hvis den bliver kompromitteret, kan en hacker bruge den til at nulstille alle dine adgangskoder via "glemt adgangskode"-funktionen og få adgang til mange andre websteder. Derfor er det vigtigt at sikre den ordentligt.

En e-mailkonto bør oprettes med en unik og stærk adgangskode (detaljer i kapitel 7) og ideelt set med et to-faktor-godkendelsessystem (detaljer i kapitel 8).

Selvom vi alle allerede har en e-mailkonto, er det vigtigt at overveje at oprette en ny, mere moderne konto for at starte forfra.

### Valg af e-mailudbyder og håndtering af e-mailadresser

Korrekt håndtering af vores e-mailadresser er afgørende for at sikre sikkerheden for vores online adgang. Det er vigtigt at vælge en sikker og privatlivsrespektfuld e-mailudbyder. For eksempel er ProtonMail en sikker og privatlivsrespektfuld e-mailtjeneste.
Når du vælger en e-mail-udbyder og opretter en adgangskode, er det vigtigt aldrig at genbruge den samme adgangskode til forskellige online-tjenester. Det anbefales at oprette nye e-mail-adresser regelmæssigt og adskille brugen ved at bruge forskellige e-mail-adresser. Det er bedst at vælge en sikker e-mail-tjeneste til vigtige konti. Det skal også bemærkes, at nogle tjenester begrænser længden af adgangskoder, så det er vigtigt at være opmærksom på denne begrænsning. Der findes også tjenester til oprettelse af midlertidige e-mail-adresser, som kan bruges til konti med begrænset varighed.
Det er vigtigt at overveje, at ældre e-mail-udbydere som La Poste, Arobase, Wig, Hotmail stadig bruges, men deres sikkerhedspraksis er måske ikke lige så god som Gmails. Derfor anbefales det at have to separate e-mail-adresser, en til generel kommunikation og en anden til gendannelse af konti, hvor sidstnævnte er bedre sikret. Det er bedst at undgå at blande e-mail-adressen med din telefonoperatør eller internetudbyder, da dette kan være en angrebsvektor.

### Skal jeg ændre min e-mail-konto?

Det anbefales at bruge hjemmesiden Have I Been Pwned (https://haveibeenpwned.com/) til at kontrollere, om vores e-mail-adresse er blevet kompromitteret, og for at få besked om fremtidige databrud. En hacket database kan udnyttes af hackere til at sende phishing-e-mails eller genbruge kompromitterede adgangskoder.
Generelt set er det ikke en dårlig praksis at begynde at bruge en ny, mere sikker e-mail-adresse, og det er endda nødvendigt, hvis man ønsker at starte på en sund basis.
Bonus Bitcoin: Det kan være en god idé at oprette en specifik e-mail-adresse til vores Bitcoin-aktiviteter (oprettelse af børserkonti) for at adskille områderne af aktivitet i vores liv.

### Vejledning: Oprettelse af ProtonMail-konto

**_Vejledning under konstruktion, for at bidrage eller tilføje den, kan du gå gennem GitHub_**

## Adgangskodeadministrator

![adgangskodeadministrator](https://youtu.be/HzLuZ6noePY)

### Hvad er en adgangskodeadministrator?

En adgangskodeadministrator er et værktøj, der giver dig mulighed for at gemme, generere og administrere dine adgangskoder til forskellige online-konti. I stedet for at huske flere adgangskoder behøver du kun én hovedadgangskode for at få adgang til alle de andre.

Med en adgangskodeadministrator behøver du ikke længere bekymre dig om at glemme dine adgangskoder eller skrive dem ned et sted. Du skal kun huske én hovedadgangskode. Derudover genererer de fleste af disse værktøjer stærke adgangskoder for dig, hvilket forbedrer sikkerheden for dine konti.

### Forskelle mellem nogle populære administratorer:

- LastPass: En af de mest populære administratorer. Det er en tredjepartstjeneste, hvilket betyder, at dine adgangskoder gemmes på deres servere. Den tilbyder en gratis version og en betalt version med en brugervenlig grænseflade.

- Dashlane: Det er også en tredjepartstjeneste med en intuitiv grænseflade og ekstra funktioner som sporing af kreditkortoplysninger og sikre noter.

### Selvhosting for mere kontrol:

- Bitwarden: Det er et open-source-værktøj, hvilket betyder, at du kan gennemgå koden for at verificere sikkerheden. Selvom Bitwarden tilbyder en hostet service, giver den også brugerne mulighed for selvhosting, hvilket betyder, at du kan kontrollere, hvor dine adgangskoder gemmes, og potentielt tilbyde mere sikkerhed og kontrol.

- KeePass: Det er en open-source-løsning, der primært er beregnet til selvhosting. Dine data gemmes som standard lokalt, men du kan synkronisere adgangskodedatabasen ved hjælp af forskellige metoder, hvis du ønsker det. KeePass er bredt anerkendt for sin sikkerhed og fleksibilitet, selvom det måske er lidt mindre brugervenligt for begyndere.
Bemærk: Valget mellem en tredjepartstjeneste eller en selvhostet tjeneste afhænger af dit niveau af teknologisk komfort og hvordan du prioriterer kontrol versus bekvemmelighed. Tredjepartstjenester er generelt mere bekvemme for de fleste mennesker, mens selvhosting kræver mere teknisk viden, men kan tilbyde mere kontrol og tryghed med hensyn til sikkerhed.

### Hvad der udgør en god adgangskode:

En god adgangskode er generelt:

- Lang: mindst 12 tegn.
- Kompleks: en blanding af store og små bogstaver, tal og symboler.
- Unik: brug ikke den samme adgangskode til forskellige konti.
- Ikke baseret på personlig information: undgå fødselsdatoer, navne osv.

For at sikre sikkerheden af din konto er det afgørende at oprette stærke og sikre adgangskoder. Længden på adgangskoden er ikke nok til at sikre dens sikkerhed. Tegnene skal være helt tilfældige for at modstå brute force-angreb. Uafhængigheden af begivenheder er også vigtig for at undgå de mest sandsynlige kombinationer. Almindelige adgangskoder som "password" er lette at kompromittere.

For at oprette en stærk adgangskode anbefales det at bruge et stort antal tilfældige tegn uden at bruge forudsigelige ord eller mønstre. Det er også vigtigt at inkludere tal og specialtegn. Det skal dog bemærkes, at nogle hjemmesider kan begrænse brugen af visse specialtegn. Adgangskoder, der ikke er tilfældigt genereret, er nemme at gætte. Variationer eller tilføjelser til adgangskoder er ikke sikre. Hjemmesider kan ikke garantere sikkerheden af adgangskoder, der er valgt af brugerne.

Tilfældigt genererede adgangskoder tilbyder et højere niveau af sikkerhed, selvom de kan være sværere at huske. Adgangskodehåndteringsprogrammer kan generere mere sikre tilfældige adgangskoder. Ved at bruge en adgangskodehåndteringsprogram behøver du ikke at huske alle dine adgangskoder. Det er vigtigt gradvist at erstatte dine gamle adgangskoder med dem, der er genereret af programmet, da de er stærkere og længere. Sørg for, at hovedadgangskoden til din adgangskodehåndteringsprogram også er stærk og sikker.

### Vejledning: Oprettelse af en hovedadgangskode

**_Vejledning under konstruktion, for at bidrage eller tilføje den, kan du gå gennem GitHub_**

### Vejledning: BitWarden

**_Vejledning under konstruktion, for at bidrage eller tilføje den, kan du gå gennem GitHub_**

### Vejledning: KeePass

**_Vejledning under konstruktion, for at bidrage eller tilføje den, kan du gå gennem GitHub_**

## To-faktor-godkendelse

![2FA](https://youtu.be/863n4N1XNjk)

### Hvorfor implementere 2FA

To-faktor-godkendelse (2FA) er et ekstra lag af sikkerhed, der bruges til at sikre, at de personer, der forsøger at få adgang til en online konto, er dem, de hævder at være. I stedet for kun at indtaste et brugernavn og en adgangskode kræver 2FA en anden form for verifikation.

Dette andet trin kan være:

- En midlertidig kode, der sendes via SMS.
- En kode genereret af en applikation som Google Authenticator eller Authy.
- En fysisk sikkerhedsnøgle, som du indsætter i din computer.

Med 2FA vil en hacker, selvom de får fat i din adgangskode, ikke kunne få adgang til din konto uden denne anden verifikationsfaktor. Dette gør 2FA essentiel for at beskytte dine online konti mod uautoriseret adgang.

### Hvilken mulighed skal du vælge?

De forskellige muligheder for stærk godkendelse tilbyder varierende niveauer af sikkerhed.

- SMS betragtes ikke som den bedste mulighed, da den kun giver bevis for ejerskab af et telefonnummer.
- 2FA (to-faktor-godkendelse) er mere sikker, da den bruger flere typer beviser, såsom viden, ejerskab og identifikation. Engangskoder (HOTP og TOTP) er sikrere end SMS, fordi de kræver kryptografisk beregning og gemmes lokalt i stedet for i hukommelsen.
- Hardwaretokens som USB-nøgler eller smartcards tilbyder optimal sikkerhed ved at generere en unik privat nøgle til hver side og verificere URL'en, før forbindelsen tillades.
For optimal sikkerhed med stærk godkendelse anbefales det at bruge en sikker e-mail-adresse, en sikker adgangskodeadministrator og vedtage 2FA ved hjælp af YubiKeys. Det er også tilrådeligt at købe to YubiKeys for at være forberedt på tab eller tyveri, for eksempel ved at opbevare en sikkerhedskopi både derhjemme og på dig.

Biometri kan bruges som erstatning, men det er mindre sikkert end kombinationen af viden og besiddelse. Biometriske data bør forblive på godkendelsesenheden og ikke offentliggøres online. Det er vigtigt at overveje trusselsmodellen forbundet med forskellige godkendelsesmetoder og justere praksis derefter.

### Konklusion på træningen:

Som du har forstået, er implementering af god digital hygiejne ikke nødvendigvis enkelt, men det forbliver tilgængeligt!

- Oprettelse af en ny sikker e-mail-adresse.
- Opsætning af en adgangskodeadministrator.
- Aktivering af 2FA.
- Gradvis udskiftning af vores gamle adgangskoder med stærke adgangskoder med 2FA.

Bliv ved med at lære og implementer gradvist gode praksisser!

Gylden regel: Cybersikkerhed er et bevægeligt mål, der vil tilpasse sig din læringsrejse!

### Vejledning: 2FA og YubiKey-løsninger

**_Vejledning under konstruktion, for at bidrage eller tilføje den, kan du gå gennem GitHub._**

# Gå videre

## Sådan arbejder du inden for cybersikkerhedsbranchen

![konklusion og arbejde i branchen](https://youtu.be/YZ2EKaPvoZU)

# Cybersikkerhed: Et voksende felt med uendelige muligheder

Hvis du brænder for at beskytte systemer og data, tilbyder cybersikkerhedsbranchen et væld af muligheder. Hvis denne branche interesserer dig, er her nogle nøgletrin til at guide dig.

### Akademiske grundlag og certificeringer:

En solid uddannelse inden for datalogi, informations-systemer eller et beslægtet område er ofte det ideelle udgangspunkt. Disse studier giver det nødvendige fundament for at forstå de tekniske udfordringer inden for cybersikkerhed. For at supplere denne uddannelse er det klogt at opnå anerkendte certificeringer inden for feltet. Selvom disse certificeringer kan variere afhængigt af regionen, nyder nogle, som f.eks. CISSP eller CEH, global anerkendelse.

Cybersikkerhed er et omfattende og konstant udviklende felt. Det er afgørende at sætte sig ind i essentielle værktøjer og forskellige systemer. Derudover, med så mange underdomæner, fra hændelsesrespons til etisk hacking, er det gavnligt at finde dit speciale og specialisere dig i det.

### Opnå praktisk erfaring:

Betydningen af praktisk erfaring må ikke undervurderes. At søge praktikpladser eller juniorstillinger i virksomheder med cybersikkerhedsteams er en fremragende måde at anvende din teoretiske viden på. Desuden kan deltagelse i etiske hackingkonkurrencer eller cybersikkerhedssimulationer forfine dine færdigheder i virkelige situationer.

Styrken i et professionelt netværk er uvurderlig. Ved at deltage i professionelle foreninger, hackerspaces eller online fora får du en platform til at udveksle idéer med andre eksperter. På samme måde giver deltagelse i cybersikkerhedskonferencer og workshops dig ikke kun mulighed for at lære, men hjælper også med at opbygge forbindelser til branchefolk.

Den konstante udvikling af trusler kræver regelmæssig overvågning af nyheder og specialiserede fora. I en sektor, hvor tillid er afgørende, er det essentielt at handle med etik og integritet på alle stadier af din karriere.

### Færdigheder og værktøjer til at fordybe sig i:

- Cybersikkerhedsværktøjer: Wireshark, Metasploit, Nmap.
- Operativsystemer: Linux, Windows, MacOS.
- Programmeringssprog: Python, C, Java.
- Netværk: TCP/IP, VPN, firewall.
- Databaser: SQL, NoSQL.
- Kryptografi: SSL/TLS, symmetrisk/asymmetrisk kryptering.
- Hændelseshåndtering: Loganalyse, hændelsesrespons.
- Etisk hacking: Penetrationsteknikker, indtrængningstest.
- Governance: ISO-standarder, GDPR/CCPA-regler.

Ved at mestre disse færdigheder og værktøjer vil du være godt rustet til at navigere succesfuldt i cybersikkerhedens verden.

## Interview med Renaud

![Interview](https://youtu.be/RVjE-KOSKDs)
Effektiv passwordhåndtering og styrkelse af autentificering: En akademisk tilgang

I træningsmodulet "Sikkerhed 101" tilbudt af Découvre Bitcoin inden for Akademiet, diskuterede vi vigtigheden af password-managere. Tre dimensioner er essentielle at overveje: oprettelse, opdatering og implementering af passwords på hjemmesider.

Det anbefales generelt ikke at bruge browserudvidelser til automatisk udfyldning af passwords. Disse værktøjer kan gøre brugeren mere sårbar over for phishing-angreb. Renaud, en anerkendt ekspert inden for cybersikkerhed, foretrækker manuel håndtering ved brug af KeePass, som indebærer manuel kopiering og indsættelse af passwordet. Udvidelser har tendens til at øge angrebsfladen, kan sænke browserens ydeevne og udgøre derfor en betydelig risiko. Derfor anbefales minimal brug af udvidelser i browseren.

Password-managere opfordrer generelt til brug af yderligere autentificeringsfaktorer, såsom to-faktor autentificering. For optimal sikkerhed anbefales det at opbevare engangskoder (One-Time Passwords) på din mobile enhed. AndoTP tilbyder en open-source løsning til generering og opbevaring af engangskoder på din telefon. Mens Google Authenticator tillader eksport af autentificeringskodesæder, er tilliden til backup på en Google-konto begrænset. Derfor anbefales OTI- og AndoTP-applikationerne til autonom håndtering af engangskoder.

Spørgsmålet om digital arv og digital sorg rejser vigtigheden af at have en procedure til at videregive passwords efter en persons død. En password-manager letter denne overgang ved at sikker opbevare alle digitale hemmeligheder ét sted. Password-manageren tillader også identifikation af alle åbne konti og håndtering af deres lukning eller overførsel. Det anbefales at skrive hovedpasswordet ned på papir, men det bør opbevares på et skjult og sikkert sted. Hvis harddisken er krypteret, og computeren er låst, vil passwordet ikke være tilgængeligt, selv i tilfælde af indbrud.

Mod en post-password-æra: Udforskning af troværdige alternativer

Passwords, selvom de er udbredte, har mange ulemper, herunder muligheden for risikabel transmission under autentificeringsprocessen. Førende virksomheder som Microsoft og Apple tilbyder innovative alternativer som biometri og hardware-tokens, hvilket indikerer en progressiv tendens til at opgive passwords.

'Passkeys tilbyder f.eks. krypterede tilfældige nøgler, kombineret med en lokal faktor (biometri eller PIN), som er hostet af en udbyder, men forbliver uden for deres rækkevidde. Selvom dette kræver opdatering af hjemmesider, eliminerer tilgangen behovet for passwords og giver dermed et højt niveau af sikkerhed uden de begrænsninger, der er forbundet med traditionelle passwords eller problemet med at håndtere en digital sikkerhedsboks.

Passkiz er et andet levedygtigt og sikkert alternativ til password-håndtering. Dog er der stadig et stort spørgsmål om tilgængelighed i tilfælde af udbyderfejl. Det ville derfor være ønskeligt, at internetgiganterne foreslår systemer til at garantere denne tilgængelighed.

Direkte autentificering til den relevante service er en interessant mulighed for ikke længere at være afhængig af en tredjepart. Dog medfører Single Sign-On (SSO) tilbudt af internetgiganter også problemer med hensyn til tilgængelighed og risici for censur. For at forhindre læk af data er det afgørende at minimere mængden af information, der indsamles under autentificeringsprocessen.

Computer sikkerhed: nødvendigheden af sikre praksisser og risici forbundet med menneskelig forsømmelighed

Computer sikkerhed kan kompromitteres af simple praksisser og brugen af standard passwords som f.eks. "admin". Avancerede angreb er ikke altid nødvendige for at true computer sikkerheden. For eksempel blev administratorpasswords til en YouTube-kanal skrevet i en virksomheds private kildekode. Sikkerhedssårbarheder er ofte resultatet af menneskelig forsømmelighed.
Det skal også bemærkes, at internettet er meget centraliseret og i vid udstrækning under amerikansk kontrol. DNS-serveren kan være genstand for censur og bruger ofte vildledende DNS for at blokere adgangen til visse websteder. DNS er en gammel og utilstrækkelig sikkerhedsprotokol, hvilket kan føre til sikkerhedsproblemer. Nye protokoller som f.eks. DNSsec er dukket op, men er stadig ikke bredt anvendt. For at omgå censur og blokering af annoncer er det muligt at vælge alternative DNS-udbydere.

Alternativer til indtrængende reklamer inkluderer Google DNS, OpenDNS og andre uafhængige tjenester. Den standard DNS-protokol efterlader DNS-forespørgsler synlige for internetudbyderen. DOH (DNS over HTTPS) og DOT (DNS over TLS) krypterer DNS-forbindelsen og giver større privatliv og sikkerhed. Disse protokoller anvendes bredt i virksomheder på grund af deres forbedrede sikkerhed og understøttes naturligt af Windows, Android og iPhone. For at bruge DOH og DOT skal der indtastes et TLS-værtsnavn i stedet for en IP-adresse. Gratis DOH- og DOT-udbydere er tilgængelige online. DOH og DOT forbedrer privatliv og sikkerhed ved at undgå "man in the middle"-angreb. Andre vigtige overvejelser

Som en del af træningsmodulet "Sikkerhed 101" på Découvre Bitcoin Academy diskuterede vi også Lightning-autentificering. Dette system genererer en forskellig identifikator for hver tjeneste uden behov for at angive en e-mail-adresse eller personlige oplysninger. Det er muligt at have brugerstyrede decentraliserede identiteter, men der mangler standardisering og normalisering i decentraliserede identitetsprojekter. Pakkehåndteringsprogrammer som Nuget og Chocolaté, der tillader download af open-source-software uden for Microsoft Store, anbefales for at undgå ondsindede angreb. Sammenfattende er DNS afgørende for online sikkerhed, men det er nødvendigt at være opmærksom på potentielle angreb på DNS-servere.

## Anerkendelser og fortsæt med at grave kaninhullet

### Bedøm træningen og støt os

Denne kursus, sammen med alt indholdet på denne academy, er blevet givet til dig gratis af vores fællesskab. For at støtte os kan du dele det med andre, blive medlem af akademiet og endda bidrage til dets udvikling via GitHub. På vegne af hele teamet, tak!

Et bedømmelsessystem for træningen vil snart blive integreret i denne nye e-læringsplatform! I mellemtiden takker jeg dig meget for at have taget kurset, og hvis du nød det, bedes du overveje at dele det med andre.

### Gå videre

Tillykke med at have gennemført denne SECU 101-træning! Jeg håber oprigtigt, at du nød det, og at det åbnede døre for dig. Du er nu klar til at få din første bitcoin eller bare fortsætte eventyret med level 2-kurser!

- BTC 101 vil give dig de teoretiske grundlæggende om Bitcoin
- BTC 102 vil hjælpe dig med at oprette din bitcoin-plan
- LN 201 og 202 vil introducere dig til Lightning Network, et betalingsnetværk på andet niveau
- ECON 201 vil dække østrigsk økonomi
- MINING 201 for at lære mere om minedrift
- (og mange flere)

En kæmpe tak til vores Patreon, medlemmer og donorer for deres økonomiske støtte, tak til de mennesker, der deler, og tak til dem, der har gjort denne træning mulig: Théo pantamis, Renaud, Théo, Fabien, Noury, Muriel og hele teamet.
Vi ses snart!