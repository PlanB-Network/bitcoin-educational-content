---
term: Dustrelayfee
definition: Node-parameter die het tarief definieert dat wordt gebruikt om de stoflimiet te berekenen.
---

Een standaardisatieregel die door netwerkknooppunten wordt gebruikt om te bepalen wat zij als de "Dust limiet" beschouwen Deze parameter bepaalt een tarief in Sats per virtuele kilobyte (Sats/kvB) dat als referentie dient om te berekenen of de waarde van een UTXO minder is dan de benodigde kosten om het in een transactie op te nemen. Een UTXO wordt namelijk beschouwd als "Dust" op Bitcoin als het meer aan vergoedingen vereist om te worden overgedragen dan de waarde die het zelf vertegenwoordigt. De berekening van deze limiet is als volgt:


```text
limit = (input size + output size) * fee rate
```


Omdat het vereiste vergoedingstarief voor een transactie om te worden opgenomen in een Bitcoin blok voortdurend varieert, kan elk knooppunt met de `DustRelayFee` parameter het vergoedingstarief definiëren dat wordt gebruikt bij deze berekening. Standaard is deze waarde op Bitcoin core ingesteld op 3.000 Sats/kvB. Om bijvoorbeeld de Dust limiet te berekenen voor een P2PKH input en output, die respectievelijk 148 en 34 bytes meten, zou de berekening zijn:


```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```


Dit betekent dat het betreffende knooppunt geen transacties doorgeeft met een P2PKH beveiligd UTXO waarvan de waarde lager is dan 546 Sats.