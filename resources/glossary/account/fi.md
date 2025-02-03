---
term: ACCOUNT

---
HD-lompakoissa (Hierarchical Deterministic) tili edustaa BIP32:n mukaan 3. syvyyskerroksen johdannaiskerrosta. Kukin tili numeroidaan juoksevasti alkaen `/0'/` (kovennettu derivointi, eli todellisuudessa `/2^31/` tai `/2 147 483 648/`). Tässä johdannaiskerroksessa sijaitsevat tunnetut `xpubs`. Nykyään HD-lompakossa käytetään yleensä vain yhtä tiliä. Alun perin ne kuitenkin suunniteltiin erottelemaan eri käyttöluokat saman lompakon sisällä. Jos esimerkiksi otamme ulkoisen Taproot-vastaanottoosoitteen (P2TR) tavallisen johdannaispolun: `m/86'/0'/0'/0'/0/0`, tili-indeksi on toinen `/0'/`.

![](../../dictionnaire/assets/17.webp)