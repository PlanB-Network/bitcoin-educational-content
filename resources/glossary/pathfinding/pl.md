---
term: PATHFINDING
---

Proces wykorzystywany przez węzeł w celu określenia optymalnej ścieżki kierowania płatności przez sieć kanałów Lightning. Wyznaczanie ścieżki jest przeprowadzane przez węzeł płatnika, który musi wybrać najbardziej odpowiednie węzły pośrednie, aby dotrzeć do odbiorcy. Wybór ten opiera się na szeregu kryteriów, takich jak opłaty, przepustowość kanału i blokady czasowe.


Algorytmy wyszukiwania ścieżek budują graf topologii sieci z danych plotek i oceniają różne możliwe trasy między węzłem płatnika i odbiorcy. Trasy te są uszeregowane od najlepszej do najgorszej według różnych kryteriów. Następnie węzeł testuje te trasy, aż uda mu się dokonać płatności na jednej z nich.