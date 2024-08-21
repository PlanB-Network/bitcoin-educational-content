---
termi: VAIKEUSASTEEN SÄÄTÖ
---

Vaikeusasteen säätö on säännöllisesti toistuva prosessi, joka määrittelee uudelleen vaikeustavoitteen Bitcoinin proof of work -mekanismille (louhinta). Tämä tapahtuma tapahtuu joka 2016 lohkon jälkeen (noin joka toinen viikko). Sen tarkoituksena on lisätä tai vähentää vaikeuskerrointa (jota kutsutaan myös vaikeustavoitteeksi), riippuen siitä, kuinka nopeasti viimeiset 2016 lohkoa löydettiin. Säädön tavoitteena on ylläpitää vakaa ja ennustettava lohkojen tuotantonopeus, yhden lohkon taajuudella joka 10. minuutti, huolimatta louhijoiden käyttämän laskentatehon vaihteluista. Vaikeusasteen muutos säädön aikana on rajoitettu tekijään 4. Solmujen suorittama kaava uuden tavoitteen laskemiseksi on seuraava:
$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$
&nbsp;
Missä:
* $N$: Uusi tavoite;
* $A$: Edellisten 2016 lohkon vanha tavoite;
* $T$: Viimeisten 2016 lohkon kokonaisaika sekunteina;
* $1,209,600$: Tavoiteltu aika sekunteina tuottaa 2016 lohkoa 10 minuutin välein kunkin lohkon välillä.

> ► *Ranskaksi termiä "reciblage" käytetään joskus myös viittaamaan säätöön. Englanniksi sitä kutsutaan "Difficulty Adjustment" eli vaikeusasteen säädöksi.*