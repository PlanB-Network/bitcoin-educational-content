---
term: COINSWAP
---

Protokół tajnego transferu Ownership między użytkownikami. Metoda ta ma na celu przeniesienie posiadania bitcoinów z jednej osoby na drugą i odwrotnie, bez widoczności Exchange na Blockchain. Coinwap wykorzystuje inteligentne kontrakty do dokonywania transferu bez potrzeby zaufania między stronami.


Wyobraźmy sobie naiwny przykład (który nie działa) z Alice i Bobem. Alicja posiada 1 BTC zabezpieczony kluczem prywatnym $A$, a Bob również 1 BTC zabezpieczony kluczem prywatnym $B$. Teoretycznie mogliby Exchange swoje klucze prywatne za pośrednictwem zewnętrznego kanału komunikacyjnego, aby przeprowadzić tajny transfer. Ta naiwna metoda wiąże się jednak z wysokim ryzykiem pod względem zaufania. Nic nie stoi na przeszkodzie, aby Alicja zachowała kopię klucza prywatnego $A$ po Exchange i wykorzystała ją później do kradzieży bitcoinów, gdy klucz znajdzie się w rękach Boba. Co więcej, nie ma gwarancji, że Alicja nie otrzyma klucza prywatnego $B$ Boba i nigdy nie przekaże swojego klucza prywatnego $A$ w Exchange. Exchange opiera się zatem na nadmiernym zaufaniu między stronami i jest nieskuteczny w zapewnieniu bezpiecznego, tajnego transferu Ownership.


Aby rozwiązać te problemy i umożliwić wymianę monet między stronami, które sobie nie ufają, będziemy używać systemów Smart contract, które sprawiają, że Exchange jest "atomowy". Mogą to być HTLC (*Hash Time-Locked Contracts*) lub PTLC (*Point Time-Locked Contracts*). Te dwa protokoły działają w podobny sposób, wykorzystując system blokady czasowej, który zapewnia, że Exchange zostanie pomyślnie zakończony lub całkowicie anulowany, chroniąc w ten sposób integralność środków obu stron. Główna różnica między HTLC i PTLC polega na tym, że HTLC wykorzystuje hashe i obrazy wstępne do zabezpieczenia transakcji, podczas gdy PTLC wykorzystuje podpisy adaptera.


W scenariuszu wymiany monet przy użyciu HTLC lub PTLC między Alicją i Bobem, Exchange odbywa się w bezpieczny sposób: albo się powiedzie i każdy otrzyma BTC drugiej strony, albo się nie powiedzie i każdy zatrzyma swój własny BTC. Dzięki temu żadna ze stron nie może oszukać ani ukraść BTC drugiej strony.


Wykorzystanie podpisów adaptera jest szczególnie interesujące w tym kontekście, ponieważ umożliwia rezygnację z tradycyjnych skryptów (mechanizm czasami określany jako "skrypty bezskryptowe"). Zmniejsza to koszty związane z Exchange. Inną ważną zaletą podpisów adaptacyjnych jest to, że nie wymagają one użycia wspólnego Hash dla obu stron transakcji, co pozwala uniknąć konieczności ujawniania bezpośredniego połączenia między nimi w niektórych typach Exchange.