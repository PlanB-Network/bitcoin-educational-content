---
term: HASH FUNKCE

---
Matematická funkce, která přijímá vstup o proměnné velikosti (tzv. zprávu) a vytváří výstup o pevné velikosti (tzv. hash, hashování, digest nebo otisk prstu). Hašovací funkce jsou široce používanými primitivy v kryptografii. Vykazují specifické vlastnosti, díky nimž jsou vhodné pro použití v bezpečných kontextech:


- Odolnost proti předobrazu: musí být velmi obtížné najít zprávu, která vytváří určitý hash, tj. najít předobraz $m$ pro hash $h$ takový, že $h = H(m)$, kde $H$ je hashovací funkce;
- Druhá odolnost proti předobrazu: je-li dána zpráva $m_1$, musí být velmi obtížné najít jinou zprávu $m_2$ (odlišnou od $m_1$) tak, aby $H(m_1) = H(m_2)$;
- Odolnost proti kolizi: musí být velmi obtížné najít dvě různé zprávy $m_1$ a $m_2$ tak, aby $H(m_1) = H(m_2)$;
- Odolnost proti neoprávněné manipulaci: malé změny na vstupu musí způsobit výrazné a nepředvídatelné změny na výstupu.

V kontextu Bitcoinu se hashovací funkce používají k několika účelům, včetně mechanismu proof-of-work (*Proof-of-Work*), identifikátorů transakcí, generování adres, výpočtů kontrolních součtů a vytváření datových struktur, jako jsou Merklovy stromy. Na straně protokolu používá Bitcoin výhradně funkci `SHA256d`, nazývanou také `HASH256`, která se skládá z dvojitého hashe `SHA256`. funkce `HASH256` se používá také při výpočtu některých kontrolních součtů, zejména pro rozšířené klíče (`xpub`, `xprv`...). Na straně peněženky se používají také následující prvky:


- Jednoduchý `SHA256` pro kontrolní součty mnemotechnických frází;
- `SHA512` v rámci algoritmů `HMAC` a `PBKDF2` používaných při odvozování deterministických a hierarchických peněženek;
- `HASH160`, který popisuje postupné použití `SHA256` a `RIPEMD160`. `HASH160` se používá v procesu generování přijímacích adres (kromě P2PK a P2TR) a při výpočtu otisků nadřazených klíčů pro rozšířené klíče.

> ► V angličtině se označuje jako "hash function".*