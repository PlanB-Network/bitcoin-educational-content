---
term: P2MS
definition: Multisignature script dat bitcoins vergrendelt met meerdere publieke sleutels en een drempelwaarde van handtekeningen vereist.
---

P2MS staat voor *Betalen aan Multisig*, wat zich vertaalt naar "betalen aan meerdere handtekeningen". Het is een standaard scriptmodel dat wordt gebruikt om bestedingsvoorwaarden op een UTXO vast te stellen. Hiermee kunnen bitcoins met meerdere publieke sleutels worden vergrendeld. Om deze bitcoins uit te geven, is een handtekening nodig met een vooraf bepaald aantal bijbehorende privésleutels. Bijvoorbeeld, een `P2MS 2/3` omvat `3` publieke sleutels met `3` geassocieerde geheime privésleutels. Om de bitcoins die vergrendeld zijn met dit P2MS script uit te geven, is een handtekening nodig met tenminste `2` van de `3` privésleutels. Dit is een drempel-veiligheidssysteem.


Dit script werd in 2011 uitgevonden door Gavin Andresen toen hij het onderhoud van de hoofdclient Bitcoin overnam. Vandaag de dag wordt P2MS slechts marginaal gebruikt door sommige applicaties. De overgrote meerderheid van moderne multisignaturen gebruikt andere scripts zoals P2SH of P2WSH. Vergeleken hiermee is P2MS extreem triviaal. De publieke sleutels waaruit het bestaat worden onthuld bij het ontvangen van de transactie. Het gebruik van P2MS is ook duurder dan andere scripts voor meerdere handtekeningen.


