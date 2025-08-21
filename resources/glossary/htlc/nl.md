---
term: HTLC
---

Staat voor "*Hashed Timelock Contract*". Dit is een Smart contract mechanisme dat voornamelijk gebruikt wordt op Lightning. Het wordt soms ook gevonden in atomaire swaps. In principe maakt HTLC een geldoverdracht afhankelijk van de onthulling van een geheim, en bevat het ook een tijdsvoorwaarde om het geld van de verzender te beschermen in het geval van een mislukte transactie.


Op Lightning kun je met HTLC bitcoins versturen naar een node waarmee je geen direct kanaal hebt, door verschillende kanalen te doorlopen, zonder dat je onderweg vertrouwen hoeft te hebben. De betaling tussen elk knooppunt is afhankelijk van het leveren van een pre-image (het geheim dat, als het gehasht is, overeenkomt met een afgesproken waarde). Als de uiteindelijke ontvanger deze pre-image levert, kan hij het geld opeisen en kan elk tussenliggend knooppunt noodzakelijkerwijs het geld in cascade opeisen.


Als Alice bijvoorbeeld 1 BTC naar David wil sturen, maar geen direct kanaal met hem heeft, moet ze via Bob en Carol, die wel betalingskanalen met elkaar hebben. Dit is hoe de transactie werkt:




- David geeft Alice een Invoice Bliksem. Deze bevat de Hash $h$ van een geheime $s$ (het pre-beeld) die alleen David kent. Dus we hebben: $h = \text{Hash}(s)$ ;
- Alice creëert een HTLC met Bob, die aanbiedt haar 1 BTC te sturen op voorwaarde dat Bob haar een geheime $s$ (de pre-image) geeft die overeenkomt met de Hash $h$ ;
- Bob maakt een HTLC met Carol, die aanbiedt hem 1 BTC te sturen op voorwaarde dat zij hetzelfde geheime $s$ geeft;
- Carol maakt een HTLC met David, die nog eens 1 BTC biedt als hij het $s$ preimage onthult;
- David onthult $s$ (die alleen hij wist) aan Carol om 1 BTC te ontvangen. Carol kan nu $s$ gebruiken om de BTC van Bob te krijgen. En Bob, die nu $s$ kent, doet hetzelfde met Alice.


Tenslotte stuurde Alice 1 BTC naar David via Bob en Carol (een neutrale actie voor de laatste), zonder dat iemand elkaar hoeft te vertrouwen, want alles is in cascade beveiligd door de voorwaarden van de HTLC's.


HTLC's maken dus zogenaamde "atomaire" uitwisselingen mogelijk: of de overdracht is volledig succesvol, of hij mislukt en het geld wordt teruggestuurd. Dit garandeert de veiligheid van transacties, zelfs tussen meerdere deelnemers die geen vertrouwen nodig hebben.