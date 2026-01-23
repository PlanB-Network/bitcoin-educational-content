---
term: Anchors.dat
definition: Plik Bitcoin Core przechowujący adresy IP węzłów, z którymi klient był połączony przed zamknięciem, aby ułatwić ponowne połączenie po ponownym uruchomieniu.
---

Plik używany w kliencie Bitcoin Core do przechowywania adresów IP węzłów wychodzących, z którymi klient był połączony przed zamknięciem. Anchors.dat jest zatem tworzony za każdym razem, gdy węzeł jest zatrzymywany i usuwany po jego ponownym uruchomieniu. Węzły, których adresy IP znajdują się w tym pliku, są używane do szybkiego nawiązywania połączeń po ponownym uruchomieniu węzła.