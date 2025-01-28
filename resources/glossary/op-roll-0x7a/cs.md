---
term: OP_ROLL (0X7A)

---
Přesune položku ze zásobníku na jeho vrchol na základě hloubky určené hodnotou na vrcholu zásobníku před operací. Pokud je například hodnota na vrcholu zásobníku `4`, `OP_ROLL` vybere čtvrtou položku z vrcholu zásobníku a přesune ji na vrchol. funkce `OP_ROLL` plní stejnou funkci jako `OP_PICK` s tím rozdílem, že odstraní položku z její původní pozice.