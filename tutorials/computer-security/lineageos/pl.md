---
name: LineageOS
description: Darmowy, nieskomplikowany system operacyjny Android dla smartfonów
---

![cover](assets/cover.webp)



Konwencjonalne systemy Android preinstalowane na naszych smartfonach stwarzają szereg dobrze znanych problemów: intensywna integracja usług Google prowadząca do ciągłego śledzenia danych, niechciane sponsorowane aplikacje (bloatware) narzucane przez producentów oraz porzucenie śledzenia aktualizacji po kilku latach, skazując wciąż działające urządzenia na zaprogramowaną przestarzałość.



LineageOS prezentuje się jako elegancka odpowiedź na te problemy. LineageOS, produkt społeczności open source i bezpośredni następca CyanogenMod (wycofanego pod koniec 2016 roku), to darmowy mobilny system operacyjny oparty na Androidzie, który przywraca użytkownikom kontrolę nad ich smartfonami. Oficjalnie uruchomiony w grudniu 2016 roku projekt może pochwalić się obecnie ponad 4,4 milionami aktywnych instalacji na całym świecie i obsługuje setki modeli telefonów ponad 20 różnych marek.



![lineageos-homepage](assets/fr/01.webp)



*Oficjalna strona LineageOS prezentująca projekt i jego cele*



## Czym jest LineageOS?



### Filozofia i cele



LineageOS to mobilny system operacyjny typu open source oparty na Android Open Source Project (AOSP), rozwijany przez ogromną społeczność wolontariuszy na całym świecie. Jego nieoficjalnym mottem może być "Twoje urządzenie, twoje zasady": projekt ma na celu wydłużenie żywotności smartfonów, oferując jednocześnie usprawnione, przyjazne dla prywatności doświadczenie Androida.



Projekt powstał z popiołów CyanogenMod, jednego z najpopularniejszych alternatywnych ROM-ów Androida w historii. Kiedy CyanogenMod Inc. zamknął swoje podwoje w grudniu 2016 roku, społeczność zmobilizowała się do stworzenia LineageOS, zachowując ducha innowacji i filozofię open-source, która charakteryzowała jego poprzednika.



W przeciwieństwie do dystrybucji OEM Androida, LineageOS nie instaluje domyślnie żadnych aplikacji Google i całkowicie eliminuje bloatware. Użytkownicy zaczynają od minimalistycznego systemu zawierającego tylko niezbędne aplikacje (telefon, wiadomości, aparat, przeglądarka) i mogą swobodnie wybierać, co dodać później.



### Wpływ i społeczność



Oficjalne statystyki ujawniają skalę projektu: z ponad 4,4 milionami aktywnych instalacji w 224 krajach, LineageOS stanowi jedną z najbardziej rozpowszechnionych alternatyw dla Androida na świecie. Brazylia jest liderem z ponad 2 milionami użytkowników, a za nią plasują się Chiny i USA, co pokazuje uniwersalną atrakcyjność darmowego, konfigurowalnego Androida.




## Główne cechy



### Interface i doświadczenie użytkownika



**Czysty Android**: LineageOS oferuje autentyczne doświadczenie Androida zbliżone do AOSP, bez nakładek producenta i zbędnych aplikacji. Interface pozostaje znajomy dla użytkowników Androida, oferując jednocześnie optymalną płynność dzięki braku bloatware.



** Domyślnie bez Google**: Żadne usługi Google nie są preinstalowane ze względów prawnych i etycznych. To "wolne od Google" podejście gwarantuje całkowitą kontrolę nad danymi osobowymi i poprawia wydajność poprzez unikanie usług działających w tle.



### Personalizacja i bezpieczeństwo



**Zaawansowana personalizacja**: LineageOS odblokowuje wiele opcji niedostępnych w standardowym systemie Android: rekonfiguracja przycisków nawigacyjnych, konfigurowalne motywy systemowe, profile użytkowania dostosowane do różnych kontekstów (praca, życie osobiste, gry).



**Outil Trust**: Zintegrowana funkcja, która monitoruje stan bezpieczeństwa urządzenia i ostrzega o potencjalnych zagrożeniach, zapewniając wgląd w bezpieczeństwo systemu w czasie rzeczywistym.



**Rozszerzone aktualizacje**: Społeczność LineageOS jest zaangażowana w dostarczanie comiesięcznych poprawek zabezpieczeń, umożliwiając urządzeniom wycofanym przez ich producentów dalsze otrzymywanie najnowszych poprawek zabezpieczeń Androida.



## Kompatybilne urządzenia



LineageOS obsługuje setki urządzeń od ponad 20 producentów: Samsung, Xiaomi, OnePlus, Motorola, Sony, Google Pixel, Fairphone i wielu innych. Ta szeroka kompatybilność jest jedną z głównych zalet projektu w porównaniu z alternatywami, takimi jak GrapheneOS, które są ograniczone do urządzeń Pixel.



![devices-compatibility](assets/fr/02.webp)



*Strona urządzeń kompatybilnych z LineageOS z filtrami według producenta*



![google-devices](assets/fr/03.webp)



*Obsługiwane urządzenia Google, w tym Pixel 4 (nazwa kodowa "flame")*



### Popularne urządzenia



Według oficjalnych statystyk, najczęściej używane modele obejmują różne urządzenia w różnych przedziałach cenowych i wiekowych, co pokazuje zdolność LineageOS do tchnięcia nowego życia w starsze smartfony, a także optymalizacji nowszych.



### Najważniejsze punkty przed instalacją



**Odblokowany bootloader**: Sprawdź, czy Twój producent/operator zezwala na odblokowanie. Niektóre marki, takie jak Huawei, zrezygnowały z tej możliwości w najnowszych modelach, podczas gdy inne narzucają określone procedury.



**Dokładny model**: Ważne jest, aby pobrać ROM, który dokładnie odpowiada Twojemu urządzeniu. Dwa modele o podobnych nazwach handlowych mogą różnić się pod względem technicznym (na przykład Galaxy S10 vs S10 5G) i wymagać różnych obrazów.



**Skalowalne wsparcie**: Nowsze urządzenia mogą nie być obsługiwane od razu, ponieważ portowanie wymaga dewelopera-wolontariusza, który się nimi zajmie. I odwrotnie, wsparcie może zostać wstrzymane, jeśli opiekun urządzenia wycofa się z projektu.



## Instalacja



### Niezbędne warunki wstępne



⚠️ **Przeczytaj całą instrukcję przed rozpoczęciem**, aby uniknąć jakichkolwiek problemów!



**Przywrócenie fabrycznego oprogramowania układowego (jeśli to konieczne) :**




- Narzędzie Android Flash**: Użyj oficjalnego narzędzia Google [flash.android.com](https://flash.android.com), aby łatwo przywrócić urządzenie Pixel do standardowego systemu Android z poziomu przeglądarki internetowej (wymagany Chrome/Edge)
- Alternatywa**: Obrazy fabryczne ręcznie z [developers.google.com/android/images](https://developers.google.com/android/images)



**Obowiązkowe testy wstępne:**




- Uruchom urządzenie co najmniej raz** z oryginalnym systemem fabrycznym
- Przetestuj wszystkie funkcje**: SMS, połączenia, Wi-Fi, dane mobilne
- Ważne**: Sprawdź, czy możesz wysyłać/odbierać wiadomości SMS i wykonywać/odbierać połączenia (w tym przez WiFi i 4G/5G). Jeśli nie działa na systemie stockowym, nie będzie też działać na LineageOS!
- Najnowsze urządzenia**: Niektóre z nich wymagają użycia VoLTE/VoWiFi przynajmniej raz w systemie stockowym w celu udostępnienia IMS



**Przygotowanie systemu:**




- Usuń wszystkie konta Google** z urządzenia, aby uniknąć ochrony przed przywróceniem ustawień fabrycznych, która może zablokować aktywację
- Pełna kopia zapasowa** : Proces ten spowoduje całkowite usunięcie telefonu. Tworzenie kopii zapasowych zdjęć, kontaktów, aplikacji i ważnych plików



**Narzędzia ADB i Fastboot:** Postępuj zgodnie z [oficjalnym przewodnikiem LineageOS](https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot), aby zainstalować narzędzia platformy Android SDK. Zweryfikuj instalację za pomocą `adb version` i `fastboot --version`.



**Konfiguracja telefonu:**




- Aktywuj **Opcje deweloperskie**: Ustawienia > Informacje > dotknij "Numer kompilacji" 7 razy



![android-version](assets/fr/06.webp)



*Przejdź do Ustawienia > Informacje o telefonie, aby aktywować tryb programisty*





- Włącz **Debugowanie USB** w opcjach programisty
- Aktywuj **OEM Unlock** (niezbędne do odblokowania bootloadera)



![developer-options](assets/fr/07.webp)



*Włącz opcje programisty, debugowanie USB i odblokowywanie OEM*



### Szczegółowa instalacja



⚠️ **Instrukcje te są specyficzne dla LineageOS 22.2. Postępuj dokładnie według każdego kroku. Nie kontynuuj, jeśli coś się nie powiedzie!



#### Krok 1: Sprawdzenie oprogramowania sprzętowego



**Wymagane oprogramowanie**: Twoje urządzenie musi mieć zainstalowany system Android 13 przed kontynuowaniem (dla Pixel 4). Oprogramowanie układowe odnosi się do obrazów specyficznych dla urządzenia zawartych w systemie stockowym.



![pixel4-info](assets/fr/04.webp)



*Oficjalna strona Pixel 4 z linkami do pobrania i instrukcjami instalacji*



![downloads-page](assets/fr/05.webp)



*Strona pobierania kompilacji LineageOS i pliki*



**Pixel 4 specyficzne pliki do pobrania:**




- Zbuduj LineageOS**: [download.lineageos.org/devices/flame/builds](https://download.lineageos.org/devices/flame/builds)
- Wymagane pliki**: Pobierz 3 wymagane pliki z tej strony (będą one używane w kolejnych krokach):
  - `lineage-22.2-YYYYMMDD-nightly-flame-signed.zip` (główna pamięć ROM)
  - dtbo.img` (drzewo partycji blob)
  - `boot.img` (recovery LineageOS)



⚠️ **Ważne**: Sprawdź wersję Androida, a nie wersję systemu operacyjnego producenta. Korzystanie z niestandardowej pamięci ROM (nawet LineageOS) nie gwarantuje spełnienia tego wymogu.



wskazówka**: W przypadku wątpliwości co do posiadanego oprogramowania sprzętowego, przed kontynuowaniem należy powrócić do systemu stockowego!



#### Krok 2: Odblokowanie bootloadera



⚠️ **Ten krok usuwa wszystkie dane!





- Przetestuj połączenie ADB**: Podłącz urządzenie przez USB i przetestuj za pomocą polecenia `adb devices` z terminala komputera



![adb-devices](assets/fr/08.webp)



*Sprawdź połączenie ADB za pomocą polecenia `adb devices`*





- Autoryzuj połączenie** w telefonie



![usb-debugging-auth](assets/fr/09.webp)



*Debugowanie USB włączone z odciskiem palca RSA komputera*





- Uruchomienie w trybie bootloadera** :


```
adb -d reboot bootloader
```


Lub przytrzymaj **Volume Down + Power** urządzenie wyłączone





- Sprawdź połączenie fastboot**:


```
fastboot devices
```



![fastboot-mode](assets/fr/10.webp)



*Polecenia Fastboot w terminalu do sprawdzania połączenia*



![bootloader-screen](assets/fr/11.webp)



*Wyświetlacz szybkiego uruchamiania Pixela 4 z informacjami o systemie*





- Odblokowanie bootloadera** :


```
fastboot flashing unlock
```


Na urządzeniu użyj przycisków głośności do nawigacji i naciśnij przycisk **Zasilanie**, aby wybrać "Odblokuj bootloader" i potwierdź operację



![unlock-bootloader](assets/fr/12.webp)



*Potwierdzenie odblokowania bootloadera na urządzeniu*



⚠️ **Telefon uruchomi się ponownie automatycznie** po potwierdzeniu odblokowania





- Po automatycznym restarcie**, ponownie włącz debugowanie USB w opcjach deweloperskich




#### Krok 3: Flashowanie dodatkowych partycji



⚠️ **Wymagane, aby odzyskiwanie działało poprawnie**





- Uruchom ponownie program ładujący**: Ciszej + Zasilanie
- Flash** (zastąp `/path/to/` folderem, do którego pobrałeś plik) :


```
fastboot flash dtbo /chemin/vers/dtbo.img
```



![flash-partitions](assets/fr/13.webp)



*Flashowanie partycji dtbo i boot.img przez fastboot*



#### Krok 4: Instalacja systemu odzyskiwania LineageOS





- Flash recovery** (zastąp `/path/to/` folderem, do którego pobrałeś plik) :


```
fastboot flash boot /chemin/vers/boot.img
```




- Uruchom ponownie w trybie odzyskiwania**, aby sprawdzić



#### Krok 5: Instalacja LineageOS





- Ponowne uruchomienie w trybie odzyskiwania**: Ciszej + Zasilanie → Tryb odzyskiwania



![recovery-mode](assets/fr/14.webp)



*Interface z LineageOS recovery z menu głównym*





- Przywracanie ustawień fabrycznych** : Wpisz "Factory Reset" → "Formatuj dane / przywróć ustawienia fabryczne"



![factory-reset](assets/fr/15.webp)



*Proces przywracania ustawień fabrycznych w LineageOS* recovery





- Powrót do menu głównego**
- Sideload LineageOS** :
   - Na urządzeniu: "Apply Update" → "Apply from ADB"
   - Na PC: `adb -d sideload /path/to/lineageos.zip`



![apply-update](assets/fr/16.webp)



*Wybierz "Zastosuj aktualizację", a następnie "Zastosuj z ADB" w recovery*



![sideload-process](assets/fr/17.webp)



*Instalacja LineageOS w toku poprzez sideload*



![sideload-terminal](assets/fr/18.webp)



*Polecenie Sideload w terminalu z postępem instalacji*



**Normalne**: Proces może zatrzymać się na 47% lub wyświetlić błędy "Success" - jest to normalne!



#### Krok 6: Pierwsze uruchomienie





- Reboot**: "Uruchom ponownie system teraz"
- Pierwsze uruchomienie**: Może potrwać do 15 minut



**Instalacja zakończona!



### Punkty uwagi



⚠️ **Ostrzeżenie**: LineageOS jest dostarczany "tak jak jest" bez gwarancji. Chociaż dokładamy wszelkich starań, aby wszystko działało, instalujesz to na własne ryzyko!



**Krytyczne kontrole:**




- Zgodność z oprogramowaniem sprzętowym**: Należy sprawdzić wymaganą wersję oprogramowania sprzętowego na stronie pobierania danego modelu
- Nigdy nie odblokowuj** bootloadera po zainstalowaniu LineageOS
- Postępuj zgodnie z instrukcjami** dla swojego urządzenia



## Konfiguracja i aplikacje



### Pierwsze uruchomienie


Usprawniony Interface, zbliżony do standardowego Androida, bez Google. Prosta konfiguracja: język, Wi-Fi, nie wymaga konta.



### Alternatywne zastosowania



**Bezpieczne źródła aplikacji:**



**F-Droid** : Sklep z aplikacjami open source, preinstalowany z LineageOS dla microG lub do pobrania bezpośrednio. F-Droid oferuje wyłącznie oprogramowanie open source, które zostało zweryfikowane i skompilowane w przejrzysty sposób, gwarantując brak trackerów lub złośliwych komponentów.



**Aurora Store**: Anonimowy klient umożliwiający dostęp do Sklepu Google Play bez konta Google. Aurora pożycza współdzielone anonimowe konta, umożliwiając pobieranie popularnych aplikacji przy jednoczesnym zachowaniu prywatności.



**Niezbędne aplikacje alternatywne:**





- Nawigacja**: Organic Maps (mapy offline oparte na OpenStreetMap)
- Komunikacja**: Signal (szyfrowane wiadomości end-to-end), K-9 Mail (darmowy klient poczty e-mail)
- Media**: NewPipe (YouTube bez reklam i śledzenia), VLC (uniwersalny odtwarzacz multimedialny)
- Produktywność**: Nextcloud (własna chmura), Simple Calendar (synchronizacja CalDAV)
- Bezpieczeństwo**: Bitwarden (menedżer haseł), Aegis Authenticator (kody 2FA)



Aplikacje te, z których większość jest dostępna za pośrednictwem F-Droid, tworzą spójny ekosystem, który może w pełni zastąpić usługi Google, oferując jednocześnie nowoczesne, funkcjonalne wrażenia użytkownika.



## Użytkowanie i konserwacja



### Codzienne doświadczenie



LineageOS przekształca doświadczenie Androida, nadając priorytet płynności i responsywności. Usprawniony Interface jest szczególnie skuteczny na starszych urządzeniach, które otrzymują nowe życie, z wydajnością ogólnie lepszą od ROM-ów producenta dzięki brakowi ciężkich nakładek i zbędnych procesów.



Podstawowe funkcje (połączenia, SMS-y, zdjęcia, przeglądanie) działają płynnie, a narzędzia do dostosowywania umożliwiają precyzyjne dostosowanie systemu do indywidualnych preferencji bez uszczerbku dla stabilności.



### System aktualizacji OTA



LineageOS oferuje wyjątkowo łatwy w użyciu system aktualizacji Over-The-Air. Nowe wersje są proponowane automatycznie za pośrednictwem powiadomień, a ich instalacja zajmuje zaledwie kilka kliknięć, bez potrzeby skomplikowanej interwencji technicznej. Proces ten w pełni zachowuje zainstalowane dane i aplikacje.



Te regularne aktualizacje są dużym atutem, zwłaszcza w przypadku urządzeń, które zostały wycofane przez ich producentów, którzy mogą nadal korzystać z najnowszych poprawek zabezpieczeń Androida.



### Zalecane najlepsze praktyki



**Bezpieczeństwo po instalacji:**




- Ustaw silny kod PIN lub hasło do odblokowania
- Sprawdź, czy szyfrowanie pamięci masowej jest włączone (zazwyczaj domyślnie)
- Zainstaluj menedżera haseł, takiego jak Bitwarden przez F-Droid



**Konserwacja zapobiegawcza:**




- Regularne aktualizacje OTA dla bezpieczeństwa
- Ograniczenie instalacji aplikacji do zaufanych źródeł (F-Droid, Aurora Store)
- Okresowy przegląd uprawnień przyznanych aplikacjom
- Sporadyczne restarty optymalizują wydajność i zwalniają pamięć



## Zalety i ograniczenia



**Korzyści:**




- Domyślna prywatność (brak śledzenia przez Google)
- Szeroka kompatybilność (ponad 300 modeli)
- Najwyższa wydajność (bez zbędnego oprogramowania)
- Rozszerzone aktualizacje na starszych urządzeniach



ograniczenia:**




- Instalacja techniczna
- Brak Android Auto/Google Pay
- Aplikacje bankowe mogą być problematyczne



## GrapheneOS vs LineageOS: Jaka jest różnica?



### Różne podejścia



**GrapheneOS** koncentruje się wyłącznie na maksymalnym bezpieczeństwie i działa tylko na Google Pixels, aby wykorzystać ich dedykowane chipy bezpieczeństwa. System zawiera liczne zaawansowane zabezpieczenia przed exploitami i znacznie wzmacnia sandboxing aplikacji.



**LineageOS** równoważy bezpieczeństwo, prywatność i wygodę na jak największej liczbie urządzeń. Podejście jest bardziej pragmatyczne, mające na celu rozszerzoną kompatybilność, a nie absolutne bezpieczeństwo.



### Zarządzanie usługami Google



**GrapheneOS**: Oferuje opcjonalny system Google Play w piaskownicy. Google Play może być zainstalowany, ale działa w ścisłej piaskownicy, bez specjalnych uprawnień systemowych. To unikalne podejście umożliwia korzystanie z ekosystemu Google przy zachowaniu ścisłej kontroli bezpieczeństwa.



**LineageOS**: Pozwala użytkownikowi wybrać instalację usług Google (GApps), microG (darmowa alternatywa) lub pozostać całkowicie wolnym od Google. Maksymalna elastyczność dostosowana do potrzeb użytkownika.



### Porównanie techniczne



| **Aspect** | **GrapheneOS** | **LineageOS** |
|------------|----------------|---------------|
| **Compatibilité** | Pixels uniquement | Centaines d'appareils |
| **Sécurité** | Mitigations avancées | Sécurité AOSP standard |
| **Google Play** | Sandboxé optionnel | Installation classique possible |
| **Installation** | Interface web + USB | Procédure manuelle technique |
| **Philosophie** | Sécurité avant tout | Équilibre et liberté de choix |

### Zalecenia dotyczące użytkowania



**Wybierz GrapheneOS**, jeśli posiadasz Pixela, jeśli maksymalne bezpieczeństwo jest Twoim priorytetem i jeśli akceptujesz ograniczenia dla lepszej ochrony.



**Wybierz LineageOS**, jeśli masz urządzenie inne niż Pixel, szukasz dobrej równowagi między prywatnością a praktycznością lub chcesz swobodnie wybrać poziom kompromisu z ekosystemem Google.



## Wnioski



LineageOS oferuje dojrzałą alternatywę dla odzyskania kontroli nad smartfonem z Androidem. Nieskrępowane doświadczenie, optymalna wydajność, szeroka kompatybilność: idealny wybór łączący prywatność i codzienną praktyczność.



## Zasoby



### Oficjalna dokumentacja




- [Oficjalna strona LineageOS](https://lineageos.org)
- [LineageOS Wiki](https://wiki.lineageos.org) - Przewodniki instalacji według modelu
- [LineageOS dla microG](https://lineage.microg.org) - Wersja ze zintegrowanym microG



### Wspólnota




- [Subreddit r/LineageOS](https://reddit.com/r/LineageOS)
- [Konto Mastodon @LineageOS](https://fosstodon.org/@LineageOS)



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1