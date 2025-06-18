---
term: POBIERANIE POCZĄTKOWEGO BLOKU (IBD)
---

Odnosi się do procesu, w którym węzeł pobiera i weryfikuje Blockchain z bloku Genesis oraz synchronizuje się z innymi węzłami w sieci Bitcoin. IBD musi zostać przeprowadzony podczas uruchamiania nowego Full node. Na początku tej początkowej synchronizacji węzeł nie ma informacji o poprzednich transakcjach. Dlatego pobiera każdy blok z innych węzłów w sieci, weryfikuje jego ważność, a następnie dodaje go do swojej lokalnej wersji Blockchain. Warto zauważyć, że IBD może być długotrwałe i wymagające dużej ilości zasobów ze względu na rosnący rozmiar zestawu Blockchain i UTXO. Szybkość jego wykonania zależy od możliwości obliczeniowych komputera hostującego węzeł, jego pojemności pamięci RAM, szybkości urządzenia pamięci masowej i przepustowości. Aby dać ci wyobrażenie, jeśli masz potężne połączenie internetowe, a węzeł jest hostowany na najnowszym MacBooku z dużą ilością pamięci RAM, IBD zajmie tylko kilka godzin. Z drugiej strony, jeśli używasz mikrokomputera, takiego jak Raspberry Pi, IBD może potrwać tydzień lub dłużej.


> w języku francuskim powszechnie przyjmuje się bezpośrednie odniesienie do IBD. Czasami używa się tłumaczenia "synchronisation initiale" lub "téléchargement initial des blocs"