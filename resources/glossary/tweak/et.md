---
term: TWEAK
---

Krüptograafias tähendab avaliku võtme "tweakimine" selle muutmist lisaväärtusega, mida nimetatakse "tweakiks", nii et see jääb kasutatavaks, kui on teada nii esialgne privaatne võti kui ka tweak. Tehniliselt on parandus skalaarne väärtus, mis lisatakse algsele avalikule võtmele. Kui $P$ on avalik võti ja $t$ on tweak, muutub tweakitud avalik võti :


$$
P' = P + tG
$$


Kus $G$ on kasutatava elliptilise kõvera generaator. Selle operatsiooni tulemuseks on uus avalik võti, mis on tuletatud algsest, säilitades samas teatavad krüptograafilised omadused, mis võimaldavad seda kasutada. Seda meetodit kasutatakse näiteks Taproot (P2TR) aadresside puhul, et võimaldada kulutusi kas traditsioonilisel viisil Schnorr'i allkirja esitamisega või ühe Merkle Tree tingimuse täitmisega, mida tuntakse ka "MAST" nime all.