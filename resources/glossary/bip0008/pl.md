---
term: BIP0008
---

Opracowany po debatach na temat SegWit, który wykorzystywał BIP9 do aktywacji, BIP8 jest metodą aktywacji Soft Fork, która natywnie zawiera automatyczny mechanizm UASF (*User-Activated Soft Fork*). Podobnie jak BIP9, BIP8 wykorzystuje sygnalizację Miner, ale dodaje parametr `LOT` (*Lock-in On Time out*). Jeśli `LOT` jest ustawiony na `true`, po wygaśnięciu okresu sygnalizacji bez osiągnięcia wymaganego progu, automatycznie uruchamiany jest UASF, wymuszając aktywację Soft Fork. Takie podejście zmusza górników do współpracy lub ryzykowania nałożenia UASF przez użytkowników. Co więcej, w przeciwieństwie do BIP9, BIP8 definiuje okres sygnalizacji w oparciu o wysokość bloku, eliminując potencjalne manipulacje za pomocą Hash przez górników. BIP8 pozwala również na ustawienie zmiennego progu głosowania i wprowadza parametr minimalnej wysokości bloku do aktywacji, dając górnikom czas na przygotowanie i zasygnalizowanie swojej zgody z wyprzedzeniem, niekoniecznie będąc gotowym. Kiedy Soft Fork jest aktywowany przez BIP8 z parametrem `LOT=true`, wykorzystuje to bardzo agresywną metodę przeciwko górnikom, którzy są natychmiast poddawani presji potencjalnego UASF. W rzeczywistości pozostawia im tylko 2 możliwości:


- Bądź chętny do współpracy, a tym samym ułatw proces aktywacji;
- Nie współpracować, w którym to przypadku użytkownicy automatycznie wykonują UASF w celu nałożenia Soft Fork.