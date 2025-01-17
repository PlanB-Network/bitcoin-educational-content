---
term: ANONSETS (ANONYMITETSSETT)

---
Anonsett fungerer som indikatorer for å vurdere personvernnivået til en bestemt UTXO. Mer spesifikt måler de antallet UTXOer som ikke kan skilles fra hverandre i settet som inkluderer mynten som studeres. Siden det kreves en gruppe identiske UTXO-er, beregnes anonsett vanligvis innenfor en syklus av coinjoins. De gjør det mulig å bedømme kvaliteten på myntforbindelsene der det er hensiktsmessig. Et stort anonsett betyr økt grad av anonymitet, ettersom det blir vanskelig å skille ut en bestemt UTXO i settet. Det finnes to typer anonsett:


- Det potensielle anonymitetssettet;
- Det retrospektive anonymitetssettet.

Den første indikerer størrelsen på gruppen som den studerte UTXO-en er skjult blant, og som kjenner UTXO-en ved inngangen. Denne indikatoren gjør det mulig å måle motstanden til myntens personvern mot en analyse fra fortid til nåtid (input til output). På engelsk er navnet på denne indikatoren "*forward anonset*", eller "*forward-looking metrics*"

![](../../dictionnaire/assets/39.webp)

Den andre indikerer antall mulige kilder for en gitt mynt, med kjennskap til UTXO ved utgangen. Denne indikatoren gjør det mulig å måle motstanden til myntens personvern mot en analyse fra nåtid til fortid (utgang til inngang). På engelsk heter denne indikatoren "*backward anonset*", eller "*backward-looking metrics*"

![](../../dictionnaire/assets/40.webp)

> på fransk er det vanlig å bruke uttrykket "anonset" Det kan imidlertid oversettes med "ensemble d'anonymat" eller "potentiel d'anonymat" På både engelsk og fransk brukes også begrepet "score" noen ganger om anonset (prospektiv score og retrospektiv score)