---
name: Narzędzia statystyk Whirlpool - Anonsets
description: Zrozumienie pojęcia anonset i sposobu jego obliczania za pomocą WST
---
![cover](assets/cover.webp)


***OSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, narzędzie Whirlpool Stats Tool nie jest już dostępne do pobrania, ponieważ było hostowane na Gitlab Samourai. Nawet jeśli wcześniej pobrałeś to narzędzie lokalnie na swój komputer lub było ono zainstalowane na twoim węźle RoninDojo, WST nie będzie teraz działać. Jego działanie opierało się na danych dostarczonych przez OXT.me, a strona ta nie jest już dostępna. Obecnie WST nie jest szczególnie przydatny, ponieważ protokół Whirlpool jest nieaktywny. Istnieje jednak możliwość, że oprogramowanie to zostanie przywrócone w nadchodzących tygodniach. Co więcej, teoretyczna część tego artykułu pozostaje istotna dla zrozumienia zasad i celów coinjoinów w ogóle (nie tylko Whirlpool), a także zrozumienia skuteczności modelu Whirlpool. Można również dowiedzieć się, jak ilościowo określić prywatność zapewnianą przez cykle CoinJoin*


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

> *Przerwij połączenie, które pozostawiają po sobie monety*

W tym samouczku przeanalizujemy koncepcję anonsetów, wskaźników, które pozwalają nam oszacować jakość procesu CoinJoin na Whirlpool. Omówimy metodę obliczania i interpretacji tych wskaźników. Po części teoretycznej przejdziemy do praktyki, ucząc się obliczać anonsety dla konkretnej transakcji za pomocą narzędzia Python *Whirlpool Stats Tools* (WST).


## Co to jest CoinJoin na Bitcoin?

**CoinJoin to technika, która łamie identyfikowalność bitcoinów na Blockchain**. Opiera się ona na wspólnej transakcji o określonej strukturze o tej samej nazwie: transakcji CoinJoin.


Transakcje CoinJoin zwiększają prywatność użytkowników Bitcoin, komplikując analizę łańcucha zewnętrznym obserwatorom. Ich struktura umożliwia łączenie wielu monet od różnych użytkowników w jedną transakcję, zaciemniając w ten sposób ślady i utrudniając określenie powiązań między adresami wejściowymi i wyjściowymi.


Zasada CoinJoin opiera się na podejściu opartym na współpracy: kilku użytkowników, którzy chcą mieszać swoje bitcoiny, wpłaca identyczne kwoty jako dane wejściowe tej samej transakcji. Kwoty te są następnie redystrybuowane w wyjściach o równoważnej wartości. Po zakończeniu transakcji niemożliwe staje się powiązanie konkretnego wyniku z danym użytkownikiem. Nie istnieje bezpośrednie powiązanie między danymi wejściowymi i wyjściowymi, tym samym zrywając powiązanie między użytkownikami i ich UTXO, a także historią każdej monety.


![coinjoin](assets/notext/1.webp)


Przykład transakcji CoinJoin:

[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Aby przeprowadzić CoinJoin przy jednoczesnym zapewnieniu, że każdy użytkownik zachowuje kontrolę nad swoimi środkami przez cały czas, proces rozpoczyna się od skonstruowania transakcji przez koordynatora, który następnie przesyła ją do każdego uczestnika. Następnie każdy użytkownik podpisuje transakcję po sprawdzeniu, czy mu odpowiada. Wszystkie zebrane podpisy są ostatecznie zintegrowane z transakcją. Jeśli użytkownik lub koordynator podejmie próbę przekierowania środków, modyfikując dane wyjściowe transakcji CoinJoin, podpisy okażą się nieważne, co doprowadzi do odrzucenia transakcji przez węzły.


Istnieje kilka implementacji CoinJoin, takich jak Whirlpool, JoinMarket lub Wabisabi, z których każda ma na celu zarządzanie koordynacją między uczestnikami i zwiększenie wydajności transakcji CoinJoin.

W tym poradniku skupimy się na mojej ulubionej implementacji: Whirlpool, która jest dostępna w Samourai Wallet i Sparrow Wallet. Moim zdaniem jest to najbardziej wydajna implementacja coinjoinów na Bitcoin.


## Jaka jest użyteczność CoinJoin na Bitcoin?


Użyteczność CoinJoin polega na jego zdolności do tworzenia wiarygodnego zaprzeczenia, poprzez utopienie monety w grupie nieodróżnialnych monet. Celem tego działania jest zerwanie powiązań identyfikowalności, zarówno z przeszłości do teraźniejszości, jak i z teraźniejszości do przeszłości.


Innymi słowy, analityk, który zna początkową transakcję na wejściu cykli CoinJoin, nie powinien być w stanie z całą pewnością zidentyfikować UTXO na wyjściu cykli remiksowych (analiza od wejścia do wyjścia cyklu).


![coinjoin](assets/en/2.webp)


I odwrotnie, analityk, który zna twój UTXO na wyjściu z cykli CoinJoin, nie powinien być w stanie określić pierwotnej transakcji na wejściu do cykli (analiza od wyjścia z cyklu do wejścia w cykl).


![coinjoin](assets/en/3.webp)


Aby ocenić trudność analityka w powiązaniu przeszłości z teraźniejszością i odwrotnie, konieczne jest ilościowe określenie wielkości grup, w których ukryta jest moneta. Ta miara mówi nam o liczbie analiz o identycznym prawdopodobieństwie. Tak więc, jeśli poprawna analiza jest utopiona wśród 3 innych analiz o równym prawdopodobieństwie, poziom ukrycia jest bardzo niski. Z drugiej strony, jeśli poprawna analiza znajduje się w zestawie 20 000 analiz o jednakowym prawdopodobieństwie, moneta jest bardzo dobrze ukryta.


I właśnie wielkość tych grup reprezentuje wskaźniki, które nazywane są "anonsets".


## Zrozumienie anonsów

Anonsety służą jako wskaźniki do oceny stopnia prywatności danego UTXO. Mówiąc dokładniej, mierzą one liczbę nierozróżnialnych UTXO w zbiorze zawierającym badaną monetę. Wymóg jednorodnego zbioru UTXO oznacza, że anonsety są zwykle obliczane dla cykli CoinJoin. Zastosowanie tych wskaźników jest szczególnie istotne w przypadku połączeń monet Whirlpool ze względu na ich jednorodność.


Anonsety pozwalają, w stosownych przypadkach, ocenić jakość coinjoinów. Duży rozmiar anonsetu oznacza zwiększony poziom anonimowości, ponieważ rozróżnienie konkretnego UTXO w zestawie staje się trudne.


Istnieją dwa rodzaje anonsów:


- Perspektywiczny zestaw anonimowości;**
- Retrospektywny zestaw anonimowości.**

Pierwszy wskaźnik pokazuje wielkość grupy, w której badana UTXO jest ukryta pod koniec cyklu, znając UTXO na wejściu, czyli liczbę nieodróżnialnych monet obecnych w tej grupie. Wskaźnik ten pozwala zmierzyć odporność poufności monety na analizę od przeszłości do teraźniejszości (od wejścia do wyjścia). W języku angielskim nazwa tego wskaźnika to "*forward anonset*" lub "*forward-looking metrics*".

![coinjoin](assets/en/4.webp)


Ta metryka szacuje stopień, w jakim twój UTXO jest chroniony przed próbami odtworzenia jego historii od punktu wejścia do punktu wyjścia w procesie CoinJoin.


Na przykład, jeśli twoja transakcja uczestniczyła w pierwszym cyklu CoinJoin i dwa inne cykle potomne zostały zakończone, potencjalny anonset twojej monety wynosiłby `13`:


![coinjoin](assets/en/5.webp)


Drugi wskaźnik pokazuje liczbę możliwych źródeł dla danej monety, znając UTXO na koniec cyklu. Wskaźnik ten mierzy odporność poufności monety na analizę od teraźniejszości do przeszłości (od wyjścia do wejścia), czyli jak trudno jest analitykowi prześledzić wstecz do pochodzenia monety, przed cyklami CoinJoin. W języku angielskim nazwa tego wskaźnika to "*backward anonset*" lub "*backward-looking metrics*".


![coinjoin](assets/en/6.webp)


Znając swój UTXO na wyjściu z cykli, retrospektywny anonset określa liczbę potencjalnych transakcji Tx0, które mogły stanowić twoje wejście w cykle CoinJoin. Na poniższym wykresie odpowiada to sumie wszystkich pomarańczowych bąbelków.


![coinjoin](assets/en/7.webp)


## Obliczanie anonsetów za pomocą Whirlpool Stats Tools (WST)

Aby obliczyć te wskaźniki na własnych monetach, które przeszły przez cykle CoinJoin, można użyć narzędzia specjalnie opracowanego przez Samourai Wallet: *Whirlpool Stats Tools*.


Jeśli posiadasz RoninDojo, WST jest preinstalowany na Twoim węźle. Możesz więc pominąć kroki instalacji i bezpośrednio postępować zgodnie z krokami użytkowania. Dla tych, którzy nie mają węzła RoninDojo, zobaczmy, jak kontynuować instalację tego narzędzia na komputerze.


Potrzebne będą: Tor Browser (lub Tor), Python 3.4.4 lub nowszy, git oraz pip. Otwórz terminal. Aby sprawdzić obecność i wersję tych programów w systemie, wprowadź następujące polecenia:

```plaintext
python --version
git --version
pip --version
```


W razie potrzeby można je pobrać z odpowiednich stron internetowych:


- https://www.python.org/downloads/ (pip jest dostarczany bezpośrednio z Pythonem od wersji 3.4);
- https://www.torproject.org/download/;
- https://git-scm.com/downloads.

Po zainstalowaniu wszystkich tych programów, z terminala sklonuj repozytorium WST:

```plaintext
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```


![WST](assets/notext/8.webp)


Przejdź do katalogu WST:

```plaintext
cd whirlpool_stats
```


Zainstaluj zależności:

```plaintext
pip3 install -r ./requirements.txt
```


![WST](assets/notext/9.webp)


Można również zainstalować je ręcznie (opcjonalnie):

```plaintext
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```


Przejdź do podfolderu `/whirlpool_stats`:

```plaintext
cd whirlpool_stats
```


Start WST:

```plaintext
python3 wst.py
```


![WST](assets/notext/10.webp)


Uruchom Tor lub Tor Browser w tle.


**-> Użytkownicy RoninDojo mogą wznowić samouczek bezpośrednio tutaj


Ustaw proxy na Tor (RoninDojo),

```plaintext
socks5 127.0.0.1:9050
```


lub do przeglądarki Tor, w zależności od używanej przeglądarki:

```plaintext
socks5 127.0.0.1:9150
```


Ta manipulacja pozwoli ci pobrać dane na OXT przez Tor, aby nie wyciekły informacje o twoich transakcjach. Jeśli jesteś nowicjuszem i ten krok wydaje ci się skomplikowany, wiedz, że polega on po prostu na kierowaniu ruchu internetowego przez Tor. Najprostsza metoda polega na uruchomieniu przeglądarki Tor w tle na komputerze, a następnie wykonaniu tylko drugiego polecenia, aby połączyć się za pośrednictwem tej przeglądarki (`socks5 127.0.0.1:9150`).


![WST](assets/notext/11.webp)


Następnie przejdź do katalogu roboczego, z którego zamierzasz pobrać dane WST za pomocą polecenia `workdir`. Folder ten będzie służył do przechowywania danych transakcyjnych, które zostaną pobrane z OXT w postaci plików `.csv`. Informacje te są niezbędne do obliczenia wskaźników, które chcesz uzyskać. Możesz dowolnie wybrać lokalizację tego katalogu. Rozsądne może być utworzenie folderu specjalnie dla danych WST. Jako przykład wybierzmy folder pobierania. Jeśli korzystasz z RoninDojo, ten krok nie jest konieczny:

```plaintext
workdir path/to/your/directory
```


Wiersz poleceń powinien zmienić się, aby wskazać katalog roboczy.


![WST](assets/notext/12.webp)


Następnie pobierz dane z puli zawierającej transakcję. Na przykład, jeśli jestem w puli `100,000 Sats`, polecenie jest następujące:

```plaintext
download 0001
```


![WST](assets/notext/13.webp)


Kody nominałów na WST są następujące:


- Pula 0,5 bitcoina: `05`
- Pula 0.05 bitcoinów: `005`
- Pula 0,01 bitcoina: `001`
- Pula 0,001 bitcoinów: `0001`

Po pobraniu danych należy je załadować. Na przykład, jeśli jestem w puli `100,000 Sats`, polecenie jest następujące:

```plaintext
load 0001
```


Ten krok zajmuje kilka minut w zależności od komputera. Teraz jest dobry moment na zrobienie sobie kawy! :)


![WST](assets/notext/14.webp)


Po załadowaniu danych wpisz polecenie `score`, a następnie txid (identyfikator transakcji), aby uzyskać jego wyniki:

```plaintext
score TXID
```


**Uwaga:** wybór txid do użycia różni się w zależności od anonsetu, który chcesz obliczyć. Aby ocenić przyszły anonset monety, konieczne jest wprowadzenie, za pomocą komendy `score`, txid odpowiadającego jej pierwszemu CoinJoin, który jest początkową mieszanką wykonaną z tym UTXO. Z drugiej strony, aby określić anonset retrospektywny, należy wprowadzić txid ostatniego wykonanego CoinJoin. Podsumowując, anonset prospektywny jest obliczany na podstawie txid pierwszej mieszanki, podczas gdy anonset retrospektywny jest obliczany na podstawie txid ostatniej mieszanki.


Następnie WST wyświetla wynik retrospektywny (*metryka retrospektywna*) i wynik prospektywny (*metryka prospektywna*). Na przykład, wziąłem txid losowej monety na Whirlpool, która nie należy do mnie.


![WST](assets/notext/15.webp)


Transakcja, o której mowa: [7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://Mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)


Jeśli uznamy tę transakcję za pierwszą CoinJoin wykonaną dla danej monety, wówczas korzysta ona z potencjalnego anonsetu wynoszącego `86,871`. Oznacza to, że jest ona ukryta wśród `86,871` nieodróżnialnych monet. Dla zewnętrznego obserwatora, który zna tę monetę na początku cykli CoinJoin i próbuje prześledzić jej wynik, będzie miał do czynienia z `86,871` możliwych UTXO, z których każdy ma identyczne prawdopodobieństwo bycia poszukiwaną monetą.


Jeśli uznamy tę transakcję za ostatni CoinJoin monety, to ma ona retrospektywny anonset w wysokości `42 185`. Oznacza to, że istnieje `42 185` potencjalnych źródeł dla tego UTXO. Jeśli zewnętrzny obserwator zidentyfikuje tę monetę pod koniec cykli i spróbuje prześledzić jej pochodzenie, będzie miał do czynienia z `42 185` możliwych źródeł, z których wszystkie mają równe prawdopodobieństwo bycia poszukiwanym źródłem.

Oprócz wyników anonset, WST zapewnia również wskaźnik dyfuzji wyników w puli w oparciu o anonset. Ten drugi wskaźnik pozwala po prostu ocenić potencjał ulepszenia utworu. Wskaźnik ten jest szczególnie przydatny dla potencjalnych anonsetów. Rzeczywiście, jeśli twój utwór ma wskaźnik dyfuzji 15%, oznacza to, że można go pomylić z 15% utworów w puli. To dobrze, ale nadal masz bardzo duży margines na poprawę poprzez dalsze remiksowanie. Z drugiej strony, jeśli twój utwór ma współczynnik dyfuzji 95%, to zbliżasz się do granic puli. Możesz kontynuować remiksowanie, ale twój anonset niewiele wzrośnie.


Należy zauważyć, że anonsety obliczane przez WST nie są idealnie dokładne. Biorąc pod uwagę ogromną ilość danych do przetworzenia, WST wykorzystuje algorytm *HyperLogLogPlusPlus*, aby znacznie zmniejszyć obciążenie związane z lokalnym przetwarzaniem danych i niezbędną pamięcią. Jest to algorytm, który pozwala oszacować liczbę odrębnych wartości w bardzo dużych zbiorach danych przy zachowaniu wysokiej dokładności wyniku. W związku z tym podane wyniki są wystarczająco dobre, aby można je było wykorzystać w analizach, ponieważ są bardzo zbliżone do rzeczywistości, ale nie należy ich interpretować jako dokładnych wartości dla jednostki.


Podsumowując, należy pamiętać, że nie jest konieczne systematyczne obliczanie anonsetów dla każdego z elementów w coinjoinach. Już sama konstrukcja Whirlpool zapewnia gwarancje. Rzeczywiście, retrospektywny anonset rzadko jest problemem. Z początkowego miksu uzyskujesz szczególnie wysoki wynik retrospektywny dzięki dziedzictwu poprzednich miksów od Genesis CoinJoin. Jeśli chodzi o prospektywny anonset, wystarczy utrzymać swój utwór na koncie po miksie przez wystarczająco długi okres.


Dlatego też uważam, że wykorzystanie Whirlpool jest szczególnie istotne w strategii *HODL -> Mix -> Spend -> Replace*. Moim zdaniem najbardziej logicznym podejściem jest utrzymywanie większości swoich oszczędności Bitcoin w Cold Wallet, przy jednoczesnym ciągłym utrzymywaniu pewnej liczby sztuk w coinjoinach na Samourai w celu pokrycia codziennych wydatków. Gdy bitcoiny z coinjoinów zostaną wydane, są one zastępowane nowymi, aby powrócić do określonego progu mieszanych sztuk. Metoda ta pozwala uwolnić się od obaw związanych z naszymi anonsetami UTXO, a jednocześnie sprawia, że czas potrzebny na skuteczność coinjoinów jest znacznie mniej ograniczony.


**Zasoby zewnętrzne:**



- [Podcast w języku francuskim on chain analiza](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [Artykuł w Wikipedii na temat HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog)
- Repozytorium Samourai dla statystyk Whirlpool
- Strona internetowa Whirlpool by Samourai
- [Średni artykuł w języku angielskim na temat prywatności i Bitcoin autorstwa Samourai](https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [Średni artykuł w języku angielskim na temat koncepcji anonimowości ustalonej przez Samourai](https://medium.com/samourai-Wallet/diving-head-first-into-Whirlpool-anonymity-sets-4156a54b0bc7)