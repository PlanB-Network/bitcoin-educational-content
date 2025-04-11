---
term: ETIKETT (STILLE BETALINGER)

---
I Silent Payments-protokollen er etiketter heltall som brukes til å endre den opprinnelige statiske adressen for å opprette mange andre statiske adresser. Bruken av disse etikettene gjør det mulig å skille ut betalinger som sendes via Silent Payments, ved å bruke forskjellige statiske adresser for hver bruk, uten å øke den operasjonelle byrden for å oppdage disse betalingene (skanning). Bob bruker en statisk adresse $B$, som består av to offentlige nøkler: $B_{\text{scan}}$ for skanning og $B_{\text{spend}}$ for utgifter. Hashverdien av $b_{\text{scan}}$ og et heltall $m$, skalarmultiplisert med generatorpunktet $G$, legges til den offentlige utgiftsnøkkelen $B_{\text{spend}}$ for å opprette en slags ny offentlig utgiftsnøkkel $B_m$:

$$ B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G $$$

Den første nøkkelen $B_1$ oppnås for eksempel på denne måten:

$$ B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$$

Den statiske adressen som publiseres av Bob, vil nå bestå av $B_{\text{scan}}$ og $B_m$. For eksempel vil den første statiske adressen med etiketten $1$ være:

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

Vi starter bare fra etikett $1$, fordi etikett $0$ er reservert for endring. Alice, som ønsker å sende bitcoins til den merkede statiske adressen som Bob har oppgitt, vil utlede den unike betalingsadressen $P_0$ ved å bruke den nye $B_1$ i stedet for $B_{\text{spend}}$:

$$ P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$$

I virkeligheten vet Alice kanskje ikke engang at Bob har en merket adresse, ettersom hun bare bruker den andre delen av den statiske adressen han oppga, som i dette tilfellet er verdien $B_1$ i stedet for $B_{\text{spend}}$. For å skanne etter betalinger vil Bob alltid bruke verdien av sin opprinnelige statiske adresse med $B_{\text{spend}}$ på denne måten:

$$ P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$$

Deretter trekker han ganske enkelt fra verdien han finner for $P_0$ fra hver utgang én etter én. Deretter sjekker han om et av resultatene av disse subtraksjonene samsvarer med verdien på en av etikettene han bruker på lommeboken sin. Hvis det for eksempel stemmer overens med utdata nr. 4 med merkelappen $1$, betyr det at denne utgangen er en stille betaling knyttet til hans statiske adresse merket $B_1$:

$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$$

Dette fungerer fordi:

$$ B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$$

Takket være denne metoden kan Bob bruke en rekke statiske adresser (med $B_1$, $B_2$, $B_3$ ...), som alle er avledet fra hans statiske basisadresse ($B = B_{\tekst{scan}} \text{ ‖ } B_{\tekst{spend}}$), for å skille bruksområdene fra hverandre på en god måte.

Denne separasjonen av statiske adresser er imidlertid bare gyldig fra et personlig lommebokadministrasjonsperspektiv, men tillater ikke separasjon av identiteter. Siden alle har samme $B_{\text{scan}}$, er det veldig enkelt å knytte alle de statiske adressene sammen og utlede at de tilhører én enkelt enhet.