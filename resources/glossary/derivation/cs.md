---
term: DERIVACE

---
Označuje proces generování podřízených párů klíčů z rodičovského páru klíčů (soukromý a veřejný klíč) a řetězového kódu v rámci deterministické a hierarchické (HD) peněženky. Tento proces umožňuje segmentaci větví a organizaci peněženky do různých úrovní s mnoha podřízenými páry klíčů, které lze všechny obnovit pouze se znalostí základních informací pro obnovu (mnemotechnická fráze a případná přístupová fráze). K získání podřízeného klíče se používá funkce `HMAC-SHA512` s kódem rodičovského řetězce a konkatenace rodičovského klíče a 32bitového indexu. Existují dva typy odvození:


- Normální odvození, které používá nadřazený veřejný klíč jako základ funkce `HMAC-SHA512`;
- Zpřísněná derivace, která používá nadřazený soukromý klíč jako základ funkce `HMAC-SHA512`;

Výsledek HMAC-SHA512 se rozdělí na dvě části: prvních 256 bitů se stane podřízeným klíčem (soukromým nebo veřejným po zpracování pomocí ECDSA) a zbývajících 256 bitů se stane podřízeným řetězovým kódem.