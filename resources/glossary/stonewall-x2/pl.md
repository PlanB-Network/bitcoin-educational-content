---
term: STONEWALL X2
---

Specyficzna forma transakcji Bitcoin mająca na celu zwiększenie prywatności użytkownika podczas wydatków poprzez współpracę z osobą trzecią niezaangażowaną w wydatki. Metoda ta symuluje mini-CoinJoin między dwoma uczestnikami, podczas dokonywania płatności na rzecz strony trzeciej. Transakcje Stonewall x2 są dostępne zarówno w aplikacji Samourai Wallet, jak i oprogramowaniu Sparrow Wallet (oba są interoperacyjne).


Jego działanie jest stosunkowo proste: wykorzystuje UTXO będący w naszym posiadaniu do dokonania płatności i szuka pomocy strony trzeciej, która również wnosi swój wkład za pomocą UTXO, który posiada. Transakcja kończy się czterema wyjściami: dwa z nich o równych kwotach, jeden przeznaczony dla Address odbiorcy płatności, drugi dla Address należącego do współpracownika. Trzeci UTXO jest wysyłany z powrotem do innego Address współpracownika, umożliwiając mu odzyskanie początkowej kwoty (działanie neutralne dla niego, pomniejszone o opłaty Mining), a ostatni UTXO wraca do Address, którego jesteśmy właścicielem, co stanowi zmianę z płatności. W ten sposób w transakcjach Stonewall x2 zdefiniowane są trzy różne role:


- Nadawca, który dokonuje skutecznej płatności;
- Współpracownik, który dostarcza bitcoiny, aby poprawić ogólną anonimowość transakcji, jednocześnie w pełni odzyskując swoje środki na koniec;
- Odbiorca, który może być nieświadomy konkretnego charakteru transakcji i po prostu oczekuje płatności od nadawcy.


![](../../dictionnaire/assets/3.webp)


Struktura Stonewall x2 dodaje dużo entropii do transakcji i utrudnia analizę łańcucha. Z zewnątrz taka transakcja może być interpretowana jako mały CoinJoin między dwiema osobami. Ale w rzeczywistości jest to płatność. Metoda ta generuje zatem niepewność w analizie łańcucha, a nawet prowadzi do fałszywych tropów. Nawet jeśli zewnętrznemu obserwatorowi uda się zidentyfikować schemat transakcji Stonewall x2, nie będzie on posiadał wszystkich informacji. Nie będzie w stanie określić, który z dwóch UTXO o równych kwotach odpowiada płatności. Co więcej, nie będą w stanie dowiedzieć się, kto dokonał płatności. Wreszcie, nie będą w stanie ustalić, czy dwa wejściowe UTXO pochodzą od dwóch różnych osób, czy też należą do jednej osoby, która je połączyła. Ten ostatni punkt wynika z faktu, że klasyczne transakcje Stonewall przebiegają dokładnie według tego samego schematu, co transakcje Stonewall x2. Z zewnątrz i bez dodatkowych informacji na temat kontekstu niemożliwe jest odróżnienie transakcji Stonewall od transakcji Stonewall x2. Jednak te pierwsze nie są transakcjami opartymi na współpracy, podczas gdy te drugie są. To jeszcze bardziej zwiększa wątpliwości co do wydatków.