---
name: LN VPN

description: Konfiguracja sieci VPN
---

![image](assets/cover.webp)


LN VPN to konfigurowalna usługa VPN, która akceptuje tylko błyskawiczne płatności. Dziś pokażę ci, jak z niej korzystać i pozostawiać mniej śladów podczas przeglądania Internetu.


Istnieje wielu wysokiej jakości dostawców usług VPN, a my przeprowadziliśmy kompleksową recenzję w tym artykule (hiperłącze). Jednak LN VPN wyróżnia się i nie mogliśmy przegapić okazji, aby go przedstawić.


Większość dostawców usług VPN, takich jak ProtonVPN i Mullvad, oferuje opcję płatności bitcoinami, ale wymaga utworzenia konta i wykupienia planu na dłuższy lub krótszy okres, co może nie pasować do budżetu każdego.


LN VPN umożliwia korzystanie z VPN na żądanie nawet przez godzinę, dzięki implementacji płatności Bitcoin za pośrednictwem Lightning Network. Natychmiastowe i anonimowe płatności błyskawiczne otwierają świat możliwości dla mikropłatności.


Uwaga💡: **Niniejszy przewodnik opisuje sposób korzystania z LN VPN z poziomu systemu Linux Ubuntu 22.04 LTS


## Wymagania wstępne: Wireguard


Mówiąc prościej, Wireguard służy do tworzenia bezpiecznego tunelu między komputerem a zdalnym serwerem, przez który będziesz przeglądać Internet. To właśnie adres IP Address tego serwera będzie wyświetlany jako twój na czas trwania dzierżawy Contract, postępując zgodnie z tym przewodnikiem.


Oficjalna instrukcja instalacji Wireguard: https://www.wireguard.com/install/


```
Wireguard installation
$ sudo apt-get update
$ sudo apt install wireguard
```


## Wymagania wstępne: Błyskawica Bitcoin Wallet


Jeśli nie masz jeszcze Lightning Bitcoin Wallet, nie martw się, stworzyliśmy dla ciebie bardzo prosty przewodnik tutaj. (sekcja samouczka LN może ci pomóc)


## Krok 1: Contract leasing


Na stronie https://lnvpn.com należy wybrać kraj wyjściowego adresu IP tunelu VPN oraz czas trwania. Po ustawieniu tych parametrów kliknij przycisk Zapłać błyskawicą.


![image](assets/1.webp)


Zostanie wyświetlona błyskawica Invoice, którą wystarczy zeskanować za pomocą błyskawicy Wallet.


Po opłaceniu Invoice będziesz musiał poczekać od kilku sekund do dwóch minut na wygenerowanie ustawień konfiguracji Wireguard. Jeśli potrwa to trochę dłużej, nie panikuj, wykonaliśmy tę procedurę dziesiątki razy i czasami trwa to trochę dłużej.

Poniższy tekst został przetłumaczony na język angielski z zachowaniem tego samego układu markdown, co tekst oryginalny:


Pojawi się następny ekran i wystarczy kliknąć "Pobierz jako plik", aby otrzymać plik konfiguracyjny, który będzie miał nazwę wyglądającą jak lnvpn-xx-xx.conf, gdzie "xx" odpowiada bieżącej dacie.

![image](assets/2.webp)


## Krok 2: Aktywacja tunelu


Najpierw należy zmienić nazwę pliku konfiguracyjnego uzyskanego w poprzednim kroku, aby mógł on zostać automatycznie rozpoznany przez Wireguard.


Przejdź do folderu pobierania w oknie terminala lub eksploratora plików i zmień nazwę pliku lnvpn-xx-xx.conf na wg0.conf w następujący sposób:


```
$ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
$ sudo wg-quick up ~/Downloads/wg0.conf
```


Proszę bardzo! Tunel został aktywowany!


## Krok 3: Weryfikacja


Skorzystaj z usługi online, takiej jak whatismyip, aby sprawdzić, czy Twój publiczny adres IP Address jest teraz tym z właśnie aktywowanej sieci VPN.


## Krok 4: Wyłącz


Po wygaśnięciu dzierżawy należy wyłączyć połączenie, aby odzyskać dostęp do Internetu. Następnie możesz powtórzyć kroki od 1 do 3 za każdym razem, gdy chcesz ustanowić dzierżawę z LN VPN.


Wyłączenie tunelu:


```
$ sudo ip link delete dev wg0
```


I gotowe! Teraz już wiesz, jak korzystać z LN VPN, unikalnej usługi VPN!