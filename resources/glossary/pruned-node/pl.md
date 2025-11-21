---
term: PRZYCIĘTY WĘZEŁ
---

Przycięty węzeł, w języku angielskim "Pruned Node", to Full node, który wykonuje przycinanie Blockchain. Polega to na stopniowym usuwaniu najstarszych bloków, po ich należytej weryfikacji, aby zachować tylko najnowsze bloki. Limit retencji jest określony w pliku `Bitcoin.conf` poprzez parametr `prune=n`, gdzie `n` jest maksymalnym rozmiarem bloków w megabajtach (MB). Jeśli po tym parametrze podano `0`, przycinanie jest wyłączone, a węzeł zachowuje Blockchain w całości.


Przycięte węzły są czasami uważane za inne typy węzłów niż pełne węzły. Wykorzystanie przyciętego węzła może być szczególnie interesujące dla użytkowników borykających się z ograniczeniami pojemności pamięci masowej. Obecnie Full node musi mieć prawie 600 GB tylko do przechowywania Blockchain. Przycięty węzeł może ograniczyć wymaganą przestrzeń dyskową do 550 MB. Chociaż wykorzystuje mniej miejsca na dysku, przycięty węzeł utrzymuje poziom weryfikacji i walidacji podobny do Full node. Przycięte węzły oferują zatem większe zaufanie użytkownikom w porównaniu z lekkimi węzłami (SPV).