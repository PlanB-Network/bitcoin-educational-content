---
term: HLUBKA
---

V kontextu HD (Hierarchicky Deterministických) peněženek se hlubka odkazuje na specifickou úroveň klíče (veřejného nebo soukromého), řetězového kódu, rozšířeného klíče nebo adresy v rámci struktury odvození peněženky od hlavního klíče. Každá úroveň této struktury může být vnímána jako patro ve stromu klíčů, kde hlavní klíč je u kořene (hlubka 0) a následující úrovně definují různé atributy, jako jsou:
účel (hlubka 1), typ měny (hlubka 2), účet (hlubka 3), typ řetězce (hlubka 4) a index specifické adresy (hlubka 5).

![](../../dictionnaire/assets/18.png)

Pro přechod z jedné hlubky na další se používá proces odvození z páru rodičovských klíčů na pár dětských klíčů.

> ► *Termín "patro odvození" je někdy také používán místo hlubky.*