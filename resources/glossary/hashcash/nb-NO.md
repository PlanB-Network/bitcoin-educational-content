---
term: HASHCASH

---
HashCash er et proof-of-work-system som ble utviklet av Adam Back i 1997 for å bekjempe spam og DoS-angrep. Det er basert på prinsippet om at en avsender må utføre en beregningsoppgave (nærmere bestemt å finne en delvis kollisjon i en kryptografisk hash-funksjon) for å bevise sitt arbeid. Denne oppgaven er kostbar i form av tid og energi for avsenderen, men det er raskt og enkelt for mottakeren å verifisere resultatet. Denne protokollen har vist seg å være spesielt godt egnet til å bekjempe søppelpost i e-postkommunikasjon, ettersom den er minimalt belastende for legitime brukere, samtidig som den utgjør en betydelig hindring for spammere. Det tar noen sekunder å sende en enkelt e-post, men å gjenta denne operasjonen millioner av ganger blir ekstremt kostbart i form av energi og tid, noe som ofte opphever den økonomiske interessen av spamkampanjer, enten de har markedsføringsformål eller er ondsinnede. Dessuten gjør det det mulig å bevare avsenderens anonymitet.

HashCash ble raskt adoptert av cypherpunks som ønsket å utvikle et anonymt elektronisk valutasystem uten mellomledd. Adam Backs innovasjon introduserte faktisk knapphetsbegrepet i den digitale verden for første gang. Konseptet med proof of work finnes i flere elektroniske valutasystemer fra tiden før Bitcoin, blant annet:


- b-money av Wei Dai utgitt i 1998;
- R-POW av Hal Finney utgitt i 2004;
- BitGold av Nick Szabo utgitt i 2005.

HashCash-prinsippet finnes også i Bitcoin-protokollen, der det brukes som en beskyttelsesmekanisme mot Sybil-angrep.