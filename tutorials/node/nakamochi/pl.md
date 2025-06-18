---
name: Nakamochi
description: Node Running Made Easy - Jak skonfigurować i używać Nakamochi Bitcoin i Lightning node.
---

Uruchomienie własnego Bitcoin i Lightning Full node nie musi już być skomplikowanym zadaniem ograniczonym do ekspertów technicznych. Tradycyjnie konfigurowanie węzłów i zarządzanie nimi wymagało dogłębnej wiedzy z zakresu kryptografii, sieci i tworzenia oprogramowania. Nakamochi zmienia to, udostępniając węzły każdemu, niezależnie od zaplecza technicznego.


Dzięki Nakamochi każdy może skonfigurować i obsługiwać węzeł z domu, zapewniając pełną prywatność i niezależność finansową. Prowadzenie Full node nie tylko zabezpiecza własne transakcje, ale także przyczynia się do wzmocnienia sieci Bitcoin. Zdecentralizowana i odporna sieć Bitcoin opiera się na szerokiej dystrybucji węzłów, aby zapewnić jej bezpieczeństwo i niezależność.


### Spis treści



- Czym jest Nakamochi i jak działa?
- Konfiguracja Nakamochi
- Informacje o Lightning Network
- Otwieranie kanałów i dokonywanie transakcji w Lightning Network



## Czym jest Nakamochi i jak działa?


Nakamochi to Full node obsługujący tylko Bitcoin, który obsługuje zarówno sieci Bitcoin, jak i Lightning. Zawiera zintegrowany Bitcoin i Lightning Wallet, umożliwiając użytkownikom uruchomienie bezpiecznego, suwerennego węzła Bitcoin, jednocześnie korzystając z szybkości Lightning Network i niskich kosztów transakcji.


Węzłem Nakamochi można zarządzać za pośrednictwem aplikacji mobilnej [BitBanana (Android)](https://bitbanana.app) i [Zeus (iOS)](https://bitbanana.app), co pozwala na wygodną kontrolę z dowolnego miejsca. Aplikacje te działają jako zdalne sterowanie węzłem, umożliwiając bezpośrednie płatności za pomocą Bitcoin lub Lightning, zarządzanie transakcjami, otwieranie lub zamykanie kanałów, sprawdzanie sald i monitorowanie wydajności węzła, a wszystko to z łatwością.



## Konfiguracja Nakamochi zajmuje zaledwie 5 minut


### Krok 1: Podłącz i rozpocznij


1. Podłącz Nakamochi do zasilania i Wi-Fi.

2. Kliknij **"Setup New Wallet"** i bezpiecznie zapisz swoją 24-słowną frazę odzyskiwania.

3. Użyj aplikacji do zarządzania węzłami (Zeus lub BitBanana), aby połączyć się z Nakamochi:

4. Otwórz aplikację i zeskanuj kod QR wyświetlony na urządzeniu Nakamochi.

5. W celu zwiększenia bezpieczeństwa należy ustawić kod PIN na urządzeniu.


![image](assets/en/01.webp)

podłącz zasilanie i zapisz 24-słowną frazę seed_


![image](assets/en/02.webp)

_Poczekaj, aż Blockchain dogoni_


![image](assets/en/03.webp)

_Ustaw nowy Wallet w zakładce Lightning_


![image](assets/en/04.webp)

_Scan QR Code with Node Management App_


![image](assets/en/05.webp)

_Dla dodatkowego bezpieczeństwa ustaw kod PIN_


**Uwaga:** _Pozwól węzłowi Nakamochi zsynchronizować się z Blockchain. Proces ten może zająć trochę czasu w zależności od połączenia internetowego



## Informacje o Lightning Network


Bitcoin Lightning Network rewolucjonizuje transakcje Bitcoin, czyniąc je szybszymi, tańszymi i bardziej wydajnymi. Jest idealny do codziennego użytku, umożliwiając niemal natychmiastowe płatności przy minimalnych opłatach, idealny do mikrotransakcji, takich jak zakup kawy lub obsługa częstych drobnych zakupów.

Obsługując off-chain, Lightning został zaprojektowany do skalowania, obsługując tysiące transakcji na sekundę bez przeciążania głównego Bitcoin Blockchain. To czyni go kluczowym graczem w ewolucji Bitcoin w praktyczny, globalny system płatności.

Kolejną zaletą jest prywatność, ponieważ transakcje na Lightning są kierowane przez prywatne kanały płatności, a nie rejestrowane bezpośrednio na Blockchain. Zapewnia to bardziej dyskretny sposób dokonywania transakcji przy jednoczesnym zachowaniu solidnego bezpieczeństwa Bitcoin.



#### Wyjaśnienie kanałów płatności


Lightning Network działa za pośrednictwem kanałów płatności, które są połączeniami między dwiema stronami umożliwiającymi wiele transakcji bez bezpośredniej interakcji z Blockchain. Gdy kanał jest otwarty, saldo między dwiema stronami jest aktualizowane w tym drugim rozwiązaniu Layer Lightning dla każdej transakcji, zapewniając szybkie i tanie płatności. Tylko otwarcie i zamknięcie kanału są rejestrowane na On-Chain, co zmniejsza przeciążenie Bitcoin Blockchain. Taka konstrukcja zapewnia skalowalność i prywatność, ponieważ poszczególne transakcje pozostają niezarejestrowane na publicznym Ledger.


**Przykład:** Alice i Bob otwierają kanał poprzez zatwierdzenie Bitcoin. Alice wysyła Bitcoiny do Boba, a ich salda off-chain aktualizują się natychmiast bez zapisu On-Chain. Jeśli Alice następnie zapłaci Charliemu, a Alice nie ma bezpośredniego kanału do Charliego, płatność może zostać przekierowana przez kanał Boba, aby dotrzeć do Charliego. Routing przez węzły pośredniczące zapewnia płatności nawet bez bezpośrednich połączeń, dzięki czemu sieć jest bardzo wydajna.



## Otwieranie kanałów i dokonywanie transakcji w Lightning Network


Po skonfigurowaniu Nakamochi i połączeniu z aplikacją do zarządzania węzłami można rozpocząć korzystanie z Lightning Network, otwierając kanały i dokonując transakcji.


### Otwieranie kanałów w aplikacji Zeus (iOS):


1. Przejdź do zakładki **"Kanały "** (dolne menu).

2. Kliknij **"+"**, aby otworzyć nowy kanał.

3. Zeskanuj lub wprowadź klucz publiczny węzła, z którym chcesz się połączyć.

4. Wprowadź zablokowaną kwotę (wybierz z peerem lub użyj minimalnej stałej kwoty dla dobrze znanych węzłów).

5. Kliknij **"Otwórz kanał "**.


![image](assets/en/06.webp)

_ZEUS Screenshot_


Więcej informacji: [Channels | Zeus Documentation](https://docs.zeusln.app/)


### Otwieranie kanałów w BitBanana (Android):


1. Otwórz menu hamburgera (po lewej).

2. Przejdź do **"Kanały "**.

3. Kliknij **"+"**, aby dodać/otworzyć nowy kanał.

4. Zeskanuj lub wklej klucz publiczny.

5. Wprowadź zablokowaną kwotę (wybierz z peerem lub użyj minimalnej stałej kwoty dla dobrze znanych węzłów).


![image](assets/en/07.webp)

_Zrzut ekranu Bitbanana_


Więcej informacji: [BitBanana](https://bitbanana.com)


Po otwarciu kanału można za jego pośrednictwem kierować płatności do innych uczestników sieci. Salda dostosowują się do off-chain, dzięki czemu transakcje są niemal natychmiastowe i wiążą się z minimalnymi opłatami.

Jeśli kanał nie jest już potrzebny, można go zamknąć. Ta czynność rozlicza ostateczne saldo między użytkownikiem a jego peerem i zapisuje je w On-Chain. W idealnej sytuacji obie strony zgadzają się i są online w celu "wspólnego zamknięcia" (szybsze i niższe opłaty w porównaniu do "wymuszonego zamknięcia" z niereagującym/offline peerem).

Zasadniczo zalecamy pozostawienie otwartych kanałów w celu obniżenia kosztów oraz zwiększenia niezawodności i wydajności sieci. Utrzymując otwarte kanały, minimalizujesz opłaty transakcyjne On-Chain, unikasz przestojów związanych z ponownym połączeniem kanałów i utrzymujesz stabilną zdolność routingu w celu płynnego przetwarzania płatności. Takie podejście sprzyja solidnej i odpornej sieci, jednocześnie poprawiając ogólne wrażenia użytkownika i zmniejszając koszty operacyjne.



### Przydatne linki



- [O Nakamochi](https://nakamochi.io/)
- [Subskrybuj biuletyn Nakamochi](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)