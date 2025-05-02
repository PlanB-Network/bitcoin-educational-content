---
term: SHARDS (RGB)
---

W kontekście protokołu RGB, Shard reprezentuje odrębną gałąź w acyklicznym grafie skierowanym (DAG), który śledzi historię przejść stanu Contract. Stanowi ona spójny podzbiór zbioru przejść, odpowiadający na przykład sekwencji operacji wymaganych do poświadczenia ważności określonego zasobu od Genesis. Mechanizm ten umożliwia wyodrębnienie określonych segmentów ogólnej historii w celu ułatwienia weryfikacji po stronie klienta.