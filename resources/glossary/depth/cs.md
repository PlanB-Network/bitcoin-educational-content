---
term: DEPTH

---
V kontextu HD (Hierarchical Deterministic) peněženek se hloubka vztahuje na konkrétní úroveň klíče (veřejného nebo soukromého), řetězového kódu, rozšířeného klíče nebo adresy v rámci struktury peněženky odvozené od hlavního klíče. Každou úroveň této struktury si lze představit jako patro ve stromu klíčů, kde hlavní klíč je v kořeni (hloubka 0) a následující úrovně definují různé atributy, jako např:

účel (hloubka 1), typ měny (hloubka 2), účet (hloubka 3), typ řetězce (hloubka 4) a index konkrétní adresy (hloubka 5).

![](../../dictionnaire/assets/18.webp)

Pro přechod z jedné hloubky do druhé se používá proces odvození z dvojice nadřazených klíčů na dvojici podřazených klíčů.

> *Někdy se místo termínu hloubka používá také termín "odvozovací podlaha".*