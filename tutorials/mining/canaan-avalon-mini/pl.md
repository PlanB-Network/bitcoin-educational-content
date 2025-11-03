---
name: Canaan Avalon Mini 3
description: Konfiguracja ASIC Avalon do solominingu lub Miner pooling
---

![cover](assets/cover.webp)



W tym samouczku przyjrzymy się, jak skonfigurować Canaan Avalon Mini 3, aby ułatwić korzystanie z Miner w domu.



Do tej pory maszyny ASIC (*Application Specific Integrated Circuit*) zaprojektowane specjalnie do wykonywania określonego zadania - w tym przypadku obliczania Hash (SHA-256) dla Miner z Bitcoin - były szczególnie nieodpowiednie do użytku domowego. Uciążliwy hałas, generowane ciepło i konieczność dostosowania instalacji elektrycznej do obsługi ogromnej mocy tych urządzeń powstrzymywały większość z nas przed wzięciem w nich udziału.



Obecnie Canaan, jeden z wiodących producentów maszyn ASIC, postanowił zająć się rynkiem osób prywatnych, które chcą mieć Miner w domu, oferując gamę produktów, które są stosunkowo ciche i bardzo łatwe w instalacji (plug & play).



Urządzenia te są sprzedawane albo jako dodatkowy grzejnik w przypadku **Avalon Nano 3S (140W)**, albo jako mini grzejnik o mocy wyjściowej **800W** w przypadku **Avalon Mini 3**.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

Należy pamiętać, że różnica w cenie w porównaniu z tradycyjnymi grzejnikami o równoważnej mocy w zdecydowanej większości przypadków nie pozwala na osiągnięcie zysku finansowego. Satoshi generowane przez Mining nigdy nie zrekompensują tej różnicy w cenie, chyba że masz dostęp do darmowej (nadwyżki) lub bardzo taniej energii elektrycznej.



Moim zdaniem urządzenia te powinny być postrzegane bardziej jako prosty sposób na Miner w domu dla tych, którzy chcą to zrobić z powodów osobistych: *uzyskać nie-KYC Satss / zagrać w "loterię" poprzez solominację / uczestniczyć w decentralizacji Hashrate etc.*., jednocześnie czerpiąc korzyści **jako bonus** z generowanego ciepła do ogrzania swojego pokoju w zimie. Ale nie jako sposób na oszczędzanie pieniędzy przynajmniej w większości przypadków (kraje zachodnie).



## Unboxing i funkcje



### Avalon Nano 3S



Najpierw zobaczmy, co znajduje się w pudełku Avalon Mini 3.



![image](assets/fr/24.webp)



Po otwarciu pudełka instrukcja obsługi znajduje się bezpośrednio przed tobą, ale co ważniejsze, moduł odbiornika WIFI jest ukryty pod okrągłą białą naklejką po lewej stronie instrukcji obsługi. Będzie on potrzebny później.



![image](assets/fr/25.webp)



Poniżej bloku pianki znajduje się urządzenie, a po wyjęciu z pudełka, jednostka zasilająca Supply.



![image](assets/fr/26.webp)




![image](assets/fr/27.webp)



## Włączanie zasilania i łączenie z siecią lokalną



Po rozpakowaniu, umieść Avalon Mini 3 w stosunkowo otwartym miejscu, jeśli to możliwe, aby umożliwić prawidłową cyrkulację ciepła. Następnie zacznij od włożenia małego modułu odbiornika WIFI do portu USB na spodzie urządzenia, podłączając zasilanie Supply i upewniając się, że przycisk zasilania znajduje się w pozycji "1".



![image](assets/fr/28.webp)



Po wykonaniu tych czynności, wyświetlacz LED urządzenia zaświeci się i pokaże symbol "Bluetooth", wskazując, że urządzenie jest gotowe do połączenia z siecią lokalną za pośrednictwem aplikacji Avalon Family.



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Aby to zrobić, przejdź do sklepu z aplikacjami mobilnymi, wyszukaj i pobierz aplikację **Avalon Family**.



![image](assets/fr/11.webp)


Po zainstalowaniu, otwórz ją klikając na "Skip" w prawym górnym rogu, następnie na przycisk "Add" i na końcu na "Search". Upewnij się, że masz włączony Bluetooth na swoim smartfonie, aby wykrywanie urządzenia przebiegało płynnie.



![image](assets/fr/12.webp)


Po wykryciu urządzenia przez aplikację, kliknij na nie i wybierz "Połącz". Następnie zostaniesz przeniesiony do ekranu, na którym możesz wprowadzić szczegóły połączenia WIFI.


![image](assets/fr/13.webp)


Po podłączeniu do sieci lokalnej, Mini 3 wyświetli informacje takie jak IP Address, czas, Hashrate i zasilanie elektryczne.



Poniżej znajduje się tabela podsumowująca ogólną specyfikację techniczną Mini 3:



| Caractéristique                                      | Valeur                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Consommation électrique                              | 800 W                                                     |
| Bruit                                                | 35-55 dB                                                  |
| Température de l'air en sortie                       | 60-70°C (sous température ambiante 25°C)                  |
| Exigences de température ambiante pour l'utilisation | -5° C - 40°C                                              |
| Plage d'entrée de l'appareil                         | 110V-240V AC 50/60Hz                                      |
| Taille de la machine                                 | Longueur: 760 mm / Profondeur: 104 mm / Hauteur: 214.5 mm |
| Poids de la machine                                  |  8.35 kg                                                  |

## Podłączanie do Mining pool



**Ta część jest wspólna dla urządzeń Nano 3s i Mini 3, ponieważ procesy są ściśle identyczne **



Niezależnie od tego, czy chcemy "solominować", czy "poolować" Miner, będziemy musieli połączyć się z Mining pool. W rzeczywistości nasze urządzenie to nic innego jak Hash-maker bez świadomości sieci Bitcoin. Podłączenie go do puli daje mu dostęp do sieci Bitcoin i pozwala na otrzymywanie szablonów bloków do pracy.



### Korzystanie z aplikacji do łączenia się z Mining pool



W aplikacji Avalon Family wybierz urządzenie, jak pokazano poniżej. Zostaniesz automatycznie poproszony o zmianę hasła administratora urządzenia. Kliknij "OK", jeśli chcesz to zrobić, lub "Anuluj", aby pozostawić domyślne hasło dostępu "admin".


![image](assets/fr/16.webp)


Następnie wybierz "Settings", a następnie "Pool Config" i wprowadź parametry dla 3 żądanych pul.


Pule #2 i #3 będą działać jako kopie zapasowe w przypadku awarii jednej z nich, dzięki czemu Miner nie będzie działać na darmo. Domyślnie Hashrate będzie wskazywał na pulę #1



W naszym przypadku wybieramy:




- 1 - Basen publiczny,
- 2 - CkPool,
- 3 - Ocean.



![image](assets/fr/17.webp)



Aby uzyskać więcej informacji na temat łączenia się z Mining pool, zapoznaj się z tymi samouczkami:



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

Podsumowując, potrzebujemy





- gW-25 puli, zwykle **stratum+tcp://xxxxxxxx:port**.





- nazwa "pracownika" składająca się z *twojego Bitcoin Address* i *pseudonimu* wybranego dla urządzenia, przy czym te dwa elementy są oddzielone *kropką*, na przykład:**bc1qxxxxxxxxxxxxxxxxx.MonAvalonNano3S**





- hasło, które zwykle jest zawsze "**x**"



Po wprowadzeniu informacji o puli kliknij przycisk "Zapisz".



![image](assets/fr/18.webp)


Uruchom ponownie urządzenie zgodnie z instrukcjami i poczekaj kilka minut, aż urządzenie Hashrate zostanie skierowane na preferowaną pulę (#1).



### Używanie przeglądarki do łączenia się z Mining pool



Można również połączyć się z Mining pool i, bardziej ogólnie, uzyskać dostęp do systemu zarządzania Interface urządzenia za pośrednictwem ulubionej przeglądarki.



Aby to zrobić, wpisz w pasku wyszukiwania przeglądarki adres IP Address urządzenia pokazanego na poniższym ekranie, w naszym przykładzie **192.168.144.6**



![image](assets/fr/15.webp)



Pojawi się następująca strona z prośbą o otwarcie aplikacji Avalon Family i zeskanowanie kodu QR wyświetlanego wraz z aplikacją.



![image](assets/fr/20.webp)



Otwórz aplikację i kliknij 3 kreski w prawym górnym rogu, a następnie skanuj. Zeskanuj kod QR przeglądarki, a następnie wprowadź hasło administratora aplikacji i kliknij OK.



![image](assets/fr/21.webp)



Tutaj znajduje się strona internetowa, która umożliwia interakcję z Avalonem. Jest to bardziej pulpit nawigacyjny do wyświetlania wskaźników urządzenia niż sposób jego konfiguracji.



Ale ustawienia puli są nadal dostępne w ten sposób, klikając **"Konfiguracja puli "** w prawym dolnym rogu.



![image](assets/fr/22.webp)



Podobnie jak w przypadku aplikacji mobilnej, można tu wprowadzić parametry basenu.



![image](assets/fr/23.webp)



## Sterowanie urządzeniem za pomocą aplikacji Avalon Family



Podłączyliśmy teraz nasz domowy Miner do sieci lokalnej i skierowaliśmy Hashrate na baseny Minings. Teraz odkryjmy podstawowe funkcje naszej maszyny za pomocą aplikacji Avalon Family.



W menu głównym aplikacji rodziny Avalon kliknij ikonę odpowiadającą urządzeniu Avalon Mini 3. Zostaniesz przeniesiony bezpośrednio do menu zarządzania trybami pracy.



dostępne są 3 opcje: tryb "Grzałka", tryb "Mining" lub tryb "Noc".





- W trybie "Grzałka" dostępne są 2 poziomy mocy "Eco" lub "Super".


Poziom "Eco" odpowiada mocy grzewczej 500 W dla Hashrate około 25 Th/s i 40 dB dla poziomu hałasu.


Poziom "Super" odpowiada mocy wyjściowej 650 W przy około 30 Th/s i 45 dB. Tryb ten umożliwia ustawienie maksymalnej temperatury otoczenia, powyżej której urządzenie przestanie działać.



![image](assets/fr/36.webp)




- W trybie "Mining" urządzenie działa z maksymalną prędkością, bez możliwości ustawienia docelowej temperatury (oczywiście poza wbudowanym limitem przegrzania). Celem jest maksymalne wykorzystanie wydajności Miner. Tutaj moc wyjściowa zbliża się do 800 W przy około 37,5 Th/s i poziomie hałasu 50-55 dB.



![image](assets/fr/37.webp)


Wreszcie, w trybie "Noc" Mini 3 działa z najniższą możliwą prędkością przy minimalnym poziomie hałasu. 400 W, 20 Th/s i ok. 33 dB.



Tutaj również można ustawić temperaturę docelową, powyżej której urządzenie przechodzi w tryb nieaktywny i zatrzymuje Miner. Jeśli temperatura spadnie, urządzenie uruchomi się ponownie i wznowi ogrzewanie i Miner. W tym trybie diody LED wyświetlacza są domyślnie wyłączone, ale można je włączyć w razie potrzeby, aby oświetlić pomieszczenie w ciemności, jak lampka nocna (patrz zdjęcie poniżej).



![image](assets/fr/38.webp)



![image](assets/fr/39.webp)



Wreszcie, możesz bawić się diodami LED Avalona za pomocą menu "Wyświetlacz". Możesz przewijać odpowiednie informacje operacyjne, wyświetlać godzinę, a nawet niestandardowy (pikselowy) obraz.



![image](assets/fr/40.webp)



![image](assets/fr/41.webp)



Podobnie jak w przypadku Avalon Nano 3S, menu "Ustawienia" umożliwia zmianę hasła administratora, ustawień basenu, sprawdzenie niedrożności filtra (znajdującego się na spodzie urządzenia), kontakt z pomocą techniczną lub przeglądanie dzienników urządzenia.



![image](assets/fr/42.webp)



Ponownie, filtr w dolnej części urządzenia można czyścić odkurzaczem, im częściej, tym lepiej.



Dotarliśmy do końca tego samouczka, w którym dowiedzieliśmy się, jak podłączyć nasz Avalon Mini 3 do naszej sieci lokalnej, jak skierować nasz Hashrate na pule Mining oraz jak poruszać się po opcjach i ustawieniach za pomocą aplikacji Avalon Family.



Aby dowiedzieć się więcej, zapoznaj się z naszym samouczkiem na temat mniejszej wersji Avalon: Nano 3S.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6