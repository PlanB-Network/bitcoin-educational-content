---
name: Nmap
description: Master Nmap do mapowania sieci i skanowania luk w zabezpieczeniach
---

![cover](assets/cover.webp)



*Ten samouczek jest oparty na oryginalnej treści Mickaela Dorigny'ego opublikowanej na stronie [IT-Connect](https://www.it-connect.fr/). Licencja [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Wprowadzono zmiany w oryginalnym tekście



___



Witamy w tym samouczku wprowadzającym do Nmap, przeznaczonym dla każdego, kto chce opanować to potężne narzędzie do skanowania sieci. Celem jest dostarczenie podstawowej wiedzy potrzebnej do efektywnego korzystania z Nmap na co dzień.



Nmap to wszechstronne narzędzie, szeroko stosowane przez specjalistów IT, sieci i cyberbezpieczeństwa do diagnostyki, wykrywania sieci i audytu bezpieczeństwa. Ten samouczek jest skierowany do tych, którzy są nowicjuszami w tych dziedzinach i chcą nauczyć się podstaw Nmap. Zalecana jest podstawowa wiedza z zakresu administracji systemem i siecią.



Poznasz podstawy Nmapa, dowiesz się, jak wykonywać skanowanie portów, identyfikować aktywne hosty w sieci, wykrywać wersje usług i systemów operacyjnych, wykonywać skanowanie luk w zabezpieczeniach i wiele więcej. Każda sekcja zawiera szczegółowe wyjaśnienia i praktyczne przykłady, które pomogą ci opanować korzystanie z Nmap w różnych kontekstach.



Pod koniec tego samouczka będziesz miał solidne zrozumienie Nmap i będziesz w stanie skutecznie go używać w celu poprawy bezpieczeństwa i zarządzania sieciami. Miłej lektury.



## 1 - Wprowadzenie do Nmap: Czym jest Nmap?



### I. Prezentacja



W tej pierwszej sekcji przyjrzymy się narzędziu do skanowania sieci Nmap. Przyjrzymy się kluczowym Elements, które musisz wiedzieć o tym narzędziu i jak ogólnie działa. Pomoże nam to lepiej zrozumieć resztę samouczka.



### II. Wprowadzenie do narzędzia Nmap



Nmap, czyli _Network Mapper_, to darmowe narzędzie typu open-source służące do **wykrywania sieci, mapowania i audytu bezpieczeństwa**. Może być również wykorzystywane do innych zadań, takich jak **inwentaryzacja sieci, diagnostyka lub nadzór**.



Może określić, czy hosty w docelowej sieci są aktywne i osiągalne, które usługi sieciowe są narażone, które wersje i technologie są używane oraz inne przydatne informacje analityczne. Nmap może być używany do skanowania pojedynczej usługi na określonej maszynie lub w dużych obszarach sieci, aż do całego Internetu.



Nmap ma wiele mocnych stron:





- Potężny i elastyczny**: Nmap może skanować duże sieci i korzystać z zaawansowanych technik wykrywania. Obsługuje protokoły UDP, TCP, ICMP, IPv4 i IPv6 i może wykonywać wykrywanie wersji, skanowanie luk w zabezpieczeniach lub interakcje specyficzne dla protokołu. Jego architektura jest modułowa, w szczególności dzięki skryptom NSE (Nmap Scripting Engine), którym przyjrzymy się w dalszej części tego samouczka.
- Łatwość użytkowania**: oficjalna dokumentacja jest bogata i najwyższej jakości. Dostępne są również liczne zasoby społecznościowe, które pomogą Ci rozpocząć pracę.
- Popularność i długowieczność**: Nmap jest punktem odniesienia w swojej dziedzinie od 1998 roku. Aktualna wersja, w momencie tej aktualizacji, to 7.95. Chociaż istnieją inne narzędzia do określonych zadań, Nmap pozostaje niezbędnym narzędziem do mapowania i analizy sieci.



**Nmap w kinie**



Nmap jest jednym z niewielu narzędzi bezpieczeństwa, które zyskały pewną sławę wśród ogółu społeczeństwa. Pojawia się w filmie _Matrix Reloaded_, w symbolicznej scenie, w której Trinity używa go do włamania się do systemu:



![nmap-image](assets/fr/01.webp)



matryca: Reloaded z udziałem Nmapa



Pojawia się także w innych filmach.



**Informacje zwrotne



Jako administrator systemu, a następnie audytor cyberbezpieczeństwa i pentester, **używam Nmapa prawie codziennie** i **regularnie polecam** go administratorom systemów, którzy chcą wzmocnić swoją kontrolę nad sieciami i poprawić swoje możliwości diagnostyczne.



### III. Działanie na wysokim poziomie



Nmap jest dostępny dla systemów Linux, Windows i macOS. Jest napisany głównie w językach C, C++ i Lua (dla skryptów NSE). Jest używany głównie w wierszu poleceń, chociaż dostępne są również interfejsy graficzne, takie jak Zenmap. Jednak zdecydowanie zalecamy rozpoczęcie od wiersza poleceń, aby lepiej zrozumieć, jak to działa.



Prosty przykład:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Polecenie to zostanie szczegółowo wyjaśnione później. W tym samouczku będziemy używać Nmap w systemie Linux, ale jego zastosowania są podobne w innych systemach. W systemie Windows Nmap opiera się na bibliotece **Npcap** (zastępującej przestarzałą WinPcap) do przechwytywania i wstrzykiwania pakietów sieciowych.



Nmap jest używany jak konwencjonalny program binarny, taki jak `ls` lub `ip`. Niektóre zaawansowane funkcje mogą wymagać podwyższonych uprawnień, ponieważ narzędzie czasami manipuluje pakietami w niekonwencjonalny sposób, aby sprowokować określone reakcje w systemach docelowych (zwłaszcza w celu wykrywania usług lub luk w zabezpieczeniach).



### IV. Skutki korzystania z Nmap



Przed rozpoczęciem korzystania z Nmapa należy zdawać sobie sprawę z jego potencjalnego wpływu na sieci i systemy:





- Może wysyłać **tysiące, a nawet miliony pakietów** w krótkim czasie, co może nasycić niektóre infrastruktury sieciowe.
- Może generate **zniekształcone lub niestandardowe** pakiety, które mogą zakłócić działanie niektórych urządzeń (zwłaszcza systemów przemysłowych).
- Może generować **zachowanie podobne do ataku**, które może wyzwalać alerty w systemach bezpieczeństwa (zapory ogniowe, IDS/IPS itp.).



Ogólnie rzecz biorąc, **Nmap jest bardzo gadatliwym narzędziem**, ponieważ generuje duży ruch w celu wyodrębnienia jak największej ilości informacji. Dlatego zaleca się pełne zrozumienie jego działania przed użyciem go w środowiskach wrażliwych lub produkcyjnych.



### V. Wnioski



Ta sekcja przedstawia Nmap i jego główne funkcje. Przekonaliśmy się, że jest to podstawowe, potężne i elastyczne narzędzie do mapowania sieci. Omówiliśmy również sposób jego działania i środki ostrożności, które należy podjąć podczas korzystania z niego, aby przygotować scenę dla kolejnych części samouczka.



## 2 - Dlaczego warto używać Nmap?



### I. Prezentacja



W tej sekcji przyjrzymy się głównym zastosowaniom narzędzia do skanowania sieci Nmap. Przekonamy się, że jest to narzędzie szeroko stosowane w wielu kontekstach i zawodach, a posiadanie go w swoim zestawie narzędzi i umiejętność jego opanowania jest zdecydowanie przydatną umiejętnością.



### II. Używanie Nmap do diagnostyki i nadzoru



Nmap może być używany do diagnostyki sieci i, szerzej, do monitorowania. W ten sam sposób, w jaki ping może być użyty do określenia, czy dwa hosty się komunikują, Nmap może być użyty do szybkiego określenia, czy host jest aktywny lub czy dana usługa działa. Dzięki [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap") możemy uzyskać dokładne dane dotyczące czasu odpowiedzi hosta, trasy przebytej przez pakiety, odpowiedzi wykonanej przez określoną usługę itp.



Poniższe polecenie i wynik mogą być użyte na przykład do szybkiego sprawdzenia, czy serwer WWW na hoście **192.168.1.18** jest aktywny i odpowiada poprawnie:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Użyj Nmap, aby pobrać status usługi internetowej ze zdalnego serwera.*



Tak więc korzystanie z Nmapa wykracza poza słynny "test ping" podczas debugowania lub faz diagnostycznych. Zobaczymy później, że istnieje kilka metod używanych przez Nmap do identyfikacji usługi nasłuchującej na danym porcie, w tym jej wersji.



### III. Używanie Nmap do mapowania sieci



Jako _Network Mapper_, mapowanie sieci jest głównym celem tego narzędzia. Może być używany w sieci lokalnej lub w wielu sieciach, podsieciach i sieciach VLAN, aby wyświetlić listę wszystkich osiągalnych hostów i usług. Nmap sprawia, że zadanie to jest znacznie szybsze i bardziej wydajne niż jakakolwiek metoda ręczna.



Na przykład, poniższe polecenie może być użyte do szybkiej identyfikacji aktywnych hostów w sieci **192.168.1.0/24**:



```
nmap -sn 192.168.1.0/24
```



*Uwaga: opcja `-sP` jest przestarzała i została zastąpiona przez `-sn`.*



![nmap-image](assets/fr/03.webp)



*Używanie Nmap do wykrywania osiągalnych hostów w sieci*



Zobaczymy później, że istnieje kilka metod używanych przez Nmap do określenia, czy host można uznać za "aktywny", nawet jeśli a priori nie udostępnia żadnych usług.



### IV. Używanie Nmap do oceny polityki filtrowania



Nmap ma tę zaletę, że jest oparty na faktach: jego wyniki umożliwiają ustalenie konkretnych ustaleń, w przeciwieństwie do jakiegokolwiek dokumentu architektury lub polityki filtrowania. Jest to kluczowe narzędzie do oceny skuteczności podziału systemu informatycznego, ponieważ pozwala **zweryfikować, czy polityka filtrowania jest faktycznie stosowana**.



W sieci korporacyjnej najlepsze praktyki nakazują segmentację systemów zgodnie z ich rolą, krytycznością lub lokalizacją. Reguły filtrowania (często wdrażane przez zapory sieciowe) muszą ograniczać komunikację między strefami. Konfiguracje te są jednak często złożone i podatne na błędy.



Tak więc, aby zweryfikować, czy polityka jest przestrzegana, nie ma nic lepszego niż konkretny test. Na przykład można sprawdzić, czy wrażliwe usługi administracyjne (SSH, WinRM, MSSQL, MySQL itp.) nie są dostępne ze strefy użytkownika.



Użycie **Nmap do testowania polityki filtrowania** powinno być systematyczne przed wprowadzeniem takiej polityki do produkcji. Niestety, kontrola ta jest często zaniedbywana.



Z mojego doświadczenia wynika, że wiele błędów konfiguracji pozostaje niezauważonych w przypadku braku testów walidacyjnych. Prosty błąd w zakresie adresów IP lub niedopatrzenie reguły może sprawić, że rzekomo odizolowana strefa będzie podatna na ataki.



### V. Wykorzystanie Nmap do audytu bezpieczeństwa i testów penetracyjnych



Nmap ma **wiele przydatnych funkcji do oceny bezpieczeństwa**, testów penetracyjnych (pentesty) i niestety także dla atakujących.



Funkcje wykrywania sieci są kluczowe dla atakującego, który musi zrozumieć topologię sieci po początkowej kompromitacji. Nmap oferuje jednak znacznie więcej: integruje silnik skryptów, z których **wiele jest dedykowanych wykrywaniu luk w zabezpieczeniach**.



Na przykład, polecenie to może być użyte do sprawdzenia, czy usługa FTP zezwala na anonimowe połączenie, bez konieczności łączenia się ręcznie:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Używanie skryptu NSE do sprawdzania anonimowego uwierzytelniania FTP przez Nmap.*



Wykrywanie podatności Nmap jest jednym z pierwszych kroków w audycie lub teście penetracyjnym. Pozwala szybko zidentyfikować pewne słabe punkty i zoptymalizować wysiłki związane z analizą.



Ale uwaga: **narzędzia do skanowania podatności mają swoje ograniczenia**. Nmap obejmuje tylko ułamek zagrożeń i nie gwarantuje, że system jest bezpieczny, jeśli nie zostaną wykryte żadne problemy. Dlatego ważne jest, aby **zrozumieć, jak działają używane skrypty** i nie polegać wyłącznie na ich werdykcie.



### VI. Wnioski



Przekonaliśmy się, że opanowanie Nmap może obejmować szeroki zakres przypadków użycia, od diagnostyki i monitorowania po mapowanie, ocenę polityki bezpieczeństwa i skanowanie luk w zabezpieczeniach. W następnej sekcji przejdziemy do szczegółów i zainstalujemy Nmap.




## 3 - Instalacja i konfiguracja Nmap



### I. Prezentacja



W tej sekcji dowiemy się, jak zainstalować narzędzie do skanowania sieci Nmap w systemach operacyjnych Linux i Windows. Pod koniec tej sekcji będziemy mieli wszystko, czego potrzebujemy, aby rozpocząć korzystanie z Nmap dla przyszłych modułów. Wreszcie, zobaczymy, jakich uprawnień może wymagać, gdy jest używany i dlaczego.



### II. Instalacja Nmap w systemie Linux



Nmap został pierwotnie zaprojektowany do pracy w systemach operacyjnych GNU/Linux. W rezultacie, dzięki swojej długowieczności i popularności, można go znaleźć we wszystkich oficjalnych repozytoriach głównych dystrybucji systemu Unix. W tym poradniku będę używał systemu operacyjnego opartego na Debianie [Kali Linux] (https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Ale możesz go używać w dokładnie taki sam sposób z klasycznego Debiana, CentOS, Red Hat lub czegokolwiek innego!



Pod Debianem, aby sprawdzić, czy Nmap jest obecny w bieżących repozytoriach, można użyć następującego polecenia:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



Odpowiedź tutaj wyraźnie wskazuje, że pakiet "nmap" istnieje w repozytoriach (tutaj tych z Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). Od tej chwili można zainstalować Nmap za pomocą zwykłych poleceń instalacyjnych, na razie nic nie rozbraja 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



Aby sprawdzić, czy Nmap jest poprawnie zainstalowany, wyświetlimy jego wersję:



```
nmap --version
```



Oto oczekiwany wynik:



![nmap-image](assets/fr/05.webp)



wynik wyświetlenia aktualnej wersji Nmap._



Zwróć uwagę na obecność w tym oknie biblioteki "libpcap" (_Packet Capture Library_) i jej wersji. Używana również przez Wireshark, "libpcap" jest używana przez Nmap do tworzenia i manipulowania pakietami oraz nasłuchiwania ruchu sieciowego.



### III Instalacja Nmap w systemie Windows



Instalację w systemie operacyjnym Windows należy rozpocząć od pobrania pliku binarnego z oficjalnej strony (i żadnej innej!):





- Strona pobierania Nmap na oficjalnej stronie internetowej: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




Następnie należy pobrać plik binarny o nazwie `nmap-<VERSION>-setup.exe`:



![nmap-image](assets/fr/06.webp)



strona pobierania binarnych plików instalacyjnych nmap dla systemu Windows



Gdy masz już ten plik binarny w systemie, po prostu uruchom go, aby zainstalować Nmap. Jest to prosta instalacja, a wszystkie opcje można pozostawić jako domyślne.



Moim odruchem jest odznaczenie pola "zenmap (GUI Frontend)". Jest to graficzny Interface dla Nmapa, którego nie używam i nie będzie opisany w tym samouczku, ale możesz go wypróbować po opanowaniu narzędzia wiersza poleceń Nmap!



![nmap-image](assets/fr/07.webp)



opcjonalne odznaczenie Zenmap podczas instalacji Nmap w systemie Windows



Pod koniec instalacji Nmap proponowana jest druga instalacja: biblioteki "Npcap":



![nmap-image](assets/fr/08.webp)



instalacja biblioteki "Npcap" podczas instalacji Nmap w systemie Windows



Jest to biblioteka, na której opiera się Nmap do zarządzania komunikacją sieciową, tj. tworzenia, wysyłania i odbierania pakietów sieciowych. Prawdopodobnie zetknąłeś się już z tą biblioteką, jeśli używasz Wiresharka w systemie Windows, ponieważ on również z niej korzysta i wymaga instalacji.



Podobnie jak w przypadku systemu Linux, można sprawdzić, czy Nmap jest zainstalowany, otwierając wiersz polecenia lub terminal [Powershell] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") i wpisując następujące polecenie:



```
nmap --version
```



Oto oczekiwany wynik:



![nmap-image](assets/fr/09.webp)



wynik wyświetlenia aktualnej wersji Nmap._



Nmap jest teraz zainstalowany w systemie Windows. Można go używać w dokładnie taki sam sposób, jak w systemie Linux, postępując zgodnie z tym samouczkiem.



### IV. Lokalne uprawnienia wymagane do korzystania z Nmap



Ale przy okazji, podczas korzystania z Nmap, **czy konieczne jest posiadanie podwyższonych uprawnień lokalnych w systemie**? **to zależy**.



W swojej podstawowej formie, tj. bez zagłębiania się w jego opcje, Nmap niekoniecznie wymaga uprawnień uprzywilejowanych. Jednak wkrótce zdasz sobie sprawę, że lepiej jest używać Nmapa w kontekście uprzywilejowanym ("root" w systemie Linux, "administrator" lub odpowiednik w systemie Windows), aby móc w pełni wykorzystać jego potencjał, ryzykując otrzymanie komunikatu o błędzie, takiego jak ten:



![nmap-image](assets/fr/10.webp)



komunikat o błędzie w systemie Linux, gdy opcje Nmap wymagają praw roota



Zarówno w systemie Linux, jak i Windows, istnieje wiele przypadków, w których Nmap poprosi o dostęp uprzywilejowany. Główne powody są następujące (niewyczerpująca lista):





- Konstruowanie "surowych" pakietów sieciowych**: Nmap jest zdolny do szerokiego zakresu metod skanowania, w tym zaawansowanej manipulacji i konstrukcji pakietów. Dzieje się tak na przykład, gdy chcemy wykonać skanowanie TCP SYN, które nie respektuje klasycznego _Three-way handshake_ wymiany TCP. Aby to zrobić, Nmap musi użyć funkcji innych niż te natywne dla systemów operacyjnych, które wiedzą tylko, jak przestrzegać dobrych praktyk w komunikacji sieciowej (wywołuje biblioteki "Npcap" i "libcap" widoczne powyżej). To właśnie dlatego, że Nmap nie robi rzeczy w "standardowy" sposób, jest w stanie wywnioskować pewne informacje o systemach operacyjnych, usługach i niektórych podatnościach.





- Nasłuchiwanie ruchu sieciowego**: niektóre opcje Nmapa wymagają nasłuchiwania sieci w celu uzyskania określonych informacji. Ta czynność jest uważana za wrażliwą w systemach operacyjnych, ponieważ pozwala również na podsłuchiwanie komunikacji innych aplikacji w systemie. Podobnie jak Wireshark, Nmap potrzebuje do tego określonych uprawnień, które łatwiej uzyskać będąc bezpośrednio w sesji uprzywilejowanej.





- Nasłuchiwanie na portach uprzywilejowanych**: w systemach operacyjnych porty od 0 do 1024 (zarówno TCP, jak i UDP) są uważane za uprzywilejowane, tj. są w jakiś sposób zarezerwowane dla bardzo konkretnych zastosowań i dlatego są chronione. Chociaż jest to obecnie nieco przestarzały powód, nadal konieczne jest posiadanie pewnych uprawnień do nasłuchiwania na tych portach, co Nmap może być zmuszony zrobić w zależności od tego, jak będzie używany.





- Wysyłanie pakietów UDP:** Podobnie, nasłuchiwanie aplikacji sieciowej na portach UDP (protokół bezstanowy) wymaga uprawnień uprzywilejowanych w systemach operacyjnych. Uprzywilejowana sesja będzie zatem wymagana, jeśli chcesz wykonać skanowanie UDP, dla którego Nmap będzie musiał nasłuchiwać odpowiedzi, aby przeanalizować odpowiedzi na swoje skany.




Mówiąc dokładniej, możliwe jest, przynajmniej pod Linuksem, uruchomienie Nmapa ze wszystkimi jego funkcjami i opcjami bez bycia rootem. Osiąga się to poprzez przyznanie odpowiednich _możliwości_ plikowi binarnemu. Wymaga to jednak zaawansowanej manipulacji i może nie być tak praktyczne, jak uruchomienie Nmapa bezpośrednio z uprawnieniami. Ponadto, to podejście jest mniej powszechne i może stwarzać problemy z bezpieczeństwem, jeśli zostanie źle skonfigurowane.



Jest to jednak trochę odejście od naszego samouczka Nmap, więc na razie z niego zrezygnujemy.



W pozostałej części tego samouczka należy założyć, że Nmap jest zawsze uruchamiany jako "root" (z powłoki jako "root" lub za pomocą polecenia "sudo") lub w terminalu administratora w systemie Windows, nawet jeśli nie jest to wskazane. W przeciwnym razie mogą wystąpić subtelne, ale zauważalne różnice w stosunku do samouczka.



### V. Wnioski



To wszystko! Nmap jest teraz zainstalowany w naszym systemie operacyjnym i gotowy do użycia, nie wymagając dalszej konfiguracji. Ta sekcja kończy wprowadzenie i prezentację Nmap. Mam nadzieję, że sprawiło to, że nabrałeś ochoty na rozpoczęcie ćwiczeń.



Mówiąc bardziej poważnie, mamy teraz lepsze pojęcie o tym, czym jest narzędzie do mapowania Nmap i jakie są jego najczęstsze zastosowania, a także jego ograniczenia. Przejdźmy dalej!




## 4 - Skanowanie portów TCP i UDP za pomocą Nmap



### I. Prezentacja



W tej sekcji dowiemy się, jak wykonać nasze pierwsze skanowanie portów za pomocą narzędzia do skanowania sieci Nmap. Zobaczymy, jak użyć go do skompilowania listy usług sieciowych ujawnionych na hoście, zarówno przy użyciu protokołów TCP, jak i UDP.



Od teraz pamiętaj, aby skanować tylko hosty w kontrolowanym środowisku, do których masz wyraźną autoryzację.





- Dla przypomnienia: [Kodeks karny: Rozdział III: Ataki na systemy automatycznego przetwarzania danych](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Jeśli nie masz go pod ręką**, polecam poniższe darmowe rozwiązania, które są w sam raz!





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")**: Platforma szkoleniowa dla hakerów, Hack The Box stale udostępnia podatne na ataki systemy. Dostępnych jest kilkaset systemów, ale odnowiona pula 20 maszyn jest oferowana bezpłatnie przez cały rok, z dostępem przez OpenVPN VPN.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")**: Platforma ta oferuje wiele celowo podatnych na ataki systemów do pobrania, z których można korzystać za pośrednictwem VirtualBox (również darmowe rozwiązanie) lub w inny sposób. Po pobraniu nie ma potrzeby korzystania z VPN - wszystko odbywa się lokalnie.




Możesz także **utworzyć maszynę wirtualną** w swoim ulubionym systemie operacyjnym i zainstalować na niej różne usługi jako cele testowe. Zaletą będzie to, że będziesz mógł również zobaczyć, co dzieje się po stronie serwera podczas skanowania, zwłaszcza za pomocą Wiresharka, i mieć wpływ na lokalną zaporę ogniową, gdy będziemy przeprowadzać bardziej zaawansowane testy.



Bądźmy praktyczni!



### II. Skanowanie portów TCP hosta za pomocą Nmap



#### A. Pierwsze skanowanie portów TCP za pomocą Nmap



Teraz wykonamy nasze pierwsze skanowanie za pomocą Nmap. Nasz cel jest prosty: chcemy dowiedzieć się, jakie usługi są ujawniane przez serwer WWW, który właśnie wdrożyliśmy, aby sprawdzić, czy jest coś nieoczekiwanego, takiego jak usługa administracyjna, która nie powinna być dostępna, lub ujawnienie portu aplikacji, o której myśleliśmy, że została wycofana.



W moim przykładzie skanowany host ma adres IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



Oto możliwy wynik. Widzimy klasyczny Nmap z dużą ilością informacji:



![nmap-image](assets/fr/11.webp)



wyniki prostego skanowania TCP wykonanego za pomocą Nmap._



Patrząc na ten wynik, rozumiemy, że porty TCP/22 i TCP/80 są dostępne na tym hoście.



Domyślnie i jeśli tego nie zrobisz, Nmap będzie skanował tylko porty TCP.



#### B. Zrozumienie wyników prostego skanowania Nmap



Pójdźmy jednak o krok dalej, aby zrozumieć te dane wyjściowe: każda linia jest ważna, po pierwsze, aby wiedzieć, co właśnie zostało zrobione, a po drugie, aby właściwie zinterpretować same wyniki skanowania.



Pierwszy wiersz jest zasadniczo przypomnieniem wersji i daty skanowania (przydatne do rejestrowania i archiwizacji!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



Drugi wiersz pokazuje początek wyników skanowania dla hosta "debian.home (192.168.1.19)". Informacje te będą przydatne, gdy rozpoczniemy skanowanie kilku hostów jednocześnie:



```
Nmap scan report for debian.home (192.168.1.19)
```



Trzeci wiersz mówi nam, że dany host jest "Up", czyli aktywny:



```
Host is up (0.00022s latency).
```



Wreszcie, Nmap informuje nas, że 998 portów TCP zidentyfikowanych jako zamknięte nie jest wyświetlanych w:



```
Not shown: 998 closed tcp ports (conn-refused)
```



Oszczędza nam to prawie 1000 wierszy danych wyjściowych wyglądających jak:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Dziękujemy mu za oszczędzenie nam tego!



Dlaczego 998 "zamkniętych" portów? Dodanie 2 otwartych portów daje 1000, a to jest liczba portów, które Nmap przeskanuje w domyślnej konfiguracji, a nie 65535 istniejących portów TCP! Zobaczymy później, że jest to całkowicie i łatwo konfigurowalne. Ale jeśli docelowy host ma usługę nasłuchującą na dość egzotycznym porcie, to "domyślne" skanowanie jej nie wykryje.



Po tych informacjach znajdujemy to, co najbardziej interesujące: tabelę zorganizowaną według trzech kolumn "PORT - STATE - SERVICE":





- Pierwsza kolumna "PORT" wskazuje po prostu docelowy port/protokół i ważne jest, aby sprawdzić, czy jest to port TCP (`<port>/tcp`) czy UDP (`<port>/udp`).





- Kolumna "STATE" wskazuje status usługi sieciowej wykrytej na tym porcie i określonej przez Nmap na podstawie uzyskanej odpowiedzi. Może to być "otwarty", "zamknięty", "filtrowany" lub "nieznany". Zobaczymy później, jak Nmap rozróżnia te różne stany.





- Kolumna "SERVICE" wskazuje usługę dostępną na danym porcie. Należy jednak pamiętać, że nie użyliśmy tutaj opcji aktywnego wykrywania usług. Nmap opiera się na lokalnym odniesieniu między portem/protokołem a rzekomo przypisaną usługą: plik "/etc/services"




Jeśli spojrzysz na plik "/etc/services" w systemie Linux, znajdziesz link "port/protokół - usługa" podobny do tego wyświetlanego przez Nmap:



![nmap-image](assets/fr/12.webp)



wyodrębnia zawartość pliku "/etc/services" w systemie Linux



Ważne jest, aby zrozumieć, że na razie Nmap nie przeprowadził żadnego aktywnego wykrywania usług. Na przykład, nie byłby w stanie zidentyfikować usługi SSH za portem TCP/80, gdyby tak było. Dlatego tak ważne jest, aby wiedzieć, jak korzystać z odpowiednich opcji - już wkrótce!



Wiedza o tym, jak interpretować dane wyjściowe Nmapa jest ważną częścią opanowania tego narzędzia. Dobrą wiadomością jest to, że dane wyjściowe będą w dużej mierze takie same, niezależnie od użytych opcji.



#### C. Pod maską: analiza sieci za pomocą Wireshark



Jeśli dokładnie przyjrzymy się temu, co dzieje się w sieci Interface hosta skanującego serwer lub na samym serwerze, działania Nmapa będą znacznie jaśniejsze. To właśnie zamierzamy tutaj zrobić.



To, co mogę tutaj pokazać, to tylko część tego, co jest widoczne w Wireshark. Jeśli chcesz dowiedzieć się więcej, możesz samodzielnie wykonać przechwytywanie sieci podczas skanowania, a następnie przejrzeć to, co zostało przechwycone.



W tym teście mój host skanowania (192.168.1.18) i host docelowy (192.168.1.19) znajdują się w tej samej sieci lokalnej.



Nmap rozpoczyna od sprawdzenia, czy host docelowy jest aktywny w sieci lokalnej, wysyłając żądanie ARP. Jeśli otrzyma odpowiedź, wie, że host jest aktywny i rozpoczyna skanowanie sieci:



![nmap-image](assets/fr/13.webp)



żądanie ARP wydane przez Nmap w celu ustalenia, czy host docelowy jest obecny w sieci lokalnej



Jeśli host do przeskanowania znajduje się w sieci zdalnej, Nmap rozpoczyna od wysłania żądania ping i próbuje uzyskać dostęp do niektórych z najczęściej eksponowanych portów (TCP/80, TCP/443):



![nmap-image](assets/fr/14.webp)



żądanie ping wydane przez Nmap w celu ustalenia, czy host docelowy jest osiągalny w sieci zdalnej



Jeśli uzyska odpowiedź na którykolwiek z tych testów, uznaje cel za aktywny.



Gdy Nmap ustali, że cel jest aktywny, spróbuje rozwiązać jego nazwę domeny za pomocą serwera DNS skonfigurowanego na karcie sieciowej:



![nmap-image](assets/fr/15.webp)



rozdzielczość dNS na celu skanowania Nmap



Teraz, gdy Nmap zidentyfikował swój cel i wie, że jest on aktywny, rozpoczyna skanowanie portu TCP:



![nmap-image](assets/fr/16.webp)



transmisja pakietu tCP SYN i odbiór RST/ACK podczas skanowania Nmap



Aby to zrobić, na każdym porcie TCP w domyślnym zakresie **wysyła pakiety TCP SYN i czeka na odpowiedź**. Na powyższym zrzucie ekranu otrzymuje pakiety TCP RST/ACK od skanowanego serwera, co oznacza "ruszaj się, nie ma tu nic do oglądania" - innymi słowy, te porty są zamknięte. Jak widzieliśmy w wynikach, będzie tak w przypadku większości skanowanych portów. Z dwoma wyjątkami:



![nmap-image](assets/fr/17.webp)



odpowiedź na pakiet TCP SYN wysłany na port 22, aktywny na celu skanowania



Na powyższym zrzucie ekranu widzimy pakiet TCP SYN/ACK wysłany przez host docelowy**. Port jest aktywny i udostępnia usługę. Nmap potwierdza otrzymanie odpowiedzi, a następnie kończy połączenie (TCP RST/ACK). **W ten sposób wiadomo, że port TCP/22 był aktywny**.



Widzieliśmy tutaj, że Nmap respektuje "Three Way Handshake" podczas skanowania sieci TCP. Ze względów wydajnościowych można poprosić go, aby nie odpowiadał na zwrot serwera, oszczędzając w ten sposób kilka tysięcy pakietów podczas skanowania dużej sieci. Ale przyjrzymy się tym opcjom i optymalizacjom w dalszej części samouczka.



Mamy teraz lepsze wyobrażenie o tym, jak wykonać skanowanie TCP i co faktycznie dzieje się podczas jego wykonywania. Zauważyliśmy również, że domyślnie Nmap wykonuje skanowanie portów TCP na ograniczonej liczbie portów.



### III. Skanowanie portów UDP za pomocą Nmap



#### A. Pierwsze skanowanie portu UDP za pomocą Nmap



Zobaczmy teraz, jak przeskanować porty UDP hosta. Jak widzieliśmy, domyślnie Nmap zawsze skanuje porty TCP. Może to oznaczać utratę wielu informacji, jeśli nie jesteśmy tego świadomi.



Dla przypomnienia, na potrzeby tego testu mój host skanowania (192.168.1.18) i host docelowy (192.168.1.19) znajdują się w tej samej sieci lokalnej.



```
nmap -sU 192.168.1.19
```



Tutaj otrzymany wynik ma taki sam format jak w przypadku skanowania TCP, ale wyświetlane aktywne usługi są w formacie `<port>/UDP`, zgodnie z żądaniem!



![nmap-image](assets/fr/18.webp)



wynik prostego skanowania UDP wykonanego za pomocą Nmap._



Opcja "-sU" służy do poinformowania Nmap, że chcesz pracować na UDP, a nie TCP, jak jest domyślnie.



Przy okazji, prawdopodobnie zauważyłeś, że Nmap wymaga uprawnień "root" do skanowania UDP, jak wspomniano wcześniej w samouczku.



uwaga: Od najnowszych wersji Nmapa zawsze zaleca się uruchamianie skanowania UDP z uprawnieniami administratora, aby zapewnić wiarygodne wyniki, ponieważ niektóre funkcje wymagają nieprzetworzonego dostępu do gniazd sieciowych



Skanowanie UDP może trwać bardzo długo (1100 sekund na przeskanowanie 1000 portów w moim przykładzie), ze względu na brak "Three Way Handshake" w UDP, co oznacza, że Nmap będzie czekał na odpowiedź dla każdego wysłanego pakietu UDP i określi port jako "zamknięty" tylko wtedy, gdy nie będzie odpowiedzi po określonym czasie (timeout). Ta odpowiedź od skanowanych hostów nie jest systematyczna i często jest ograniczona pod względem liczby odpowiedzi na sekundę, aby uniknąć pewnych ataków wzmacniających. Jest to przeciwieństwo TCP, gdzie istnieje natychmiastowa odpowiedź od skanowanego hosta, niezależnie od tego, czy port jest otwarty czy zamknięty. Zobaczymy później, jak to zoptymalizować.



Drugą trudnością związaną z UDP jest **to, że usługi nie zawsze odpowiadają na przychodzące pakiety**, po prostu dlatego, że nie zawsze jest to konieczne i jest to zasada UDP. W takim przypadku, gdy nie zostanie odebrany żaden komunikat ICMP "port unreachable", usługa zostanie oznaczona przez Nmap jako "open|filtered", jak pokazano na powyższym zrzucie ekranu.



#### B. Pod maską: analiza sieci za pomocą Wireshark



Podobnie jak w przypadku skanowania TCP, przyjrzyjmy się bliżej temu, co dzieje się na poziomie sieci podczas skanowania UDP przy użyciu analizy Wireshark. Zachowanie Nmapa podczas określania, czy host jest aktywny jest takie samo.



Jedyną prawdziwą różnicą podczas skanowania UDP jest to, że Nmap nie będzie czekał na "Three Way Handshake", ponieważ mechanizm ten nie istnieje w UDP (protokół bezstanowy):



![nmap-image](assets/fr/19.webp)



transmisja pakietów uDP i odbiór ICMP (port nieosiągalny) podczas skanowania Nmap



Na powyższym zrzucie ekranu widzimy, że Nmap wysyła dużą liczbę pakietów UDP, a w odpowiedzi na większość z nich otrzymuje pakiet ICMP "Destination unreachable (Port unreachable)". Jest to normalne, ponieważ jest to odpowiednia odpowiedź zdefiniowana przez [RFC 1122] (https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122"), gdy port UDP jest nieosiągalny:



![nmap-image](assets/fr/20.webp)



wyciąg z RFC 1122._



Przyjrzyjmy się bliżej temu przechwyceniu Wireshark, które pokazuje **trzy możliwe scenariusze** w UDP:



![nmap-image](assets/fr/21.webp)



przechwytywanie sieci podczas skanowania UDP na różnych portach za pomocą Nmap._



Te trzy przypadki są następujące:





- Pierwszy Exchange składa się z pakietów nr. 3, 4 i 8, 9. Nmap wysyła pakiety UDP na klasycznym porcie SNMP i dlatego **konstruuje pakiety zgodne z protokołem z wyprzedzeniem**. Następnie otrzymuje odpowiedź od serwera (pakiety nr 8 i 9). Wynik: Nmap otrzymał odpowiedź, usługa jest "otwarta".





- Drugi Exchange składa się z pakietów 6 i 7. Nmap wysyła "pusty" pakiet UDP (bez struktury protokołu) na port UDP/165 i otrzymuje w odpowiedzi pakiet ICMP: "Destination unreachable (Port nieosiągalny)". Wynik: Nmap otrzymał (negatywną) odpowiedź, host działa, ale usługa, z którą próbował się połączyć, nie działa na tym porcie, który zostanie oznaczony jako "zamknięty".





- Ostatni Exchange składa się z pakietu nr 12: Nmap wysyła "pusty" pakiet UDP na port UDP/1235. Nie ma żadnej odpowiedzi, nawet wyraźnej odmowy ze strony skanowanego hosta. Wynik: Nmap oznacza port jako "open|filtered", ponieważ nie jest w stanie stwierdzić, czy jest to spowodowane obecnością firewalla, skonfigurowanego tak, aby nie odpowiadał, czy też aktywną usługą UDP, która i tak nie zwraca odpowiedzi (nie jest to obowiązkowe w UDP).




Oto wynik wyświetlony przez Nmap po tych trzech przypadkach:



![nmap-image](assets/fr/22.webp)



możliwe wyniki skanowania UDP wykonanego przez Nmap._



Mamy teraz lepsze pojęcie o tym, jak wykonać skanowanie UDP i co właściwie dzieje się podczas jego wykonywania. Do tej pory używaliśmy Nmapa w bardzo prosty sposób, nie decydując tak naprawdę, które porty skanować, ale to się wkrótce zmieni!



### IV. Dostrajanie skanowania portów za pomocą Nmap



#### A. Przypomnienie domyślnego zachowania Nmapa



Jak widzieliśmy, Nmap sam wybiera numer i porty do skanowania, jeśli nie określisz żadnych opcji. Jest to "domyślna" konfiguracja używana przez Nmap, gdy nie powiemy mu dokładnie, co ma robić. Te domyślne opcje zostały zaprojektowane, aby dać wyobrażenie o głównych odsłoniętych portach, które są wybierane według częstotliwości ekspozycji (najczęstsze lub częste porty), a nie w kolejności numerycznej (port 1, 2, 3 itd.), A także w celu uniknięcia rozpoczęcia skanowania 65535 możliwych portów, jeśli nie określisz odpowiednich opcji, które byłyby zbyt długie i skomplikowane dla "domyślnego" przypadku użycia.



**Jak wybierane są te porty?



1000 portów skanowanych w trybie domyślnym jest wybieranych zgodnie z częstotliwością ich występowania. Statystyki te są utrzymywane przez Nmap i aktualizowane w taki sam sposób, jak sam plik binarny i jego skrypty (moduły). Statystyki te można przeglądać samodzielnie w pliku "/usr/shares/nmap/nmap-services":



![nmap-image](assets/fr/23.webp)



wyodrębniony z pliku "/usr/shares/nmap/nmap-services"._



Tutaj, w trzeciej kolumnie, widzimy coś, co wygląda jak prawdopodobieństwo (między 0 a 1) lub rozkład procentowy. Jest to częstotliwość występowania każdej pary port/protokół. Widzimy, że najbardziej znane porty (FTP, SSH, TELNET i SMTP w tym fragmencie) mają znacznie wyższą wartość niż pozostałe.



#### B. Precyzyjne określenie portów docelowych dla skanowania Nmap



Jednak w prawdziwym świecie możemy potrzebować przeskanować tylko określony port, kilka portów lub określony zakres portów. Nmap sprawia, że łatwo jest to zrobić, w jednolity sposób zarówno dla skanowania UDP, jak i TCP.



**Skanowanie określonego portu przez Nmap**



Jeśli chcemy przeskanować pojedynczy port, a nie 1000, możemy określić ten port za pomocą opcji Nmap "-p" lub "--port":



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



W rezultacie skanowanie będzie oczywiście znacznie szybsze, a Nmap wyemituje tylko pakiety potrzebne do wykrycia, czy host jest aktywny, a następnie czy określony port jest osiągalny. Oszczędza to czas, jeśli chcesz po prostu przeprowadzić szybki test, aby sprawdzić, czy usługa internetowa w witrynie pokazowej nadal działa.



**Skanowanie wielu portów przez Nmap**



W ten sam sposób możemy określić kilka portów dla Nmap, używając tej samej opcji i łącząc określone porty przecinkiem:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Niezależnie od kolejności, Nmap sprawdzi wszystkie te porty i tylko te na docelowym hoście. Zauważysz, że dane wyjściowe Nmapa **wyraźnie informują nas o wszystkich portach i ich statusie**, nawet jeśli są "zamknięte". W przeciwieństwie do domyślnego zachowania, w którym te pełne dane wyjściowe zajęłyby zbyt dużo miejsca:



![nmap-image](assets/fr/24.webp)



*Wynik skanowania Nmap TCP na wskazanych portach.*



**Skanowanie szeregu portów



Jeśli liczba portów do przeskanowania jest zbyt duża, można określić je według zakresu, na przykład:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Oczywiście można je dowolnie łączyć i dopasowywać:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**Skanowanie portów TCP i UDP



Możliwe jest także jednoczesne skanowanie UDP i TCP na wybranych portach:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



W tym ostatnim przykładzie można zauważyć obecność "U:" oznaczającego port UDP i "T:" oznaczającego port TCP. Oto możliwy wynik tego typu skanowania:



![nmap-image](assets/fr/25.webp)



*Wynik skanowania portów TCP i UDP za pomocą Nmap.*



To ciekawy sposób na personalizację skanów!



**Skanowanie wszystkich portów



Wreszcie, możliwe jest określenie znacznie większych lub mniejszych zakresów dla Nmapa. Widzieliśmy, że domyślna lista wybrana przez Nmap zawiera 1000 portów. Możemy również poprosić o 100 najczęściej występujących portów lub 200, używając opcji "--top-ports":



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Na koniec możemy poprosić o przeskanowanie wszystkich możliwych portów (wszystkie 65535), używając notacji "-p-":



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



To drugie potrwa dłużej, zwłaszcza w przypadku UDP, ale na pewno nie pominiesz żadnych otwartych portów.



*Uwaga: Opcja "-p-" jest zalecaną metodą skanowania wszystkich portów TCP. W przypadku skanowania UDP zaleca się ograniczenie liczby portów ze względu na wydajność, ponieważ pełne skanowanie wszystkich portów UDP może zająć bardzo dużo czasu



W dalszej części samouczka zobaczymy, jak zoptymalizować szybkość skanowania Nmap do naszych potrzeb, co będzie szczególnie przydatne w przypadku skanowania na wszystkich portach TCP i UDP.



### V. Wnioski



W tej sekcji w końcu zdobyliśmy trochę praktycznej praktyki, dzięki czemu wiemy już **jak używać Nmapa w podstawowy sposób do skanowania portów TCP i UDP hosta**. Przyjrzeliśmy się również szczegółowo temu, co dzieje się na poziomie sieci i **jak Nmap określa, czy port TCP lub UDP jest aktywny, czy nie**. Wreszcie, wiemy jak precyzyjnie wybrać porty, które chcemy przeskanować i **co tak naprawdę robią domyślne opcje Nmapa**. W dalszej części wykorzystamy tę wiedzę i zastosujemy ją do skanowania całej sieci, w tym globalnego mapowania i wykrywania sieci.




## 5 - Mapowanie i wykrywanie sieci za pomocą Nmap



### I. Prezentacja



W tej sekcji dowiemy się, jak używać narzędzia do skanowania sieci Nmap do mapowania sieci. Zobaczymy, jak skuteczne może być to zadanie, dzięki różnym opcjom. Na koniec przyjrzymy się różnym sposobom określania celów naszego skanowania do Nmap.



W szczególności wykorzystamy to, czego nauczyliśmy się w poprzedniej sekcji o tym, jak Nmap określa, czy host jest aktywny i osiągalny.



Jak wspomniano we wstępie do Nmap, jest to Network Mapper. W związku z tym jest to idealne narzędzie do sporządzania listy dostępnych hostów w sieci, zarówno lokalnej, jak i zdalnej.



**Powrót autora:**



W rzeczywistości, jako audytor cyberbezpieczeństwa i pentester, systematycznie używam Nmapa podczas przeprowadzania wewnętrznych testów penetracyjnych, aby dowiedzieć się, gdzie jestem, kim są moi sąsiedzi w sieci lokalnej i jakie inne sieci są dostępne, a także jakie systemy się w nich znajdują. Mój cel jest prosty: zmapować sieć, określić rozmiar systemu informatycznego, a w szczególności naszkicować jego powierzchnię ataku.



Mapowanie sieci może być również przydatne w kontekście diagnostyki sieci, nadzoru, mapowania zasobów (czy naprawdę jesteś pewien, że Twój system informatyczny składa się wyłącznie z tego, co znajduje się w Active Directory lub w GLPI/OCS Inventory? Może być również wykorzystywane do wykrywania obecności Shadow IT w systemie informatycznym.



### II. Używanie Nmap do skanowania zasięgu sieci



#### A. Wykrywanie sieci za pomocą skanowania Nmap



Chcielibyśmy teraz przejść na wyższy poziom i przeanalizować całą naszą sieć lokalną. Nic nie może być prostsze: wszystko, co musimy zrobić, to ponownie użyć poleceń, które widzieliśmy w poprzedniej sekcji, ale określić CIDR zamiast prostego IP Address.



CIDR (**Classless Inter Domain Routing**) to "klasyczna" notacja do określania zakresu sieci i jej zasięgu (przy użyciu maski). Na przykład "192.168.0.0/24" jest "tłumaczeniem" zapisu maski dziesiętnej "255.255.255.0".



Aby użyć Nmap poprzez określenie CIDR, możemy użyć go w następujący sposób:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



Możliwe jest również, podobnie jak w przypadku portów w poprzedniej sekcji, określenie wielu hostów, wielu sieci lub zakresu:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



Oto przykład wyników, które możemy uzyskać podczas skanowania sieci:



![nmap-image](assets/fr/26.webp)



wyniki skanowania Nmap w celu zmapowania kilku sieci



W szczególności widzimy kilka aktywnych hostów, a każda sekcja hosta zaczyna się od takiej linii:



```
Nmap scan report for <name> (<IP>)
```



Pozwala nam to wyraźnie zobaczyć, do którego hosta odnoszą się poniższe wyniki. Ostatnia linia jest również ważna:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Wiemy, że w przeskanowanych sieciach Nmap wykrył 5 aktywnych hostów.



#### B. Pod maską: analiza sieci za pomocą Wireshark



Przyjrzymy się teraz bliżej temu, co dzieje się na poziomie sieci podczas wykrywania sieci za pomocą Nmapa.



Jak widzieliśmy w poprzedniej sekcji, domyślnie Nmap używa protokołu ARP do wykrywania obecności hostów w sieci lokalnej:



![nmap-image](assets/fr/27.webp)



pakiety aRP przechwycone podczas skanowania sieci lokalnej przy użyciu Nmapa i jego domyślnych opcji



W ten sposób jest w stanie wykryć praktycznie wszystkie hosty w sieci lokalnej, ponieważ odpowiedź na żądanie ARP jest zazwyczaj dostarczana przez wszystkie hosty aktywne w sieci i nie wydaje się w żaden sposób podejrzana.



W przypadku sieci zdalnych Nmap wykorzystuje kombinację technik:



![nmap-image](assets/fr/28.webp)



pakiety iCMP i TCP przechwycone podczas skanowania zdalnej sieci przy użyciu Nmapa i jego domyślnych opcji



Aby być bardziej precyzyjnym, Nmap używa pakietu echa ICMP (klasyczny przypadek pingowania) i pakietu ICMP Timestamp, zwykle używanego do obliczania czasu tranzytu pakietów. Nmap ma nadzieję uzyskać odpowiedź od hostów w zdalnych sieciach.



Ale jest w tym coś więcej. Na powyższym zrzucie Wireshark widać, że pakiety **TCP SYN** są systematycznie wysyłane na porty TCP/443 każdego potencjalnego hosta w skanowanych sieciach, a także pakiety **TCP ACK** na port TCP/80.



**Po co wysyłać pakiety TCP na porty w ramach wykrywania sieci?



Wysłanie pakietu SYN na dany port pozwala Nmapowi **określić, czy usługa nasłuchuje na tym porcie**. Jeśli host odpowie na pakiet SYN pakietem SYN/ACK, oznacza to, że jest aktywny i że usługa nasłuchuje na tym porcie. Nmap próbuje więc szczęścia na tej usłudze, **nawet jeśli nie uzyskano odpowiedzi na ping**.



Wysłanie pakietu ACK na dany port pozwala Nmapowi **określić, czy firewall jest obecny na tym hoście**. Jeśli host odpowie na pakiet ACK pakietem RST (Reset), oznacza to, że firewall jest prawdopodobnie obecny na tym hoście i blokuje niechciany ruch. W ten sposób host zdradza swoją obecność w sieci, nawet jeśli nie odpowiedział na inne żądania.



Należy jednak pamiętać, że wykrywanie zapory przy użyciu tej techniki może nie być całkowicie niezawodne we wszystkich przypadkach. Niektóre hosty mogą odpowiadać generate RST z powodów innych niż obecność zapory sieciowej, takich jak określona konfiguracja usługi lub systemu operacyjnego. Ponadto nowoczesne zapory sieciowe można skonfigurować tak, aby nie odpowiadały na tego typu próby wykrywania.



Przeszliśmy już długą drogę i możemy wykonać podstawowe wykrywanie sieci. Przyjrzymy się teraz kilku dodatkowym opcjom, które dadzą nam większą kontrolę nad zachowaniem Nmapa.



### III. Wykrywanie sieci bez skanowania portów za pomocą Nmap



Jak być może zauważyłeś, domyślnie Nmap **wykonuje skanowanie portów po wykryciu aktywnego hosta**, co dodaje ogromną ilość pakietów i oczekiwanie na odpowiedzi do naszego skanowania. Jeśli masz 5 hostów w sieci, Nmap spróbuje sprawdzić stan około 5000 portów, co zajmie więcej czasu.



Możliwe jest jednak użycie opcji Nmapa do **wykrycia tylko aktywnych hostów** w sieci, bez wykrywania ich usług.



Jeśli chcemy tylko wiedzieć, które hosty są osiągalne, bez żadnych informacji o usługach i portach, które eksponują, możemy użyć opcji "-sn", aby wykonać **tylko skanowanie za pomocą żądań ICMP Echo (ping) i ARP**. Innymi słowy, można całkowicie wyłączyć skanowanie portów:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Oto wynik wykrywania sieci Nmap wykonanego bez skanowania portów:



![nmap-image](assets/fr/29.webp)



Wynik wykrywania sieci bez skanowania portów za pomocą Nmap.



Wspomnieliśmy już o możliwych ograniczeniach używania samego protokołu ICMP do wykrywania hostów (w przypadku sieci zdalnych). Dlatego Nmap wykorzystuje również kilka sztuczek, które mogą zdradzić obecność firewalla lub określonej usługi na hostach. Za pomocą opcji możemy ponownie wykorzystać te sztuczki, a nawet je rozszerzyć, bez konieczności ponownego rozpoczynania pełnego skanowania portów każdego wykrytego hosta.



Aby to zrobić, użyjemy opcji "-PS" (TCP SYN) i "-PA" (TCP ACK), które pozwolą nam określić porty, do których chcemy dołączyć w ramach naszego wykrywania hostów, a także opcji "-PP":



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Skanowanie to zapewnia już, że wykrywanie hostów jest nieco bardziej kompletne niż w przypadku opcji domyślnych.



Zaczynamy otrzymywać dość wszechstronne polecenia, używając wielu opcji. Dzieje się tak, ponieważ wiemy, jak działa Nmap i jakie są ograniczenia jego "domyślnych" opcji, które czasami mogą spowodować, że stracimy czas lub przegapimy ważne Elements. To jest cały sens poświęcania czasu na jego opanowanie!



Aby wyszczególnić opcje naszego ostatniego zamówienia:





- "`-sn`: wyłącza skanowanie portów dla każdego aktywnego hosta wykrytego przez Nmap.





- "`-PP`: włącza echo ICMP (skanowanie ping) w celu wykrycia hosta.





- "`-PS <PORT>`": wysyła pakiet TCP SYN na wskazany port(y) w celu wykrycia aktywnej usługi zdradzającej obecność hosta, który nie odpowiedział na ping.





- "`-PA <PORT>`": wysyła pakiet TCP ACK na wskazany port(y) w celu wykrycia aktywnej zapory sieciowej zdradzającej obecność hosta, który nie odpowiedział na ping.




W powyższym przykładzie określam porty, które uważam za najczęściej ujawniane w moich kontekstach Nmap dla opcji "-PS". Te różne porty zostaną następnie przetestowane na każdym hoście, nie w celu sprawdzenia, czy usługa, którą hostują, jest naprawdę aktywna, ale w celu sprawdzenia, czy pozwala nam to wykryć hosta, który nie odpowiedział na nasze ICMP Echo, a jednocześnie jest aktywny (poprzez odpowiedź z usługi lub zapory hosta).



Oto, co można zobaczyć na zrzucie sieci wykonanym w czasie takiego skanowania, w tym przypadku wyciągu na pojedynczym hoście docelowym:



![nmap-image](assets/fr/30.webp)



pakiety wysyłane przez Nmap podczas zaawansowanego wykrywania sieci, bez skanowania portów



Znajdujemy nasze pakiety TCP SYN, nasze TCP ACK na porcie TCP/80 i nasze echo ICMP. Nmap wykona wszystkie te testy dla każdego hosta będącego celem naszego skanowania wykrywającego sieć.



### IV. Używanie pliku zasobów do namierzania za pomocą Nmap



Określanie celów może szybko okazać się skomplikowane w rzeczywistych systemach informatycznych, które czasami mogą składać się z dziesiątek lub setek sieci, podsieci i sieci VLAN. Dlatego łatwiej jest użyć pliku jako źródła dla Nmapa niż określać je jeden po drugim w wierszu poleceń.



Na początek utwórz prosty plik zawierający jeden wpis w wierszu:



![nmap-image](assets/fr/31.webp)



plik zawierający jeden cel (host lub sieć) w wierszu



Następnie możemy użyć wszystkich opcji Nmap, które widzieliśmy do tej pory i określić opcję "-iL <ścieżka/plik>":



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Nmap uwzględni wtedy w swoim skanowaniu wszystkie cele zawarte w naszym pliku.



Jeśli chcesz mieć pewność, że wszystkie cele zostaną wzięte pod uwagę, możesz użyć opcji "-sL -n". Nmap zinterpretuje wtedy tylko CIDR i hosty w pliku i wyświetli je, bez wysyłania żadnych pakietów przez sieć:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Zapewnia to, że lista hostów do przeskanowania jest dokładna.



Ostatnia ważna wskazówka, którą chciałbym się z wami podzielić, dotyczy **wykluczenia hosta lub sieci jako części skanowania**. Potrzeba wykluczenia hosta może być konieczna w wielu przypadkach, szczególnie jeśli chcemy mieć pewność, że **wrażliwy komponent systemu informatycznego nie zostanie zakłócony lub zakłócony przez nasze skanowanie**.



Częstymi przykładami takich potrzeb są sytuacje, w których firma posiada sprzęt przemysłowy (PLC) lub sprzęt medyczny. Taki sprzęt jest czasami źle zaprojektowany i wcale nie jest przeznaczony do odbierania źle sformatowanych pakietów lub zbyt wielu z nich. Z oczywistych względów dostępności lub ryzyka biznesowego/ludzkiego, lepiej jest wykluczyć je z testów.



Aby wykluczyć adresy IP lub sieci z naszego skanowania, możemy użyć opcji Nmap "--exclude", na przykład:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



W tym przykładzie skanuję sieć "192.168.1.0/24", ale wykluczam znajdującego się w niej hosta "192.168.1.140". Żadne pakiety nie zostaną wysłane przez Nmap do tego hosta. Inny przykład z wykluczeniem podsieci:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



Podobnie, przeskanuję dużą sieć "10.0.0.0/16", ale sieć "10.0.100.0/24" nie zostanie przeskanowana. Ponownie zalecam użycie opcji "-sL -n", aby uzyskać bardzo jasny obraz tego, które hosty zostaną przeskanowane, a które zostaną wykluczone ze skanowania, zwłaszcza jeśli działasz w wrażliwym kontekście.



### V. Wykrywanie sieci i skanowanie portów



Możemy teraz połączyć to, czego nauczyliśmy się w tej sekcji z tym, czego dowiedzieliśmy się w poprzedniej sekcji o opcjach skanowania portów. Domyślnie Nmap skanuje 1000 najczęściej używanych portów na każdym aktywnym hoście, który wykryje. Widzieliśmy, jak zapobiec temu zachowaniu, jeśli tego nie chcemy, ale możemy je w pełni kontrolować, a nawet rozszerzyć, jeśli odpowiada to naszym potrzebom.



Na przykład poniższe polecenie sprawdzi obecność usługi nasłuchującej na porcie TCP/22 na każdym skanowanym hoście:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap najpierw wykona wykrywanie sieci, aby wyświetlić listę aktywnych hostów, a dla każdego z nich sprawdzi, czy usługa jest obecna na porcie TCP/22.



W ten sam sposób możemy wykonać pełne skanowanie wszystkich portów TCP na każdym hoście wykrytym w sieci "192.168.0.0/24", wyłączając na przykład hosta "192.168.0.4":



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Możesz dowolnie łączyć wszystkie opcje, których nauczyliśmy się do tej pory, aby dostosować je do własnych potrzeb.



### VI. Wnioski



W tej sekcji zobaczyliśmy, jak używać Nmapa do mapowania sieci przy użyciu różnych opcji. Mamy teraz dokładne zrozumienie celów naszego skanowania, a także zachowania Nmapa podczas skanowania portów i metody wykrywania hostów. A co najważniejsze, wiemy, jakie są domyślne zachowania i ograniczenia Nmapa oraz jak korzystać z jego głównych opcji, aby pójść dalej.



W następnej sekcji przyjrzymy się mechanizmom i opcjom wykrywania wersji usług i systemów operacyjnych skanowanych przez Nmap.




## 6 - Wykrywanie wersji usług i systemu operacyjnego za pomocą Nmap



### I. Prezentacja



W tej sekcji dowiemy się, jak używać Nmapa do wykrywania i dokładnego wykrywania wersji usług i systemów operacyjnych używanych przez skanowane hosty. Przyjrzymy się szczegółowo, w jaki sposób Nmap wykonuje to zadanie, a także ograniczeniom narzędzia, aby lepiej zrozumieć i zinterpretować jego wyniki.



Jak widzieliśmy w poprzednich sekcjach tego samouczka, domyślnie Nmap nie sprawdza, jakie usługi są dostępne na portach, które skanuje i uważa za otwarte. Jeśli więc nasłuchujesz usługi internetowej na porcie TCP/22, Nmap będzie nadal zgłaszał ją jako otwartą, ale jako usługę `SSH`. Dzieje się tak, ponieważ Nmap używa [bazy danych](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) lokalnego systemu do wyszukiwania relacji między portem/protokołem a nazwą usługi (plik `/etc/services/`).



W większości przypadków [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) dostarczy prawidłowych informacji, ponieważ w środowisku produkcyjnym rzadko można znaleźć takie przypadki. Jednak pozostałe przypadki to sytuacje, w których klasyczna usługa ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP itp.) jest wystawiona na nieklasycznym porcie (np. 2022 dla usługi SSH), w którym to przypadku Nmap nie znajdzie dopasowania w swojej lokalnej bazie danych lub takie, które nie pasuje do rzeczywistości, a ty przegapisz ważne informacje.



Na szczęście Nmap oferuje bardzo precyzyjne opcje i mechanizmy wykrywania, która dokładnie usługa może ukrywać się za otwartym portem. Posiada nawet bazę zapytań i sygnatur do identyfikacji dokładnych technologii i wersji. Oprócz usług, Nmap może również zidentyfikować używaną technologię i jej wersję.



Właśnie temu przyjrzymy się w tej sekcji.



### II. Jak wykryć technologię lub wersję



#### A. Przypomnienie sposobu identyfikacji technologii lub wersji



Identyfikacja technologii i wersji wymaga pobrania nazwy usługi, CMS, aplikacji lub oprogramowania nasłuchującego na docelowym porcie. Na przykład, strona internetowa jest zarządzana przez CMS (`WordPress`), uruchamiana przez usługę internetową (`Apache`, IIS, Nginx) i hostowana przez serwer (Linux lub Windows). Ale skąd wiadomo, która usługa sieciowa jest uruchomiona?



Klasyczną metodologią wyszukiwania tych informacji jest _banner grabbing_, który polega po prostu na zlokalizowaniu miejsca, w którym dana usługa wyświetla te informacje i odczytaniu danych. Bardzo często, w domyślnej konfiguracji lub przetwarzaniu, usługi wyświetlają swoją nazwę, a nawet wersję jako pierwszą odpowiedź po połączeniu.



![nmap-image](assets/fr/32.webp)



wyświetla wersję, gdy tylko połączenie TCP zostanie nawiązane przez usługę FTP



Tutaj widzimy, że proste połączenie TCP z tą usługą poprzez `telnet` skutkuje pakietem TCP zawierającym jej technologię i wersję.



Gdy już wiesz, z jakim typem usługi masz do czynienia, możesz również wysyłać określone polecenia lub żądania do tej usługi, aby wydobyć z niej informacje. Te żądania/polecenia mogą być również wysyłane na ślepo (bez pewności, że są właściwym typem usługi), w nadziei, że jedno z nich sprowokuje odpowiedź z danej usługi.



W innych, bardziej zaawansowanych przypadkach konieczne jest wysłanie określonych pakietów, aby wywołać reakcję, taką jak błąd, który dostarczy szczegółowych informacji na temat używanej wersji lub technologii.



Jak można sobie wyobrazić, Nmap użyje wszystkich tych technik, aby spróbować zidentyfikować dokładny typ usługi hostowanej na porcie, a także nazwę jej technologii i wersji.



#### B. Zrozumienie sond i dopasowań Nmap



Aby przeprowadzić wszystkie te kontrole na każdym skanowanym porcie, Nmap korzysta z lokalnej bazy danych, która jest często aktualizowana (podobnie jak plik binarny lub jego moduły). Jest to plik tekstowy składający się z kilku tysięcy wierszy: `/usr/share/nmap/nmap-service-probes`.



Plik ten składa się z wielu wpisów zorganizowanych wokół dwóch głównych wytycznych:





- The `Probe`: jest to definicja pakietu, który Nmap wyśle w celu sprowokowania reakcji ze strony usługi, która ma zostać zidentyfikowana. Potraktuj to jako ślepą próbę w stylu _Hello? Guten Tag? Halo? Um... Może Buenos Dias? Gdy tylko docelowa usługa otrzyma sondę, którą rozumie (tj. mówi poprawnym protokołem), odpowie Nmapowi, który następnie potwierdzi typ usługi.





- Match": są to wyrażenia regularne, które Nmap stosuje do otrzymanej odpowiedzi. Jeśli wysłanie żądania HTTP GET wywołało odpowiedź z usługi, Nmap zastosuje dziesiątki wyrażeń regularnych do tej odpowiedzi, aby zidentyfikować obecność, na przykład, słowa `Apache`, `Nginx`, `Microsoft IIS` itp.




Istnieje kilka innych dyrektyw dla konkretnych przypadków, ale najważniejsze dla zrozumienia, jak działa Nmap i dostosowania jego użycia są te. Aby uczynić tę część teorii bardziej konkretną, oto przykład:



![nmap-image](assets/fr/33.webp)



przykład sondy w pliku `/usr/share/nmap/nmap-service-probes` Nmapa



W pierwszym wierszu tego przykładu widzimy łatwą do zrozumienia sondę o nazwie `GetRequest`. Jest to pakiet TCP zawierający puste żądanie HTTP GET do katalogu głównego usługi sieciowej przy użyciu protokołu HTTP/1.0, po którym następuje podawanie wiersza i pusty wiersz.



Linia `ports` mówi Nmapowi, na który port wysłać tę sondę. Pozwala to nadać priorytet testom i zaoszczędzić czas.



Na koniec mamy dwa przykłady `match`. Pierwszy, na przykład, skategoryzuje skanowaną usługę sieciową jako `ajp13`, jeśli wyrażenie regularne zawarte w tej linii pasuje do otrzymanej odpowiedzi usługi.



Aby pomóc ci zrozumieć, jak mogą wyglądać sondy, oto lista niektórych z nich, które znajdziesz w tym pliku (w chwili pisania tego samouczka jest ich 188).



![nmap-image](assets/fr/34.webp)



przykład kilku sond używanych przez Nmap i obecnych w pliku `/usr/share/nmap/nmap-service-probes`._



Pierwsze dwa (zwane `NULL` i `GenericLines`) są tutaj szczególnie interesujące, ponieważ po prostu wysyłają pusty pakiet TCP lub taki, który zawiera przerwanie linii. Usługi serwera często ogłaszają się dokładnie w momencie otrzymania połączenia, bez żadnych konkretnych działań, poleceń lub żądań ze strony klienta.



Oto przypadek nieco bardziej złożonego _match_:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



Dokładne wyrażenie regularne jest tutaj zawarte pomiędzy `m|` i `|`, które ograniczają każde wyrażenie regularne w tym pliku. Poświęć trochę czasu na przeczytanie całego przykładu. Zauważysz zaznaczenie w wyrażeniu regularnym: `([\d.]+)`, używane do wyodrębnienia wersji. Ten przykład definiuje również inne Elements, takie jak nazwa produktu `p/nginx/`, pobrana wersja `v/$1/` i CPE z wersją `cpe:/a:igor_sysoev:nginx:$1/`.



CPE (Common Platform Enumeration) to znormalizowany system notacji używany do identyfikacji i opisu oprogramowania i sprzętu. Format ten umożliwia bardziej efektywne zarządzanie podatnościami i konfiguracjami bezpieczeństwa, a przede wszystkim ujednolicony sposób ich reprezentowania, niezależnie od danego produktu. Oto dwa przykłady CPE: `cpe:/o:microsoft:windows_8.1:r1` i `cpe:/a:apache:http_server:2.4.35`



Tutaj wyraźnie określamy ich typy `o` dla systemu operacyjnego, `a` dla aplikacji, dostawcy, produktu i wersji.



Tak więc, w przypadku _match_ z jednym z tych wyrażeń regularnych, pobierzemy nie tylko nazwę usługi, ale także jej wersję i dokładne CPE, co ułatwi znalezienie CVE wpływających na tę wersję. Informacje te znajdują się w standardowym wyjściu Nmapa i są bardzo przydatne do innych celów, które omówimy w kilku sekcjach.



Dokładna składnia _matches_ i, bardziej ogólnie, dyrektyw w pliku `/usr/share/nmap/nmap-service-probes` nie kończy się na tym i może wydawać się dość skomplikowana, jeśli nie jesteś przyzwyczajony do manipulowania Nmapem i jego wynikami. Powinieneś jednak przynajmniej pamiętać o jego istnieniu i ogólnym działaniu, co przyda się później, gdy będziesz chciał zrozumieć lub debugować wynik, dostosować skanowanie lub nawet przyczynić się do rozwoju Nmapa.



### III. Używanie Nmap do wykrywania wersji



Teraz użyjemy całej tej złożonej mechaniki _Probe_ i _Match_ poprzez prostą opcję: `-sV`. To po prostu mówi Nmapowi: spróbuj dowiedzieć się dokładnie, które usługi i wersje portów ustawiłeś jako otwarte.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



Oto kompletny przykład wyniku takiego polecenia:



![nmap-image](assets/fr/35.webp)



wyniki wykrywania wersji aplikacji Nmap wystawionych w sieci



Tutaj widzimy, że Nmap zdołał zidentyfikować wszystkie wersje usług sieciowych wystawionych przez ten cel i wyświetla te informacje w nowej kolumnie `VERSION`. Możliwe jest wyświetlenie dość dokładnych informacji, nawet do systemu operacyjnego, jeśli informacje te są częścią odzyskanej sygnatury.



Aby szczegółowo zrozumieć, co dzieje się podczas skanowania podatności, możemy użyć opcji `--version-trace`. Zapewni to widok trybu debugowania, wyświetlający _Probe_, który doprowadził do wykrycia:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



W rezultacie będziemy mieli wiele informacji do posortowania. Spróbuj zidentyfikować linie zaczynające się od `Service scan Hard match`. Zobaczysz wtedy linie takie jak te:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Możemy wyraźnie zobaczyć, które _Probes_ zostały użyte do wykrycia technologii i wersji (w tym przypadku `NULL` i `GetRequest` _Probes_), a także pobrane informacje.



### IV. Opanowanie testów i dokładność wykrywania



Wrócimy teraz do dyrektywy w pliku `/usr/share/nmap/nmap-service-probes`, której nie przyjrzeliśmy się wcześniej:



![nmap-image](assets/fr/36.webp)



dyrektywa `rarity` probes w pliku `/usr/share/nmap/nmap-service-probes`._



Ta dyrektywa jest używana do wskazania rzadkości (tj. priorytetu/prawdopodobieństwa) związanej z _Probe_. Ta notacja od 1 do 9 pozwala kontrolować kompletność analizy wykonywanej przez Nmap podczas wysyłania _Probes_. W systemie "notacji" Nmapa, rzadkość 1 dostarcza informacji w zdecydowanej większości przypadków, podczas gdy rzadkość 8 lub 9 reprezentuje bardzo szczególny przypadek, specyficzny dla konfiguracji lub usługi, która rzadko występuje.



Dla jasności, w domyślnym przypadku Nmap wyśle do każdej usługi, która ma zostać zidentyfikowana, _Probes_, które mają rzadkość od 1 do 7. Aby dać ci lepsze wyobrażenie o rozkładzie _Probes_ według _rarity_, oto ich liczba:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Może się to wydawać sprzeczne z intuicją, jest więcej "rzadkości" 8 i 9 niż pozostałych. Dzieje się tak właśnie dlatego, że sondy rarity 1 są ogólne i działają w większości przypadków, niezależnie od usługi (pamiętaj o sondzie `NULL`, która po prostu wysyła pusty pakiet TCP). Podczas gdy bardziej złożone sondy są prawie unikalne dla każdej usługi.



Jeśli chcemy ręcznie zarządzać sondami, których chcemy użyć w naszym skanowaniu wersji, możemy użyć opcji `--version-intensity`. Oto dwa przykłady:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Aby zakończyć ten temat, oto przykład _Probe_ 9 i 8:



![nmap-image](assets/fr/37.webp)



przykłady sondy o rzadkości 8 i 9 w pliku `/usr/share/nmap/nmap-service-probes`._



Te dwa _Probes_ wykrywają serwery Quake1 i Quake2 (gra wideo). Interesujące z nostalgicznego punktu widzenia, ale mało przydatne w codziennym życiu.



W zależności od potrzeb związanych z precyzją lub szybkością, należy pamiętać, że zasada "rzadkości" istnieje i może mieć wpływ na wynik.



### V. Używanie Nmap do wykrywania systemów operacyjnych



Przyjrzymy się teraz, w jaki sposób Nmap może pomóc nam wykryć systemy operacyjne hostów skanowanych i wykrywanych w sieci. Aby to zrobić, użyj opcji Nmap `-O` (dla `OS Scan`).



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



Oto przykład wyników. Tutaj Nmap mówi nam, że jest to prawdopodobnie system operacyjny Linux i oferuje nam różne statystyki dotyczące jego dokładnej wersji.



![nmap-image](assets/fr/38.webp)



wykrywanie prawdopodobieństwa identyfikacji systemu operacyjnego przez Nmap



Aby to osiągnąć, Nmap użyje wielu technik, które działają w bardzo podobny sposób do _Probes_ i _Matches_ do wykrywania technologii i wersji. Główną różnicą jest to, że Nmap użyje dość "niskopoziomowych" parametrów ICMP, TCP, UDP i innych protokołów. Oto dwa przykłady testów wykrywających system operacyjny Microsoft Windows 11:



![nmap-image](assets/fr/39.webp)



przykłady testów przeprowadzonych przez Nmap w celu wykrycia systemu operacyjnego Windows 11



Spójrzmy prawdzie w oczy, testy te są bardzo trudne do zinterpretowania i nie zamierzamy próbować zrozumieć ich dogłębnie w kontekście wprowadzającego samouczka Nmap. Jeśli chcesz zagłębić się w temat, plik zawierający te informacje to `/usr/share/nmap/nmap-os-db`.



Należy jednak pamiętać, że wykrywanie systemu operacyjnego jest bardziej prawdopodobieństwem ustalonym przez Nmap niż pewnością.



### VI. Wnioski



W tej sekcji dowiedzieliśmy się, jak korzystać z opcji Nmapa do wykrywania technologii, wersji i systemów operacyjnych skanowanych hostów i usług. Teraz dobrze rozumiemy, w jaki sposób Nmap uzyskuje te informacje zdalnie. Zapoznaliśmy się również z opcjami zarządzania szczegółowością i dokładnością testów, a także ograniczeniami narzędzia w tym zakresie.



W następnej sekcji dowiemy się, jak używać skryptów Nmap NSE do przeprowadzania analizy bezpieczeństwa naszego systemu informatycznego. Poświęć trochę czasu na ponowne przeczytanie ostatnich sekcji, jeśli potrzebujesz, i nie wahaj się ćwiczyć i zagłębiać się w trzewia narzędzia, aby lepiej opanować to, czego nauczyliśmy się do tej pory.




## 7 - Analiza bezpieczeństwa: wykrywanie luk w zabezpieczeniach



### I. Prezentacja



W tej sekcji dowiemy się, jak używać narzędzia do skanowania sieci Nmap do wykrywania i analizowania luk w zabezpieczeniach na obiektach docelowych naszych skanów. W szczególności przyjrzymy się różnym opcjom dostępnym do wykonania tego zadania i zbadamy ograniczenia możliwości narzędzia, aby lepiej zrozumieć i zinterpretować jego wyniki.



W tej pierwszej sekcji przyjrzymy się skanerowi podatności Nmap i zobaczymy, jak korzystać z podstawowych opcji wykrywania podatności. W kolejnych sekcjach przyjrzymy się bliżej, jak działa ta funkcja i jak można ją dostosować.



### II. Używanie Nmap do wykrywania luk w zabezpieczeniach



Teraz chcemy użyć skanera sieciowego Nmap do wykrywania luk w usługach i systemach naszego systemu informatycznego. Oznacza to, że oprócz wykrywania aktywnych hostów, wyliczania narażonych usług oraz wykrywania wersji i technologii, Nmap będzie szukał luk w zabezpieczeniach.



Aby to osiągnąć, Nmap opiera się na skryptach NSE (_Nmap Scripting Engine_), które można postrzegać jako moduły umożliwiające granularne podejście do testowania.



Dzięki odpowiednim opcjom poprosimy Nmapa o użycie różnych skryptów NSE na każdej wykrytej usłudze, umożliwiając nam wykrycie:





- Błędy konfiguracji ;





- Dodatkowe i bardziej zaawansowane wersje i odkrycia systemu operacyjnego;





- Znane luki w zabezpieczeniach (CVE) ;





- Słabe identyfikatory ;





- Charakterystyczne Elements infekcji złośliwym oprogramowaniem ;





- Możliwości odmowy usługi ;





- Itd.




Jak widać, skrypty NSE znacznie rozszerzają możliwości Nmapa w zakresie operacji sieciowych, które może wykonywać. I to do wykonywania znacznie bardziej zaawansowanych zadań niż kiedykolwiek wcześniej. Dobrą wiadomością jest to, że jak zwykle, funkcje te mogą być używane po prostu za pomocą opcji i w domyślnym kontekście. To właśnie zobaczymy w następnej kolejności.



### III. Przykład skanowania podatności



Skrypty NSE mogą być używane podczas korzystania z Nmapa do skanowania pojedynczego portu na hoście, wszystkich usług na tym hoście lub wszystkich usług wykrytych w kilku sieciach. Możemy zatem użyć opcji, które zobaczymy we wszystkich kontekstach, które do tej pory przeanalizowaliśmy.



Aby włączyć skanowanie podatności za pomocą Nmapa, musimy użyć opcji `-sC`:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Pamiętaj, że domyślnie, jeśli nic nie określisz, Nmap przeskanuje tylko 1000 najpopularniejszych portów. Nie wykryje luk w zabezpieczeniach na bardziej egzotycznych portach, które mogą zostać ujawnione przez cele.



Przed użyciem tej funkcjonalności w produkcyjnym systemie informatycznym, zapraszam do dalszej lektury samouczka. W kolejnych sekcjach przyjrzymy się, jak lepiej kontrolować wpływ i typy testów, które zostaną uruchomione.



Dzięki ponownemu wykorzystaniu tego, czego nauczyliśmy się wcześniej, możemy na przykład być bardziej wszechstronni i skanować wszystkie porty TCP celu:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Oto wynik skanowania Nmap przy użyciu skryptów NSE:



![nmap-image](assets/fr/40.webp)



przykład wyników skanowania podatności hosta za pomocą Nmap._



Tutaj widzimy wyświetlanie dodatkowych informacji interesujących w kontekście analizy podatności:





- Usługa FTP może być dostępna anonimowo i nie jest chroniona przez uwierzytelnianie. Skrypt NSE odpowiedzialny za tę weryfikację mówi nam o tym, a nawet wyświetla część struktury drzewa usługi FTP. Tutaj widzimy, że mamy dostęp do katalogu `C` systemu Windows!





- Skrypt NSE odpowiedzialny za zaawansowane pobieranie usług internetowych wyświetla tytuł strony, dając nam lepsze wyobrażenie o tym, co hostuje usługa internetowa.





- Mamy również mini analizę konfiguracji usługi SMB (skrypty `smb2-time`, `smb-security-mode` i `smb2-security-mode`). Informacje są wyświetlane nieco inaczej, po wynikach skanowania sieci, aby ułatwić ich odczytanie. W szczególności informacje te wskazują na brak sygnatur SMB Exchange. Ta słabość konfiguracji pozwala na wykorzystanie celu w ataku SMB Relay, co jest istotną luką w zabezpieczeniach często wykorzystywaną w testach włamań/ataków cybernetycznych.




Oczywiście jest to tylko jeden przykład. Nmap posiada skrypty NSE dla wielu usług, ukierunkowane na szeroki zakres luk. Przyjrzymy się bliżej tym możliwościom w następnej sekcji.



Na zakończenie tego wprowadzenia do skanowania podatności, oto kompletne polecenie do wykrywania sieci, skanowania portów TCP, wykrywania wersji i podatności:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



Oto polecenie, które zaczyna przypominać bardziej realistyczne przypadki użycia Nmapa!



### IV. Zrozumienie ograniczeń Nmapa w skanowaniu podatności na ataki



Postawmy sprawę jasno: Nmap nie jest w stanie przeprowadzić pełnego testu penetracyjnego systemu informatycznego ani symulacji operacji Red Team. Ma kilka ograniczeń, których należy być świadomym, aby nie mieć fałszywego poczucia bezpieczeństwa:





- Ograniczony zasięg**: chociaż skrypty NSE Nmap są potężne, ich zasięg testowy może być ograniczony w porównaniu z innymi wyspecjalizowanymi narzędziami do wykrywania podatności. Niektóre podatności mogą nie być objęte dostępnymi skryptami NSE, takimi jak podatności Active Directory, narażenie wrażliwych danych lub bardziej zaawansowane przypadki podatnych aplikacji internetowych.





- Złożoność podatności**: niektóre typy podatności mogą być trudne do wykrycia za pomocą skryptów NSE ze względu na ich złożoność. Na przykład podatności wymagające złożonej interakcji ze zdalną usługą mogą nie zostać skutecznie wykryte przez Nmap (jak w przypadku nadmiernych uprawnień w udziale plików lub błędu kontroli uprawnień w aplikacji internetowej).





- Wykrywanie pasywne**: Nmap koncentruje się głównie na aktywnym skanowaniu w celu wykrycia luk w zabezpieczeniach, co oznacza, że może nie wykrywać skutecznie potencjalnych luk w zabezpieczeniach bez nawiązania aktywnego połączenia z hostami docelowymi. Podatności, które nie ujawniają się podczas aktywnego skanowania, mogą zatem zostać pominięte (jak w przypadku wstrzyknięcia kodu w aplikacji internetowej).





- Zależność od aktualizacji**: [Baza danych](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) skryptów NSE Nmapa stale się rozwija, ale może wystąpić opóźnienie między odkryciem nowej luki a dodaniem odpowiedniego skryptu do Nmapa. W rezultacie Nmap może nie zawsze być na bieżąco z najnowszymi lukami.





- Fałszywe alarmy i fałszywe alarmy negatywne**: jak w przypadku każdego narzędzia bezpieczeństwa, skrypty NSE Nmap mogą generować fałszywe alarmy (fałszywe alarmy o podatnościach) lub fałszywe alarmy negatywne (niewykryte podatności). Należy o tym pamiętać podczas analizowania wyników Nmap.




Dlatego ważne jest, aby zrozumieć, co Nmap robi, a czego nie robi, a także wiedzieć, jak interpretować jego wyniki. W szczególności widzieliśmy w tym samouczku, że domyślne opcje mogą sprawić, że przegapimy ważne Elements, które można odkryć przy ostrożnym użyciu.



Niezależnie od tego, czy jesteś administratorem systemu sieciowego, inżynierem bezpieczeństwa, czy nawet CISO, korzystanie z Nmap daje przegląd stanu bezpieczeństwa systemu informatycznego. Jest to ważny pierwszy krok w zabezpieczaniu systemu, który może być regularnie przeprowadzany przez zespół IT. Nie powinien on jednak zastępować interwencji i porad ekspertów [cyberbezpieczeństwa] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), którzy będą w stanie odkryć słabości znacznie bardziej kompleksowo niż Nmap.



### V. Wnioski



W tej pierwszej sekcji Modułu 3 wprowadziliśmy skanowanie luk w zabezpieczeniach za pomocą Nmap. Wiemy już, jak użyć głównej opcji do wykonania tego zadania, ale znamy również ograniczenia tego ćwiczenia. W następnej sekcji przyjrzymy się bliżej tej funkcjonalności, używając skryptów NSE, aby dziesięciokrotnie rozszerzyć możliwości Nmapa.



## 8 - Korzystanie ze skryptów Nmap NSE



### I. Prezentacja



W tej sekcji przyjrzymy się dogłębnie skryptom NSE (_Nmap Scripting Engine_). W szczególności przyjrzymy się, dlaczego są one jedną z największych zalet tego narzędzia, jak działają oraz jak przeglądać i korzystać z wielu istniejących skryptów.



Ta sekcja jest kontynuacją poprzedniego samouczka, w którym nauczyliśmy się, jak korzystać z funkcji skanowania podatności Nmap w podstawowy sposób. Teraz przyjrzymy się bliżej, jak działa [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) w tym zakresie, abyśmy mogli ponownie przeprowadzić bardziej precyzyjne i kontrolowane skanowanie.



### II. Koncepcja skryptów Nmap NSE



Skrypty Nmap NSE pozwalają na rozszerzenie jego możliwości w bardzo elastyczny sposób. Są one napisane w LUA, języku skryptowym, który jest łatwiejszy w obsłudze i dostępie niż C lub C# używany przez Nmap. Zaletą używania skryptu LUA z Nmapem zamiast samodzielnego narzędzia jest to, że pozwala nam to wykorzystać szybkość wykonywania Nmapa i standardowe funkcje (wykrywanie hosta, portu i wersji itp.).



Skrypty te są uporządkowane według kategorii, a pojedynczy skrypt może należeć do więcej niż jednej kategorii:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Technicznie rzecz biorąc, kategorie, do których należy skrypt, są wskazane bezpośrednio w jego kodzie.



![nmap-image](assets/fr/41.webp)



kategorie skryptów nSE `ftp-anon`._



Ten przykład pokazuje część kodu skryptu NSE `ftp-anon.nse`, którego wykonanie widzieliśmy w poprzedniej sekcji.



### III. Lista istniejących skryptów NSE



Domyślnie skrypty Nmap NSE znajdują się w katalogu `/usr/share/nmap/scripts/`, bez określonej struktury drzewa lub hierarchii. Oto przegląd zawartości tego katalogu:



![nmap-image](assets/fr/42.webp)



wyodrębnia zawartość katalogu `/usr/share/nmap/scripts/` zawierającego skrypty NSE



Ten katalog zawiera ponad 5000 skryptów NSE. W większości przypadków pierwsza część nazwy skryptu zawiera protokół lub kategorię, do której należy. Umożliwia to sortowanie listy, na przykład jeśli chcemy wyświetlić wszystkie skrypty dotyczące usługi FTP:



![nmap-image](assets/fr/43.webp)



lista skryptów NSE Nmap z nazwami zaczynającymi się od `ftp-`._



Nmap tak naprawdę nie oferuje opcji przeglądania i listowania skryptów NSE; można użyć polecenia `--script-help`, po którym następuje nazwa kategorii lub słowo:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



Wynikiem będzie jednak nazwa każdego skryptu i jego opis, co nie jest optymalne, jeśli wyszukiwanie prowadzi do kilkudziesięciu skryptów:



![nmap-image](assets/fr/44.webp)



wynik użycia polecenia `--script-help` Nmapa



Moim zdaniem najskuteczniejszą metodą jest użycie klasycznych poleceń Linuksa w katalogu `/usr/share/nmap/scripts/`:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Zachęcamy do przeglądania kodu modułów, które do ciebie przemawiają, aby lepiej zrozumieć, jak działa skrypt NSE.



### IV. Korzystanie ze skryptów Nmap NSE



Teraz nauczymy się, jak przeprowadzać skanowanie podatności na zagrożenia, starannie wybierając interesujące nas skrypty NSE.



#### A. Wybieranie skryptów według kategorii



Na początek możemy wybrać wykonywanie wszystkich skryptów należących do określonej kategorii. Musimy wskazać tę kategorię lub te kategorie Nmapowi za pomocą argumentu `--script <category>`:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Pierwsze polecenie jest odpowiednikiem komendy `nmap -sC`. Domyślnie Nmap wybierze skrypty z kategorii `default`, ale to tylko na potrzeby argumentacji. Następne polecenie, na przykład, użyje wszystkich skryptów z kategorii `discovery`:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Jak widzieliśmy, niektóre kategorie pozwalają nam szybko zidentyfikować, co robią powiązane skrypty NSE (`discovery`, `vuln`, `exploit`), podczas gdy inne definiują poziom ryzyka, wykrywalności lub stabilności przeprowadzonego testu. Jeśli znajdujemy się we wrażliwym kontekście i nie mamy dobrego zrozumienia różnych działań wykonywanych przez nasz wybór skryptów, możemy połączyć wybory, aby wybrać tylko te skrypty, które należą do kategorii `discovery` i `safe`:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Jeśli absolutnie i wyraźnie chcesz wykluczyć skrypty z kategorii `dos` i `intrusive`, możesz użyć następującej notacji:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Należy pamiętać, że określenie warunków wykluczenia w powyższy sposób spowoduje użycie wszystkich innych kategorii, które nie zostały wyraźnie wykluczone. Aby być bardziej sprawiedliwym, moglibyśmy określić, na przykład:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Oto kilka przykładów, jak obsługiwać skrypty NSE według kategorii, szczególnie w przypadku korzystania z Nmapa do analizy luk w zabezpieczeniach w rzeczywistych kontekstach.



#### B. Wybór skryptów jako jednostki



Możemy również zdecydować się na przeprowadzenie pojedynczego konkretnego testu podczas analizy, testu odpowiadającego skryptowi NSE. Aby to zrobić, musimy określić nazwę skryptu w parametrze `-script <name>`. Na przykładzie skryptu `ftp-anon.nse`:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



Otrzymujemy wtedy bardzo precyzyjny wynik:



![nmap-image](assets/fr/45.webp)



wynik użycia skryptu NSE `ftp-anon` na porcie FTP przez Nmap._



Widzimy wynik uruchomienia skryptu `ftp-anon` na porcie 21 i żadnym innym, ponieważ określiliśmy opcję `-p 21`. Mogliśmy również wykonać podstawowe skanowanie portów, wykonując skrypt `ftp-anon` NSE tylko na wykrytych usługach FTP:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



W ten sposób Nmap wykonałby również ten anonimowy test połączenia, gdyby znalazł usługę FTP na innym porcie.



Aby uzyskać krótki opis działania skryptu NSE, można użyć wspomnianej powyżej opcji `--script-help`:



![nmap-image](assets/fr/46.webp)



pomoc w wyświetleniu wyniku dla skryptu NSE `sshv1`._



Krótko mówiąc, po raz kolejny możemy ponownie wykorzystać wszystkie opcje wykrywania sieci, usługi, wersje i technologie, z których korzystaliśmy do tej pory!



#### C. Zarządzanie argumentami skryptu



W trakcie korzystania z Nmapa natkniesz się na pewne skrypty NSE, które wymagają argumentów wejściowych do poprawnego działania. Przyjrzymy się teraz, jak przekazać argumenty do tych skryptów za pomocą opcji Nmap.



Jako przykład weźmy skrypt `ssh-brute`, który pozwala na przeprowadzenie ataku brute force na usługę SSH.



Klasyczny atak brute force polega na przetestowaniu kilku haseł (czasami milionów) w celu uwierzytelnienia się na określonym koncie. Próbując tak wielu haseł, atakujący stawia na prawdopodobieństwo, że użytkownik użył słabego hasła w słowniku haseł używanym do ataku.



Ten skrypt ma "domyślne" opcje, które możemy dostosować do naszego kontekstu. Na przykład w kontekście tego ataku możemy dostarczyć Nmapowi listę użytkowników i słownik haseł, które mają zostać użyte. O ile mi wiadomo, nie jest możliwe łatwe wylistowanie argumentów wymaganych dla skryptu, więc najbardziej niezawodnym sposobem jest odwiedzenie oficjalnej strony Nmap. Bezpośredni link do dokumentacji skryptu NSE można uzyskać w odpowiedzi na opcję `--script-help`:



![nmap-image](assets/fr/47.webp)



wynik wyświetlenia pomocy dla skryptu NSE `ssh-brute` z linkiem do nmap.org._



Klikając na wskazany link, przechodzimy na tę stronę internetową witryny [https://nmap.org](https://nmap.org/):



![nmap-image](assets/fr/48.webp)



lista argumentów, które można przekazać do skryptu Nmap `ssh-brute` NSE



Tutaj mamy jasny widok argumentów, które mogą być użyte, główne z nich w naszym kontekście to `passdb` (plik zawierający listę haseł) i `userdb` (plik zawierający listę użytkowników). Dokumentacja odnosi się tutaj do wewnętrznych bibliotek Nmap, ponieważ te mechanizmy brute force i powiązane z nimi opcje są wzajemnie powiązane, aby były używane jednolicie w kilku skryptach (`ssh-brute`, `mysql-brute`, `mssql-brute` itp.) i dlatego będą miały mniej więcej te same argumenty:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Jak widać w tym ostatnim poleceniu, możemy określić niezbędne argumenty do skryptu Nmap za pomocą opcji `--scripts-args key=value,key=value`. Oto możliwy wynik działania Nmap podczas wykonywania SSH brute force za pomocą skryptu `ssh-brute` NSE:



![nmap-image](assets/fr/49.webp)



wynik wykonania SSH bruteforce przez Nmap._



Jak widać, informacje generowane przez skrypty NSE są poprzedzone przedrostkiem `NSE: [nazwa skryptu]` w interaktywnym wyjściu (wyjście terminala), co ułatwia ich znalezienie. W ramach zwykłego wyświetlania wyników Nmapa mamy po prostu podsumowanie wskazujące, czy wykryto słabe identyfikatory (w tym hasła, pamiętaj).



Aby pójść o krok dalej i przypomnieć, że wszystko to można wykorzystać oprócz wszystkich opcji, którym już się przyjrzeliśmy, oto polecenie, które wykryje sieć `10.10.10.0/24`, przeskanuje 2000 najczęściej używanych portów TCP i uruchomi anonimowe wyszukiwanie dostępu do usług FTP oraz kampanię brute force w usługach SSH:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



To tylko jeden przykład z wielu dostępnych skryptów i ich opcji. Ale teraz mamy lepsze pojęcie o tym, jak poradzić sobie ze skryptami NSE, czy wymagają one argumentów i jak przekazać te argumenty do Nmapa.



### V. Wnioski



W tej sekcji dowiedzieliśmy się, jak używać skryptów Nmap NSE do wykonywania różnych zadań. Zapraszam do zapoznania się z różnymi kategoriami skryptów i samymi skryptami, aby zobaczyć, jak wiele testów można zautomatyzować.



Od kilku odcinków gromadzimy mniej lub bardziej zaawansowane opcje wykrywania, skanowania i wyliczania. Do tej pory powinieneś być świadomy, że dane wyjściowe Nmapa i wyświetlane wyniki zaczynają być dość obszerne, czasem nawet zbyt gadatliwe dla naszego terminala. W następnej sekcji dowiemy się, jak opanować te dane wyjściowe, w szczególności poprzez przechowywanie ich w plikach w różnych formatach.






## 9 - Zarządzanie danymi wyjściowymi Nmap




### I. Prezentacja



W tej sekcji przyjrzymy się wynikom generowanym przez Nmap, a w szczególności różnym opcjom formatowania tych wyników. Przekonamy się, że Nmap może generować kilka formatów wyjściowych, aby zaspokoić różne potrzeby i że jest to również jedna z największych zalet tego narzędzia.



Domyślnie Nmap oferuje szczegółowy widok wyników skanowania i testów, które wykonuje. Obejmuje to przeskanowane hosty i usługi, te wykryte jako dostępne, specyfikę otwartych portów, ich status i wersję. Ponadto szczegóły skryptów NSE są również dostępne na wyjściu terminala. Jednak dane wyjściowe mogą szybko stać się obszerne, nawet przy jasnym formatowaniu informacji, co może utrudniać znalezienie dokładnych informacji w wynikach.



### II. Opanowanie formatów wyjściowych Nmap



#### A. Zapisywanie wyników skanowania w pliku tekstowym



Aby ułatwić pracę, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) umożliwia bardzo łatwe zapisanie wyników w pliku tekstowym. Może to być przydatne do archiwizacji, porównania z innymi testami, ale także do przeglądania tych danych wyjściowych za pomocą wyspecjalizowanych narzędzi do edycji tekstu lub języków skryptowych, takich jak Sublime text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed itp. Aby zapisać standardowe wyjście Nmapa w pliku tekstowym, możemy użyć opcji `-oN <filename>` ("N" w "normal"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Nic więc dziwnego, że Nmap wyświetli swoje standardowe wyjście w naszym terminalu, ale także w określonym pliku.



#### B. Dane wyjściowe generate Nmap w skondensowanym formacie



Istnieje również drugi format wyjściowy w stylu "tekstowym", który może być łatwo interpretowany przez człowieka: format "greppable".



Format ten został stworzony w celu zapewnienia "skondensowanego" widoku wyjścia Nmap, ustrukturyzowanego w taki sposób, aby ułatwić jego przetwarzanie przez narzędzia takie jak `grep`. Spójrzmy na przykład tego typu danych wyjściowych:



![nmap-image](assets/fr/50.webp)



nmap skanowanie sieci i wyjście w formacie "greppable"



Tutaj przeprowadziłem wykrywanie sieci, a także skanowanie portów oraz analizę technologii i wersji w sieci /24, a następnie zapisałem dane wyjściowe w pliku w formacie "greppable". Ostatecznie otrzymałem plik zawierający 2 wiersze dla każdego aktywnego hosta:





- Pierwsza linia mówi mi, że taki a taki host jest _Up_;





- Drugi wiersz mówi mi, które porty zostały przeskanowane, ich status oraz informacje o technologii i wersji pobrane w bardzo specyficznym formacie: `<port>/<status/<protokół>//<usługa>//<wersja>/,`




To formatowanie ze stałym separatorem pozwala na szybkie przetwarzanie przez narzędzia do przetwarzania tekstu, takie jak `grep`, lub języki skryptowe i programowania. Poniższe polecenie, na przykład, pozwala mi łatwo pobrać informacje o hoście `10.10.10.5` w przypadku ogromnego skanowania wykonanego przez Nmap, którego dane wyjściowe byłyby trudne do przeglądania:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



I odwrotnie, mogę również łatwo wyświetlić listę wszystkich hostów, które mają otwarty port 21, ponieważ porty i adresy IP znajdują się w tej samej linii:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



Aby generate takie wyjście, musimy użyć opcji `-oG <nazwa pliku>.gnmap` ("G" w "grep"). Z przyzwyczajenia używam tutaj rozszerzenia `.gnmap` dla takiego pliku, ale możesz użyć dowolnego:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Format ten może być wykorzystywany do różnych celów i jest szczególnie przydatny do szybkiego tworzenia skryptów/sortowania. Niemniej jednak jest on coraz częściej porzucany na rzecz formatu, któremu przyjrzymy się w następnej kolejności.



uwaga: format `-oG` greppable został oficjalnie wycofany od Nmap 7.90. Nadal może być używany w celu zapewnienia kompatybilności. Może być nadal używany do celów kompatybilności, ale zaleca się używanie formatu XML lub normalnego do wszelkich prac rozwojowych lub automatycznego parsowania



#### C. Format XML dla danych wyjściowych Nmap



Ostatnim formatem, o którym warto wspomnieć w tym samouczku, jest XML. W przeciwieństwie do poprzednich dwóch formatów, ten nie jest przeznaczony do odczytu przez ludzi, ale przez inne narzędzia lub skrypty.



XML (_eXtensible Markup Language_) to język znaczników używany do przechowywania i transportu danych, oferujący hierarchiczną strukturę za pomocą niestandardowych znaczników.



W Nmap format XML jest używany do generate szczegółowych raportów z przeprowadzonych skanowań, w tym informacji o hostach, portach i wykrytych lukach, a także dodatkowych informacji, które nie są wyświetlane w standardowym wyjściu Nmap.



Aby uzyskać plik wyjściowy generate w formacie XML, musimy użyć opcji `-oX` ("O" od "XML"):



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



Wynikiem jest standardowe wyjście Nmapa w terminalu, a także plik w formacie XML w bieżącym katalogu.



Oczywiście format XML nie jest przeznaczony do odczytu i interpretacji przez ludzi. Niemniej jednak, jeśli chcesz wykonywać skrypty lub zautomatyzowaną analizę tego formatu danych wyjściowych Nmapa, nadal musisz mieć pojęcie o używanych tagach i strukturze. Na przykład, oto część zawartości pliku XML utworzonego przez Nmap, który pokazuje wyniki skanowania dla 1 hosta:



![nmap-image](assets/fr/51.webp)



przykład rekordu XML dla 1 hosta podczas skanowania Nmap



Jest tu wiele informacji, a nas szczególnie interesują dwa otwarte porty:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Rozumiemy, że ten format ułatwi automatyczne analizowanie wyników, ponieważ każda informacja jest starannie uporządkowana w dedykowanym, nazwanym tagu lub atrybucie. W szczególności znajdujemy informację, z którą wcześniej się nie spotkaliśmy: CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Krótko wspomnieliśmy o CPE w sekcji 2 modułu 2, a informacje te są określane w dopasowaniach podczas wykrywania wersji. Nmap wykorzystuje swoje mechanizmy wykrywania usług, technologii i wersji, aby znaleźć powiązane CPE.



Pozwala nam to na ponowne wykorzystanie tych informacji w bazach danych i aplikacjach, które z nich korzystają. Mam na myśli w szczególności bazę danych NVD, która odwołuje się do CVE. Dla każdego CVE zawiera ona CPE, których dotyczy luka. Oto przykład CVE dotyczącego `a:microsoft:internet_information_services:7.5` z bazy danych NVD:



![nmap-image](assets/fr/52.webp)



obecność CPE w szczegółach CVE w bazie danych NVD



Teraz lepiej rozumiemy zalety tego formatu, który oferuje bardzo przejrzystą strukturę informacji i zawiera wszystkie dane zebrane lub przetworzone przez Nmap.



Odruchowo, systematycznie zapisuję moje skany Nmap we wszystkich trzech formatach jednocześnie. Jest to możliwe dzięki opcji `-oA <nazwa>` ("A" dla "All"), która utworzy plik `<nazwa>.nmap`, `<nazwa>.xml` i `<nazwa>.gnmap`. W ten sposób mam pewność, że nie zabraknie mi niczego, gdy będę musiał wrócić do wyników.



Dzięki tym trzem formatom powinieneś mieć wszystko, czego potrzebujesz, aby zapisać i ostatecznie przetworzyć wyniki Nmap w zautomatyzowany sposób. Format XML zostanie ponownie wykorzystany w następnej sekcji, gdy przyjrzymy się wykorzystaniu Nmap z innymi narzędziami bezpieczeństwa.



#### III. Generowanie raportu HTML ze skanowania Nmap



Format XML oferuje wiele możliwości, nie tylko służenie jako podstawa do generowania raportu w formacie HTML, który będzie bardziej przyjemny wizualnie do przeglądania.



Aby przekształcić plik Nmap w formacie XML na stronę internetową, użyjemy narzędzia `xsltproc`, które musimy najpierw zainstalować:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Po zainstalowaniu tego narzędzia wystarczy podać mu plik XML, który ma zostać przekonwertowany oraz nazwę raportu HTML, który ma zostać wygenerowany:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



W rezultacie cały nasz skan będzie ładnie ustrukturyzowany, z kilkoma kolorami i klikalnymi linkami w spisie treści!



![nmap-image](assets/fr/53.webp)



wyciąg z raportu skanowania Nmap w formacie HTML wygenerowany przez xsltproc._



Mówiąc ogólnie, plik XML zapisany przez Nmap zawiera odniesienie do innego pliku w formacie XSL:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



Konwersja do HTML jest zatem funkcją dostarczaną i ułatwianą przez Nmap, `xsltproc` jest powszechnym i uznanym narzędziem do wykonywania tego zadania (które nie pochodzi z pakietu narzędzi Nmap).



XSLT (_Extensible Stylesheet Language Transformations_) to podzbiór XSL, który umożliwia wyświetlanie danych XML na stronie internetowej i "przekształcanie" ich, równolegle ze stylami XSL, w czytelne, sformatowane informacje w formacie HTML.



źródło: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



Poziom informacji w raporcie jest równoważny z formatem XML Nmapa i wyższy niż w standardowym wyjściu terminala (_interactive output_).



### IV. Zarządzanie poziomem szczegółowości Nmapa



Przyjrzymy się teraz kilku opcjom Debugger Nmap lub śledzenia jego postępów.



Pierwszą opcją, o której powinniśmy wspomnieć, jest opcja `-v`, która zwiększa szczegółowość Nmapa. Oto przykład:



![nmap-image](assets/fr/54.webp)



szczegółowe dane wyjściowe nmapa przy użyciu opcji `-v`._



W przypadku skanowania wielu hostów i portów, wyjście terminala stanie się trudne do wykorzystania ze względu na ilość wyświetlanych informacji. Z tego powodu opcja ta powinna być używana w połączeniu z opcjami opisanymi wcześniej, które pozwalają na przechowywanie standardowego wyjścia Nmapa w pliku. Informacje związane z użyciem słowności nie będą zawarte w tym pliku wyjściowym. Jak widać na powyższym przykładzie, ta szczegółowość pozwala śledzić działania i odkrycia Nmapa w sposób jasny i bezpośredni. W przypadku dłuższego skanowania, gdzie wyświetlanie danych może być powolne, pozwala to uniknąć bycia ślepym na bieżącą aktywność Nmapa i wiedzieć, że sprawy postępują i w jakim tempie. Aby zwiększyć szczegółowość o kolejny poziom, można użyć opcji `-vv`.



Aby dokładniej śledzić aktywność Nmapa podczas skanowania, można użyć opcji `--packet-trace`. Z opcją `-v` otrzymujemy log na żywo wszystkich otwartych portów wykrytych przez Nmapa, podczas gdy z tą opcją otrzymujemy linię logu dla każdego pakietu wysłanego do portu. Naturalnie daje to bardzo szczegółowe dane wyjściowe, ale pozwala na szczegółowe monitorowanie aktywności Nmapa, oto przykład:



![nmap-image](assets/fr/55.webp)



szczegółowe monitorowanie aktywności Nmap poprzez `--packet-trace`



Ponownie, informacje te nie zostaną zapisane w pliku wyjściowym tworzonym przez Nmap, jeśli używane są opcje `-oN`, `-oG`, `-oX` lub `-oA`.



Nmap oferuje również dwie opcje debugowania: `-d` i `-dd`. Opcje te zachowują się podobnie do opcji `-v`, ale dodają dodatkowe informacje techniczne, takie jak podsumowanie parametrów technicznych na początku skanowania:



![nmap-image](assets/fr/56.webp)



opcje synchronizacji są wyświetlane w widoku debugowania Nmapa



W kilku następnych sekcjach przyjrzymy się opcjom "Timing" i dlaczego warto je znać.



Wreszcie, jeśli chcesz mieć tylko podstawowy, syntetyczny przegląd postępu skanowania Nmap, możesz użyć opcji `--stats-every 5s`. "5s" oznacza tutaj 5 sekund i może być modyfikowane w zależności od potrzeb. Jest to częstotliwość, z jaką będziemy otrzymywać informacje zwrotne od Nmapa na temat jego postępów:



![nmap-image](assets/fr/57.webp)



informacje wyświetlane przez opcję Nmap `--stats-every`



W szczególności możemy uzyskać procent postępu, a także wskazanie fazy, w której się znajduje: faza wykrywania hosta za pomocą [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/), faza wykrywania odsłoniętych portów TCP itp. Informacje te można również uzyskać na wyjściu terminala, naciskając "Enter" podczas skanowania.



Nmap nie jest jednak zbyt dobry w szacowaniu czasu trwania zadania, między innymi dlatego, że nie wie z góry, ile hostów i usług będzie musiał przeskanować.



### V. Wnioski



W tej sekcji przyjrzeliśmy się wielu opcjom zapisywania wyników skanowania Nmap w różnych formatach plików. Będzie to bardzo przydatne, ponieważ w realistycznym kontekście wyniki skanowania mogą zajmować setki, a nawet tysiące wierszy! Zobaczyliśmy również, jak zwiększyć poziom szczegółowości Nmapa w celu debugowania lub uzyskania raportu o postępie skanowania.



Format XML będzie szczególnie przydatny w następnej sekcji, w której przyjrzymy się kilku narzędziom, które mogą pracować z wynikami Nmap.




## 10 - Korzystanie z Nmap z innymi narzędziami bezpieczeństwa



### I. Prezentacja



W tej sekcji przyjrzymy się niektórym klasycznym zastosowaniom Nmapa z innymi darmowymi i otwartymi narzędziami bezpieczeństwa. W szczególności wykorzystamy to, czego nauczyliśmy się w poprzednich sekcjach, aby jeszcze bardziej zwiększyć moc i wydajność Nmapa.



Możliwość zapisywania wyników skanowania Nmap w formacie XML sprawia, że dane są kompatybilne z wieloma innymi narzędziami. Ponieważ obecnie prawie wszystkie języki programowania i skryptowe mają biblioteki zdolne do analizowania XML, znacznie ułatwia to przetwarzanie tych danych. Wiele narzędzi, szczególnie tych nastawionych na ofensywne bezpieczeństwo, posiada funkcje przetwarzania formatu XML generowanego przez Nmap. Przyjrzyjmy się temu bliżej.



Zamierzam wspomnieć o kilku narzędziach ofensywnych bez szczegółowego opisywania sposobu ich użycia lub działania. Zakładam, że czytelnik jest zaznajomiony z ich podstawowym zastosowaniem i że już działają. Ta sekcja będzie szczególnie interesująca dla profesjonalistów [cyberbezpieczeństwa] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), osób szkolących się lub tych, którzy zdecydowali się zagłębić w ten temat.



### II. Importowanie wyników Nmapa do Metasploita



Pierwszym narzędziem, któremu przyjrzymy się pod kątem ponownego wykorzystania danych Nmap w ofensywnych badaniach nad bezpieczeństwem i lukami w zabezpieczeniach, jest Metasploit.



Metasploit jest frameworkiem do przeprowadzania exploitów i ataków. Jest to darmowe rozwiązanie i uznane narzędzie, które zawiera dużą liczbę modułów napisanych w języku Ruby lub Python. Umożliwiają one wykorzystywanie luk w zabezpieczeniach, przeprowadzanie ataków, generowanie backdoorów, zarządzanie wywołaniami zwrotnymi (C&C lub funkcje komunikacji i kontroli) oraz jednolite wykorzystanie wszystkich funkcji.



W szczególności ten dobrze znany i szeroko stosowany system operacyjny może współpracować z bazą danych PostgreSQL (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/), w której przechowywane są hosty, porty, usługi, informacje uwierzytelniające i inne.





- Oficjalna dokumentacja Metasploit: [https://docs.metasploit.com/](https://docs.metasploit.com/)




W tym miejscu do gry wkracza Nmap i jego dane wyjściowe, ponieważ format XML danych wyjściowych Nmap można łatwo zaimportować do bazy danych Metasploita, aby zapełnić bazę danych hostów i usług, które można następnie szybko wyznaczyć jako cele tego lub innego ataku.



Po wejściu do interaktywnej powłoki Metasploit, zaczynam od stworzenia przestrzeni roboczej, rodzaju przestrzeni specyficznej dla mojego środowiska w danym dniu:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Po utworzeniu mojego obszaru roboczego musimy sprawdzić, czy komunikacja z bazą danych działa:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Na koniec możemy użyć polecenia Metasploit `db_import`, aby zaimportować nasz skan Nmap w formacie XML:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Oto wynik wykonania wszystkich tych poleceń:



![nmap-image](assets/fr/58.webp)



import skanowania Nmap w formacie XML do bazy danych Metasploit



Tutaj widać, że każdy host jest importowany wraz z jego usługami. Dane te można następnie wyświetlić za pomocą polecenia `services` lub `services -p <port>` dla określonej usługi:



![nmap-image](assets/fr/59.webp)



lista usług zaimportowanych z pliku XML do bazy danych Metasploit



Wreszcie, możemy szybko i łatwo ponownie wykorzystać te dane w module dzięki opcji `-R`, która "przekonwertuje" listę usług uzyskanych jako dane wejściowe dla dyrektywy `RHOSTS`, która służy do określenia celów ataku, który ma zostać przeprowadzony. Oto przykład z modułem `ssh_login`, który umożliwia przeprowadzenie ataku brute force na usługi [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



użyj opcji `services -R`, aby zaimportować usługi określone jako cel ataku



To tylko mały przykład tego, co można zrobić z danymi Nmap w Metasploit, ale daje on wyobrażenie o tym, jak szybko i łatwo można ponownie wykorzystać te informacje w ramach testu penetracyjnego, skanowania podatności lub cyberataku. Warto również wspomnieć, że Nmap może być uruchamiany bezpośrednio z Metasploita w celu zaimportowania wyników do bazy danych (polecenie `db_nmap`), co jest kolejnym interesującym tematem do omówienia!



### III. Używanie Nmap ze skanerem internetowym Aquatone



Drugim narzędziem, które chciałbym przedstawić w tej sekcji na temat ponownego wykorzystania wyników Nmap do ofensywnej analizy bezpieczeństwa i podatności, jest Aquatone.



Aquatone to skaner sieciowy przeznaczony do efektywnego badania aplikacji internetowych w sieci. Oferuje zaawansowane funkcje wykrywania usług internetowych, identyfikacji subdomen, analizy portów i odcisków palców aplikacji internetowych. Wszystko przedstawione w przejrzysty i zwięzły sposób w raportach HTML, JSON i tekstowych dla łatwej analizy bezpieczeństwa sieci.



Podobnie jak Metasploit, Aquatone może bezpośrednio przetwarzać format XML Nmapa i używać go jako celu skanowania. W szczególności może wyodrębnić tylko interesujące hosty i usługi (usługi sieciowe) ze wszystkich danych, które może zawierać raport Nmap.





- Link do narzędzia: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




Aby użyć danych wyjściowych XML Nmap z Aquatone, wystarczy wysłać plik XML w potoku, który zostanie wykorzystany przez Aquatone. Oto przykład:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Podczas gdy Aquatone normalnie wykonuje wykrywanie portów na hostach w celu znalezienia usług internetowych, w tym kontekście będzie polegać wyłącznie na wynikach Nmap, który już wykonał tę operację, oszczędzając w ten sposób czas:



![nmap-image](assets/fr/61.webp)



przy użyciu Nmap wyniki w formacie XML z `aquatone`._



Poniżej znajduje się fragment raportu przygotowanego przez Aquatone:



![nmap-image](assets/fr/62.webp)



przykład raportu `aquatone`



Osobiście często korzystam z Aquatone, aby uzyskać szybki przegląd typów stron internetowych obecnych w sieci, w szczególności dzięki funkcji zrzutów ekranu.



Również w tym przypadku posiadanie kompletnego raportu Nmap w formacie XML oszczędza czas i ułatwia jego ponowne wykorzystanie w innym narzędziu.



### IV. Wnioski



Te dwa przykłady wyraźnie pokazują, że format XML Nmapa ułatwia innym narzędziom korzystanie z jego wyników, ponieważ jest to ustrukturyzowany, łatwy w użyciu format danych. Istnieje wiele innych narzędzi zdolnych do przetwarzania tych wyników, takich jak zautomatyzowane narzędzia do raportowania, reprezentacje graficzne lub bardziej złożone, zastrzeżone skanery podatności.



Oczywiście można również tworzyć własne skrypty i narzędzia w Pythonie, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) lub dowolnym innym języku z biblioteką parsowania XML, aby manipulować i ponownie wykorzystywać dane wyników Nmap według własnego uznania.



Ta sekcja prowadzi nas do końca modułu samouczka na temat bardziej zaawansowanego wykorzystania Nmapa, w szczególności do skanowania luk w zabezpieczeniach za pomocą skryptów NSE.



W następnej części samouczka skupimy się między innymi na dodatkowych, bardziej technicznych najlepszych praktykach i wskazówkach dotyczących konkretnego skanowania, które może wykonać Nmap. Przyjrzymy się również opcjom optymalizacji wydajności skanowania, które są szczególnie przydatne podczas skanowania dużych sieci.




## 11 - Poprawa wydajności skanowania sieci



### I. Prezentacja



W tym rozdziale dowiemy się, jak zoptymalizować szybkość skanowania sieci wykonywanego za pomocą Nmapa przy użyciu różnych konkretnych opcji. W szczególności dowiemy się więcej o wewnętrznym działaniu Nmapa, od zarządzania _timeout_ po wstępnie zapisane konfiguracje narzędzia.



Teraz, gdy dobrze przyjrzeliśmy się funkcjom Nmapa, przejdźmy do bestii i jej mocy. Jeśli kiedykolwiek używałeś tego narzędzia w dużych sieciach, prawdopodobnie zauważyłeś, że niektóre skany mogą zająć dużo czasu, pomimo mocy narzędzia. I nie bez powodu: proste polecenie `nmap` z kilkoma opcjami może generate miliony pakietów celujących w setki tysięcy potencjalnych systemów i usług.



Co więcej, niektóre konfiguracje sprzętu sieciowego mogą celowo narzucać wolniejszą szybkość (liczbę pakietów na sekundę), ryzykując odrzucenie pakietów lub zablokowanie IP Address ze względów bezpieczeństwa.



W zależności od kontekstu, warto spróbować to wszystko zoptymalizować, o czym przekonamy się w tym rozdziale.



W każdym razie, możesz sprawdzić domyślne wartości parametrów, którym będziemy się przyglądać, a także czy opcje, których zamierzasz użyć, zostały poprawnie wzięte pod uwagę, poprzez debug Nmap (opcja `-d` opisana w poprzednim rozdziale):



![nmap-image](assets/fr/63.webp)



wyświetl opcje synchronizacji za pomocą opcji `-d` Nmapa



### II. Zarządzanie szybkością skanowania Nmap



#### A. Zarządzanie równoległością



Domyślnie Nmap używa zrównoleglenia w swoich skanach, aby je zoptymalizować, a wszystkie parametry, których używa, można modyfikować za pomocą różnych opcji. Jednak przypadki, w których faktycznie konieczna jest modyfikacja tych parametrów, są dość rzadkie, więc nie będziemy ich szczegółowo omawiać w tym samouczku:





- `--min-hostgroup/max-hostgroup <size>`: rozmiar równoległych grup skanowania hostów.





- `--min-parallelism/max-parallelism <numprobes>`: równoległość sond.





- `--scan-delay/--max-scan-delay <time>`: dostosowuje opóźnienie między sondami.




Wystarczy wiedzieć, że istnieją i można z nich korzystać.



#### B. Zarządzanie liczbą pakietów na sekundę



Domyślnie Nmap sam dostosowuje liczbę wysyłanych pakietów na sekundę w zależności od odpowiedzi sieci. Możliwe jest jednak wymuszenie tego ustawienia poprzez zdefiniowanie wysokiej i/lub minimalnej wartości liczby pakietów na sekundę. To ustawienie jest dokonywane za pomocą opcji `--min-rate <liczba>` i `--max-rate <liczba>`, gdzie `liczba` reprezentuje liczbę pakietów na sekundę. Przykład:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Opcje te pozwalają dostosować prędkość skanowania do konkretnych potrzeb, aby przyspieszyć proces lub ograniczyć wykorzystywaną przepustowość. Ten drugi przypadek (ograniczenie prędkości skanowania) jest tym, który najprawdopodobniej doprowadzi cię do tych opcji, zwłaszcza jeśli doświadczasz opóźnień sieciowych podczas korzystania z Nmap (co jest dość rzadkie).



### III. Zarządzanie awariami połączeń i limitami czasu



Innym parametrem, którym możemy się bawić, aby zoptymalizować szybkość skanowania Nmap (lub zagwarantować większą dokładność), jest _timeout_ i _retry_.



Dla _timeouts_ jest to **czas braku odpowiedzi**, po którym Nmap przestanie czekać na odpowiedź i uzna usługę lub hosta za nieosiągalnego. Dla _retry_, jest to **liczba kolejnych prób wykonania operacji**, które Nmap wykona przed przejściem dalej.



Podobnie jak w przypadku zrównoleglenia, zarządzanie _timeout_ i _retry_ może być zastosowane do faz wykrywania hosta lub usługi:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: określa czas rundy Exchange. Ponownie, ten parametr jest obliczany i dostosowywany w locie podczas skanowania. Jest mało prawdopodobne, że będziesz musiał go użyć, ponieważ Nmap oblicza ten czas w locie zgodnie z reakcją sieci.





- `--max-retries <liczba>`: ogranicza liczbę retransmisji pakietów podczas skanowania portów. Domyślnie Nmap może wykonać do 10 ponownych prób dla pojedynczej usługi, zwłaszcza jeśli wykryje opóźnienia lub straty na poziomie sieci, ale w większości przypadków wykonywana jest tylko jedna.





- `--host-timeout <time>`: określa maksymalny czas, jaki Nmap spędzi na hoście dla wszystkich swoich operacji, w tym skanowania portów, wykrywania usług i wszelkich innych operacji związanych z tym hostem. Jeśli ten interwał czasowy zostanie przekroczony bez żadnej odpowiedzi lub **zakończenia operacji**, Nmap porzuci tego hosta bez wyświetlania żadnych wyników na jego temat i przejdzie do następnego na liście. Pozwala to kontrolować maksymalny czas, jaki Nmap spędza na danym hoście, unikając utknięcia na opornych hostach i optymalizując ogólny czas skanowania.




W mojej codziennej pracy używam opcji `--max-retries` i `--host-timeout` do optymalizacji skanowania:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Parametry te zapewniają dodatkową elastyczność w dostosowywaniu zachowania skanowania do określonych potrzeb i warunków sieciowych. Należy jednak zdawać sobie sprawę z ich konsekwencji w zakresie obciążenia skanowanych hostów i potencjalnej utraty dokładności.



### IV. Korzystanie z przygotowanych konfiguracji



Różne opcje, które widzieliśmy w tym rozdziale, mogą być używane indywidualnie lub jako część gotowych konfiguracji oferowanych przez Nmap. Opcja, która umożliwia użycie tych _szablonów_ (szablonów konfiguracji) to `-T <numer>` lub `-T <nazwa>`. Dostępnych jest 5 poziomów _szablonów_:



```
-T<0-5>: Set timing template (higher is faster)
```



Domyślnie Nmap używa _template_ 3 (_normal_), co jest ogólnie wystarczające.



Z mojej strony, zazwyczaj działam w kontekstach, w których muszę być dość szybki (pozostając tak kompletnym, jak to tylko możliwe) i często używam opcji `-T4`.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Oto, co pokazują nam informacje debugowania dla tego skanowania:



![nmap-image](assets/fr/64.webp)



użycie konfiguracji `-T4` podczas skanowania Nmap



### V. Wnioski



W tym rozdziale przyjrzeliśmy się różnym technikom i opcjom, których można użyć do zarządzania mocą, agresywnością i wydajnością Nmapa. Opcje te są szczególnie przydatne podczas skanowania dużych sieci, a rzadziej do celów ukrycia.



W następnym rozdziale przyjrzymy się kilku najlepszym praktykom korzystania z Nmapa i zapewniania jego bezpieczeństwa.




## 12 - Bezpieczeństwo i poufność danych podczas korzystania z Nmap



### I. Prezentacja



W tym rozdziale przyjrzymy się kilku dobrym praktykom, które należy przyjąć w odniesieniu do bezpieczeństwa, a przede wszystkim poufności danych generowanych, przetwarzanych i przechowywanych przez Nmap.



Użycie Nmapa w systemie informatycznym może być szybko zakwalifikowane jako działanie ofensywne. W związku z tym należy podjąć szereg środków ostrożności, aby działać w ramach prawnych, jednocześnie gwarantując bezpieczeństwo zamierzonych celów, zebranych danych i systemu używanego do skanowania.



### II. Uzyskanie odpowiednich zezwoleń



Przed skanowaniem sieci lub systemu upewnij się, że uzyskałeś odpowiednie uprawnienia. Skanowanie systemów w poszukiwaniu luk (`skrypty NSE`) bez autoryzacji może być nielegalne i może mieć konsekwencje prawne, zwłaszcza jeśli bezpieczeństwo systemu informatycznego nie jest częścią twoich oficjalnych kompetencji.





- Dla przypomnienia: [Kodeks karny: Rozdział III: Ataki na systemy automatycznego przetwarzania danych](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Ochrona wrażliwych danych



Wyniki uzyskane przez Nmap można uznać za wrażliwe, zwłaszcza gdy zawierają informacje o słabych punktach systemu informatycznego, które mogą zostać wykorzystane przez atakującego. Ale także wtedy, gdy dotyczą systemów, które nie są dostępne dla wszystkich (np. wrażliwych, przemysłowych, opieki zdrowotnej lub [zapasowych] systemów informatycznych (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



Zauważyliśmy również, że w zależności od użytych skryptów NSE, wyniki skanowania NSE [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) mogą również zawierać identyfikatory.



W ten sposób złośliwa osoba, która zdoła uzyskać dostęp do tych wyników skanowania, będzie miała pod ręką mapę systemu informatycznego i bogactwo informacji technicznych, bez samodzielnego wykonywania tych działań, ryzykując wykrycie.



Dlatego ważne jest, aby uważać, aby nie gromadzić ani nie przechowywać poufnych informacji podczas korzystania z Nmap, w tym między innymi następujących:





- Szyfrowanie danych wyjściowych: jeśli konieczne jest przechowywanie lub przesyłanie wyników skanowania Nmap, należy je zaszyfrować w celu ochrony poufności danych. Zapobiegnie to nieautoryzowanemu przechwyceniu poufnych informacji. Najlepiej, jeśli dane zostaną zaszyfrowane, gdy tylko opuszczą system używany do wykonania skanowania (archiwum ZIP zaszyfrowane silnym hasłem to bardzo dobry początek).





- Skonfiguruj kontrolę dostępu: upewnij się, że tylko upoważnione osoby mają dostęp do wyników skanowania Nmap, gdzie będą one przechowywane. Skonfiguruj odpowiednią kontrolę dostępu, aby chronić poufne informacje przed nieautoryzowanym dostępem.





- Czujność podczas obsługi danych: podczas przesyłania, kopiowania lub przetwarzania danych skanowania, należy upewnić się, że bezpieczeństwo danych jest pod ścisłą kontrolą. Oznacza to: nie zostawiaj ich leżących w katalogu `Download` stacji roboczej podłączonej do Internetu, nie pozwól im przechodzić przez wewnętrzną aplikację HTTP Exchange, nie zostawiaj otwartego Notatnika bez zablokowania stacji roboczej podczas przerwy na lunch itp.




### IV. Zarządzanie agresywnymi skanami



Jak widzieliśmy w tym samouczku, Nmap może być bardzo gadatliwy na poziomie sieci. Może również wysyłać pakiety, które nie są odpowiednio sformatowane i które nie przestrzegają ściśle struktury protokołu w ramkach sieciowych i pakietach, które generuje. Wszystkie te działania mogą mieć wpływ na niektóre systemy i usługi, czasami nawet powodując awarię lub nasycenie zasobów systemowych i sieciowych.



Aby uniknąć jakichkolwiek incydentów, musisz opanować zachowanie Nmapa i wiedzieć, jak dostosować go do kontekstu, w którym jest używany, za pomocą różnych opcji omówionych w tym samouczku. Niekoniecznie będziemy używać Nmapa w taki sam sposób w systemie informatycznym zawierającym [sprzęt] przemysłowy (https://www.it-connect.fr/actualites/actu-materiel/), jak w sieci użytkownika składającej się z systemów Windows chronionych przez lokalny firewall lub w rdzeniu sieci.



Mamy nadzieję, że różne lekcje w tym samouczku nauczyły cię, jak opanować i analizować zachowanie Nmapa, ale najlepszym sposobem na naukę jest działanie. Upewnij się więc, że jesteś zaznajomiony z opcjami Nmap, których będziesz używać.



### V. Ochrona systemu skanowania



W pierwszym rozdziale zauważyliśmy, że w większości przypadków Nmap musi być uruchamiany jako `root` lub lokalny administrator. Wynika to z faktu, że wykonuje on operacje sieciowe, czasami na dość niskim poziomie, za pośrednictwem bibliotek sieciowych, które wymagają wysokich i ryzykownych uprawnień z punktu widzenia stabilności systemu lub poufności innych aplikacji.



W rezultacie Nmap może być postrzegany jako wrażliwy komponent systemu, na którym jest zainstalowany. Upewnij się, że używasz najnowszej wersji Nmap, ponieważ starsze wersje mogą zawierać znane luki w zabezpieczeniach. Korzystając z aktualnej wersji, można zminimalizować ryzyko związane z korzystaniem z narzędzia.



Jeśli zdecydowałeś się używać Nmapa nie poprzez sesję jako `root`, ale poprzez przyznanie określonych uprawnień uprzywilejowanemu użytkownikowi, tak aby miał wszystko, czego potrzebuje do korzystania z Nmapa (`sudo` lub _capabilities_), pamiętaj, że Nmap może być używany jako część pełnego podniesienia uprawnień:



![nmap-image](assets/fr/65.webp)



podniesienie uprawnień Nmap poprzez `sudo`._



Tutaj używam polecenia Nmap poprzez `sudo`, ale to pozwala mi uzyskać interaktywną powłokę jako `root` w systemie, co nie było pierwotnym celem.



Wysoce niewskazane jest również instalowanie Nmapa na systemach, które nie są przeznaczone do skanowania sieci. Mam tu na myśli w szczególności serwery lub stacje robocze. Z jednej strony dodałoby to potencjalny wektor do podniesienia uprawnień, ale przede wszystkim dałoby atakującemu łatwy dostęp do narzędzia ofensywnego.



Wreszcie, bezpieczeństwo systemu używanego do skanowania musi być zapewnione w szerszym zakresie, aby sam nie stał się wektorem włamania lub wycieku informacji. Jako administrator systemu lepiej jest używać dedykowanego systemu, najlepiej o ograniczonej żywotności, niż własnej stacji roboczej.



### VI. Wnioski



Podsumowując, upewnij się, że prawidłowo opanowałeś Nmap przed użyciem go w warunkach rzeczywistych lub produkcyjnych i zachowaj czujność podczas przetwarzania i zarządzania jego wynikami. Szkoda byłoby spowodować szkody, wyciek danych lub ułatwić kompromitację, gdy początkowe podejście ma na celu poprawę bezpieczeństwa firmy.



## 13 - Skanowanie portów przez TCP: SYN, Connect i FIN



### I. Prezentacja



W tym i następnym rozdziale przyjrzymy się bliżej różnym typom skanowania TCP dostępnym w Nmapie, zaczynając od tych najczęściej używanych: SYN, Connect i FIN.



Jak zapewne zauważyłeś, Nmap oferuje kilka opcji skanowania TCP:



![nmap-image](assets/fr/66.webp)



techniki skanowania dostępne w Nmap._



Pomysł polega na wyjaśnieniu niektórych z tych metod, aby pomóc zrozumieć ich różnice, zalety i ograniczenia. Przekonasz się, że w zależności od kontekstu lub tego, co chcesz wiedzieć, lepiej jest wybrać jedną lub drugą opcję.



### II. Skanowanie TCP SYN lub "skanowanie półotwarte



Pierwszym typem skanowania TCP, któremu się przyjrzymy, jest `TCP SYN Scan`, znany również jako `Half Open Scan`. Jeśli pamiętasz skanowanie sieci, które wykonaliśmy po naszym pierwszym skanowaniu portów, jest to typ skanowania używany domyślnie przez [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/), gdy jest uruchamiany z prawami roota.



Tłumaczenie pomoże ci zrozumieć, jak działa to skanowanie. W rzeczywistości skanowanie TCP SYN wysyła pakiet TCP SYN do każdego docelowego portu, który jest pierwszym pakietem wysyłanym przez klienta (żądającego nawiązania połączenia) w ramach słynnego _Three way handshake_ TCP. Zwykle, jeśli port jest otwarty na serwerze docelowym, z uruchomioną za nim usługą, serwer odeśle pakiet TCP SYN/ACK w celu sprawdzenia poprawności SYN klienta i zainicjowania połączenia TCP. Ta odpowiedź ma postać pakietu TCP z flagami SYN i ACK ustawionymi na 1, co pozwala nam potwierdzić, że port jest otwarty i prowadzi do usługi.



Z drugiej strony, jeśli port jest zamknięty, serwer wyśle nam pakiet `TCP` z flagami RST i ACK ustawionymi na 1, aby zakończyć żądanie połączenia, więc będziemy wiedzieć, że żadna usługa nie wydaje się być aktywna za tym portem:



![nmap-image](assets/fr/67.webp)



diagram zachowania tCP SYN Scan dla otwartych i zamkniętych portów



Aby uzyskać bardziej konkretny obraz `TCP SYN Scan`, wykonałem skanowanie portu TCP/80 do hosta, który miał aktywny serwer WWW na tym porcie. Przeprowadzając skanowanie sieci za pomocą Wiresharka, możemy zobaczyć następujący przepływ (źródło skanowania: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



przechwytywanie sieci podczas skanowania TCP SYN dla otwartego portu



W pierwszym wierszu widzimy, że źródło skanowania wysyła pakiet TCP do hosta `10.10.10.203` na porcie TCP/80. W tym pakiecie TCP flaga SYN jest ustawiona na 1, aby wskazać, że jest to żądanie inicjalizacji połączenia TCP.



Następnie w drugiej linii widzimy, że cel odpowiada `TCP SYN/ACK`, co oznacza, że akceptuje zainicjowanie połączenia, a tym samym odbieranie strumieni na porcie TCP/80. Możemy zatem wywnioskować, że port TCP/80 jest otwarty i że serwer WWW jest obecny na skanowanym serwerze.



Nasz host odsyła następnie pakiet RST w celu zamknięcia połączenia, pozwalając skanowanemu hostowi nie utrzymywać otwartego połączenia TCP w oczekiwaniu na odpowiedź. W przypadku skanowania na wielu portach, niezamykanie połączeń TCP może prowadzić do odmowy usługi, nasycając liczbę połączeń oczekujących na odpowiedź, które serwer może utrzymać (patrz [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



W Wireshark można zobaczyć status flag TCP dla każdego testu, który wykonujemy. Pokaże to, czy pakiet jest pakietem SYN, SYN/ACK, ACK itp:



![nmap-image](assets/fr/69.webp)



wyświetlanie flag TCP pakietu w Wireshark (tutaj TCP SYN)



I odwrotnie, przeprowadziłem ten sam test między dwoma maszynami, ale tym razem skanując port TCP/81, na którym nie jest aktywna żadna usługa (źródło skanowania: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



przechwytywanie sieci podczas skanowania TCP SYN dla zamkniętego portu



Skanowany host zwraca `TCP RST/ACK` w odpowiedzi na mój `TCP SYN`, gdy port nie jest otwarty.



Jak wspomniano, podczas uruchamiania Nmapa z uprzywilejowanego terminala, skanowanie TCP SYN jest trybem domyślnym i może być wymuszone za pomocą opcji `-sS` (`scan SYN`):



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




Skanowanie TCP SYN jest najczęściej używane ze względu na szybkość. Z drugiej strony, brak sfinalizowania przez klienta _Three Way Handshake_ (tj. brak wysłania ACK po SYN/ACK serwera) może wydawać się podejrzany, jeśli jest obserwowany zbyt wiele razy na serwerze lub z tego samego źródła w sieci. Rzeczywiście, normalnym zachowaniem klienta po otrzymaniu pakietu TCP SYN/ACK w odpowiedzi na TCP SYN jest wysłanie `potwierdzenia` (ACK), a następnie rozpoczęcie Exchange.



Niemniej jednak, zapewnia nieco szybsze skanowanie, ponieważ nie zawraca sobie głowy wysyłaniem ACK dla każdej pozytywnej odpowiedzi. Zaletą SYN Scan jest jego szybkość, ponieważ tylko jeden pakiet jest wysyłany na skanowany port, kosztem większej szansy na wykrycie.



Ponadto skanowanie TCP SYN jest w stanie wykryć, czy port jest filtrowany (chroniony) przez zaporę sieciową. W rzeczywistości firewall przed hostem docelowym można wykryć po sposobie, w jaki zachowuje się, gdy odbiera pakiet TCP SYN na porcie, który ma chronić. Po prostu nie odpowie. Jednak, jak widzieliśmy, w obu przypadkach (otwarty lub zamknięty port) istnieje odpowiedź ze strony hosta. To trzecie zachowanie ujawni obecność zapory sieciowej między skanowanym hostem a maszyną uruchamiającą skanowanie. Oto wynik, jaki Nmap może zwrócić, gdy skanowany port jest filtrowany przez zaporę sieciową:



![nmap-image](assets/fr/71.webp)



wyświetlanie nmap podczas skanowania filtrowanego portu



Kiedy wykonujemy przechwytywanie sieci w czasie skanowania, widzimy, że nie otrzymujemy żadnej odpowiedzi:



![nmap-image](assets/fr/72.webp)



przechwytywanie sieci podczas skanowania TCP SYN dla portu filtrowanego przez zaporę sieciową



Różnica między portem zamkniętym a portem filtrowanym jest następująca: port filtrowany to port chroniony przez zaporę sieciową, podczas gdy port zamknięty to port, na którym nie działa żadna usługa i który w związku z tym nie jest w stanie przetwarzać naszych pakietów TCP. Niektóre typy skanowania TCP, takie jak skanowanie TCP SYN, są w stanie wykryć, czy port jest filtrowany, podczas gdy inne typy skanowania tego nie potrafią.



### III. Skanowanie TCP Connect lub skanowanie Full Open



Drugim typem skanowania TCP jest skanowanie `TCP Connect`, znane również jako _Full Open Scan_. Działa w taki sam sposób jak skanowanie TCP SYN, ale tym razem zwraca `TCP ACK` po pozytywnej odpowiedzi z serwera (SYN/ACK). Właśnie dlatego nazywa się "Full Open", ponieważ połączenie jest w pełni otwarte i zainicjowane na każdym porcie otwartym podczas skanowania, przestrzegając w ten sposób TCP _Three Way Handshake_:



![nmap-image](assets/fr/73.webp)



diagram zachowania tCP Connect Scan dla otwartych i zamkniętych portów



Oto, co można zobaczyć w sieci podczas skanowania `TCP Connect` na otwartym porcie:



![nmap-image](assets/fr/74.webp)



podsłuchiwanie sieci podczas skanowania TCP Connect w poszukiwaniu otwartego portu



Widzimy, że pierwszym wysłanym pakietem TCP jest `TCP SYN` wysłany przez klienta, a serwer odpowie `TCP SYN/ACK`, wskazując, że port jest otwarty i hostuje aktywną usługę. Aby zasymulować legalnego klienta, Nmap wyśle następnie `TCP ACK` z powrotem do serwera. I odwrotnie, podczas skanowania zamkniętego portu:



![nmap-image](assets/fr/75.webp)



przechwytywanie sieci podczas skanowania TCP Connect dla zamkniętego portu



Zauważ, że odpowiedzią serwera na nasz pakiet `SYN` jest ponownie pakiet `TCP RST/ACK`, więc możemy wywnioskować, że port jest zamknięty i nie działają na nim żadne usługi.



Podczas korzystania z Nmap, opcja `-sT` (`scan Connect`) jest używana do wykonania skanowania TCP Connect. Należy pamiętać, że gdy Nmap jest używany z nieuprzywilejowanej sesji, jest to domyślny tryb skanowania TCP:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



Skanowanie `TCP Connect Scan` symuluje bardziej uzasadnione żądanie połączenia, z zachowaniem, które najbardziej przypomina zachowanie klienta lambda, więc trudniej jest wykryć skanowanie na zmniejszonej liczbie portów. Jest jednak wolniejsze, ponieważ całkowicie inicjalizuje każde połączenie TCP na otwartych portach skanowanej maszyny.



Skanowanie Nmapem 10 000 portów będzie nadal łatwe do wykrycia, jeśli zainstalowane są sieciowe usługi wykrywania i ochrony przed włamaniami (IDS, IPS, EDR). Gdy atakujący chce zachować niski profil, będzie miał tendencję do skupiania się na niewielkiej liczbie strategicznie wybranych portów, takich jak 445 (SMB) lub 80 (HTTP), które są często otwarte na serwerach i stanowią powszechne luki w zabezpieczeniach.



Ponieważ TCP Connect Scan oczekuje odpowiedzi w obu przypadkach, może również wykryć obecność zapory sieciowej, która może filtrować porty na hoście docelowym.



### IV. Skanowanie TCP FIN lub "Stealth Scan



Funkcja `TCP FIN Scan`, znana również jako _Stealth Scan_, wykorzystuje zachowanie klienta kończącego połączenie TCP w celu wykrycia otwartego portu.



W TCP, koniec sesji oznacza wysłanie pakietu TCP z flagą FIN ustawioną na 1. W normalnym Exchange, serwer przerywa całą komunikację z klientem (brak odpowiedzi). Jeśli serwer nie ma aktywnego połączenia TCP z klientem, wyśle `RST/ACK`. Możemy zatem rozróżnić otwarte i zamknięte porty, wysyłając pakiety `TCP FIN` do zestawu portów:



![nmap-image](assets/fr/76.webp)



diagram zachowania skanowania tCP FIN dla otwartych i zamkniętych portów



Ponownie przechwyciłem sieć podczas skanowania _Stealth_ i oto, co widać, gdy skanowany port jest otwarty:



![nmap-image](assets/fr/77.webp)



przechwytywanie sieci podczas skanowania TCP FIN w poszukiwaniu otwartego portu



Widzimy, że klient wysyła jeden lub dwa pakiety, aby zakończyć połączenie TCP, a serwer nie odpowiada. Po prostu akceptuje zakończenie połączenia i przestaje się komunikować.



Oto, co widzimy teraz podczas skanowania zamkniętego portu:



![nmap-image](assets/fr/78.webp)



przechwytywanie sieci podczas skanowania TCP FIN dla zamkniętego portu



Widzimy, że serwer odsyła pakiet `TCP RST/ACK`, więc istnieje różnica w zachowaniu między otwartym i zamkniętym portem, a my jesteśmy w stanie wyświetlić listę otwartych portów na serwerze, wysyłając pakiet TCP FIN. Używając Nmap, opcja `-sF` (`scan FIN`) jest używana do wykonania skanowania TCP FIN:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN Scan nie działa na hostach Windows, ponieważ system operacyjny ma tendencję do ignorowania pakietów TCP FIN, gdy są one wysyłane na porty, które nie są otwarte. Jeśli więc uruchomisz TCP FIN Scan na hoście z systemem Windows, będziesz mieć wrażenie, że wszystkie porty są zamknięte.



Dlatego ważne jest, aby zapoznać się z kilkoma metodami skanowania i zrozumieć różnicę między nimi.



Ponieważ w obu przypadkach TCP FIN nie będzie czekać na odpowiedź, nie będzie w stanie wykryć obecności zapory ogniowej między hostem docelowym a źródłem skanowania.



Oto przykład wyniku skanowania TCP FIN przez Nmap:



![nmap-image](assets/fr/79.webp)



wyniki skanowania TCP FIN przez Nmap._



W rzeczywistości brak odpowiedzi od hosta na danym porcie może oznaczać, że port jest filtrowany, ale także, że jest otwarty i aktywny.



Skanowanie to jest określane jako "stealth", ponieważ nie generuje dużego ruchu generate i generalnie nie powoduje rejestrowania w docelowych systemach. Może być używane do dyskretnego wykrywania portów w sieci bez podnoszenia jakichkolwiek alarmów. Jednak, jak wspomniano powyżej, jego skuteczność może się różnić w zależności od systemu docelowego, podobnie jak jego dyskrecja w zależności od konfiguracji sprzętu zabezpieczającego.



### V. Wnioski



To tyle, jeśli chodzi o pierwszy z dwóch rozdziałów na temat różnych typów skanowania TCP oferowanych przez Nmap! W następnym rozdziale przyjrzymy się typom skanowania TCP XMAS, Null i ACK, które działają na różne sposoby w celu wykrycia otwartych portów na hoście.





## 14 - Skanowanie portów przez TCP: XMAS, Null i ACK



### I. Prezentacja



W tej sekcji będziemy kontynuować badanie różnych metod skanowania TCP oferowanych przez Nmap. Tutaj przyjrzymy się metodom `XMAS`, `Null` i `ACK`, które wykorzystują specyficzne funkcje TCP do pobierania informacji o portach i usługach otwartych na danym celu.



### II. Skanowanie TCP XMAS



XMAS Scan TCP jest nieco nietypowy, ponieważ w ogóle nie symuluje normalnego zachowania użytkownika lub maszyny w sieci. W rzeczywistości XMAS Scan wysyła pakiety TCP z flagami `URG` (Pilne), `PSH` (Push) i `FIN` (Zakończ) ustawionymi na 1, aby ominąć niektóre zapory ogniowe lub mechanizmy filtrowania.



Nazwa XMAS pochodzi od faktu, że widok tych flag włączonych jest niezwykły. Gdy wszystkie trzy flagi są ustawione jednocześnie w pakiecie TCP, wygląda to jak rozświetlona choinka:



![nmap-image](assets/fr/80.webp)



flagi tCP używane podczas skanowania XMAS



Nie wchodząc tutaj w szczegóły roli tych flag, ważne jest, aby wiedzieć, że wysyłając pakiet z włączonymi tymi trzema flagami, aktywna usługa za portem docelowym nie zwróci żadnych pakietów. Z drugiej strony, jeśli port jest zamknięty, otrzymamy pakiet TCP RST/ACK. Teraz będziemy w stanie rozróżnić zachowanie otwartego i zamkniętego portu podczas wyświetlania listy portów na komputerze:



![nmap-image](assets/fr/81.webp)



diagram zachowania tCP XMAS Scan dla otwartych i zamkniętych portów



Zgodnie z tą samą logiką, skanowanie sieci na porcie TCP/80 hosta z aktywnym serwerem WWW wykazuje następujące zachowanie podczas wykrywania otwartego portu (źródło skanowania `10.10.14.84`):



![nmap-image](assets/fr/82.webp)



przechwytywanie sieci podczas skanowania TCP XMAS w poszukiwaniu otwartego portu



Widzimy, że źródło skanowania wysyła dwa pakiety TCP XMAS (z flagami `FIN`, `PSH` i `URG` ustawionymi na 1) do hosta `10.10.10.203` i że nie ma zwrotu z celu, co wskazuje, że port jest otwarty. I odwrotnie, podczas wykonywania `TCP XMAS Scan` na zamkniętym porcie, obserwowany jest następujący wynik:



![nmap-image](assets/fr/83.webp)



przechwytywanie sieci podczas skanowania TCP XMAS dla zamkniętego portu



Odpowiedzią na nasz pakiet TCP jest wtedy `TCP RST/ACK`, wskazujący, że port jest zamknięty. Aby użyć tej techniki z Nmap, opcja `-sX` (`scan XMAS`) pozwala na wykonanie skanowania TCP XMAS:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



Ważne jest, aby pamiętać, że skanowanie TCP XMAS nie jest w stanie wykryć zapór ogniowych, które mogą znajdować się między celem a maszyną skanującą, w przeciwieństwie do niektórych innych typów skanowania, takich jak TCP SYN lub Connect. W rzeczywistości aktywna zapora sieciowa między dwoma hostami zapewni, że żaden zwrot TCP nie zostanie wykonany, jeśli docelowy port jest filtrowany (tj. chroniony przez zaporę). W przypadku braku odpowiedzi nie można zatem stwierdzić, czy port jest chroniony przez zaporę, czy otwarty i aktywny. Należy również pamiętać, że podobnie jak w przypadku skanowania TCP FIN, niektóre aplikacje lub systemy operacyjne, takie jak Windows, mogą zniekształcać wyniki tego typu skanowania.



uwaga: obsługa skanowania XMAS/FIN/NULL w najnowszych wersjach systemu Windows pozostaje ograniczona, a wyniki mogą być niespójne w przypadku tego typu celu. (Aktualizacja 2025)_



### III. Skanowanie TCP Null



W przeciwieństwie do skanowania TCP XMAS, skanowanie TCP Null będzie wysyłać pakiety skanowania TCP ze wszystkimi flagami ustawionymi na 0. Jest to również zachowanie, które nigdy nie zostanie znalezione w normalnym Exchange między maszynami, ponieważ wysyłanie pakietu TCP bez flagi nie jest określone w RFC opisującym protokół TCP. Dlatego też można to łatwiej wykryć.



Podobnie jak skanowanie TCP XMAS, skanowanie to może zakłócać działanie niektórych zapór sieciowych lub modułów filtrujących, umożliwiając przechodzenie pakietów:



![nmap-image](assets/fr/84.webp)



diagram zachowania tCP Null Scan dla otwartych i zamkniętych portów



Oto, co można zobaczyć w sieci podczas skanowania TCP Null na otwartym porcie:



![nmap-image](assets/fr/85.webp)



przechwytywanie sieci podczas skanowania TCP Null dla otwartego portu



Maszyna skanująca wysyła pakiet bez flagi (`[<None>]` w Wireshark) bez żadnej odpowiedzi z serwera. I odwrotnie, gdy port docelowy jest zamknięty:



![nmap-image](assets/fr/86.webp)



przechwytywanie sieci podczas skanowania TCP Null dla zamkniętego portu



Aby wykonać skanowanie TCP Null za pomocą Nmap, wystarczy użyć opcji `-sN` (`scan Null`):



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Ponieważ odpowiedź, gdy port jest otwarty i gdy firewall jest aktywny (brak informacji zwrotnej od serwera w obu przypadkach) jest identyczna, skanowanie TCP Null nie jest w stanie wykryć obecności firewalla. Co więcej, firewall może nawet zafałszować wynik, sugerując, że port jest otwarty, ponieważ nie odpowiada na pakiety TCP bez flag, nawet jeśli port jest filtrowany. Jest to ważna informacja, której należy być świadomym podczas korzystania ze skanów, które nie są w stanie rozróżnić między portem otwartym a filtrowanym (chronionym przez zaporę), takich jak skany `TCP Null`, `XMAS` lub `FIN`, aby zachować spójność w interpretacji uzyskanych wyników.



### IV. Skanowanie TCP ACK



Skanowanie TCP ACK służy do wykrywania obecności zapory sieciowej na hoście docelowym lub między hostem docelowym a źródłem skanowania.



W przeciwieństwie do innych skanów, skanowanie TCP ACK nie próbuje zidentyfikować, które porty są otwarte na hoście, ale raczej czy system filtrowania jest aktywny, odpowiadając dla każdego portu `filtered` lub `unfiltered`. Niektóre skany TCP, takie jak `TCP SYN` lub `TCP Connect`, mogą wykonywać obie te czynności w tym samym czasie, podczas gdy inne, takie jak `TCP FIN` lub `TCP XMAS`, nie mogą w ogóle określić obecności filtrowania. Właśnie dlatego skanowanie TCP ACK może być przydatne:



![nmap-image](assets/fr/87.webp)



diagram zachowania tCP ACK Scan dla portów filtrowanych i niefiltrowanych



Do wykonania tego typu skanowania użyjemy opcji `-sA` Nmapa. Oto wynik skanowania TCP ACK, jeśli port jest filtrowany, tj. zablokowany i chroniony przez zaporę sieciową:



![nmap-image](assets/fr/88.webp)



wyświetlanie nmap podczas TCP ACK Scan._



Przykładowy wynik dla hosta z firewallem i jednego bez. Nmap zwraca `filtered` na portach TCP/80 i TCP/81 hosta `10.10.10.203`. Analizując sieć za pomocą Wiresharka, zachowanie wygląda następująco:



![nmap-image](assets/fr/89.webp)



przechwytywanie sieci podczas skanowania TCP ACK dla portu niefiltrowanego przez zaporę sieciową



Maszyna docelowa nie zwraca nic, jeśli obecny jest firewall.



Aby uruchomić to skanowanie za pomocą Nmap, użyj opcji `-sA` (`scan ACK`):



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Wnioski



Przyjrzeliśmy się trzem różnym metodom skanowania przez TCP, oprócz tych już przedstawionych. Te różne metody mają być stosowane w bardzo specyficznych warunkach i kontekstach, zwłaszcza w kontekście testów penetracyjnych lub operacji Red Team, podczas których występuje pojęcie dyskrecji.



## 15 - Nmap CheatSheet - Podsumowanie poleceń samouczka



### I. Prezentacja



Oto krótkie podsumowanie wielu poleceń i przypadków użycia Nmapa, dzięki czemu można je szybko znaleźć i ponownie wykorzystać w codziennym użytkowaniu.



### II. Nmap: CheatSheet IT-Connect



Oto ściągawka z prezentowanych poleceń. Ta strona ułatwia znalezienie najczęstszych zastosowań Nmap.





- Skanowanie portów




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Wykrywanie aktywnych hostów




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



uwaga: Opcja `-sP` jest przestarzała od kilku lat i powinna zostać zastąpiona przez `-sn`. (Aktualizacja 2025)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Wykrywanie wersji




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- Skrypty NSE: szukanie luk w zabezpieczeniach




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Zarządzanie danymi wyjściowymi Nmap




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Optymalizacja wydajności




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- Typy skanowania TCP




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Mam nadzieję, że te polecenia okażą się przydatne. Nie zapomnij dostosować celu skanowania do kontekstu i zapoznać się z oficjalną dokumentacją, aby w pełni opanować wykonywane testy.



### III. Wnioski



Samouczek Nmap został ukończony. Masz teraz podstawy potrzebne do korzystania z tego wszechstronnego i potężnego narzędzia. Zdecydowanie zalecamy ćwiczenie na kontrolowanych środowiskach (Hack The Box, VulnHub, maszyny wirtualne) przed użyciem go w produkcji.



Wiele pozostaje jeszcze do odkrycia na temat wewnętrznego działania narzędzia i jego zaawansowanych funkcji. Jednak opanowanie przedstawionych tutaj poleceń i pojęć pozwoli ci korzystać z Nmap z pewnością i przydatnością.