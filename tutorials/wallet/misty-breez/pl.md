---
name: Misty Breez
description: Bezzałogowa Błyskawica Wallet.
---

![misty-breez-cover](assets/cover.webp)



Misty Breez to samoobsługowy Wallet Lightning opracowany przez Breez w oparciu o ich Software Development Kit i sieć **Liquid** opracowaną przez BlockStream.


Oferuje zupełnie nowe podejście do działania bez węzła Lightning: potencjalny **ZMIENIACZ GRY** w transferach międzysieciowych Bitcoin.


W tym samouczku opiszemy, jak działa to portfolio i przedstawimy pełny przegląd.



## Jak działa Misty Breez?



Misty Breez to implementacja bez węzła Lightning jako backendu. Została opracowana na podstawie Breez SDK i Liquid.



Liquid to równoległy Layer do sieci Bitcoin, oferujący znaczną poprawę szybkości i kosztów transakcji. Layer pozwala Misty Breez zrezygnować z węzła Lightning i zamiast tego korzystać z usług Exchange innych firm, takich jak **Boltz**, aby zapewnić interoperacyjność między Liquid Network i Lightning Network. Nie spiesz się, jeszcze do tego wrócimy.



Na razie zacznijmy naszą przygodę z Misty Breez Wallet.



## Pierwsze kroki z Misty Breez



Aplikacja mobilna Misty Breez jest dostępna na oficjalnych platformach pobierania, takich jak Google Play Store (na Androida) i Apple Store (na iOS). Możesz również zostać przekierowany do odpowiedniej aplikacji z oficjalnej strony internetowej [Misty Breez] (https://breez.technology/misty/).



⚠️ Upewnij się, że nie mylisz Misty Breez z Breez Wallet.



⚠️ **WAŻNE**: Dla bezpieczeństwa swoich bitcoinów, konieczne jest pobranie aplikacji z oficjalnych platform, aby zapewnić jej autentyczność.



![download-misty-breez](assets/fr/01.webp)



W tym samouczku zaczniemy od urządzenia z systemem Android. Niemniej jednak każdy z kroków i konkretnych funkcji opisanych w tej sekcji ma zastosowanie do systemu iOS.



Po instalacji Misty Breez daje ci możliwość utworzenia nowego Wallet lub przywrócenia starego Lightning Wallet, dla którego masz słowa odzyskiwania.


W tym samouczku zdecydujemy się utworzyć nowe portfolio.



⚠️Misty Breez jest obecnie w fazie rozwoju, więc radzimy zacząć od rozsądnych kwot.



![create-wallet](assets/fr/02.webp)


### Zapisz słowa odzyskiwania:


Jedną z pierwszych rzeczy, które należy zrobić podczas tworzenia nowego portfolio, jest utworzenie kopii zapasowej 12 słów odzyskiwania.


Oto kilka wskazówek, jak wykonać kopię zapasową frazy kopii zapasowej.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Aby utworzyć kopię zapasową fraz, wybierz menu **Preferencje > Bezpieczeństwo**, a następnie opcję **Sprawdź kopię zapasową fraz**.



![backup](assets/fr/03.webp)


Aby zwiększyć bezpieczeństwo, można również **stworzyć kod PIN** w celu uwierzytelnienia dostępu do Wallet.




Znajdź swoją lokalną walutę wśród wielu walut akceptowanych przez Misty Breez. Skonfiguruj swoją walutę w menu **Preferencje > Waluty Fiata**, a następnie wybierz walutę lub waluty, których potrzebujesz.



![devises](assets/fr/04.webp)



### Dokonywanie pierwszych transakcji


Jeśli jesteś już zaznajomiony z portfolio Breez, intuicyjny Interface Misty Breez wcale Cię nie zniechęci.



W menu Interface **Balance** kliknij opcję **Receive**, aby utworzyć faktury w celu otrzymania bitcoinów na Wallet.



⚠️ Misty Breez poprosi o aktywację powiadomień dla aplikacji w ustawieniach telefonu, aby uzyskać prawo do Lightning Address.



Dzięki Misty Breez możesz :




- Otrzymuj bitcoiny na Lightning Network od **100 satoshi** do **25 000 000 satoshi**.
- Otrzymuj bitcoiny w głównej sieci Bitcoin od **25 000 satoshi**.



![transactions](assets/fr/05.webp)



To tutaj zaczyna się magia Misty Breez.


W przeciwieństwie do Breez Wallet, który zapewnia węzeł Lightning i prosi o samodzielne pokrycie kosztów otwierania i zamykania kanałów płatności, Misty Breez nie prosi o nic. Jak wspomniano wcześniej, Misty Breez nie działa nawet w oparciu o węzeł Lightning.



Przyjrzyjmy się bliżej temu, co dzieje się za kulisami.



W rzeczywistości posiadasz portfel Liquid, który jest powiązany z portfelem Misty Breez. Logicznie rzecz biorąc, będziesz obsługiwać L-BTC (Liquid Bitcoin) po stałych kursach powiązanych z usługami konwersji satelitów podwodnych innych firm, które umożliwią Ci współpracę z Lightning Network.



Po otrzymaniu płatności na Misty Breez Wallet, nadawca wysyła satoshis, które przechodzą przez usługę konwersji, taką jak Boltz (obecnie używaną przez Misty Breez), w celu konwersji wysłanych satoshis na L-BTC, które zostaną odebrane na Misty Breez Wallet (powiązane Liquid Wallet).


Oto uproszczony schemat procesu za kulisami.



![lnswap-in](assets/fr/06.webp)



Kliknij na Interface w menu **Balance**, kliknij na opcję **Send**, aby zapłacić piorunem Invoice.


Włóż kartę Lightning Invoice, kartę Lightning Address odbiorcy lub po prostu zeskanuj kod QR na karcie Invoice, aby dokonać płatności.



![send-bitcoins](assets/fr/07.webp)



Za kulisami umożliwiasz Liquid Wallet powiązanemu z twoim Misty Breez Wallet konwersję równowartości L-BTC na satoshis za pośrednictwem Boltz, a następnie przesyłasz te satoshis do Lightning Wallet odbiorcy (obecnego na Lightning Network).



![send-bitcoin-bts](assets/fr/08.webp)



Ta funkcja infrastruktury Misty Breez umożliwia użytkownikom przeprowadzanie transakcji nawet wtedy, gdy Misty Breez jest offline.



Dla bardziej doświadczonych dostępne jest również menu **Preferencje > Deweloperzy**, które pozwala uzyskać nieco więcej szczegółów na temat :




- Wersja oprogramowania Breez Software Development Kit.
- Klucz publiczny Misty Breez Wallet.
- Pożyczkobiorca, unikalny identyfikator pochodzący z głównego klucza publicznego.
- Saldo portfela.
- Wskazówka Liquid, do wysyłania małych ilości L-BTC.
- Końcówka Bitcoin do wysyłania niewielkich ilości Bitcoin.



Można również wykonywać określone czynności, takie jak synchronizacja z Liquid Network, tworzenie kopii zapasowych kluczy, udostępnianie dziennika aktywności i ponowne skanowanie Liquid Network.



![dev-mode](assets/fr/09.webp)


Gratulacje! Teraz dobrze rozumiesz portfolio Misty Breez i jego wkład w transakcje międzysieciowe Bitcoin. Jeśli ten samouczek okazał się przydatny, prosimy o kciuk Green. Będzie nam niezmiernie miło, jeśli się odezwiesz.



Aby pójść dalej, polecam również zapoznać się z naszym samouczkiem na temat Aqua Wallet, który działa w podobny sposób jak Misty Breez :



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125