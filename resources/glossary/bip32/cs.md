---
term: BIP32

---
BIP32 zavedl koncept hierarchické deterministické peněženky (HD peněženka). Tento návrh umožňuje generovat hierarchii párů klíčů ze společného "master seedu" pomocí jednosměrných derivačních funkcí. Každý vygenerovaný pár klíčů může být sám rodičem dalších podřízených klíčů, čímž vytváří stromovou (hierarchickou) strukturu. Výhodou BIP32 je, že umožňuje spravovat více různých klíčových párů, přičemž k jejich regeneraci stačí uchovávat pouze jeden seed. Tato inovace zejména pomohla v boji proti problému opakovaného použití adres, který je závažný pro soukromí uživatelů. BIP32 také umožňuje vytvářet dílčí větve v rámci jedné peněženky, což usnadňuje její správu.