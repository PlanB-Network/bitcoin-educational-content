---
term: OP_CHECKSIGVERIFY (0XAD)

---
Utfører samme operasjon som `OP_CHECKSIG`, men hvis signaturverifiseringen mislykkes, stopper skriptet umiddelbart med en feilmelding, og transaksjonen er dermed ugyldig. Hvis verifiseringen lykkes, fortsetter skriptet uten å skyve en `1` (true)-verdi på stakken. Oppsummert utfører `OP_CHECKSIGVERIFY` operasjonen `OP_CHECKSIG` etterfulgt av `OP_VERIFY`. Denne opkoden ble modifisert i Tapscript for å verifisere Schnorr-signaturer.