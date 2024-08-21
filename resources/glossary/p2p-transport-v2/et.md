---
term: P2P TRANSPORT V2
---

Bitcoin P2P transpordiprotokolli uus versioon, mis sisaldab juhuslikku krüpteerimist, et parandada sõlmede vahelise suhtluse privaatsust ja turvalisust. See täiustus on suunatud mitmete algse P2P protokolli probleemide lahendamisele, eriti muutes vahetatavad andmed passiivsele vaatlejale (näiteks internetiteenuse pakkujale) eristamatuks, vähendades seeläbi tsensuuri ja rünnakute riske, mis põhinevad andmepakettides kindlate mustrite tuvastamisel.

Rakendatud krüpteerimine ei hõlma autentimist, et vältida tarbetu keerukuse lisamist ja mitte ohustada võrguühenduse lubadevaba olemust. See uus P2P transpordiprotokoll pakub siiski paremat kaitset passiivsete rünnakute vastu ja muudab aktiivsed rünnakud oluliselt kallimaks ja tuvastatavamaks (eriti MITM-rünnakud). Pseudojuhusliku andmevoo kasutuselevõtt raskendab ründajate ülesannet, kes soovivad suhtlust tsenseerida või manipuleerida.

P2P Transport V2 lisati valikuna (vaikimisi välja lülitatud) Bitcoin Core versioonis 26.0, mis juurutati detsembris 2023. Seda saab aktiveerida konfiguratsioonifailis valikuga `v2transport=1`.