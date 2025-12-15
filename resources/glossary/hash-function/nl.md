---
term: Hash FUNCTIE
---

Een wiskundige functie die een invoer van variabele grootte neemt (een bericht genoemd) en een uitvoer van vaste grootte produceert (Hash, hashing, digest of vingerafdruk genoemd). Hash functies zijn veelgebruikte primitieven in cryptografie. Ze vertonen specifieke eigenschappen die ze geschikt maken voor gebruik in veilige contexten:


- Preimage-resistentie: het moet erg moeilijk zijn om een bericht te vinden dat een specifieke Hash produceert, d.w.z. om een preimage $m$ te vinden voor een Hash $h$ zodat $h = H(m)$, waarbij $H$ de Hash functie is;
- Tweede preimage weerstand: gegeven een bericht $m_1$, moet het heel moeilijk zijn om een ander bericht $m_2$ (verschillend van $m_1$) te vinden zodat $H(m_1) = H(m_2)$;
- Botsingsweerstand: het moet heel moeilijk zijn om twee verschillende berichten $m_1$ en $m_2$ te vinden zodat $H(m_1) = H(m_2)$;
- Sabotagebestendigheid: kleine veranderingen in de ingang moeten significante en onvoorspelbare veranderingen in de uitgang veroorzaken.


In de context van Bitcoin worden Hash functies gebruikt voor verschillende doeleinden, waaronder het Proof-of-Work mechanisme (*Proof-of-Work*), transactie identifiers, Address generatie, checksum berekeningen en het creëren van datastructuren zoals Merkle bomen. Aan de protocolzijde gebruikt Bitcoin uitsluitend de `SHA256d` functie, ook wel `HASH256` genoemd, die bestaat uit een dubbele `SHA256` Hash. `HASH256` wordt ook gebruikt bij de berekening van bepaalde checksums, met name voor uitgebreide sleutels (`xpub`, `xprv`...). Aan de Wallet kant worden ook de volgende gebruikt:


- Eenvoudige `SHA256` voor checksums van Mnemonic zinnen;
- `SHA512` binnen de `HMAC` en `PBKDF2` algoritmen die gebruikt worden in het proces om deterministische en hiërarchische wallets af te leiden;
- `HASH160`, dat een opeenvolgend gebruik beschrijft van een `SHA256` en een `RIPEMD160`. `HASH160` wordt gebruikt bij het genereren van ontvangstadressen (behalve P2PK en P2TR) en bij het berekenen van oudersleutel fingerprints voor uitgebreide sleutels.


> ► *In het Engels wordt het een "Hash functie" genoemd.*