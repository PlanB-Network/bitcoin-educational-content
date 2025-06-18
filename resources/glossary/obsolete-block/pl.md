---
term: PRZESTARZAŁY (BLOK)
---

Odnosi się do bloku bez dzieci: ważny blok, ale wykluczony z głównego łańcucha Bitcoin. Występuje, gdy dwóch górników znajdzie ważny blok na tej samej wysokości łańcucha w krótkim okresie czasu i rozgłosi go w sieci. Węzły ostatecznie wybierają tylko jeden blok do włączenia do łańcucha, zgodnie z zasadą łańcucha z największą ilością zgromadzonej pracy, czyniąc inne "przestarzałymi". Proces prowadzący do wytworzenia przestarzałego bloku wygląda następująco:


- Dwóch górników znajduje ważny blok na tej samej wysokości łańcucha w krótkim odstępie czasu. Nazwijmy ich `Blok A` i `Blok B`;
- Każdy z nich transmituje swój blok do sieci węzłów Bitcoin. Każdy węzeł ma teraz 2 bloki na tej samej wysokości. Istnieją zatem dwa prawidłowe łańcuchy;
- Górnicy nadal szukają dowodów pracy dla kolejnych bloków, ale aby to zrobić, muszą koniecznie wybrać tylko jeden blok pomiędzy `Blokiem A` i `Blokiem B`, na którym będą wydobywać;
- Miner ostatecznie znajduje prawidłowy blok powyżej `Bloku B`. Nazwijmy go "Blok B+1";
- Rozgłaszają one `Block B+1` do węzłów sieci;
- Ponieważ węzły podążają za najdłuższym łańcuchem (z największą ilością zgromadzonej pracy), oszacują, że "łańcuch B" jest tym, za którym należy podążać;
- Porzucą `Blok A`, który nie jest już częścią głównego łańcucha. W ten sposób stał się on przestarzałym blokiem.


![](../../dictionnaire/assets/9.webp)


> w języku angielskim jest on określany jako "Stale Block". W języku francuskim można go również nazwać "bloc périmé" lub "bloc abandonné". Chociaż nie zgadzam się z tym użyciem, niektórzy bitcoinerzy używają terminu "bloc orphelin" w odniesieniu do tego, co w rzeczywistości jest przestarzałym blokiem