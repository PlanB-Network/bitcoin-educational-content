---
term: MINISCRIPT
---

Framework navržený tak, aby poskytoval rámec pro bezpečné programování skriptů na Bitcoinu. Původní jazyk Bitcoinu se nazývá skript. V praxi je jeho použití poměrně složité, zejména pro sofistikované a přizpůsobené aplikace. Především je velmi obtížné ověřit omezení skriptu. Miniscript používá podmnožinu Bitcoinových skriptů, aby zjednodušil jejich tvorbu, analýzu a ověření. Každý miniscript je ekvivalentní 1 ku 1 s původním skriptem. Používá se uživatelsky přívětivý jazyk politik, který je poté zkompilován do miniscriptu, aby nakonec odpovídal původnímu skriptu.

![](../../dictionnaire/assets/30.png)

Miniscript tedy umožňuje vývojářům vytvářet sofistikované skripty bezpečnějším a spolehlivějším způsobem. Základní vlastnosti Miniscriptu jsou následující:
* Umožňuje statickou analýzu skriptu, včetně podmínek výdajů, které umožňuje, a jeho nákladů z hlediska zdrojů;
* Umožňuje vytváření skriptů, které se řídí konsensem;
* Umožňuje analýzu, zda různé cesty výdajů dodržují standardní pravidla uzlů;
* Stanovuje obecný standard, srozumitelný a komponovatelný, pro veškerý software a hardware peněženek.

Projekt Miniscript byl spuštěn v roce 2018 Peterem Wuille, Andrewem Poelstra a Sanketem Kanjalkarem prostřednictvím společnosti Blockstream. Miniscript byl přidán do peněženky Bitcoin Core v režimu pouze pro sledování v prosinci 2022 s verzí 24.0 a poté plně v květnu 2023 s verzí 25.0.