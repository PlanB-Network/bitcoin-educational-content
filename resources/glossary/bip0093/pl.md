---
term: BIP0093
---

Informacyjny BIP, który sugeruje standard zapisywania i przywracania seed hierarchicznego deterministycznego portfela (zgodnie z BIP32) przy użyciu tajnego udostępniania kluczy Shamira. Protokół ten definiuje format "codex32", który jest inspirowany formatem bech32, poprzez wprowadzenie ustrukturyzowanego ciągu składającego się z prefiksu, parametru progowego, identyfikatora, indeksu współdzielenia, ładunku i sumy kontrolnej (BCH). Metoda ta umożliwia podział seed na maksymalnie 31 udziałów, z których zdefiniowany próg (od 1 do 9) jest wymagany do pełnego odzyskania seed.