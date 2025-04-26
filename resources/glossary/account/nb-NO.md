---
term: KONTO

---
I HD-lommebøker (Hierarchical Deterministic) representerer en konto et avledningslag på dybde 3 i henhold til BIP32. Hver konto er sekvensielt nummerert fra `/0'/` (herdet avledning, så i virkeligheten `/2^31/` eller `/2 147 483 648/`). Det er på denne avledningsdybden at de velkjente `xpubene` befinner seg. I dag brukes vanligvis bare én konto i en HD-lommebok. Opprinnelig ble de imidlertid utviklet for å skille mellom ulike kategorier av bruk i samme lommebok. Hvis vi for eksempel tar en standard avledningssti for en ekstern Taproot (P2TR)-mottaksadresse: `m/86'/0'/0'/0'/0/0`, er kontoindeksen den andre `/0'/`.

![](../../dictionnaire/assets/17.webp)