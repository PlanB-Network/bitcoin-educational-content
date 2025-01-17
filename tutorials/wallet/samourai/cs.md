---
name: Samourai

description: Získejte zpět své soukromí s Samourai
---

![Samourai Wallet](assets/cover.webp)

---

***VAROVÁNÍ:** Po zatčení zakladatelů peněženky Samourai a zabavení jejich serverů 24. dubna aplikace Samourai stále funguje, ale **je nutné použít vlastní Dojo** pro přístup k informacím o blockchainu a odesílání transakcí.*

_Pozorně sledujeme vývoj této kauzy i vývoj souvisejících nástrojů. Ujistěte se, že tento návod aktualizujeme, jakmile budou k dispozici nové informace._

_Tento návod je poskytován pouze pro vzdělávací a informační účely. Nepodporujeme ani nevyzýváme k používání těchto nástrojů pro kriminální účely. Je zodpovědností každého uživatele dodržovat zákony ve své jurisdikci._

---

**Samourai Wallet** je peněženka zaměřená na soukromí. Přestože má uživatelsky přívětivé rozhraní, nabízí velkou míru flexibility ve svém používání a bezpečnosti.

Jelikož je **100% non-custodial**, budete potřebovat **zálohovat** svých 12 slov a určitě zahrnout **heslovou frázi**, kterou byste neměli ztratit.

Po vstupu do peněženky se odesílání a přijímání provádí tradičním způsobem, ale s množstvím nástrojů pro soukromí, jako jsou **Ricochet**, **Stonewall**, **Whirlpool**, **JoinMarket**, **PayNyms** a další.

Pro vysvětlení každého z těchto nástrojů se můžete odkázat na sekci **"Nástroje pro soukromí"** v návodu nebo navštívit [**oficiální dokumentační stránku Samourai Wallet**](https://docs.samourai.io/)

## Samourai Wallet ve videu

![Video návod od Rogzy](https://youtu.be/ajs1a8m76TI)

## Průvodce

### rychlá instalace pro začátečníky

> Převzato z https://docs.samourai.io/wallet/start

Naše nová uvítací obrazovka nabízí přehled funkcí naší peněženky. Po jejich přečtení klepněte na 'Začít'.

![obrázek](assets/1.webp)

Povolení

Udělte nezbytná povolení, aby peněženka mohla automaticky vytvořit šifrovanou zálohu vaší peněženky.

![obrázek](assets/2.webp)

Tor

Většina uživatelů by poté měla povolit Tor pro soukromí na úrovni sítě. Poté klepněte na Vytvořit novou peněženku.

![obrázek](assets/3.webp)

Vytvoření heslové fráze

Vytvořte si bezpečnou, ale snadno zapamatovatelnou heslovou frázi. Tato heslová fráze poskytne vaší peněžence další zabezpečení a je kompatibilní s jakoukoli peněženkou, která implementovala široce podporovanou specifikaci BIP39.

Vaše heslová fráze je nezbytnou součástí při obnově pomocí mnemonické fráze (někdy nazývané Obnovovací slova) nebo při párování s desktopovými aplikacemi Whirlpool. Je zásadní, abyste svou heslovou frázi neztratili ani na ni nezapomněli.

> Nemáme znalost vaší heslové fráze, pokud na ni zapomenete, nemůžeme vám pomoci ji resetovat.
> Nezapomeňte na svou heslovou frázi!

![obrázek](assets/4.webp)

Vytvoření PIN kódu

Nyní budete požádáni, abyste vytvořili a potvrdili PIN kód o délce 5 až 8 číslic. PIN kód slouží k snadnému odemčení vaší peněženky bez nutnosti zadávat heslovou frázi.

Pokud zapomenete svůj PIN kód, vždy můžete přistupovat k peněžence pomocí heslové fráze.

![obrázek](assets/5.webp)

Vytvoření papírové zálohy

Nyní jste vytvořili zcela novou Bitcoinovou peněženku. Budou vám zobrazena 12 náhodných slov. Je zásadní, abyste si tyto 12 tajných slov zapsali a bezpečně uložili.

Tato slova, použitá společně s vaší heslovou frází, mohou regenerovat celou vaši peněženku, zůstatek a historii v jakémkoli kompatibilním softwaru pro peněženky.

> Pracovní list pro papírovou zálohu Poskytujeme šablonu pro vytvoření vaší vlastní offline papírové zálohy
Vaše tajná slova musí zůstat tajemstvím. Každý, kdo zná vaše tajná slova a heslovou frázi, bude moci ukrást vaše bitcoiny. Nikdy neskladujte svá slova uložená na počítači nebo v cloudu.
Získejte svého PayNym robota

PayNym je typ stealth adresy, která se od běžných bitcoinových adres liší tím, že ji je bezpečné sdílet veřejně bez odhalení jakýchkoli informací o vaší peněžence včetně zůstatku nebo historie transakcí.

Po úspěšném vytvoření vaší peněženky budete vyzváni k získání PayNym robota. To je vizuální reprezentace SHA-256 hash vaší PayNym adresy peněženky.

Po získání vám bude přiřazeno unikátní jméno robota, které je nahráno do veřejného adresáře robotů PayNym, který lze najít na https://paynym.is

![obrázek](assets/6.webp)

## použití

V této fázi můžete jednoduše přijímat a posílat bitcoiny. Peněženka Samourai je poměrně pokročilá v technických možnostech, podrobněji se tomu budeme věnovat v nadcházejícím průvodci.