---
term: BLOCKS/REV*.DAT
---

Nimi failidele Bitcoin Core'is, mis talletavad vajaliku informatsiooni, et potentsiaalselt tagasi pöörata muudatused, mis on tehtud UTXO komplektis eelnevalt lisatud plokkide poolt. Iga fail on identifitseeritud unikaalse numbriga, mis on sama mis vastaval blk*.dat failil. Rev*.dat failid sisaldavad tagasipööramise andmeid, mis vastavad blk*.dat failides talletatud plokkidele. See andmestik on sisuliselt nimekiri kõikidest UTXO-dest, mis on kulutatud sisenditena plokis. Need tagasipööramise failid võimaldavad noodil naasta eelmisesse seisundisse juhul, kui plokiahela ümberkorraldamine põhjustab varem valideeritud plokkide hülgamise.