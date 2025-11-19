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

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematikk for implementering av Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Elliptisk kurvekryptografi

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin Transaksjonens indre arbeid

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Transaksjonsparsing og ECDSA-signaturer

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Skript- og transaksjonsvalidering

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Transaksjonskonstruksjon og betal-til-skript Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin Nettverkets indre struktur

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin Blokker og Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Nettverkskommunikasjon og Merkle Trees

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Avansert nodekommunikasjon og segregert vitne

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Siste del


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Anmeldelser og rangeringer


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>


## Konklusjon


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
