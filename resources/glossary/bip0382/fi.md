---
term: BIP0382

definition: wpkh() ja wsh() -funktiot SegWit-skriptien kuvaamiseen deskriptoreissa.
---
Otetaan käyttöön funktiot `wpkh(KEY)` (Pay-to-Witness-PubKey-Hash) ja `wsh(SCRIPT)` (Pay-to-Witness-Script-Hash) kuvaajia varten. Nämä funktiot standardoivat tavan kuvata SegWit-skriptityyppejä kuvaajissa. BIP382 toteutettiin yhdessä kaikkien muiden kuvaajiin liittyvien BIP:ien kanssa (paitsi BIP386) Bitcoin Coren versiossa 0.17.