---
name: PayJoin - Wróbel Wallet
description: Jak dokonać transakcji PayJoin na Sparrow Wallet?
---

![tutorial cover image sparrow payjoin](assets/cover.webp)


oSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, Payjoins Stowaway na Samourai Wallet działa teraz tylko poprzez ręczną wymianę PSBT między zaangażowanymi stronami, pod warunkiem, że obaj użytkownicy są połączeni z własnym Dojo. Jeśli chodzi o Sparrow, Payjoiny przez BIP78 nadal działają. Narzędzia te mogą jednak zostać ponownie uruchomione w nadchodzących tygodniach. W międzyczasie zawsze możesz przeczytać ten artykuł, aby zrozumieć teoretyczne działanie payjoins._


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

> *Zmusić szpiegów Blockchain do przemyślenia wszystkiego, co myślą, że wiedzą*

PayJoin to specyficzna struktura transakcji Bitcoin, która zwiększa prywatność użytkownika podczas wydawania środków poprzez współpracę z odbiorcą płatności. Istnieje kilka implementacji, które ułatwiają konfigurację i automatyzację PayJoin. Wśród tych implementacji najbardziej znaną jest Stowaway opracowana przez zespół Samourai Wallet. Niniejszy samouczek ma na celu przeprowadzenie użytkownika przez proces dokonywania transakcji PayJoin Stowaway przy użyciu oprogramowania Sparrow Wallet.


## Jak działa Stowaway?


Jak wspomniano wcześniej, Samourai Wallet oferuje narzędzie PayJoin o nazwie "Stowaway" Jest ono dostępne za pośrednictwem oprogramowania Sparrow Wallet na PC lub aplikacji Samourai Wallet na Androida. Aby wykonać PayJoin, odbiorca, który działa również jako współpracownik, musi korzystać z oprogramowania kompatybilnego ze Stowaway, a mianowicie Sparrow lub Samourai Wallet. Te dwa oprogramowania są interoperacyjne, umożliwiając transakcje Stowaway między Sparrow Wallet i Samourai Wallet i odwrotnie.


Stowaway opiera się na kategorii transakcji, które Samourai określa jako "Cahoots" Cahoot to zasadniczo transakcja współpracy między wieloma użytkownikami, która wymaga informacji off-chain Exchange. Obecnie Samourai oferuje dwa narzędzia Cahoots: Stowaway (Payjoins) i StonewallX2 (które omówimy w przyszłym artykule).


Transakcje Cahoots obejmują wymianę częściowo podpisanych transakcji między użytkownikami. Proces ten może być długotrwały i uciążliwy, zwłaszcza gdy odbywa się zdalnie. Nadal jednak można go wykonać ręcznie z innym użytkownikiem, co może być wygodne, jeśli współpracownicy są fizycznie blisko siebie. W praktyce wymaga to ręcznej wymiany pięciu kodów QR, które należy kolejno zeskanować.


Gdy odbywa się to zdalnie, proces ten staje się zbyt skomplikowany. Aby rozwiązać ten problem, Samourai opracował szyfrowany protokół komunikacyjny oparty na sieci Tor, zwany "Soroban" Dzięki Soroban niezbędna wymiana PayJoin jest zautomatyzowana za pomocą przyjaznego dla użytkownika Interface. Jest to druga metoda, którą omówimy w tym artykule.


Te zaszyfrowane wymiany wymagają ustanowienia połączenia i uwierzytelnienia między uczestnikami Cahoots. Komunikacja Soroban opiera się na Paynyms użytkowników. Jeśli nie jesteś zaznajomiony z Paynyms, zapraszam do zapoznania się z tym artykułem po więcej szczegółów: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/On-Chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)

Mówiąc prościej, Paynym to unikalny identyfikator powiązany z Wallet, który umożliwia korzystanie z różnych funkcji, w tym szyfrowanych wiadomości. Paynym jest prezentowany w formie identyfikatora i ilustracji przedstawiającej robota. Oto przykład mojego na Testnet: ![Paynym Sparrow](assets/en/1.webp)


**Podsumowanie:**



- _Payjoin_ = Specyficzna struktura transakcji opartej na współpracy;
- _Stowaway_ = implementacja PayJoin dostępna na Samourai i Sparrow Wallet;
- _Cahoots_ = Nazwa nadana przez Samourai wszystkim rodzajom transakcji opartych na współpracy, w tym PayJoin Stowaway;
- _Soroban_ = zaszyfrowany protokół komunikacyjny ustanowiony w sieci Tor, umożliwiający współpracę z innymi użytkownikami w kontekście transakcji Cahoots.
- _Paynym_ = Unikalny identyfikator Wallet umożliwiający komunikację z innym użytkownikiem na Sorobanie w celu

przeprowadzić transakcję Cahoots.


[**-> Dowiedz się więcej o transakcjach PayJoin i ich użyteczności**](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)


## Jak nawiązać połączenie między Paynyms?


Aby wykonać zdalną transakcję Cahoots, w szczególności PayJoin (Stowaway) za pośrednictwem Samourai lub Sparrow, konieczne jest "śledzenie" użytkownika, z którym zamierzasz współpracować, przy użyciu jego Paynym. W przypadku pasażera na gapę oznacza to śledzenie osoby, do której chcesz wysłać bitcoiny.


**Oto procedura ustanowienia tego połączenia:**


Najpierw należy uzyskać identyfikator Paynym odbiorcy. Można to zrobić za pomocą jego pseudonimu lub kodu płatności. Aby to zrobić, w aplikacji Sparrow Wallet odbiorcy wybierz zakładkę "Narzędzia", a następnie kliknij "Pokaż PayNym".

![Show Paynym](assets/notext/2.webp)

![Paynym Sparrow](assets/en/1.webp)

Po swojej stronie otwórz Sparrow Wallet i uzyskaj dostęp do tego samego menu `Pokaż PayNym`. Jeśli korzystasz z Paynym po raz pierwszy, musisz uzyskać identyfikator, klikając `Retrieve PayNym`.

![Retrieve paynym](assets/notext/3.webp)

Następnie wprowadź identyfikator Paynym współpracownika (jego pseudonim `+...` lub kod płatności `PM...`) w polu `Znajdź kontakt`, a następnie kliknij przycisk `Dodaj kontakt`.

![add contact](assets/notext/4.webp)

Oprogramowanie wyświetli przycisk "Połącz z kontaktem". Kliknięcie tego przycisku nie jest konieczne w przypadku naszego samouczka. Ten krok jest konieczny tylko wtedy, gdy planujesz dokonywać płatności na rzecz Paynym wskazanego w kontekście BIP47, który nie jest związany z naszym samouczkiem.


Gdy Paynym odbiorcy będzie podążać za Twoim Paynym, powtórz tę operację w przeciwnym kierunku, aby odbiorca również podążał za Tobą. Następnie możesz wykonać PayJoin.


## Jak wykonać PayJoin na Sparrow Wallet?


Jeśli wykonałeś te kilka wstępnych kroków, jesteś wreszcie gotowy do przeprowadzenia transakcji PayJoin! Aby to zrobić, postępuj zgodnie z naszym samouczkiem wideo:

![Payjoin Tutorial - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)


**Zasoby zewnętrzne:**



- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.