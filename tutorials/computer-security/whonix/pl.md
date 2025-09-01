---
name: Whonix
description: Zachowanie prywatności i poufności.
---

![cover](assets/cover.webp)



**Whonix** to dystrybucja Linuksa oparta na **Debianie**, zaprojektowana w celu zapewnienia środowiska łączącego **bezpieczeństwo**, **anonimowość** i **prywatność**. Łatwy w nauce i kompatybilny z różnymi interfejsami (maszyny wirtualne, Qubes OS, tryb Live), zawiera domyślnie routing ruchu sieciowego przez **Tor**, **podwójny firewall** (jeden firewall na bramie i drugi na stacji roboczej), **pełną ochronę przed wyciekami IP/DNS** i narzędzia do skutecznego maskowania aktywności przed obserwatorami sieci, w tym przed dostawcą usług internetowych. Więcej niż tylko anonimowy system, **Whonix** jest kompletnym, bezpiecznym środowiskiem programistycznym.



## Dlaczego warto wybrać Whonix?





- Darmowy**: Podobnie jak większość dystrybucji Linuksa, Whonix jest systemem open-source licencjonowanym całkowicie za darmo. Jest rozwijany w modelu open source, z aktywną i przejrzystą społecznością.
- Prywatność, bezpieczeństwo i anonimowość**: Głównym celem Whonix jest oferowanie ultra bezpiecznego środowiska, w którym wszystkie dane są chronione, a komunikacja szyfrowana za pośrednictwem sieci Tor.
- Łatwy w użyciu**: Whonix oferuje intuicyjny, wstępnie skonfigurowany graficzny Interface, odpowiedni nawet dla początkujących użytkowników. Nie trzeba być ekspertem, aby korzystać z zaawansowanej ochrony.
- Idealne środowisko do bezpiecznego rozwoju**: Whonix umożliwia tworzenie, testowanie, audytowanie lub uruchamianie programów bez ujawniania prawdziwego adresu IP Address lub nawyków związanych z przeglądaniem lub komunikacją sieciową.
- Sesje jednorazowe i tryb Live**: Whonix może być uruchamiany w trybie Live lub za pośrednictwem maszyn jednorazowych (np. za pośrednictwem **Qubes OS**), umożliwiając wykonywanie krytycznych zadań bez pozostawiania trwałych śladów po zakończeniu sesji.
- Stosunkowo prosta instalacja**: Dostarczane są gotowe do użycia obrazy umożliwiające szybką instalację w maszynach wirtualnych (VirtualBox, KVM, Qubes). System jest udokumentowany i regularnie aktualizowany.



## Instalacja i konfiguracja



Zanim przejdziemy do instalacji Whonix, należy pamiętać, że ta dystrybucja **nie jest jeszcze oficjalnie dostępna** jako główny system, który można zainstalować bezpośrednio na dysku Hard (w trybie bare metal). Innymi słowy, nie można jeszcze zainstalować Whonix jako klasycznego systemu operacyjnego**, takiego jak Ubuntu lub standardowy Debian.



Dostępnych jest jednak kilka wersji, dzięki czemu Whonix może być używany **ulotnie** (tryb Live, sesje tymczasowe) lub **trwale** (za pośrednictwem maszyn wirtualnych lub integracji z Qubes OS).



Dla długoterminowego, stabilnego użytkowania, **wirtualizacja jest obecnie jedyną oficjalnie zalecaną metodą**. Whonix można uruchomić za pomocą **VirtualBox** (Whonix-Gateway i Whonix-Workstation) lub zintegrować go z systemem takim jak **Qubes OS**. W tym samouczku skupimy się na instalacji VirtualBox.



### Wymagania wstępne



Zanim będzie można zainstalować Whonix w trybie wirtualnym, należy upewnić się, że komputer spełnia minimalne wymagania techniczne. Wirtualizacja wymaga pewnych zasobów, które nie wszystkie komputery mogą zaoferować. Dlatego ważne jest, aby procesor obsługiwał technologię wirtualizacji (Intel VT-x lub AMD-V) i aby ta opcja była włączona w BIOS-ie/UEFI.



Oto zalecane specyfikacje dla płynnego i stabilnego korzystania z Whonix:





- Pamięć o dostępie swobodnym (RAM)**: zdecydowanie zalecane jest minimum **8 GB**. Im więcej pamięci RAM, tym więcej zasobów można przydzielić maszynom wirtualnym (Gateway i Workstation), poprawiając ich wydajność.
- Dostępne miejsce na dysku**: należy zapewnić co najmniej 30 GB wolnego miejsca na dysku**. Obejmuje to przestrzeń wymaganą dla dwóch maszyn wirtualnych, plików systemowych i wszelkich danych lub migawek.
- Procesor**: zalecany jest procesor z co najmniej **4 fizycznymi rdzeniami** (8 logicznymi wątkami), zwłaszcza jeśli chcesz równolegle uruchamiać inne usługi lub narzędzia.



### Pobierz Whonix



Whonix jest dostępny w kilku wersjach, w zależności od rodzaju środowiska, w którym chcesz go używać. Dla większości użytkowników (Windows, Linux lub MacOs), edycja VirtualBox jest najłatwiejsza do skonfigurowania. Obraz można pobrać bezpośrednio z [oficjalnej strony](https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **nie jest kompatybilny** z MacBookami używającymi procesorów Apple Silicon (architektura ARM).



## Instalacja VirtualBox



Do uruchomienia Whonix potrzebny jest **hiperwizor**, taki jak VirtualBox, Qubes lub KVM.



Po pobraniu pliku zainstaluj go tak, jak każde inne oprogramowanie. Zaakceptuj domyślne opcje, chyba że masz określone wymagania. Zgubiłeś się? Zapoznaj się z naszym przewodnikiem po VirtualBox.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Importowanie Whonix



Po zainstalowaniu VirtualBox można zaimportować pobrane wcześniej pliki Whonix `.ova` (`Whonix-Gateway-Xfce.ova` i `Whonix-Workstation-Xfce.ova`).



Otwórz VirtualBox, a następnie kliknij **File → Import appliance**.


Wybierz odpowiedni plik `.ova` (zacznij od Gateway).



![0_03](assets/fr/03.webp)



Wybierz lokalizację, w której będą przechowywane pliki maszyny wirtualnej Whonix.



![0_04](assets/fr/04.webp)



Zaakceptuj warunki użytkowania, a następnie uruchom import i poczekaj na zakończenie procesu.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Konfiguracja Whonix



Przed uruchomieniem Whonix ważne jest, aby dostosować niektóre **ustawienia systemowe**, aby zapewnić lepszą wydajność:



Wybierz maszynę wirtualną **Whonix-Workstation-Xfce**, a następnie kliknij **Konfiguracja**.



![0_06](assets/fr/07.webp)



Przejdź do zakładki **System**, gdzie domyślna alokacja pamięci RAM wynosi 2048 MB. Zalecamy **zwiększenie jej do 4096 MB (4 GB)** w celu uzyskania większej płynności, zwłaszcza jeśli zamierzasz otworzyć kilka aplikacji lub pracować w długich sesjach. Brama może pozostać na poziomie 2048 MB, chyba że używasz wielu połączeń Tor równolegle.



![0_08](assets/fr/08.webp)



### Rozpoczęcie pracy z Whonix



Aby Whonix działał prawidłowo i bezpiecznie, **musisz przestrzegać tej sekwencji uruchamiania**:



Najpierw należy uruchomić maszynę **Whonix-Gateway-Xfce**. Ta maszyna jest odpowiedzialna za kierowanie całego ruchu przez sieć **Tor**. Bez uruchomionej bramy, żaden ruch nie będzie kierowany przez sieć Tor i utracisz anonimowość.



![0_09](assets/fr/09.webp)



Po pełnym uruchomieniu Gateway (zobaczysz, że Tor jest podłączony), możesz uruchomić **Whonix-Workstation-Xfce**, który automatycznie połączy się przez Gateway.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Aktualizacja systemu



Przejdź do terminala i wprowadź następujące polecenie, aby zaktualizować listę pakietów:



```shell
sudo apt update
```



Następnie uruchom następujące polecenie, aby zainstalować dostępne aktualizacje:



```shell
sudo apt full-upgrade
```



## Odkryj Whonix



**Whonix** to system zaprojektowany w celu zapewnienia **bezpiecznego**, **anonimowego** i **poufnego** środowiska komputerowego, idealnego do surfowania po Internecie bez narażania tożsamości lub danych. Aby to osiągnąć, jest on wyposażony w szereg przydatnych aplikacji codziennego użytku zaprojektowanych w celu wzmocnienia bezpieczeństwa cyfrowego od samego początku.


### KeepassXC



**KeePassXC** to zintegrowany menedżer haseł firmy Whonix. Umożliwia on **tworzenie, przechowywanie i zarządzanie** hasłami w bezpieczny sposób, bez konieczności zapamiętywania ich wszystkich ręcznie. Hasła są przechowywane w **szyfrowanej bazie danych**, chronionej hasłem głównym.



### Przeglądarka Tor



**Tor Browser** jest domyślną przeglądarką internetową Whonix. Opiera się ona na sieci **Tor**, która przekierowuje ruch przez kilka przekaźników na całym świecie, dzięki czemu identyfikacja prawdziwego adresu IP Address jest praktycznie niemożliwa.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Electrum Bitcoin Wallet



**Electrum** to lekki i szybki Bitcoin Wallet, preinstalowany na Whonix, aby umożliwić anonimowe zarządzanie **transakcjami kryptowalutowymi**. Nie pobiera całego Blockchain, ale wykorzystuje zdalne serwery do uzyskania niezbędnych informacji, dzięki czemu jest znacznie lżejszy niż pełny Wallet.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix to coś więcej niż tylko system operacyjny: to prawdziwe **bezpieczne środowisko** zaprojektowane w celu ochrony anonimowości, prywatności i wrażliwych działań. Dzięki architekturze opartej na Torze, inteligentnemu partycjonowaniu między Gateway i Workstation oraz preinstalowanym narzędziom, takim jak Tor Browser, KeePassXC i Electrum, oferuje gotowe rozwiązanie dla każdego, kto chce **przeglądać anonimowo**, **bezpiecznie pracować** lub **obsługiwać poufne dane**.



Aby zwiększyć bezpieczeństwo systemu Unix, zapoznaj się z naszym samouczkiem dotyczącym audytu komputera: sprawdź luki w zabezpieczeniach systemu operacyjnego i upewnij się, że Twoje dane nie są zagrożone.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af