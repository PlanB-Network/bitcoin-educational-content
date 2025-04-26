---
term: OP_HASH256 (0XAA)

---
Vezme vrchní položku ze zásobníku a nahradí ji jejím hashem pomocí funkce `SHA256` dvakrát. Vstup je jednou zaheslován pomocí `SHA256` a poté je digest podruhé zaheslován pomocí `SHA256`. Tento dvoufázový proces vytvoří 256bitový otisk prstu.