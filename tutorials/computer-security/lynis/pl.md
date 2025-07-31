---
name: Lynis
description: Przeprowadzenie audytu bezpieczeństwa maszyny z systemem Linux za pomocą Lynis
---
![cover](assets/cover.webp)



___



*Ten samouczek jest oparty na oryginalnej treści autorstwa Fares CHELLOUG opublikowanej na [IT-Connect](https://www.it-connect.fr/). Licencja [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). W oryginalnym tekście mogły zostać wprowadzone zmiany



___



## I. Prezentacja



**W tym poradniku nauczymy się jak przeprowadzić audyt bezpieczeństwa na maszynie z systemem Linux przy użyciu Lynis! Dla tych z was, którzy nie znają **Lynis,** jest to małe narzędzie wiersza poleceń, które przeanalizuje konfigurację twojego serwera i wyda zalecenia dotyczące **poprawy bezpieczeństwa twojej maszyny**



Lynis to narzędzie open source od CISOFY, firmy specjalizującej się w **audytowaniu i wzmacnianiu systemów**. Jeśli chcesz poczynić postępy w hartowaniu Linuksa i popularnych usług (SSH, Apache2 itp.), Lynis jest twoim sprzymierzeńcem! Lynis nie tylko powie ci, co jest nie tak, ale także dostarczy zaleceń, które wskażą ci właściwy kierunek (i zaoszczędzą czas).



**Lynis** współpracuje z większością dystrybucji Linuksa, w tym: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis jest przeznaczony dla użytkowników Linux / UNIX, ale jest również **kompatybilny z macOS**. Bardzo szybki w instalacji, nie ma zarządzania zależnościami na poziomie pakietów.



Jest on używany do różnych celów:





- Audyty bezpieczeństwa
- Testy zgodności (PCI, HIPAA i SOX)
- Trudniejsze konfiguracje systemu
- Wykrywanie luk w zabezpieczeniach



Narzędzie jest szeroko stosowane przez szerokie grono użytkowników, w tym administratorów systemów, audytorów IT i pentesterów. W przypadku analiz, narzędzie opiera się na standardach takich jak **CIS Benchmark, NIST, NSA, OpenSCAP** oraz na oficjalnych zaleceniach **Debian, Gentoo, Red Hat**.



Projekt jest dostępny pod tym Address na **Github**:





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Pobierz Lynis z CISOFY](https://cisofy.com/lynis/#download)



W tym samouczku krok po kroku będę **używał VPS z Debianem 12** i skoncentruję się na części SSH, ponieważ chciałbym sprawdzić jego konfigurację i ją ulepszyć.



## II. Pobieranie i instalacja



Istnieje kilka sposobów na pobranie i zainstalowanie Lynis. Wybierz preferowany z poniższej listy.



### A. Instalacja z repozytoriów Debiana



Ten tryb instalacji pozwala na użycie polecenia **lynis** z dowolnego miejsca w systemie, w przeciwieństwie do instalacji ze źródła, gdzie musisz znajdować się w katalogu.



Połącz się z serwerem przez SSH i wprowadź następujące polecenia, aby zainstalować Lynis :



```
sudo apt-get update
sudo apt-get install lynis -y
```



To jest to, co otrzymujesz:



![Image](assets/fr/024.webp)



### B. Pobierz z oficjalnej strony internetowej



Można go również pobrać ze strony internetowej Cisofy:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



To jest to, co otrzymujesz:



![Image](assets/fr/032.webp)



Następnie rozpakujemy archiwum za pomocą następującego polecenia:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



To jest to, co otrzymujesz:



![Image](assets/fr/020.webp)



Przejdźmy do folderu **lynis**:



```
cd lynis
```



Możemy sprawdzić dostępność aktualizacji za pomocą następującego polecenia:



```
./lynis update info
```



To jest to, co otrzymujesz:



![Image](assets/fr/023.webp)



### C. Pobierz z GitHub



Pobierzemy **Lynis** z oficjalnego repozytorium GitHub, używając następującego polecenia (*git* musi być obecny na twoim komputerze):



```
git clone https://github.com/CISOfy/lynis.git
```



To jest to, co otrzymujesz:



![Image](assets/fr/060.webp)



## III. Korzystanie z Lynis



Lynis jest obecny na naszym komputerze, więc nauczmy się go używać!



### A. Główne elementy sterujące i opcje



Aby wyświetlić dostępne polecenia, wystarczy wpisać następującą komendę:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe :
./lynis
```



To jest to, co otrzymujesz:



![Image](assets/fr/039.webp)



Dostępne są również następujące opcje:



![Image](assets/fr/040.webp)



Aby wyświetlić wszystkie dostępne polecenia, wprowadź następujące polecenie:



```
sudo lynis show
```



To jest to, co otrzymujesz:



![Image](assets/fr/022.webp)



Aby wyświetlić wszystkie opcje, należy wprowadzić :



```
sudo lynis show options
```



To jest to, co otrzymujesz:



![Image](assets/fr/021.webp)



W dalszej części tego artykułu dowiemy się, jak korzystać z niektórych opcji.



### B. Przeprowadzanie audytu systemu



Poprosimy **Lynis** o audyt naszego systemu, podkreślając, co jest poprawnie skonfigurowane, a co można poprawić. Aby to zrobić, wprowadź następujące polecenie:



```
sudo lynis audit system
# ou
./lynis audit system
```



Domyślnie, jeśli nie jesteś zalogowany jako root podczas uruchamiania tego polecenia, narzędzie zostanie uruchomione z uprawnieniami aktualnie zalogowanego użytkownika. Niektóre testy nie zostaną uruchomione w tym kontekście:



![Image](assets/fr/052.webp)



Oto testy, które nie będą wykonywane w tym trybie:



![Image](assets/fr/051.webp)



Po wykonaniu polecenia rozpocznie się analiza. Wystarczy chwilę poczekać.



Na koniec audytu otrzymujemy to (widzimy, że **Lynis** poprawnie zidentyfikował system **Debian 12** i użyje **Debian plugin** do analizy):



![Image](assets/fr/017.webp)



Następnie Lynis wymieni zestaw punktów odpowiadających wszystkiemu, co sprawdził w naszym systemie. Jest to zorganizowane według kategorii, jak zobaczymy. Warto również zauważyć, że do wyróżnienia rekomendacji używany jest kolorowy kod:





- Czerwony** dla krytycznego Elements lub nieprzestrzegania najlepszych praktyk (na przykład brakujący pakiet), tj. serwer nie przestrzega tego punktu
- Żółty** dla sugestii lub częściowej zgodności z zaleceniem (powiedzmy, że plusem jest zgodność z punktem wyróżnionym tym kolorem (niepriorytetowym))
- Green** dla punktów, w których konfiguracja serwera jest zgodna
- Biały**, gdy neutralny



Tutaj widzimy, że Lynis zaleca zainstalowanie **fail2ban**:



![Image](assets/fr/057.webp)



W sekcji "**Boot i usługi**" widzimy, że ochrona usług przez *systemd* mogłaby zostać poprawiona. Z drugiej strony, Grub2 jest obecny i nie ma problemów z uprawnieniami na :



![Image](assets/fr/029.webp)



Następnie mamy sekcje "**Jądro**" i "**Pamięć i procesy**":



![Image](assets/fr/037.webp)



Następnie sekcja "**Użytkownicy, grupy i uwierzytelnianie**". Narzędzie informuje nas o ostrzeżeniu dotyczącym uprawnień katalogu "**/etc/sudoers.d**". W tej chwili nie wiemy nic więcej, ale pod koniec analizy będziemy mogli zobaczyć, jakie są zalecenia.



![Image](assets/fr/049.webp)



Oto, co można znaleźć w sekcjach "**Powłoki", "Systemy plików" i "Urządzenia USB "**. Między innymi widzimy, że istnieją sugestie dotyczące punktów montowania i że urządzenia USB są obecnie dozwolone na tym komputerze.



![Image](assets/fr/048.webp)



Następnie sekcje: "**Nazwa usług", "Porty i pakiety", "Sieć".** Wskazano tutaj, że pakiety, które nie są już używane, mogą zostać wyczyszczone i że nie ma narzędzia zdolnego do zarządzania automatycznymi aktualizacjami.



![Image](assets/fr/058.webp)



Widzimy, że firewall jest aktywowany (i tak, jest iptables!). Ponadto widzimy, że znalazł nieużywane reguły i że zainstalowany jest serwer WWW Apache.



![Image](assets/fr/055.webp)



Po tym następuje analiza samego serwera WWW, ponieważ usługa została zidentyfikowana.



Widzimy, że znalazł pliki konfiguracyjne **Nginx**, a dla części SSL/TLS **szyfry** są skonfigurowane przy użyciu protokołu, który byłby niezabezpieczony. Z drugiej strony, według Lynisa, zarządzanie logami jest prawidłowe.



![Image](assets/fr/038.webp)



Usługa SSH jest obecna na moim serwerze VPS. Jej konfiguracja jest analizowana przez Lynis. Trzeba powiedzieć, że bezpieczeństwo SSH można łatwo poprawić! Wrócimy do tego obszaru szczegółowo po uzyskaniu zaleceń.



![Image](assets/fr/026.webp)



Oto sekcje **"Obsługa SNMP", "Bazy danych", "PHP", "Obsługa Squid", "Usługi LDAP", "Rejestrowanie i pliki "**.



Jest jedna naprawdę ważna sugestia dotycząca zarządzania logami: zdecydowanie zaleca się, aby nie przechowywać logów lokalnie na komputerze. Jeśli maszyna zostałaby uszkodzona przez atakującego, jest prawdopodobne, że spróbowałby on usunąć swoje ślady... Musimy więc uzewnętrznić logi.



![Image](assets/fr/050.webp)



Tutaj mamy audyt podatnych usług, zarządzanie kontem, zaplanowane zadania i synchronizację NTP. Wskazuje się, że poziom jest niski na banerze i części identyfikacyjnej: jest to zrozumiałe, jeśli wyświetlasz wersję systemu, daje to wskazówkę potencjalnemu atakującemu. Jest to ustawienie domyślne.



Interesujące byłoby aktywowanie **auditd**, aby mieć logi na wypadek **analizy kryminalistycznej**. **NTP** jest również sprawdzany, ponieważ aby efektywnie przeszukiwać logi, lepiej jest mieć systemy na czas, co upraszcza wyszukiwanie.



![Image](assets/fr/036.webp)



Następnie Lynis przygląda się kryptograficznemu Elements, wirtualizacji, kontenerom i ramom bezpieczeństwa. Niektóre sekcje są puste, ponieważ nie ma zgodności z analizowaną maszyną. Widzimy jednak, że mam dwa wygasłe certyfikaty SSL i nie aktywowałem **SELinux**.



![Image](assets/fr/027.webp)



Tutaj również jest miejsce na ulepszenia: nie ma skanera antywirusowego ani antywirusowego, a my mamy sugestie dotyczące uprawnień do plików.



![Image](assets/fr/028.webp)



Następnie Lynis skupia się na zaostrzeniu konfiguracji jądra Linuksa (w tym reguł dla stosu IPv4), a także zarządzaniu katalogami "domowymi" maszyny z Linuksem.



![Image](assets/fr/035.webp)



Doszliśmy do końca analizy... Ten ostatni punkt pokazuje, że mielibyśmy wszystko, aby zyskać na posiadaniu ClamAV na tej maszynie.



![Image](assets/fr/030.webp)



## IV. Zalecenia



Po audycie przychodzi czas na przeczytanie i przeanalizowanie zaleceń. W tym miejscu otrzymujemy zalecenia i wyjaśnienia dotyczące każdego z testów przeprowadzonych przez Lynis.



Weźmy na przykład zalecenia dotyczące SSH. **Dla każdej sugestii znajdziesz zalecany parametr i link, który wyjaśni punkt bezpieczeństwa ** Decyzja należy do Ciebie, w zależności od kontekstu i zastosowania.



Przyjrzyjmy się kilku przykładom zaleceń, które bezpośrednio odzwierciedlają punkty podkreślone w całym audycie...



### A. Przykłady zaleceń





- Jak widzieliśmy wcześniej, NTP jest ważny dla znakowania czasem logów:



![Image](assets/fr/043.webp)





- Lynis sugeruje również zainstalowanie pakietu **apt-listbugs**, aby uzyskać informacje o krytycznych błędach podczas instalacji pakietów poprzez **apt.**



![Image](assets/fr/041.webp)





- Narzędzie sugeruje zainstalowanie **needrestart, aby móc** zobaczyć, które procesy używają starej wersji biblioteki i wymagają ponownego uruchomienia.



![Image](assets/fr/054.webp)





- Ta sugestia sugeruje zainstalowanie **fail2ban** w celu automatycznego blokowania hostów, które nie mogą się uwierzytelnić (zwłaszcza metodą brute force).



![Image](assets/fr/044.webp)





- Aby wzmocnić usługi systemowe, zaleca on uruchomienie niebieskiego polecenia dla każdej usługi na naszym komputerze.



![Image](assets/fr/056.webp)





- Sugeruje on ustawienie dat wygaśnięcia dla wszystkich chronionych haseł do kont.



![Image](assets/fr/031.webp)





- Ta sugestia sugeruje ustawienie minimalnych i maksymalnych wartości dla wieku hasła. Zapewni to między innymi regularną zmianę haseł.



![Image](assets/fr/042.webp)





- Zalecamy korzystanie z oddzielnych partycji, aby ograniczyć wpływ problemów z miejscem na dysku na jednej partycji.



![Image](assets/fr/047.webp)





- To zalecenie sugeruje wyłączenie pamięci USB i FireWire, aby zapobiec wyciekowi danych



![Image](assets/fr/033.webp)





- Aby spełnić to zalecenie, wystarczy zainstalować i skonfigurować na przykład **unnatended-upgrade**.



![Image](assets/fr/053.webp)



### B. Instalowanie zalecanych pakietów



Aby poprawić konfigurację systemu, zainstalujemy kilka pakietów na maszynie: niektóre zalecane przez Lynis, niektóre, które osobiście polecam.



Będziesz miał dobrą podstawę do pracy, o ile poświęcisz trochę czasu na ich konfigurację. Aby to zrobić, zapoznaj się z witryną IT-Connect, innymi artykułami w Internecie i dokumentacją narzędzi.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Niektóre informacje o zainstalowanych pakietach :





- Clamav** to program antywirusowy.
- unattend-upgrades** umożliwia automatyczne zarządzanie aktualizacjami, a nawet ponowne uruchomienie komputera lub automatyczne usuwanie starych pakietów, jest w pełni konfigurowalny.
- rkhunter** to antyrootkit, który skanuje system plików.
- Fail2ban** będzie bazował na plikach dziennika zgodnie z tym, co dasz mu do odczytu i będzie współpracował z **iptables**, na przykład w celu zablokowania adresów IP, które próbują "brute force" twojego serwera w SSH.



### C. Zalecenia dla SSH



Przyjrzyjmy się zaleceniom SSH. Są one wymienione poniżej. Nie martw się, zaraz wyjaśnimy, jak poprawić konfigurację.



![Image](assets/fr/034.webp)



Przyjrzyjmy się bliżej mojej obecnej konfiguracji **SSH** w :**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



Sugerowana poniżej konfiguracja może być jeszcze zoptymalizowana, ale daje dobrą bazę. *Uwaga: usunąłem kilka komentarzy dla większej czytelności*.



Będziemy :





- Zmiana portu połączenia SSH (zapomnij o domyślnym 22)
- Zwiększenie poziomu szczegółowości logów z **INFO do VERBOSE**
- Ustaw **LoginGraceTime** na **2 minuty**



Jeśli w ciągu dwóch minut nie zostaną wprowadzone żadne informacje o połączeniu, połączenie zostanie przerwane.





- Aktywuj **strictModes**



Określa, czy "sshd" powinien sprawdzać tryby i właściciela plików użytkownika, a także katalog domowy użytkownika przed zatwierdzeniem połączenia. Jest to zwykle pożądane, ponieważ czasami nowicjusze przypadkowo pozostawiają swój katalog lub pliki w pełni dostępne dla wszystkich. Domyślnym ustawieniem jest "yes".





- Ustaw **MaxAuthtries** na 3



Reprezentuje liczbę nieudanych prób uwierzytelnienia przed zamknięciem komunikacji.





- Ustaw **MaxSessions** na 2



Jest to maksymalna liczba jednoczesnych sesji.





- Włącz uwierzytelnianie kluczem publicznym



```
PubkeyAuthentication yes
```





- Zachowanie uwierzytelniania hasłem :



```
PasswordAuthentication yes
```



Zakaz pustych haseł i uwierzytelniania **Kerberos**, jak również **bezpośredniego uwierzytelniania roota**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Upewnij się, że masz "**PermitRootLogin no", jeśli jest równe "tak", jest to "absolutne zło "**.





- Zakaz przekierowywania połączeń TCP



```
AllowTcpForwarding no
```



Wskazuje, czy przekierowania TCP są dozwolone, z "tak" jako ustawieniem domyślnym. Uwaga: wyłączenie przekierowań TCP nie zwiększa bezpieczeństwa, jeśli użytkownicy mają dostęp do powłoki, ponieważ nadal mogą skonfigurować własne narzędzia przekierowujące.





- Zakaz przekierowania X11



```
X11Forwarding no
```



Wskazuje, czy przekierowania X11 są akceptowane, z "nie" jako ustawieniem domyślnym. Uwaga: nawet jeśli przekierowania X11 są wyłączone, nie zwiększa to bezpieczeństwa, ponieważ użytkownicy mogą nadal konfigurować własne przekierowania. Przekierowanie X11 jest automatycznie wyłączane, jeśli wybrana jest opcja **UseLogin**.





- Ustawienie limitu czasu komunikacji między klientem a sshd



```
ClientAliveInterval  300
```



Określa limit czasu w sekundach, po którym, jeśli żadne dane nie zostaną odebrane od klienta, usługa sshd wysyła wiadomość z prośbą o odpowiedź od klienta. Domyślnie opcja ta jest ustawiona na "0", co oznacza, że wiadomości te nie są wysyłane do klienta. Tylko wersja 2 protokołu SSH obsługuje tę opcję.



```
ClientAliveCountMax 0
```



Zgodnie z [dokumentacją (*man page*) dla sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html), oto co oznacza ta opcja: "Ustawia liczbę wiadomości wstrzymania (patrz wyżej), które mają zostać wysłane bez odpowiedzi od klienta dla **sshd**. Jeśli ten próg zostanie osiągnięty podczas wysyłania wstrzymanych wiadomości, **sshd** rozłączy klienta i zakończy sesję. Ważne jest, aby pamiętać, że te wiadomości wstrzymujące bardzo różnią się od opcji **KeepAlive** (poniżej). Komunikaty wstrzymania połączenia są wysyłane przez szyfrowany tunel, a zatem nie można ich podrobić. Wstrzymywanie połączenia na poziomie TCP włączone przez **KeepAlive** jest możliwe do podrobienia. Mechanizm utrzymywania połączenia jest interesujący, gdy klient lub serwer musi wiedzieć, czy połączenie jest bezczynne."





- Zapobieganie ujawnianiu informacji poprzez wyłączenie **motd, banner, lastlog**



```
PrintMotd no
```



Określa, czy sshd powinien wyświetlać zawartość pliku "/etc/motd", gdy użytkownik loguje się w trybie interaktywnym. W niektórych systemach zawartość ta może być również wyświetlana przez powłokę, za pośrednictwem pliku /etc/profile lub podobnego pliku. Domyślną wartością jest "yes".



```
Banner none
```



Warto zauważyć, że w niektórych jurysdykcjach wysłanie wiadomości przed uwierzytelnieniem może być warunkiem wstępnym ochrony prawnej. Zawartość określonego pliku jest przesyłana do zdalnego użytkownika przed udzieleniem autoryzacji połączenia. Opcja ta musi zostać skonfigurowana, ponieważ domyślnie nie będzie wyświetlana żadna wiadomość.



W obrazach daje to :



![Image](assets/fr/019.webp)



### D. Wynik audytu



Na koniec nie zapomnijmy sprawdzić **wyniku audytu Lynis**! Widzimy, że **mój wynik Hardening wynosi 63** i że plik raportu można wyświetlić w "**/var/log/lynis-report.dat**". Istnieje również plik "**/var/log/lynis.log**".



**Innymi słowy, im wyższy wynik, tym lepiej! Dlatego należy pracować nad konfiguracją, aby osiągnąć jak najwyższy wynik, jednocześnie umożliwiając normalne działanie maszyny i hostowanych usług (co oznacza przeprowadzanie testów funkcjonalnych).



![Image](assets/fr/046.webp)



Przyjrzyjmy się wynikom na moim drugim serwerze, na którym spędziłem trochę więcej czasu! To normalne, że wynik jest wyższy (**76**).



![Image](assets/fr/045.webp)



## V. Zautomatyzowane planowanie Lynis



**Lynis** oferuje również opcję uruchamiania swoich testów poprzez zaplanowane zadanie. W rzeczywistości istnieje opcja **"--cronjob "**, która uruchomi wszystkie testy Lynis bez potrzeby walidacji lub działania użytkownika. Następnie można w bardzo prosty sposób utworzyć skrypt, który uruchomi **Lynis** i umieści dane wyjściowe w pliku ze znacznikiem czasu z nazwą danego serwera. Oto plik tego typu, który można umieścić w folderze */etc/cron.daily*:



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



Zmienna **"AUDITOR_NAME "** jest po prostu zmienną, którą ustawimy w opcji **"--auditor "** w **Lynis**, aby ta nazwa była wyświetlana w raporcie:



![Image](assets/fr/059.webp)



Utworzymy również kilka zmiennych kontekstowych, które pomogą nam lepiej się zorganizować, takich jak nazwa hosta i data nadania nazwy raportowi i oznaczenia go znacznikiem czasu, a także ścieżka do folderu, w którym chcemy umieścić nasze raporty.



## VI. Wnioski



Lynis to bardzo praktyczne narzędzie, które pomoże ci zaoszczędzić czas i zwiększyć wydajność, gdy chcesz dowiedzieć się więcej o stanie konfiguracji serwera Linux, szczególnie pod względem bezpieczeństwa. Nie należy jednak zapominać, że każda modyfikacja musi zostać przetestowana przed zastosowaniem w produkcji, biorąc pod uwagę własne użycie i kontekst.



Prawdopodobnie nie zastosujesz tej samej konfiguracji dla VPS wystawionego na działanie sieci, gdzie potrzebujesz tylko jednego połączenia SSH (ponieważ jesteś jedyną łączącą się osobą), w przeciwieństwie do **bastionu** lub **schedulera**, które będą wymagały zwielokrotnienia **połączeń SSH**



Gdy masz już konfigurację, która odpowiada Ci pod względem hartowania, zaleca się przyjęcie narzędzia do automatyzacji, abyś nie musiał powtarzać zadań ręcznie, ponieważ byłoby to czasochłonne i podatne na błędy. Na przykład, można użyć **: Puppet, Chef, Ansible, itp...**



Nie zapomnij o komunikacji z zespołami przed wdrożeniem: musisz sprawić, by zrozumieli, dlaczego wprowadzasz te zmiany, a nie tylko powiedzieć im, że je wprowadzasz. Ostatecznie celem będzie przekazanie dobrych praktyk, co zwiększy szanse na sukces.



Wreszcie, można również porównać **Lynis** z innymi narzędziami, których jest kilka. Jeśli chcesz przejść do scentralizowanego zarządzania, pozostając przy otwartym oprogramowaniu, polecam narzędzie [Wazuh] (https://wazuh.com/).



**Tutorial dobiegł końca, miłej zabawy z Lynis!