---
name: Lightning Smoke Machine
description: Wyzwalaj maszynę do dymu za pomocą płatności Lightning za pośrednictwem ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Wprowadzenie



Przekształca klasyczną maszynę do dymu w urządzenie płatne w Bitcoin przez Lightning Network. Każda płatność automatycznie wyzwala strumień dymu!





- Poziom: Średnio zaawansowany
- Szacowany czas: 2-3 godziny
- Przypadki użycia: Wydarzenia Bitcoin, występy artystyczne, dema Lightning, zautomatyzowane efekty sceniczne



## Wymagania wstępne



### Wiedza





 - Podstawowa elektronika (okablowanie, przekaźniki)
 - Spawanie (lub użycie złączy Dupont)
 - Konfiguracja sieci (WiFi, WebSocket)



### Wymagane konta





- Serwer BTCPay: Funkcjonalna instancja (hostowana samodzielnie lub hostowana)
- Blink Wallet : Konto + dostęp API



### Dostęp





- Dostęp administratora do serwera BTCPay
- Połączenie WiFi dla ESP32



## Wymagane materiały



### Sprzęt - komponenty elektroniczne





- 1 Mikrokontroler - ESP32-WROOM-32


*ESP32-WROOM-32 to kompaktowy, tani mikrokontroler WiFi/Bluetooth do podłączania urządzeń elektronicznych do Internetu i zdalnego sterowania nimi*



![ESP32](assets/fr/1.webp)





- 1 Moduł przekaźnika - 5 V z transoptorem


*Przekaźnik jest jak przełącznik, który ESP32 może obsługiwać, aby włączyć lub wyłączyć maszynę do dymu*



![relay](assets/fr/2.webp)





- ~10 kabli Dupont - męski/żeński i męski/żeński



![dupont-cables](assets/fr/3.webp)





- 1 Zasilanie dla ESP32 - 5V USB lub bateria Li-Po



![battery](assets/fr/4.webp)





- 1 kabel micro-USB - połączenie pomiędzy ESP32 i zasilaczem



![micro-usb-cables](assets/fr/5.webp)





- 1 maszyna do mgły 220 V z pilotem na baterie 12 V



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 butelka płynu kompatybilnego z maszyną do dymu



### Sprzęt - Narzędzia





- Lutownica + cyna (w przypadku lutowania)
- Śrubokręt
- Multimetr (zalecane)



### Oprogramowanie





- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- Przeglądarka internetowa kompatybilna z WebSerial (Chrome/Edge/Brave)
- Skonfigurowany serwer BTCPay. Aby uzyskać więcej informacji na temat tworzenia instancji serwera BTCPay, odwiedź ten samouczek: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Architektura systemu



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **OSTRZEŻENIE DOTYCZĄCE BEZPIECZEŃSTWA - PRZECZYTAJ PRZED KONTYNUOWANIEM** **⚠️**



Ten projekt obejmuje maszynę do wytwarzania mgły podłączoną do **zasilania sieciowego 220 V**. Nieprawidłowa obsługa może spowodować **śmiertelne porażenie prądem** lub **pożar**.



**Zasady niepodlegające negocjacjom:**



1. **Przed otwarciem pilota zdalnego sterowania lub ingerencją w okablowanie należy ZAWSZE odłączyć urządzenie od zasilania**


2. **Wyjmij baterię z pilota zdalnego sterowania** przed przystąpieniem do obsługi (ryzyko zwarcia i uszkodzenia podzespołów)


3. **Sprawdź, czy wszystkie połączenia są odizolowane** przed ponownym podłączeniem czegokolwiek


4. **Nigdy nie podłączać ponownie zasilania 220 V**, dopóki skrzynka zdalnego sterowania nie zostanie zamknięta i zabezpieczona



Jeśli nie czujesz się komfortowo z tego rodzaju obsługą, zabierz ze sobą kogoś, kto to potrafi.



---

## CZĘŚĆ 1: Montaż sprzętu



### Krok 1: Przygotowanie pilota zdalnego sterowania



Cel: Podłącz przekaźnik do przycisku ON/OFF na pilocie zdalnego sterowania


1. Otwarty pilot zdalnego sterowania




    - Identyfikacja przycisku ON/OFF
    - Odkręć obudowę, aby otworzyć pilota zdalnego sterowania


2. Lokalizacja połączeń




 - Zlokalizuj zaciski + i - urządzenia
 - Test ciągłości za pomocą multimetru (opcjonalnie)



![smoke-machine-remote](assets/fr/8.webp)



3. Okablowanie przycisków (lutowanie lub złącza)




    - Przylutuj czarny przewód do zacisku - przycisku
    - Przylutuj czerwony przewód do wspólnego zacisku +



![smoke-machine-remote](assets/fr/9.webp)



### Krok 2: Podłączenie do modułu przekaźnika



**Przypomnienie: Terminologia przekaźników



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**Okablowanie od pilota do modułu przekaźnika:**




- Czarny przewód od przycisku ON/OFF **→** NO (normalnie otwarty)
- Przewód czerwony (wspólny) **→** COM (wspólny)



**Logika:**


Gdy ESP32 aktywuje przekaźnik, łączy COM i NO, co jest dokładnie tym samym, co naciśnięcie przycisku pilota.


Gdy ESP32 rozłączy przekaźnik, COM i NO zostaną rozdzielone, co jest równoznaczne ze zwolnieniem przycisku.



![remote-relay](assets/fr/10.webp)



### Krok 3: Podłączenie ESP32 do modułu przekaźnika



**Schemat okablowania:**



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**Weryfikacja:**




- VCC i GND dobrze połączone (polaryzacja)
- GPIO 21 używane jako sygnał sterujący
- Brak widocznego zwarcia



![relay-esp32](assets/fr/11.webp)



**Checkpoint Hardware**


Przed przejściem na oprogramowanie należy sprawdzić :




- Prawidłowo podłączony pilot zdalnego sterowania
- Moduł przekaźnika podłączony do ESP32
- Brak gołych przewodów dotykających innych komponentów
- 220V zawsze odłączone



![relay-esp32](assets/fr/12.webp)





---


## CZĘŚĆ 2: Konfiguracja oprogramowania



Użyjemy *Blink* jako przykładu, ale *BTCPay Server* oferuje również *Strike, Breez i Boltz*, jeśli wolisz inną opcję.



### Krok 1: Wtyczki, instalacja *BitcoinSwitch* + *Blink



1 - Przejdź do instancji *BTCPay Server* za pomocą konta administratora



2 - Stwórz swoją pierwszą żaluzję



3 - Po lewej stronie *BTCPay Server*, przewiń do dołu i przejdź do *"Manage Plugins "*



![btcpay-plugins](assets/fr/13.webp)



4 - Zamierzamy zainstalować wtyczki *BitcoinSwitch* oraz *Blink*



![btcpay-plugins](assets/fr/14.webp)



5 - Przewiń listę wtyczek w dół i kliknij *"Zainstaluj "*: *BitcoinSwitch i Blink* (lub dostępny wallet do wyboru)



![btcpay-plugins](assets/fr/15.webp)



6 - Po zakończeniu instalacji uruchom ponownie *BTCPay Server* i poczekaj 1 minutę na ponowne uruchomienie instancji



![btcpay-plugins](assets/fr/16.webp)



7 - Po powrocie do *"Zarządzaj wtyczkami "* sprawdź, czy obie wtyczki zostały zainstalowane



![btcpay-plugins](assets/fr/17.webp)



### Krok 2: Konfiguracja backendu: *BTCPay Server + Blink*



**1 - Utwórz wallet *Blink***




- Odwiedź https://www.blink.sv
- Utwórz swoje konto. Zapoznaj się z samouczkiem :



[https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd](https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Wygenerowanie klucza API *Blink***




- Uzyskaj dostęp do interfejsu API: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** i zaloguj się za pomocą tego samego konta, którego użyłeś do utworzenia wallet *Blink*



![blink-api](assets/fr/18.webp)





   - Po nawiązaniu połączenia przejdź do zakładki *API Keys*



![blink-api](assets/fr/19.webp)





   - Kliknij *" + "* w prawym górnym rogu, aby uzyskać dostęp do konfiguracji klucza API



![blink-api](assets/fr/20.webp)





   - Nadaj swojemu kluczowi API nazwę i pozostaw ustawienia domyślne. Następnie, w trzecim kroku, zanotuj swój klucz API - zobaczysz go tylko raz: `blink_mZ5KxxxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Po utworzeniu powinien pojawić się na liście aktywnych kluczy API.



![blink-api](assets/fr/22.webp)



**3 - Podłącz *Blink* do *BTCPay Server***




- Otwórz swój *BTCPay Server*
- Przejdź do : *Wallet* **→** *Lightning*



![btcpay-server](assets/fr/23.webp)





- Kliknij *Użyj węzła niestandardowego*
- Wklej następujący ciąg połączenia:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Ważne** :




- Nie modyfikuj pierwszej części: `type=blink;server=https://api.blink.sv/graphql`;
- Wymienić tylko :
    - api-key= * według klucza API Blink*
    - wallet-id= *przez twój wallet Blink* ID
- Następnie kliknij *Testuj połączenie*, a potem *Zapisz*



![btcpay-server](assets/fr/24.webp)





 - Sprawdź, czy połączenie zostało nawiązane (zielony status)



![btcpay-server](assets/fr/25.webp)



**4 - Utwórz punkt sprzedaży (PoS)**




- W BTCPay Server przejdź do zakładki *Plugins* i kliknij *Point of sale*



![btcpay-server](assets/fr/26.webp)





- Nadaj swojemu PoS nazwę i kliknij *Create* (Utwórz)



![btcpay-server](assets/fr/27.webp)





- Konfiguracja PoS :
    - Wybierz styl punktu sprzedaży = *Wyświetlacz*
    - Waluta = *SATS*
    - Kliknij *ZAPISZ*



![btcpay-server](assets/fr/28.webp)





- Konfiguracja produktu :
    - Usuń wszystkie domyślne produkty
    - Następnie kliknij *dodaj element*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Konfiguracja produktu:
    - Tytuł : *smoke-machine*
    - Cena : *10 sats*
    - Przełącznik GPIO Bitcoin: 21
    - Czas przełączania Bitcoin (w milisekundach) : 5000
    - Kliknij przycisk *Zamknij*, a następnie *Zapisz*, aby zapisać nowy produkt



![btcpay-server](assets/fr/31.webp)



### Krok 3: Oprogramowanie układowe: Flashowanie ESP32



**1 - Przejdź do strony flash




- Przejdź do : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash oprogramowania sprzętowego BitcoinSwitch**




- Podłącz ESP32 do komputera za pomocą kabla USB/Micro-USB
- Następnie kliknij *Połącz z urządzeniem*
- Otworzy się okno, w którym należy wybrać port USB urządzenia ESP32, a następnie kliknąć przycisk *Connect* (Połącz)



![bitcoinswitch-lnbits](assets/fr/33.webp)





- Po podłączeniu ESP32 sflashujemy oprogramowanie sprzętowe BitcoinSwitch. W sekcji *T-Display* kliknij *Upload Firmware*, aby uzyskać najnowszą dostępną wersję (obecnie: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Poczekaj na przesłanie, proces zostanie zakończony, gdy w logach pojawi się *"Leaving... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Odłącz ESP32



**3 - Sprawdź instalację oprogramowania sprzętowego BitcoinSwitch




- Przeładuj stronę: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Ponownie podłącz ESP32 do komputera za pomocą kabla USB/Micro-USB
- Następnie kliknij *Połącz z urządzeniem
- Wybierz port USB w urządzeniu ESP32, a następnie kliknij przycisk *Connect*, jak opisano powyżej
- Po podłączeniu naciśnij przycisk **RESET** na ESP32
- Sprawdź w logach, czy ostatnie linie pokazują :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Jest to normalne, oznacza to, że nie ma jeszcze konfiguracji, ale oprogramowanie sprzętowe zostało zainstalowane)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - Generowanie adresu URL WebSocket LNURL**



Oczekiwany format końcowy :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Etapy generowania :




- Otwórz swoją instancjęBTCPay Server, a następnie przejdź do PoS, który utworzyliśmy później.
- Następnie kliknij "Widok", aby otworzyć swój PoS w przeglądarce



![btcpay-server-https](assets/fr/37.webp)





- Skopiuj adres URL strony, na przykład :



![btcpay-server-https](assets/fr/38.webp)



Rozpakujmy ten adres URL:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → domena instancji serwera BTCPay
- `46XXXXXXXXXXXXXXXXwFB` → unikalny identyfikator PoS użytkownika
- `/pos` → oznacza punkt sprzedaży



Przekształć go:




- Zastąp `https://` przez `wss://`
- Dodaj `/bitcoinswitch` na końcu



Wynik:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Zachowaj ten adres URL do przyszłej konfiguracji, ponieważ umożliwi on ESP32 komunikację w czasie rzeczywistym z serwerem BTCPay. Protokół WebSocket (`wss://`) ustanawia stałe połączenie między nimi: gdy tylko płatność Lightning zostanie potwierdzona w PoS, BTCPay natychmiast wysyła informacje do ESP32, który może następnie uruchomić maszynę do dymu.



**5 - Konfiguracja WiFi i WebSocket




- Powrót do strony: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) z podłączonym ESP32
- Przejdź do *Konfiguracja urządzenia* → *Ustawienia Wi-Fi*



Inform :




- WiFi SSID: nazwa sieci Wi-Fi
- Hasło Wi-Fi: hasło do sieci Wi-Fi



![bitcoinswitch-lnbits](assets/fr/39.webp)





- W sekcji *LNbits Device URL* wklej adres URL WebSocket utworzony w poprzednim kroku
- Kliknij *Upload config* (Prześlij konfigurację)



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Poczekaj na zakończenie przesyłania; dzienniki powinny wyświetlać wprowadzone parametry (SSID, hasło i adres URL WebSocket)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Poczekaj, aż ESP32 nawiąże połączenie WebSocket. Powinieneś zobaczyć :



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Można teraz odłączyć ESP32



---
## Oprogramowanie Checkpoint



Przed testem końcowym należy sprawdzić :





- Blink połączony z BTCPay
- PoS utworzony z co najmniej 1 pozycją
- ESP32 flashowany za pomocą BitcoinSwitch
- WiFi skonfigurowane na ESP32
- Poprawny adres URL WebSocket
- Dzienniki ESP32 wolne od błędów



---

## Testowanie i debugowanie



### Ukończenie testu końcowego



1. Podłącz maszynę do dymu (220 V) i włącz ją


2. Zasilanie ESP32 (bateria lub USB)


3. Otwórz swój BTCPay PoS w przeglądarce


4. Skanowanie elementu "smoke-machine"


5. Płać za pomocą wallet Lightning (Blink lub innego wallet)


6. Obserwować:




 - Kliknięcie przekaźnika (słyszalny dźwięk i zaświecenie się diody LED przekaźnika)
 - Maszyna do dymu jest aktywowana
 - Generowany dym!



### Problemy i rozwiązania dotyczące sprawiedliwości



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## Zasoby



### Przydatne linki





- Oprogramowanie sprzętowe BitcoinSwitch: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Dokumenty serwera BTCPay : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 Pinout : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Społeczność i wsparcie





- Serwer BTCPay** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Oficjalny Mattermost
- Serwer BTCPay Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Oficjalny Telegram, aktywna społeczność
- BitcoinSwitch (błędy w oprogramowaniu sprzętowym)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Kod źródłowy





- Kod źródłowy oprogramowania sprzętowego BitcoinSwitch: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** Układaj sats, rób dym, baw się dobrze, zachowaj pokorę! **⚡**