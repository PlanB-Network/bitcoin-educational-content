---
name: VirtualBox
description: Zainstaluj VirtualBox na Windows 11 i utwórz pierwszą maszynę wirtualną
---
![cover](assets/cover.webp)



___



*Ten samouczek jest oparty na oryginalnej treści autorstwa Floriana Burnela opublikowanej na stronie [IT-Connect](https://www.it-connect.fr/). Licencja [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). W oryginalnym tekście mogły zostać wprowadzone zmiany



___




## I. Prezentacja



W tym samouczku dowiemy się, jak zainstalować VirtualBox w systemie Windows 11, aby tworzyć maszyny wirtualne, niezależnie od tego, czy chodzi o system Windows 10, Windows 11, Windows Server czy dystrybucję Linuksa (Debian, Ubuntu, Kali Linux itp.).



Ten samouczek wprowadzający do VirtualBox pomoże ci rozpocząć pracę z tym rozwiązaniem wirtualizacyjnym typu open source opracowanym przez Oracle, które jest całkowicie bezpłatne. Później w sieci pojawią się kolejne poradniki, które pozwolą ci zgłębić ten temat.



Jeśli chodzi o wirtualizację stacji roboczej, czy to do celów testowych w ramach projektu, czy podczas studiów informatycznych, VirtualBox jest zdecydowanie dobrym rozwiązaniem. Jest to również alternatywa dla innych rozwiązań, takich jak Hyper-V, który jest zintegrowany z systemami Windows 10 i Windows 11 (a także Windows Server) oraz VMware Workstation (płatny) / VMware Workstation Player (bezpłatny do użytku osobistego).



Moja konfiguracja: **stacja robocza z systemem Windows 11, na której zamierzam zainstalować VirtualBox**, ale można zainstalować VirtualBox na Windows 10 (lub starszej wersji), a także na Linuksie. Jeśli chodzi o maszyny wirtualne, VirtualBox obsługuje szeroką gamę systemów, w tym Windows (np. Windows 10, Windows 11, Windows Server 2022 itp.), Linux (Debian, Rocky Linux, Ubuntu, Fedora itp.), BSD (PfSense) i macOS.



## II. Pobierz VirtualBox dla Windows 11



Aby pobrać VirtualBox do instalacji na komputerze z systemem Windows, jest tylko jeden dobry Address: [oficjalna strona VirtualBox](https://www.virtualbox.org/wiki/Downloads) w sekcji "**Downloads**". Wystarczy kliknąć "Windows hosts", aby rozpocząć pobieranie tego pliku wykonywalnego o rozmiarze nieco ponad 100 MB.



![Image](assets/fr/025.webp)



## III. Instalacja VirtualBox w systemie Windows 11



### A. Instalacja VirtualBox



Instalacja VirtualBox** jest prosta, a proces jest taki sam dla wszystkich wersji systemu Windows. Zacznij od uruchomienia właśnie pobranego pliku wykonywalnego VirtualBox, a następnie kliknij "**Next**".



![Image](assets/fr/026.webp)



Tę instalację można dostosować, ale zalecam zainstalowanie wszystkich funkcji: co ma miejsce w przypadku domyślnego wyboru. Na poniższym obrazku widać różne Elements, w tym :





- VirtualBox USB Support**, aby umożliwić VirtualBox obsługę urządzeń USB
- VirtualBox Bridged Network** do integracji obsługi sieci w trybie "Bridge" (maszyna wirtualna może łączyć się bezpośrednio z siecią lokalną)
- VirtualBox Host-Only Network** do integracji obsługi sieci w trybie "Host-Only" (maszyna wirtualna może komunikować się tylko z fizycznym hostem Windows 11 i innymi maszynami wirtualnymi w tym trybie)



Kliknij "**Next**", aby kontynuować.



![Image](assets/fr/001.webp)



Kliknij "**Tak**", pamiętając, że **sieć zostanie na chwilę przerwana na komputerze z systemem Windows 11**, podczas gdy VirtualBox przeprowadzi modyfikacje sieci w celu obsługi różnych typów sieci, w tym trybu Bridge.



![Image](assets/fr/002.webp)



Po potwierdzeniu rozpocznie się instalacja... Pojawi się powiadomienie "**Do you want to install this device software?**". Zaznacz opcję "**Always trust software from Oracle Corporation**" i kliknij "**Install**". VirtualBox musi zainstalować kilka sterowników na komputerze.



![Image](assets/fr/003.webp)



Instalacja została zakończona! Zaznacz opcję "**Uruchom Oracle VM VirtualBox 6.1.34 po instalacji**" i kliknij "**Kliknij**", aby uruchomić oprogramowanie.



![Image](assets/fr/004.webp)



### B. Dodaj pakiet rozszerzeń



Wciąż na oficjalnej stronie VirtualBox (patrz poprzedni link) można pobrać oficjalny pakiet rozszerzeń, dostępny w sekcji "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**", klikając link "**Wszystkie obsługiwane platformy**". Pakiet ten umożliwia dodanie dodatkowych funkcji do VirtualBox: nie jest to obowiązkowe, ale może być przydatne! Obejmuje on na przykład obsługę USB 3.0 w maszynach wirtualnych, obsługę kamery internetowej i szyfrowanie dysków.



Otwórz VirtualBox, kliknij "**Plik**", a następnie "**Ustawienia**" w menu.



![Image](assets/fr/005.webp)



Kliknij na "**Extensions**" po lewej stronie (1), a następnie na przycisk "**+**" po prawej stronie (2), aby **załadować właśnie pobrany pakiet rozszerzeń VirtualBox** (3).



![Image](assets/fr/006.webp)



Potwierdź, klikając przycisk "**Instalacja**".



![Image](assets/fr/007.webp)



Kliknij "**OK**": oficjalny pakiet rozszerzeń został zainstalowany w instancji VirtualBox!



![Image](assets/fr/008.webp)



Przejdźmy teraz do utworzenia naszej pierwszej maszyny wirtualnej.



## IV. Tworzenie pierwszej maszyny wirtualnej VirtualBox



Aby utworzyć nową maszynę wirtualną w VirtualBox, wystarczy kliknąć przycisk "**Nowy**", aby uruchomić kreator tworzenia maszyn wirtualnych. Ponieważ jest to pierwsze uruchomienie VirtualBox, chciałbym podać kilka dodatkowych informacji na temat Interface i innych przycisków.





- Ustawienia**: ogólna konfiguracja VirtualBox (domyślny folder maszyny wirtualnej, zarządzanie aktualizacjami, język, sieci NAT, rozszerzenia itp.)
- Import**: import urządzenia wirtualnego w formacie OVF
- Export**: eksport istniejącej maszyny wirtualnej w formacie OVF w celu utworzenia urządzenia wirtualnego
- Dodaj**: dodanie istniejącej maszyny wirtualnej do wykazu VirtualBox w standardowym formacie VirtualBox (.vbox) lub w formacie XML



Po lewej stronie sekcja "**Narzędzia**" daje dostęp do **zaawansowanych funkcji, w szczególności do zarządzania siecią wirtualną, ale także do zarządzania pamięcią masową maszyn wirtualnych**. Pod pozycją "**Narzędzia**" maszyny wirtualne zostaną dodane później.



![Image](assets/fr/009.webp)



### A. Proces tworzenia maszyny wirtualnej



**Dla przypomnienia, VirtualBox obsługuje wiele systemów operacyjnych, w tym Windows, Linux i BSD. W tym przykładzie utworzę maszynę wirtualną dla systemu Windows 11. Należy wypełnić kilka pól:





- Nazwa**: nazwa maszyny wirtualnej (jest to nazwa, która będzie wyświetlana w VirtualBox)
- Folder maszyny**: miejsce przechowywania maszyny wirtualnej, wiedząc, że w tej lokalizacji zostanie utworzony podfolder z nazwą maszyny wirtualnej
- Typ**: typ systemu operacyjnego, w zależności od tego, jaki system operacyjny ma zostać zainstalowany
- Wersja**: wersja systemu, którą chcesz zainstalować, w tym przypadku Windows 11, więc "**Windows11_64**"



Kliknij "**Next**", aby kontynuować.



![Image](assets/fr/010.webp)



W zależności od systemu operacyjnego wybranego w poprzednim kroku, **VirtualBox wydaje zalecenia dotyczące zasobów, które należy przydzielić maszynie wirtualnej**. Tutaj mówimy o pamięci RAM, którą chcesz przydzielić maszynie wirtualnej. Załóżmy 4 GB, ponieważ jest to rzeczywiście zalecane dla systemu Windows 11, ale jeśli brakuje ci zasobów, określ 2 GB zamiast tego. **Kontynuuj



**Uwaga**: zasoby przydzielone maszynie wirtualnej mogą zostać zmodyfikowane później.



![Image](assets/fr/011.webp)



Jeśli chodzi o wirtualny dysk Hard, zaczynamy od zera, więc musimy wybrać "**Utwórz wirtualny dysk Hard teraz**", aby maszyna wirtualna miała przestrzeń dyskową do zainstalowania systemu operacyjnego i przechowywania danych. Klikamy na "**Twórz**".



![Image](assets/fr/012.webp)



VirtualBox obsługuje trzy różne formaty wirtualnych dysków Hard, co stanowi istotną różnicę w porównaniu z innymi rozwiązaniami, takimi jak VMware i Hyper-V. Do wyboru są trzy formaty:





- VDI**, oficjalny format VirtualBox
- VHD**, który jest oficjalnym formatem Hyper-V, chociaż nowy format VHDX jest obecnie częściej używany
- VMDX** to oficjalny format VMware zarówno dla VMware Workstation, jak i VMware ESXi



Aby utworzyć maszynę wirtualną, która będzie używana tylko w tej instancji VirtualBox, wybierz "**VDI**". Z drugiej strony, jeśli wirtualny dysk Hard ma zostać dołączony do hosta Hyper-V w późniejszym terminie, dobrym pomysłem może być rozpoczęcie od formatu VHD, aby uniknąć konieczności jego konwersji. Kliknij "**Next**".



![Image](assets/fr/013.webp)



**Dysk wirtualny może mieć rozmiar dynamiczny lub stały**. Gdy jest dynamiczny, plik reprezentujący **dysk wirtualny (tutaj plik .vdi) będzie rósł wraz z zapisywaniem danych na dysku**, aż osiągnie swój maksymalny rozmiar, ale nie zmniejszy się, jeśli dane zostaną usunięte. I odwrotnie, gdy ma stały rozmiar, **całkowita przestrzeń dyskowa jest przydzielana natychmiast (a zatem zarezerwowana)**, co pozwala na nieco wyższą wydajność, ale trwa dłużej, gdy dysk wirtualny jest tworzony po raz pierwszy.



Osobiście, dla testowych maszyn wirtualnych z VirtualBox, uważam tryb "**Dynamicznie alokowany**" za wystarczający.



![Image](assets/fr/014.webp)



**Następnym krokiem jest określenie rozmiaru wirtualnego dysku**, pamiętając, że domyślnie dysk będzie przechowywany w katalogu maszyny wirtualnej (można to zmienić na tym etapie). Wskazałem rozmiar 64 GB, aby spełnić wymagania systemu Windows 11, ale również w tym przypadku można przypisać mniejszy rozmiar. Kliknij "**Twórz**", aby utworzyć maszynę wirtualną!



![Image](assets/fr/015.webp)



W tym momencie maszyna wirtualna znajduje się w naszym wykazie, jest skonfigurowana, ale system operacyjny nie jest zainstalowany. Musimy sfinalizować konfigurację maszyny wirtualnej przed jej uruchomieniem.



### B. Przypisywanie obrazu ISO do maszyny wirtualnej VirtualBox



Aby zainstalować Windows 11 lub jakikolwiek inny system, potrzebujemy źródeł instalacji. W większości przypadków do instalacji systemu operacyjnego używamy obrazu dysku w formacie ISO. **Konieczne jest załadowanie obrazu ISO systemu Windows 11 do wirtualnego napędu DVD naszej maszyny wirtualnej



Kliknij maszynę wirtualną w wykazie VirtualBox (1), a następnie przycisk "**Konfiguracja**" (2), który daje dostęp do ogólnej konfiguracji tej maszyny wirtualnej. To menu służy do zarządzania zasobami (np. zwiększania pamięci RAM, konfigurowania procesora itp.) Kliknij na "**Storage**" po lewej stronie (3), na napędzie DVD, gdzie jest napisane "**Empty**" (4), a następnie kliknij na ikonę w kształcie DVD (5) i "**Choose a disk file**".



![Image](assets/fr/016.webp)



Wybierz obraz ISO systemu operacyjnego, który chcesz zainstalować, a następnie kliknij OK. Oto, co otrzymuję:



![Image](assets/fr/017.webp)



Pozostań w sekcji "**Konfiguracja**" maszyny wirtualnej, mam jeszcze kilka rzeczy do wyjaśnienia.



### C. Połączenie sieciowe maszyny wirtualnej



Przejdź do sekcji "**Sieć**" po lewej stronie. Ta sekcja pozwala zarządzać siecią maszyny wirtualnej: liczbą wirtualnych interfejsów sieciowych (do 4 na maszynę wirtualną), MAC Address i trybem dostępu do sieci (NAT, dostęp mostkowy, sieć wewnętrzna itp.). **Jeśli chcesz, aby maszyna wirtualna miała dostęp do Internetu, wybierz "NAT" lub "Bridge Access "**, ale ten drugi tryb wymaga aktywnego serwera DHCP w sieci lub będziesz musiał ręcznie skonfigurować IP Address.



Uwaga: Wrócę do części sieciowej bardziej szczegółowo w dedykowanym artykule.



![Image](assets/fr/018.webp)



### D. Liczba procesorów wirtualnych



Podobnie jak komputer fizyczny, maszyna wirtualna potrzebuje do działania pamięci RAM, dysku Hard i procesora. Kiedy tworzyliśmy maszynę wirtualną, być może zauważyłeś, że kreator nie zawierał konfiguracji procesora. Można to jednak skonfigurować w dowolnym momencie za pomocą zakładki "**System**", a następnie "**Procesor**", gdzie można wybrać liczbę wirtualnych procesorów.



Uwaga: opcja "**Enable VT-x/AMD-v nested**" jest wymagana dla wirtualizacji zagnieżdżonej.



W moim przypadku maszyna wirtualna ma 2 procesory wirtualne:



![Image](assets/fr/019.webp)



**Nie wahaj się zajrzeć do innych sekcji menu konfiguracji.



### E. Pierwszy rozruch i instalacja systemu operacyjnego



Aby uruchomić maszynę wirtualną, wystarczy wybrać ją w wykazie i kliknąć przycisk "**Start**". Otworzy się drugie okno, zapewniające wizualny przegląd maszyny wirtualnej.



![Image](assets/fr/020.webp)



Auć, dostaję paskudny błąd i moja maszyna wirtualna nie chce się uruchomić! Błąd brzmi "Logowanie do maszyny wirtualnej nie powiodło się..." z następującymi szczegółami:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



W rzeczywistości jest to normalne, ponieważ **funkcja wirtualizacji nie jest włączona na moim komputerze**! Aby rozwiązać ten problem, należy ponownie uruchomić komputer, aby uzyskać dostęp do systemu BIOS i włączyć wirtualizację.



![Image](assets/fr/021.webp)



Nie czekając, zrestartowałem komputer i **nacisnąłem klawisz "SUPPR", aby uzyskać dostęp do BIOS-u** (klawisz może się różnić w zależności od maszyny i może to być na przykład F2) mojej płyty głównej ASUS. Aby aktywować wirtualizację, w moim przypadku należy włączyć "SVM Mode". Również w tym przypadku, w zależności od płyty głównej i producenta, nazwa może się zmienić. Szukaj funkcji odnoszącej się do **AMD-V** (dla procesora AMD) lub **Intel VT-x** (dla procesora Intel).



![Image](assets/fr/022.webp)



Gdy to zrobisz, zapisz modyfikację i uruchom ponownie maszynę fizyczną... Tym razem **VirtualBox może uruchomić maszynę wirtualną** i załadować obraz ISO Windows, aby zainstalować system operacyjny! 🙂



![Image](assets/fr/023.webp)



Na naszym fizycznym hoście Windows 11, na którym zainstalowany jest VirtualBox, widzimy, że folder maszyny wirtualnej Windows 11 zawiera różne pliki.





- Plik VBOX** (w formacie XML) odpowiadający konfiguracji maszyny wirtualnej (RAM, CPU itp.)
- Plik VBOX-PREV** jest kopią zapasową poprzedniej konfiguracji
- Plik VDI** odpowiada wirtualnemu dyskowi Hard w trybie dynamicznym, więc obecnie ma tylko 13 GB, podczas gdy jego maksymalny rozmiar to 64 GB
- Plik NVRAM** zawiera stan BIOS-u maszyny wirtualnej, który jest odpowiednikiem pamięci nieulotnej maszyny fizycznej



![Image](assets/fr/024.webp)



## V. Wnioski



**VirtualBox jest teraz uruchomiony na naszej fizycznej maszynie z Windows 11! Wszystko, co pozostało, to wykorzystać go i stworzyć maszyny wirtualne! Wrócę do instalacji Windows 11 w wirtualnej maszynie VirtualBox w innym artykule. Jeśli chodzi o Windows 10, Windows Server lub dystrybucję Linuksa (Ubuntu, Debian itp.), po prostu pozwól nam Cię poprowadzić!