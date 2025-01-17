---
term: BECH32 JA BECH32M

---
`Bech32` ja `Bech32m` on kaks aadressi kodeerimise formaati bitcoinide vastuvõtmiseks. Need põhinevad pisut modifitseeritud baasil 32. Need sisaldavad kontrollsummat, mis põhineb veakorrektsioonialgoritmil nimega BCH (*Bose-Chaudhuri-Hocquenghem*). Võrreldes Legacy-aadressidega, mis on kodeeritud `Base58check`, on `Bech32` ja `Bech32m` aadressidel tõhusam kontrollsumma, mis võimaldab tuvastada ja potentsiaalselt automaatselt parandada kirjavigu. Nende formaat on ka paremini loetav, kuna kasutatakse ainult väikseid tähemärke. Siin on selle formaadi liitmismaatriks baasist 10:

&nbsp;

| + | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

| --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 0 | q | p | z | r | y | 9 | x | 8 |

| 8 | g | f | 2 | t | v | d | w | 0 |

| 16 | s | 3 | j | n | 5 | 4 | k | h |

| 24 | c | e | 6 | m | u | a | 7 | l |

&nbsp;

Bech32 ja Bech32m on kodeerimisformaadid, mida kasutatakse SegWit-aadresside esitamiseks. Bech32 on aadressi kodeerimisformaat, mille võttis kasutusele BIP173 2017. aastal. See kasutab numbritest ja väiketähtedest koosnevat spetsiifilist tähemärkide kogumit, et vähendada trükivigu ja hõlbustada lugemist. Bech32-aadressid algavad tavaliselt sõnaga `bc1`, mis näitab, et need on SegWitile omased. Seda formaati kasutatakse ainult SegWit V0-aadressidel koos skriptidega P2WPKH (Pay to Witness Public Key Hash) ja P2WSH (Pay to Witness Script Hash). Siiski on Bech32-vormingule omane väike ootamatu viga. Kui aadressi viimane märk on "p", siis sellele vahetult eelnevate "q" märkide lisamine või eemaldamine ei muuda kontrollsummat kehtetuks. See ei mõjuta SegWit V0 aadresside (BIP173) olemasolevaid kasutusviise, kuna need on piiratud kahe kindlaksmääratud pikkusega. See võib aga mõjutada Bech32 kodeeringu tulevast kasutamist. Bech32m-vorming on lihtsalt Bech32-vorming, milles see viga on parandatud. See võeti kasutusele koos BIP350-ga 2020. aastal. Bech32m-aadressid algavad samuti `bc1`-ga, kuid need on spetsiaalselt loodud ühilduma SegWit V1 (Taproot) ja hilisemate versioonidega, skriptiga P2TR (Pay to TapRoot).