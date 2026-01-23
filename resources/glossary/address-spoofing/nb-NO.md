---
term: Address spoofing
definition: Et angrep der en ondsinnet aktør oppretter en adresse som sterkt ligner offerets adresse for å lure dem og omdirigere deres betalinger.
---

Angrep der en ondsinnet aktør oppretter en Address (eller annen betalingsidentifikator) som er svært lik offerets. Målet er å lure brukeren til å kopiere feil Address under en transaksjon, noe som resulterer i at bitcoins sendes til angriperen i stedet for den tiltenkte destinasjonen.



Angriperen utnytter brukerens hastverk til å kopiere feil Address hvis han gjennomfører transaksjonen uten å sjekke nøyaktigheten. For å gjennomføre dette angrepet foretar angriperen vanligvis betalinger med små summer til offerets Wallet for å integrere den falske Address i transaksjonshistorikken hans. Dette angrepet brukes gjerne med altcoins, der det er vanlig praksis å gjenbruke de samme mottakeradressene, i motsetning til Bitcoin, der det er mer utbredt å bruke blanke adresser for hver transaksjon. Bitcoin-brukere er imidlertid ikke immune mot dette angrepet.



En annen metode for å presentere en feil adresse for offeret er bruken av falsk programvare for lommebokadministrasjon som etterligner legitim programvare, eller endring av adressen når en maskin er kompromittert, mellom tidspunktet den kopieres og tidspunktet transaksjonen konstrueres. Dette omtales noen ganger som '"*address swapping*"'.



For å beskytte deg mot disse ulike angrepsmetodene er det viktig å sjekke flere tegn i Address, spesielt sjekksummen (på slutten), på skjermen til signeringsenheten før du signerer transaksjonen.



Denne typen angrep omtales også noen ganger som '"*address poisoning*"'.