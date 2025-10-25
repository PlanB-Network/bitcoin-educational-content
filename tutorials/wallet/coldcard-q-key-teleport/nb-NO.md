---
name: COLDCARD Q - Key Teleport
description: Hva er Key Teleport, og hvordan bruker jeg det?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Hva er **Key Teleport**-funksjonen som Coinkite tilbyr med sitt flaggskip ColdCardQ-enhet?



**Med Key Teleport** kan du overføre konfidensielle data mellom to ColdCardQ-er på en sikker måte. Overføringskanalen trenger ikke engang å være kryptert, og den kan være offentlig.



Denne kan brukes til å overføre:





- **gW-0-fraser** (ColdCard Qs seed-master eller hemmelighetene som er lagret i ColdCardQs [seed Vault](https://coldcard.com/docs/temporary-seeds/#seed-vault).
- **konfidensielle notater og passord**: dette kan være en hvilken som helst hemmelighet eller hele [Secure Notes & Passwords]-katalogen (https://coldcard.com/docs/secure_notes/) på ColdCardQ.
- en sikkerhetskopi av hele **ColdCardQ**: ColdCardQ som mottar denne sikkerhetskopien, må ikke ha en seed Master for at dette skal fungere.
- gW-3 (**Delsignerte Bitcoin-transaksjoner** som en del av en multisignaturordning).



Dette krever at du har oppgradert [enhetens fastvare til versjon v1.3.2Q] (https://coldcard.com/docs/upgrade/) eller høyere.



## Hvordan bruker jeg Key Teleport?



### 1- For å overføre alle typer data



Her skal vi se på overføring av seed-setninger, notater, passord eller en hel overføring av en ColdCardQ-sikkerhetskopi. PSBT-overføringer for transaksjoner med flere signaturer vil bli behandlet senere.



#### Gjør enheten klar til å motta hemmelighetene



I menyen **"Avansert/Verktøy**" på ColdCardQ velger du **"Key Teleport (start)"**.


På neste skjermbilde foreslås et 8-sifret passord, her "20420219". Du må kommunisere dette passordet til avsenderen. Du kan for eksempel sende passordet på sms, via et sikkert meldingssystem eller via en telefonsamtale.



Klikk deretter på **"Enter**"-knappen på ColdCardQ for å gå videre til neste trinn.




![CCQ-key-teleport](assets/fr/01.webp)




En QR-kode genereres på skjermen. Denne QR-koden må du igjen kommunisere til ColdCardQ-"avsenderen". Den enkleste måten å gjøre dette på er via en videosamtale.



**IKKE SEND DENNE QR-KODEN VIA DEN SAMME OVERFØRINGSKANALEN SOM BLE BRUKT TIL Å SENDE DET FORRIGE 8-SIFREDE PASSORDET**.



![CCQ-key-teleport](assets/fr/02.webp)



*For de av dere som er interessert, la oss prøve å forstå den underliggende mekanismen som gjør det mulig å overføre hemmeligheter via usikrede kanaler*



*Det vi faktisk gjør her, er å sette i gang en overføring av hemmeligheter via Diffie-Hellman-metoden, som dekkes i BTC204-kurset jeg har inkludert nedenfor*



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*Vi har for øyeblikket:*




- genererte et flyktig nøkkelpar (offentlig/privat henholdsvis Ka og ka med Ka=G.ka, der G er ECDH-generatorpunktet), og et 8-sifret passord.
- brukte dette passordet til å kryptere den offentlige nøkkelen (Ka) via AES-256-CTR, og overførte deretter dette passordet via en kommunikasjonskanal A til den "sendende" ColdCardQ.
- til slutt sendte vi den krypterte pakken til avsenderen via QR-koden ovenfor, ved hjelp av en annen kommunikasjonskanal B enn den første.



#### Klargjør enheten som skal sende hemmelighetene



Fra avsenderenheten klikker du på **"QR"**-knappen for å skanne QR-koden du har fått tilsendt fra mottakerenheten, og deretter skriver du inn det 8-sifrede passordet du ble informert om i forrige trinn via en separat kanal. Vi er nå klare til å begynne å sende data fra den "sendende" enheten.



**Vennligst ikke skriv inn det 8-sifrede passordet feil, da vises det ingen feilmelding og prosessen fortsetter. Den endelige dataoverføringen vil imidlertid mislykkes, og du må starte på nytt**.



![CCQ-key-teleport](assets/fr/03.webp)



*For de mer nysgjerrige blant dere, la oss ta en ny titt på hva vi holder på med når det gjelder kryptografi og hemmelig overføring:*




- vi importerte de krypterte dataene ved å skanne QR-koden på mottakerenheten.
- deretter dekrypterte vi dem ved hjelp av det 8-sifrede passordet som ble sendt til oss via en sekundær kanal.
- vi er derfor i besittelse av den offentlige nøkkelen (Ka) som ble generert av mottakeren i utgangspunktet
- Deretter generate et nytt kortvarig nøkkelpar (Kb/kb, med Kb=G.kb) på den sendende enheten, som vi bruker til å bruke ECDH på Ka. Vi utfører derfor operasjonen kb.Ka=Ks, der Ks kalles **"Sesjonsnøkkel"**.




Du blir nå bedt om å velge hvilken type hemmeligheter som skal overføres mellom de to ColdCardQ-ene (konfidensielle notater, passord, full sikkerhetskopi, frø i hvelvet ditt, seed-enhetens master).



![CCQ-key-teleport](assets/fr/04.webp)



Her vil vår hemmelighet være en kort melding ved å velge **"Quick Text Message"**. Skriv inn meldingen din (for oss "PlanB Network rocks") og trykk deretter **"ENTER"**.


Enheten genererer deretter et nytt tilfeldig passord kalt **"Teleport Password"** , i eksempelet "NE XG BT SK".



![CCQ-key-teleport](assets/fr/05.webp)



Trykk på **"ENTER"**, så får du opp en ny QR-kode. Få den skannet av mottakerenheten. Og på en annen kommunikasjonskanal overfører du **"Teleport Password"** til mottakeren.



![CCQ-key-teleport](assets/fr/06.webp)



*Her igjen, for den nysgjerrige, i løpet av denne fasen:*




- etter å ha valgt hemmelighetene som skal overføres, lager vi generate et nytt tilfeldig passord kalt **"Teleport Password"**.
- vi krypterer deretter hemmelighetene via AES-256-CTR ved hjelp av **"Session Key"**, "Ks", som ble generert i forrige trinn
- vi prefikserer pakken som allerede er kryptert med **"Session Key"** med vår Kb-publikumsnøkkel, og legger deretter til en ytterligere Layer med AES-256-CTR-kryptering med **"Teleport Password"**. Det hele blir deretter kodet som en QR-kode




#### Fullfør overføringen av hemmeligheter til mottakerenheten



Trykk på **"QR"**-knappen for å skanne QR-koden som presenteres av den sendende enheten gjennom visio-kanalen. Du blir bedt om å oppgi **"Teleport Password"** for oss "NE XG BT SK".



![CCQ-key-teleport](assets/fr/07.webp)





Deretter dekrypteres dataene og gjøres forståelige for mottakerenheten. Meldingen som mottas er faktisk "PlanB Network rocks". Det er alt.



![CCQ-key-teleport](assets/fr/08.webp)



*Hva skjedde egentlig i løpet av denne siste fasen :*?




- vi har dekryptert dataene som avsenderen har sendt ved hjelp av **"Teleport Password"**
- har vi derfor den offentlige nøkkelen Kb og vår hemmelige melding kryptert med **"Session Key"**, "Ks". Men hvordan kan vi gjøre dette siden vi som mottaker ikke kjenner Ks, som ble opprettet av avsenderen?
- Vi må bruke vår private nøkkel "ka" fra det første trinnet **"Forbered enheten som skal motta dataene"** til den offentlige nøkkelen Kb.
- Ved å regne ut ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks, finner vi Ks. Som til slutt brukes til å dechiffrere den hemmelige meldingen



### 2- Slik overfører du PSBT til Multisig (avansert)



Dette forutsetter at din Wallet Multisig allerede er opprettet, og at ColdCardQ-enheten din allerede er forhåndsinnstilt til å kunne utføre multisignaturtransaksjoner. Hvis dette ikke er tilfelle, finner du forklaringer [her] (https://coldcard.com/docs/Multisig/) på Coinkites nettsted.



En rask påminnelse om hva en multisignatur Wallet (Multisig) er.



Vanligvis trenger du bare én privat nøkkel for å låse opp UTXO-ene som er knyttet til adressene dine, for å bruke Wallet-midlene dine.


I tilfellet med en Wallet Multisig kan det være behov for opptil 15 private nøkler og dermed 15 signaturer for å bruke midlene. Dette er kjent som en "M av N"-portefølje, der N er mellom 1 og 15 og M er antallet signaturer som kreves for at midlene skal kunne brukes. For eksempel vil en Wallet Multisig 3 av 5 kreve minst 3 signaturer av 5 mulige.



Utfordringen er da å koordinere mellom signatørene for å signere en "PSBT" for "Partially Signed Bitcoin Transaction" i tur og orden. I denne sammenhengen kan "**Key Teleport**" brukes til å overføre PSBT mellom medunderskriverne på en enkel og konfidensiell måte. En enkel videosamtale mellom medunderskriverne vil gjøre susen.



Slik gjøres det på en Multisig 3 av 4.



**Underskriver 1:**



Underskriver 1 importerer og signerer PSBT. Til slutt klikker han på **"T"** for å bruke **"Key Teleport"** til å overføre PSBT til signatar 2.



![CCQ-key-teleport](assets/fr/09.webp)




Etter at du har valgt signatar 2 ved å klikke på **"ENTER"**, får du et "TELEPORT PASSWORD" (her JJ YC AB 6A), som må overføres til signatar 2 via en annen kommunikasjonskanal. For eksempel en SMS eller en taleanrop, men **ikke** en videosamtale.



Trykk på **"ENTER"** igjen, og en QR-kode som representerer PSBT signert av 1 og deretter kryptert med "TELEPORT PASSWORD" vises.



![CCQ-key-teleport](assets/fr/10.webp)



**Underskriver 2:**



Underskriver 2 skanner QR-koden som underskriver 1 har gitt ham. Deretter skriver han inn "TELEPORT PASSWORD" som overføres via den sekundære kommunikasjonskanalen for å dekryptere de overførte dataene.



Underskriver 2 signerer transaksjonen og klikker deretter på **"T"** for å overføre PSBT til underskriver 3 via "Key Teleport".


Det er tydelig at to signaturer allerede er brukt. Det eneste som mangler er signatur fra underskriver 3 for at transaksjonen skal være gyldig. Velg underskriver 3 ved å klikke på **"ENTER"**.



![CCQ-key-teleport](assets/fr/11.webp)



Og et nytt "TELEPORT PASSWORD" opprettes, etterfulgt igjen av en QR-kode som koder PSBT signert av 1 og 2 og deretter kryptert med dette nye "TELEPORT PASSWORD" (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**Underskriver 3:**



Gjenta samme trinn som ovenfor.


Underskriver 3 skanner QR-koden som underskriver 2 har gitt ham. Deretter skriver han inn "TELEPORT PASSWORD" som overføres via den sekundære kommunikasjonskanalen.



Underskriver 3 signerer transaksjonen, og siden 3 av 4 signaturer er brukt denne gangen, blir transaksjonen angitt som fullført, og er klar for distribusjon via ulike medier (SD-kort, NFC, QR osv.).



![CCQ-key-teleport](assets/fr/13.webp)



Hvis ColdCardQs "Push Tx"-funksjon er aktivert, er det bare å feste ColdCardQ på baksiden av en NFC-aktivert Internett-tilkoblet enhet (smarttelefon/nettbrett) for å sende transaksjonen over Bitcoin-nettverket.



![CCQ-key-teleport](assets/fr/14.webp)



*For PSBT-overføringer fra en underskriver til en annen brukes "Key Teleport" ganske enkelt via et "Teleport Password" på hvert trinn, som krypterer PSBT når den overføres fra en underskriver til en annen. Ettersom de overførte dataene ikke kan brukes til å stjele midler, er det ikke behov for Diffie-Hellman, slik tilfellet er når man sender svært konfidensielle hemmeligheter (seed, passord osv.)*.



![CCQ-key-teleport](assets/fr/15.webp)



*Kilde: [ColdCards offisielle nettside [ColdCards offisielle nettsted](https://coldcard.com/)*