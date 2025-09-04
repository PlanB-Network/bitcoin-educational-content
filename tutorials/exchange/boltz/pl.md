---
name: Boltz
description: Przełączaj się między różnymi warstwami Bitcoin, zachowując kontrolę.
---


![cover](assets/cover.webp)



Od czasu wdrożenia w 2009 r., elektroniczny system gotówkowy peer-to-peer Bitcoin rozwijał się wykładniczo, dając życie rozwiązaniom, które dziś pozwalają mu być systemem, z którego możemy korzystać natychmiast w naszych codziennych działaniach, zwłaszcza za pośrednictwem Lightning Network.



Pozostawał jednak poważny problem pomiędzy warstwami protokołu Bitcoin: płynna interoperacyjność. Aby w pełni wykorzystać potencjał Bitcoin, konieczne było znalezienie rozwiązania, które umożliwiłoby transakcje między różnymi warstwami protokołu. Potrzeba ta doprowadziła w 2019 roku do powstania Boltz, mostu łączącego kilka warstw Bitcoin.



## Co to jest Boltz?



[Boltz](https://boltz.Exchange) to platforma nie wymagająca opieki, idealna dla każdego, kto chce dokonywać transakcji między różnymi warstwami protokołu Bitcoin:




- on chain**: Główny łańcuch Bitcoin, w którym transakcje są potwierdzane średnio co 10 minut, opłaty transakcyjne są często wysokie, co niekoniecznie zaspokaja potrzeby użytkowników;
- Lightning Network**: Nakładka Bitcoin do natychmiastowych płatności przy niskich opłatach, umożliwiająca korzystanie z Bitcoin do codziennych płatności;
- Liquid Network**: nakładka na Bitcoin stworzona przez Blockstream, umożliwiająca szybkie korzystanie z Confidential Transactions i innych instrumentów finansowych opartych na Bitcoin;
- RootStock**: Rozwiązanie do tworzenia inteligentnych kontraktów opartych na protokole Bitcoin.



![layers](assets/fr/01.webp)



Interoperacyjność między tymi różnymi warstwami ma ogromne znaczenie, ponieważ zapewnia użytkownikom elastyczność, której potrzebują, aby w pełni wykorzystać wszystko, co ma do zaoferowania ekosystem Bitcoin.



Boltz wykorzystuje swapy atomowe. Technologia ta umożliwia wymianę bitcoinów między 2 warstwami (np. BTC onchain w Exchange na BTC w Lightning) bezpośrednio między dwiema stronami, bez potrzeby zaufania i bez potrzeby pośrednika. Wymiany te nazywane są "atomowymi", ponieważ mogą przynieść tylko dwa wyniki:




- Albo Exchange zakończy się sukcesem i obaj uczestnicy skutecznie wymienią swoje BTC;
- Albo Exchange się nie powiedzie, a obaj uczestnicy wyjdą z oryginalnymi BTC.



W ten sposób zachowujesz stałą kontrolę nad swoimi bitcoinami, a Exchange nie opiera się na żadnym zaufaniu do kontrahenta: albo Exchange się powiedzie, albo nie, ale żadna ze stron nie może ukraść środków drugiej strony.



Atomowy Exchange współpracuje z inteligentnymi kontraktami [HTLC](https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*). W tym typie Contract kwota jest "blokowana" w kanale dwukierunkowym i wprowadzane jest ograniczenie czasowe, tak że jeśli transakcja nie zostanie zakończona w określonym czasie, saldo powraca do deponenta. Jest to mechanizm wykorzystywany przez platformę Boltz.



## Twoje pierwsze wymiany z Boltzem



Boltz to niedepozytowa platforma internetowa, która nie wymaga od użytkownika podawania żadnych danych osobowych. Boltz ma minimalistyczny, płynny Interface, który pozwala rozpocząć handel w mniej niż minutę.



![boltz](assets/fr/02.webp)



Po wejściu na platformę można tworzyć wymiany atomowe między różnymi warstwami ekosystemu Bitcoin.



![home](assets/fr/03.webp)



Zobaczysz minimalną i maksymalną liczbę satoshi (najmniejsza jednostka Bitcoin), którą możesz handlować za pośrednictwem Boltz, w tym opłaty sieciowe i procent pobierany przez Boltz w wysokości od 0,1% do 0,5%.



![fees](assets/fr/04.webp)



Następnie wybierz Layer, z którego chcesz wykonać atomowy Exchange, i wybierz Layer, na którym chcesz otrzymać bitcoiny.



![couches](assets/fr/05.webp)



W tym samouczku skupimy się na atomowym Exchange od głównego Layer do Lightning Network.



Jednostkę bazową można skonfigurować dla swoich central, wybierając jedną z opcji :




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



Po ukończeniu podstawowych konfiguracji wprowadź kwotę swojego atomowego Exchange, a następnie utwórz Lightning Invoice dla równoważnej kwoty lub po prostu wstaw swój LNURL.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



Aby zachować bezpieczeństwo, sprawdź parametry swojego atomowego Exchange, aby wyeksportować klucze zapasowe powiązane z Exchange.



Na ikonie **Ustawienia** pobierz klucz kopii zapasowej i odpowiednio zapisz plik.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



Plik ten zawiera 12 słów kluczowych portfela powiązanych z giełdami atomowymi.



Następnie kliknij przycisk **Utwórz atomowy Exchange** i dokonaj płatności wskazanej kwoty.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Po dokonaniu i potwierdzeniu płatności, automatycznie otrzymasz jej równowartość na konto Lightning Wallet.



W menu **Refundacja** znajdź historię Exchange, aby zidentyfikować Exchange, na którym chcesz otrzymać zwrot pieniędzy. Można również zaimportować historię wymian dokonanych na innym urządzeniu, na przykład przy użyciu pliku klucza zapasowego powiązanego z tymi wymianami.



![refund](assets/fr/11.webp)



W menu **Historia** można pobrać bardziej szczegółową historię wymian powiązanych z kluczem ratunkowym, klikając przycisk **Kopia zapasowa**.



![backup](assets/fr/12.webp)



⚠️ Prosimy również o nieujawnianie tego pliku, ponieważ zawiera on wszystkie informacje związane z transakcjami i kluczem zapasowym powiązanym z tymi transakcjami.



Boltz oferuje wysoki poziom poufności dzięki dostępowi przez łącze `.onion` w sieci Tor. Spraw, by wymiana atomowa była całkowicie anonimowa, wybierając menu **Onion** po aktywacji przeglądania Tor w przeglądarce.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Na pewno znasz już Boltz, unikalną platformę Exchange, która umożliwia interoperacyjność między różnymi warstwami ekosystemu Bitcoin.