---
term: HTLC
---

Står for "*Hashed Timelock Contract*". Dette er en Smart contract-mekanisme som hovedsakelig brukes på Lightning. Den finnes også noen ganger i atombytter. I utgangspunktet gjør HTLC en pengeoverføring betinget av at en hemmelighet avsløres, og inkluderer også en tidsbetingelse for å beskytte avsenderens penger i tilfelle en mislykket transaksjon.


På Lightning lar HTLC deg sende bitcoins til en node som du ikke har en direkte kanal med, ved å passere gjennom flere kanaler, uten behov for tillit underveis. Betaling mellom hver node er betinget av at det leveres et forhåndsbilde (hemmeligheten som, når den er hashet, tilsvarer en avtalt verdi). Hvis den endelige mottakeren leverer dette forhåndsbildet, kan han eller hun gjøre krav på pengene, noe som nødvendigvis gjør det mulig for alle mellomliggende noder å gjøre krav på pengene i kaskade.


Hvis Alice for eksempel vil sende 1 BTC til David, men ikke har en direkte kanal med ham, må hun gå gjennom Bob og Carol, som har betalingskanaler med hverandre. Slik fungerer transaksjonen:




- David gir Alice et Invoice-lyn. Dette inneholder Hash $h$ av et hemmelig $s$ (forbildet) som bare David kjenner til. Så vi har $h = \text{Hash}(s)$ ;
- Alice oppretter en HTLC med Bob, som tilbyr seg å sende henne 1 BTC på betingelse av at Bob gir henne en hemmelighet $s$ (forbildet) som tilsvarer Hash $h$ ;
- Bob oppretter en HTLC med Carol, som tilbyr seg å sende ham 1 BTC på betingelse av at hun oppgir den samme hemmeligheten $s$ ;
- Carol oppretter en HTLC med David, som tilbyr ytterligere 1 BTC hvis han avslører forhåndsbildet $ s$;
- David avslører $s$ (som bare han visste) til Carol for å motta 1 BTC. Carol kan nå bruke $s$ til å få BTC fra Bob. Og Bob, som nå kjenner $s$, gjør det samme med Alice.


Til slutt sendte Alice 1 BTC til David via Bob og Carol (en nøytral handling for sistnevnte), uten at noen trengte å stole på hverandre, ettersom alt er sikret i kaskade av HTLC-betingelsene.


HTLC muliggjør dermed såkalte "atomiske" utvekslinger: Enten er overføringen helt vellykket, eller så mislykkes den, og pengene returneres. Dette garanterer sikkerheten ved transaksjoner, selv mellom flere deltakere uten behov for tillit.