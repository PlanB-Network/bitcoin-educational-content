---
term: GŁĘBOKOŚĆ
---

W kontekście portfeli HD (Hierarchical Deterministic) głębokość odnosi się do konkretnego poziomu klucza (publicznego lub prywatnego), kodu łańcucha, klucza rozszerzonego lub Address w strukturze wyprowadzania Wallet z klucza głównego. Każdy poziom tej struktury może być postrzegany jako piętro w drzewie kluczy, gdzie klucz główny znajduje się w korzeniu (głębokość 0), a kolejne poziomy definiują różne atrybuty, takie jak:

cel (głębokość 1), typ waluty (głębokość 2), konto (głębokość 3), typ łańcucha (głębokość 4) i indeks konkretnego Address (głębokość 5).


![](../../dictionnaire/assets/18.webp)


Aby przejść z jednej głębokości do następnej, wykorzystywany jest proces derywacji z pary kluczy nadrzędnych do pary kluczy podrzędnych.


> określenie "dno derywacji" jest czasami używane zamiast głębokości