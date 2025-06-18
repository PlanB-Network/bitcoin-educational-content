---
term: MINISCRIPT
---

Framework zaprojektowany w celu zapewnienia ram dla bezpiecznego programowania skryptów na Bitcoin. Natywnym językiem Bitcoin jest język skryptowy. W praktyce jest on dość skomplikowany w użyciu, zwłaszcza w przypadku zaawansowanych i niestandardowych aplikacji. Przede wszystkim bardzo trudno jest zweryfikować ograniczenia skryptu. Miniscript wykorzystuje podzbiór skryptów Bitcoin, aby uprościć ich tworzenie, analizę i weryfikację. Każdy miniskrypt jest równoważny 1 do 1 z natywnym skryptem. Używany jest przyjazny dla użytkownika język polityki, który jest następnie kompilowany do miniskryptu, aby ostatecznie odpowiadać natywnemu skryptowi.


![](../../dictionnaire/assets/30.webp)


Miniscript umożliwia programistom tworzenie zaawansowanych skryptów w bezpieczniejszy i bardziej niezawodny sposób. Podstawowe właściwości Miniscript są następujące:


- Pozwala to na statyczną analizę skryptu, w tym warunków wydawania, na które pozwala, oraz jego kosztu pod względem zasobów;
- Umożliwia tworzenie skryptów zgodnych z konsensusem;
- Pozwala to na analizę, czy różne ścieżki wydatków są zgodne ze standardowymi zasadami węzłów;
- Ustanawia ogólny standard, zrozumiały i możliwy do skomponowania, dla całego oprogramowania i sprzętu Wallet.


Projekt Miniscript został uruchomiony w 2018 roku przez Petera Wuille'a, Andrew Poelstrę i Sanketa Kanjalkara za pośrednictwem firmy Blockstream. Miniscript został dodany do Bitcoin Core Wallet w trybie watch-only w grudniu 2022 r. w wersji 24.0, a następnie w pełni w maju 2023 r. w wersji 25.0.