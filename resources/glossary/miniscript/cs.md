---
term: MINISCRIPT

---
Framework navržený tak, aby poskytoval rámec pro bezpečné programování skriptů na Bitcoinu. Nativní jazyk Bitcoinu se nazývá skript. Jeho použití v praxi je poměrně složité, zejména pro sofistikované a přizpůsobené aplikace. Především je velmi obtížné ověřit omezení skriptu. Miniscript používá podmnožinu skriptů Bitcoinu, aby zjednodušil jejich vytváření, analýzu a ověřování. Každý miniskript je ekvivalentní 1 za 1 s nativním skriptem. Používá se uživatelsky přívětivý jazyk zásad, který je následně zkompilován do miniskriptu, aby nakonec odpovídal nativnímu skriptu.

![](../../dictionnaire/assets/30.webp)

Miniscript tak umožňuje vývojářům vytvářet sofistikované skripty bezpečnějším a spolehlivějším způsobem. Základní vlastnosti Miniscriptu jsou následující:


- Umožňuje statickou analýzu skriptu, včetně podmínek, za kterých je možné jej utratit, a jeho nákladů z hlediska zdrojů;
- Umožňuje vytvářet skripty, které dodržují konsensus;
- Umožňuje analyzovat, zda různé cesty výdajů odpovídají standardním pravidlům uzlů;
- Zavádí obecný standard, který je srozumitelný a složitelný pro veškerý software a hardware peněženek.

Projekt Miniscript spustili v roce 2018 Peter Wuille, Andrew Poelstra a Sanket Kanjalkar prostřednictvím společnosti Blockstream. Miniscript byl přidán do peněženky Bitcoin Core v režimu pouze pro sledování v prosinci 2022 ve verzi 24.0 a poté plně v květnu 2023 ve verzi 25.0.