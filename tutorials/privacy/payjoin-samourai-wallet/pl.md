---
name: Payjoin - Samourai Wallet
description: Jak wykonać transakcję PayJoin na Samourai Wallet?
---
![samourai payjoin cover](assets/cover.webp)


***UWAGA:** Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, Payjoins Stowaway na Samourai Wallet działa tylko poprzez ręczną wymianę PSBT między zainteresowanymi stronami, pod warunkiem, że obaj użytkownicy są połączeni z własnym Dojo. Jeśli chodzi o Sparrow, Payjoiny przez BIP78 nadal działają. Możliwe jednak, że narzędzia te zostaną ponownie uruchomione w nadchodzących tygodniach. W międzyczasie nadal możesz przeczytać ten artykuł, aby zrozumieć teoretyczne działanie Stowaway.*


jeśli planujesz wykonać transakcję Stowaway ręcznie, procedura jest bardzo podobna do tej opisanej w tym samouczku. Główna różnica polega na wyborze typu transakcji Stowaway: zamiast wybierać `Online`, kliknij `In Person / Manual`. Następnie będziesz musiał ręcznie Exchange PSBT, aby skonstruować transakcję Stowaway. Jeśli jesteś fizycznie blisko swojego współpracownika, możesz kolejno skanować kody QR. Jeśli jesteś na odległość, pliki JSON mogą być wymieniane za pośrednictwem bezpiecznego kanału komunikacji. Pozostała część samouczka pozostaje bez zmian


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

> *Zmusić szpiegów Blockchain do przemyślenia wszystkiego, co myślą, że wiedzą*

PayJoin to specyficzna struktura transakcji Bitcoin, która zwiększa prywatność użytkownika podczas wydatków poprzez współpracę z odbiorcą płatności. Istnieje kilka implementacji, które ułatwiają konfigurację i automatyzację PayJoin. Wśród tych implementacji najbardziej znaną jest Stowaway, opracowana przez zespoły Samourai Wallet. Ten samouczek wyjaśnia, jak wykonać transakcję PayJoin Stowaway przy użyciu aplikacji Samourai Wallet.


## Jak działa Stowaway?


Jak wspomniano wcześniej, Samourai Wallet oferuje narzędzie PayJoin o nazwie "Stowaway" Jest ono dostępne za pośrednictwem oprogramowania Sparrow Wallet na PC lub aplikacji Samourai Wallet na Androida. Aby wykonać PayJoin, odbiorca, który działa również jako współpracownik, musi korzystać z oprogramowania kompatybilnego ze Stowaway, a mianowicie Sparrow lub Samourai. Te dwa oprogramowania są interoperacyjne, umożliwiając transakcję Stowaway między Sparrow Wallet a Samourai Wallet i odwrotnie.


Stowaway opiera się na kategorii transakcji, które Samourai określa jako "Cahoots" Cahoot jest zasadniczo transakcją opartą na współpracy między wieloma użytkownikami, wymagającą informacji off-chain Exchange. Do tej pory Samourai oferuje dwa narzędzia Cahoots: Stowaway (Payjoins) i StonewallX2 (które omówimy w przyszłym artykule).


Transakcje Cahoots obejmują wymianę częściowo podpisanych transakcji między użytkownikami. Proces ten może być długotrwały i uciążliwy, zwłaszcza gdy odbywa się zdalnie. Nadal jednak można go wykonać ręcznie z innym użytkownikiem, co może być wygodne, jeśli współpracownicy są fizycznie blisko siebie. W praktyce wymaga to ręcznej wymiany pięciu kodów QR, które należy kolejno zeskanować.


Gdy odbywa się to zdalnie, proces ten staje się zbyt skomplikowany. Aby rozwiązać ten problem, Samourai opracował szyfrowany protokół komunikacyjny oparty na sieci Tor, zwany "Soroban" Dzięki Soroban wymiana danych niezbędna do PayJoin jest zautomatyzowana za pomocą przyjaznego dla użytkownika Interface. Jest to druga metoda, którą przeanalizujemy w tym artykule.


Te zaszyfrowane wymiany wymagają ustanowienia połączenia i uwierzytelnienia między uczestnikami Cahoots. Komunikacja Soroban opiera się zatem na Paynyms użytkowników. Jeśli nie jesteś zaznajomiony z Paynyms, zapraszam do zapoznania się z tym artykułem po więcej szczegółów: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)



Mówiąc prościej, Paynym to unikalny identyfikator powiązany z Wallet, który umożliwia korzystanie z różnych funkcji, w tym szyfrowanych wiadomości. Paynym jest prezentowany w formie identyfikatora i ilustracji przedstawiającej robota. Oto przykład mojego na Testnet: ![paynym samourai Wallet](assets/en/1.webp)


**Podsumowanie:**


- _Payjoin_ = Specyficzna struktura transakcji opartych na współpracy;
- _Stowaway_ = implementacja PayJoin dostępna na Samourai i Sparrow Wallet;
- _Cahoots_ = Nazwa nadana przez Samourai wszystkim rodzajom transakcji opartych na współpracy, w tym PayJoin Stowaway;
- _Soroban_ = zaszyfrowany protokół komunikacyjny ustanowiony w sieci Tor, umożliwiający współpracę z innymi użytkownikami w kontekście transakcji Cahoots;
- _Paynym_ = Unikalny identyfikator Wallet umożliwiający komunikację z innym użytkownikiem na Sorobanie w celu przeprowadzenia transakcji Cahoots.


[**-> Dowiedz się więcej o transakcjach PayJoin i ich użyteczności**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)


## Jak nawiązać połączenie między Paynyms?


Aby przeprowadzić zdalną transakcję Cahoots, w szczególności PayJoin (Stowaway) za pośrednictwem Samourai, konieczne jest "śledzenie" użytkownika, z którym zamierzasz współpracować, za pomocą jego Paynym. W przypadku pasażera na gapę oznacza to śledzenie osoby, do której chcesz wysłać bitcoiny.


**Oto procedura ustanowienia tego połączenia:**


Aby rozpocząć, należy uzyskać kod płatności Paynym odbiorcy dla PayJoin. W aplikacji Samourai Wallet odbiorca musi dotknąć ikony swojego Paynym (mały robot) znajdującej się w lewym górnym rogu ekranu, a następnie kliknąć swój pseudonim Paynym, zaczynając od `+...`. Na przykład mój to `+namelessmode0aF`. Jeśli twój współpracownik używa Sparrow Wallet, zapraszam do zapoznania się z naszym dedykowanym samouczkiem, klikając tutaj.


![connexion paynym samourai](assets/notext/2.webp)


Współpracownik zostanie przekierowany na swoją stronę Paynym. Stamtąd może udostępnić swoje dane uwierzytelniające Paynym lub udostępnić kod QR do zeskanowania. Aby to zrobić, należy kliknąć małą ikonę "udostępnij" znajdującą się w prawym górnym rogu ekranu.

![partager paynym samourai](assets/en/1.webp)


Po swojej stronie uruchom aplikację Samourai Wallet i uzyskaj dostęp do menu "PayNyms" w ten sam sposób. Jeśli po raz pierwszy korzystasz z Paynyms, musisz uzyskać identyfikator.


![demander un paynym](assets/notext/3.webp)


Następnie kliknij niebieski "+" w prawym dolnym rogu ekranu.

![ajouter paynym collaborateur](assets/notext/4.webp)

Następnie możesz wkleić kod płatności swojego współpracownika, wybierając `COLLER LE CODE PAIEMENT` lub otworzyć kamerę, aby zeskanować jego kod QR, naciskając `SCANNEZ LE CODE QR`.![wklej identyfikator paynym](assets/notext/5.webp)


Kliknij przycisk `SUIVRE`.

![follow paynym](assets/notext/6.webp)

Potwierdź klikając `Tak`.

![confirm follow paynym](assets/notext/7.webp)

Oprogramowanie wyświetli przycisk `SE CONNECTER`. Kliknięcie tego przycisku nie jest konieczne w przypadku naszego samouczka. Ten krok jest wymagany tylko wtedy, gdy planujesz dokonywać płatności na rzecz innego Paynym w ramach BIP47, co nie jest związane z naszym samouczkiem.

![connect paynym](assets/notext/8.webp)

Gdy Paynym odbiorcy będzie podążać za Twoim Paynym, powtórz tę operację w przeciwnym kierunku, aby odbiorca również podążał za Tobą. Następnie możesz wykonać PayJoin.


## Jak zrobić PayJoin na Samourai Wallet?


Jeśli wykonałeś te wstępne kroki, jesteś wreszcie gotowy do przeprowadzenia transakcji PayJoin! Aby to zrobić, postępuj zgodnie z naszym samouczkiem wideo:


![Payjoin Video Tutorial - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)


**Zasoby zewnętrzne:**


- https://docs.samourai.io/en/spend-tools#stowaway.