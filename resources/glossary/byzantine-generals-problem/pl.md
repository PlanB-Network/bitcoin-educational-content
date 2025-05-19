---
term: PROBLEM GENERAŁÓW BIZANTYJSKICH
---

Problem ten został po raz pierwszy sformułowany przez Leslie Lamporta, Roberta Shostaka i Marshalla Pease'a w specjalistycznym czasopiśmie *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) w lipcu 1982 roku. Jest on dziś używany do zilustrowania wyzwań w zakresie podejmowania decyzji, gdy system rozproszony nie może zaufać żadnemu aktorowi.


W tej metaforze grupa bizantyjskich generałów i ich armie obozują wokół miasta, które chcą zaatakować lub oblegać. Generałowie są geograficznie oddzieleni od siebie i muszą komunikować się za pośrednictwem posłańca, aby koordynować swoją strategię. To, czy zaatakują, czy się wycofają, nie ma znaczenia, o ile wszyscy generałowie osiągną konsensus.


Dlatego możemy rozważyć następujące wymagania:


- Każdy generał musi podjąć decyzję: atak lub odwrót (tak lub nie);
- Raz podjętej decyzji nie można zmienić;
- Wszyscy generałowie muszą uzgodnić tę samą decyzję i wykonać ją synchronicznie.


Co więcej, generał może komunikować się z innymi tylko za pośrednictwem wiadomości przesyłanych przez kuriera, które mogą zostać opóźnione, zniszczone, zmienione lub utracone. A nawet jeśli wiadomość zostanie pomyślnie dostarczona, jeden lub więcej generałów może zdecydować się (z jakiegokolwiek powodu) zdradzić ustanowione zaufanie i wysłać fałszywą wiadomość, siejąc chaos.


Stosując ten dylemat w kontekście Bitcoin Blockchain, każdy generał reprezentuje węzeł w sieci, który musi osiągnąć konsensus w sprawie stanu systemu. Innymi słowy, większość uczestników rozproszonej sieci musi zgodzić się i wykonać tę samą akcję, aby uniknąć całkowitej awarii. Jedynym sposobem na osiągnięcie konsensusu w tego typu systemie rozproszonym jest posiadanie co najmniej 2/3 węzłów sieci, które są niezawodne i uczciwe. Dlatego też, jeśli większość sieci zdecyduje się działać złośliwie, system jest podatny na ataki.


> ten dylemat jest czasami nazywany "problemem niezawodnego nadawania"