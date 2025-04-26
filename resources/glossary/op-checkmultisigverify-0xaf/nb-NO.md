---
term: OP_CHECKMULTISIGVERIFY (0XAF)

---
Kombinerer en `OP_CHECKMULTISIG` og en `OP_VERIFY`. Det tar flere signaturer og offentlige nøkler for å verifisere at `M` av `N` signaturer er gyldige, akkurat som `OP_CHECKMULTISIG` gjør. Hvis verifiseringen mislykkes, stopper skriptet umiddelbart med en feilmelding, på samme måte som `OP_VERIFY`. Hvis verifiseringen er vellykket, fortsetter skriptet uten å skyve noen verdi til stakken. Denne opkoden ble fjernet i Tapscript.