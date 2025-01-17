---
term: BIP61

---
Innførte en avvisningsmelding i kommunikasjonsprotokollen mellom noder. Målet med BIP61 er å legge til en tilbakemeldingsmekanisme når en node mottar en transaksjon eller en blokk fra en annen node som den anser som ugyldig. Denne avvisningsmeldingen ville gjøre det mulig for en node å signalisere til avsenderen hvorfor den ble avvist. Denne typen kommunikasjon var ment å forbedre interoperabiliteten mellom ulike klienter og kommunikasjonen mellom fullstendige noder og SPV-klienter. Funksjonalitetene som BIP61 brakte med seg, ble til slutt forlatt fra og med versjon 0.20.0 av Bitcoin Core, ettersom de ble ansett som unødvendige, samtidig som de medførte økt behov for båndbredde.