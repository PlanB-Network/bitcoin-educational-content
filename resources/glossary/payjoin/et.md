---
term: PAYJOIN

---
Konkreetne Bitcoini tehingu struktuur, mis suurendab kasutaja privaatsust kulutuste ajal, tehes koostööd makse saajaga. Payjoini ainulaadsus seisneb selles, et ta suudab luua tehingu, mis esmapilgul näeb välja tavaline, kuid on tegelikult kahe osapoole vaheline mini coinjoin. Selleks kaasab tehingu struktuur sisenditesse makse saaja koos tegeliku saatjaga. Seega sisaldab saaja tehingu keskel ka iseendale tehtud makse, mis võimaldab talle maksta. Näiteks kui te ostate baguette'i 6 000 sati eest, kasutades 10 000 sati UTXO-d ja valite Payjoin'i, lisab teie pagar sisendina talle kuuluva 15 000 sati UTXO-d, mille ta lisaks teie 6 000 sati-le täies mahus väljundina tagasi saab.

Payjoini tehing täidab kaks eesmärki. Esiteks on selle eesmärk eksitada välist vaatlejat, luues ahelanalüüsis ühise sisendi omandiõiguse heuristikal (CIOH) põhineva peibutussüsteemi. Tavaliselt, kui tehingul on plokiahelas mitu sisendit, eeldatakse, et kõik need sisendid kuuluvad tõenäoliselt samale üksusele. Seega, kui analüütik uurib Payjoini tehingut, usutakse, et kõik sisendid pärinevad samalt isikult. See arusaam on aga vale, sest lisaks tegelikule maksjale panustab sisenditesse ka makse saaja. Teiseks petab Payjoin ka välist vaatlejat tehtud makse tegeliku summa osas. Tehingu struktuuri uurides võib analüütik arvata, et makse on võrdne ühe väljundi summaga. Tegelikkuses ei vasta makse summa ühelegi väljundile. See on tegelikult erinevus saaja UTXO väljundi ja saaja UTXO sisendi vahel. Sellega langeb Payjoini tehing steganograafia valdkonda. See võimaldab varjata tehingu tegelikku summat valetehingu sisse, mis toimib peibutajana.

![](../../dictionnaire/assets/14.webp)

> ► *Payjoin'i nimetatakse mõnikord ka "P2EP (Pay-to-End-Point)", "Stowaway" või "steganograafiline tehing"