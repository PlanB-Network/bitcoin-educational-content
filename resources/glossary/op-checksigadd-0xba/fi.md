---
term: OP_CHECKSIGADD (0XBA)

---
Poimii pinosta kolme ylintä arvoa: `julkinen avain`, `CScriptNum` `n` ja `allekirjoitus`. Jos allekirjoitus ei ole tyhjä vektori eikä kelvoton, skripti päättyy virheeseen. Jos allekirjoitus on kelvollinen tai tyhjä vektori (`OP_0`), esitetään kaksi skenaariota:


- Jos allekirjoitus on tyhjä vektori: pinoon työnnetään `CScriptNum`, jonka arvo on `n`, ja suoritus jatkuu;
- Jos allekirjoitus ei ole tyhjä vektori ja se on edelleen voimassa: pinoon työnnetään `CScriptNum`, jonka arvo on `n + 1`, ja suoritus jatkuu.

Yksinkertaisuuden vuoksi `OP_CHECKSIGADD` suorittaa samanlaisen operaation kuin `OP_CHECKSIG`, mutta sen sijaan, että se työntäisi pinoon true- tai false-arvon, se lisää `1` pinon toisena olevaan arvoon, jos allekirjoitus on kelvollinen, tai jättää tämän arvon ennalleen, jos allekirjoitus edustaa tyhjää vektoria. `OP_CHECKSIGADD` mahdollistaa samojen monisignaattorikäytäntöjen luomisen Tapscriptissä kuin `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY`, mutta eräajona todennettavassa muodossa, mikä tarkoittaa, että se poistaa perinteisen monisignaattorikäytännön todentamiseen liittyvän hakuprosessin ja nopeuttaa siten todentamista vähentäen samalla solmujen suorittimien kuormitusta. Tämä op-koodi lisättiin Tapscriptiin yksinomaan Taprootin tarpeita varten.
