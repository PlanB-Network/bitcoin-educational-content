---
term: VAIKEUKSIEN MUKAUTTAMINEN

---
Vaikeuden säätö on jaksottainen prosessi, jossa määritellään uudelleen Bitcoinin proof of work -mekanismin (louhinnan) vaikeustavoite. Tämä tapahtuma tapahtuu joka 2016 lohko (noin kahden viikon välein). Sen tarkoituksena on kasvattaa tai pienentää vaikeuskerrointa (jota kutsutaan myös vaikeustavoitteeksi) sen mukaan, kuinka nopeasti viimeiset 2016-lohkot löydettiin. Mukautuksella pyritään säilyttämään vakaa ja ennustettava lohkojen tuotantonopeus, joka on yksi lohko 10 minuutin välein, huolimatta louhijoiden käyttämän laskentatehon vaihteluista. Vaikeusasteen muutos säädön aikana on rajoitettu 4-kertaiseksi. Solmujen suorittama kaava uuden tavoitteen laskemiseksi on seuraava:

$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$$

&nbsp;

Missä:


- $N$: Uusi kohde;
- $A$: Viimeisen 2016 lohkon vanha tavoite;
- $T$: Viimeisten 2016 lohkon todellinen kokonaisaika sekunteina;
- $1,209,600$: Tavoiteaika sekunteina tuottaa 2016 lohkoa 10 minuutin välein.

> ► *Ranskan kielessä käytetään joskus myös termiä "reciblage", jolla viitataan säätöön. Englanniksi siitä käytetään nimitystä "Difficulty Adjustment".*