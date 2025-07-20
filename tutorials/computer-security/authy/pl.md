---
name: Authy 2FA
description: Jak korzystać z aplikacji 2FA?
---
![cover](assets/cover.webp)


W dzisiejszych czasach uwierzytelnianie dwuskładnikowe (2FA) stało się niezbędne do zwiększenia bezpieczeństwa kont internetowych przed nieautoryzowanym dostępem. Wraz ze wzrostem liczby cyberataków, poleganie wyłącznie na haśle w celu zabezpieczenia kont jest czasami niewystarczające. 2FA wprowadza dodatkowy Layer bezpieczeństwa, wymagając drugiej formy uwierzytelnienia oprócz hasła. Weryfikacja ta może przybierać różne formy, takie jak kod wysyłany SMS-em, kod dynamiczny generowany przez dedykowaną aplikację lub użycie fizycznego klucza bezpieczeństwa. Korzystanie z 2FA znacznie zmniejsza ryzyko naruszenia bezpieczeństwa kont, nawet w przypadku kradzieży hasła.


## 2FA za pośrednictwem aplikacji uwierzytelniających


Inne rozwiązania, takie jak fizyczne klucze bezpieczeństwa, omówimy w innych samouczkach, ale w tym proponuję omówić konkretnie aplikacje 2FA. Działanie tych aplikacji jest dość proste: gdy 2FA jest aktywowane na koncie, przy każdym logowaniu zostaniesz poproszony nie tylko o zwykłe hasło, ale także o 6-cyfrowy kod. Kod ten jest generowany przez aplikację 2FA. Ważną cechą tego 6-cyfrowego kodu jest to, że nie jest on statyczny; nowy kod jest generowany przez aplikację co 30 sekund.

![AUTHY 2FA](assets/notext/01.webp)

Odnawianie kodu co 30 sekund znacznie utrudnia atakującemu uzyskanie dostępu do konta. System ten uniemożliwia atakującym ponowne wykorzystanie skradzionego lub przechwyconego kodu, ponieważ szybko wygasa. Tak więc, nawet jeśli atakującemu uda się uzyskać kod, będzie mógł go użyć tylko przez bardzo krótki czas, zanim będzie wymagany nowy kod. Co więcej, fakt, że kod zmienia się tak często, znacznie skraca czas dostępny dla hakera próbującego odgadnąć kod metodą brute force.


2FA za pośrednictwem aplikacji uwierzytelniających stanowi zatem łatwą w użyciu i bezpłatną metodę znacznego zwiększenia bezpieczeństwa kont internetowych.


Istnieje wiele aplikacji do konfigurowania 2FA, wśród których najbardziej znane są Google Authenticator i Microsoft Authenticator. W tym poradniku chciałbym jednak przedstawić inne, mniej znane rozwiązanie o nazwie Authy. Wszystkie te aplikacje działają przy użyciu tego samego protokołu TOTP (*Time based One Time Password*), dzięki czemu ich użycie jest dość podobne.

Authy oferuje kilka zalet w porównaniu z innymi rozwiązaniami dużych firm technologicznych. Przede wszystkim umożliwia synchronizację tokenów 2FA na wielu urządzeniach, co może być przydatne w przypadku utraty lub zmiany telefonu. Authy umożliwia również tworzenie zaszyfrowanych kopii zapasowych generate i przechowywanie ich online, zapewniając, że nigdy nie stracisz dostępu do tokenów, nawet w przypadku utraty głównego urządzenia. Z perspektywy użytkownika Interface osobiście uważam, że Authy oferuje również przyjemniejsze i bardziej intuicyjne doświadczenie niż jego alternatywy.


## Jak zainstalować Authy?


Na smartfonie przejdź do sklepu z aplikacjami (Google Play Store lub Apple Store) i wyszukaj "*Twilio Authy Authenticator*".



- [Apple](https://apps.apple.com/us/app/twilio-authy/id494168017)
- [Android](https://play.google.com/store/apps/details?id=com.authy.authy)

![AUTHY 2FA](assets/notext/02.webp)

Po pierwszym uruchomieniu aplikacji konieczne będzie utworzenie konta. Wybierz kod wybierania w swoim kraju, a także numer telefonu, a następnie kliknij "*Submit*".

![AUTHY 2FA](assets/notext/03.webp)

Wprowadź swój adres e-mail Address, aby odzyskać kod.

![AUTHY 2FA](assets/notext/04.webp)

Zostanie wysłana wiadomość e-mail w celu weryfikacji Address. Wprowadź otrzymane 6 cyfr, aby potwierdzić.

![AUTHY 2FA](assets/notext/05.webp)

Wybierz jedną z dwóch dostępnych metod weryfikacji numeru telefonu. Jeśli zdecydujesz się na otrzymanie wiadomości SMS, wprowadź 6-cyfrowy kod otrzymany w wiadomości, aby potwierdzić swój numer.

![AUTHY 2FA](assets/notext/06.webp)

Gratulacje, konto Authy zostało utworzone!

![AUTHY 2FA](assets/notext/07.webp)

## Jak skonfigurować Authy?


Aby rozpocząć, przejdź do ustawień aplikacji, klikając trzy małe kropki znajdujące się w prawym górnym rogu ekranu.

![AUTHY 2FA](assets/notext/08.webp)

Następnie kliknij "*Ustawienia*".

![AUTHY 2FA](assets/notext/09.webp)

W zakładce "*Moje konto*" masz możliwość modyfikacji swojego konta. Zalecam dodanie kodu PIN do aplikacji poprzez wybranie opcji "*App Protection*". Dodaje to dodatkowe Layer zabezpieczeń dostępu do aplikacji.

![AUTHY 2FA](assets/notext/10.webp)

W zakładce "*Accounts*" można skonfigurować kopię zapasową tokenów. Ta kopia zapasowa umożliwia odzyskanie kodów w przypadku wystąpienia problemu. Jest ona szyfrowana przy użyciu hasła, które należy zdefiniować. Ważne jest, aby to hasło było silne i przechowywane w bezpiecznym miejscu. Konfiguracja tej kopii zapasowej nie jest obowiązkowa, jeśli masz inne metody odzyskiwania, takie jak na przykład drugie urządzenie z tym samym kontem Authy.

![AUTHY 2FA](assets/notext/11.webp)In the "*Devices*" tab, you can see all the devices synchronized with your Authy account. You have the option to disable the use of multiple devices, which restricts access to your account to that device only. If you use only one device, this can increase the security of your account, but make sure you have another backup method in case you lose that device.


Jeśli wolisz zezwolić na dodawanie innych urządzeń, radzę aktywować opcję, która wymaga potwierdzenia z aktualnie autoryzowanych urządzeń na koncie Authy przed dodaniem nowego urządzenia.

![AUTHY 2FA](assets/notext/12.webp)

Aby dodać nowe urządzenie, wystarczy powtórzyć proces instalacji przedstawiony w poprzedniej części, używając tych samych poświadczeń. Następnie zostaniesz poproszony o potwierdzenie nowego dostępu z głównego urządzenia.


## Jak skonfigurować 2FA na koncie?


Aby skonfigurować kod uwierzytelniania 2FA za pośrednictwem aplikacji takiej jak Authy na koncie, konto musi obsługiwać tę funkcję. Obecnie większość usług online oferuje tę opcję 2FA, ale nie zawsze tak jest. Weźmy przykład konta pocztowego Proton, które przedstawiłem w innym poradniku:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

![AUTHY 2FA](assets/notext/13.webp)

Opcję 2FA można zazwyczaj znaleźć w ustawieniach konta, często w sekcji "*Hasło*" lub "*Bezpieczeństwo*".

![AUTHY 2FA](assets/notext/14.webp)

Po aktywowaniu tej opcji na koncie pocztowym Proton zostanie wyświetlony kod QR. Następnie należy zeskanować ten kod QR za pomocą aplikacji Authy.

![AUTHY 2FA](assets/notext/15.webp)

W Authy kliknij przycisk "*+*".

![AUTHY 2FA](assets/notext/16.webp)

Kliknij na "*Scan QR Code*". Następnie zeskanuj kod QR na stronie internetowej.

![AUTHY 2FA](assets/notext/17.webp)

W razie potrzeby możesz również zmienić swoją nazwę użytkownika. Po wprowadzeniu zmian kliknij przycisk "*ZAPISZ*".

![AUTHY 2FA](assets/notext/18.webp)

Następnie Authy wyświetli dynamiczny 6-cyfrowy kod specyficzny dla tego konta, który odświeża się co 30 sekund.

![AUTHY 2FA](assets/notext/19.webp)

Wprowadź ten kod na stronie internetowej, aby sfinalizować konfigurację 2FA.

![AUTHY 2FA](assets/notext/20.webp)

Niektóre witryny udostępniają również kody odzyskiwania po aktywacji 2FA. Kody te umożliwiają dostęp do konta w przypadku utraty dostępu do aplikacji Authy. Zalecam zapisanie ich w bezpiecznym miejscu.

![AUTHY 2FA](assets/notext/21.webp)Your account is now secured with two-factor authentication via the Authy app.

![AUTHY 2FA](assets/notext/22.webp)

Za każdym razem, gdy logujesz się na konto, musisz podać dynamiczny kod wygenerowany przez Authy. Możesz teraz zabezpieczyć wszystkie swoje konta kompatybilne z tą metodą 2FA. Aby dodać nowe konto w Authy, kliknij trzy małe kropki w prawym górnym rogu aplikacji.

![AUTHY 2FA](assets/notext/23.webp)

Następnie kliknij "*Dodaj konto*".

![AUTHY 2FA](assets/notext/24.webp)

Wykonaj te same kroki, co w przypadku pierwszego konta. Różne kody dynamiczne będą widoczne na stronie głównej Authy.