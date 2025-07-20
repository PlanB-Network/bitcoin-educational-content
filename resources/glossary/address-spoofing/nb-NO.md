---
term: Address SPOOFING
---

Angrep der en ondsinnet aktør oppretter en Address (eller annen betalingsidentifikator) som er svært lik offerets. Målet er å lure brukeren til å kopiere feil Address under en transaksjon, noe som resulterer i at bitcoins sendes til angriperen i stedet for den tiltenkte destinasjonen.


Angriperen utnytter brukerens hastverk til å kopiere feil Address hvis han gjennomfører transaksjonen uten å sjekke nøyaktigheten. For å gjennomføre dette angrepet foretar angriperen vanligvis betalinger med små summer til offerets Wallet for å integrere den falske Address i transaksjonshistorikken hans. Dette angrepet brukes gjerne med altcoins, der det er vanlig praksis å gjenbruke de samme mottakeradressene, i motsetning til Bitcoin, der det er mer utbredt å bruke blanke adresser for hver transaksjon. Bitcoin-brukere er imidlertid ikke immune mot dette angrepet.


En annen metode for å plassere feil Address foran offeret er bruk av bedragersk Wallet-administrasjonsprogramvare som etterligner legitim programvare, eller å endre Address når en maskin kompromitteres, mellom det tidspunktet den kopieres og det tidspunktet transaksjonen opprettes. Dette omtales noen ganger som "*Address swapping*".


For å beskytte deg mot disse ulike angrepsmetodene er det viktig å sjekke flere tegn i Address, spesielt sjekksummen (på slutten), på skjermen til signeringsenheten før du signerer transaksjonen.


> ► *Dette angrepet omtales også noen ganger som Address-forgiftning