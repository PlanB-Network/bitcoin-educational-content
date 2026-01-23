---
term: Assume utxo
definition: Parametr Bitcoin Core umożliwiający szybką synchronizację nowego węzła przy użyciu snapshot zbioru UTXO założonego za poprawny, przed weryfikacją historii w tle.
---
Parametr konfiguracyjny w głównym kliencie Bitcoin Core, który umożliwia węzłowi, który właśnie został zainicjowany (ale nie przeprowadził jeszcze IBD), odroczenie weryfikacji transakcji i zestawu UTXO przed danym snapshotem. Koncepcja opiera się na wykorzystaniu zestawu UTXO (listy wszystkich istniejących UTXO w danym momencie) dostarczonego przez Core i uznanego za dokładny, co pozwala węzłowi na bardzo szybką synchronizację z łańcuchem o największej skumulowanej pracy. Ponieważ węzeł pomija długi etap IBD, staje się on bardzo szybko funkcjonalny dla użytkownika.

Assume UTXO dzieli synchronizację (IBD) na dwie części: Po pierwsze, węzeł wykonuje Header First Sync (tylko weryfikacja nagłówków) i uznaje zestaw UTXO dostarczony przez Core za ważny; Następnie, gdy już będzie funkcjonalny, węzeł sprawdzi pełną historię bloków w tle, aktualizując nowy zestaw UTXO, który sam zweryfikuje. Jeśli ten ostatni nie będzie zgadzał się z zestawem UTXO dostarczonym przez Core, wyświetli komunikat o błędzie.

Assume UTXO pozwala zatem przyspieszyć przygotowanie nowego węzła Bitcoin poprzez odroczenie procesu weryfikacji transakcji i zestawu UTXO dzięki zaktualizowanemu snapshotowi dostarczonemu w Core.







