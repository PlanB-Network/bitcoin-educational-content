---
term: MTP (MINEVIKU MEDIAAN)

---
Seda kontseptsiooni kasutatakse Bitcoini protokollis, et määrata võrgu konsensuse ajatempli marginaal. MTP on määratletud kui 11 viimase kaevandatud ploki ajatempli mediaan. Selle näitaja kasutamine aitab vältida lahknevuste korral sõlmede vahelisi lahkarvamusi täpse aja osas. MTP-d kasutati algselt selleks, et kontrollida plokkide ajatemplite kehtivust mineviku suhtes. Alates BIP113-st on seda kasutatud ka võrguaja võrdlusalusena, et kontrollida ajalukuga tehingute kehtivust (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` ja `OP_CHECKSEQUENCEVERIFY`).