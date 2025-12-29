---
name: Plan dziedziczenia Bitcoin
description: Jak przekazać bitcoiny swoim bliskim?
---

![cover](assets/cover.webp)



Transmisja bitcoinów stanowi poważne wyzwanie techniczne, które wielu posiadaczy pomija. W przeciwieństwie do tradycyjnych aktywów bankowych, w których instytucja finansowa może przekazać środki prawowitym właścicielom, Bitcoin działa bez pośredników. Twoi bliscy nigdy nie będą mogli uzyskać dostępu do Twoich środków bez niezbędnych informacji technicznych, niezależnie od ich legalności.



Ten samouczek poprowadzi Cię przez proces tworzenia technicznego planu dziedziczenia. Dowiesz się, jak działają mechanizmy on-chain do automatycznej transmisji, jak dokumentować swoje konfiguracje i jak wybrać odpowiednie rozwiązania, aby zapewnić, że twoje dziedzictwo Bitcoin pozostanie dostępne dla twoich bliskich.



## Dlaczego plan dziedzictwa technicznego jest niezbędny



Bitcoin opiera się na fundamentalnej zasadzie kryptograficznej: ten, kto posiada klucze prywatne, kontroluje fundusze. Ta suwerenność staje się poważnym zagrożeniem, gdy posiadacz klucza znika bez przekazania niezbędnych informacji.



Plan spadkowy Bitcoin musi spełniać dwa pozornie sprzeczne cele: umożliwiać bliskim dostęp do środków, gdy nadejdzie czas, a jednocześnie uniemożliwiać innym przedwczesny dostęp do nich. Ta delikatna równowaga opiera się na natywnych możliwościach programowania Bitcoin.



Złożoność techniczna dodaje dodatkową warstwę trudności. Spadkobiercy będą musieli manipulować pojęciami, takimi jak frazy odzyskiwania, deskryptory portfela lub ścieżki pochodne. Bez odpowiedniego przygotowania nawet spadkobierca o dobrych intencjach może popełnić nieodwracalne błędy.



## Jak działa dziedziczenie on-chain



Bitcoin wykorzystuje swój język skryptowy do kodowania warunków wydatków bezpośrednio w transakcjach. Dziedziczenie on-chain wykorzystuje tę programowalność do tworzenia alternatywnych ścieżek odzyskiwania, które aktywują się automatycznie.



### Zegary



Blokady czasowe są podstawowym mechanizmem dziedziczenia Bitcoin. Umożliwiają one blokowanie środków do momentu spełnienia określonego warunku czasowego.



**CLTV (CheckLockTimeVerify)**: Ta bezwzględna blokada czasowa sprawdza, czy określony czas (data lub wysokość bloku) został osiągnięty przed zatwierdzeniem wydatku. Na przykład "te środki mogą zostać wydane dopiero po bloku 900000" lub "po 1 stycznia 2026 r.". Zaletą CLTV jest to, że pozwala na duże opóźnienia (kilka lat), ale data jest stała i dotyczy identycznie wszystkich UTXO w portfelu. Aby zachować kontrolę nad swoimi środkami, należy okresowo tworzyć nowy portfel z wydłużoną datą wygaśnięcia i przenosić do niego swoje środki.



**CSV (CheckSequenceVerify)**: Ta względna blokada czasowa sprawdza, czy upłynęła określona liczba bloków od utworzenia UTXO. Na przykład "środki te mogą zostać wydane dopiero po 52560 blokach (~ 1 rok) od ich otrzymania". Zaletą CSV jest to, że każdy UTXO ma swój własny niezależny licznik. Za każdym razem, gdy wykonujesz transakcję, nowo utworzone UTXO resetują swój własny limit czasu. Jednak techniczny limit 65535 bloków (maksymalnie ~15 miesięcy) ogranicza możliwe ramy czasowe. Takie podejście jest bardziej naturalne w codziennym użytkowaniu, ponieważ normalna aktywność użytkownika automatycznie przesuwa terminy.



### Wiele ścieżek wydatków



Portfel dziedziczenia łączy kilka ścieżek wydatków w każdym adresie:





- Główna ścieżka** : Właściciel może wydać swoje środki w dowolnym momencie za pomocą klucza głównego, bez ograniczeń czasowych.
- Ścieżki odzyskiwania **: Jeden lub więcej kluczy alternatywnych może wydać środki dopiero po upływie określonego czasu.



Każda transakcja wykonana przez właściciela "odświeża" UTXO, tworząc nowe wyjścia z zresetowanymi zegarami. Mechanizm ten zapewnia, że dopóki właściciel pozostaje aktywny, ścieżki odzyskiwania nigdy się nie aktywują.



### Miniscript i Taproot



**Miniscript** to ustrukturyzowany język opracowany przez Andrew Poelstrę, Pietera Wuille'a i Sanketa Kanjalkara, który ułatwia pisanie i analizowanie złożonych skryptów Bitcoin. Umożliwia on tworzenie czytelnych i weryfikowalnych warunków wydawania, niezbędnych w przypadku konfiguracji dziedziczenia obejmujących wiele kluczy i zegarów.



**Taproot** (aktywowany w listopadzie 2021 r.) znacznie poprawia dziedziczenie on-chain. Dzięki drzewiastej strukturze (MAST), na blockchainie ujawniane są tylko wykorzystane warunki wydatkowania. Jeśli właściciel wyda swoje środki normalnie, warunki dziedziczenia pozostaną niewidoczne. Ta poufność zmniejsza również koszty transakcji w przypadku złożonych ścieżek.



## Kluczowe znaczenie deskryptorów



W przypadku starszych portfeli fraza odzyskiwania (seed) nie wystarcza do przywrócenia dostępu do środków. Krytycznym elementem staje się **deskryptor**.



Deskryptor to ciąg znaków, który wyczerpująco opisuje strukturę portfela: zaangażowane klucze publiczne, warunki wydatków, ścieżki derywacji i skonfigurowane zegary. Oto uproszczony przykład:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Ten deskryptor mówi: "albo klucz główny może zostać wydany natychmiast, albo klucz odzyskiwania może zostać wydany po 52560 blokach".



Rozpakujmy ten przykład:




- `wsh()` : Skrypt świadka Hash, wskazuje typ adresu (P2WSH)
- or_d()`: warunek "lub" z domyślną gałęzią
- pk([fingerprint/path]xpub...)`: Główny klucz publiczny z jego odciskiem palca i ścieżką derywacji
- and_v()`: warunek "and" łączący klucz odzyskiwania z blokadą czasową
- `older(52560)`: Względny czas blokady 52560 bloków



**Bez deskryptora, nawet przy użyciu wszystkich zwrotów odzyskiwania, spadkobiercy nie będą w stanie odbudować portfela.** Standardowy portfel można przywrócić tylko z seed, ponieważ podąża za standardowymi ścieżkami wyprowadzania (BIP44, BIP84). Z drugiej strony, starszy portfel wykorzystuje niestandardowe skrypty, których nie można odgadnąć. Kopia zapasowa deskryptora (lub plik konfiguracyjny wyeksportowany przez oprogramowanie) musi towarzyszyć frazom odzyskiwania w planie dziedziczenia.



## Dokumenty składające się na plan spadkowy



Poza mechanizmami technicznymi, skuteczny legacy plan opiera się na trzech filarach dokumentacji.



### List spadkowy



Ten osobisty list jest punktem wejścia do planu. Napisany dla spadkobierców, wyjaśnia kontekst i środki ostrożności, które należy podjąć.



List musi zawierać wyraźne zasady bezpieczeństwa:




- Nie spiesz się, poświęć trochę czasu na naukę przed przeniesieniem środków
- Nigdy nie przekazuj kompletnej frazy odzyskiwania pojedynczej osobie
- Nigdy nie wprowadzaj frazy odzyskiwania do niezweryfikowanego oprogramowania lub komputera
- Uważaj na oszustwa i osoby oferujące niezamówioną pomoc
- Przed podjęciem jakiejkolwiek decyzji zasięgnij porady co najmniej dwóch zaufanych osób



List ten zawiera również dane kontaktowe notariusza i lokalizację testamentu. Nigdy nie powinien zawierać fraz odzyskiwania danych ani haseł.



### Katalog zaufanych kontaktów



Żaden spadkobierca nie powinien sam zmagać się z odzyskiwaniem bitcoinów. Ten katalog zawiera listę osób, które mogą zapewnić pomoc techniczną lub prawną.



Dla każdej osoby kontaktowej udokumentuj: imię i nazwisko, relację z Tobą, rolę w planie, poziom zaufania, umiejętności Bitcoin i pełne dane kontaktowe. Podstawowa zasada: spadkobiercy powinni zawsze konsultować się z co najmniej dwiema różnymi osobami przed podjęciem jakiejkolwiek ważnej decyzji.



### Inwentaryzacja aktywów Bitcoin



Ta sekcja zawiera mapę wszystkich bitcoinów wraz z informacjami technicznymi potrzebnymi do ich odzyskania.



Dla każdego portfela należy udokumentować :




- Typ portfela**: sprzęt, oprogramowanie, konfiguracja (single-sig, multisig, legacy)
- Lokalizacja urządzenia**: fizyczna lokalizacja sprzętu wallet
- Lokalizacja pliku Descriptor/konfiguracji**: krytyczna dla zaawansowanych portfeli
- Lokalizacja frazy odzyskiwania**: oddzielnie od deskryptora
- Kody dostępu**: gdzie przechowywane są kody PIN i hasła
- Skonfigurowane opóźnienia**: kiedy aktywowane są ścieżki odzyskiwania



## Dostępne rozwiązania techniczne



Kilka pakietów oprogramowania implementuje mechanizmy dziedziczenia on-chain. Każdy z nich ma swoją własną charakterystykę techniczną.



### Liana



Liana to oprogramowanie desktopowe (Linux, macOS, Windows) wykorzystujące Miniscript do tworzenia portfeli z czasowymi ścieżkami odzyskiwania. Projekt jest rozwijany przez Wizardsardine, którego współzałożycielem jest Antoine Poinsot (współtwórca Bitcoin Core).



**Architektura techniczna**: Liana domyślnie tworzy portfele P2WSH (natywne dla SegWit), z obsługą Taproot dostępną w zależności od kompatybilności sprzętu wallet. Architektura opiera się na ścieżce głównej i jednej lub kilku ścieżkach odzyskiwania. Wygenerowany deskryptor koduje wszystkie warunki i musi zostać zapisany.



**Używane timelocki**: Liana używa względnych blokad czasowych (CSV), ograniczonych do 65535 bloków (~15 miesięcy). Aby zachować kontrolę, należy wykonać transakcję odświeżania przed wygaśnięciem blokady czasowej.



**Integracja sprzętowa wallet**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY i inne urządzenia są kompatybilne do podpisywania transakcji.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper to aplikacja mobilna (iOS, Android) łącząca multisig i timelocki poprzez "Enhanced Vaults". Podejście mobilne ze zintegrowanymi wskazówkami sprawia, że jest ona dostępna dla mniej zaawansowanych technicznie użytkowników.



**Architektura techniczna**: Enhanced Vaults wykorzystują Miniscript do tworzenia konfiguracji multisig, w których dodatkowe klucze aktywują się po określonych opóźnieniach. Klucz dziedziczenia dodaje się do istniejącego kworum, podczas gdy klucz awaryjny może całkowicie ominąć multisig.



**Używane timelocki**: Bitcoin Keeper używa bezwzględnych zegarów czasowych (CLTV), umożliwiając czas realizacji przekraczający 15 miesięcy. Data aktywacji jest ustawiana podczas tworzenia wallet i ma zastosowanie do wszystkich UTXO. Aplikacja zawiera funkcję "revaulting", która automatycznie zarządza odświeżaniem: użytkownik po prostu postępuje zgodnie z instrukcjami, bez konieczności ręcznego tworzenia nowego wallet.



**Dodatkowe funkcje**: Zintegrowane dokumenty dziedziczenia, Canary Wallets do wykrywania naruszenia kluczy i przypomnienia o odświeżeniu.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Dziedzictwo



Heritage to aplikacja desktopowa wykorzystująca skrypty Taproot do kodowania warunków dziedziczenia. Wykorzystanie Taproot zapewnia zwiększoną poufność, ponieważ nieużywane ścieżki pozostają niewidoczne w łańcuchu bloków.



**Architektura techniczna**: Każdy adres Heritage integruje główną ścieżkę i alternatywne ścieżki dla każdego spadkobiercy, z progresywnymi ramami czasowymi. Hierarchiczna struktura umożliwia zdefiniowanie osobistej kopii zapasowej w ciągu 6 miesięcy i spadkobierców rodzinnych w ciągu 12-15 miesięcy.



**Tryby użytkowania**: Samodzielna wersja z własnym węzłem (bezpłatna) lub usługa zarządzana dodająca przypomnienia i powiadomienia dla spadkobierców (0,05%/rok).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Proces odzyskiwania spadkobiercy



Zrozumienie procesu odzyskiwania pomaga przygotować skuteczny plan. Oto kroki techniczne, które spadkobierca będzie musiał wykonać.



### Wymagania dotyczące odzyskiwania



Spadkobierca potrzebuje :


1. **deskryptor lub plik konfiguracyjny** oryginalnego portfela (format JSON lub tekstowy, w zależności od oprogramowania)


2. **jego fraza odzyskiwania** (ta powiązana z jego kluczem dziedziczenia, zwykle 12 lub 24 słowa)


3. **Kompatybilne oprogramowanie** (Liana, Bitcoin Keeper, Heritage lub Sparrow/Specter dla standardowych deskryptorów)


4. **Połączenie z węzłem Bitcoin** w celu sprawdzenia stanu blokady czasowej i rozgłaszania transakcji



### Kroki odzyskiwania



1. **Zainstaluj oprogramowanie** na bezpiecznym urządzeniu i skonfiguruj połączenie z siecią Bitcoin (węzeł osobisty lub serwer Electrum)


2. **Import deskryptora** w celu odtworzenia struktury portfela. Oprogramowanie automatycznie generate wszystkie używane adresy


3. **Przywróć klucz dziedziczenia** z frazy odzyskiwania. Oprogramowanie sprawdzi, czy ten klucz odpowiada jednemu z kluczy autoryzowanych w deskryptorze


4. **Synchronizuj portfolio**, aby odkryć wszystkie UTXO i ich warunki wydatków


5. **Sprawdź wygaśnięcie blokady czasowej**: oprogramowanie wskaże dla każdego UTXO, czy ścieżka odzyskiwania jest aktywna


6. **Utworzyć transakcję odzyskiwania** na adres kontrolowany wyłącznie przez spadkobiercę (najlepiej nowy pojedynczy wallet)


7. **Podpisanie i rozgłaszanie** transakcji w sieci Bitcoin



Jeśli blokada czasowa jeszcze nie wygasła, spadkobierca będzie musiał poczekać. Oprogramowanie wyświetli datę lub blok, od którego odzyskanie środków stanie się możliwe. Podczas tego okresu oczekiwania środki pozostają bezpieczne w łańcuchu bloków.



### Punkty, na które należy zwrócić uwagę w przypadku spadkobiercy



Spadkobierca musi zwrócić szczególną uwagę na :




- Sprawdzanie autentyczności pobranego oprogramowania** (sumy kontrolne, podpisy)
- Nigdy nie dziel się swoją frazą dotyczącą powrotu do zdrowia** z nikim, kto oferuje pomoc
- Przed przystąpieniem do odzyskiwania danych skonsultuj się z co najmniej dwiema zaufanymi osobami**
- Przeniesienie środków do prostego portfela**, który będzie w pełni kontrolowany po powrocie do zdrowia



## Najlepsze praktyki



### Rozdzielenie informacji



Nigdy nie należy przechowywać wszystkich informacji w jednym miejscu. Deskryptor musi być oddzielony od fraz odzyskiwania, które z kolei są oddzielone od kodów PIN. Taka dystrybucja utrudnia dostęp atakującemu, a jednocześnie pozostaje możliwa do odtworzenia przez prawowitych spadkobierców.



### Testy odzyskiwania



Przed zdeponowaniem znacznych środków należy przetestować cały proces odzyskiwania przy użyciu niewielkiej kwoty. Sprawdź, czy możesz przywrócić portfel z deskryptora i fraz odzyskiwania na pustym urządzeniu. Udokumentuj kroki dla swoich spadkobierców.



### Konserwacja blokady czasowej



Odświeżanie blokad czasowych należy zaplanować na długo przed ich wygaśnięciem. W przypadku 12-miesięcznej blokady czasowej należy przeprowadzać transakcję co 9-10 miesięcy. Oprogramowanie zazwyczaj oferuje funkcje przypomnień lub automatycznego odświeżania.



### Aktualizacja planu



Konfiguracja Bitcoin ewoluuje. Każda istotna zmiana (nowy portfel, modyfikacja terminów, dodanie spadkobiercy) musi zostać odzwierciedlona w dokumentacji. Ustanowienie rutynowego corocznego przeglądu.



## Wybór podejścia



Wybór między różnymi rozwiązaniami zależy od profilu technicznego i konkretnych potrzeb.



**Liana** jest odpowiedni dla użytkowników komputerów stacjonarnych, którzy preferują oprogramowanie open source z pełną kontrolą za pośrednictwem własnego węzła. Konfiguracja pozostaje dostępna dzięki interfejsowi z przewodnikiem. Względne zegary (CSV) upraszczają konserwację, ponieważ normalna aktywność automatycznie przesuwa terminy. Ograniczenie: maksymalne opóźnienie ok. 15 miesięcy (65535 bloków).



*aplikacja *Bitcoin Keeper** skierowana jest do użytkowników mobilnych poszukujących intuicyjnego interfejsu ze zintegrowanymi dokumentami towarzyszącymi. Aplikacja oferuje dwa rodzaje kluczy specjalnych: klucz dziedziczenia (który zwiększa kworum) i klucz awaryjny (który całkowicie je omija). Bezwzględne blokady czasowe (CLTV) umożliwiają czas realizacji przekraczający 15 miesięcy, a zintegrowana funkcja revaultingu upraszcza odświeżanie. Plan Diamond Hands odblokowuje zaawansowane starsze funkcje.



**Dziedziczenie** jest przeznaczone dla użytkowników technicznych, którzy cenią sobie poufność Taproot i hierarchiczne dziedziczenie z progresywnymi opóźnieniami. Struktura drzewa Taproot ukrywa warunki dziedziczenia podczas normalnych transakcji, ujawniając tylko warunek używany podczas odzyskiwania.



Wszystkie trzy rozwiązania mają jedną wspólną cechę: wymagają okresowego odświeżania, aby zapobiec przedwczesnej aktywacji ścieżek odzyskiwania. To ograniczenie jest zarówno ceną, jak i gwarancją niezaufanego dziedzictwa on-chain. Zaplanuj regularne przypomnienia i uczyń tę konserwację częścią rutyny zarządzania Bitcoin.



## Wnioski



Techniczny plan Bitcoin łączy mechanizmy kryptograficzne (timelocki, Miniscript, Taproot) z rygorystyczną dokumentacją. Zaawansowane portfele umożliwiają automatyczne przesyłanie bitcoinów po okresie bezczynności, bez interwencji osób trzecich.



Najważniejsze elementy, które należy przekazać spadkobiercom to: deskryptor lub plik konfiguracyjny, fraza odzyskiwania, szczegółowe instrukcje odzyskiwania oraz dane kontaktowe kompetentnych osób, które mogą im pomóc.



Zacznij od wyboru rozwiązania technicznego dopasowanego do Twojego profilu, przetestuj je z niewielką ilością, a następnie udokumentuj całość w ustrukturyzowanym planie. Początkowa złożoność gwarantuje, że aktywa Bitcoin zostaną przekazane z pełnym zaufaniem.



## Zasoby



### Szablon planu dziedziczenia





- [Szablon planu spadkowego Bitcoin (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Szablon dokumentacji Plan ₿ Network



### Referencje techniczne





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Specyfikacja absolutnych zegarów czasowych (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Specyfikacja względnych zegarów (CSV)
- [Miniscript Reference](https://bitcoin.sipa.be/miniscript/) - Oficjalna dokumentacja Miniscript autorstwa Pieter Wuille



### Oficjalne strony internetowe z rozwiązaniami





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Dziedzictwo Wallet](https://btc-heritage.com/) - Crypto7