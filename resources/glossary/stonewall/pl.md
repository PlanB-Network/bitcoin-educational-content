---
term: STONEWALL
---

Specyficzna forma transakcji Bitcoin mająca na celu zwiększenie prywatności użytkownika podczas wydawania pieniędzy poprzez naśladowanie CoinJoin między dwiema osobami, bez faktycznego bycia jedną z nich. W rzeczywistości transakcja ta nie jest oparta na współpracy. Użytkownik może skonstruować ją samodzielnie, angażując tylko własne UTXO jako dane wejściowe. W związku z tym można utworzyć transakcję Stonewall na dowolną okazję, bez konieczności synchronizacji z innym użytkownikiem.


Działanie transakcji Stonewall jest następujące: na wejściu transakcji nadawca używa 2 UTXO, które do niego należą. Następnie transakcja generuje 4 wyjścia, z których 2 będą dokładnie taką samą kwotą. Pozostałe 2 będą stanowić zmianę. Spośród 2 wyjść o tej samej kwocie, tylko jedno faktycznie trafi do odbiorcy płatności.


W związku z tym w transakcji Stonewall występują tylko 2 role:


- Nadawca, który dokonuje faktycznej płatności;
- Odbiorca, który może być nieświadomy konkretnego charakteru transakcji i po prostu oczekuje płatności od nadawcy.


![](../../dictionnaire/assets/33.webp)

Transakcje Stonewall są dostępne zarówno w aplikacji Samourai Wallet, jak i oprogramowaniu Sparrow Wallet.


Struktura Stonewall dodaje dużo entropii do transakcji i zaciemnia ślad do analizy łańcucha. Z zewnątrz taka transakcja może być interpretowana jako mały CoinJoin między dwiema osobami. Ale w rzeczywistości, podobnie jak transakcja Stonewall x2, jest to płatność. Metoda ta generuje zatem niepewność w analizie łańcucha, a nawet prowadzi do fałszywych śladów. Nawet jeśli zewnętrzny obserwator zdoła zidentyfikować wzorzec transakcji Stonewall, nie będzie miał wszystkich informacji. Nie będzie w stanie określić, który z dwóch UTXO o tych samych kwotach odpowiada płatności. Co więcej, nie będą w stanie określić, czy dwa UTXO na wejściu pochodzą od dwóch różnych osób, czy też należą do jednej osoby, która je połączyła. Ten ostatni punkt wynika z faktu, że transakcje Stonewall x2 przebiegają dokładnie według tego samego schematu, co transakcje Stonewall. Z zewnątrz i bez dodatkowych informacji kontekstowych niemożliwe jest odróżnienie transakcji Stonewall od transakcji Stonewall x2. Jednak te pierwsze nie są transakcjami opartymi na współpracy, podczas gdy te drugie są. Dodaje to jeszcze więcej wątpliwości co do tego wydatku.