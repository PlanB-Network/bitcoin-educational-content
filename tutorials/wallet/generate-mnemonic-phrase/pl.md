---
name: Mnemonic Fraza - Rzut kostką
description: Jak generate własną frazę odzyskiwania za pomocą kości?
---

![cover](assets/cover.webp)


W tym samouczku dowiesz się, jak ręcznie skonstruować frazę odzyskiwania dla Bitcoin Wallet przy użyciu rzutów kośćmi.


**OSTRZEŻENIE:** Wygenerowanie frazy Mnemonic w bezpieczny sposób wymaga niepozostawienia cyfrowego śladu podczas jej tworzenia, co jest prawie niemożliwe. W przeciwnym razie Wallet stanowiłby zbyt dużą powierzchnię ataku, znacznie zwiększając ryzyko kradzieży bitcoinów. **W związku z tym zdecydowanie odradza się przelewanie środków na Wallet, który zależy od wygenerowanej przez ciebie frazy odzyskiwania **, nawet jeśli postępujesz zgodnie z tym samouczkiem, istnieje ryzyko, że fraza odzyskiwania może zostać naruszona. **Dlatego też niniejszy poradnik nie powinien być stosowany do tworzenia prawdziwego Wallet.** Użycie Hardware Wallet do tego zadania jest znacznie mniej ryzykowne, ponieważ generuje on frazę offline, a prawdziwi kryptografowie rozważali użycie jakościowych źródeł entropii.


Ten samouczek może być stosowany wyłącznie w celach eksperymentalnych do tworzenia fikcyjnego Wallet, bez zamiaru używania go z prawdziwymi bitcoinami. Doświadczenie to oferuje jednak dwie korzyści:



- Po pierwsze, pozwala lepiej zrozumieć mechanizmy leżące u podstaw Bitcoin Wallet;
- Po drugie, pozwala dowiedzieć się, jak to zrobić. Nie twierdzę, że to się kiedyś przyda, ale może!


## Co to jest fraza Mnemonic?


Fraza odzyskiwania, czasami nazywana również "frazą Mnemonic", "frazą seed" lub "tajną frazą", to sekwencja zwykle składająca się z 12 lub 24 słów, która jest generowana w sposób pseudolosowy ze źródła entropii. Sekwencja pseudolosowa jest zawsze zakończona sumą kontrolną.


Fraza Mnemonic, wraz z opcjonalną passphrase, jest używana do deterministycznego wyprowadzenia wszystkich kluczy powiązanych z HD (Hierarchical Deterministic) Wallet. Oznacza to, że na podstawie tej frazy możliwe jest deterministyczne generate i odtworzenie wszystkich kluczy prywatnych i publicznych Bitcoin Wallet, a w konsekwencji uzyskanie dostępu do powiązanych z nim środków.

![mnemonic](assets/notext/1.webp)

Celem tego zdania jest zapewnienie łatwego w użyciu sposobu tworzenia kopii zapasowych i odzyskiwania bitcoinów. Konieczne jest przechowywanie frazy Mnemonic w bezpiecznym miejscu, ponieważ każdy, kto jest w jej posiadaniu, miałby dostęp do środków odpowiadającego jej Wallet. Jeśli jest on używany w kontekście tradycyjnego Wallet i bez opcjonalnego passphrase, często stanowi SPOF (Single Point Of Failure).

Zazwyczaj fraza ta jest podawana bezpośrednio podczas tworzenia Wallet przez używane oprogramowanie lub Hardware Wallet. Możliwe jest jednak również samodzielne wpisanie tej frazy w generate, a następnie wprowadzenie jej na wybranym nośniku w celu uzyskania kluczy Wallet. Tego właśnie nauczymy się w tym poradniku.


## Przygotowanie niezbędnych materiałów


Do ręcznego utworzenia frazy odzyskiwania potrzebne będą:



- Kartka papieru;
- Długopis lub ołówek, najlepiej w różnych kolorach, aby ułatwić organizację;
- Kilka kości, aby zminimalizować ryzyko błędu związanego z niewyważoną kością;
- [Wydrukowano listę 2048 słów BIP39](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf).


Następnie do obliczenia sumy kontrolnej konieczne będzie użycie komputera z terminalem. Właśnie z tego powodu odradzam ręczne generowanie frazy Mnemonic. Moim zdaniem ingerencja komputera, nawet przy zachowaniu środków ostrożności wspomnianych w tym poradniku, znacznie zwiększa podatność Wallet na ataki.


W przypadku eksperymentalnego podejścia dotyczącego "fikcyjnego Wallet" możliwe jest użycie zwykłego komputera i jego terminala. Jednak w przypadku bardziej rygorystycznego podejścia mającego na celu ograniczenie ryzyka naruszenia frazy, idealnym rozwiązaniem byłoby użycie komputera odłączonego od Internetu (najlepiej bez komponentu Wi-Fi lub połączenia przewodowego RJ45), wyposażonego w minimum urządzeń peryferyjnych (z których wszystkie powinny być podłączone kablem, aby uniknąć Bluetooth), a przede wszystkim działającego na amnezyjnej dystrybucji Linuksa, takiej jak [Tails](https://tails.boum.org/index.fr.html), uruchamianej z nośnika wymiennego.


![mnemonic](assets/notext/2.webp)


W prawdziwym kontekście kluczowe byłoby zapewnienie poufności miejsca pracy poprzez wybranie lokalizacji z dala od wścibskich oczu, bez ruchu ludzi i bez kamer (kamer internetowych, telefonów...).

Zaleca się użycie dużej liczby kości, aby złagodzić wpływ potencjalnie niezrównoważonej kości na entropię. Przed użyciem zaleca się sprawdzenie kości: można to osiągnąć, testując je w misce z wodą nasyconą solą, pozwalając kościom unosić się na wodzie. Następnie należy rzucić każdą kostką około dwudziestu razy w słonej wodzie, obserwując wyniki. Jeśli jedna lub dwie twarze pojawią się nieproporcjonalnie w porównaniu do innych, należy rozszerzyć test o więcej rzutów. Równomiernie rozłożone wyniki wskazują, że kość jest niezawodna. Jeśli jednak jedna lub dwie powierzchnie regularnie dominują, kości te należy odłożyć na bok, ponieważ mogą one zagrozić entropii frazy Mnemonic, a w konsekwencji bezpieczeństwu Wallet.

W rzeczywistych warunkach, po przeprowadzeniu tych kontroli, byłbyś gotowy do generate niezbędnej entropii. W przypadku eksperymentalnego fikcyjnego Wallet stworzonego w ramach tego samouczka, można oczywiście pominąć te przygotowania.


## Kilka przypomnień na temat frazy odzyskiwania


Na początek omówimy podstawy tworzenia frazy Mnemonic zgodnie z BIP39. Jak wyjaśniono wcześniej, fraza pochodzi z pseudolosowej informacji o określonym rozmiarze, do której dodawana jest suma kontrolna w celu zapewnienia jej integralności.


Rozmiar tej początkowej informacji, często określanej jako "entropia", jest określany przez liczbę słów, które chcesz uzyskać w frazie odzyskiwania. Najpopularniejszymi formatami są frazy składające się z 12 i 24 słów, co daje odpowiednio entropię 128 bitów i 256 bitów. Poniżej znajduje się tabela przedstawiająca różne rozmiary entropii zgodnie z BIP39:


| Phrase (words) | Entropy (bits) | Checksum (bits) | Entropy + Checksum (bits) |
| -------------- | -------------- | --------------- | ------------------------- |
| 12             | 128            | 4               | 132                       |
| 15             | 160            | 5               | 165                       |
| 18             | 192            | 6               | 198                       |
| 21             | 224            | 7               | 231                       |
| 24             | 256            | 8               | 264                       |

Entropia jest więc liczbą losową pomiędzy 128 a 256 bitów. W tym samouczku weźmiemy przykład 12-wyrazowej frazy, w której entropia wynosi 128 bitów, co oznacza, że generate będzie losową sekwencją 128 `0` lub `1`. Reprezentuje to liczbę składającą się ze 128 cyfr o podstawie 2 (binarnej).

Na podstawie tej entropii generowana jest suma kontrolna. Suma kontrolna to wartość obliczana na podstawie zestawu danych, używana do weryfikacji integralności i ważności tych danych podczas ich przesyłania lub przechowywania. Algorytmy sum kontrolnych są zaprojektowane do wykrywania przypadkowych błędów lub zmian w danych.

W przypadku naszej frazy Mnemonic, funkcją sumy kontrolnej jest wykrycie wszelkich błędów podczas wprowadzania frazy do oprogramowania Wallet. Nieprawidłowa suma kontrolna sygnalizuje obecność błędu we frazie. I odwrotnie, prawidłowa suma kontrolna wskazuje, że fraza jest najprawdopodobniej poprawna.


Aby uzyskać tę sumę kontrolną, entropia jest przekazywana przez funkcję SHA256 Hash. Ta operacja daje na wyjściu 256-bitową sekwencję, z której tylko pierwsze `N` bitów zostanie zachowanych, `N` w zależności od pożądanej długości frazy odzyskiwania (patrz tabela powyżej). Tak więc, dla 12-wyrazowej frazy, zachowane zostaną pierwsze 4 bity Hash.

![mnemonic](assets/en/3.webp)

Te pierwsze 4 bity, tworzące sumę kontrolną, zostaną następnie dodane do oryginalnej entropii. Na tym etapie fraza odzyskiwania jest praktycznie ukonstytuowana, ale nadal ma postać binarną. Aby przekonwertować tę sekwencję binarną na słowa zgodnie ze standardem BIP39, najpierw podzielimy sekwencję na 11-bitowe segmenty.

![mnemonic](assets/notext/4.webp)

Każdy z tych pakietów reprezentuje liczbę binarną, która następnie zostanie przekonwertowana na liczbę dziesiętną (podstawa 10). Dodamy `1` do każdej liczby, ponieważ w obliczeniach liczenie zaczyna się od `0`, ale lista BIP39 jest numerowana od `1`.


![mnemonic](assets/notext/5.webp)


Wreszcie, liczba w systemie dziesiętnym mówi nam o pozycji odpowiedniego słowa w [liście 2048 słów BIP39](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf). Pozostaje tylko wybrać te słowa, aby skomponować frazę odzyskiwania dla naszego Wallet.


![mnemonic](assets/notext/6.webp)


Przejdźmy teraz do praktyki! Stworzymy generate 12-wyrazową frazę odzyskiwania. Jednak ta operacja pozostaje identyczna w przypadku 24-słowowej frazy, z wyjątkiem tego, że wymagałaby 256 bitów entropii i 8-bitowej sumy kontrolnej, jak wskazano w tabeli równoważności znajdującej się na początku tej sekcji.


## Krok 1: Generowanie entropii


Przygotuj kartkę papieru, długopis i kostkę do gry. Aby rozpocząć, będziemy musieli losowo generate 128 bitów, czyli sekwencję 128 `0` i `1` w rzędzie. Aby to zrobić, użyjemy kości do gry.

![mnemonic](assets/notext/7.webp)


Kości mają 6 boków, wszystkie z identycznym prawdopodobieństwem wyrzucenia. Naszym celem jest jednak uzyskanie wyniku binarnego, co oznacza dwa możliwe rezultaty. Dlatego przypiszemy wartość `0` do każdego rzutu, który wyląduje na liczbie parzystej i `1` dla każdej liczby nieparzystej. W rezultacie wykonamy 128 rzutów, aby stworzyć naszą 128-bitową entropię. Jeśli kość pokaże `2`, `4` lub `6`, zapiszemy `0`; dla `1`, `3` lub `5`, będzie to `1`. Każdy wynik będzie zapisywany sekwencyjnie, od lewej do prawej i od góry do dołu.


Aby ułatwić poniższe kroki, pogrupujemy bity w pakiety po cztery i trzy, jak pokazano na poniższym obrazku. Każda linia musi zawierać 11 bitów: 2 pakiety po 4 bity i jeden pakiet po 3 bity.


![mnemonic](assets/notext/8.webp)


Jak widać na moim przykładzie, dwunaste słowo składa się obecnie tylko z 7 bitów. Zostaną one uzupełnione 4 bitami sumy kontrolnej w następnym kroku, tworząc 11 bitów.


![mnemonic](assets/notext/9.webp)


## Krok 2: Obliczanie sumy kontrolnej


Ten krok jest najbardziej krytyczny w ręcznym generowaniu frazy Mnemonic, ponieważ wymaga użycia komputera. Jak wspomniano wcześniej, suma kontrolna odpowiada początkowi SHA256 Hash wygenerowanego z entropii. Chociaż teoretycznie możliwe jest ręczne obliczenie SHA256 dla danych wejściowych o długości 128 lub 256 bitów, zadanie to może zająć cały tydzień. Co więcej, każdy błąd w ręcznych obliczeniach zostałby zidentyfikowany dopiero pod koniec procesu, zmuszając do rozpoczęcia od początku. W związku z tym niewyobrażalne jest wykonanie tego kroku za pomocą kartki papieru i długopisu. Komputer jest niemal obowiązkowy. Jeśli nadal chcesz dowiedzieć się, jak wykonać SHA256 ręcznie, wyjaśniamy, jak to zrobić w [kursie CRYPTO301](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f).


Z tego powodu zdecydowanie odradzam tworzenie ręcznej frazy dla rzeczywistego Wallet. Moim zdaniem korzystanie z komputera na tym etapie, nawet przy zachowaniu wszelkich niezbędnych środków ostrożności, bezzasadnie zwiększa powierzchnię ataku Wallet.

Aby obliczyć sumę kontrolną, pozostawiając jak najmniej śladów, użyjemy amnezyjnej dystrybucji Linuksa z dysku wymiennego o nazwie **Tails**. Ten system operacyjny uruchamia się z pamięci USB i działa całkowicie na pamięci RAM komputera, bez interakcji z dyskiem Hard. Teoretycznie nie pozostawia więc żadnych śladów na komputerze po jego wyłączeniu. Należy pamiętać, że Tails jest kompatybilny tylko z procesorami typu x86_64, a nie z procesorami typu ARM.

Aby rozpocząć, ze zwykłego komputera [pobierz obraz Tails z oficjalnej strony internetowej](https://tails.net/install/index.fr.html). Upewnij się, że pobrany plik jest autentyczny, korzystając z podpisu dewelopera lub narzędzia weryfikacyjnego oferowanego przez witrynę.

![mnemonic](assets/notext/10.webp)

Najpierw sformatuj pamięć USB, a następnie zainstaluj Tails za pomocą narzędzia takiego jak [Balena Etcher](https://etcher.balena.io/).

![mnemonic](assets/notext/11.webp)

Po potwierdzeniu, że flashowanie powiodło się, wyłącz komputer. Następnie należy odłączyć zasilanie Supply i wyjąć napęd Hard z płyty głównej komputera. W przypadku obecności karty WiFi należy ją odłączyć. Podobnie należy odłączyć kabel Ethernet RJ45. Aby zminimalizować ryzyko wycieku danych, zaleca się odłączenie skrzynki internetowej i wyłączenie telefonu komórkowego. Ponadto należy odłączyć od komputera wszelkie zbędne urządzenia peryferyjne, takie jak mikrofon, kamera internetowa, głośniki lub zestaw słuchawkowy, a także sprawdzić, czy inne urządzenia peryferyjne są podłączone wyłącznie przewodowo. Wszystkie te kroki przygotowania komputera nie są niezbędne, ale po prostu pomagają zmniejszyć powierzchnię ataku w jak największym stopniu w rzeczywistym kontekście.


Sprawdź, czy system BIOS jest skonfigurowany tak, aby umożliwić uruchamianie z urządzenia zewnętrznego. Jeśli nie, zmień to ustawienie, a następnie uruchom ponownie komputer. Po zabezpieczeniu środowiska komputerowego uruchom ponownie komputer z pamięci USB z systemem operacyjnym Tails.


Na ekranie powitalnym Tails wybierz język, a następnie uruchom system, klikając `Start Tails`.


![mnemonic](assets/notext/12.webp)


Na pulpicie kliknij zakładkę `Aplikacje`.


![mnemonic](assets/notext/13.webp)


Przejdź do menu `Utilities`.


![mnemonic](assets/notext/14.webp)


Na koniec kliknij aplikację `Terminal`.


![mnemonic](assets/notext/15.webp)


Pojawi się nowy pusty terminal poleceń.


![mnemonic](assets/notext/16.webp)

Wpisz komendę `echo`, a następnie wygenerowaną wcześniej entropię, pamiętając o wstawieniu spacji między `echo` a sekwencją cyfr binarnych.

![mnemonic](assets/notext/17.webp)


Dodaj dodatkową spację, a następnie wprowadź następujące polecenie, używając _pipe_ (`|`):


```plaintext
| shasum -a 256 -0


![mnemonic](assets/notext/18.webp)


W przykładzie z moją entropią całkowita komenda wygląda następująco:


```plaintext
echo 11010111000110111011000011000010011000100111000001000000001001011011001010111111001010011111110001010100000101110010010011011010 | shasum -a 256 -0
```


W tym poleceniu:



- `echo` jest używane do wysyłania sekwencji bitów;
- `|`, _pipe_, jest używane do kierowania wyjścia komendy `echo` na wejście następnej komendy;
- `shasum` inicjuje funkcję haszującą należącą do rodziny SHA (_Secure Hash Algorithm_);
- `-a` określa wybór konkretnego algorytmu haszującego;
- `256` wskazuje, że używany jest algorytm SHA256;
- `-0` pozwala na interpretację wejścia jako liczby binarnej.


Po dokładnym sprawdzeniu, czy sekwencja binarna nie zawiera żadnych błędów, naciśnij klawisz `Enter`, aby wykonać polecenie. Terminal wyświetli SHA256 Hash entropii.


![mnemonic](assets/notext/19.webp)


Na razie Hash jest wyrażony w formacie szesnastkowym (podstawa 16). Na przykład mój to:


```plaintext
a27abf1aff70311917a59a43ce86fa45a62723a00dd2f9d3d059aeac9b4b13d8
```


Aby sfinalizować naszą frazę Mnemonic, potrzebujemy tylko pierwszych 4 bitów Hash, które stanowią sumę kontrolną. W formacie szesnastkowym każdy znak reprezentuje 4 bity. Dlatego zachowamy tylko pierwszy znak Hash. W przypadku frazy składającej się z 24 słów konieczne byłoby uwzględnienie dwóch pierwszych znaków. W moim przykładzie odpowiada to literze: `a`. Starannie zanotuj ten znak gdzieś na swoim arkuszu, a następnie wyłącz komputer.


Następnym krokiem jest przekonwertowanie tego znaku szesnastkowego (podstawa 16) na wartość binarną (podstawa 2), ponieważ nasza fraza jest skonstruowana w tym formacie. W tym celu można skorzystać z poniższej tabeli konwersji:


| Decimal (base 10) | Hexadecimal (base 16) | Binary (base 2) |
| ----------------- | --------------------- | --------------- |
| 0                 | 0                     | 0000            |
| 1                 | 1                     | 0001            |
| 2                 | 2                     | 0010            |
| 3                 | 3                     | 0011            |
| 4                 | 4                     | 0100            |
| 5                 | 5                     | 0101            |
| 6                 | 6                     | 0110            |
| 7                 | 7                     | 0111            |
| 8                 | 8                     | 1000            |
| 9                 | 9                     | 1001            |
| 10                | a                     | 1010            |
| 11                | b                     | 1011            |
| 12                | c                     | 1100            |
| 13                | d                     | 1101            |
| 14                | e                     | 1110            |
| 15                | f                     | 1111            |

W moim przykładzie litera `a` odpowiada liczbie binarnej `1010`. Te 4 bity tworzą sumę kontrolną naszej frazy odzyskiwania. Możesz teraz dodać je do entropii już zanotowanej na kartce papieru, umieszczając je na końcu ostatniego słowa.


![mnemonic](assets/notext/20.webp)


Twoja fraza Mnemonic jest teraz kompletna, ale jest w formacie binarnym. Następnym krokiem będzie przekonwertowanie go na system dziesiętny, aby można było powiązać każdą liczbę z odpowiednim słowem na liście BIP39.


## Krok 3: Konwersja słów na liczbę dziesiętną


Aby przekonwertować każdą linię binarną na liczbę dziesiętną, użyjemy metody ułatwiającej ręczne obliczenia. Obecnie masz dwanaście linii na papierze, z których każda składa się z 11 cyfr binarnych `0` lub `1`. Aby przejść do konwersji na liczbę dziesiętną, przypisz każdej pierwszej cyfrze wartość `1024`, jeśli jest to `1`, w przeciwnym razie `0`. Dla drugiej cyfry zostanie przypisana wartość `512`, jeśli jest to `1`, w przeciwnym razie `0`, i tak dalej aż do jedenastej cyfry. Odpowiedniki są następujące:



- 1. bit: `1024`;
- 2. bit: `512`;
- 3. bit: `256`;
- 4. bit: `128`;
- 5. bit: `64`;
- 6. bit: `32`;
- 7. bit: `16`;
- 8. bit: `8`;
- 9. bit: `4`;
- 10. bit: `2`;
- 11. bit: `1`.


Dla każdej linii dodamy wartości odpowiadające cyfrom `1`, aby uzyskać dziesiętny odpowiednik liczby binarnej. Weźmy przykład linii binarnej równej:


```plaintext
1010 1101 101
```


Konwersja wyglądałaby następująco:

![mnemonic](assets/notext/21.webp)

Wynik byłby wtedy następujący:


```plaintext
1389
```


Dla każdego bitu równego `1`, podaj powiązaną liczbę poniżej. Dla każdego bitu równego `0`, nie zgłaszaj nic.


![mnemonic](assets/notext/22.webp)

Następnie wystarczy zsumować wszystkie liczby zatwierdzone przez `1`, aby uzyskać liczbę dziesiętną reprezentującą każdą linię binarną. Na przykład, oto jak to wygląda dla mojego arkusza:

![mnemonic](assets/notext/23.webp)


## Krok 4: Wyszukiwanie słów frazy Mnemonic


Po uzyskaniu liczb dziesiętnych możemy teraz zlokalizować odpowiednie słowa na liście, aby utworzyć frazę Mnemonic. Jednak numeracja 2048 słów na liście BIP39 waha się od `1` do `2048`. Ale nasze obliczone wyniki binarne mieszczą się w zakresie od `0` do `2047`. Istnieje zatem przesunięcie o jedną jednostkę, które należy skorygować. Aby skorygować to przesunięcie, wystarczy dodać `1` do dwunastu wcześniej obliczonych liczb dziesiętnych.


![mnemonic](assets/notext/24.webp)


Po tej korekcie otrzymasz rangę każdego słowa na liście. Pozostaje tylko zidentyfikować każde słowo według jego numeru. Oczywiście, podobnie jak w przypadku wszystkich innych kroków, nie wolno używać komputera do wykonania tej konwersji. Dlatego upewnij się, że wcześniej wydrukowałeś listę.


[**-> Wydruk listy BIP39 w formacie A4.**](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf)


Na przykład, jeśli liczba pochodząca z pierwszej linii wynosi 1721, odpowiadające jej słowo będzie 1721. na liście:


```plaintext
1721. strike
```


![mnemonic](assets/notext/25.webp)

W ten sposób postępujemy kolejno z 12 słowami, aby skonstruować naszą frazę Mnemonic.


![mnemonic](assets/notext/26.webp)


## Krok 5: Tworzenie Bitcoin Wallet


W tym momencie pozostaje tylko zaimportować naszą frazę Mnemonic do oprogramowania Bitcoin Wallet. W zależności od naszych preferencji, można to zrobić na oprogramowaniu stacjonarnym, aby uzyskać Hot Wallet, lub na Hardware Wallet, aby uzyskać Cold Wallet.


![mnemonic](assets/notext/27.webp)


Tylko podczas importowania można zweryfikować poprawność sumy kontrolnej. Jeśli oprogramowanie wyświetli komunikat "Nieprawidłowa suma kontrolna", oznacza to, że w procesie tworzenia wkradł się błąd. Ogólnie rzecz biorąc, błąd ten wynika albo z błędnych obliczeń podczas ręcznej konwersji i dodawania, albo z literówki podczas wprowadzania entropii w terminalu na Tails. Konieczne będzie ponowne uruchomienie procesu od początku, aby poprawić te błędy.


![mnemonic](assets/notext/28.webp)

Po utworzeniu Wallet nie zapomnij wykonać kopii zapasowej frazy odzyskiwania na nośniku fizycznym, takim jak papier lub metal, i zniszczyć arkusz kalkulacyjny użyty podczas jego generowania, aby zapobiec wyciekom informacji.


## Szczególny przypadek opcji rzutu kostką na kartach Coldcard


Portfele sprzętowe z rodziny Coldcard oferują [funkcję o nazwie _Dice Roll_](https://youtu.be/Rc29d9m92xg?si=OeFW2iCGRvxexhK7), do generate frazy odzyskiwania Wallet za pomocą kości. Ta metoda jest doskonała, ponieważ daje bezpośrednią kontrolę nad tworzeniem entropii, bez konieczności korzystania z zewnętrznego urządzenia do obliczania sumy kontrolnej, jak w naszym samouczku.


Jednak ostatnio odnotowano przypadki kradzieży Bitcoin z powodu niewłaściwego korzystania z tej funkcji. Zbyt mała liczba rzutów kośćmi może prowadzić do niewystarczającej entropii, teoretycznie umożliwiając brutalne wymuszenie frazy Mnemonic i kradzież powiązanych bitcoinów. Aby uniknąć tego ryzyka, zaleca się wykonanie co najmniej 99 rzutów kośćmi na karcie Coldcard, co zapewni wystarczającą entropię.


Metoda interpretacji wyników zaproponowana przez Coldcard różni się od tej przedstawionej w tym poradniku. Podczas gdy w samouczku zalecamy 128 rzutów, aby osiągnąć 128 bitów bezpieczeństwa, Coldcard sugeruje 99 rzutów, aby osiągnąć 256 bitów bezpieczeństwa. Rzeczywiście, w naszym podejściu możliwe są tylko dwa wyniki dla każdego rzutu kostką: parzysty (`0`) lub nieparzysty (`1`). Dlatego entropia generowana przez każdy rzut jest równa `log2(2)`. W przypadku Coldcard, który bierze pod uwagę sześć możliwych twarzy kości (od `1` do `6`), entropia na rzut jest równa `log2(6)`. Dlatego w naszym samouczku musimy wykonać więcej rzutów, aby osiągnąć ten sam poziom entropii.


```plaintext
Entropy = number of rolls * log2(number of possible outcomes on the dice)

Coldcard :

Entropy = 99 * log2(6)
Entropy = 255.91

Our tutorial :

Entropy = 128 * log2(2)
Entropy = 128
```