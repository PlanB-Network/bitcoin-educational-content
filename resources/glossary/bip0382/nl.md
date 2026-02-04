---
term: BIP0382
definition: wpkh() en wsh() functies voor het beschrijven van SegWit scripts in descriptors.
---

Introduceert de functies `wpkh(KEY)` (Pay-to-Witness-PubKey-Hash) en `wsh(SCRIPT)` (Pay-to-Witness-Script-Hash) voor descriptors. Deze functies standaardiseren de manier om SegWit scripttypes te beschrijven in descriptors. BIP382 is geïmplementeerd samen met alle andere Descriptor-gerelateerde BIP's (behalve BIP386) in versie 0.17 van Bitcoin core.