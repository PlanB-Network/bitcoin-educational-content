`Bech32` ja `Bech32m` on kaks aadressi kodeerimisformaati bitcoini vastuvõtmiseks. Need põhinevad veidi muudetud alusel 32. Nad sisaldavad kontrollsummat, mis põhineb veaparandusalgoritmil nimega BCH (*Bose-Chaudhuri-Hocquenghem*). Võrreldes Legacy aadressidega, mis on kodeeritud `Base58check` formaadis, on `Bech32` ja `Bech32m` aadressidel efektiivsem kontrollsumma, mis võimaldab tuvastada ja potentsiaalselt automaatselt parandada trükivigu. Nende formaat pakub ka paremat loetavust, kasutades ainult väiketähti. Siin on selle formaadi lisamismatriks aluselt 10:

&nbsp;

| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

&nbsp;
Bech32 ja Bech32m on kodeerimisformaadid, mida kasutatakse SegWit aadresside esitamiseks. Bech32 on aadressi kodeerimisformaadi, mille tutvustas BIP173 aastal 2017. See kasutab spetsiifilist tähemärkide komplekti, mis koosneb numbritest ja väiketähtedest, et minimeerida trükivigu ja hõlbustada lugemist. Bech32 aadressid algavad üldiselt `bc1`-ga, et näidata, et need on SegWitile omased. Seda formaati kasutatakse ainult SegWit V0 aadressidel, skriptidega P2WPKH (Pay to Witness Public Key Hash) ja P2WSH (Pay to Witness Script Hash). Siiski on Bech32 formaadis väike, ootamatu viga. Kui aadressi viimane tähemärk on `p`, siis sellele vahetult eelnevate `q` tähemärkide arvu lisamine või eemaldamine ei muuda kontrollsummat kehtetuks. See ei mõjuta SegWit V0 aadresside olemasolevat kasutust (BIP173) nende kahe määratletud pikkuse piirangu tõttu. Siiski võib see mõjutada Bech32 kodeerimise tulevasi kasutusviise. Bech32m formaat on lihtsalt Bech32 formaat selle veaga parandatud. See tutvustati BIP350-ga aastal 2020. Bech32m aadressid algavad samuti `bc1`-ga, kuid need on spetsiaalselt kavandatud olema ühilduvad SegWit V1 (Taproot) ja hilisemate versioonidega, skriptiga P2TR (Pay to TapRoot).