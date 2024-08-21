---
term: HASHOVACÍ FUNKCE
---

Matematická funkce, která přijímá vstup proměnné velikosti (nazývaný zpráva) a produkuje výstup pevné velikosti (nazývaný hash, hašování, digest nebo otisk). Hashovací funkce jsou široce používané primitiva v kryptografii. Vyžadují specifické vlastnosti, které je činí vhodnými pro použití v bezpečných kontextech:
* Odolnost vůči nalezení původního obrazu: musí být velmi obtížné najít zprávu, která produkuje specifický hash, tj. najít původní obraz $m$ pro hash $h$ tak, že $h = H(m)$, kde $H$ je hashovací funkce;
* Odolnost vůči nalezení druhého obrazu: pro danou zprávu $m_1$ musí být velmi obtížné najít jinou zprávu $m_2$ (odlišnou od $m_1$), tak, že $H(m_1) = H(m_2)$;
* Odolnost vůči kolizím: musí být velmi obtížné najít dvě rozdílné zprávy $m_1$ a $m_2$ tak, že $H(m_1) = H(m_2)$;
* Odolnost vůči manipulaci: malé změny ve vstupu musí způsobit významné a nepředvídatelné změny ve výstupu.

V kontextu Bitcoinu jsou hashovací funkce používány pro několik účelů, včetně mechanismu důkazu práce (*Proof-of-Work*), identifikátorů transakcí, generování adres, výpočtů kontrolních součtů a vytváření datových struktur jako jsou Merkleovy stromy. Na protokolové úrovni Bitcoin výhradně používá funkci `SHA256d`, také nazývanou `HASH256`, která se skládá z dvojitého haše `SHA256`. `HASH256` je také používán při výpočtu určitých kontrolních součtů, zejména pro rozšířené klíče (`xpub`, `xprv`...). Na straně peněženky jsou také používány následující:
* Jednoduchý `SHA256` pro kontrolní součty mnemonických frází;
* `SHA512` v rámci algoritmů `HMAC` a `PBKDF2` používaných v procesu odvozování deterministických a hierarchických peněženek;
* `HASH160`, který popisuje postupné použití `SHA256` a `RIPEMD160`. `HASH160` je používán v procesu generování přijímacích adres (kromě P2PK a P2TR) a při výpočtu otisků rodičovských klíčů pro rozšířené klíče.

> ► *V angličtině se tomu říká "hash function".*