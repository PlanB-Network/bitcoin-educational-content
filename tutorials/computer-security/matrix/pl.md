---
name: Matryca
description: Przewodnik po zrozumieniu, konfiguracji i korzystaniu z Matrix, bezpiecznej, otwartej i zdecentralizowanej platformy komunikacyjnej.
---

![cover](assets/cover.webp)



## Czym jest Matrix?



Matrix to **zdecentralizowany protokół komunikacyjny** zaprojektowany w celu umożliwienia wymiany wiadomości, plików i połączeń audio/wideo między użytkownikami i aplikacjami, bez zależności od centralnego przedsiębiorstwa. W przeciwieństwie do tradycyjnych platform komunikacyjnych, Matrix jest **otwartą infrastrukturą**, porównywalną do poczty elektronicznej: każdy może wybrać serwer lub samodzielnie go obsługiwać, zachowując jednocześnie możliwość wymiany z resztą sieci.



Matrix wyróżnia się trzema podstawowymi zasadami:



### Protokół, a nie aplikacja



Matrix nie jest aplikacją taką jak WhatsApp czy Telegram.


Jest to ustandaryzowany język, z którego może korzystać wiele aplikacji.


Innymi słowy, szeroka gama oprogramowania Element, FluffyChat, Cinny, Nheko i innych, zapewnia dostęp do tej samej sieci Matrix.



Gwarantuje to całkowitą swobodę: zmiana aplikacji bez utraty kontaktów, różnorodność interfejsów, niezależność od jednego dostawcy.



![capture](assets/fr/03.webp)



### Zdecentralizowana sieć federacyjna



Struktura Matrix opiera się na **federacji**, modelu, w którym kilka niezależnych serwerów współpracuje ze sobą.


Każdy serwer (zwany _homeserver_) może hostować użytkowników, czaty i synchronizować wiadomości z innymi serwerami w sieci.


Tak więc :





- żaden pojedynczy podmiot nie kontroluje całego systemu;
- serwer może zniknąć bez wpływu na resztę sieci;
- każda organizacja lub osoba może zarządzać własną przestrzenią.



Model ten zapewnia **wysoką odporność** i odzwierciedla wartości suwerenności technologicznej.



![capture](assets/fr/03.webp)



### Bezpieczny, szyfrowany system



Matrix obsługuje **szyfrowanie end-to-end (E2EE)** dla prywatnych wymian i zaszyfrowanych grup.


Wiadomości mogą być odczytywane tylko przez uczestników, a nie przez serwery pośredniczące.


Takie podejście umożliwia komunikację bez ujawniania treści wymiany stronom trzecim, przy jednoczesnym zachowaniu przejrzystości protokołu i możliwości hostowania własnego serwera.



![capture](assets/fr/05.webp)



### Wyjątkowa interoperacyjność



Jednym z głównych atutów Matrix jest jego zdolność do działania jako **most pomiędzy różnymi systemami komunikacji**. Dzięki _mostom_ możliwe jest połączenie :





- Telegram
- WhatsApp
- Signal
- Posłaniec
- Slack
- Discord
- IRC, XMPP itp.



Umożliwia to ujednolicenie społeczności rozproszonych na kilku platformach, przy jednoczesnym zachowaniu kontroli nad infrastrukturą.



![capture](assets/fr/06.webp)



## Jak działa Matrix?



Ta sekcja przedstawia wewnętrzną strukturę sieci Matrix, aby zrozumieć, w jaki sposób użytkownicy, serwery i aplikacje współdziałają w tym zdecentralizowanym ekosystemie. Matrix opiera się na trzech podstawowych elementach: _homeserwerach_, tożsamościach i _klientach_ wykorzystywanych do komunikacji.



### Serwery: serwery domowe



Matrix działa na niezależnych serwerach zwanych _homeserwerami_.


Każdy serwer domowy zarządza :





- kont użytkowników, które obsługuje,
- prywatne rozmowy i salony, w których uczestniczą ci użytkownicy,
- synchronizacja z innymi serwerami sieciowymi.



Wszystkie serwery domowe podłączone do sieci Matrix automatycznie wymieniają się wiadomościami i zdarzeniami ze współdzielonych salonów. Na przykład:





- użytkownik zarejestrowany na serwerze A może czatować z użytkownikiem na serwerze B,
- salon może być rozproszony na dziesiątki serwerów,
- nikt nie ma kontroli nad salonem lub całą społecznością.



Model ten jest wysoce odporny i pozwala każdej organizacji lub osobie zarządzać własną infrastrukturą.



### Identyfikatory matrycy



Każdy użytkownik ma unikalny identyfikator, zwany **MXID** (_Matrix ID_), który wygląda jak adres:



```bash
@nomdutilisateur:serveur.xyz
```



Składa się z :





- nazwa użytkownika poprzedzona **@**
- nazwa serwera, na którym konto zostało utworzone, poprzedzona **:**



Przykłady:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



Identyfikator ten umożliwia komunikację z każdym innym użytkownikiem Matrix, niezależnie od serwera źródłowego.



### Klienci macierzy (aplikacje)



Aby korzystać z Matrix, należy połączyć się z aplikacją o nazwie **klient Matrix**.



Najbardziej znane z nich to :





- Element (web, mobile, desktop)
- FluffyChat (mobilny)
- Cinny (minimalistyczny web/desktop)
- Nheko (komputer stacjonarny)



Aplikacje te są jedynie interfejsami dla :





- aby wyświetlić wiadomości,
- wysyłać tekst, obrazy lub pliki,
- dołączać do targów lub je tworzyć,
- wykonywanie połączeń audio/wideo.



Wszystkie aplikacje komunikują się z serwerami za pośrednictwem tego samego standardowego protokołu.



### Pokoje i prywatne wiadomości (DM)



W Matrix wymiana odbywa się w **pomieszczeniach**:





- pokój może być publiczny lub prywatny
- może pomieścić dwie osoby lub tysiące
- może być współdzielony między kilkoma serwerami
- ma unikalny identyfikator zaczynający się od **!**



Prywatne wiadomości to po prostu czaty z dwoma uczestnikami, często określane jako **DM (Direct Messages)**.



Synchronizacja salonów odbywa się w czasie rzeczywistym między uczestniczącymi serwerami, zapewniając płynne działanie przy jednoczesnym zachowaniu decentralizacji.



## Dlaczego warto korzystać z Matrix?



Matrix to nie tylko alternatywa dla scentralizowanych systemów przesyłania wiadomości: to technologia, która spełnia rzeczywiste potrzeby w zakresie suwerenności cyfrowej, bezpieczeństwa i interoperacyjności. Istnieje wiele powodów, dla których coraz więcej osób, firm i instytucji wybiera ten protokół do komunikacji.



### Odzyskaj kontrolę nad swoją komunikacją



Większość platform komunikacyjnych działa w modelu scentralizowanym: pojedynczy gracz kontroluje serwery, dostęp, dane i zasady użytkowania. Model ten oznacza całkowitą zależność od dostawcy.


Matrix przyjmuje inne podejście.


Każdy może wybrać miejsce hostowania swojego konta, a nawet wdrożyć własny serwer. Żaden podmiot nie jest w stanie zablokować użytkownika, zażądać inwazyjnej identyfikacji lub narzucić zmiany polityki.


Architektura ta daje autonomię zarówno jednostkom, jak i organizacjom. Komunikacja nie opiera się już na zaufaniu do firmy, ale na otwartym, udokumentowanym i weryfikowalnym protokole.



### Bezpieczna, szyfrowana komunikacja



Matrix obsługuje szyfrowanie end-to-end dla prywatnych konwersacji i grup. Mechanizm ten zapewnia, że tylko uczestnicy mogą czytać wiadomości, nawet jeśli przechodzą one przez serwery innych firm w federacji.



Protokół wykorzystuje algorytm Megolm/Olm, zaprojektowany specjalnie w celu zapewnienia silnego bezpieczeństwa w rozproszonych środowiskach z wieloma urządzeniami.



Umożliwia to :





- chronić wrażliwe rozmowy,
- zapobiec nieautoryzowanemu dostępowi (nawet z serwera hosta),
- zachować poufność w dłuższej perspektywie.



Szyfrowanie nie jest opcją: to podstawowy składnik protokołu.



### Brak zależności od pojedynczej aplikacji



Matrix nie jest aplikacją, ale protokołem.



Ta różnorodność klientów gwarantuje :





- wybór dostosowany do indywidualnych potrzeb,
- możliwość korzystania z Matrix na dowolnym typie urządzenia,
- brak zależności od jednego oprogramowania.



Jeśli klient jest nieodpowiedni lub przestaje być obsługiwany, wystarczy wybrać innego: konto nadal działa normalnie.



### Federacja i łączenie różnych społeczności



Federacja pozwala różnym serwerom współpracować ze sobą, będąc jednocześnie zarządzanymi niezależnie.


Tak więc :





- organizacja może zarządzać własnym serwerem domowym,
- osoby mogą dołączyć do serwerów publicznych,
- wszyscy mogą komunikować się ze sobą tak, jakby byli na tej samej platformie.



Ta elastyczność umożliwia tworzenie przestrzeni komunikacyjnych dostosowanych do wszelkich potrzeb: zespołów, stowarzyszeń, społeczności, instytucji czy projektów open source.



Matrix jest szczególnie popularny w kręgach technicznych, kolektywach aktywistów, naukowcach, rządach i coraz częściej w społecznościach Bitcoin.



### Unikalna interoperacyjność w środowisku przesyłania wiadomości



Jednym z głównych atutów Matrix jest jego zdolność do **rozszerzania** giełd dzięki mostom zdolnym do łączenia :





- WhatsApp
- Telegram
- Signal
- Slack
- Discord
- IRC
- XMPP
- i wiele innych platform



Matrix staje się w ten sposób warstwą ujednolicającą komunikację, łącząc kilka społeczności rozproszonych w różnych aplikacjach.



Ta interoperacyjność zmniejsza fragmentację i upraszcza współpracę.



### Darmowy, otwarty i zrównoważony protokół



Protokół Matrix jest całkowicie otwarty i przejrzyście opracowany.


Gwarantuje to kilka korzyści:





- ciągła ewolucja standardu,
- możliwość sprawdzenia kodu przez każdego,
- niezależność od zmian handlowych lub politycznych,
- długoterminowa odporność.



W przeciwieństwie do zastrzeżonych systemów przesyłania wiadomości, przyszłość Matrix nie zależy od jednej firmy, ale od globalnej społeczności i otwartego standardu.



## Jak utworzyć konto Matrix?



Utworzenie konta Matrix jest proste i nie wymaga żadnych umiejętności technicznych. Użytkownicy mogą dołączyć do istniejącego serwera, utworzyć login i natychmiast rozpocząć czat. W tej sekcji opisano najważniejsze kroki.



### Wybierz serwer (publiczny lub prywatny)



Matrix jest siecią federacyjną: istnieje wiele serwerów (serwerów domowych) zarządzanych przez różne organizacje, społeczności lub osoby prywatne. Wybór serwera określa jedynie _gdzie_ konto jest hostowane, ale nie uniemożliwia komunikacji z całą siecią.


**Dostępne są dwie opcje:**



### - Korzystanie z serwera publicznego



To najprostsze rozwiązanie.


Przykłady popularnych serwerów:





- _matrix.org_ (najbardziej znany)
- _envs.net_
- tematyczne serwery społeczności (technologia, prywatność, open-source...)



Serwery te są odpowiednie dla początkujących użytkowników, którzy chcą się szybko zarejestrować.



### - Korzystanie z prywatnego serwera



Idealny dla :





- organizacja,
- rodzina,
- projekt open source,
- zespół roboczy,
- lub do suwerennego, samodzielnego użytku.



W takim przypadku ktoś musi administrować serwerem (Synapse, Dendrite, Conduit...).


Niezależnie od wybranego serwera, użytkownicy mogą ze sobą rozmawiać dzięki federacji.



### Tworzenie konta krok po kroku



Ponieważ Matrix jest protokołem otwartym, dostęp do niego może uzyskać wiele aplikacji.


Jak opisano powyżej, oferują one różne interfejsy i funkcje w zależności od wymagań:





- Element**: najbardziej kompletny klient, dostępny na wszystkich platformach.
- FluffyChat**: prosta, nowoczesna i idealna na telefony komórkowe.
- Nheko**: lekki, ergonomiczny klient dla komputerów PC.
- SchildiChat**: Wariant Element z ulepszeniami ergonomicznymi.
- NeoChat**: zintegrowany z ekosystemem KDE.



Wybór klienta nie ma wpływu na konto: wszystkie działają z dowolnym serwerem Matrix.



### Kroki klasyczne :





- Otwórz wybraną aplikację. W naszym przypadku zrobimy to za pomocą [Element](app.element.io).
- Wybierz opcję "Utwórz konto".



![cover-kali](assets/fr/10.webp)



Dla uproszczenia można utworzyć konto Matrix za pomocą **Google, Facebooka, Apple, GitHub lub GitLab**. Usługi te będą wiedzieć tylko, że ich konto zostało użyte do uzyskania dostępu do Matrix: jest to znane jako **połączenie społecznościowe**.



Dla większej poufności można również zarejestrować się ręcznie, wybierając **nazwę użytkownika**, **hasło** i **adres e-mail**.



W zależności od wybranego serwera może być wymagana **captcha**, a także akceptacja **warunków użytkowania**.



Po zatwierdzeniu rejestracji wysyłana jest wiadomość e-mail z potwierdzeniem.


Wystarczy kliknąć łącze, aby aktywować konto i uzyskać dostęp do aplikacji internetowej (Element), aby dołączyć do pierwszych rozmów Matrix.



![cover-kali](assets/fr/11.webp)



Masz teraz konto i korzystasz z internetowej wersji Element.



## Dodaj swój pierwszy kontakt



Aby komunikować się z kimś w Matrix, wystarczy znać jego pełny identyfikator, zwany **Matrix ID**.



Przykład:



`@alice:matrix.org @bened:monserveur.bj`



### Dodaj kontakt



Aby zaprosić znajomych do czatu grupowego, kliknij kółko `i` w prawym górnym rogu. Spowoduje to otwarcie panelu po prawej stronie. Kliknij "Osoby", aby wyświetlić listę członków w tym pokoju: w tej chwili powinieneś być jedyną obecną osobą.



![cover-kali](assets/fr/12.webp)



Kliknij "Zaproś do tego pokoju" u góry listy osób, a otworzy się okno, w którym możesz zaprosić znajomych, aby dołączyli do Ciebie w Matrix. Jeśli są już zalogowani do Matrix, wprowadź ich Matrix ID. Jeśli nie, wpisz ich adres e-mail, a zostaną zaproszeni do dołączenia do nas.



Nie ma systemu "znajomych": kontakt to po prostu osoba, z którą rozpoczęto rozmowę.



![cover-kali](assets/fr/13.webp)



Zaproszona osoba może zaakceptować lub odrzucić zaproszenie. Jeśli zaakceptuje, powinna dołączyć do pokoju. Im więcej, tym weselej!



![cover-kali](assets/fr/14.webp)



### Konfiguracja własnego serwera



Matrix naprawdę sprawdza się w połączeniu z osobistym serwerem.


Wdrożenie własnego serwera domowego pozwala na :





- zachować pełną kontrolę nad danymi,
- zdefiniować własne zasady użytkowania,
- hostowanie wielu kont (znajomych, zespołu, społeczności),
- i zapewnić maksymalną odporność w przypadku ograniczeń lub cenzury.



**Dostępne rozwiązania:**





- Synapse**: historyczna i najbardziej kompletna implementacja.
- Dendrite**: lżejszy, mocniejszy i zaprojektowany z myślą o przyszłości protokołu.
- Conduit**: minimalistyczny wariant, który jest łatwy do wdrożenia.



**Wymagania wstępne:**





- nazwa domeny,
- maszyna lub VPS,
- minimalne umiejętności administrowania systemem.



Nawet jeśli wymaga to nieco konfiguracji, zarządzanie własnym serwerem zamienia Matrix w suwerenne i trwałe narzędzie.



### Udział w pierwszych targach



Matrix opiera się w dużej mierze na _rooms_ (pokojach dziennych).


Istnieją targi publiczne, prywatne, społeczne, techniczne, lokalne i międzynarodowe.



**Trzy sposoby na dołączenie do salonu:**



1. **Poprzez link zaproszenia** (często w formie adresu URL `matrix.to`).


2. **Wyszukiwanie nazwy salonu** w aplikacji.


3. **Wprowadzając pełny identyfikator programu**, np :


`#bitcoin:matrix.org`


`#communauté-bénin:monsrv.bj`



Po dołączeniu, chatroom zachowuje się jak klasyczna grupa dyskusyjna, z historią, szyfrowaniem, plikami, reakcjami i połączeniami audio/wideo, w zależności od używanego klienta.



![capture](assets/fr/09.webp)



## Idąc dalej



Po opanowaniu podstaw Matrix oferuje wiele zaawansowanych możliwości. Niezależnie od tego, czy chcesz połączyć inne systemy przesyłania wiadomości, hostować własny serwer, czy zorganizować społeczność, ekosystem jest bardzo bogaty.



### Mosty (WhatsApp, Telegram, Signal itp.)



Most łączy Matrix z innymi systemami przesyłania wiadomości.


Za jego pomocą można wysyłać i odbierać wiadomości z :





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Discord
- Luz**
- IRC** (IRC)
- i wiele innych



### Co mogą zrobić mosty





- Scentralizuj wszystkie rozmowy w Matrix
- Zapewnienie otwartego interfejsu do interakcji z zastrzeżonymi usługami
- Zarządzanie wieloplatformową społecznością z jednego miejsca



Niektóre mosty są oficjalne, inne oparte na społeczności.


W zależności od działu, mogą one wymagać :





- osobisty serwer,
- dodatkowa konfiguracja,
- lub wykorzystanie istniejącego mostu publicznego.



### Korzystanie z Matrix dla organizacji, społeczności lub projektu Bitcoin



Matrix to nie tylko narzędzie osobiste.


Może być wykorzystywany do strukturyzowania grup roboczych, organizowania lokalnych społeczności lub zarządzania komunikacją w ramach projektu.



**Przykłady użycia:**





- Społeczności open source
- Projekty ekosystemów Bitcoin i Lightning
- Grupy studentów lub deweloperów
- Organizacje obywatelskie
- Niezależne media
- Lokalne grupy i stowarzyszenia



**Dlaczego jest to interesujące?





- narzędzie w 100% open-source**
- Suwerenna i zdecentralizowana** komunikacja
- Przestrzenie podzielone na **salony**, **podgrupy**, **prywatne salony** itp.
- Integracja z Nextcloud, GitLab, Mattermost lub niestandardowymi botami
- Dopracowane zarządzanie uprawnieniami i moderacją



Matrix staje się wówczas filarem komunikacji dla każdej struktury, która chce pozostać niezależna od dużych scentralizowanych platform.



## Wnioski



Matrix stanowi nowoczesne, otwarte i bezpieczne rozwiązanie do komunikacji w czasie rzeczywistym, oferując zdecentralizowaną alternatywę dla tradycyjnych platform. Dzięki swojej federacyjnej architekturze i zaawansowanym protokołom szyfrowania, pozwala użytkownikom zachować kontrolę nad swoimi danymi, jednocześnie ciesząc się płynnym, interoperacyjnym doświadczeniem. Niezależnie od tego, czy chodzi o użytek osobisty, zawodowy czy społecznościowy, Matrix oferuje solidne i skalowalne ramy do budowania środowisk komunikacyjnych dostosowanych do dzisiejszych potrzeb.



Aby dowiedzieć się więcej i odkryć wszystkie funkcje oferowane przez Matrix, można zapoznać się z oficjalną dokumentacją dostępną tutaj :


[https://matrix.org/docs/](https://matrix.org/docs/)