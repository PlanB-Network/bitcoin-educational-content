---
term: SIGOPS (SIGNATUROPERASJONER)

---
Refererer til de digitale signaturoperasjonene som er nødvendige for å validere transaksjoner. Hver Bitcoin-transaksjon kan inneholde flere inndata, og hver av dem kan kreve én eller flere signaturer for å anses som gyldig. Verifiseringen av disse signaturene gjøres gjennom bruk av spesifikke opkoder kalt "sigops". Dette inkluderer `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIG` og `OP_CHECKMULTISIGVERIFY`. Disse operasjonene påfører nettverksnodene som skal verifisere dem, en viss arbeidsbelastning. For å forhindre DoS-angrep gjennom kunstig oppblåsing av antall sigops, setter protokollen derfor en grense for antall tillatte sigops per blokk for å sikre at valideringsbelastningen forblir håndterbar for nodene. Denne grensen er for øyeblikket satt til maksimalt 80 000 sigops per blokk. Nodene følger disse reglene for å telle:

I `scriptPubKey` teller `OP_CHECKSIG` og `OP_CHECKSIGVERIFY` som 4 sigops. Opkodene `OP_CHECKMULTISIG` og `OP_CHECKMULTISIGVERIFY` teller 80 sigops. Under tellingen blir disse operasjonene multiplisert med 4 når de ikke er en del av en SegWit-inngang (for en P2WPKH vil antallet sigops derfor være 1);

I `redeemScript` teller også opkodene `OP_CHECKSIG` og `OP_CHECKSIGVERIFY` som 4 sigops, `OP_CHECKMULTISIG` og `OP_CHECKMULTISIGVERIFY` regnes som `4n` hvis de kommer før `OP_n`, og ellers som 80 sigops;

For `witnessScript` er `OP_CHECKSIG` og `OP_CHECKSIGVERIFY` verdt 1 sigop, `OP_CHECKMULTISIG` og `OP_CHECKMULTISIGVERIFY` regnes som `n` hvis de er introdusert av `OP_n`, eller 20 sigop ellers;

I Taproot-skript behandles sigops på en annen måte enn i tradisjonelle skript. I stedet for å telle hver signaturoperasjon direkte, innfører Taproot et sigops-budsjett for hver transaksjonsinngang, som er proporsjonalt med størrelsen på denne inngangen. Dette budsjettet er 50 sigops pluss bytestørrelsen på inndataens vitne. Hver signaturoperasjon reduserer dette budsjettet med 50. Hvis utførelsen av en signaturoperasjon reduserer budsjettet til under null, er skriptet ugyldig. Denne metoden gir større fleksibilitet i Taproot-skript, samtidig som den beskytter mot potensielt misbruk knyttet til sigops, ved å knytte dem direkte til vekten på inndataene. Taproot-skript er derfor ikke inkludert i grensen på 80 000 sigops per blokk.