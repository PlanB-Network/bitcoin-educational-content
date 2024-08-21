---
termi: CHAIN CODE
---

Hierarkkisen deterministisen (HD) Bitcoin-lompakoiden johdannaisuudessa ketjukoodi on 256-bittinen kryptografinen suolaa arvo, jota käytetään lapsiavainten luomiseen vanhemmasta avaimesta BIP32-standardin mukaisesti. Ketjukoodia käytetään yhdessä vanhemman avaimen ja lapsen indeksin kanssa deterministisesti uuden avainparin (yksityinen avain ja julkinen avain) luomiseen paljastamatta vanhempaa avainta tai muita johdettuja lapsiavaimia.

Näin ollen jokaisella avainparilla on ainutlaatuinen ketjukoodi. Ketjukoodi saadaan joko hashaamalla lompakon siemen ja ottamalla bittien oikea puoli. Tässä tapauksessa sitä kutsutaan pääketjukoodiksi, joka liittyy pääyksityisavaimen kanssa. Vaihtoehtoisesti se voidaan saada hashaamalla vanhempi avain sen vanhemman ketjukoodin ja indeksin kanssa, sitten pitämällä oikeat bitit. Tätä kutsutaan sitten lapsiketjukoodiksi.

Avainten johdattaminen ilman kunkin vanhemman parin yhteydessä olevaa ketjukoodia on mahdotonta. Se tuo pseudo-satunnaisia tietoja johdatusprosessiin varmistaakseen, että kryptografisten avainten luominen pysyy arvaamattomana hyökkääjille, samalla kun se on determinististä lompakon haltijalle.

> ► *Englanniksi "code de chaîne" kutsutaan "chain code":ksi, ja "code de chaîne maître" kutsutaan "master chain code":ksi.*