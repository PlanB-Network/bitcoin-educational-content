---
term: PODPIS NIEWIDOMEGO
---

Ślepe podpisy Chauma są formą podpisu cyfrowego, w której wystawca podpisu nie zna treści podpisywanej wiadomości. Podpis można jednak później zweryfikować za pomocą oryginalnej wiadomości. Technika ta została opracowana przez kryptografa Davida Chauma w 1983 roku.


Rozważmy przykład firmy, która chce uwierzytelnić poufny dokument, taki jak Contract, bez ujawniania jego treści. Firma stosuje proces maskowania, który kryptograficznie przekształca oryginalny dokument w sposób odwracalny. Ten zmodyfikowany dokument jest wysyłany do urzędu certyfikacji, który stosuje ślepy podpis, nie znając jego treści. Po otrzymaniu zamaskowanego podpisanego dokumentu firma usuwa maskowanie podpisu. Rezultatem jest oryginalny dokument uwierzytelniony podpisem urzędu, bez jego wglądu w oryginalną treść.


Ślepe podpisy Chauma pozwalają zatem na poświadczenie autentyczności dokumentu bez znajomości jego treści, zapewniając zarówno poufność danych użytkownika, jak i integralność podpisanego dokumentu.


W Bitcoin protokół ten jest używany w systemach banków Chaumian jako nakładka (Cashu, Fedimint itp.), ale szczególnie w protokołach Chaumian CoinJoin, aby zapewnić, że koordynator nie jest w stanie połączyć wejścia z wyjściem.