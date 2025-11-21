---
term: CICHE PŁATNOŚCI
---

Metoda wykorzystywania statycznych adresów Bitcoin do otrzymywania płatności bez ponownego wykorzystywania Address, bez interakcji i bez widocznego powiązania On-Chain między różnymi płatnościami a statycznym Address. Technika ta eliminuje potrzebę generate nowych, nieużywanych adresów odbiorczych dla każdej transakcji, unikając w ten sposób zwykłych interakcji w Bitcoin, w których odbiorca musi dostarczyć nowy Address płatnikowi.


W przypadku cichych płatności płatnik wykorzystuje klucze publiczne odbiorcy (klucz publiczny wydawania i klucz publiczny skanowania) oraz sumę własnych kluczy prywatnych jako dane wejściowe do generate nowego Address dla każdej płatności. Tylko odbiorca, za pomocą swoich kluczy prywatnych, może obliczyć klucz prywatny odpowiadający tej płatności Address. ECDH (*Elliptic-Curve Diffie-Hellman*), algorytm Exchange klucza kryptograficznego, jest używany do ustanowienia wspólnego sekretu, który jest następnie używany do wyprowadzenia otrzymanego Address i klucza prywatnego (tylko po stronie odbiorcy). Aby zidentyfikować przeznaczone dla nich ciche płatności, odbiorcy muszą zeskanować Blockchain i sprawdzić każdą transakcję spełniającą kryteria protokołu. W przeciwieństwie do BIP47, który wykorzystuje transakcję powiadomienia do ustanowienia kanału płatności, Silent Payments eliminuje ten krok, oszczędzając transakcję. Kompromis polega jednak na tym, że odbiorca musi przeskanować wszystkie potencjalne transakcje, aby ustalić, stosując ECDH, czy są one do niego adresowane.


Na przykład statyczny Address $B$ Boba reprezentuje konkatenację jego klucza publicznego skanowania i klucza publicznego wydawania:


$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$


Klucze te są po prostu wyprowadzane z następującej ścieżki:


```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```


Ten statyczny Address jest publikowany przez Boba. Alicja pobiera go, aby dokonać cichej płatności na rzecz Boba. Oblicza ona płatność Address $P_0$ Boba w ten sposób:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$


Gdzie:


$$ \text{inputHash} = \text{Hash}(\text{outpoint}_L \text{ ‖ } A) $$


Z:


- $B_{\text{scan}}$: klucz publiczny skanu Boba (statyczny Address);
- $B_{\text{spend}}$: klucz publiczny Boba (statyczny Address);
- $A$: Suma kluczy publicznych na wejściu (tweak);
- $a$: Klucz prywatny tweaku, czyli suma wszystkich par kluczy użytych w `scriptPubKey` UTXO wykorzystanych jako dane wejściowe w transakcji Alicji;
- $\text{outpoint}_L$: Najmniejszy UTXO (leksykograficznie) użyty jako dane wejściowe w transakcji Alicji;
- $\text{ ‖ }$: Konkatenacja (operacja łączenia operandów od końca do końca);
- $G$: Punkt generatora krzywej eliptycznej `secp256k1`;
- $\text{Hash}$: Funkcja SHA256 Hash oznaczona tagiem `BIP0352/SharedSecret`;
- $P_0$: Pierwszy klucz publiczny / unikalny Address do płatności na rzecz Boba;
- $0$: Liczba całkowita używana do generate wielu unikalnych adresów płatności.


Bob skanuje Blockchain, aby znaleźć swoją cichą płatność w ten sposób:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$


Z:


- $b_{\text{scan}}$: prywatny klucz skanowania Boba.


Jeśli znajdzie $P_0$ jako Address zawierający cichą płatność zaadresowaną do niego, obliczy $p_0$, klucz prywatny pozwalający mu wydać środki wysłane przez Alice do $P_0$:


$$ p_0 = (b_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \mod n $$


Z:


- $b_{\text{spend}}$: prywatny klucz wydatków Boba;
- $n$: rząd krzywej eliptycznej `secp256k1`.


Oprócz tej podstawowej wersji, etykiety mogą być również używane do generate kilku różnych adresów statycznych z tego samego podstawowego statycznego Address, w celu oddzielenia wielu zastosowań bez nieuzasadnionego zwielokrotnienia pracy wymaganej podczas skanowania.