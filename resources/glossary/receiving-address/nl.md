---
term: Ontvangstadres
definition: Informatie waarmee bitcoins kunnen worden ontvangen, meestal samengesteld uit een gehashte publieke sleutel.
---

Informatie die gebruikt wordt om bitcoins te ontvangen. Een Address wordt meestal geconstrueerd door een publieke sleutel te hashen, met `SHA256` en `RIMPEMD160`, en metadata aan deze digest toe te voegen. De publieke sleutels die gebruikt worden om een ontvangende Address te construeren, maken deel uit van de Wallet van de gebruiker en zijn daarom afgeleid van hun seed. Bijvoorbeeld, SegWit adressen zijn samengesteld uit de volgende informatie:


- Een HRP om "Bitcoin" aan te wijzen: `bc`;
- Een scheidingsteken: `1`;
- De gebruikte versie van SegWit: `q` of `p`;
- De payload: de digest van de publieke sleutel (of direct de publieke sleutel in het geval van Taproot);
- De controlesom: een BCH-code.


Een ontvangende Address kan echter ook iets anders voorstellen, afhankelijk van het gebruikte scriptmodel. P2SH adressen worden bijvoorbeeld geconstrueerd met Hash van het script. Taproot adressen, aan de andere kant, bevatten de getweakte publieke sleutel direct zonder het te hashen.


Een ontvangen Address kan worden weergegeven in de vorm van een alfanumerieke tekenreeks of als een QR-code. Elke Address kan meerdere keren gebruikt worden, maar dit wordt sterk afgeraden. Om een zekere mate van privacy te behouden, wordt namelijk geadviseerd om elke Bitcoin Address slechts eenmaal te gebruiken. Een nieuwe Address moet worden gegenereerd voor elke inkomende betaling aan iemands Wallet. Een Address is gecodeerd in `Bech32` voor SegWit V0 adressen, in `Bech32m` voor SegWit V1 adressen, en in `Base58check` voor Legacy adressen. Vanuit een technisch standpunt vertaalt het ontvangen van Bitcoin zich naar het bezitten van de private sleutel geassocieerd met een publieke sleutel (en dus een Address). Wanneer iemand bitcoins ontvangt, past de verzender de bestaande beperking op zijn uitgaven aan, zodat alleen de ontvanger nu over deze bevoegdheid kan beschikken.


