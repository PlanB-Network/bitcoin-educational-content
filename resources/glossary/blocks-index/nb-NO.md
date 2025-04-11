---
term: BLOCKS INDEX

---
En LevelDB-datastruktur i Bitcoin Core som katalogiserer metadata om alle blokker. Hver oppføring i denne indeksen inneholder detaljer som blokkens identifikator, dens høyde i blokkjeden, pekeren til blokken i databasen og andre metadata. Denne indekseringen gjør det mulig å raskt hente frem en lagret blokk i minnet.