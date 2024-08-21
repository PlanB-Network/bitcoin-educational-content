---
term: TWEAK (AVALIK VÕTI)
---

Krüptograafia valdkonnas tähendab avaliku võtme "tweakimine" selle võtme muutmist, kasutades lisandväärtust, mida nimetatakse "tweakiks", nii et see jääb kasutatavaks teades algset privaatvõtit ja tweaki. Tehniliselt on tweak skalaarväärtus, mis lisatakse algsele avalikule võtmele. Kui $P$ on avalik võti ja $t$ on tweak, siis muudetud avalik võti saab olema:

$$
P' = P + tG
$$

Kus $G$ on kasutatava elliptilise kõvera generaator. See toiming võimaldab saada uue avaliku võtme, mis on tuletatud algsest võtmest, säilitades samal ajal teatud krüptograafilised omadused, mis teevad selle kasutatavaks. Näiteks kasutatakse seda meetodit Taproot aadresside (P2TR) jaoks, mis võimaldavad kulutamist kas esitades Schnorri allkirja traditsioonilisel viisil või täites ühe tingimustest, mis on öeldud Merkle puus, mida nimetatakse ka "MASTiks".

![](../../dictionnaire/assets/26.png)