---
name: NOSTR

description: Odkryj i zacznij korzystać z NOSTR
---

Pod koniec tego przewodnika zrozumiesz, czym jest Nostr, utworzysz konto i będziesz mógł z niego korzystać.


![A new challenger has arrived](assets/1.webp)


## Czym jest Nostr?


Nostr to protokół, który może zastąpić Twittera, Telegram i inne platformy mediów społecznościowych. Jest to prosty, otwarty protokół zdolny do stworzenia globalnie odpornej sieci społecznościowej raz na zawsze.


## Jak to działa?


Nostr opiera się na trzech komponentach: parach kluczy, klientach i przekaźnikach.


Każdy użytkownik ma jedną lub więcej tożsamości, a każda tożsamość jest określana przez parę kluczy kryptograficznych.


Aby uzyskać dostęp do sieci, należy użyć oprogramowania klienckiego i połączyć się z przekaźnikami w celu odbierania i przesyłania treści.


![Key system](assets/2.webp)


## 1. Klucze kryptograficzne


W przeciwieństwie do Facebooka czy Twittera, gdzie użytkownicy muszą podać prywatnej firmie adres e-mail Address i mnóstwo informacji, Nostr działa bez centralnego organu. Użytkownicy generate posiadają parę kluczy kryptograficznych, klucz tajny (znany również jako klucz prywatny) i klucz publiczny.


Tajny klucz, nsec, znany tylko użytkownikowi, jest używany do uwierzytelniania i publikowania treści.


Klucz publiczny, npub, jest unikalnym identyfikatorem, do którego dołączane są wszystkie treści publikowane przez użytkownika. Twój klucz publiczny jest jak nazwa użytkownika, która pozwala innym użytkownikom znaleźć cię i zasubskrybować twój kanał Nostr.


## 2. Klienci


Klienci to oprogramowanie umożliwiające interakcję z Nostr. Głównymi klientami są:



- iOS: damus
- Android: ametyst
- Sieć: iris.to; snort.social; astral.ninja


Klienci umożliwiają użytkownikom generate utworzenie nowej pary kluczy (co jest równoznaczne z utworzeniem konta) lub uwierzytelnienie za pomocą istniejącej pary kluczy.


## 3. Przekaźniki


Przekaźniki to uproszczone serwery, które można opuścić w dowolnym momencie, jeśli nie podoba nam się dostarczana przez nie zawartość. Jeśli chcesz, możesz również uruchomić własny przekaźnik.


**Pro tip:** Płatne przekaźniki są generalnie bardziej skuteczne w filtrowaniu spamu i niechcianych treści.


### Przewodnik


Teraz wiesz już wystarczająco dużo o Nostr, aby zacząć i stworzyć swoją pierwszą tożsamość w tym protokole.


Do celów tego przewodnika będziemy używać iris.to (https://iris.to/), ponieważ ten klient internetowy działa na dowolnej platformie.


## Krok 1: Generowanie kluczy


ris utworzy dla ciebie zestaw kluczy bez konieczności robienia czegokolwiek poza wprowadzeniem nazwy (prawdziwej lub fikcyjnej) dla twojego profilu. Następnie kliknij GO i gotowe!


![Main menu](assets/3.webp)


⚠️ **Uwaga!** Będziesz musiał śledzić swoje klucze, jeśli chcesz mieć dostęp do swojego profilu ponownie po zamknięciu sesji. Pokażę ci, jak to zrobić na samym końcu tego przewodnika.


## Krok 2: Publikowanie treści


Publikowanie treści jest tak proste i intuicyjne, jak napisanie kilku słów w polu publikacji.


![Publication](assets/4.webp)


No i proszę! Opublikowałeś swoją pierwszą notkę na Nostr.


![Post](assets/5.webp)


## Krok 3: Znajdź przyjaciela


Znajdź mnie na Nostr i nigdy więcej nie bądź sam. Zasubskrybuję z powrotem każdego, kto zasubskrybuje mój kanał. Aby to zrobić, wystarczy wprowadzić mój klucz publiczny


npub1hartx53w6t3q5wv9xdqdwrk7h6r5866t8u775q0304zedpn5zgssasp7d3 w pasku wyszukiwania.


![My profile](assets/6.webp)


Kliknij "śledź", a w ciągu kilku dni zasubskrybuję również Twój kanał. Będziemy przyjaciółmi. Chętnie przeczytam też Twoją wiadomość, jeśli zechcesz do mnie napisać.


Na koniec, zasubskrybuj kanał Agora256, aby otrzymywać powiadomienia za każdym razem, gdy opublikujemy coś nowego: npub1ag0rawstycy7nanuc6sz4v287rneen2yapcq3fd06972f8ncrhzqx


## Krok 4: Dostosuj swój profil


Nadal musisz wykonać trochę pracy, aby dostosować swój profil. Aby to zrobić, kliknij awatar, który iris automatycznie wygenerował dla Ciebie w prawym górnym rogu ekranu, a następnie kliknij "edytuj profil".


![Profile](assets/7.webp)


Wszystko, co musisz teraz zrobić, to powiedzieć iris, gdzie znaleźć swoje zdjęcie i baner profilowy w Internecie. Zalecam hosting własnych treści: chroń to, co należy do ciebie.


![Another option](assets/8.webp)


Jeśli wolisz, możesz również przesyłać obrazy, które będą przechowywane przez iris na nostr.build, bezpłatnej usłudze hostingu treści wizualnych dla Nostr.


Jak widać, można również skonfigurować klienta tak, aby mógł odbierać i wysyłać Sats. W ten sposób możesz nagradzać autorów treści, które Ci się spodobały lub, jeszcze lepiej, gromadzić Sats za świetne treści, które opublikujesz.


## Krok 5: Utworzenie kopii zapasowej pary kluczy


Ten krok jest kluczowy, jeśli chcesz zachować dostęp do swojego profilu po wylogowaniu się z klienta lub wygaśnięciu sesji.

Najpierw kliknij ikonę "ustawień" reprezentowaną przez koło zębate

![Setting](assets/9.webp)


Następnie skopiuj i wklej po kolei swoje npub, npub hex, nsec i nsec hex do pliku tekstowego, który będziesz przechowywać w bezpiecznym miejscu. Zalecam zaszyfrowanie tego pliku, jeśli wiesz, jak to zrobić.


![Key](assets/10.webp)


⚠️ **Zwróć uwagę na ostrzeżenie, które daje ci iris:** podczas gdy możesz bez obaw udostępniać swój klucz publiczny, inaczej jest w przypadku klucza prywatnego. Każdy, kto posiada ten ostatni, będzie mógł uzyskać dostęp do konta.


## Wnioski


Proszę bardzo, mały strusiu, postawiłeś swoje pierwsze kroki na Nostr. Teraz musisz nauczyć się działać z prędkością błyskawicy. Wkrótce opublikujemy przewodniki, które pokażą ci, jak zarządzać kluczami i jak zintegrować błyskawicę z doświadczeniem Nostr za pomocą getalby.