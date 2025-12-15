---
name: Electrum Airgap
description: Et første skritt mot sikkerhet, en cold wallet med Electrum
---
![cover](assets/cover.webp)



## Cold Wallet



I denne veiledningen vil jeg forklare hvordan du lager din første luftgap-signeringsenhet, frakoblet fra Internett, selv uten å ha en dedikert Hardware Wallet. Alt du trenger er å ha to datamaskiner tilgjengelig:




- en gammel enhet som for alltid er forhindret fra å koble seg til Internett;
- datamaskinen du bruker til daglig.



Denne konfigurasjonen gir en større grad av sikkerhet enn den klassiske `Hot Wallet`: Den gamle datamaskinen - uten nettverkstilkobling - er vokter av de private nøklene dine, som aldri eksponeres på Internett, men lagres offline ("airgap" eller "Cold").



I stedet installerer du en Wallet-skjerm ("watch-only") på den daglige datamaskinen din, som er koblet til nettverket og som du for eksempel kan bruke til å sjekke saldoer og forberede kvitteringstransaksjoner.



## Wallet Airgap: Hva og hvordan



Ved å utføre trinnene i denne veiledningen vil vi installere to Software Wallet Electrum på to forskjellige datamaskiner og til slutt opprette to lommebøker med forskjellige nøkkellagre: Wallet airgap vil bruke hele hierarkiet til Wallet HD, mens Wallet display vil bli generert med den offentlige hovednøkkelen.



Disse to lommebøkene vil på alle måter være svært forskjellige fra hverandre. Det eneste de vil ha til felles, som vi skal se, er adressene:




- gW-13 på airgap-datamaskinen kan bare signere, men når den er koblet fra nettverket, kjenner den ikke til balansen og adressene som brukes;
- gW-12 på den daglige datamaskinen vil bare kunne forberede og forplante transaksjoner, uten å kunne disponere utgiftene, i fravær av de private nøklene.



## Foreløpige forberedelser



For å laste ned Electrum anbefaler jeg at du følger de første trinnene i denne veiledningen:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Etter nedlasting må du alltid verifisere utgivelsen før du installerer den, og deretter fortsette til "One Server"-konfigurasjonen, som du finner i hjelpeseksjonen under `Start med en Dummy Wallet`.



Konfigurasjonsoperasjonen "Én server" er bare nødvendig for Wallet som er installert på den daglige datamaskinen, ettersom den andre datamaskinen alltid vil være frakoblet.



De følgende operasjonene innebærer å øve på to forskjellige datamaskiner (og lommebøker), så for enkelhets skyld og for å holde fokus valgte jeg å stille inn Wallet airgap med det lyse temaet, mens Wallet-skjermen har det mørke temaet.



## Wallet Opprettelse av luftgap



Etter at du har lastet ned og bekreftet nedlastingen av Electrum, tar du en kopi av den kjørbare filen og tar den med til datamaskinen din offline. Start den deretter og installer Electrum.



Dobbeltklikk for å starte Electrum: datamaskinen der du vil bruke denne Wallet er frakoblet, ignorere nettverksinnstillingene og gå til opprettelsen av Wallet som vi i denne guiden vil kalle `airgap`.



![image](assets/en/01.webp)



Velg _Standard lommebok_.



![image](assets/en/02.webp)



Velg deretter _Create a new seed_ for å få programvaren til å generate Mnemonic.



![image](assets/en/03.webp)



Transkriber de 12 generate-ordene fra Electrum nøyaktig til et papirunderlag, og fortsett med verifiseringstrinnet ved å skrive inn ordene på nytt i riktig rekkefølge når Electrum ber om det.



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Etter at Wallet-opprettelsen er fullført, angi et komplekst passord (`Strong`) for å kryptere Wallet-filen på airgap-enheten. Dette trinnet er veldig delikat og viktig, ettersom passordet som er valgt nå, forhindrer tilgang til Wallet som har dispositiv makt, å kunne bruke midler til å signere transaksjoner.



![image](assets/en/06.webp)



Ved å klikke på _Finish_ defineres Wallet og vises på skjermen. Indikatoren for nettverkstilkobling, dvs. den fargede prikken i nedre høyre hjørne, er selvfølgelig rød, ettersom datamaskinen er frakoblet og ikke tillater Wallet å eksponere online-tastene.



![image](assets/en/07.webp)



## Opprettelse Wallet av visualisering



Nå som Wallet har private nøkler offline, må du sette opp en Wallet-skjerm, eller "watch-only", som lar deg se saldoen, samt forberede kvitteringstransaksjoner for å fortsette å samle Sats på en trygg måte.



Fra Wallet på den frakoblede enheten velger du menyen _Wallet_ -> _Information_



![image](assets/en/08.webp)



Vinduet med all Wallet-informasjonen din vises, der du kan krysse av for `derivasjonssti` og `masterfingeravtrykk`, for eksempel for å markere dem ved siden av ordene i Mnemonic-setningen (anbefales på det sterkeste).



![image](assets/en/09.webp)



Husk at du tar disse dataene fra en datamaskin som ikke er tilkoblet, så du må kopiere/lim inn `zpub` til en tekstfil og lagre den på en USB-pinne.



Nå kan du flytte til datamaskinen som er koblet til Internett, for å starte Electrum og opprette en ny Wallet.



Velg _New/Restore_ fra _File_-menyen.



![image](assets/en/10.webp)



Den nye Wallet er kun for visning, så i denne veiledningen vil vi kalle den "kun for visning".



![image](assets/en/12.webp)



På neste skjermbilde velger du _Standard lommebok_ og fortsetter ved å klikke på _Neste_.



![image](assets/en/13.webp)



Når du velger `Keystore`, må du være forsiktig: For å opprette displayet Wallet velger du _Use a master key_. Fortsett deretter med _Neste_.



![image](assets/en/14.webp)



Lim inn her `zpub` som er kopiert fra Wallet offline og som du tok med til denne datamaskinen via usb-mediet.



![image](assets/en/15.webp)



Avslutt med å angi et sterkt passord også for denne Wallet, eventuelt et annet enn det som er valgt for den tilsvarende Cold.



Du vil se displayet Wallet vises, med en advarsel. Meldingen minner deg på at dette er en Wallet som kun vises, og at du ikke kan bruke de tilknyttede midlene med den.



**Bemerk godt**: **Du må derfor alltid ha de private nøklene for å disponere UTXOene til denne Wallet**. Med et godt backup-system vil det ikke være vanskelig for deg å forbli i full besittelse av dine Bitcoins.



![image](assets/en/16.webp)



Denne advarselen vil vises hver eneste gang du åpner denne Wallet. Klikk på _Ok_, og la oss gå videre til bekreftelsestrinnet.



## Verifisering av de to Wallet



Som vi lærte i begynnelsen av denne veiledningen, er en Wallet airgap og dens display Wallet to porteføljer som har forskjellige funksjoner, men som **deler de samme adressene**.



Hvis vi ser på de to lommebøkene side om side, legger vi visuelt merke til at i Wallet-luftgapet er det et "seed" -symbol, mens det ikke er det i den eneste klokken. Selv denne detaljen vil hjelpe deg å huske at Wallet-skjermen Wallet ikke har private nøkler.



![image](assets/en/17.webp)



For å gjøre en nøyaktig første sjekk, velger du menyen `Addresses` i begge lommebøkene: Siden de deler de samme adressene, bør adresselisten være identisk for begge.



![image](assets/en/18.webp)



⚠️ **OPPMERKSOMHET**: **det finnes ingen mellomting; adressene må være de samme. Hvis de er forskjellige, er det nødvendig å slette alt arbeidet som er gjort så langt, og begynne på nytt**.



Nå kan du fortsette med å gjøre to forskjellige kontroller. Først kan du prøve å slette de to lommebøkene og gjenopprette dem fra bunnen av, hver på den aktuelle datamaskinen. Hvis du fortsetter med denne verifiseringen, er prosedyrene for visning av Wallet identiske med de som er beskrevet ovenfor.



For Wallet airgap må du imidlertid velge _I already have a seed_ på skjermbildet `keystore` og skrive inn ordene ved å kopiere dem fra papirbackupen din.



Etter at prøveperioden er over, kan du prøve å foreta en transaksjon med et lite beløp og bruke det umiddelbart.



## Mottak og bruk av transaksjoner



For å begynne å bruke Electrum-luftgapet ditt, kan du foreta en kvitteringstransaksjon med et lite beløp, og deretter bruke det på en egen Address. Deretter kan du gjøre deg kjent med prosedyren og bekrefte at du har full kontroll over midlene.



**Merknad**: Jeg anbefaler ikke at du setter inn et stort beløp på Wallet før du er sikker på at du kan utføre alle operasjoner problemfritt.



Trinnene som er forklart nedenfor, kan ved første øyekast virke kompliserte. Men ikke la deg skremme av dette: Når du har prøvd dem første gang, vil du oppdage at det bare tar noen få minutter å gjennomføre dem.



For å motta midler, må du nødvendigvis bruke skjermen Wallet som ligger på datamaskinen din koblet til Internett. Fra `Motta`-menyen klikker du på _Create request_ for å få Electrum generate den første tilgjengelige Address og bruke den til å sende oss noen få Satss.



![image](assets/en/19.webp)



![image](assets/en/20.webp)



Når transaksjonen har blitt forplantet, kan du allerede se at den - som naturlig er - bare er synlig på displayet Wallet og ikke på Wallet-luftgapet.



![image](assets/en/21.webp)



Etter at transaksjonen er bekreftet, kan du forberede utgiften og dermed prøve signeringsprosedyren fra Wallet utenfor nettverket. Forbered deretter transaksjonen på watch-only og trykk på _Preview_ for å sjekke den



![image](assets/en/22.webp)



Du får opp det avanserte transaksjonsvinduet der du kan se det:




- transaksjonen er ikke signert (`Status: Unsigned);
- kommandoene `Sign` og `Broadcast` er sperret.



Det eneste du kan gjøre er å eksportere transaksjonen slik den er, ta den med til Wallet airgap og signere den.



Sett inn en USB-minnepinne i datamaskinen, og velg _Share_ fra menyen nederst til venstre.



![image](assets/en/23.webp)



Deretter velger du _Lagre til fil_.



![image](assets/en/24.webp)



Lagre transaksjonen på minnepinnen.



Du vil legge merke til at Electrum gir filen et navn med de første sifrene i transaction ID, og filtypen er `.PSBT`, som betyr `Partially Signed Bitcoin Transaction`.



Pakk ut mediet med filen `.PSBT` og koble det til datamaskinen uten nett.



Fra Wallet airgap velger du nå menyen _Verktøy_, deretter _Last inn transaksjon_ og deretter Fra fil_.



![image](assets/en/25.webp)



Med filbehandleren velger du `.PSBT` fra plasseringen.



![image](assets/en/29.webp)



Programvaren utenfor nettverket vil automatisk åpne det avanserte transaksjonsvinduet, helt identisk med hvordan du så det på Wallet-skjermen. Status er "Usignert", men forskjellen er at kommandoen "Signer" her er aktiv. Og det er nettopp det du må utføre.



![image](assets/en/26.webp)



![image](assets/en/27.webp)



Nå som transaksjonen er signert, må du huske at Wallet er på en frakoblet maskin. Derfor - selv om du ser at kommandoen `Broadcast` er aktiv - vil ikke Wallet være i stand til å videreformidle transaksjonen til Bitcoin-nettverket.



Det du trenger å gjøre nå, er å gjenta operasjonen med å eksportere den signerte transaksjonen til USB-pinnen, slik at du kan importere den til en datamaskin som er koblet til Internett og spre den.



Velg _Share_ nederst til venstre i menyen igjen, og velg deretter _Save to file_.



![image](assets/en/28.webp)



Nå har filen en annen filtype: **I stedet for `.PSBT` har transaksjonen nå utvidelsen `.txn`. Fra nå av er det slik Electrum vil la deg gjenkjenne signerte transaksjoner fra usignerte**.



![image](assets/en/30.webp)



For den endelige forplantningen av transaksjonen tar du USB-pinnen ut av den offline datamaskinen og setter den inn i datamaskinen som er koblet til Internett.



Gjenta importprosedyren fra Watch-only, det vil si at du fra menyen _Tools_ velger _Load transaction_ og til slutt _From file_.



![image](assets/en/31.webp)



Electrum åpner transaksjonsvinduet for deg, som skiller seg markant fra det som ble vist tidligere på denne Wallet, ved at det nå er signert (`Status: Signed`) og `Broadcast`-kommandoen er tilgjengelig.



Den siste operasjonen du trenger å gjøre, er nettopp det:



![image](assets/en/32.webp)



## Konklusjoner



Testene dine er nå ferdige. Hvis du fulgte veiledningen og fikk de samme resultatene, har du opprettet en Wallet Cold med Electrum, på to forskjellige datamaskiner, som du kan bruke på airgap-måte til å lagre Bitcoins.



Det eneste du må være oppmerksom på, er to ting:


1) **bruk aldri Wallet airgap til generate mottaksadresser**. Siden den er frakoblet, vil den alltid tilby deg den første Address, som sammenfaller med den du nettopp brukte til å foreta testtransaksjonen;



![image](assets/en/33.webp)



_Som du kan se på bildet over, kjenner ikke den frakoblede Wallet sin egen Address-historie. Den er helt blind i så måte. **Den eneste oppgaven den kan gjøre for deg, er å lagre frakoblede nøkler og signere transaksjonene dine**_.



2) Bruk en USB-minnepinne som kun er beregnet til dette formålet, **ikke bruk et medium du bruker ofte**. Hverdagsverktøy er mer utsatt for cyberangrep, og utilsiktet kan du angripe til og med datamaskinen du holder frakoblet fra nettverket. En USB-pinne som du kun bruker til dette formålet, har svært få muligheter til å komme i kontakt med PC-en din på nettet, spesielt hvis du er en hodler som ikke trenger å bruke penger, og dermed reduserer sannsynligheten for å motta og deretter overføre virus, skadelig programvare osv.