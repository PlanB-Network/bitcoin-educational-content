---
term: ASSUME UTXO
---

Parametr konfiguracyjny w wiodącym kliencie Bitcoin Core, który umożliwia węzłowi, który właśnie został zainicjowany (ale nie przeszedł jeszcze IBD), odroczenie weryfikacji transakcji i zestawu UTXO do określonej migawki. Koncepcja ta opiera się na wykorzystaniu zestawu UTXO (lista wszystkich istniejących UTXO w danym momencie) dostarczonego przez Core i zakładanego jako dokładny, co pozwala na bardzo szybką synchronizację węzła z łańcuchem o największej ilości zgromadzonej pracy. Ponieważ węzeł pomija długi krok IBD, bardzo szybko staje się operacyjny dla swojego użytkownika. Załóżmy, że UTXO dzieli synchronizację (IBD) na dwie części:


- Najpierw węzeł wykonuje Header First Sync (weryfikacja tylko nagłówków) i uznaje zestaw UTXO dostarczony przez Core za prawidłowy;
- Następnie, po uruchomieniu, węzeł zweryfikuje pełną historię bloków w tle, aktualizując nowy zestaw UTXO, który sam zweryfikował. Jeśli ten nowy zestaw UTXO nie pasuje do tego dostarczonego przez Core, wygeneruje komunikat o błędzie.


Dlatego załóżmy, że UTXO przyspiesza przygotowanie nowego węzła Bitcoin poprzez odroczenie procesu weryfikacji transakcji i zestawu UTXO poprzez zaktualizowaną migawkę dostarczoną w Core.