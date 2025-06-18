---
term: BECH32 NA BECH32M
---

`Bech32` na `Bech32m` ni aina mbili za usimbaji za Address za kupokea bitcoins. Zinatokana na msingi uliorekebishwa kidogo 32. Hujumuisha hundi kulingana na algorithm ya kusahihisha makosa inayoitwa BCH (*Bose-Chaudhuri-Hocquenghem*). Ikilinganishwa na anwani za Urithi, zilizosimbwa katika `Base58check`, anwani za `Bech32` na `Bech32m` zina ukaguzi bora zaidi, unaoruhusu ugunduzi na uwezekano wa kusahihisha makosa kiotomatiki. Umbizo lao pia hutoa usomaji bora, na herufi ndogo pekee. Hapa kuna matrix ya nyongeza ya umbizo hili kutoka msingi wa 10:


| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

Bech32 na Bech32m ni miundo ya usimbaji inayotumiwa kuwakilisha anwani za SegWit. Bech32 ni muundo wa usimbaji wa Address ulioanzishwa na BIP173 mwaka wa 2017. Inatumia seti maalum ya wahusika, inayojumuisha nambari na herufi ndogo, ili kupunguza makosa ya kuandika na kuwezesha kusoma. Kwa ujumla anwani za Bech32 huanza na `bc1` ili kuonyesha kwamba zina asili ya SegWit. Umbizo hili linatumika tu kwenye anwani za SegWit V0, pamoja na hati za P2WPKH (Pay to Shahidi Ufunguo wa Umma Hash) na P2WSH (Hati ya Lipa kwa Shahidi Hash). Hata hivyo, kuna dosari ndogo, isiyotarajiwa maalum kwa umbizo la Bech32. Wakati wowote herufi ya mwisho ya Address ni `p`, kuongeza au kuondoa idadi yoyote ya herufi `q` mara moja inayotangulia hakubatilishi hesabu. Hii haiathiri matumizi yaliyopo ya anwani za SegWit V0 (BIP173) kwa sababu ya kizuizi chao kwa urefu mbili zilizobainishwa. Walakini, hii inaweza kuathiri matumizi ya baadaye ya usimbaji wa Bech32. Umbizo la Bech32m ni umbizo la Bech32 tu na hitilafu hii imerekebishwa. Ilianzishwa na BIP350 mwaka wa 2020. Anwani za Bech32m pia huanza na `bc1`, lakini zimeundwa mahususi ili ziendane na SegWit V1 (Taproot) na matoleo ya baadaye, pamoja na hati ya P2TR (Lipa kwa Taproot).