---
name: NOSTR

description: Objevte a začněte používat NOSTR
---

Na konci tohoto průvodce budete rozumět, co je Nostr, vytvoříte si účet a budete ho umět používat.

![Nový vyzývatel přichází](assets/1.webp)

## Co je Nostr?

Nostr je protokol, který má sílu nahradit Twitter, Telegram a další sociální média. Jedná se o jednoduchý otevřený protokol schopný vytvořit globálně odolnou sociální síť jednou provždy.

## Jak to funguje?

Nostr je založen na třech komponentách: párech klíčů, klientech a reléch.

Každý uživatel má jednu nebo více identit a každá identita je určena kryptografickým párem klíčů.

Pro přístup k síti potřebujete použít klientský software a připojit se k reléům pro příjem a přenos obsahu.

![Systém klíčů](assets/2.webp)

## 1. Kryptografické klíče

Na rozdíl od Facebooku nebo Twitteru, kde uživatelé musí poskytnout e-mailovou adresu a spoustu informací soukromé společnosti, Nostr funguje bez centrální autority. Uživatelé generují kryptografický pár klíčů, tajný klíč (také známý jako soukromý klíč) a veřejný klíč.

Tajný klíč, nsec, známý pouze uživateli, se používá pro autentizaci a publikování obsahu.

Veřejný klíč, npub, je jedinečný identifikátor, ke kterému je připojen veškerý obsah publikovaný uživatelem. Váš veřejný klíč je jako uživatelské jméno, které umožňuje ostatním uživatelům vás najít a přihlásit se k odběru vašeho Nostr kanálu.

## 2. Klienti

Klienti jsou software, který umožňuje interakci s Nostr. Hlavní klienti jsou:

> iOS: damus
> Android: amethyst
> Web: iris.to; snort.social; astral.ninja

Klienti umožňují uživatelům generovat nový pár klíčů (ekvivalent k vytvoření účtu) nebo se autentizovat s existujícím párem klíčů.

## 3. Relé

Relé jsou zjednodušené servery, které můžete kdykoli opustit, pokud se vám nelíbí obsah, který vám poskytují. Také si můžete provozovat vlastní relé, pokud chcete.

> 💡 Profi tip: Placená relé jsou obecně účinnější při filtrování spamu a nechtěného obsahu.

# Průvodce

Nyní víte dost o Nostru, abyste mohli začít a vytvořit svou první identitu na tomto protokolu.

Pro účely tohoto průvodce použijeme iris.to (https://iris.to/) jako tento webový klient funguje na jakékoli platformě.

## Krok 1: Generování klíčů

Iris pro vás vytvoří sadu klíčů, aniž byste museli dělat cokoli víc, než zadat jméno (skutečné nebo fiktivní) pro váš profil. Poté klikněte na GO a hotovo!

![Hlavní menu](assets/3.webp)

> ⚠️ Pozor! Budete muset sledovat své klíče, pokud chcete být schopni znovu přistupovat k vašemu profilu, jakmile vaše relace skončí. Ukážu vám, jak to udělat na samém konci tohoto průvodce.

## Krok 2: Publikování obsahu

Publikování obsahu je stejně jednoduché a intuitivní, jako psaní několika slov do pole pro publikaci.

![Publikace](assets/4.webp)

A je to! Publikovali jste svou první poznámku na Nostr.

![Příspěvek](assets/5.webp)

## Krok 3: Najít přítele

Najděte mě na Nostr a nikdy nebudete sami. Odebírat zpět budu každého, kdo se přihlásí k odběru mého kanálu. K tomu stačí zadat můj veřejný klíč

npub1hartx53w6t3q5wv9xdqdwrk7h6r5866t8u775q0304zedpn5zgssasp7d3 do vyhledávacího pole.
![Můj profil](assets/6.webp)
Klikněte na "sledovat" a nejpozději za pár dní se také přihlásím k odběru vašeho kanálu. Budeme přátelé. Budu také rád, když mi napíšete zprávu, pokud budete chtít.

A nakonec se ujistěte, že jste se také přihlásili k odběru kanálu Agora256, abyste dostávali oznámení pokaždé, když něco nového publikujeme: npub1ag0rawstycy7nanuc6sz4v287rneen2yapcq3fd06972f8ncrhzqx

## Krok 4: Přizpůsobení vašeho profilu

Stále máte co dělat, abyste si přizpůsobili svůj profil. K tomu klikněte na avatar, který pro vás iris automaticky vygeneroval v pravém horním rohu obrazovky, a poté klikněte na "upravit profil".

![Profil](assets/7.webp)

Nyní už jen musíte říct iris, kde najít váš obrázek a banner profilu na internetu. Doporučuji hostovat vlastní obsah: chraňte, co je vaše.

![Další možnost](assets/8.webp)

Pokud chcete, můžete také nahrát obrázky, které pro vás iris uloží na nostr.build, bezplatnou službu pro hostování vizuálního obsahu pro Nostr.

Jak vidíte, můžete také nakonfigurovat svého klienta tak, aby mohl přijímat a odesílat sats. Tímto způsobem můžete odměnit autory obsahu, který se vám líbil, nebo ještě lépe, akumulovat sats za skvělý obsah, který budete publikovat.

## Krok 5: Zálohování páru klíčů

Tento krok je zásadní, pokud chcete udržet přístup k vašemu profilu, jakmile se odhlásíte z klienta nebo když vyprší vaše relace.
Nejprve klikněte na ikonu "nastavení" reprezentovanou ozubeným kolem
![Nastavení](assets/9.webp)

Poté zkopírujte a vložte jeden po druhém váš npub, npub hex, nsec a nsec hex do textového souboru, který si bezpečně uschováte. Doporučuji tento soubor zašifrovat, pokud víte, jak na to.

![Klíč](assets/10.webp)

> ⚠️ Všimněte si varování od iris. Zatímco svůj veřejný klíč můžete sdílet bez obav, s vaším soukromým klíčem je to jiný příběh. Kdokoli ho má, bude moci přistupovat k vašemu účtu.

## Závěr

A je to, malý pštrosi, udělali jste své první kroky na Nostr. Nyní se budete muset naučit běhat rychlostí blesku. Brzy zveřejníme průvodce, které vám ukážou, jak spravovat vaše klíče a jak integrovat lightning do vašeho zážitku s Nostr pomocí getalby.