---
term: BIP156
---

Ettepanek, mida tuntakse kui Dandelion, mille eesmärk on parandada tehingute marsruutimise privaatsust Bitcoin'i võrgus, et vastu seista deanonüümimisele. Bitcoin'i tavapärases toimimises levitatakse tehinguid kohe mitmele sõlmele. Kui vaatleja suudab näha iga tehingu edastamist igas võrgu sõlmes, võib ta eeldada, et esimene tehingu saatnud sõlm on ka selle tehingu lähtesõlm ja seega pärineb see sõlme operaatorilt. See nähtus võib potentsiaalselt võimaldada vaatlejatel seostada tehinguid, mis on tavaliselt anonüümsed, IP-aadressidega.

BIP156 eesmärk on see probleem lahendada. Selleks tutvustab see levitamisprotsessi lisafaasi, et säilitada anonüümsus enne avalikku levitamist. Seega kasutab Dandelion esmalt "vart" faasi, kus tehing saadetakse läbi juhusliku sõlmede tee, enne kui see levitatakse kogu võrgule "pahmakas" faasis. Vars ja pahmakas on viited tehingu leviku käitumisele võrgus, meenutades võilille kuju (*dandelion* inglise keeles).

See marsruutimismeetod varjab raja, mis viib tagasi lähtesõlmeni, muutes tehingu jälitamise võrgus tagasi selle alguspunkti keeruliseks. Dandelion parandab seega privaatsust, piirates vastaste võimet võrgu deanonüümida. See meetod on veelgi tõhusam, kui tehing ületab "vart" faasis sõlme, mis krüpteerib oma võrgusuhtluse, näiteks Tori või *P2P Transport V2* abil. BIP156 ei ole veel lisatud Bitcoin Core'i. 

![](../../dictionnaire/assets/36.png)