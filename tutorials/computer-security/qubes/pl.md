---
name: Qubes
description: W miarę bezpieczny system operacyjny.
---

![cover](assets/cover.webp)



Qubes OS to darmowy system operacyjny o otwartym kodzie źródłowym, przeznaczony dla użytkowników, którzy stawiają bezpieczeństwo na pierwszym miejscu wśród swoich priorytetów. Jego specyfika opiera się na prostym, ale radykalnym pomyśle: zamiast traktować komputer jako całość, dzieli jego użycie na niezależne przedziały zwane **_qubes_**.



Każdy qube działa jako **izolowane środowisko wirtualne**, z określonym poziomem zaufania i funkcją. Więc nawet jeśli aplikacja zostanie naruszona, atak pozostanie ograniczony do jej qube bez wpływu na resztę systemu.



> Jeśli poważnie myślisz o bezpieczeństwie, Qubes OS jest najlepszym dostępnym obecnie systemem operacyjnym. - **Edward Snowden**.

Instalacja Qubes OS wymaga jednak więcej przygotowań niż instalacja konwencjonalnego systemu operacyjnego. Obejmuje ona sprawdzenie pewnych wymagań sprzętowych, zrozumienie podstaw wirtualizacji i zaakceptowanie innego doświadczenia, w którym każde codzienne zadanie jest rozpatrywane w kategoriach separacji. Jednak po zainstalowaniu, Qubes OS oferuje solidną strukturę, która na nowo definiuje sposób codziennej interakcji z komputerem. W tym samouczku wyjaśnimy, jak działa Qubes OS i jak łatwo zainstalować go w systemie.



## Jak działa system operacyjny Qubes?



Qubes OS opiera się na zasadzie kompartmentalizacji. Zamiast korzystać z pojedynczego systemu, opiera się na hiperwizorze **Xen** w celu tworzenia odizolowanych maszyn wirtualnych, zwanych qubes. Każdy qube jest dedykowany określonemu zadaniu lub poziomowi zaufania (praca, osobiste przeglądanie, bankowość itp.). Ta separacja zapewnia, że jakikolwiek kompromis w jednym qube nie może rozprzestrzenić się na inne, działając jak kilka niezależnych komputerów w ramach jednej maszyny.



Użytkownik Interface jest zarządzany przez centralną, bezpieczną domenę o nazwie **dom0**. Domena ta jest całkowicie odizolowana od Internetu, co czyni ją sercem systemu. Chociaż okna i menu są wyświetlane przez dom0, rzeczywiste wykonywanie aplikacji odbywa się w ich odpowiednich qubach.



## Różne rodzaje qubów



Wokół dom0 obracają się różne rodzaje qubów, z których każdy ma do odegrania bardzo specyficzną rolę.





- Maszyny **AppVM** są używane do uruchamiania codziennych aplikacji: użytkownik może w ten sposób oddzielić swoje profesjonalne e-maile od przeglądania stron internetowych lub czynności bankowych, przy czym każde środowisko pozostaje całkowicie niezależne od innych.





- Te AppVM są oparte na **TemplateVM**, które służą jako scentralizowane szablony do instalowania i aktualizowania oprogramowania, eliminując potrzebę zarządzania każdą kostką osobno.



Qubes OS integruje również maszyny wirtualne specjalizujące się w **usługach systemowych**.





- **NetVM** bezpośrednio zarządza **urządzeniami sieciowymi** i zapewnia połączenie z Internetem. Są one często powiązane z **FirewallVM**, które interweniują w celu **filtrowania ruchu** i ograniczenia ekspozycji innych qubów.





- Maszyny ServiceVM odgrywają podobną rolę, na przykład w zarządzaniu urządzeniami USB, zawsze z tą samą logiką: izoluj najbardziej ryzykowne komponenty, aby zmniejszyć powierzchnię ataku.



Wreszcie, dla sporadycznych lub ryzykownych zadań, Qubes OS oferuje **DisposableVM**. Te efemeryczne quby są tworzone w locie, aby **otworzyć podejrzany dokument** lub **odwiedzić podejrzaną witrynę**, a następnie całkowicie znikają po zamknięciu, usuwając wszystkie ślady i zapobiegając wszelkim trwałym atakom.



### Mechanizm bezpiecznego kopiowania (qrexec)



Wymiana między qubami opiera się na **qrexec**, systemie komunikacji między maszynami wirtualnymi zaprojektowanym z myślą o bezpieczeństwie. Zamiast pozwalać qubom na swobodną komunikację, qrexec narzuca **specyficzne zasady**: plik kopiowany z jednej AppVM do drugiej lub tekst przesyłany przez schowek zawsze przechodzi przez kanał monitorowany i weryfikowany przez system. W ten sposób nawet prosta czynność kopiowania i wklejania jest kontrolowana, aby zapobiec rozprzestrzenianiu się złośliwego oprogramowania.



### Zarządzanie dyskami



Qubes OS wykorzystuje pomysłowy system zarządzania pamięcią masową. TemplateVM zawierają wspólną bazę oprogramowania, podczas gdy AppVM dodają tylko swoje osobiste dane i określone pliki. Zmniejsza to wykorzystanie przestrzeni dyskowej i ułatwia globalne aktualizacje. Z kolei maszyny DisposableVM wykorzystują tymczasowe woluminy, które całkowicie znikają po zamknięciu. Model ten gwarantuje nie tylko większe bezpieczeństwo, ale także efektywne zarządzanie zasobami.



## Dlaczego warto wybrać Qubes OS?



Zaletą Qubes OS jest przede wszystkim unikalny model bezpieczeństwa. Sercem tego podejścia jest kompartmentalizacja, która chroni użytkownika poprzez izolowanie każdego zadania w oddzielnych maszynach wirtualnych. W praktyce, zainfekowana wiadomość e-mail lub złośliwa strona internetowa może zagrozić tylko jednemu qubesowi, pozostawiając resztę systemu i dane osobowe w pełni chronione. Taka architektura znacznie ogranicza złożone ataki, które w konwencjonalnym systemie mogłyby się swobodnie rozprzestrzeniać.



Qubes OS oferuje również całkowitą przejrzystość i kontrolę nad środowiskiem cyfrowym. Wiesz dokładnie, które oprogramowanie ma dostęp do którego zasobu, niezależnie od tego, czy jest to sieć, urządzenie USB czy inne wrażliwe komponenty. System domyślnie integruje zaawansowane funkcje bezpieczeństwa, takie jak pełne szyfrowanie dysku, i ułatwia korzystanie z usług anonimizujących, takich jak system operacyjny Whonix.



https://planb.academy/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

Zamiast dążyć do stworzenia nieprzeniknionego systemu, Qubes OS koncentruje się na odporności: hermetyzuje uszkodzenia w przypadku kompromisu, zmniejszając ryzyko dla reszty systemu. To pragmatyczne podejście sprawia, że Qubes OS jest preferowanym wyborem dla użytkowników o wysokich wymaganiach w zakresie bezpieczeństwa lub chcących zachować maksymalną kontrolę nad swoim cyfrowym życiem.



## Instalacja Qubes OS



Przed instalacją Qubes OS należy upewnić się, że sprzęt spełnia minimalne wymagania, ponieważ system opiera się na wirtualizacji w celu odizolowania qubes. Głównymi komponentami do sprawdzenia są :




- **Procesor**: 64-bitowy procesor kompatybilny z wirtualizacją sprzętową (Intel VT-x lub AMD-V).
- Pamięć RAM: wymagane jest co najmniej 8 GB, ale zalecamy 16 GB lub więcej pamięci RAM, aby uruchomić kilka qubów jednocześnie.
- **Przestrzeń dyskowa**: minimum 36 GB, a najlepiej 128 GB na dysku SSD dla optymalnej wydajności.



Aby zainstalować Qubes OS, należy pobrać oficjalny obraz ISO z Qubes OS [oficjalna strona](https://www.qubes-os.org/downloads/). Konieczne jest sprawdzenie integralności ISO za pomocą dostarczonych podpisów GPG, aby upewnić się, że plik nie został zmodyfikowany i że pobieranie jest bezpieczne.



https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



Po zweryfikowaniu ISO należy utworzyć bootowalny nośnik instalacyjny, zwykle pamięć USB. W tym celu należy pobrać i zainstalować oprogramowanie takie jak **Rufus** w systemie Windows lub **Etcher** w systemach Windows, Linux lub macOS. Narzędzia te umożliwiają skopiowanie ISO na pamięć USB, tak aby była ona bootowalna.



Przed rozpoczęciem instalacji konieczne jest skonfigurowanie **BIOS lub UEFI** komputera, aby **włączyć wirtualizację** i umożliwić rozruch z USB. W zależności od modelu komputera może być konieczne **wyłączenie Secure Boot**, ponieważ Qubes OS może nie uruchomić się z włączoną tą opcją.



![0_02](assets/fr/02.webp)



Po spełnieniu tych warunków należy ponownie uruchomić komputer i uzyskać dostęp do BIOS/UEFI, natychmiast naciskając **Esc**, **Del**, **F9**, **F10**, **F11** lub **F12** (w zależności od producenta). W menu rozruchowym wybierz klucz USB jako urządzenie rozruchowe, aby uruchomić instalację Qubes OS.



**Ekran startowy**


Podczas uruchamiania z pamięci USB zostaniesz przeniesiony bezpośrednio do menu **GRUB**, gdzie możesz wybrać akcję do wykonania. Używając klawiszy strzałek na klawiaturze, wybierz "Zainstaluj Qubes OS" i naciśnij "Enter".



![0_03](assets/fr/03.webp)



**Wybór języka** :



Po rozpoczęciu instalacji pierwszym krokiem jest **wybranie języka** i **wariantu regionalnego** odpowiedniego dla danej konfiguracji. Zapewni to prawidłowe wyświetlanie systemu i opcji instalacji w preferowanym języku.



![0_04](assets/fr/04.webp)



**Konfiguracja parametrów** :



Na tym etapie należy skonfigurować kilka Elements przed uruchomieniem instalacji na komputerze.



![0_05](assets/fr/05.webp)



**Układ klawiatury** :



Kliknij opcję **Keyboard**, a następnie wybierz **odpowiedni układ** dla swojego komputera. Po dokonaniu wyboru kliknij **Zakończono**, aby przejść do następnego kroku.



**Wybór miejsca docelowego** :



Wybierz opcję "Miejsce docelowe instalacji", aby wybrać dysk, na którym chcesz zainstalować Qubes OS. Domyślnie partycjonowanie odbywa się automatycznie, umożliwiając usunięcie wszystkich danych z dysku i zainstalowanie na nim systemu. Możesz jednak wybrać **Customized** lub **Advanced Customization**, aby wykonać partycjonowanie dostosowane do własnych potrzeb. Następnie kliknij "Gotowe". System poprosi o ustawienie **hasła**, które działa jako zabezpieczenie Layer do szyfrowania danych. Pamiętaj, aby wybrać złożone i unikalne hasło.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Wybierz format daty i godziny** :


Kliknij opcję Godzina i data, a następnie wybierz strefę geograficzną. Możesz także wybrać preferowany format czasu: 24h lub 12h.



![0_08](assets/fr/08.webp)



**Tworzenie konta użytkownika** :


Kliknij **Utwórz użytkownika**, aby utworzyć **pierwsze konto**, które umożliwi zalogowanie się do Qubes OS.



![0_09](assets/fr/09.webp)



**Aktywuj konto root** :


Można również **włączyć konto root**, ustawiając osobne hasło dla administracji.



![0_10](assets/fr/10.webp)



Po dokonaniu tych ustawień, kliknij na **Start installation**, aby rozpocząć proces.



![0_11](assets/fr/11.webp)



Poczekaj na **zakończenie instalacji**, a następnie kliknij **restart system**, aby sfinalizować instalację i uruchomić Qubes OS.



![0_12](assets/fr/12.webp)



**Dodatkowa konfiguracja** :


Po ponownym uruchomieniu Qubes OS wyświetli monit o sfinalizowanie **domyślnych szablonów i konfiguracji qubes**. Wprowadź hasło zdefiniowane w celu zaszyfrowania dysku.



![0_13](assets/fr/13.webp)



Następnie zacznij od wybrania **TemplateVM**, którą chcesz zainstalować. Typowe opcje obejmują **Debian 12 Xfce**, **Fedora 41 Xfce** i **Whonix 17**, przy czym ten ostatni jest zalecany do zastosowań wymagających **anonimowości i bezpieczeństwa sieci**. Można również zdefiniować **domyślny szablon**, który posłuży jako podstawa do tworzenia nowych **AppVM**.



![0_14](assets/fr/14.webp)



W sekcji **Główna konfiguracja** można wybrać automatyczne tworzenie niezbędnych qubów systemowych, takich jak **sys-net**, **sys-firewall** i **default DisposableVM**. Zaleca się włączenie opcji, aby **sys-firewall i sys-usb były jednorazowe**, aby ograniczyć narażenie urządzenia i sieci w przypadku naruszenia bezpieczeństwa. Można również utworzyć domyślne **AppVMs**, takie jak **personal**, **work**, **untrusted** i **vault**, aby zorganizować swoje działania zgodnie z ich poziomem zaufania.



![0_15](assets/fr/15.webp)



Qubes OS pozwala również utworzyć **qube dedykowany urządzeniom USB** (sys-usb) i skonfigurować **Whonix Gateway i Workstation qubes**, aby zabezpieczyć komunikację za pośrednictwem sieci Tor. Dla zaawansowanych użytkowników, sekcja **Zaawansowana konfiguracja** umożliwia utworzenie **LVM thin pool** w celu efektywnego zarządzania przestrzenią dyskową pomiędzy qubami.



Po skonfigurowaniu wszystkich opcji, kliknij na **Complete**, a następnie na **Finish configuration**. Poczekaj, aż system zastosuje te ustawienia. Następnie zostaniesz poproszony o **zalogowanie się na swoje konto użytkownika**, a twoje środowisko Qubes OS będzie gotowe do użycia, bezpieczne i odpowiednio odizolowane dla różnych działań.



![0_17](assets/fr/17.webp)



System operacyjny jest teraz zainstalowany i gotowy do użycia.



![0_18](assets/fr/18.webp)



## Utwórz qube w swoim systemie



Aby utworzyć qube, proces jest zarządzany przez narzędzie **Qube Manager**, dostępne z menu Start. W oknie narzędzia wystarczy kliknąć ikonę **Create qube**, aby otworzyć nowe okno konfiguracji. Najpierw wprowadź nazwę qube, taką jak "perso-web" lub "work", aby zidentyfikować jego zastosowanie.



Następnie wybieramy jego **Typ**, zazwyczaj **AppVM** do rutynowych zadań lub **DisposableVM** do tymczasowego użytku. Ważne jest, aby wybrać **Template**, na którym będzie oparty qube, taki jak "fedora-39" lub "debian-12", ponieważ zapewni on system operacyjny i oprogramowanie. Wyznaczysz również **NetVM**, który jest qube odpowiedzialnym za dostęp do Internetu, domyślnie **sys-firewall**.



Wreszcie, po dostosowaniu rozmiaru pamięci i pamięci RAM, jeśli to konieczne, proste kliknięcie **OK** uruchomi proces tworzenia. Po zakończeniu procesu nowy qube będzie widoczny na liście i gotowy do użycia.



Podsumowując, Qubes OS nie jest zwykłym systemem operacyjnym, ale najnowocześniejszym rozwiązaniem bezpieczeństwa, które zmienia architekturę komputera osobistego. Jego podejście, oparte na separacji i izolacji poprzez wirtualizację, oferuje niezrównaną ochronę przed najbardziej wyrafinowanymi zagrożeniami. Segmentując środowisko pracy na wyspecjalizowane kuby dla każdego zadania, zapewnia, że złośliwe oprogramowanie nie może się rozprzestrzeniać i zagrażać całemu systemowi.



Niezależnie od tego, czy musisz bezpiecznie surfować po Internecie, chronić poufne informacje, czy pracować z różnymi poziomami zaufania, Qubes OS zapewnia odporną, przejrzystą strukturę. Przyjmując dobre praktyki i w pełni wykorzystując jego funkcje, będziesz mieć **cyfrową fortecę** dostosowaną do współczesnych zagrożeń. Dowiedz się więcej o ochronie danych i prywatności.



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1