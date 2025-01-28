---
term: HASHCASH

---
HashCash on Adam Backin vuonna 1997 suunnittelema proof-of-work-järjestelmä roskapostin ja DoS-hyökkäysten torjumiseksi. Se perustuu periaatteeseen, jonka mukaan lähettäjän on suoritettava laskutehtävä (erityisesti löydettävä osittainen törmäys kryptografisessa hash-funktiossa) todistaakseen työnsä. Tehtävä on lähettäjälle aikaa ja energiaa vievä, mutta vastaanottaja voi todentaa tuloksen nopeasti ja yksinkertaisesti. Tämä protokolla on osoittautunut erityisen sopivaksi roskapostin torjuntaan sähköpostiviestinnässä, sillä se on mahdollisimman vähän rasittavaa laillisille käyttäjille ja muodostaa samalla merkittävän esteen roskapostittajille. Yhden sähköpostiviestin lähettäminen vaatii muutaman sekunnin laskennan, mutta tämän operaation toistaminen miljoonia kertoja tulee erittäin kalliiksi energian ja ajan suhteen, mikä usein mitätöi roskapostikampanjoiden taloudelliset edut, olivatpa ne sitten markkinointitarkoituksessa tai ilkivaltaisia. Lisäksi se mahdollistaa lähettäjän anonymiteetin säilyttämisen.

HashCashin ottivat nopeasti käyttöön salakirjoittajat, jotka halusivat kehittää anonyymin sähköisen valuuttajärjestelmän ilman välikäsiä. Adam Backin innovaatio tosiaankin toi ensimmäistä kertaa niukkuuden käsitteen digitaaliseen maailmaan. Proof of Work -käsite on sittemmin ollut esillä useissa Bitcoinia edeltäneissä sähköisissä valuuttajärjestelmissä, kuten mm:


- wei Dain vuonna 1998 julkaisema b-money;
- Hal Finneyn vuonna 2004 julkaisema R-POW;
- Nick Szabon vuonna 2005 julkaisema BitGold.

HashCash-periaate on myös Bitcoin-protokollassa, jossa sitä käytetään suojausmekanismina Sybil-hyökkäyksiä vastaan.