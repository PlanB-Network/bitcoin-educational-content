---
term: RPC (REMOTE PROCEDURE CALL)

---
En dataprotokoll som gjør det mulig for et program å utføre en prosedyre på en annen ekstern datamaskin som om den ble utført lokalt. I Bitcoin-sammenheng brukes den spesielt til å gjøre det mulig for applikasjoner å samhandle med Bitcoin. Det kan brukes til å utføre kommandoer på en Bitcoin-node, for eksempel å sende transaksjoner, administrere lommebøker eller få tilgang til informasjon i blokkjeden. Sikkerheten i denne interaksjonen sikres gjennom autentisering via en `.cookie`-fil eller legitimasjon, slik at bare autoriserte klienter kan utføre RPC-er på noden.

> på engelsk kan det oversettes med "Remote Procedure Call"