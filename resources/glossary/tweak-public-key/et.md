---
term: TWEAK (AVALIK VÕTI)

---
Krüptograafia valdkonnas tähendab avaliku võtme "parendamine" selle võtme muutmist, kasutades lisaväärtust, mida nimetatakse "paranduseks", nii et see jääb kasutatavaks, kui on teada algne privaatne võti ja parandus. Tehniliselt on parandus skalaarne väärtus, mis lisatakse esialgsele avalikule võtmele. Kui $P$ on avalik võti ja $t$ on parandus, siis saab parandatud avalikuks võtmeks:

$$
P' = P + tG
$$

Kus $G$ on kasutatava elliptilise kõvera generaator. See operatsioon võimaldab saada uue avaliku võtme, mis on tuletatud algsest võtmest, säilitades samas teatavad krüptograafilised omadused, mis muudavad selle kasutatavaks. Näiteks kasutatakse seda meetodit Taproot-aadresside (P2TR) puhul, et võimaldada kulutusi kas Schnorr-allkirja esitamisega traditsioonilisel viisil või ühe Merkle-puu, mida nimetatakse ka "MAST", tingimuse täitmisega.

![](../../dictionnaire/assets/26.webp)