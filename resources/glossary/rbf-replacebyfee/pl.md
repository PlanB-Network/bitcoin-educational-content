---
term: RBF (Replace-by-fee)
---

Mechanizm transakcyjny, który pozwala nadawcy zastąpić jedną transakcję inną, płacąc wyższe opłaty, aby przyspieszyć jej potwierdzenie. Jeśli transakcja ze zbyt niskimi opłatami utknie, nadawca może użyć *Replace-by-fee*, aby zwiększyć opłaty i nadać priorytet transakcji zastępczej w mempoolach.


RBF ma zastosowanie tak długo, jak transakcja znajduje się w mempoolach; gdy znajdzie się w bloku, nie może być już zastąpiona. Podczas początkowego wysyłania, transakcja musi określić swoją dostępność do zastąpienia poprzez dostosowanie wartości `nSequence` do liczby mniejszej niż `0xfffffe`. Jest to znane jako "flaga" RBF. To ustawienie sygnalizuje możliwość aktualizacji transakcji po jej emisji, co następnie pozwala na RBF. Czasami jednak możliwe jest zastąpienie transakcji, która nie zasygnalizowała RBF. Węzły używające parametru konfiguracyjnego `mempoolfullrbf=1` akceptują takie zastąpienie, nawet jeśli RBF nie został początkowo zasygnalizowany.


W przeciwieństwie do CPFP (*Child Pays For Parent*), gdzie odbiorca może działać w celu przyspieszenia transakcji, RBF (*Replace-by-fee*) pozwala nadawcy przejąć inicjatywę w celu przyspieszenia własnej transakcji poprzez zwiększenie opłat.