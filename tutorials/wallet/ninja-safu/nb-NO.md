---
name: SAFU Ninja
description: Lagre seed med SAFU Ninja-metoden
---

![cover](assets/cover.webp)


## 1. Innledning



**Ninja SAFU**-metoden er en **DIY (Do It Yourself)**-løsning som lar deg lage en **bærekraftig, sikker og diskret** sikkerhetskopi av din **seed-frase** (en Mnemonic-frase på 12 eller 24 ord som er definert av **BIP-39**-standarden). Denne frasen er avgjørende for å gjenopprette en Bitcoin Wallet eller en hvilken som helst annen kompatibel Wallet.



I stedet for å skrive ned ordene dine på papir - en enkel, men sårbar metode - graverer du dem på **skiver i rustfritt stål**, montert på en **Bolt**. Resultatet er en kompakt, brann-, korrosjons-, vann- og støtsikker backup. I motsetning til papir, som kan ødelegges av flammer, fuktighet eller tid, garanterer rustfritt stål langvarig bevaring, selv under ekstreme forhold (opp til 1300 °C eller 20 tonns trykk).



Ninja SAFU-metoden har flere fordeler:





- **Konfidensialitet**: Du kjøper ikke et produkt som er identifisert som beregnet for sikkerhetskopiering av kryptovaluta. Komponentene er standard (skiver, bolter, metallboks), tilgjengelige i maskinvareforretninger, noe som reduserer risikoen for målretting i tilfelle en datalekkasje fra en spesialisert leverandør.





- **Rimelig pris**: Denne løsningen koster mellom **15 og 140 EUR**, avhengig av hvilke verktøy du allerede har.





- **Pålitelighet**: Metoden har blitt testet siden 2020 og er utprøvd og testet av sikkerhetseksperter som [Jameson Lopp] (https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/), som har utsatt den for strenge stresstester (ekstrem varme, korrosjon, mekanisk trykk).



Denne trinnvise veiledningen viser deg hvordan du lager din egen Ninja SAFU-sikkerhetskopi for å beskytte bitcoinsene dine bedre mot tap eller ødeleggelse. Hvis du vil lære mer om sikkerhetskopiering og beskyttelse av en seed-frase, kan du se i vedleggene.




## 2. Maskinvare



For å lage en Ninja SAFU-sikkerhetskopi trenger du følgende komponenter, som alle er tilgjengelige i maskinvareforretninger eller på nettet.



### 2.1 Nødvendige materialer





- **Skiver i rustfritt stål (M8 anbefales)**:
- **Materiale**: Rustfritt stål (f.eks. 304 eller V4A for økt korrosjonsbestandighet)
- **Størrelse**: M8 (indre diameter 8 mm, ytre diameter ~24 mm). M6-skiver er for små og vanskelige å gravere.
- **Antall**: 12 eller 24 skiver for en standard seed-setning, pluss valgfrie skiver (se avsnitt 3.4) og ca. ti skiver for tester eller feil.





- **Rustfritt stål Bolt og mutter (M8)** :
- **Spesifikasjoner**: Bolt 2,5 til 5 cm lang, avhengig av antall og tykkelse på skivene, diameter 8 mm. En vingemutter gjør det lettere å åpne uten verktøy, men en enkel mutter kan også brukes.



![image](assets/fr/03.webp)





- **Bokstav- og tallstansesett (3 mm eller 6 mm)**:
- **Spesifikasjoner**: 6 mm høye bokstaver gjør det lettere å lese og kan være å foretrekke hvis en del av bokstavene er ødelagt. Velg et robust sett for gjentatt bruk.



![image](assets/fr/04.webp)





- **Hammer eller slegge**:
    - En slegge er å foretrekke for tilstrekkelig og presis stemplingskraft





- **Ambolt eller solid underlag**:
 - Et tykt Hard-underlag (f.eks. 1 kg ambolt eller 10 cm belegningsstein) for å absorbere støt.



Hvis du ikke ønsker å investere i et sett med stanser, kan du også gravere skivene dine med en graveringspenn. Denne løsningen er ofte mer økonomisk, men krever større omhu for å oppnå et tilfredsstillende resultat.



### 2.2 Valgfrie verktøy





- **Stempelanordning**: Holder skiven og styrer stempelet, noe som gir presis, ren stempling, bedre orientering og jevn avstand mellom bokstavene



![image](assets/fr/05.webp)





- **Forseglingsanordninger**: Forseglet pose eller forseglingsstrimmel



![image](assets/fr/06.webp)





- **Hermetisk forseglet beholder**: For oppbevaring av skiveblokken



![image](assets/fr/07.webp)


### 2.3 Sikkerhet





- **Hansker** og **Vernebriller** anbefales.
- **Rørtang** til å skyve stansen inn i, slik at du holder stansen med rørtangen og ikke med fingrene.



### 2.4 Mengder og estimert kostnad





- **Antall for en sikkerhetskopi på 24 ord**: 24 skiver (minimum), 1 Bolt, 1 vingemutter, 1 sett med stempler, 1 hammer/massett, 1 ambolt/støtte.





- **Total kostnad**:
 - Skiver og bolter/muttere: ~ 15 EUR
 - Stansesett: ~ 45 EUR
 - Beskyttelsesveske: ~ 55 EUR
 - Med alt tilbehør: ~ 140 EUR





- Se appendiks for eksempler på utstyr.




## 3. Trinn-for-trinn-instruksjoner



1. **Gjør deg klar:**




 - Privat sted, ingen kameraer (inkludert smarttelefoner)
 - Robust, støtdempende overflate
 - Hansker og vernebriller
 - Rengjør vaskemaskinene for fett og smuss
 - Øv deg på testskiver


2. **Brenne Mnemonic ord** :




    - Graver inn hele ordet på den ene siden. Ikke begrens deg til de fire første bokstavene, i tilfelle den fjerde blir skadet.
    - Slå hardt med hammeren, og hold stansen med en rørtang


3. **Nummerer skivene** :




    - Graver inn ordet posisjonsnummer på samme side, viktig hvis skivene løsner.


4. **Registrer informasjon** (valgfritt og anbefalt) :




    - Graver inn det overflødige ordet på den andre siden av pucken
    - Graver inn en Wallet-identifikator på en ekstra skive
    - Graver inn avledningsstien til kontoen du bruker på en ekstra skive. Du finner denne informasjonen i innstillingene til porteføljeprogramvaren din. For en standard Taproot-portefølje vil for eksempel standard avledningssti være: `m / 86' / 0' / 0' /`
    - Skriv inn PIN-koden for å låse opp Hardware Wallet, eller anti-phishing-ordene hvis du bruker et COLDCARD.


5. **Ikke brenn passphrase :**




 - Hvis du bruker en passphrase, må du passe på at du ikke skriver den ned på samme kort som Mnemonic. passphrase er utformet for å beskytte Wallet i tilfelle tyveri av Mnemonic. Du finner mer informasjon i vedlegget.


6. **Sjekk lesbarhet** :




    - Sørg for at alle ord og tall er tydelige og leselige.


7. **Monter skivene** :




    - Tre skivene på Bolt i nummerrekkefølgen.
    - Valgfritt: legg til blanke skiver i endene.
    - Skru på vingemutteren for å feste batteriet.
    - Stram godt til for å øke beskyttelsen mot vann, brann og mekanisk belastning.


8. **Test backup** :




    - Prøv å gjenopprette porteføljen din fra den nye sikkerhetskopien
- **Forsegling av sikkerhetskopien** (valgfritt og anbefalt):
 - Ved å forsegle strimler, eller i forseglede poser.
 - Hvis du bruker en pose, bør du notere det unike identifikasjonsnummeret, slik at du kan kontrollere at det er den riktige posen og ikke en attrapp som erstatter den originale.




## 4. Lagring



### 4.1 Velg et egnet sted



Oppbevar sikkerhetskopien på et **diskret sted**, ute av syne og tilgjengelig for regelmessige kontroller. Velg **brannsikker og vanntett oppbevaring**, hjemme eller på et sted du har **eksklusiv kontroll over**.



Unngå steder der du er avhengig av en tredjepart (banksafe, notarius publicus): Du vil miste selvstendig tilgang til midlene dine, noe som strider mot Bitcoins prinsipper om suverenitet.



Avslør aldri at du bruker en metode som Ninja SAFU. Diskresjon er en Layer av sikkerhet i seg selv.



### 4.2 Redundans



Lag om nødvendig **flere kopier** og oppbevar dem på **ulike geografiske steder**.


Selv om du har valgt vann- og brannsikre materialer til enheten din, vil du ikke kunne få tilgang til den hvis den ligger begravd under flere kubikkmeter med steinsprut i hjemmet ditt, og det vil være svært vanskelig, om ikke umulig, å hente den ut igjen.




## 5. Oppfølging og vedlikehold



Selv om sikkerhetskopien er godt lagret, må den **kontrolleres regelmessig**:





- Inspiser sikkerhetskopien utenfor synsvidde **en eller to ganger i året**.
- Hvis graveringene **forringes**, må du lage en ny sikkerhetskopi, **teste den** og deretter **destruere den gamle kopien** forsiktig.
- Hvis sikkerhetskopien er i en forseglet pose :
 - Sjekk innloggingen din
 - Kontroller integriteten
 - Åpne konvolutten med jevne mellomrom for å inspisere tilstanden til graveringene, og hvis alt er i orden, legger du sikkerhetskopien i en ny lomme




**STAY SAFU!**


![image](assets/fr/08.webp)




## VEDLEGG



### A.1 Lagre gjenopprettingsfrasen din



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### A.2 Forståelse av passphrase BIP39



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

### A.3 Hvordan Bitcoin-porteføljer fungerer



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f


### A.4 Klassifisering av Ninja SAFU-metoden



Ifølge Jameson Lopp





- [Rapport] (https://jlopp.github.io/metal-Bitcoin-storage-reviews/reviews/safu-ninja/) om Ninja SAFU-metoden





- Sammenligningstabell [komplett](https://jlopp.github.io/metal-Bitcoin-storage-reviews/?ref=blog.lopp.net)





- Delvis tabell :


![image](assets/fr/09.webp)



### A.5 Eksempel på maskinvare





- **Skiver** for
 - [Titan] (https://pleb.style/fr-fr/products/disques-de-seed-supplementaires-titan-Wallet)
- Skiver + mutter + **beskyttelsesetui** (for skiver)
 - [Titan] (https://pleb.style/fr-fr/products/titan-Wallet-premium-acier-steel-Wallet-backup?variant=50022696419664)
 - [TerraSteel](https://pleb.style/fr-fr/products/terrasteel-Wallet-plebstyle-acier-backup)
- Stansesett
 - [PlebStyle](https://pleb.style/fr/products/schlagstempelset-a-z-0-9-3mm)
- **Grunnlag for typing**
 - [PlebStyle](https://pleb.style/fr/products/schlagunterlage-10cm-x-10cm-x-1-5cm)
- **Tappeinnretning** (guide)
 - [TerraSteel](https://pleb.style/fr-fr/products/zubehor-einschlag-vorrichtung?_pos=1&_sid=2767fd66f&_ss=r)
- Forseglingsenhet
 - [Forseglet pose] (https://pleb.style/fr/products/zubehor-5x-sicherheitstasche-tamper-evident)
 - [Tetningslister] (https://pleb.style/fr/products/zubehor-5x-siegel-streifen-fur-dein-seed-backup)
- **Komplett** sett
 - [Titan](https://pleb.style/fr-fr/products/titan-Wallet-diy-kit-premium-seed-backup-steelwallet-plebstyle?pr_prod_strat=e5_desc&pr_rec_id=aa9f36359&pr_rec_pid=8728733155664&pr_ref_pid=8730877788496&pr_seq=uniform)
 - [TerraSteel](https://pleb.style/fr-fr/products/kopie-von-terrasteel-Wallet-starter-kit)



Merk: Lenker til nettbutikker er kun ment som informasjon.


Det foreligger ikke noe kommersielt samarbeid mellom Plan B og de ovennevnte selgerne og produsentene.


Plan B kan ikke holdes ansvarlig for mangler, prisvariasjoner eller problemer knyttet til kvalitet eller levering av produkter. **DYOR**




### A.6 Fotokreditter



https://pleb.style/fr/


https://x.com/lopp/status/1463155802345193475


https://bitcointalk.org/index.php?topic=5389446.0


https://x.com/econoalchemist/status/1329271981712289797


https://www.waivio.com/@themarkymark/opprett-din-egen-metall-seed-nøkkel-backup


https://github.com/minibolt-guide/minibolt/blob/main/bonus/Bitcoin/safu-ninja.md