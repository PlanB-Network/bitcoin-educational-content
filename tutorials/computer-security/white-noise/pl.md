---
name: White Noise
description: Prywatna, zdecentralizowana aplikacja do przesyłania wiadomości oparta na protokołach Nostr i MLS
---

![cover](assets/cover.webp)




## Wprowadzenie



"Pośród trudności kryje się szansa". Ten cytat Alberta Einsteina przypomina nam, że problemy nie są ostateczne, ale zawierają w sobie nasiona nowych, innowacyjnych rozwiązań.



Motywacje stojące za uruchomieniem rozwiązania, które prezentujemy w tym samouczku, doskonale to ilustrują. Jest to **White Noise**, zrodzony z konieczności.



Według słów jego założyciela, Maxa Hillebranda, opisanych przez *Bitcoin Magazine*: "Uruchomiliśmy ten projekt z braku alternatyw" Wyjaśnia on, że "istniejące aplikacje szyfrujące są nieefektywne na dużą skalę: dodanie 100 osób do rozmowy grupowej znacznie spowalnia szyfrowanie. Tymczasem zdecentralizowane platformy nie oferują prywatnych wiadomości. Wreszcie, otwarta sieć Nostr pozwala każdemu na rozpowszechnianie pomysłów, ale ochrona bezpośrednich wiadomości pozostaje dramatycznie niewystarczająca. Zdaliśmy sobie sprawę, że aby chronić wolność, musimy połączyć te systemy"



## Co to jest White Noise?



White Noise to aplikacja open source do przesyłania wiadomości opracowana przez zespół non-profit. Aplikacja promuje bezpieczeństwo, prywatność i decentralizację. W przeciwieństwie do konwencjonalnych aplikacji, nie wymaga ani numeru telefonu, ani adresu e-mail.


White Noise wyróżnia się integracją dwóch podstawowych protokołów - Nostr i MLS - które stanowią jego podstawę techniczną.



Nostr (Notes and Other Stuff Transmitted by Relays) to zdecentralizowany protokół o otwartym kodzie źródłowym zaprojektowany z myślą o ochronie przed cenzurą.  Protokół wykorzystuje przekaźniki, pary kluczy i klientów.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Dzięki funkcji White Noise można nawet wybrać własne ustawienia przekaźnika, aby zmaksymalizować prywatność.



Z drugiej strony MLS (Messaging Layer Security) to protokół bezpieczeństwa, który umożliwia szyfrowanie wiadomości od końca do końca. Innymi słowy, wiadomości są dostępne tylko w punktach końcowych, tj. u nadawcy i odbiorcy wiadomości. Oznacza to, że przekaźniki zaangażowane w routing wiadomości nie mogą uzyskać dostępu do ich treści.



Oto krótkie porównanie White Noise z kilkoma najbardziej znanymi aplikacjami do przesyłania wiadomości.



| Points de comparaisons      | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| Chiffrement E2EE / 1:1      | ✅ Oui       | Facultatif | ✅ Oui           | ✅ Oui   | ✅ Oui    | ✅ Oui            | ✅ Oui  |
| Chiffrement de groupe E2EE  | ✅ Oui       | ❌ Non      | ✅ Oui           | ✅ Oui   | ✅ Oui    | Facultatif       | ✅ Oui  |
| Anonymisation de l'identité | ✅ Oui       | Facultatif | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Serveur open source         | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Client open source          | ✅ Oui       | ✅ Oui      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Serveur décentralisé        | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Année de création           | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |


## Rozpoczęcie pracy z White Noise



### Instalacja White Noise



Wejdź na stronę [White Noise website](https://www.whitenoise.chat/), a następnie kliknij **Download**.



![screen](assets/fr/03.webp)



White Noise jest obecnie dostępny tylko na urządzeniach mobilnych.


W nowo wyświetlonym interfejsie naciśnij :





- przycisk **Zapstore** lub **Android APK**, jeśli chcesz pobrać go na Androida;
- na przycisku **iOS TestFlight**, jeśli używasz iPhone'a.



![screen](assets/fr/04.webp)



Na potrzeby tego samouczka przeprowadzimy pobieranie systemu Android.


Jeśli wybierzesz pobieranie przez **Zapstore**, zostaniesz do niego przekierowany. Po wejściu na Zapstore, wpisz **White Noise** w pasku wyszukiwania. Następnie przejdź do pobierania, klikając **Install**.



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



Jeśli zdecydujesz się pobrać plik APK, zostaniesz przekierowany do repozytorium White Noise GitHub, aby wybrać odpowiednią wersję dla swojego smartfona.



Dostępne pliki APK to :





- whitenoise-0.2.1-arm64-v8a.apk** (57,7 MB), odpowiedni dla najnowszych telefonów z 64-bitowymi procesorami;
- whitenoise-0.2.1-armeabi-v7a.apk** (47,5 MB) odpowiedni dla starszych telefonów z 32-bitowymi procesorami.



Dostępne są również pliki **.sha256**, które są jedynie sumami kontrolnymi służącymi do weryfikacji integralności pobranego pliku.



![screen](assets/fr/07.webp)



Po zakończeniu pobierania zainstaluj i otwórz aplikację.



![screen](assets/fr/08.webp)



### Początkowa konfiguracja konta użytkownika



Aby nawiązać pierwsze połączenie z White Noise, naciśnij przycisk **Register**.



![screen](assets/fr/09.webp)



Następnie skonfiguruj swój profil, wybierając zdjęcie profilowe, nazwę i dodając krótki opis swojej osoby. Nie musisz podawać swojej prawdziwej tożsamości (imienia i zdjęcia).


Zwróć uwagę, że White Noise automatycznie wybierze dla ciebie nazwę (pseudonim), którą możesz zachować lub zmienić. Na koniec naciśnij przycisk **End**.



![screen](assets/fr/10.webp)



Zostaniesz przekierowany do **ekranu głównego** White Noise, gdzie będą wyświetlane Twoje rozmowy. Twoje konto jest teraz skonfigurowane i gotowe do użycia. Możesz udostępnić swój profil lub wyszukać znajomych, aby rozpocząć czat.



![screen](assets/fr/11.webp)




### Wykrywanie interfejsów White Noise



W głównym interfejsie, w górnej części ekranu zobaczysz :



Ikona profilu w lewym górnym rogu to miniatura zdjęcia profilowego lub pierwsza litera nazwy profilu. Kliknij ją, aby uzyskać dostęp do ustawień konta.



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



W prawym górnym rogu znajduje się ikona umożliwiająca rozpoczęcie nowej rozmowy.



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## Ustawienia konta użytkownika



Naciśnij ikonę profilu w lewym górnym rogu, aby uzyskać dostęp do ustawień.



![screen](assets/fr/16.webp)



W górnej części interfejsu **Ustawień** znajdziesz swoje zdjęcie i nazwę profilu, a następnie klucz publiczny, który możesz udostępnić za pomocą znajdującego się obok kodu QR.



![screen](assets/fr/17.webp)



Tuż poniżej znajduje się przycisk **Zmień konto**, który pozwala połączyć się z innym profilem w aplikacji.



![screen](assets/fr/18.webp)



Następnie masz pierwszą sekcję z czterema (4) podmenu, takimi jak :





- Modyfikacja profilu**



W tym podmenu można zmodyfikować nazwę profilu, adres Nostr (NIP-05).... Nie zapomnij kliknąć **Zapisz**, aby zapisać zmiany.



![screen](assets/fr/19.webp)





- Klucze profilu**



Tutaj masz dostęp do swoich publicznych i prywatnych (tajnych) kluczy. Jak przypomina White Noise, klucz prywatny nie może być ujawniany pod żadnym pozorem.



![screen](assets/fr/20.webp)





- Przekaźnik sieciowy



W tym podmenu można dodawać lub usuwać **przekaźniki ogólne** (przekaźniki zdefiniowane do użytku we wszystkich aplikacjach Nostr), **przekaźniki wewnętrzne** i **przekaźniki pakietu kluczy**.



Aby to zrobić, dotknij ikony **śmieci** przed przekaźnikiem, aby go usunąć, lub dotknij ikony **+** (plus), aby dodać nowy.



![screen](assets/fr/21.webp)





- Rozłączanie**



Kliknij to podmenu, aby odłączyć swoje konto od aplikacji. Upewnij się jednak, że zapisałeś swoje klucze prywatne w trybie offline, w przeciwnym razie nie będziesz mógł zalogować się ponownie później.



![screen](assets/fr/22.webp)




Druga sekcja oferuje podmenu:





- Ustawienia aplikacji



Tutaj możesz zdefiniować wygląd (motyw i język wyświetlania) aplikacji, a nawet usunąć dane, jeśli uważasz, że zostały naruszone lub jeśli sam czujesz się zagrożony.



![screen](assets/fr/23.webp)





- Przekaż darowiznę na rzecz White Noise



Możesz wesprzeć zespół stojący za White Noise (organizacja non-profit) darowiznami za pośrednictwem ich adresu Lightning lub adresu cichej płatności Bitcoin.



![screen](assets/fr/24.webp)



Na samym dole znajdują się **ustawienia deweloperskie**.



![screen](assets/fr/25.webp)




## Rozpocznij rozmowę



Przyjrzyjmy się teraz, jak rozpocząć rozmowę. W chwili pisania tego tekstu White Noise oferuje trzy opcje komunikacji. Po kolei przyjrzymy się **Rozmowom prywatnym** (**Chat 1:1**), tj. tylko między tobą a jedną inną osobą, **Rozmowom grupowym** i **Wysyłaniu plików multimedialnych**.




### Kat 1:1



W głównym interfejsie, aby dodać nowego korespondenta, kliknij ikonę rozpoczęcia nowej konwersacji.


Następnie zeskanuj kod QR klucza publicznego (1) lub wklej klucz publiczny (2) nowego korespondenta do paska wyszukiwania, aby go znaleźć.



![screen](assets/fr/26.webp)



Następnie dotknij przycisku **Rozpocznij rozmowę**, aby rozpocząć rozmowę z korespondentem. Możesz także **Śledzić** swojego korespondenta lub zaprosić go do rozmowy grupowej, naciskając przycisk **Dodaj do grupy**.



![screen](assets/fr/27.webp)



Pierwsza wiadomość do nowego korespondenta przypomina prośbę o zaproszenie. Prośba ta musi zostać zaakceptowana przez korespondenta, zanim będzie można się z nim komunikować. Jeśli odmówi, rozmowa nie będzie możliwa.



![screen](assets/fr/28.webp)



Co więcej, dopóki nie zaakceptują zaproszenia, nie będą mogli przeczytać treści początkowej wiadomości.



Po zaakceptowaniu przez niego zaproszenia, może on teraz odpowiedzieć, a wy możecie komunikować się płynnie i bezpiecznie.



![screen](assets/fr/29.webp)



Co więcej, w dyskusji masz dodatkowe funkcje.



Długie naciśnięcie określonego komunikatu powoduje wyświetlenie opcji takich jak :




- zareagować na wiadomość za pomocą emoji (1) ;
- utwórz **bezpośredni cytat**, aby odpowiedzieć na wiadomość, naciskając **Odpowiedź** (2) ;
- skopiować wiadomość, naciskając przycisk **Kopiuj** (3).



![screen](assets/fr/30.webp)





- usuń wiadomość za pomocą przycisku **Usuń** tylko wtedy, gdy pochodzi ona od Ciebie.



![screen](assets/fr/31.webp)



Można wyszukiwać w obrębie konwersacji.



Kliknij awatar korespondenta w górnej części ekranu, aby uzyskać dostęp do "informacji o konwersacji" i dotknij przycisku **Szukaj w konwersacji**.



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



W wyświetlonym pasku wyszukiwania wpisz słowo, które chcesz wyszukać i uruchom wyszukiwanie. Wyszukiwane słowa zostaną wyróżnione **pogrubioną czcionką**.



![screen](assets/fr/34.webp)




### Rozmowy grupowe



Grupy konwersacyjne można tworzyć na White Noise.



Aby to zrobić, dotknij ikony w interfejsie uruchamiania nowej konwersacji, a następnie kliknij **Nowa konwersacja grupowa**. Następnie w pasku wyszukiwania wprowadź klucz publiczny pierwszego członka, którego chcesz dodać do grupy.



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



Ostatecznie, jeśli ta opcja nie zadziała, w interfejsie **Rozpocznij nową konwersację** wprowadź klucz publiczny pierwszego członka, którego chcesz dodać do grupy w pasku wyszukiwania. Możesz również zeskanować kod QR powiązany z jego kluczem publicznym.



Tym razem, zamiast naciskać przycisk **Rozpocznij rozmowę**, kliknij przycisk **Dodaj do grupy**.



![screen](assets/fr/37.webp)



W wyświetlonym menu podręcznym dotknij **Nowa rozmowa grupowa**.



![screen](assets/fr/38.webp)



Następnie naciśnij **Kontynuuj** (nie musisz ponownie wprowadzać klucza publicznego).



![screen](assets/fr/39.webp)



Jako twórca grupy jesteś automatycznie jej administratorem. Wypełnij szczegóły grupy, takie jak **nazwa i opis grupy**, a następnie kliknij przycisk **Utwórz grupę**.



![screen](assets/fr/40.webp)



Użytkownik dodany jako pierwszy członek oraz inni dodani później otrzymają powiadomienie z zaproszeniem do dołączenia do grupy. Aby dołączyć do grupy, muszą zaakceptować zaproszenie, klikając przycisk **Accept**.



![screen](assets/fr/41.webp)



Możliwe jest również dodanie nowego członka, z którym już rozmawiasz, do istniejącej grupy. Aby to zrobić, kliknij awatar korespondenta w górnej części ekranu, aby uzyskać dostęp do "informacji o rozmowie" i dotknij przycisku **Dodaj do grupy**.



![screen](assets/fr/42.webp)



W nowym interfejsie, który się pojawi, **zaznacz** grupę, do której chcesz go dodać i dotknij **Dodaj do grupy**. Pozostaje tylko poczekać, aż zgodzi się dołączyć do grupy.



![screen](assets/fr/43.webp)



Należy pamiętać, że tylko administrator grupy może modyfikować informacje o grupie oraz dodawać lub usuwać członków. Ponadto rotacja kluczy uniemożliwia zablokowanym członkom odszyfrowanie przyszłych wiadomości.



Aby usunąć członka, w głównym interfejsie grupy dotknij ikony grupy u góry, aby uzyskać dostęp do interfejsu informacji o grupie.



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



Następnie kliknij nazwę członka i **Usuń z grupy**. Z poziomu tego interfejsu możesz również wysłać mu wiadomość, obserwować go lub dodać do innej grupy.



![screen](assets/fr/46.webp)



### Wysyłanie plików multimedialnych



Na chwilę obecną w White Noise można udostępniać tylko zdjęcia między użytkownikami. Niezależnie od tego, czy prowadzisz prywatną rozmowę, czy czat grupowy, aby to zrobić, musisz :





- naciśnij symbol **plus (+)** po lewej stronie pola wprowadzania wiadomości tekstowej.



![screen](assets/fr/47.webp)





- następnie kliknij pole oznaczone **Photos** na dole, aby uzyskać dostęp do swojej galerii.



![screen](assets/fr/48.webp)





- wybierz zdjęcia do wysłania.



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## Kluczowe punkty do zapamiętania



White Noise oferuje dobry poziom poufności i najwyższy poziom bezpieczeństwa. Z drugiej strony jest to bardzo nowa aplikacja, niezbyt rozpowszechniona i wciąż w powijakach. W związku z tym jest jeszcze zbyt wcześnie, aby wyciągać jakiekolwiek aktywne wnioski. Możliwe jest napotkanie kilku usterek podczas użytkowania.



Obecnie brakuje mu pewnych funkcji (brak połączeń audio lub wideo, brak wysyłania plików multimedialnych audio lub wideo) w porównaniu z popularnymi aplikacjami do przesyłania wiadomości.



Niemniej jednak White Noise pozostaje interesującą opcją dla rozmów, w których poufność jest najważniejsza (np. z rodziną, bliskimi przyjaciółmi lub aktywistami we wspólnej sprawie), nawet jeśli wymaga trochę wysiłku, aby zainstalować (za pośrednictwem alternatywnych sklepów z aplikacjami lub plików APK) i nauczyć się (opanowując nieco koncepcję par kluczy, klientów i przekaźników z protokołem Nostr).



Teraz już wiesz, jak używać White Noise do bezpiecznej komunikacji ze znajomymi i rodziną. Daj nam kciuka w górę, jeśli uznasz ten poradnik za przydatny.



Polecamy nasz samouczek na temat Tox Chat, aplikacji, która pozwala rozmawiać bez pośredników za pośrednictwem zdecentralizowanego protokołu Tox.



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3