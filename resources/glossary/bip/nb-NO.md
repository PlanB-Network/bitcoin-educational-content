---
term: BIP

---
Forkortelse for "Bitcoin Improvement Proposal" Et Bitcoin Improvement Proposal (BIP) er en formell prosess for å foreslå og dokumentere forbedringer og endringer i Bitcoin-protokollen og dens standarder. Siden Bitcoin ikke har en sentral enhet som bestemmer om oppdateringer, gjør BIP-er det mulig for fellesskapet å foreslå, diskutere og implementere forbedringer på en strukturert og transparent måte. Hver BIP beskriver målene med den foreslåtte forbedringen, begrunnelser, potensielle konsekvenser for kompatibiliteten samt fordeler og ulemper. BIP-er kan skrives av alle medlemmer av fellesskapet, men må godkjennes av andre utviklere og redaktørene som vedlikeholder Bitcoin Core GitHub-databasen: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun og Ruben Somsen. Det er imidlertid viktig å forstå at disse personenes rolle i redigeringen av BIP-er ikke betyr at de kontrollerer Bitcoin. Hvis noen foreslår en forbedring som ikke blir akseptert innenfor det formelle BIP-rammeverket, kan de fortsatt presentere den direkte for Bitcoin-fellesskapet eller til og med opprette en fork som inkluderer deres modifikasjon. Fordelen med BIP-prosessen ligger i dens formalitet og sentralisering, noe som letter debatten for å unngå splittelse blant Bitcoin-brukere, og søker å implementere oppdateringer på en konsensus måte. Til syvende og sist er det prinsippet om økonomisk flertall som bestemmer maktdynamikken i protokollen.

BIP-er klassifiseres i tre hovedkategorier:


- BIP-er for standardspor*: Gjelder endringer som direkte påvirker Bitcoin-implementeringer, for eksempel regler for transaksjons- og blokkvalidering;
- Informative BIP-er*: Gir informasjon eller anbefalinger uten å foreslå direkte endringer i protokollen;
- Prosess BIP-er*: Beskriv endringer i prosedyrene rundt Bitcoin, for eksempel styringsprosesser.

Standard Track og Informational BIP-er klassifiseres også etter "lag":


- Konsensuslag*: BIP-er i dette laget gjelder konsensusreglene for Bitcoin, for eksempel endringer i blokkerings- eller transaksjonsvalideringsreglene. Disse forslagene kan enten være myke gafler (bakoverkompatible modifikasjoner) eller harde gafler (ikke-bakoverkompatible modifikasjoner). BIP-ene for SegWit og Taproot tilhører for eksempel denne kategorien;
- Peer Services*: Dette laget omhandler driften av Bitcoin-nodenettverket, det vil si hvordan noder finner og kommuniserer med hverandre på Internett.
- API/RPC*: BIP-ene i dette laget gjelder API (Application Programming Interfaces) og RPC (Remote Procedure Calls) som gjør det mulig for Bitcoin-programvare å samhandle med noder;
- Applikasjonslag*: Dette laget gjelder applikasjoner som er bygget på toppen av Bitcoin. BIP-ene i denne kategorien omhandler vanligvis modifikasjoner på nivået for Bitcoin-lommebokstandarder.

Prosessen med å sende inn en BIP begynner med konseptualisering og diskusjon av ideen på e-postlisten *Bitcoin-dev*. Hvis ideen er lovende, utarbeider forfatteren et utkast til en BIP i et bestemt format og sender det inn via en Pull Request på Core GitHub-depotet. Redaktørene går gjennom forslaget for å kontrollere at det oppfyller alle kriteriene. BIP-en må være teknisk gjennomførbar, gunstig for protokollen, overholde den påkrevde formateringen og være i samsvar med Bitcoins filosofi. Hvis BIP-en oppfyller disse vilkårene, blir den offisielt integrert i GitHub-arkivet for BIP-er. Den blir deretter tildelt et nummer. Dette nummeret bestemmes vanligvis av redaktøren, ofte Luke Dashjr, og tildeles logisk: BIP-er som omhandler lignende emner, får ofte fortløpende nummer.

BIP-ene går deretter gjennom ulike statuser i løpet av livssyklusen. Den gjeldende statusen er angitt i overskriften til hver BIP:


- Utkast: Forslaget er fortsatt i en redaksjons- og debattfase;
- Foreslått: BIP-en anses som komplett og klar for gjennomgang av samfunnet;
- Utsatt: BIP-en settes på vent til senere av mesteren eller en redaktør;
- Avvist: En BIP klassifiseres som avvist hvis den ikke har vist noen aktivitet på tre år. Forfatteren kan velge å gjenoppta den senere, slik at den kan gå tilbake til status som utkast;
- Trekkes tilbake: BIP-en er trukket tilbake av forfatteren;
- Endelig: BIP er akseptert og implementert i stor grad på Bitcoin;
- Aktiv: Denne statusen tildeles kun for prosess-BIP-er når det er oppnådd en viss konsensus;
- Erstattet/foreldet: BIP-en er ikke lenger aktuell eller har blitt erstattet av et nyere forslag som gjør den overflødig.

![](../../dictionnaire/assets/25.webp)

> ► *BIP er forkortelsen for "Bitcoin Improvement Proposal". På fransk kan det oversettes som "Proposition d'amélioration de Bitcoin". De fleste franske tekster bruker imidlertid akronymet "BIP" direkte som et vanlig substantiv, noen ganger i femininum, noen ganger i maskulinum*