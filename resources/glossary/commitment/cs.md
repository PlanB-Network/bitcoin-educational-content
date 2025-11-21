---
term: Commitment
---

Commitment (v kryptografickém smyslu) je matematický objekt, označený $C$, odvozený deterministicky z operace na strukturovaných datech $m$ (zpráva) a náhodné hodnoty $r$. Píšeme :


$$
C = \text{commit}(m, r)
$$


Tento mechanismus zahrnuje dvě hlavní operace:




- Závazek: na zprávu $m$ a náhodnou hodnotu $r$ aplikujeme kryptografickou funkci a vytvoříme $C$ ;
- Ověření: Pomocí $C$, zprávy $m$ a hodnoty $r$ ověříme, zda je tento Commitment správný. Funkce vrací `Pravdu` nebo `Pravdu`.


Příkaz Commitment musí respektovat dvě vlastnosti:




- Vazba: musí být nemožné najít dvě různé zprávy, které by produkovaly stejné $C$ :


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Jako například :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Skrytí: znalost $C$ nesmí odhalit obsah $m$.


V případě protokolu RGB je do transakce Bitcoin začleněn protokol Commitment, který má prokázat existenci určité informace v daném čase, aniž by došlo k prozrazení informace samotné.