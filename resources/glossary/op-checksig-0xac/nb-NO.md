---
term: OP_CHECKSIG (0XAC)

---
Verifiserer gyldigheten av en signatur mot en gitt offentlig nøkkel. Den tar de to øverste elementene fra bunken: signaturen og den offentlige nøkkelen, og evaluerer om signaturen er korrekt for transaksjonshashen og den angitte offentlige nøkkelen. Hvis verifiseringen er vellykket, skyver den verdien `1` (true) til stakken, ellers `0` (false). Denne opkoden ble modifisert i Tapscript for å verifisere Schnorr-signaturer.