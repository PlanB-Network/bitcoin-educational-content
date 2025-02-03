---
term: LOMMEBOKIMPORTFORMAT (WIF)

---
En metode for å kode en privat Bitcoin-nøkkel på en måte som gjør det enklere å importere eller eksportere den mellom ulike lommebøker. WIF er basert på `Base58Check`-koding, som inkluderer informasjon om versjonen, komprimeringen av den tilsvarende offentlige nøkkelen og en sjekksum for å oppdage skrivefeil. En privat WIF-nøkkel starter med tegnene `5` for ukomprimerte nøkler, eller `K` og `L` for komprimerte nøkler, og inneholder alle tegnene som er nødvendige for å rekonstruere den opprinnelige private nøkkelen. WIF-formatet gir en standardisert måte å overføre en privat nøkkel mellom ulike lommebokprogrammer.