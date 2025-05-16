---
term: LNURL
---

Kommunikatsiooniprotokoll, mis määrab kindlaks hulga funktsioone, mis on mõeldud Lightning-sõlmede ja klientide ning kolmandate osapoolte rakenduste vahelise suhtluse lihtsustamiseks. See protokoll põhineb HTTP-l ja võimaldab luua linke erinevate toimingute jaoks, näiteks maksetaotluse, väljavõtmistaotluse või muude kasutajakogemust parandavate funktsioonide jaoks. Iga LNURL on bech32-koodiga kodeeritud URL, mille eesliide on `lnurl` ja mis skaneerimisel käivitab Lightning Wallets rea automaatseid toiminguid.


Näiteks LNURL-withdraw (LUD-03) võimaldab teil raha teenusest välja võtta, skaneerides QR-koodi, ilma et peaksite käsitsi generate ja Invoice kasutama. Või LNURL-auth (LUD-04) võimaldab teil parooli asemel ühendada end võrguteenustega, kasutades oma Lightning Wallet privaatvõtit.