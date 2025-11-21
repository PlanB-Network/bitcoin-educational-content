---
term: TRANSAKCJA ZAMIANY
---

Wzorzec lub model transakcji stosowany w analizie łańcucha w celu określenia charakteru transakcji. Model ten charakteryzuje się konsumpcją pojedynczego UTXO jako wejścia i produkcją pojedynczego UTXO jako wyjścia. Interpretacja tego modelu jest taka, że mamy do czynienia z autotransferem. Użytkownik przeniósł swoje bitcoiny do siebie, do innego Address, którego jest właścicielem. Ponieważ w transakcji nie ma żadnej zmiany, jest bardzo mało prawdopodobne, że mamy do czynienia z płatnością. W rzeczywistości, gdy dokonywana jest płatność, prawie niemożliwe jest, aby płatnik posiadał UTXO, który dokładnie odpowiada kwocie wymaganej przez sprzedającego, oprócz opłat transakcyjnych. Ogólnie rzecz biorąc, płatnik jest zatem zmuszony do wytworzenia zmienionego wyniku. Wiemy wtedy, że obserwowany użytkownik prawdopodobnie nadal jest w posiadaniu tego UTXO. W kontekście analizy łańcucha, jeśli wiemy, że UTXO użyty jako dane wejściowe w transakcji należy do Alice, możemy założyć, że UTXO na wyjściu również należy do niej.


![](../../dictionnaire/assets/6.webp)


> w języku francuskim "sweep transaction" można przetłumaczyć jako "transaction de balayage"