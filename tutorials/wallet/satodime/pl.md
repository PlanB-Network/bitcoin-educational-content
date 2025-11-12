---
name: Satodime
description: Dowiedz się, jak korzystać z Satodime za pomocą aplikacji mobilnej
---
![cover](assets/cover.webp)



Ten przewodnik przeprowadzi Cię przez instalację, konfigurację i korzystanie z aplikacji mobilnej Satodime. Dowiesz się, jak wejść w posiadanie karty, tworzyć sejfy, dodawać środki, odpieczętowywać i odzyskiwać klucze prywatne. Dodatki zawierają zasoby, najlepsze praktyki i wyjaśnienia techniczne.



## Wprowadzenie



**Satodime**, opracowany przez **[Satochip](https://satochip.io/fr/)**, jest bezpieczną kartą na okaziciela do przechowywania Bitcoin w namacalny i prosty sposób. Działa ona jako samowystarczalny sprzęt wallet, w którym użytkownik ma pełną kontrolę nad swoimi kluczami prywatnymi bez zależności od strony trzeciej. Posiada certyfikat open-source i EAL6+ i obsługuje do trzech niezależnych sejfów.



### Tło produktu



Satodime, **carte au porteur, należy do każdego, kto fizycznie ją posiada**, bez potrzeby wcześniejszej rejestracji lub identyfikacji. Zaspokaja potrzebę bezpiecznego, przenośnego przechowywania bitcoinów, umożliwiając każdemu, kto posiada kartę, korzystanie z niej lub przesyłanie bitcoinów poprzez skanowanie jej za pośrednictwem aplikacji mobilnej w celu przejęcia lub odblokowania sejfów. W przeciwieństwie do papierowego banknotu, wykorzystuje ona bezpieczny chip do zapieczętowania kluczy prywatnych, które są ujawniane dopiero po odpieczętowaniu, dzięki czemu karta jest podobna do gotówki, gdzie własność jest określana przez fizyczne posiadanie. Idealna do dawania bitcoinów w prezencie, ułatwia bezpieczny transfer bitcoinów z rąk do rąk, podczas gdy aplikacja mobilna wykorzystuje NFC do dostępnej interakcji ze smartfonem.





- Bezpieczeństwo**: Klucze prywatne generowane i przechowywane w odpornym na manipulacje chipie; widoczny stan (zapieczętowany, niezapieczętowany, pusty).
- Funkcje**: Kupuj bitcoiny bezpośrednio przez aplikację (partner Paybis); zarządzaj Mainnet i Testnet.
- Open-source**: Kod na licencji AGPLv3, możliwy do zweryfikowania na GitHub.



### Ciągła ewolucja



Aplikacja jest regularnie rozwijana. Aktualizacje można znaleźć na stronie internetowej Satochip lub w sklepach. Na przykład mogą zostać dodane nowe łańcuchy bloków lub funkcje zakupu. Sprawdź [Satochip GitHub](https://github.com/Toporin/Satodime-Applet) pod kątem bieżących zmian.



## 1. Wymagania wstępne



Przed rozpoczęciem korzystania z **Satodime** upewnij się, że posiadasz następujące elementy:





- Kompatybilny smartfon**: Urządzenie z systemem Android lub iOS z włączoną funkcją NFC.
- Karta Satodime**: Nowa lub niezainicjowana.
- Połączenie internetowe**: Aby pobrać aplikację.
- Podstawowa wiedza**: Zrozumienie kluczy prywatnych/publicznych i ryzyka ich utraty (nieodwracalnej).
- Bezpieczny nośnik**: Bezpieczne miejsce do zapisywania kluczy prywatnych po ich odpieczętowaniu (papier, metal; nigdy cyfrowy).



## 2. Instalacja





- Pobierz aplikację** :
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Sklep Google Play](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Sprawdź dewelopera (Satochip), aby uniknąć oszustwa.
 - Satodime jest oprogramowaniem **open-source**. Kod źródłowy : [Satochip's GitHub](https://github.com/Toporin/Satodime-Applet).





- Zainstaluj i uruchom aplikację**: Aktywuj NFC w telefonie, jeśli to konieczne.



![image](assets/fr/01.webp)



## 3. Konfiguracja początkowa



### 3.1 Uruchom aplikację i skanuj



Otwórz aplikację i postępuj zgodnie z instrukcjami kreatora. Umieść kartę Satodime w czytniku NFC telefonu (zwykle z tyłu). Przytrzymaj ją przez cały czas trwania operacji, aby zapewnić stabilne połączenie.





- Jeśli NFC nie działa, sprawdź ustawienia telefonu.
- Toast potwierdza sukces: "Udanej lektury".



![image](assets/fr/02.webp)



Zgodnie z ogólną zasadą, **wszystkie poniższe operacje będą wymagały potwierdzenia poprzez zeskanowanie karty Satodime**



### 3.2 Wejście w posiadanie karty (*Ownership*)



Przy pierwszym użyciu należy stać się właścicielem karty, aby ją zabezpieczyć:





- Kliknij "*Wybierz Ownership*" w aplikacji.
- Potwierdź operację: spowoduje to wygenerowanie unikalnego klucza właściciela.
- Zeskanuj mapę ponownie, aby zastosować zmiany.
- Ostrzeżenie**: Ten krok jest nieodwracalny. Prosimy o zapoznanie się z [artykułem na temat *własności*] (https://satochip.io/satodime-ownership-explained/).



![image](assets/fr/03.webp)




## 4. Stwórz bezpieczny



Satodime obsługuje do 3 sejfów. Utwórz jeden do przechowywania bitcoinów:





- Wybierz pusty sejf (np. Sejf 01).
- Wybierz blockchain (Bitcoin).
- Kliknij na "*Create & Seal*".
- Zeskanuj kartę do generate i zapieczętuj klucz prywatny (nieznany do momentu odpieczętowania).
- Gratulacje**: Twój sejf jest teraz zapieczętowany i gotowy do przyjmowania środków.



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5. Dodaj fundusze



Po zapieczętowaniu załaduj sejf bitcoinami:





- Wybierz sejf.
- Kliknij "*Dodaj środki*".
- Skopiuj adres publiczny lub zeskanuj kod QR.
- Wysyłanie środków z innego wallet.
- Sprawdź saldo po potwierdzeniu na blockchainie.
- Opcja zakupu: Kliknij "*Zakup*", aby dokonać zakupu bezpośrednio przez Paybis (Visa, Mastercard itp.). Obowiązujące opłaty.



![image](assets/fr/06.webp)



## 6. Rozszczelnienie sejfu



Aby uzyskać dostęp do klucza prywatnego i przenieść środki w inne miejsce, należy odblokować sejf:





- Wybierz zapieczętowany sejf.
- Kliknij przycisk "Odpieczętuj".
- Potwierdź ostrzeżenie: ta operacja jest nieodwracalna.
- Zeskanuj kartę, aby ją odblokować.
- Sejf jest ustawiony na "*Unsealed*"; klucz prywatny może być teraz przeglądany/eksportowany.
- Ostrzeżenie**: Po odblokowaniu klucz prywatny jest dostępny. Jeśli ktoś wejdzie w posiadanie smartfona, może uzyskać dostęp do tego klucza, a tym samym odzyskać środki znajdujące się w sejfie (nieodwracalnie).



![image](assets/fr/07.webp)



## 7. Odzyskaj klucz prywatny



Po rozpieczętowaniu wyeksportuj klucz do użycia w innym wallet:





- Upewnij się, że jesteś w bezpiecznym środowisku.
- Kliknij "*Pokaż klucz prywatny*".
- Wybierz format: Legacy, SegWit, WIF itp.
- Skopiuj klucz lub zeskanuj kod QR.
- Bezpieczeństwo**: Nigdy nie udostępniaj swojego klucza prywatnego. Przechowuj go offline.
- Zaimportuj go do programu wallet kompatybilnego z zarządzaniem funduszami (na przykład Sparrow, Wallet lub Electrum).



![image](assets/fr/08.webp)





## 8. Reset bagażnika



Zresetowanie sejfu nieodwracalnie usuwa powiązany z nim klucz prywatny. Innymi słowy, jeśli nie zabezpieczyłeś kopii swojego klucza prywatnego lub nie zaimportowałeś go do innego wallet, zresetowanie sejfu spowoduje nieodwracalną utratę znajdujących się w nim środków.



![image](assets/fr/09.webp)



Zresetowanie modułu powoduje, że gniazdo jest puste i gotowe na nowy moduł.



## 9. Przeniesienie własności



Aby - na przykład - oferować bitcoiny za pośrednictwem Satodime, musisz :




- Przejmij odpowiedzialność za kartę,
- Utwórz sejf Bitcoin,
- Transfer odbywa się tam,
- Przeniesienie własności karty: kolejna osoba, która zeskanuje kartę, staje się jej właścicielem,
- Przekaż kartę Satodime wybranej osobie i poproś ją o pobranie aplikacji, a następnie zeskanowanie karty, aby przejąć ją na własność - a tym samym uzyskać dostęp do "przechowywanych" na niej bitcoinów.



![image](assets/fr/10.webp)




## DODATKI



### A1. Najlepsze praktyki



Aby bezpiecznie korzystać z **Satodime** :





- Zabezpiecz kartę**: Traktuj ją jak gotówkę; utrata = utrata środków, jeśli nie właściciela.
- Kopia zapasowa kluczy**: Po rozpieczętowaniu należy zapisać klucze prywatne na bezpiecznym nośniku fizycznym. Nigdy w formie cyfrowej.
- Sprawdź status**: Zawsze skanuj, aby potwierdzić własność karty i stan zapieczętowania/rozpieczętowania sejfów.
- Poufność**: Używaj nowych adresów; unikaj scentralizowanej wymiany transferów.
- Aktualizacje**: Aktualizuj aplikację za pośrednictwem sklepów.
- Odzyskiwanie**: Jeśli karta została zgubiona, ale jest własnością, środki znajdują się w łańcuchu bloków; w przypadku odpieczętowania należy użyć klucza prywatnego.



### A2. Dodatkowe zasoby



Specyficzne dla Satodime :




- [Produkt Satodime](https://satochip.io/fr/product/satodime/)
- [Przewodnik mobilny](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Academy](https://planb.academy/) dla samouczków na temat samodzielnego przechowywania, kluczy prywatnych itp.



**Zapisz swoją frazę odzyskiwania** :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Samouczek dotyczący Satochip (pierwszego produktu marki) :**



https://planb.academy/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Samouczki dla opiekunów nasion:**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. O Satochip



**Oficjalne linki** :




- [Site Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Wsparcie: info@satochip.io



**Satochip** to belgijska firma, która opracowuje rozwiązania sprzętowe i programowe do zarządzania i przechowywania bitcoinów i innych kryptowalut. Jej flagowy produkt, sprzęt Satochip wallet, to karta NFC wyposażona w secure element z certyfikatem EAL6+. Uzupełniony o Seedkeeper, mnemoniczną frazę i tajny menedżer, oraz Satodime, kartę na okaziciela, Satochip oferuje kompleksową gamę dostosowaną do potrzeb użytkowników. Jej urządzenia, oparte na oprogramowaniu open source, mają na celu demokratyzację bezpieczeństwa na Bitcoin.