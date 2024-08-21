---
termi: OP_CHECKSIGADD (0XBA)
---

Poimii pinon päältä kolme arvoa: `julkinen avain`, `CScriptNum` `n` ja `allekirjoitus`. Jos allekirjoitus ei ole tyhjä vektori ja on epäkelpo, skripti päättyy virheeseen. Jos allekirjoitus on kelpo tai on tyhjä vektori (`OP_0`), esitetään kaksi skenaariota:
* Jos allekirjoitus on tyhjä vektori: pinolle työnnetään `CScriptNum`, jonka arvo on `n`, ja suoritus jatkuu;
* Jos allekirjoitus ei ole tyhjä vektori ja pysyy kelpona: pinolle työnnetään `CScriptNum`, jonka arvo on `n + 1`, ja suoritus jatkuu.
Yksinkertaistaaksemme, `OP_CHECKSIGADD` suorittaa toiminnon, joka on samankaltainen kuin `OP_CHECKSIG`, mutta sen sijaan, että pinolle työnnettäisiin tosi tai epätosi, se lisää `1` toiseen arvoon pinon huipulla, jos allekirjoitus on kelpo, tai jättää tämän arvon muuttumattomaksi, jos allekirjoitus edustaa tyhjää vektoria. `OP_CHECKSIGADD` mahdollistaa samojen multisignatuuripolitiikkojen luomisen Tapscriptissa kuin `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY`, mutta erän verifioitavalla tavalla, mikä tarkoittaa, että se poistaa etsintäprosessin perinteisen multisigin verifioinnissa ja siten nopeuttaa verifiointia samalla vähentäen operatiivista kuormaa solmujen CPU:illa. Tämä operaatiokoodi lisättiin Tapscriptiin ainoastaan Taprootin tarpeisiin.