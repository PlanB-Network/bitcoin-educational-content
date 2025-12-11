---
name: Programmering Bitcoin
goal: Bygg et komplett Bitcoin-bibliotek fra bunnen av og forstå Bitcoins kryptografiske grunnlag
objectives: 

 - Implementere aritmetikk for finitte felt og elliptiske kurveoperasjoner i Python
 - Konstruere og analysere Bitcoin-transaksjoner programmatisk
 - Opprette Testnet-adresser og kringkaste transaksjoner over nettverket
 - Beherske det matematiske grunnlaget som ligger til grunn for Bitcoins sikkerhetsmodell

---
# En reise til Bitcoins skript og programmer


Dette intensive todagerskurset, undervist av Jimmy Song, tar deg dypt inn i Bitcoins tekniske grunnlag ved å bygge et komplett Bitcoin-bibliotek fra grunnen av. Du starter med den grunnleggende matematikken i finitte felt og elliptiske kurver, og går videre gjennom transaksjonsparsing, skriptkjøring og nettverkskommunikasjon. Gjennom praktiske kodingsøvelser i Jupyter-notatbøker oppretter du din egen Testnet Address, konstruerer transaksjoner manuelt og sender dem direkte til nettverket - samtidig som du får en dyp forståelse av de kryptografiske prinsippene som gjør Bitcoin og Trustless sikker.


Kos deg med oppdagelsen!


+++

# Introduksjon

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Kursoversikt

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Velkommen til kurset PRO 202 _**Programming Bitcoin**_, en intensiv reise som tar deg fra aritmetikk i endelige felt til å bygge og sende ekte transaksjoner på Bitcoins testnett.

I dette kurset vil du gradvis bygge et Bitcoin-bibliotek i Python mens du tilegner deg de kryptografiske, protokollmessige og programvaremessige grunnlagene som er nødvendige for å forstå nøyaktig Bitcoins sikkerhet og indre virkemåte. PRO 202-tilnærmingen er helt praktisk: hvert konsept implementeres umiddelbart i Jupyter-notatbøker, slik at teori og kode styrker hverandre.

### Grunnleggende matematiske konsepter for Bitcoin

Denne første seksjonen etablerer det uunnværlige matematiske grunnlaget. Du vil implementere aritmetikk over endelige felt og elliptiske kurveoperasjoner (gruppelov, addisjon, doblin g, skalarmultiplikasjon...) — forutsetningene for ECDSA. Målet er todelt: å forstå den algebraiske strukturen som gjør kryptografiske signaturer mulig, og å bygge pålitelige Python-verktøy for å manipulere dem.

Deretter vil du formalisere komponentene i ECDSA: nøkkelgenerering, punktformatering, hashing, signaturopprettelse og verifisering. Denne seksjonen kobler teori direkte til praksis og fremhever implementasjonsdetaljer og robustheten i den underliggende sikkerhetsmodellen.

### Den indre virkemåten til en Bitcoin-transaksjon

I den andre delen vil du analysere strukturen til en Bitcoin-transaksjon: UTXO-er, input/output, sekvenser, skript, kodinger og mer. Du vil skrive kode for å konstruere, signere og verifisere transaksjoner, og oppnå en presis forståelse av hva som forpliktes av hashen og hvorfor.

Deretter vil du implementere en minimal _Script_-utfører, gjennomgå viktige opkoder og validere utgiftsbaner. Målet er å gjøre deg i stand til å revidere transaksjonsatferd, diagnostisere valideringsfeil og vurdere sikkerheten til utgiftspolicyer.

### Den indre virkemåten til Bitcoin-nettverket

I den tredje delen vil du plassere transaksjonen innenfor det bredere systemet: blokkstruktur, overskrifter, vanskelighetsgrad og Proof-of-Work-mekanismen. Du vil håndtere protokollmeldinger, blokkoverskrifter og Merkle-trær.

Til slutt vil du studere kommunikasjon mellom peer-to-peer-noder, meldingsoptimalisering og introduksjonen av SegWit.

Som med alle kursene på Plan ₿ Academy, inkluderer den siste delen en evaluering utformet for å styrke forståelsen din. Klar til å avdekke de indre mekanismene i Bitcoin og skrive koden som driver det? La oss begynne!

# Grunnleggende matematiske begreper for Bitcoin

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Matematikk for implementering av Bitcoin

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Elliptisk kurvekryptografi

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin Transaksjonens indre arbeid

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin Transaksjonsparsing og ECDSA-signaturer

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Skript- og transaksjonsvalidering

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Transaksjonskonstruksjon og betal-til-skript Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin Nettverkets indre struktur

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Bitcoin Blokker og Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Nettverkskommunikasjon og Merkle Trees

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Avansert nodekommunikasjon og segregert vitne

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Siste del


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Anmeldelser og rangeringer


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Konklusjon


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
