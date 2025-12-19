---
name: Canaan Avalon Nano 3S
description: Konfiguracja ASIC Avalon do solominingu lub Miner pooling
---

![cover](assets/cover.webp)



W tym samouczku przyjrzymy się, jak skonfigurować Canaan Avalon Nano 3S, aby ułatwić korzystanie z Miner w domu.



Do tej pory maszyny ASIC (*Application Specific Integrated Circuit*) zaprojektowane specjalnie do wykonywania określonego zadania - w tym przypadku obliczania Hash (SHA-256) dla Miner z Bitcoin - były szczególnie nieodpowiednie do użytku domowego. Uciążliwy hałas, generowane ciepło i konieczność dostosowania instalacji elektrycznej do obsługi ogromnej mocy tych urządzeń powstrzymywały większość z nas przed wzięciem w nich udziału.



Obecnie Canaan, jeden z wiodących producentów maszyn ASIC, postanowił zająć się rynkiem osób prywatnych, które chcą mieć Miner w domu, oferując gamę produktów, które są stosunkowo ciche i bardzo łatwe w instalacji (plug & play).



Urządzenia te są sprzedawane albo jako dodatkowy grzejnik w przypadku **Avalon Nano 3S (140W)**, albo jako mini grzejnik o mocy wyjściowej **800W** w przypadku **Avalon Mini 3**.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Należy pamiętać, że różnica w cenie w porównaniu z tradycyjnymi grzejnikami o równoważnej mocy w zdecydowanej większości przypadków nie pozwala na osiągnięcie zysku finansowego. Satoshi generowane przez Mining nigdy nie zrekompensują tej różnicy w cenie, chyba że masz dostęp do darmowej (nadwyżki) lub bardzo taniej energii elektrycznej.



Moim zdaniem urządzenia te powinny być postrzegane bardziej jako prosty sposób na Miner w domu dla tych, którzy chcą to zrobić z powodów osobistych: *uzyskać nie-KYC Satss / zagrać w "loterię" poprzez solominację / uczestniczyć w decentralizacji Hashrate etc.*., jednocześnie czerpiąc korzyści **jako bonus** z generowanego ciepła do ogrzania swojego pokoju w zimie. Ale nie jako sposób na oszczędzanie pieniędzy przynajmniej w większości przypadków (kraje zachodnie).



## Unboxing i funkcje



Najpierw zobaczmy, co znajduje się w pudełku Avalon Nano 3S.



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



Po otwarciu pudełka znajdziemy kartonowe etui zawierające odbiornik WIFI, który, jak zobaczymy później, należy podłączyć do portu USB urządzenia, aby umożliwić mu połączenie z siecią lokalną. W zestawie znajduje się również instrukcja obsługi oraz metalowa szpilka do resetowania urządzenia do ustawień fabrycznych, jeśli zajdzie taka potrzeba.



![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



Po wyjęciu wszystkiego z pudełka, oto co znajduje się w środku: oczywiście samo urządzenie, instrukcja obsługi, odbiornik WIFI, wspomniana wcześniej metalowa końcówka oraz zasilacz Supply. Dołączona karta kredytowa nie jest naszym zdaniem warta wzmianki.



![image](assets/fr/05.webp)



Poniżej znajduje się tabela podsumowująca ogólne specyfikacje techniczne Nano 3S:



| Caractéristique                                      | Valeur                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Taux de hachage                                      | 6 Th/s +- 5%                                            |
| Consommation d'énergie                               | 140 W                                                   |
| Bruit                                                | 30 - 40 dB                                              |
| Plage de température de sortie d'air                 | 60-70°C (sous température ambiante 25°C)                |
| Exigences de température ambiante pour l'utilisation | de -5 à 30°C                                            |
| Plage d'entrée de l'appareil                         | 28V 5A continu                                          |
| Plage d'entrée de l'adaptateur                       | 110-240V AC 50/60Hz                                     |
| Taille de la machine                                 | Longueur: 205 mm /  Largeur: 115 mm / Hauteur:  58.5 mm |
| Poids de la machine                                  | 0.86 kg                                                 |

## Włączanie zasilania i łączenie z siecią lokalną



Po rozpakowaniu, umieść Avalon Nano 3 S, jeśli to możliwe, w stosunkowo otwartym miejscu, aby umożliwić cyrkulację ciepła. Następnie zacznij od włożenia małego modułu odbiornika WIFI, jak pokazano poniżej:



![image](assets/fr/06.webp)


Następnie podłącz wtyczkę USB-C Supply do portu USB-C urządzenia, aby je zasilić.



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



Urządzenie uruchomi się, a na ekranie pojawi się logo Avalon Nano, a następnie logo "telefonu komórkowego" z napisem "Please Configure the Network With Avalon Family App".



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



Aby to zrobić, przejdź do sklepu z aplikacjami mobilnymi, wyszukaj i pobierz aplikację **Avalon Family**.



![image](assets/fr/11.webp)


Po zainstalowaniu, otwórz ją klikając na "Skip" w prawym górnym rogu, następnie na przycisk "Add" i na końcu na "Search". Upewnij się, że masz włączony Bluetooth na swoim smartfonie, aby wykrywanie urządzenia przebiegało płynnie.



![image](assets/fr/12.webp)


Po wykryciu urządzenia przez aplikację, kliknij na nie i wybierz "Połącz". Następnie zostaniesz przeniesiony do ekranu, na którym możesz wprowadzić szczegóły połączenia WIFI.


![image](assets/fr/13.webp)


Po podłączeniu urządzenia do sieci lokalnej ekran będzie wyglądał następująco:



![image](assets/fr/14.webp)



Pokazuje "fikcyjny" Hashrate, ponieważ żadna pula nie została jeszcze skonfigurowana, oraz czas, datę, zasilanie i IP Address urządzenia - bardzo przydatne, jeśli chcesz uzyskać dostęp do Interface urządzenia za pośrednictwem komputera i przeglądarki (więcej na ten temat później).



![image](assets/fr/15.webp)




## Podłączanie do Mining pool



**Ta część jest wspólna dla Nano 3s i Mini 3, ponieważ procesy są ściśle identyczne**.



Niezależnie od tego, czy chcemy "solominować", czy "poolować" Miner, będziemy musieli połączyć się z Mining pool. W rzeczywistości nasze urządzenie to nic innego jak Hash-maker bez świadomości sieci Bitcoin. Podłączenie go do puli daje mu dostęp do sieci Bitcoin i pozwala na otrzymywanie szablonów bloków do pracy.



### Używanie aplikacji do łączenia się z Mining pool



W aplikacji Avalon Family wybierz urządzenie, jak pokazano poniżej. Zostaniesz automatycznie poproszony o zmianę hasła administratora urządzenia. Kliknij "OK", jeśli chcesz to zrobić, lub "Anuluj", aby pozostawić domyślne hasło dostępu "admin".


![image](assets/fr/16.webp)


Następnie wybierz "Settings", a następnie "Pool Config" i wprowadź parametry dla 3 żądanych pul.


Pule #2 i #3 będą działać jako kopie zapasowe w przypadku awarii jednej z nich, dzięki czemu Miner nie będzie działać na darmo. Domyślnie Hashrate będzie skierowany do puli #1



W naszym przypadku wybieramy:




- 1 - Basen publiczny,
- 2 - CkPool,
- 3 - Ocean.



![image](assets/fr/17.webp)



Aby uzyskać więcej informacji na temat łączenia się z Mining pool, zapoznaj się z tymi samouczkami:



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

Podsumowując, potrzebujemy





- gW-26 puli, zwykle **stratum+tcp://xxxxxxxx:port**.





- nazwa "pracownika" składająca się z *twojego Bitcoin Address* i *pseudonimu* wybranego dla urządzenia, przy czym te dwa elementy są oddzielone *kropką*, na przykład:**bc1qxxxxxxxxxxxxxxxxx.MonAvalonNano3S**





- hasło, które zwykle jest zawsze "**x**"



Po wprowadzeniu informacji o puli kliknij przycisk "Zapisz".



![image](assets/fr/18.webp)


Uruchom ponownie urządzenie zgodnie z instrukcjami i poczekaj kilka minut, aż Hashrate zostanie skierowany na preferowaną pulę (#1).



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



W aplikacji rodziny Avalon kliknij ikonę odpowiadającą urządzeniu Avalon Nano 3S.


zostaną wyświetlone 3 menu: "Tryb pracy", "Sterowanie oświetleniem" i "Ustawienia". Najpierw kliknij "Tryb pracy". Zostaną wyświetlone 3 tryby zasilania urządzenia.



**Low**: zapewnia około 3 Th/s Hashrate przy zużyciu energii na poziomie 70W


**Średni**: zapewnia ok. 4,5 Th/s Hashrate przy poborze mocy 100 W


**Wysoki**: zapewni około 6 Th/s Hashrate przy maksymalnym zużyciu 140 W



![image](assets/fr/31.webp)


Cofnijmy się o krok i zbadajmy menu "Kontrola światła". Jest to funkcja czysto kosmetyczna. Dostępnych jest wiele opcji zmieniających kolor, intensywność, ciepło, wyłączających diody LED urządzenia w nocy itp. Łatwo się o tym przekonać.



![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



Ostatnim dostępnym dla nas menu jest menu "Ustawienia", które widzieliśmy już przy łączeniu się z naszymi basenami Mining. Tutaj można zarządzać pulami, zmienić hasło administratora urządzenia i obserwować różne wskaźniki, takie jak data wygaśnięcia gwarancji, czystość filtra lub sposób kontaktu z pomocą techniczną w przypadku awarii.



![image](assets/fr/35.webp)


W celu konserwacji i utrzymania filtra w jak największej czystości zalecamy używanie odkurzacza i regularne odkurzanie wlotów i wylotów powietrza, aby zapobiec zatykaniu.



Doszliśmy do końca tego samouczka, który nauczył nas, jak podłączyć nasz Avalon Nano 3 S do naszej sieci lokalnej, jak skierować nasz Hashrate na pule Mining oraz jak poruszać się po opcjach i ustawieniach za pomocą aplikacji Avalon Family.



Aby dowiedzieć się więcej, zapoznaj się z naszym samouczkiem na temat lepszej wersji Avalon: Mini 3.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7