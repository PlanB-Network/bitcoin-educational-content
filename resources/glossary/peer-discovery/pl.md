---
term: PEER DISCOVERY
---

Proces, za pomocą którego węzły w sieci Bitcoin łączą się z innymi węzłami w celu uzyskania informacji. Gdy węzeł Bitcoin jest uruchamiany po raz pierwszy, nie posiada żadnych informacji o innych węzłach w sieci. Musi jednak ustanowić połączenia, aby zsynchronizować się z Blockchain, który ma najwięcej zgromadzonej pracy. W celu wykrycia tych węzłów równorzędnych wykorzystywanych jest kilka mechanizmów, uporządkowanych według priorytetu:


- Węzeł zaczyna od sprawdzenia lokalnego pliku `peers.dat`, który przechowuje informacje o węzłach, z którymi wcześniej wchodził w interakcje. Jeśli węzeł jest nowy, plik ten będzie pusty, a proces przejdzie do następnego kroku;
- W przypadku braku informacji w pliku `peers.dat` (co jest normalne dla nowo uruchomionego węzła), węzeł wykonuje zapytania DNS do serwerów DNS. Serwery te dostarczają listę adresów IP przypuszczalnie aktywnych węzłów w celu nawiązania połączenia. Adresy serwerów DNS są zakodowane na stałe w kodzie Bitcoin Core. Ten krok jest zwykle wystarczający do ukończenia wykrywania węzłów równorzędnych;
- Jeśli nasiona DNS nie odpowiedzą w ciągu 60 sekund, węzeł może zwrócić się do węzłów seed. Są to publiczne węzły Bitcoin wymienione na statycznej liście prawie tysiąca wpisów zintegrowanych bezpośrednio z kodem źródłowym Bitcoin Core. Nowy węzeł użyje tej listy do nawiązania pierwszego połączenia z siecią i uzyskania adresów IP innych węzłów;
- W bardzo mało prawdopodobnym przypadku, gdy wszystkie poprzednie metody zawiodą, operator węzła zawsze ma możliwość ręcznego dodania adresów IP węzłów w celu nawiązania pierwszego połączenia.