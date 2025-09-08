---
name: Prędkość Wallet - PoS
description: Z łatwością zintegruj płatności Bitcoin i stablecoin w swojej firmie
---
![cover](assets/cover.webp)



Przyjęcie Bitcoin na całym świecie opiera się na konkretnych przypadkach użycia w życiu codziennym. Wykorzystanie Bitcoin w natychmiastowych transakcjach handlowych na całym świecie wzmacnia to przyjęcie zarówno w dużych instytucjach, jak i małych firmach. W tym samouczku przyjrzymy się Speed Business, ujednoliconej platformie płatniczej, która umożliwia firmie akceptowanie płatności Bitcoin za pośrednictwem Lightning.



![btc-session](https://www.youtube.com/watch?v=ywUNZ_sxr0Q)



## Rozpoczęcie pracy z aplikacją Speed Business



[Speed Business](https://www.tryspeed.com/) to platforma opracowana przez [Speed Wallet](https://www.speed.app/), która umożliwia każdemu sprzedawcy integrację natychmiastowych, tanich płatności Bitcoin i stablecoin.



Speed posiada szeroki zakres funkcji obejmujących finansowe aspekty działalności. Znajdziesz tu:





- Konfiguracja płatności online**: Otrzymuj płatności od swoich klientów gdziekolwiek są, dzięki swojej stronie internetowej.





- Płatności na miejscu**: Idealny dla sklepów i firm, które pobierają gotówkę w sklepie.





- Wypłaty**: Wypłacaj swoje aktywa płynnie i używaj bitcoinów do spłacania swoich klientów i wynagrodzeń.





- Połączenie z innymi platformami**: Korzystasz z zewnętrznych narzędzi do zarządzania płatnościami? Speed oferuje możliwość podłączenia ich do swojej platformy, aby uzyskać kompleksowy ekosystem, który odzwierciedla Twoją działalność.



Utwórz konto na [Speed](https://app.tryspeed.com/register/), a my zaczniemy konfigurować płatności dla Twojej firmy.



![account-creation](assets/fr/01.webp)



Przekaż informacje do Speed Wallet, aby pomógł ci uprościć platformę zgodnie z twoim doświadczeniem z Bitcoin i Lightning Network



![onboard](assets/fr/02.webp)



Speed jest dostarczany z zestawem programistycznym, który pozwala dostosować integrację, oraz rozszerzeniem do standardowej integracji.



Na potrzeby tego samouczka będziemy pracować ze standardową integracją przy użyciu rozszerzenia dostarczonego przez Speed.



Aby ułatwić korzystanie z aplikacji, Speed oferuje tryb testowy, który pozwala wypróbować różne funkcje bez martwienia się o ich wpływ na zarządzanie sklepem.



![test-data](assets/fr/03.webp)



Możesz przetestować wszystkie aspekty omówione w tym samouczku, korzystając z trybu testowego.



Po dezaktywacji trybu testowego należy skonfigurować portfel wypłat.



![configure-wallet](assets/fr/04.webp)



Jeśli nie posiadasz jeszcze Bitcoin i/lub Lightning Wallet, zalecamy zapoznanie się z naszymi samouczkami [portfele mobilne] (https://planb.network/tutorials/wallet).



https://planb.network/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

⚠️ **WAŻNE**: Podczas konfigurowania portfela wybierz typ **BTC (On-Chain)**, gdy otrzymujesz duże kwoty, rzędu tysięcy euro, aby zapewnić wiarygodne potwierdzenie na Bitcoin, oraz typ **LN Address**, gdy chcesz otrzymywać natychmiastowe mikropłatności w swojej firmie.



![setup-wallet](assets/fr/05.webp)



Następnie potwierdź dodanie swojego portfolio za pomocą e-maila weryfikacyjnego wysłanego przez Speed.



![verfication](assets/fr/06.webp)



Zdefiniuj minimalną wypłatę i minimalne saldo, poniżej których nie będziesz mógł wypłacić swoich aktywów.



![payout](assets/fr/07.webp)



## Dodaj swoje produkty



W sekcji **Produkty** dodaj katalog produktów sprzedawanych w sklepie.



![product-creation](assets/fr/08.webp)



Naciśnij **Next**, aby kontynuować definiowanie produktu i jego funkcji.



![product-details](assets/fr/09.webp)



Następnie zdefiniuj cenę sprzedaży produktu.



![product-price](assets/fr/10.webp)



Produkty te umożliwiają generate linki do płatności, dzięki czemu klienci mogą za nie zapłacić.



## Otrzymywanie płatności



Speed Wallet daje możliwość korzystania z wielu metod otrzymywania płatności online lub na miejscu w firmie.



W menu **Odbierz płatności > Płatności** znajdziesz historię otrzymanych płatności i ich status (zapłacone, wygasłe, niezapłacone, anulowane).



![payments](assets/fr/11.webp)





- Linki do płatności znajdują się w opcji **Checkout Links** i umożliwiają skonfigurowanie unikalnych stron płatności dla produktów.



![checkout-link](assets/fr/12.webp)



W zależności od potrzeb można skonfigurować i dostosować stronę płatności do otrzymywania płatności w określonej kwocie.



![configure-checkout](assets/fr/13.webp)



![finalize-checkout](assets/fr/14.webp)



Listę linków do płatności skonfigurowanych na koncie można znaleźć w menu **Linki do płatności**.





- Faktury: Speed umożliwia generate ofert i faktur dla klientów.



![invoices](assets/fr/16.webp)



Wybierz już zarejestrowanego klienta lub z łatwością utwórz własnego.



Ustawienie waluty umożliwia dostęp do listy produktów skonfigurowanych w tej walucie.



Możesz wysłać ten Invoice w formacie PDF, e-mailem lub generate link z kodem QR do zeskanowania (idealny dla sklepów, które odbierają towar na miejscu), aby klient mógł zapłacić Invoice.



![configure-invoice](assets/fr/17.webp)






- Menu **Adresy płatności** pozwala skonfigurować Lightning Address, na który można otrzymywać wiele płatności o różnych kwotach.



![addresses](assets/fr/19.webp)



⚠️ Można dodawać i używać nazw domen innych niż Speed. Jednak w przypadku pierwszych doświadczeń zalecamy użycie standardowej konfiguracji, aby skorzystać z całej wiedzy wsparcia technicznego firmy Speed.





- The **One QR**: Idealny do płatności na miejscu, stwórz kod QR powiązany z Twoją firmą, aby umożliwić klientom płacenie za Twoje produkty.



![one-qr](assets/fr/20.webp)



## Dokonywanie płatności z aplikacji Speed



Speed Business nie tylko zbiera płatności dla Twojej firmy, ale jest to portfel, który pozwala zarządzać całą finansową stroną Twojej firmy bez żadnych przeszkód.



W menu **Wyślij płatność** znajdziesz wszystkie opcje przelewów pieniężnych, jakie oferuje speed.





- Natychmiastowe płatności**: Opcja natychmiastowego wysyłania umożliwia bezpieczne wysyłanie bitcoinów z konta sprzedawcy.





- Łącza do wypłat generate** umożliwiające partnerom i dostawcom dostęp do płatności w późniejszym terminie bez konieczności obecności online.



W opcji **Withdrawal Links** utwórz nowy link do wypłaty, a następnie skonfiguruj go, definiując walutę, kwotę i hasło, aby zabezpieczyć transakcję odbiorcy.



![withdrawal-links](assets/fr/21.webp)



linki do wypłaty ⚠️Les mogą być użyte tylko raz, zdecydowanie zalecamy ustawienie unikalnego hasła dla każdego linku, w przeciwnym razie każdy, kto jest w posiadaniu linku, może wypłacić kwotę ustawioną na linku do wypłaty.





- Wypłaty**: W menu Wypłaty zainicjuj wypłaty z salda Speed Business do osobistego Wallet.



![payouts](assets/fr/22.webp)





- Rabaty**: Zachęcaj swoich stałych klientów, ustawiając opcje rabatowe, aby zdobywać bonusy.



![cashbacks](assets/fr/23.webp)



## Explorer Speed Business



Speed Business to platforma wielowalutowa, która umożliwia przechowywanie oddzielnych portfeli w jednym systemie.



W opcji **Balances** znajdź saldo swoich portfeli Bitcoin, USDT i USDC.



![balance](assets/fr/24.webp)



Podobnie jak Speed Wallet, w menu **Swap**, Speed Business umożliwia Exchange wymianę walut między różnymi portfelami walutowymi (BTC, USDT, USDC) za jedyne Sats 20 000 (około 20 USD po obecnym kursie).



![swap](assets/fr/25.webp)



W menu **Transfer** można komunikować się z innymi sprzedawcami i łatwo przesyłać bitcoiny za pomocą ich Speed ID.



![transferts](assets/fr/26.webp)



W menu **Klienci** można zapisywać i przeglądać listę klientów (osób fizycznych lub firm).



![customers](assets/fr/27.webp)



Zdobywaj nagrody, uczestnicząc w programie partnerskim Speed.



W menu **Partnerzy** zaproś sprzedawców do założenia swojej firmy w Speed business i zarabiania pasywnego dochodu.



![partners](assets/fr/28.webp)



## Zintegruj Speed z witryną swojej firmy



Speed Business posiada zestaw deweloperski, który pozwala zintegrować rozwiązanie płatnicze z własną stroną internetową.



W menu **Developers** utwórz klucze publiczne i prywatne, aby korzystać z metod API Speed Wallet.



Znajdź pełną [dokumentację] (https://apidocs.tryspeed.com/reference/introduction) dla lepszej integracji Speed Business.



![developers](assets/fr/29.webp)



## Dostosuj swoją firmę



W menu **Ustawienia** możesz skonfigurować swój profil sprzedawcy i informacje biznesowe.



W sekcji **Ustawienia biznesowe**:





- Edytuj dane swojego konta sprzedawcy, takie jak imię i nazwisko, lokalizacja i strefa czasowa.





- Sprawdź aktywowane uprawnienia (otrzymywanie płatności, wysyłanie Bitcoin, Exchange, przelew, wypłata) na swoim koncie w menu **Stan konta**.





- Zdefiniuj portfele wypłat w menu **Payout Wallets** i skonfiguruj je w menu **Payout Scheduling**.





- Zdefiniuj wytyczne graficzne dla swojej firmy i dostosuj strony płatności, wiadomości e-mail, kody QR i faktury do swoich upodobań w menu **Branding**.





- Skonfiguruj metody płatności w akceptowanych walutach w menu **Metoda płatności**.



![payment-method](assets/fr/30.webp)



⚠️ Tolerancja odpowiada procentowemu zmniejszeniu akceptowanej kwoty Invoice, aby płatność została uznana za ważną. Jeśli klient musi zapłacić 100 USD, a tolerancja wynosi 1%, każda płatność w wysokości 99 USD zostanie zatwierdzona Invoice w wysokości 100 USD.





Masz już dobre pojęcie o Speed, zintegruj Bitcoin ze swoją firmą i rozwijaj lokalną gospodarkę o obiegu zamkniętym w oparciu o Bitcoin. Jeśli ten samouczek okazał się przydatny, jesteśmy pewni, że nasz szwajcarski samouczek Bitcoin Pay spodoba ci się równie mocno.



https://planb.network/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

