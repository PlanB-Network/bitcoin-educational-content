---
name: YubiKey 2FA
description: Jak używać fizycznego klucza bezpieczeństwa?
---
![cover](assets/cover.webp)


W dzisiejszych czasach uwierzytelnianie dwuskładnikowe (2FA) stało się niezbędne do zwiększenia bezpieczeństwa kont internetowych przed nieautoryzowanym dostępem. Wraz ze wzrostem liczby cyberataków, poleganie wyłącznie na haśle w celu zabezpieczenia kont jest czasami niewystarczające.


2FA wprowadza dodatkowy Layer bezpieczeństwa, wymagając drugiej formy uwierzytelnienia oprócz tradycyjnego hasła. Weryfikacja ta może przybierać różne formy, takie jak kod wysyłany SMS-em, kod dynamiczny generowany przez dedykowaną aplikację lub użycie fizycznego klucza bezpieczeństwa. Korzystanie z 2FA znacznie zmniejsza ryzyko naruszenia bezpieczeństwa kont, nawet w przypadku kradzieży hasła.


W innym poradniku wyjaśniłem, jak skonfigurować i korzystać z aplikacji TOTP 2FA:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Tutaj zobaczymy, jak używać fizycznego klucza bezpieczeństwa jako drugiego czynnika uwierzytelniania dla wszystkich kont.


## Czym jest fizyczny klucz bezpieczeństwa?


Fizyczny klucz bezpieczeństwa to urządzenie służące do zwiększania bezpieczeństwa kont internetowych poprzez uwierzytelnianie dwuskładnikowe (2FA). Urządzenia te często przypominają małe klucze USB, które należy włożyć do portu komputera, aby zweryfikować, czy jest to rzeczywiście uprawniony użytkownik próbujący się połączyć.

![SECURITY KEY 2FA](assets/notext/01.webp)

Logując się do konta chronionego przez 2FA i używając fizycznego klucza bezpieczeństwa, musisz nie tylko wprowadzić swoje zwykłe hasło, ale także włożyć fizyczny klucz bezpieczeństwa do komputera i nacisnąć przycisk, aby potwierdzić uwierzytelnienie. Metoda ta dodaje zatem dodatkowy Layer bezpieczeństwa, ponieważ nawet jeśli komuś uda się uzyskać hasło, nie będzie w stanie uzyskać dostępu do konta bez fizycznego posiadania klucza.


Fizyczny klucz bezpieczeństwa jest szczególnie skuteczny, ponieważ łączy w sobie dwa różne rodzaje czynników uwierzytelniania: dowód wiedzy (hasło) i dowód posiadania (klucz fizyczny).


Jednak ta metoda 2FA ma również wady. Po pierwsze, klucz bezpieczeństwa musi być zawsze dostępny, jeśli chcesz uzyskać dostęp do swoich kont. Konieczne może być dodanie go do pęku kluczy. Po drugie, w przeciwieństwie do innych metod 2FA, korzystanie z fizycznego klucza bezpieczeństwa wiąże się z początkowym kosztem, ponieważ musisz kupić małe urządzenie. Cena kluczy bezpieczeństwa zazwyczaj waha się od 30 do 100 euro w zależności od wybranych funkcji.


## Który klucz bezpieczeństwa fizycznego wybrać?


Aby wybrać klucz bezpieczeństwa, należy wziąć pod uwagę kilka kryteriów.

Przede wszystkim należy sprawdzić protokoły obsługiwane przez urządzenie. Jako minimum radzę wybrać klucz, który obsługuje OTP, FIDO2 i U2F. Szczegóły te są zwykle podkreślane przez producentów w opisach produktów. Aby zweryfikować kompatybilność każdego klucza, można również odwiedzić stronę [dongleauth.com](https://www.dongleauth.com/dongles/).

Upewnij się również, że klucz jest kompatybilny z twoim systemem operacyjnym, mimo że znane marki, takie jak Yubikey, zazwyczaj obsługują wszystkie powszechnie używane systemy.


Klucz należy również wybrać w oparciu o typ portów dostępnych w komputerze lub smartfonie. Na przykład, jeśli komputer ma tylko porty USB-C, wybierz klucz ze złączem USB-C. Niektóre klucze oferują również opcje połączenia przez Bluetooth lub NFC.

![SECURITY KEY 2FA](assets/notext/02.webp)

Można również porównywać urządzenia w oparciu o ich dodatkowe funkcje, takie jak odporność na wodę i Dust, a także kształt i rozmiar klawisza.


Jeśli chodzi o marki kluczy bezpieczeństwa, najbardziej znana jest firma Yubico z urządzeniami [YubiKey](https://www.yubico.com/), których osobiście używam i polecam. Google oferuje również urządzenie z [Titan Security Key](https://store.google.com/fr/product/titan_security_key). Jeśli chodzi o alternatywy open-source, [SoloKeys](https://solokeys.com/) (bez OTP) i [NitroKey](https://www.nitrokey.com/products/nitrokeys) są interesującymi opcjami, ale nigdy nie miałem okazji ich przetestować.


## Jak używać fizycznego klucza bezpieczeństwa?


Po otrzymaniu klucza zabezpieczeń nie jest wymagana żadna specjalna konfiguracja. Klucz jest zwykle gotowy do użycia po otrzymaniu. Można go natychmiast użyć do zabezpieczenia kont online, które obsługują ten typ uwierzytelniania. Na przykład pokażę ci, jak zabezpieczyć moje konto pocztowe Proton za pomocą tego fizycznego klucza bezpieczeństwa.

![SECURITY KEY 2FA](assets/notext/03.webp)

Opcja aktywacji 2FA znajduje się w ustawieniach konta, często w sekcji "*Hasło*" lub "*Bezpieczeństwo*". Kliknij pole wyboru lub przycisk, który umożliwia aktywację 2FA za pomocą klucza fizycznego.

![SECURITY KEY 2FA](assets/notext/04.webp)

Podłącz klucz do komputera.

![SECURITY KEY 2FA](assets/notext/05.webp)

Dotknij przycisku na kluczu bezpieczeństwa, aby zatwierdzić.

![SECURITY KEY 2FA](assets/notext/06.webp)

Wprowadź nazwę, aby zapamiętać użyty przycisk.

![SECURITY KEY 2FA](assets/notext/07.webp)

I gotowe, klucz bezpieczeństwa został pomyślnie dodany do uwierzytelniania 2FA konta.

![SECURITY KEY 2FA](assets/notext/08.webp)

W moim przykładzie, jeśli spróbuję ponownie połączyć się z moim kontem pocztowym Proton, najpierw zostanę poproszony o podanie hasła wraz z nazwą użytkownika. Jest to pierwszy czynnik uwierzytelniania.

![SECURITY KEY 2FA](assets/notext/09.webp)

Następnie zostałem poproszony o wprowadzenie klucza bezpieczeństwa dla drugiego czynnika uwierzytelniania.

![SECURITY KEY 2FA](assets/notext/10.webp)

Następnie muszę dotknąć przycisku na kluczu fizycznym, aby potwierdzić uwierzytelnienie i jestem ponownie połączony z moim kontem pocztowym Proton.

![SECURITY KEY 2FA](assets/notext/11.webp)

Powtórz tę operację dla wszystkich kont online, które chcesz zabezpieczyć w ten sposób, zwłaszcza dla kont o znaczeniu krytycznym, takich jak konta e-mail, menedżery haseł, usługi przechowywania w chmurze i online lub konta finansowe.