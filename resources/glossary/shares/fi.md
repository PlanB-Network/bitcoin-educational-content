---
term: OSAKKEET

---
Kaivospoolien yhteydessä osuus on indikaattori, jota käytetään määrittämään yksittäisen kaivosmiehen osuus poolista. Tämän mittarin perusteella lasketaan palkkio, jonka pooli jakaa uudelleen kullekin louhijalle. Kukin osuus vastaa hashia, joka täyttää vaikeustavoitteen, joka on alhaisempi kuin Bitcoin-verkon vaikeustavoite.

Selittääksesi asian vertauskuvalla, ajattele 20-sivuista noppaa. Oletetaan, että Bitcoinin osalta työn todistaminen edellyttää, että lohkon validoimiseksi on heitettävä numeroa, joka on pienempi kuin 3 (eli saavutettava tulos 1 tai 2). Kuvittele nyt, että louhintapoolien sisällä osuuden vaikeustavoitteeksi on asetettu 10. Näin ollen poolin yksittäiselle louhijalle jokainen nopanheitto, jonka tulos on pienempi kuin 10, lasketaan kelvolliseksi osakkeeksi. Louhija välittää nämä osakkeet poolille saadakseen palkkionsa, vaikka ne eivät vastaisikaan kelvollista tulosta Bitcoin-lohkolle.

Jokaisen lasketun hashin osalta yksittäinen louhija voi kohdata kolme erilaista skenaariota:


- Jos hash-arvo on suurempi tai yhtä suuri kuin poolin asettama vaikeustavoite osakkeelle, tästä hash-arvosta ei ole hyötyä. Louhija vaihtaa sen jälkeen nonce-tietonsa yrittäessään uutta hash-määritystä: `hash > share > block`.
- Jos hash on pienempi kuin osakkeen vaikeustavoite, mutta suurempi tai yhtä suuri kuin Bitcoinin vaikeustavoite, tämä hash muodostaa kelvollisen osakkeen, joka ei kuitenkaan riitä lohkon validointiin. Louhija voi lähettää tämän hashin omalle poolilleen lunastaakseen osakkeeseen liittyvän palkkion: "share > hash > block".
- Jos hash on alhaisempi kuin Bitcoin-verkon vaikeustavoite, sitä pidetään sekä kelvollisena osuutena että kelvollisena lohkona. Louhija välittää tämän hashin pooliinsa, joka kiirehtii lähettämään sen Bitcoin-verkkoon. Tämä hash lasketaan myös louhijalle kelvolliseksi osakkeeksi: `jako > blokki > hash`.

![](../../dictionnaire/assets/32.webp)

Tätä jakojärjestelmää käytetään kunkin yksittäisen louhijan tekemän työn arvioimiseen poolin sisällä ilman, että kaikkia louhijan tuottamia hasheja tarvitsee laskea erikseen uudelleen, mikä olisi poolin kannalta täysin tehotonta.

Kaivospoolien avulla osakkeiden vaikeusastetta voidaan säätää verifiointikuorman tasapainottamiseksi ja sen varmistamiseksi, että jokainen louhija, olipa hän sitten pieni tai suuri, lähettää osakkeita noin muutaman sekunnin välein. Näin voidaan laskea tarkasti kunkin louhijan hashrate ja jakaa palkkiot valitun korvauslaskentamenetelmän (PPS, PPLNS, TIDES...) mukaisesti.

> ► *Ranskaksi "shares" voidaan kääntää "osa".*