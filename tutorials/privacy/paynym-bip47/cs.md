---
name: BIP47 - PayNym
description: Použití opakovaně použitelného platebního kódu na Ashigaru
---
![cover](assets/cover.webp)



Nejhorší chybou v oblasti ochrany soukromí, které se můžete v systému Bitcoin dopustit, je opakované používání adres. Pokaždé, když na stejnou adresu přijde několik plateb, jsou tyto transakce spojeny dohromady a poskytují světu mapu vašich transakcí. Proto důrazně doporučujeme, abyste pro každou účtenku generate vždy používali jedinečnou adresu. Pro některé aplikace Bitcoin to však není jednoduchá záležitost.



BIP47, který v roce 2015 navrhl Justus Ranvier, poskytuje elegantní odpověď na tento problém. Zavádí koncept **použitelného platebního kódu**: jedinečného identifikátoru, který umožňuje přijímat prakticky neomezený počet plateb v bitcoinovém řetězci, aniž by bylo nutné opakovaně používat adresu. Díky kryptografickému mechanismu založenému na výměně ECDH (*Diffie-Hellman on elliptic curves*) je výsledkem každé platby na stejný kód prázdná adresa, specifická pro vztah mezi odesílatelem a příjemcem.



![Image](assets/fr/01.webp)



Tento princip BIP47 uplatňuje zejména systém **PayNym**, který původně vyvinula společnost Samourai Wallet a nyní jej převzala společnost Ashigaru. V tomto návodu se podíváme na to, jak aktivovat PayNym, vyměnit si platební kódy s korespondentem a provádět transakce bez opakovaného použití adresy.



Nebudu se zde zabývat podrobným fungováním BIP47. Pokud byste se chtěli tomuto tématu věnovat hlouběji, přečtěte si kapitolu 6.6 mého školení BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Předpoklady



K tomu, abyste mohli postupovat podle tohoto návodu, potřebujete pouze wallet v aplikaci Ashigaru. Pokud nevíte, jak aplikaci stáhnout, ověřit, nainstalovat nebo vytvořit wallet, doporučuji nejprve nahlédnout do tohoto návodu:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Žádost o PayNym



Prvním krokem je přihlášení se k účtu PayNym. Tuto operaci je třeba provést pouze jednou za wallet. Spojí váš platební kód BIP47 odvozený z vašeho seed (`PM...`) s jedinečným identifikátorem specifickým pro implementaci PayNym. Tento kratší a čitelnější identifikátor lze poté předat vašim korespondentům, aby se usnadnila výměna, aniž by bylo nutné sdílet dlouhý a úplný kód BIP47.



Klikněte na svůj obrázek PayNym v levém horním rohu rozhraní a poté na svůj platební kód `PM...`.



![Image](assets/fr/02.webp)



Poté klikněte na tři malé tečky v pravém horním rohu a vyberte možnost `Claim PayNym`.



![Image](assets/fr/03.webp)



Potvrďte kliknutím na tlačítko `CLAIM YOUR PAYNYM`.



![Image](assets/fr/04.webp)



Obnovte stránku: vaše ID PayNym se nyní zobrazí pod vaším obrázkem, hned nad vaším platebním kódem BIP47.



![Image](assets/fr/05.webp)



Váš PayNym je nyní aktivní a připravený k použití pro první transakce BIP47.



## Spojení s kontaktem



Existují dva typy připojení mezi PayNym: **sledovat** a **připojit**. Operace `follow` je zcela zdarma. Navazuje spojení mezi dvěma PayNym prostřednictvím Sorobanu, šifrovaného komunikačního protokolu založeného na Toru, který vyvinul tým Samourai a převzal Ashigaru. Toto spojení umožňuje dvěma uživatelům, kteří se navzájem sledují, vyměňovat si soukromě informace, zejména koordinovat společné transakce, jako je Stowaway nebo StonewallX2, kterým se budeme věnovat v jiném tutoriálu. Tento krok je specifický pro PayNym a není součástí protokolu BIP47.



![Image](assets/fr/06.webp)



Operace připojení (`connect`) naopak vyžaduje transakci on-chain. Spočívá v provedení oznamovací transakce podle definice v BIP47. Tato transakce Bitcoin obsahuje metadata ve výstupu `OP_RETURN`, který vytváří šifrovaný komunikační kanál mezi plátcem a příjemcem. Z tohoto kanálu bude plátce schopen pro každou platbu zadat jedinečné adresy příjemce generate a příjemce bude o těchto platbách informován a bude moci použít soukromé klíče generate spojené s těmito adresami, aby mohl tyto prostředky později utratit.



Tato notifikační transakce má náklady: poplatek mining a 546 sats odeslaný na notifikační adresu příjemce k signalizaci spojení. Po navázání spojení lze prostřednictvím BIP47 provádět téměř nekonečné množství plateb.



Stručně řečeno:




- follow": zdarma, navazuje šifrovanou komunikaci přes Soroban, užitečné pro nástroje spolupráce Ashigaru;
- `Connect`: zpoplatněno, provede transakci oznámení BIP47 pro aktivaci kanálu mezi plátcem a příjemcem.



Chcete-li s PayNym komunikovat, musíte jej nejprve *sledovat*. To je první krok před navázáním spojení BIP47. Řekněme, že chcete posílat opakované platby na účet PayNym `+instinctiveoffer10`.



Přejděte na svou stránku PayNym na Ashigaru a klikněte na tlačítko `+` v pravém dolním rohu rozhraní.



![Image](assets/fr/07.webp)



Poté můžete vložit celý platební kód příjemce nebo naskenovat jeho QR kód.



![Image](assets/fr/08.webp)



Pokud máte pouze jeho ID PayNym, přejděte na stránku [Paynym.rs](https://paynym.rs/), kde najdete QR kód spojený s jeho platebním kódem.



![Image](assets/fr/09.webp)



Po naskenování kódu QR klikněte na tlačítko `Sledovat` a sledujte PayNym.



![Image](assets/fr/10.webp)



Akce `FOLLOW` je dostatečná pro společné transakce (*cahoots*). Chcete-li však odeslat platby BIP47, musíte navázat spojení: kliknutím na `CONNECT` provedete oznamovací transakci.



![Image](assets/fr/11.webp)



Transakce oznámení je poté vysílána do sítě. Před provedením první platby vyčkejte, dokud se neobjeví alespoň jedno potvrzení.



![Image](assets/fr/12.webp)



## Proveďte platbu BIP47



Nyní jste spojeni s příjemcem a můžete odeslat platbu na jedinečnou adresu, která je automaticky vygenerována pomocí protokolu BIP47, aniž byste si s příjemcem předtím něco vyměnili.



Na hlavní stránce služby PayNym klikněte na kontakt, kterému chcete zaslat platbu.



![Image](assets/fr/13.webp)



V pravé horní části rozhraní klikněte na ikonu šipky.



![Image](assets/fr/14.webp)



Zadejte částku, která má být odeslána. Adresu příjemce zadávat nemusíte: bude automaticky odvozena pomocí protokolu BIP47.



![Image](assets/fr/15.webp)



Pečlivě zkontrolujte podrobnosti transakce včetně poplatků a poté přetažením zelené šipky v dolní části obrazovky transakci podepište a odvysílejte.



![Image](assets/fr/16.webp)



Transakce byla odeslána.



![Image](assets/fr/17.webp)



V tomto příkladu byla platba provedena do jiné z mých peněženek PayNym. Vidím tedy, že dorazila na mou další Ashigaru wallet, aniž by byla ručně vyměněna jakákoli adresa: byl použit pouze identifikátor PayNym.



![Image](assets/fr/18.webp)



Díky implementaci PayNym v aplikaci Ashigaru nyní víte, jak používat opakovaně použitelné platební kódy BIP47. Tento platební kód nyní můžete sdílet s kýmkoli, kdo vám chce posílat platby (zejména opakované platby). ID PayNym můžete také zveřejnit na svých webových stránkách nebo sociálních sítích a přijímat tak dary.



Chcete-li prohloubit své znalosti o tomto protokolu, podrobně pochopit jeho fungování a jeho důsledky pro důvěrnost, důrazně doporučuji absolvovat můj kurz BTC 204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c