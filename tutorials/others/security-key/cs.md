---
name: YUBIKEY 2FA
description: Jak používat fyzický bezpečnostní klíč?
---
![cover](assets/cover.webp)

V dnešní době se dvoufaktorové ověřování (2FA) stalo nezbytným pro zvýšení bezpečnosti online účtů proti neautorizovanému přístupu. S nárůstem kybernetických útoků se spoléhání pouze na heslo pro zabezpečení vašich účtů někdy jeví jako nedostatečné.

2FA představuje další vrstvu zabezpečení tím, že vyžaduje druhou formu ověření kromě tradičního hesla. Toto ověření může mít různé formy, jako je kód poslaný prostřednictvím SMS, dynamicky generovaný kód pomocí dedikované aplikace, nebo použití fyzického bezpečnostního klíče. Použití 2FA výrazně snižuje riziko kompromitace vašich účtů, i když je vaše heslo ukradeno.

V jiném tutoriálu jsem vysvětlil, jak nastavit a používat aplikaci TOTP 2FA:

https://planb.network/tutorials/others/authy

Zde se podíváme, jak používat fyzický bezpečnostní klíč jako druhý faktor ověření pro všechny vaše účty.

## Co je fyzický bezpečnostní klíč?

Fyzický bezpečnostní klíč je zařízení používané k zvýšení bezpečnosti vašich online účtů prostřednictvím dvoufaktorového ověřování (2FA). Tyto zařízení často připomínají malé USB klíče, které musí být vloženy do portu počítače, aby ověřily, že se skutečně jedná o legitimního uživatele, který se snaží připojit.
![SECURITY KEY 2FA](assets/notext/01.webp)
Když se přihlásíte k účtu chráněnému 2FA a použijete fyzický bezpečnostní klíč, musíte nejen zadat své obvyklé heslo, ale také vložit fyzický bezpečnostní klíč do počítače a stisknout tlačítko k ověření autentizace. Tato metoda přidává další vrstvu zabezpečení, protože i když se někomu podaří získat vaše heslo, nemůže přistoupit k vašemu účtu bez fyzického vlastnictví klíče.

Fyzický bezpečnostní klíč je zvláště účinný, protože kombinuje dva různé typy ověřovacích faktorů: důkaz znalosti (heslo) a důkaz vlastnictví (fyzický klíč).

Tato metoda 2FA však má také nevýhody. Zaprvé, musíte mít bezpečnostní klíč vždy k dispozici, pokud si přejete přistupovat k vašim účtům. Možná budete muset přidat klíč na svůj klíčenku. Za druhé, na rozdíl od jiných metod 2FA, použití fyzického bezpečnostního klíče zahrnuje počáteční náklady, protože musíte malé zařízení zakoupit. Cena bezpečnostních klíčů se obvykle pohybuje mezi 30 € a 100 € v závislosti na vybraných funkcích.

## Který fyzický bezpečnostní klíč si vybrat?

Při výběru bezpečnostního klíče je třeba vzít v úvahu několik kritérií.
Především je třeba zkontrolovat protokoly podporované zařízením. Jako minimum doporučuji vybrat klíč, který podporuje OTP, FIDO2 a U2F. Tyto detaily jsou obvykle výrobci zdůrazněny v popisech produktů. Pro ověření kompatibility každého klíče můžete také navštívit [dongleauth.com](https://www.dongleauth.com/dongles/).
Dále se ujistěte, že klíč je kompatibilní s vaším operačním systémem, i když známé značky jako Yubikey obvykle podporují všechny široce používané systémy.

Měli byste také vybrat klíč na základě typu portů dostupných na vašem počítači nebo smartphonu. Například, pokud váš počítač má pouze porty USB-C, vyberte klíč s konektorem USB-C. Některé klíče také nabízejí možnosti připojení přes Bluetooth nebo NFC.
![SECURITY KEY 2FA](assets/notext/02.webp)
Můžete také porovnávat zařízení na základě jejich dalších funkcí, jako je odolnost vůči vodě a prachu, stejně jako tvar a velikost klíče.
Pokud jde o značky bezpečnostních klíčů, Yubico je nejznámější díky svým zařízením [YubiKey](https://www.yubico.com/), která osobně používám a doporučuji. Google také nabízí zařízení [Titan Security Key](https://store.google.com/fr/product/titan_security_key). Pro open-source alternativy jsou zajímavé možnosti [SoloKeys](https://solokeys.com/) (bez OTP) a [NitroKey](https://www.nitrokey.com/products/nitrokeys), ale nikdy jsem neměl příležitost je vyzkoušet.
## Jak používat fyzický bezpečnostní klíč?

Jakmile obdržíte svůj bezpečnostní klíč, není vyžadováno žádné specifické nastavení. Klíč je obvykle připraven k použití ihned po obdržení. Můžete ho okamžitě použít k zabezpečení vašich online účtů, které podporují tento typ autentizace. Například vám ukážu, jak zabezpečit můj účet Proton mail s tímto fyzickým bezpečnostním klíčem.
![BEZPEČNOSTNÍ KLÍČ 2FA](assets/notext/03.webp)
Možnost povolení 2FA najdete ve vašem nastavení účtu, často pod sekci "*Heslo*" nebo "*Bezpečnost*". Klikněte na zaškrtávací políčko nebo tlačítko, které vám umožní aktivovat 2FA s fyzickým klíčem.
![BEZPEČNOSTNÍ KLÍČ 2FA](assets/notext/04.webp)
Připojte svůj klíč k počítači.
![BEZPEČNOSTNÍ KLÍČ 2FA](assets/notext/05.webp)
Dotkněte se tlačítka na vašem bezpečnostním klíči pro ověření.
![BEZPEČNOSTNÍ KLÍČ 2FA](assets/notext/06.webp)
Zadejte název, abyste si pamatovali, který klíč jste použili.
![BEZPEČNOSTNÍ KLÍČ 2FA](assets/notext/07.webp)
A to je vše, váš bezpečnostní klíč byl úspěšně přidán pro autentizaci 2FA vašeho účtu.
![BEZPEČNOSTNÍ KLÍČ 2FA](assets/notext/08.webp)
V mém příkladu, pokud se pokusím znovu připojit k mému účtu Proton mail, budu nejprve požádán, abych zadal své heslo spolu s mým uživatelským jménem. To je první faktor autentizace.
![BEZPEČNOSTNÍ KLÍČ 2FA](assets/notext/09.webp)
Poté mi bude řečeno, abych připojil svůj bezpečnostní klíč jako druhý faktor autentizace.
![BEZPEČNOSTNÍ KLÍČ 2FA](assets/notext/10.webp)
Dále musím dotknout tlačítka na fyzickém klíči pro ověření autentizace, a jsem opět připojen k mému účtu Proton mail.
![BEZPEČNOSTNÍ KLÍČ 2FA](assets/notext/11.webp)
Tento postup opakujte pro všechny online účty, které si přejete tímto způsobem zabezpečit, zejména pro kritické účty, jako jsou vaše e-mailové účty, správci hesel, vaše cloudové a online úložné služby, nebo dokonce vaše finanční účty.