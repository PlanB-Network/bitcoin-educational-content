---
term: KETJUKOODI

---
Bitcoin-lompakoiden hierarkkisen deterministisen (HD) derivaation yhteydessä ketjukoodi on 256-bittinen kryptografinen suola-arvo, jota käytetään BIP32-standardin mukaisesti lapsiavainten tuottamiseen vanhempien avaimista. Ketjukoodia käytetään yhdessä vanhemman avaimen ja lapsen indeksin kanssa uuden avainparin (yksityinen avain ja julkinen avain) deterministiseen tuottamiseen paljastamatta vanhemman avainta tai muita johdettuja lapsiavaimia.

Näin ollen jokaiselle avainparille on olemassa yksilöllinen ketjukoodi. Ketjukoodi saadaan joko hashtaamalla lompakon siemen ja ottamalla bittien oikea puolikas. Tällöin sitä kutsutaan master-ketjukoodiksi, joka liittyy master-yksityiseen avaimeen. Vaihtoehtoisesti se voidaan saada hashaamalla vanhempien avain sen vanhempien ketjukoodilla ja indeksillä ja pitämällä sitten oikeat bitit. Tätä kutsutaan tällöin lapsen ketjukoodiksi.

Avaimia on mahdotonta johtaa tuntematta kuhunkin vanhempien pariin liittyvää ketjukoodia. Se lisää johdantoprosessiin pseudosattuman, jotta varmistetaan, että kryptografisten avainten tuottaminen on hyökkääjille arvaamatonta ja lompakon haltijalle determinististä.

> ► *Englanniksi "code de chaîne" on "chain code" ja "code de chaîne maître" on "master chain code".*