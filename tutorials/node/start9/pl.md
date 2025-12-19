---
name: Start9

description: Samouczek dotyczący konfiguracji prywatnego serwera Start9

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Oto samouczek wideo od Southern Bitcoiner, przewodnik wideo, który pokazuje, jak skonfigurować i używać osobistego serwera Start9 / StartOS oraz jak uruchomić węzeł bitcoin *


## 1️⃣ Wprowadzenie


### Czym dokładnie jest Start9?


Start9 to firma założona w 2020 roku, najbardziej znana z opracowania [**StartOS**,](https://github.com/Start9Labs/start-os) systemu operacyjnego opartego na Linuksie, przeznaczonego dla serwerów osobistych. Umożliwia on użytkownikom łatwe samodzielne hostowanie szerokiej gamy usług oprogramowania - takich jak węzły Bitcoin i Lightning, aplikacje do przesyłania wiadomości lub menedżery haseł, przy jednoczesnym zachowaniu pełnej kontroli nad swoimi danymi i wyeliminowaniu zależności od scentralizowanych platform technologicznych. StartOS oferuje przyjazny dla użytkownika interfejs oparty na przeglądarce, wyselekcjonowany Marketplace do instalowania usług oraz wbudowane narzędzia do ochrony prywatności, takie jak integracja Tor i szyfrowanie HTTPS w całym systemie. Start9 zapewnia również urządzenia sprzętowe wstępnie załadowane systemem operacyjnym, chociaż oprogramowanie można zainstalować na kompatybilnym sprzęcie lub maszynach wirtualnych (VM).


### Jakie opcje są dostępne?


Start9 oferuje zarówno gotowe rozwiązania, jak i opcje wdrożenia DIY. [**Server One**](https://store.start9.com/collections/servers/products/server-one) i [**Server Pure** ](https://store.start9.com/collections/servers/products/server-pure) to oficjalne urządzenia sprzętowe wyposażone w wysokowydajne komponenty: Server One wykorzystuje procesor **AMD Ryzen 7 5825U** z konfigurowalną pamięcią RAM (16GB-64GB) i pamięcią masową (2TB-4TB NVMe SSD), podczas gdy Server Pure jest wyposażony w **Intel i7-10710U**, również oferujący konfigurowalną pamięć RAM i opcje pamięci masowej. Oba obejmują **dożywotnią pomoc techniczną** przy zakupie bezpośrednio od Start9. Dla użytkowników preferujących elastyczność, StartOS można zainstalować bezpłatnie na szerokiej gamie istniejącego sprzętu, w tym laptopach, komputerach stacjonarnych, mini PC i komputerach jednopłytkowych lub w maszynach wirtualnych.


![image](assets/en/01.webp)


### Jakie są różnice w stosunku do Umbrel?


StartOS i Umbrel upraszczają samodzielną instalację usług, ale różnią się architekturą i funkcjami. Umbrel działa jako warstwa aplikacji na systemach Debian/Ubuntu lub maszynach wirtualnych, podczas gdy Start9 jest dedykowanym systemem operacyjnym wymagającym bezpośredniej instalacji na sprzęcie lub maszynie wirtualnej. Umbrel posiada dopracowany, inspirowany macOS interfejs, podczas gdy Start9 stawia na funkcjonalny, minimalistyczny design. Umbrel oferuje większy [wybór aplikacji](https://apps.umbrel.com/), podczas gdy [Start9 Marketplace](https://marketplace.start9.com/) rekompensuje to zaawansowanymi możliwościami technicznymi. Start9 upraszcza dostęp do zaawansowanych ustawień poprzez zweryfikowane formularze interfejsu użytkownika, zmniejszając potrzebę interakcji z wierszem poleceń. Wyróżnia się również w zarządzaniu kopiami zapasowymi dzięki szyfrowanym kopiom zapasowym systemu jednym kliknięciem, funkcji, której Umbrel nie ma natywnie. StartOS zapewnia wbudowane narzędzia do monitorowania i wymusza szyfrowanie HTTPS dla dostępu do sieci lokalnej, zwiększając bezpieczeństwo. Umbrel używa lokalnie nieszyfrowanego protokołu HTTP, choć obie platformy obsługują bezpieczny zdalny dostęp przez Tor. Umbrel jest odpowiedni dla użytkowników, dla których priorytetem jest bogaty ekosystem aplikacji i dopracowany interfejs użytkownika. Start9 to dobry wybór dla tych, którzy cenią sobie bezpieczeństwo, konfigurowalność, niezawodność tworzenia kopii zapasowych i zaawansowane zarządzanie usługami bez konieczności znajomości wiersza poleceń. Aby dowiedzieć się więcej o Umbrel i różnicach w stosunku do Start9, odwiedź ten kurs:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ Wymagania wstępne DIY: Minimalne i zalecane specyfikacje


Do podstawowego użytku z minimalnymi usługami, **minimalne specyfikacje** to: **1 rdzeń vCPU (2,0 GHz + boost), 4 GB pamięci RAM, 64 GB pamięci masowej** i port Ethernet. To powiedziawszy, zalecałbym pójście znacznie dalej, zwłaszcza jeśli używasz węzła Bitcoin. Osobiście zacząłem od 1 TB i szybko zabrakło mi miejsca. Lepiej celować w **co najmniej 2 TB pamięci masowej**, wraz z **czterordzeniowym procesorem (2,5 GHz+)** i **8 GB+ pamięci RAM**. To ogromna różnica w wydajności i żywotności. Jeśli chcesz zagłębić się w temat, tutaj znajdziesz aktualny wątek społeczności dotyczący [sprzętu zdolnego do uruchomienia StartOS](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ Pobieranie i flashowanie oprogramowania sprzętowego


Aby rozpocząć konfigurację, użyj oddzielnego komputera, aby odwiedzić stronę [Start9 website](https://start9.com/) i przejdź do sekcji dokumentacji, klikając `DOCS`. Stamtąd przejdź do `Flashing Guides`, aby znaleźć odpowiednią wersję StartOS. Dostępne są dwie opcje:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Ten samouczek obejmuje opcję `x86/ARM`.


Najnowszą wersję systemu operacyjnego można pobrać ze strony [Github release page](https://github.com/Start9Labs/start-os/releases/latest). wersje [Pre-release](https://github.com/Start9Labs/start-os/releases) są również dostępne dla użytkowników, którzy chcą przetestować nowe funkcje. Na dole strony, w zakładce `Assets`, pobierz `x86_64` lub `x86_64-nonfree.iso`.  Obraz `x86_64-nonfree.iso` zawiera niewolne (zamknięte) oprogramowanie wymagane dla Server One i większości sprzętu DIY, w szczególności do obsługi grafiki i urządzeń sieciowych.


Zaleca się zweryfikowanie integralności pliku poprzez sprawdzenie jego skrótu SHA256 z tym wymienionym na GitHub. W przypadku systemu Linux można użyć polecenia `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso`, a inne systemy operacyjne są opisane w dokumentacji.


Po pobraniu i zweryfikowaniu obrazu StartOS, musi on zostać sflashowany na dysk USB. zalecanym oprogramowaniem do tego zadania jest `BalenaEtcher`. Jest to darmowe narzędzie o otwartym kodzie źródłowym do zapisywania plików obrazów systemu operacyjnego na dyskach USB i kartach SD, dostępne dla systemów Windows, macOS i Linux. Pobierz odpowiednią wersję z oficjalnej strony [Balena Etcher](https://www.balena.io/etcher/) i uruchom instalator. Podłącz docelowy dysk USB lub kartę SD, otwórz Balena Etcher i kliknij `Flash from file`, aby wybrać pobrany obraz systemu operacyjnego. Etcher automatycznie wykryje podłączone dyski; wybierz właściwy cel, jeśli jest ich kilka. Kliknij `Flash!`, aby rozpocząć zapisywanie obrazu. Etcher automatycznie zweryfikuje proces zapisu po jego zakończeniu. Po zakończeniu bezpiecznie wyjmij dysk i użyj go do uruchomienia urządzenia.


![image](assets/en/19.webp)


## 4️⃣ Konfiguracja początkowa


Informacje na temat początkowej konfiguracji można znaleźć na stronie Start9 [dokumentacja](https://docs.start9.com/0.3.5.x/) w sekcji `USER MANUAL`, a następnie `Getting Started - Initial Setup`.  Ten oficjalny przewodnik powinien być konsultowany w celu uzyskania najbardziej aktualnych informacji.


Przedstawiono dwie opcje:



- Zacznij od nowa
- Opcje odzyskiwania


W przypadku instalacji nowego serwera wybierz `Start Fresh`. Najpierw podłącz serwer do zasilania i kabla Ethernet. Upewnij się, że komputer używany do konfiguracji znajduje się w tej samej sieci lokalnej. Wyjmij nowo sflashowany dysk USB z komputera i włóż go do serwera.


Serwerem można sterować zdalnie z dowolnego komputera w tej samej sieci. Otwórz przeglądarkę internetową i przejdź do strony `http://start.local`.


**Uwaga**: Jeśli występują problemy z połączeniem z tym adresem, często jest to spowodowane tym, że sieci domowe nie rozpoznają nazw domen `.local`. Problem można rozwiązać, uzyskując bezpośredni dostęp do serwera za pośrednictwem jego adresu IP. Adres IP można znaleźć, logując się do interfejsu administratora routera (zwykle pod adresem `192.168.1.1` lub podobnym) i lokalizując urządzenie na liście klientów DHCP lub mapie sieci. Następnie należy wpisać pełny adres IP (np. `http://192.168.1.105`) w przeglądarce. Pozwala to ominąć rozpoznawanie DNS. Jeśli problemy nie ustąpią, zapoznaj się ze stroną [Typowe problemy](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) lub [skontaktuj się z pomocą techniczną](https://start9.com/contact/)


Powinien pojawić się ekran konfiguracji StartOS. Kliknij `Start Fresh`, aby rozpocząć konfigurację nowego serwera.


![image](assets/en/03.webp)


Następnym krokiem jest wybranie dysku, na którym będą przechowywane dane StartOS.


![image](assets/en/04.webp)


Ustaw silne `Hasło` dla serwera. Zapisz je zgodnie z zaleceniami Start9, a następnie kliknij `FINISH`.


![image](assets/en/05.webp)


Ekran pokaże, że StartOS inicjalizuje i konfiguruje serwer. Następnym krokiem jest "Pobranie informacji o adresie", ponieważ adres "start.local" służy wyłącznie do celów konfiguracji i nie będzie działać później.


![image](assets/en/06.webp)


Plik konfiguracyjny zawiera dwa krytyczne adresy dostępu: jeden dla `sieci lokalnej (LAN)` i drugi dla bezpiecznego dostępu przez `Tor`. Oba adresy powinny być zapisane w bezpiecznym menedżerze haseł. Następnym krokiem jest `Trust your Root CA`. Otwórz nową kartę przeglądarki i postępuj zgodnie z instrukcjami, aby zaufać głównemu urzędowi certyfikacji i zalogować się. Certyfikat Root CA można również pobrać, klikając `Pobierz certyfikat` w pobranym pliku.


## 5️⃣ Zaufaj głównemu urzędowi certyfikacji


Po pobraniu certyfikatu, `Root CA` serwera musi być zaufany przez system operacyjny. Kliknij `View Instructions` i znajdź wytyczne dla konkretnego systemu operacyjnego.


![image](assets/en/07.webp)


W przypadku systemu Linux używane są następujące polecenia. Najpierw otwórz Terminal i zainstaluj niezbędne pakiety:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Przejdź do katalogu, w którym został pobrany certyfikat, zazwyczaj `~/Downloads` . Wykonaj te polecenia, aby dodać certyfikat do magazynu zaufania systemu operacyjnego. Przejdź do folderu pobierania za pomocą `cd ~/Downloads`. Utwórz wymagany katalog za pomocą `sudo mkdir -p /usr/share/ca-certificates/start9`. Skopiuj plik certyfikatu, zastępując `your-filename.crt` rzeczywistą nazwą pliku, używając `sudo cp "your-filename.crt" /usr/share/ca-certificates/start9/`. Zarejestruj certyfikat na stałe, dołączając jego ścieżkę do konfiguracji systemu za pomocą `sudo bash -c "echo 'start9/your-filename.crt' >> /etc/ca-certificates.conf"`. Na koniec odbuduj magazyn zaufania za pomocą `sudo update-ca-certificates`. Ważne jest, aby użyć rzeczywistej nazwy pliku certyfikatu i zweryfikować wszystkie ścieżki przed wykonaniem tych poleceń. Proces ten ustanawia stałe zaufanie dla połączeń HTTPS serwera Start9.


Pomyślna instalacja zostanie zasygnalizowana komunikatem `1 added`. Większość aplikacji będzie mogła bezpiecznie łączyć się przez `https`. W przypadku korzystania z przeglądarki Firefox wymagany jest dodatkowy [ostatni krok](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff). W przypadku Chrome lub Brave wymagany jest inny [ostatni krok](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome), aby skonfigurować przeglądarkę do respektowania głównego urzędu certyfikacji. Przetestuj połączenie, odświeżając stronę. Jeśli problem nadal występuje, zamknij i ponownie otwórz przeglądarkę przed ponownym odwiedzeniem strony.


![image](assets/en/08.webp)


## 6️⃣ Rozpoczęcie pracy z systemem StartOS


Teraz powinno być możliwe zalogowanie się przy użyciu bezpiecznego połączenia HTTPS. Wprowadź `Hasło`, aby uzyskać dostęp do `Ekranu powitalnego`.


![image](assets/en/09.webp)


Ten ekran zawiera przydatne skróty ułatwiające rozpoczęcie pracy. Lewy pasek boczny zawiera główne elementy menu służące do nawigacji.


## 7️⃣ System


Karta Systemy w systemie StartOS zapewnia dostęp do podstawowych funkcji systemowych do zarządzania serwerem osobistym. Oferuje narzędzia do konserwacji systemu, bezpieczeństwa, diagnostyki i konfiguracji bez konieczności znajomości wiersza poleceń.


Sekcja `Backups` umożliwia tworzenie pełnych kopii zapasowych systemu, w tym usług, konfiguracji i danych, które można później przywrócić. Jest to niezbędne do odzyskiwania danych po awarii lub migracji na nowy sprzęt. Kopie zapasowe mogą być przechowywane na dyskach zewnętrznych i są szyfrowane przy użyciu hasła głównego.


Sekcja `Manage` w zakładce Systems pozwala na kontrolę nad kluczowymi funkcjami systemu. Użytkownicy mogą ręcznie sprawdzać dostępność i stosować aktualizacje StartOS, zachowując kontrolę nad procesem aktualizacji systemu. Możliwe jest sideloadowanie niestandardowych lub zewnętrznych usług niedostępnych na oficjalnym rynku. Jeśli serwer nie jest podłączony przez Ethernet, ustawienia Wi-Fi można skonfigurować w tej sekcji. Zaawansowani użytkownicy mogą włączyć dostęp SSH do zarządzania systemem z poziomu terminala.


![image](assets/en/10.webp)


Sekcja `Insights` zapewnia monitorowanie wydajności i stanu serwera w czasie rzeczywistym, wyświetlając użycie procesora, pamięci RAM i dysku za pomocą wykresów. Pokazuje również temperaturę systemu, co jest przydatne w przypadku urządzeń takich jak Raspberry Pi, które nie mają aktywnego chłodzenia. Wskaźniki dostępności i średniego obciążenia pomagają ocenić stabilność systemu, a dzienniki na żywo są dostępne do rozwiązywania problemów z usługami lub systemem.


Sekcja `Support` oferuje dostęp do wbudowanych FAQ, oficjalnej dokumentacji i kanałów wsparcia społeczności. Dzienniki debugowania można pobrać z tej sekcji, aby udostępnić je pomocy technicznej Start9 w celu szybszego rozwiązywania problemów.


![image](assets/en/11.webp)


## 8️⃣ Marketplace


`Marketplace` służy do wykrywania, instalowania i zarządzania usługami na serwerze osobistym. Zapewnia dostęp do oprogramowania takiego jak Bitcoin Core, BTCPay Server i electrs. StartOS obsługuje wiele rynków, w tym oficjalny rejestr Start9 i rejestry prowadzone przez społeczność. Można je dodać, klikając `CHANGE` i przełączając się na `Community Registry`, który zapewnia dostęp do szerszego zakresu usług.


![image](assets/en/12.webp)


## 9️⃣ Instalacja pełnego węzła Bitcoin


Instalacja Bitcoin full node na StartOS zapewnia pełną suwerenność nad doświadczeniem Bitcoin. Umożliwia walidację transakcji oraz zwiększa prywatność i bezpieczeństwo, eliminując zależność od zewnętrznych usług, które mogą rejestrować aktywność. Uzyskuje się pełną kontrolę nad transakcjami, umożliwiając ich transmisję bezpośrednio do sieci. Domyślną opcją jest `Bitcoin Core`, która integruje się natywnie ze StartOS i pozwala na połączenie z portfelami takimi jak Specter, Sparrow lub Electrum w celu samodzielnej konfiguracji. Alternatywa, `Bitcoin Knots`, jest również dostępna za pośrednictwem Rejestru Społeczności.


Aby zainstalować Bitcoin Core, przejdź do Marketplace. W domyślnym rejestrze znajdź i zainstaluj usługę Bitcoin Core. Po instalacji pojawi się monit `Needs Config`, wymagający uzupełnienia ustawień przed uruchomieniem usługi. Dzieje się tak zazwyczaj po aktualizacjach lub świeżych instalacjach i wymaga przejrzenia `Ustawień RPC`. Kontynuuj z domyślną konfiguracją i kliknij `Zapisz`.


![image](assets/en/13.webp)


Po pełnej synchronizacji węzeł może służyć jako prywatny backend dla portfeli takich jak Sparrow, zapewniając zwiększoną prywatność i walidację transakcji. Jednak w przypadku użytkowników przechowujących znaczne kwoty, kluczowe znaczenie ma zrozumienie kompromisów w zakresie bezpieczeństwa tego bezpośredniego połączenia. Gdy wallet łączy się bezpośrednio z Bitcoin Core, może ujawnić poufne dane, ponieważ Bitcoin Core przechowuje klucze publiczne (xpubs) i salda wallet w postaci niezaszyfrowanej na komputerze hosta. Naruszony system może pozwolić atakującemu na odkrycie twoich zasobów i zaatakowanie cię.


Aby ograniczyć to ryzyko i uzyskać solidniejszy model bezpieczeństwa, można skonfigurować prywatny Electrum Server. Serwer ten działa jako pośrednik, indeksując blockchain bez przechowywania jakichkolwiek informacji specyficznych dla wallet. Łącząc wallet z własnym serwerem Electrum zamiast bezpośrednio z Bitcoin Core, uniemożliwiasz wallet dostęp do wrażliwych danych węzła.


![image](assets/en/14.webp)


## konfiguracja elektryków


`electrs` (Electrum Rust Server) to szybki, wydajny indeksator, który łączy się z węzłem Bitcoin Core i umożliwia portfelom kompatybilnym z Electrum sprawdzanie historii transakcji i sald w czasie rzeczywistym. Uruchamiając electrs na StartOS, eliminujesz zależność od zewnętrznych serwerów Electrum, znacznie poprawiając prywatność i bezpieczeństwo - twoje zapytania wallet trafiają bezpośrednio do twojego węzła.


Aby go skonfigurować, najpierw zainstaluj usługę electrs z StartOS Marketplace. System będzie wymagał pełnej synchronizacji Bitcoin Core przed kontynuowaniem. Po instalacji potwierdź ustawienia `Needs Config` z zalecanymi wartościami domyślnymi, a electrs rozpocznie indeksowanie łańcucha bloków, co może potrwać do jednego dnia w zależności od posiadanego sprzętu.


![image](assets/en/15.webp)


Po zakończeniu można podłączyć portfele, takie jak Sparrow lub Specter. Udane połączenie umożliwia synchronizację wallet bezpośrednio z węzłem, zapewniając bezpieczne, prywatne i samodzielnie hostowane doświadczenie Bitcoin.


## 1️⃣1️⃣ Connect Sparrow Wallet


Aby połączyć `Sparrow Wallet` z węzłem StartOS za pomocą implementacji electrs, najpierw upewnij się, że Bitcoin Core jest w pełni zsynchronizowany, a electrs jest zainstalowany i uruchomiony. Otwórz Sparrow Wallet na swoim urządzeniu i przejdź do `File` -> `Settings` -> `Server`. Następnie wybierz `Private Electrum Server`. W polu URL wprowadź `Nazwa hosta tor` i `Port` dla electrs, które można znaleźć w StartOS w `Usługi` -> `electrs` -> `Właściwości` (zazwyczaj kończące się na `.onion:50001`).


![image](assets/en/16.webp)


Następnie włącz Tora, zaznaczając `Użyj proxy`, ustawiając adres proxy na `127.0.0.1` i port na `9050`. Kliknij `Test Connection` i poczekaj kilka chwil. Pomyślne połączenie spowoduje wyświetlenie komunikatu potwierdzającego, takiego jak `Connected to electrs`. Po weryfikacji zamknij ustawienia i przejdź do tworzenia lub przywracania wallet. Ta konfiguracja zapewnia, że wallet wysyła zapytania do własnego węzła za pośrednictwem electrs, zapewniając pełną prywatność i niezawodne działanie.


![image](assets/en/17.webp)


## wnioski


StartOS by Start9 to przyjazna dla użytkownika, skoncentrowana na prywatności platforma zaprojektowana do samodzielnego hostowania niezbędnych usług, takich jak węzły Bitcoin i Lightning, portfele i aplikacje osobiste. Eliminuje ona potrzebę znajomości wiersza poleceń, oferując przejrzysty interfejs graficzny, automatyczne tworzenie kopii zapasowych, monitorowanie kondycji i bezpieczny dostęp do Tora, dzięki czemu jest idealna dla użytkowników nietechnicznych. Jego modułowa architektura wspiera płynną integrację z narzędziami takimi jak electrs czy Sparrow, dając ci pełną kontrolę nad twoją finansową i cyfrową suwerennością. Dzięki silnemu naciskowi na przejrzystość, lokalną kontrolę i rozszerzalność, StartOS umożliwia użytkownikom odzyskanie własności od scentralizowanych platform i uruchomienie własnej prywatnej, odpornej infrastruktury.