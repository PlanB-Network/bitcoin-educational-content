---
term: LOCK (.LOCK)

---
Fil som brukes i Bitcoin Core for å låse datakatalogen. Den opprettes når bitcoind eller Bitcoin-qt starter for å forhindre at flere instanser av programvaren får tilgang til den samme datakatalogen samtidig. Målet er å forhindre konflikter og datakorrupsjon. Hvis programvaren stopper uventet, kan .lock-filen bli liggende igjen og må slettes manuelt før Bitcoin Core startes på nytt.