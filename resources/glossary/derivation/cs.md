---
term: DERIVATION
---

Odkazuje na proces generování dceřiných párů klíčů z rodičovského páru klíčů (soukromý klíč a veřejný klíč) a řetězového kódu v rámci deterministické a hierarchické (HD) peněženky. Tento proces umožňuje segmentaci větví a organizaci peněženky do různých úrovní s mnoha dceřinými páry klíčů, které lze všechny obnovit znalostí pouze základních informací pro obnovu (mnemonická fráze a jakékoli potenciální heslo). Pro odvození dceřiného klíče se používá funkce `HMAC-SHA512` s rodičovským řetězovým kódem a konkatenací rodičovského klíče a 32bitového indexu. Existují dva typy odvození:
* Normální odvození, které používá jako základ funkce `HMAC-SHA512` rodičovský veřejný klíč;
* Zpevněné odvození, které používá jako základ funkce `HMAC-SHA512` rodičovský soukromý klíč;

Výsledek HMAC-SHA512 je rozdělen na dvě části: prvních 256 bitů se stává dceřiným klíčem (soukromým nebo veřejným po zpracování prostřednictvím ECDSA) a zbývajících 256 bitů se stává dceřiným řetězovým kódem.