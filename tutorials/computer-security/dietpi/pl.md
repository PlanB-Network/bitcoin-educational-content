---
name: DietPi
description: Lekki system operacyjny zoptymalizowany pod kątem mało wydajnych maszyn. Z preferencją dla samodzielnego hostingu
---

![cover](assets/cover.webp)



W kręgach nietechnicznych, marki takie jak `Odroid`, `Raspberry Pi`, `Orange Pi` czy `Radxa`, są mało znane. Wystarczy jednak zajrzeć do kręgów technicznych, by przekonać się, że komputery **SBC** - zbudowane na pojedynczej płycie głównej, często mikroskopijnych rozmiarów w porównaniu do powszechnie używanych komputerów - stają się niezbędne jako wsparcie dla każdego osobistego projektu.



Są to komputery produkowane w szerokiej gamie modeli. Preferowane są na nich dystrybucje Linuksa, często przystosowane do płynnego działania na tych słabszych maszynach.



**DietPi nie jest wyjątkiem**: jest to system operacyjny oparty na Debianie, zoptymalizowany tak, aby był jak najlżejszy i sprawiał, że nawet najmniej wydajne `SBC` będą bardzo szybkie. Przełączony z Debiana12 Bookworm na Debiana13 Trixie w trakcie pisania tego poradnika, obsługuje teraz również procesory SBC oparte na otwartym kodzie źródłowym `RISC-V`. DietPi jest przyjemnym odkryciem, które zasługuje na dalsze badania.



## Mocne strony



To nie jest "zwykły duplikat" Debiana dla małych płyt typu Raspberry. Jest nim DietPi:




- Zoptymalizowany pod kątem szybkości i lekkości**: [porównanie z innymi dystrybucjami Debiana dla SBC](https://dietpi.com/blog/?p=888), DietPi jest lżejszy we wszystkim. Obraz ISO DietPi waży mniej niż 1 GB, zdecydowanie najmniej wśród tych dedykowanych starszym modelom Raspberry lub Orange PI (na przykład). Zapotrzebowanie na pamięć RAM i zasoby procesora jest bardzo niskie, dzięki czemu zawsze wydobywa to, co najlepsze z płyt, nawet tych starszych.
- Wbudowane automatyzacje i instalatory**: Zestaw dedykowanych poleceń pomaga użytkownikom monitorować zasoby systemowe, a także automatyzować zadania w celu instalowania i uruchamiania programów, aktualizowania wersji, tworzenia kopii zapasowych i sprawdzania wszystkich dzienników.
- Silna, zorientowana na eksperymenty społeczność**: [tutoriale](https://dietpi.com/forum/c/community-tutorials/8) i projekty społeczności DietPi, są idealne do czerpania inspiracji z oprogramowania, które można zainstalować jednym kliknięciem, dzięki DietPi.



**Wyciśnięcie każdego kawałka z SBC nigdy nie było łatwiejsze**.



## Automatyzacja dla samodzielnego hostingu


Chcesz poeksperymentować z własnym serwerem, aby uruchomić zaawansowane rozwiązania sieciowe lub narzędzia do rozwijania swojej wiedzy Bitcoin? DietPi może być rozwiązaniem, którego szukałeś. Chociaż wiele osób wie, jak zarządzać własną infrastrukturą i uruchamiać doskonale skonfigurowane i chronione serwery, DietPi jest odpowiednim krokiem dla tych, którzy chcą zacząć od zera.



Zamiast ręcznie wykonywać wszystkie złożone zadania, których wymaga takie zadanie, DietPi pozwala budować je za pomocą `wizarda` i własnego wiersza poleceń. Tutaj możesz eksperymentować z własną chmurą osobistą, zarządzaniem urządzeniami _smart home_, automatycznymi kopiami zapasowymi i crontabem, a także bardziej zaawansowanymi rozwiązaniami.



![img](assets/en/01.webp)



## Instalacja



### Pobierz



DietPi oferuje niezliczony zestaw obrazów ISO, aby nagrać system operacyjny na wiele różnych urządzeń. Niektóre z nich są tylko obsługiwane: na przykład ISO dla Raspberry PI5 jest wciąż w fazie testów, ale z pewnością można znaleźć odpowiednie dla swojej płyty.



W tym przewodniku zdecydowałem się zainstalować go na cienkim kliencie, więc wybór padł na _PC/VM_, a następnie na _Native PC_. Istnieją dwa obrazy ISO dla tych urządzeń, które różnią się generacją bootloadera. Maszyna używana w samouczku jest dość stara, więc wybór padł na wersję _BIOS/CSM_. Jeśli masz nowszą maszynę, właściwą wersją może być `UEFI`.



![img](assets/en/02.webp)



Wylądujesz na stronie zawierającej `obraz instalatora`, `sha256` i `Podpisy`.



![img](assets/en/03.webp)



Przygotuj katalog w `home` swojego codziennego komputera, abyś mógł pobrać niezbędne pliki za pomocą `wget`.



![img](assets/en/04.webp)



Klucz publiczny dewelopera wymagał minimum poszukiwań, ale można go znaleźć pod tym linkiem: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Sprawdź zawartość katalogu za pomocą `ls -la` i zaimportuj klucz MichaIng do swojego keyringu za pomocą `gpg --import`.



### Weryfikacja i flash



Wreszcie, część, którą polecam najbardziej: upewnij się co do autentyczności systemu operacyjnego, który pobrałeś i zamierzasz zainstalować na swoim SBC.



![img](assets/en/06.webp)



Jeśli otrzymałeś również wynik `Dobry podpis` i tę samą kontrolę Hash za pomocą polecenia sha256sum, możesz przystąpić do flashowania ISO na pamięć USB. Użyj do tego aplikacji takich jak Whale Etcher.



![img](assets/en/07.webp)



## Instalacja DietPi



![img](assets/en/09.webp)



Przenieś dysk flash do urządzenia, które będzie hostować DietPi i rozpocznij instalację systemu operacyjnego lime Green. W tym ćwiczeniu używamy cienkiego klienta z 16 GB pamięci RAM, dyskiem SSD o pojemności 128 GB dla systemu operacyjnego i drugim dyskiem na dane o pojemności 1 TB. Instalacja zajęła mniej niż 30 minut, ale jeśli będziesz używać na przykład Raspberry, zasoby mogą być mniejsze i potrwać dłużej. Postęp instalacji będzie wyświetlany na bieżąco.



![img](assets/en/08.webp)



Będąc zaprojektowanym dla Raspberry i podobnych, prawdziwą naturą DietPi jest tak zwana "bezgłowa" instalacja, bez środowiska graficznego i z natywnym dostępem do "shsh". W przewodniku zamiast tego zobaczysz środowisko graficzne, a dokładniej LXDE.



Podczas tego kroku zostaniesz również poproszony o wybranie przeglądarki internetowej, której chcesz używać domyślnie, pomiędzy Chromium i Firefox. Obie działają dobrze; nie ma żadnych szczególnych przeciwwskazań dla żadnej z nich, poza osobistymi preferencjami.



Pod koniec instalator może zapytać, czy chcesz już zainstalować jakieś programy, ale tutaj **radzę nie ładować niczego wstępnie**. Powinieneś wiedzieć, że po tym kroku zostaniesz poproszony o zmianę domyślnych haseł dwóch użytkowników, ze względów bezpieczeństwa. Co najważniejsze, będziesz musiał **ustawić `Globalne Hasło Oprogramowania (GSP)`**, które zapewni dostęp do różnych programów w kontrolowany sposób. **Jeśli pobierzesz jakiekolwiek oprogramowanie podczas instalacji systemu operacyjnego, bez ustawionego `GSP`, pozostaną one praktycznie niedostępne**. Będziesz musiał je odinstalować i zainstalować ponownie po ustawieniu `Global Software Password`: dlatego **nie wprowadzaj niczego, aby uniknąć podwójnej pracy**. (Niedogodność jest prawdopodobna, nie w 100% pewna).



Instalacja kończy się prośbą o aktywację DietPi-Survey, zautomatyzowanej usługi gromadzenia danych wykorzystywanej do wspierania rozwoju systemu operacyjnego. Zgodnie ze stroną internetową, gromadzenie danych jest aktywowane po pobraniu dowolnego oprogramowania z automatyzacji dostarczonej przez DietPi lub po uaktualnieniu do następnej wersji. Każdy ma możliwość wyrażenia zgody (_Opt IN_) lub rezygnacji (_Opt OUT_).



![img](assets/en/23.webp)



Po zakończeniu instalacji i późniejszym ponownym uruchomieniu, DietPi pojawia się na ekranie podczas konfiguracji. Na potrzeby samouczka, jak już wspomniałem, wybrałem środowisko graficzne `LXDE`. Na pulpicie znalazłem skrót do uruchomienia `htop` i otwartego terminala.



![img](assets/en/10.webp)



### "Narzędzia" z systemu operacyjnego



Zapomnij o większości programów, których używasz w swojej dystrybucji Linuksa - DietPi jest tak zoptymalizowany, że pominąłeś całkiem sporo. Zasadniczo musiałbyś zainstalować wiele poleceń ręcznie, ale jeśli dopiero próbujesz, oprzyj się pokusie i spróbuj przetestować automatyzację DietPi.



Jest to zdecydowanie terminal, który jest pierwszym użytecznym narzędziem do rozpoczęcia pracy z nowym systemem operacyjnym i otwiera się automatycznie po każdym włączeniu.



![img](assets/en/11.webp)



Na ekranie terminala znajdziesz serię poleceń poprzedzonych `dietpi-` reprezentujących [narzędzia](https://dietpi.com/docs/dietpi_tools/) tego systemu operacyjnego:




- `dietpi-launcher`: aby uzyskać dostęp do systemu operacyjnego, menedżera plików itp
- `dietpi-Software`: reprezentuje narzędzie, za pomocą którego można zainstalować całe oprogramowanie dostępne w pakiecie
- `dietpi-config`: dostęp do konfiguracji systemu, nawet tych najbardziej zaawansowanych.



![img](assets/en/14.webp)



### Kopia zapasowa



Tworzenie kopii zapasowej serwera to rutynowa czynność, którą administrator systemu powinien przewidzieć od pierwszego uruchomienia.



W DietPi dostępne jest polecenie `dietpi-Backup`, które polecam zbadać, aby znaleźć idealne rozwiązanie: pozwala ono skonfigurować regularną kopię zapasową, przyrostową lub nie, w zależności od używanych aplikacji, oraz wszystkie opcje dostosowywania procedury.



![img](assets/en/22.webp)



Wybierz miejsce docelowe kopii zapasowej, na przykład inny dysk, uruchamiając `dietpi-Drive_Manager`, aby zamontować dysk docelowy i użyć go do tej funkcji.



## Konfiguracja



Samodzielny hosting to wskazane doświadczenie dla każdego, niezależnie od tego, czy jest ciekawy, czy po prostu entuzjastyczny. Jednak uruchomienie i skonfigurowanie serwera wiąże się z niemałymi wyzwaniami technologicznymi. W tym miejscu pojawia się **prostota DietPi**, która pozwala skonfigurować system dostosowany do własnych potrzeb w kilku prostych krokach.



![img](assets/en/24.webp)



Podstawowe i zaawansowane ustawienia, wszystko na wyciągnięcie ręki w jednym Interface dostępnym wraz z poleceniem:



``dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-software


```