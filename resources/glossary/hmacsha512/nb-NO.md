---
term: HMAC-SHA512

---
hMAC-SHA512 står for "Hash-based Message Authentication Code - Secure Hash Algorithm 512". Det er en kryptografisk algoritme som brukes til å verifisere integriteten og autentisiteten til meldinger som utveksles mellom to parter. Den kombinerer den kryptografiske hashfunksjonen `SHA512` med en delt hemmelig nøkkel for å generere en unik MAC-kode (Message Authentication Code) for hver melding.

I forbindelse med Bitcoin er den naturlige bruken av `HMAC-SHA512` noe avledet. Denne algoritmen brukes i den deterministiske og hierarkiske avledningsprosessen for det kryptografiske nøkkeltreet til en lommebok. `HMAC-SHA512` brukes spesielt til å gå fra frøet til hovednøkkelen, og deretter for hver avledning fra et overordnet par til underordnede par. Denne algoritmen finnes også i en annen avledningsalgoritme kalt `PBKDF2`, som brukes til å gå fra gjenopprettingsfrasen og passordfrasen til frøet.