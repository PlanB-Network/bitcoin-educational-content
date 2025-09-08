---
name: Angry IP Scanner
description: Prosty sposób na skanowanie sieci
---
![cover](assets/cover.webp)



___



*Ten samouczek jest oparty na oryginalnej treści autorstwa Floriana BURNELA opublikowanej na stronie [IT-Connect](https://www.it-connect.fr/). Licencja [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). W oryginalnym tekście mogły zostać wprowadzone zmiany



___



## I. Prezentacja



Jak szybko i łatwo przeskanować sieć Windows w poszukiwaniu podłączonych maszyn? Odpowiedzią jest Angry IP Scanner. Ten projekt open source umożliwia łatwe skanowanie sieci za pomocą łatwego w użyciu graficznego Interface.



Narzędzie to może być używane przez osoby prywatne do **skanowania sieci lokalnej**, ale także przez profesjonalistów IT w tym samym celu. Dowodem na to, że **narzędzie to jest bardzo praktyczne**, jest fakt, że zostało ono już wykorzystane przez **niektóre grupy cyberprzestępcze** do skanowania sieci korporacyjnych (w taki sam sposób jak Nmap). Dobrym przykładem jest [grupa ransomware RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Nadal jest to solidne oprogramowanie, ale podobnie jak w przypadku innych narzędzi sieciowych i zorientowanych na bezpieczeństwo, jego użycie może być nadużywane.



Tutaj będziemy używać go na **Windows 11**, ale jest to całkowicie możliwe na innych wersjach **Windows**, a także na **Linux** i **macOS**.



Mniej wszechstronny niż Nmap, **Angry IP** Scanner jest nadal interesujący do szybkiej, podstawowej analizy sieci, ale także dlatego, że jest w zasięgu każdego. Program **wykrywa hosty podłączone do sieci** i identyfikuje **nazwy hostów** i **otwarte porty**.



Jeśli chcesz dowiedzieć się więcej, zapoznaj się z samouczkiem na temat Nmap:



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Rozpoczęcie pracy z Angry IP Scanner



### A. Pobierz i zainstaluj Angry IP Scanner



Najnowszą wersję Angry IP Scanner można pobrać z oficjalnej strony aplikacji lub z GitHub. My skorzystamy z tej drugiej opcji. Kliknij poniższy link i pobierz wersję EXE: "**ipscan-3.9.1-setup.exe**".





- [Angry IP Scanner GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Uruchom plik wykonywalny, aby kontynuować instalację. Nie ma nic specjalnego do zrobienia podczas instalacji.



![Image](assets/fr/013.webp)



### B. Uruchom wstępne skanowanie sieci



Przy pierwszym uruchomieniu należy zapoznać się z instrukcjami w oknie "**Getting Started**", aby dowiedzieć się więcej o działaniu narzędzia. Nawiasem mówiąc, należy wziąć pod uwagę kilka terminów:





- Feeder**: moduł odpowiedzialny za generowanie list adresów IP do skanowania, z losowego zakresu IP lub pliku z listą adresów IP.
- Fetcher**: zestaw modułów do pobierania informacji o hostach w sieci. Istnieją na przykład pobieracze do wykrywania adresów MAC, skanowania portów, wykrywania nazw hostów lub wysyłania żądań HTTP.



![Image](assets/fr/018.webp)



Aby przeskanować podsieć IP, po prostu wprowadź **początkowy adres IP Address** i **końcowy adres IP Address** w polu "**zakres IP**" (w przeciwnym razie zmień typ po prawej stronie). Następnie kliknij przycisk "**Start**".



![Image](assets/fr/019.webp)



Kilkadziesiąt sekund później wynik będzie widoczny w Interface oprogramowania. **Dla każdego IP Address w analizowanym zakresie pojawi się informacja, czy Angry IP Scanner wykrył hosta, czy nie.** Na ekranie pojawi się również podsumowanie, wskazujące liczbę aktywnych hostów (w tym przypadku 6) i liczbę hostów z otwartymi portami.



![Image](assets/fr/020.webp)



Tutaj widzimy obecność hosta o nazwie "**OPNsense.local.domain**", powiązanego z IP Address "**192.168.10.1**" i dostępnego na **portach 80** i **443** (HTTP i HTTPS). Kliknięcie hosta prawym przyciskiem myszy daje dostęp do dodatkowych poleceń, takich jak pingowanie, śledzenie trasy i otwieranie przeglądarki za pośrednictwem tego IP Address.



![Image](assets/fr/012.webp)



### C. Dodaj porty skanowania



Domyślnie **Angry IP Scanner** skanuje 3 porty: **80** (HTTP), **443** (HTTPS) i **8080**. Możesz dodać więcej portów do skanowania w preferencjach aplikacji. Kliknij menu "**Narzędzia**", a następnie zakładkę "**Porty**".



Tutaj można zmodyfikować listę portów za pomocą opcji "**Wybór portu**". Możesz **wskazać konkretne numery portów oddzielone przecinkiem lub zakresy portów**. Poniższy przykład dodaje dwa porty: **445** (SMB) i **389** (LDAP). Aby przeskanować porty od 1 do 1000, wpisz "**1-1000**". Nie jest określone, czy skanowanie portów jest wykonywane w protokole TCP, UDP lub obu.



![Image](assets/fr/021.webp)



Jeśli uruchomisz skanowanie ponownie, prawdopodobnie uzyskasz nowe informacje. W poniższym przykładzie Angry IP Scanner informuje mnie, że porty 389 i 445 są otwarte na hostach "**SRV-ADDS-01**" i "**SRV-ADDS-02**", dzięki nowej konfiguracji portów do skanowania.



![Image](assets/fr/022.webp)



**Uwaga**: z menu "**Skaner**" można wyeksportować wyniki skanowania do pliku tekstowego.



Jeśli chcesz kontynuować skanowanie, kliknij menu "**Narzędzia**", a następnie kliknij "**Pobieracze**". Spowoduje to dodanie "możliwości" do skanowania. Wystarczy wybrać fetchera i przesunąć go w lewo, aby go aktywować. Spowoduje to dodanie dodatkowej kolumny do wyniku skanowania.



![Image](assets/fr/014.webp)



Poniższy przykład pokazuje funkcje "**NetBIOS info**" i "**Web detection**". Pierwsza z nich dostarcza dodatkowych informacji, takich jak MAC Address i nazwa domeny komputera, podczas gdy druga wyświetla tytuł strony internetowej (co może wskazywać na typ serwera WWW lub aplikacji).



![Image](assets/fr/011.webp)



Wreszcie, w preferencjach można również zmienić metodę używaną do "**ping**", tj. do sprawdzenia, czy host jest aktywny, czy nie. Ponieważ niektóre hosty nie odpowiadają na pingi, pozwala to wypróbować inne metody (pakiet UDP, sonda portu TCP, ARP, kombinacja UDP + TCP itp.)



## III. Wnioski



Prosty i skuteczny: Angry IP Scanner wykrywa hosty podłączone do sieci i pozwala skonfigurować skanowanie portów. Pod względem opcji nie jest tak elastyczny jak Nmap i nie posuwa się tak daleko, ale jest dobrym początkiem do szybkiego skanowania.



Jeśli chcesz używać **Nmap** z graficznym Interface, możesz użyć **aplikacji Zenmap** (zobacz przegląd poniżej).



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d