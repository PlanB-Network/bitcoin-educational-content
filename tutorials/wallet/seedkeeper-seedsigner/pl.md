---
name: Seedkeeper x SeedSigner
description: Jak używać Seedkeeper z moim SeedSigner?
---

![cover](assets/cover.webp)



*Podziękowania dla zespołu [Satochip](https://satochip.io/) za zgodę na ponowne wykorzystanie [ich filmów](https://www.youtube.com/@satochip/videos) w tym samouczku. Podziękowania również dla [Crypto Guide](https://www.youtube.com/@CryptoGuide/) za fork oprogramowania układowego SeedSigner, umożliwiającego obsługę kart inteligentnych



---

SeedSigner to sprzęt wallet, który można samodzielnie zmontować ze standardowego sprzętu, zwykle wokół Raspberry Pi Zero. Ten wallet jest nazywany "*stateless*": w przeciwieństwie do większości innych modeli na rynku (Coldcard, Trezor, Ledger itp.), nie przechowuje żadnych danych w pamięci stałej i działa tylko na żywo z pamięci RAM. W rezultacie seed portfela nigdy nie jest przechowywany w SeedSigner. Przy każdym ponownym uruchomieniu należy go wypełnić, aby urządzenie mogło podpisywać transakcje. Najpopularniejszą metodą jest zapisanie seed jako kodu QR, który następnie skanuje się za każdym razem, gdy się go używa (*SeedQR*).



Podejście to wiąże się jednak ze znacznym ryzykiem: seed musi pozostać dostępny w postaci czystego tekstu, aby można go było zeskanować. W przypadku kradzieży lub włamania, atakujący może z łatwością wejść w jego posiadanie i ukraść bitcoiny użytkownika.



Aby przezwyciężyć tę słabość, SeedSigner można połączyć z [**Seedkeeper**](https://satochip.io/product/seedkeeper/), inteligentną kartą opracowaną przez Satochip. Umożliwia to przechowywanie fraz mnemonicznych (lub innych sekretów) w secure element chronionym kodem PIN. Aplet Seedkeeper jest open-source, a jego secure element posiada certyfikat EAL6+. Używany w połączeniu z SeedSigner, oferuje bardzo interesującą funkcję bezpieczeństwa: klucze pozostają zarządzane całkowicie offline, transakcje są podpisywane na zaufanym ekranie, a seed jest fizycznie chroniony na karcie inteligentnej odpornej na ataki fizyczne.



Do ukończenia instalacji potrzebne są tylko następujące elementy:




- Zwykły sprzęt potrzebny do klasycznego SeedSigner: Raspberry Pi Zero, ekran Waveshare 1,3", kompatybilna kamera i karta microSD (więcej szczegółów znajdziesz w samouczku SeedSigner poniżej);
- Zestaw rozszerzeń SeedSigner, dostępny [w oficjalnym sklepie Satochip](https://satochip.io/product/seedsigner-extension-kit/), który umożliwia odczyt i zapis na karcie inteligentnej bezpośrednio z SeedSigner. Inną opcją jest użycie zewnętrznego czytnika kart inteligentnych, który można podłączyć kablem do portu Micro-USB w Raspberry Pi. Nie testowałem jednak tego rozwiązania osobiście;
- Seedkeeper lub alternatywnie pusta karta inteligentna, na której można zainstalować aplet Seedkeeper (zestaw rozszerzeń sprzedawany przez Satochip zawiera już pustą kartę inteligentną).



![Image](assets/fr/01.webp)



Ten samouczek obejmuje dwa scenariusze:




- Jeśli masz już portfel Bitcoin zarządzany za pośrednictwem SeedSigner, po prostu zainstaluj nowe oprogramowanie układowe. Następnie możesz nadal korzystać z istniejącego wallet, tym razem używając Seedkeeper dla dodatkowego bezpieczeństwa.
- Jeśli nie masz jeszcze Bitcoin wallet powiązanego z SeedSigner, musisz wykonać kroki **5** i **6** samouczka wspomnianego poniżej. Sekcje te wyjaśniają, jak utworzyć frazę mnemoniczną generate za pomocą SeedSigner, zapisać ją za pomocą *SeedQR*, a następnie podłączyć wallet do Sparrow Wallet, aby nią zarządzać. Nie będę tutaj zagłębiał się w te procedury i **zakładam, że masz już działający Bitcoin wallet, skonfigurowany z Sparrow i SeedSigner**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Instalacja oprogramowania sprzętowego



Aby używać SeedSigner z Seedkeeper, musisz zainstalować alternatywne oprogramowanie układowe, inne niż oryginalne SeedSigner, w celu obsługi odczytu kart inteligentnych. W tym celu [zalecam użycie fork z "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Pobierz [najnowszą wersję obrazu](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) odpowiadającą używanemu modelowi Raspberry Pi.



![Image](assets/fr/02.webp)



Jeśli jeszcze go nie masz, pobierz oprogramowanie [Balena Etcher] (https://etcher.balena.io/), a następnie wykonaj następujące czynności:




- Włóż kartę microSD do komputera;
- Launch Etcher ;
- Wybierz właśnie pobrany plik `.zip`;
- Wybierz kartę microSD jako cel;
- Kliknij na `Flash!`.



![Image](assets/fr/03.webp)



Poczekaj na zakończenie procesu: karta microSD jest teraz gotowa do użycia. Możesz teraz przejść do montażu urządzenia.



Aby uzyskać więcej informacji na temat instalacji oprogramowania układowego i weryfikacji oprogramowania (co zdecydowanie zalecam), zapoznaj się z poniższym samouczkiem:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Montaż czytnika kart inteligentnych



![video](https://youtu.be/jqE8HDMCImA)



Zacznij od zainstalowania kamery na Raspberry Pi Zero, ostrożnie wkładając ją do bolca kamery i blokując czarną wypustką. Następnie umieść Pi na spodzie obudowy, upewniając się, że porty są wyrównane z odpowiednimi otworami.



![Image](assets/fr/04.webp)



Następnie podłącz czytnik kart inteligentnych do pinów GPIO Raspberry Pi Zero.



![Image](assets/fr/05.webp)



Nasuń plastikową osłonę na czytnik kart inteligentnych, aż zostanie prawidłowo umieszczona.



![Image](assets/fr/06.webp)



Następnie dodaj ekran do pinów GPIO rozszerzenia.



![Image](assets/fr/07.webp)



Na koniec włóż kartę microSD zawierającą oprogramowanie sprzętowe do bocznego portu Raspberry Pi Zero.



![Image](assets/fr/08.webp)



Możesz teraz podłączyć SeedSigner albo przez port Micro-USB Raspberry Pi Zero, albo przez port USB-C rozszerzenia. Obie opcje działają. Poczekaj kilka sekund na uruchomienie, a następnie powinien pojawić się ekran powitalny.



![Image](assets/fr/09.webp)



Aby uzyskać więcej informacji na temat początkowej konfiguracji SeedSigner, polecam poniższy samouczek:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Flashowanie karty inteligentnej za pomocą apletu Seedkeeper (opcjonalnie)



![video](https://youtu.be/NF4HemyEcOY)



Jeśli posiadasz już Seedkeeper, możesz pominąć ten krok i przejść od razu do kroku 4. W tej sekcji przyjrzymy się, jak zainstalować aplet Seedkeeper na pustej karcie inteligentnej (metoda DIY).



Aby rozpocząć, otwórz menu `Tools > Smartcard Tools` w SeedSigner.



![Image](assets/fr/10.webp)



Następnie wybierz `DIY Tools > Install Applet`.



![Image](assets/fr/11.webp)



Włóż kartę do czytnika SeedSigner chipem do dołu, a następnie wybierz aplet `SeedKeeper`.



![Image](assets/fr/12.webp)



Prosimy o cierpliwość podczas instalacji: proces może potrwać kilkadziesiąt sekund.



![Image](assets/fr/13.webp)



Po pomyślnym zainstalowaniu apletu można przejść do kroku 4.



![Image](assets/fr/14.webp)



## 4. Zapisz istniejący SeedQR w Seedkeeper



![video](https://youtu.be/X-vmFHU9Ec8)



Teraz, gdy Seedkeeper działa, można zapisać mnemonik Bitcoin wallet na karcie inteligentnej. Aby rozpocząć, włącz SeedSigner jak zwykle, a następnie zeskanuj *SeedQR* wallet, aby załadować go do urządzenia. Po zaimportowaniu seed, po prostu wybierz `Done`.



![Image](assets/fr/15.webp)



Po załadowaniu seed przejdź do menu `Backup Seed`.



![Image](assets/fr/16.webp)



Następnie włóż swój Seedkeeper do napędu SeedSigner i wybierz opcję `To SeedKeeper`.



![Image](assets/fr/17.webp)



Następnie SeedSigner poprosi o wprowadzenie kodu PIN dla Seedkeeper. Ponieważ jest to pusta karta, żaden kod nie został jeszcze zdefiniowany. Wprowadź dowolny kod, aby pominąć ten krok, a następnie zatwierdź.



![Image](assets/fr/18.webp)



SeedSigner wykrywa, że Seedkeeper nie został jeszcze zainicjowany (tj. nie ustawiono hasła). Kliknij "Rozumiem", aby kontynuować.



![Image](assets/fr/19.webp)



Teraz wybierz nowy kod PIN Seedkeepera, składający się z od 4 do 16 znaków. Aby zwiększyć bezpieczeństwo, wybierz długi, losowy kod: jest to jedyna bariera chroniąca fizyczny dostęp do frazy mnemonicznej.



Pamiętaj, aby zapisać ten kod PIN natychmiast po jego utworzeniu, albo w niezawodnym menedżerze haseł, albo na oddzielnym nośniku fizycznym, w zależności od strategii. W tym drugim przypadku należy pamiętać, aby nigdy nie przechowywać nośnika zawierającego PIN w tym samym miejscu co Seedkeeper, w przeciwnym razie ochrona stanie się nieskuteczna. Ważne jest, aby mieć kopię zapasową: **Bez tego kodu PIN nie będzie można uzyskać dostępu do seed, a bitcoiny zostaną utracone**.



![Image](assets/fr/20.webp)



Następnie można zdefiniować `Label` powiązaną z frazą mnemoniczną. Ta etykieta jest przydatna, jeśli przechowujesz kilka sekretów w Seedkeeper, dzięki czemu możesz je łatwo zidentyfikować.



![Image](assets/fr/21.webp)



Fraza mnemoniczna została zapisana na karcie inteligentnej.



![Image](assets/fr/22.webp)



Jeśli chodzi o strategię bezpieczeństwa, możliwe jest kilka podejść, w zależności od potrzeb i poziomu narażenia na ryzyko. Osobiście zalecam przechowywanie co najmniej 2 kopii seed:




- Jest to pierwsze rozwiązanie w przypadku kart inteligentnych, które mogą być łatwo dostępne do codziennych operacji, takich jak weryfikacja adresów lub podpisywanie transakcji. Ta metoda jest praktyczna (jak zobaczymy w części 5) i pozostaje bezpieczna dzięki ochronie oferowanej przez kod PIN, dzięki czemu można zachować do niej dostęp bez większego ryzyka;
- Druga kopia niezaszyfrowanej frazy mnemonicznej, służąca jako ostateczna kopia zapasowa portfela, używana tylko w przypadku utraty lub kradzieży Seedkeepera. Ponieważ ta wersja jest niezaszyfrowana, musi być przechowywana w oddzielnej, bezpieczniejszej lokalizacji, aby zapobiec jednoczesnemu naruszeniu 2 kopii zapasowych.



W zależności od strategii ochrony i profilu ryzyka można również powielić seed na kilku różnych Seedkeeperach lub utworzyć kilka fizycznych kopii mnemonika. Aby dowiedzieć się więcej o tych praktykach, zapoznaj się z poniższym samouczkiem:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Ładowanie seed z Seedkeeper



![video](https://youtu.be/ms0Iq_IyaoE)



Możesz teraz użyć Seedkeepera, aby załadować swoją frazę mnemoniczną do SeedSignera podczas uruchamiania, a tym samym podpisać transakcje Bitcoin. Aby rozpocząć, włącz SeedSigner, podłączając go, a następnie otwórz menu `Seeds`.



![Image](assets/fr/23.webp)



Następnie wybierz opcję `From SeedKeeper`.



![Image](assets/fr/24.webp)



Włóż Seedkeeper do czytnika kart inteligentnych, a następnie wprowadź kod PIN, aby go odblokować. Potwierdź wprowadzenie, naciskając prawy dolny przycisk potwierdzenia, `KEY3`.



![Image](assets/fr/25.webp)



Seedkeeper może zawierać kilka sekretów, więc SeedSigner wyświetli monit o wybranie tego, który chcesz załadować. Wyświetlana etykieta odpowiada nazwie zdefiniowanej w kroku 4. Jeśli, tak jak w moim przypadku, zarejestrowałeś tylko jeden seed, dostępna będzie tylko jedna opcja.



![Image](assets/fr/26.webp)



Urządzenie seed jest teraz załadowane. Sprawdź, czy jest to prawidłowy wallet, porównując odcisk palca wyświetlany na ekranie z odciskiem określonym w ustawieniach Sparrow Wallet. Ten odcisk palca został również podany podczas pierwszego tworzenia wallet.



Jeśli używasz passphrase, możesz go zastosować na tym etapie (patrz część 6 tego samouczka). W przeciwnym razie po prostu kliknij `Done`.



![Image](assets/fr/27.webp)



Następnie możesz normalnie korzystać z wallet: sprawdzać adresy dostawy i podpisywać transakcje, tak jak w przypadku klasycznego SeedSigner. Aby dowiedzieć się więcej o tym, jak z niego korzystać, zapoznaj się z dedykowanym samouczkiem :



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Korzystanie z Seedkeeper z passphrase BIP39



Czy używasz passphrase do ochrony swojego portfela Bitcoin? Możesz go również zarejestrować w swoim Seedkeeperze, razem z seed. To rozwiązanie umożliwi szybkie załadowanie wallet do SeedSigner, bez konieczności ręcznego wprowadzania passphrase na małej klawiaturze za każdym razem, gdy go używasz.



Uważam, że ta metoda jest szczególnie interesująca, ponieważ pozwala korzystać z zalet bezpieczeństwa passphrase, eliminując jednocześnie ograniczenia związane z jego codziennym użytkowaniem. Oto przykład konfiguracji, którą polecam:




- Przechowuj seed i passphrase w Seedkeeper, chronionym silnym kodem PIN (to ważne). Ta kopia zapasowa umożliwi łatwe korzystanie z wallet na co dzień. Jeśli chcesz, możesz powielić te informacje na drugim urządzeniu Seedkeeper;
- Zachowaj również wyraźną kopię swojego mnemonika i passphrase, na papierze lub metalu. Jest to kopia zapasowa na wypadek utraty Seedkeepera lub kodu PIN. Pamiętaj, aby przechowywać te kopie w oddzielnych lokalizacjach, aby nie mogły zostać naruszone jednocześnie.



W tej konfiguracji, jeśli ktoś dostanie w swoje ręce sam mnemonik w postaci zwykłego tekstu, nie będzie w stanie nic ukraść bez znajomości passphrase (oczywiście pod warunkiem, że jest on wystarczająco silny, aby wytrzymać atak brute-force). I odwrotnie, jeśli ktoś odkryje twój passphrase w postaci zwykłego tekstu, pozostanie on bezużyteczny bez odpowiedniej frazy mnemonicznej.



Wreszcie, jeśli komuś uda się uzyskać fizyczny dostęp do Seedkeepera zawierającego seed i passphrase, nie będzie w stanie niczego wydobyć bez znajomości kodu PIN. W przeciwieństwie do passphrase, kod ten nie może być brutalnie wymuszony, ponieważ karta automatycznie blokuje się po 5 nieprawidłowych próbach.



Bezpieczeństwo tej konfiguracji opiera się zatem na 2 zasadniczych punktach:




- **passphrase strong**: musi być długi, losowy i zawierać wiele różnych znaków. Jego złożoność nie stanowi problemu, ponieważ wystarczy wprowadzić go tylko raz na klawiaturze podczas inicjalizacji; następnie zostanie przesłany przez Seedkeeper ;
- **Silny kod PIN** dla Seedkeeper: również losowy i składający się z 16 znaków.



Aby skonfigurować tę konfigurację, zacznij od załadowania passphrase do SeedSigner w zwykły sposób. Możesz postępować zgodnie z procedurą opisaną w tym samouczku:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Po prawidłowym załadowaniu portfela z passphrase do SeedSigner, otwórz menu `Seeds` i wybierz footprint odpowiadający temu portfelowi. Należy pamiętać, że ślad ten różni się od śladu portfela bez passphrase.



![Image](assets/fr/28.webp)



Następnie kliknij `Backup Seed`, włóż Seedkeeper do napędu i wybierz `To SeedKeeper`.



![Image](assets/fr/29.webp)



Wprowadź kod PIN, aby odblokować Seedkeeper, a następnie przypisz etykietę do tego sekretu. Możesz pozostawić odcisk palca jako etykietę, aby zachować pewną formę wiarygodnego zaprzeczenia, lub na przykład wyraźnie określić `Passphrase Wallet`.



![Image](assets/fr/30.webp)



Twoje portfolio passphrase jest teraz zarejestrowane w Seedkeeper.



![Image](assets/fr/31.webp)



Przy następnym uruchomieniu wystarczy włożyć Seedkeeper do napędu, a następnie przejść do `Seeds > From SeedKeeper`.



![Image](assets/fr/32.webp)



Wprowadź kod PIN, aby odblokować kartę inteligentną, a następnie wybierz wallet odpowiadający passphrase.



![Image](assets/fr/33.webp)



Sprawdź odcisk passphrase i wallet, a następnie potwierdź.



![Image](assets/fr/34.webp)



Możesz teraz uzyskać dostęp do swojego portfela za pomocą passphrase i podpisywać swoje transakcje tak, jak normalnie w SeedSigner.



## 7. Dodatkowe opcje



W menu `Tools > Smartcard Tools` znajdziesz kilka opcji zarządzania Seedkeeperem:





- W menu `Narzędzia wspólne` można :
 - Sprawdź autentyczność karty;
 - Zmiana kodu PIN ;
 - Zmień etykiety powiązane z sekretami ;
 - Wyłączenie funkcji NFC (zalecane w przypadku korzystania wyłącznie z czytnika chipów) ;
 - Przywrócenie ustawień fabrycznych.





- W menu `SeedKeeper Functions` można :
 - Sprawdź listę zarejestrowanych tajemnic ;
 - Zapisz nowy sekret ;
 - Usuń istniejący klucz tajny ;
 - Zapisz lub załaduj deskryptory (przydatna funkcja dla portfeli multi-sig).





- W menu `DIY Tools` możesz :
 - Kompilacja apletu Seedkeeper ;
 - Zainstaluj aplet na pustej karcie;
 - Usuń aplet Seedkeeper, aby go zresetować i ponownie uczynić pustym.



Teraz już wiesz, jak używać Seedkeeper do bezpiecznego tworzenia kopii zapasowych portfela w połączeniu z SeedSigner.



Jeśli ta konfiguracja cię przekonała, nie wahaj się wspierać projektów, które to umożliwiają:




- Kupując sprzęt bezpośrednio [na stronie internetowej Satochip] (https://satochip.io/shop/);
- Przekazując [darowiznę na rzecz projektu SeedSigner](https://seedsigner.com/donate/);
- Subskrybując kanał YouTube [Crypto Guide] (https://www.youtube.com/@CryptoGuide/), prowadzony przez osobę, która utrzymuje repozytorium GitHub zawierające zmodyfikowane oprogramowanie układowe.