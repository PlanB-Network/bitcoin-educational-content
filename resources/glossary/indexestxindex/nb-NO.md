---
term: INDEKSER/TXINDEX/

---
Filer i Bitcoin Core som er dedikert til å indeksere alle transaksjoner som finnes i blokkjeden. Denne indekseringen gjør det mulig å søke raskt etter detaljert informasjon om en transaksjon ved hjelp av dens identifikator (TXID), uten å måtte gå gjennom hele blokkjeden. Opprettelsen av disse indekseringsfilene er et alternativ som ikke er aktivert som standard i Bitcoin Core. Hvis denne funksjonen ikke er aktivert, vil noden din kun indeksere transaksjoner som er tilknyttet lommebøker som er knyttet til noden din. For å aktivere indeksering av alle transaksjoner må du angi parameteren `-txindex=1` i filen `bitcoin.conf`. Dette alternativet er spesielt nyttig for applikasjoner og tjenester som ofte søker gjennom transaksjonshistorikken til Bitcoin.