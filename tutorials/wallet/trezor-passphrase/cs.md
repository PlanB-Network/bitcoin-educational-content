---
name: BIP-39 Passphrase Trezor
description: Jak mohu do svého portfolia produktů Trezor přidat produkt passphrase?
---
![cover](assets/cover.webp)



passphrase BIP39 je volitelné heslo, které v kombinaci s frází Mnemonic poskytuje dodatečné zabezpečení Layer pro deterministická a hierarchická portfolia Bitcoin. V tomto návodu společně zjistíme, jak nastavit heslo passphrase na vašem zabezpečeném zařízení Bitcoin Wallet na zařízení Trezor (Safe 3, Safe 5 a Model One).



![Image](assets/fr/01.webp)



Pokud nejste obeznámeni s konceptem passphrase, jeho fungováním a důsledky pro váš Bitcoin Wallet, před zahájením tohoto návodu vám důrazně doporučuji prostudovat tento další teoretický článek, kde vše vysvětluji (je to velmi důležité, protože používání passphrase bez plného pochopení jeho fungování může ohrozit vaše bitcoiny) :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase na Trezoru je řešen klasickým způsobem, pokud jste se při konfiguraci rozhodli pro standard BIP39 (což doporučuji, pokud nepotřebujete *Multi-share Backup*). Zvláštností Trezoru je, že passphrase můžete zadávat buď přímo na Hardware Wallet, nebo prostřednictvím klávesnice počítače pomocí softwaru Trezor Suite. Tato druhá možnost je podstatně méně bezpečná, protože počítač má nesmírně větší plochu pro útoky než Hardware Wallet. Zadávání složitého kódu passphrase však může být na běžné klávesnici rychlejší než na počítači Hardware Wallet, což by mohlo podpořit používání silných přístupových frází. Vždy je tedy lepší používat heslo passphrase, i když se musí zadávat, než ho nepoužívat vůbec. Je však důležité si i nadále uvědomovat zvýšené riziko číselných útoků, které z toho vyplývá.



Tyto možnosti nejsou k dispozici ve všech programech pro správu portfolia kompatibilních se softwarem Trezor. Například u modelu One lze passphrase zadat pomocí klávesnice na Sparrow Wallet. U modelů Model T, Safe 3 a Safe 5 je nutné buď použít Trezor Suite, nebo zadat passphrase přímo na Hardware Wallet, protože možnost zadávání přes Sparrow byla společností HWI před několika lety zakázána.



![Image](assets/fr/02.webp)



V sadě Trezor Suite máte k dispozici dva různé způsoby správy poptávky passphrase. Na kartě "*Zařízení*" můžete aktivovat možnost "*passphrase*". Pokud je tato funkce aktivována, bude vás sada Trezor Suite a všechny ostatní programy pro správu portfolia při každém spuštění systematicky žádat o zadání zařízení passphrase. Pokud dáváte přednost diskrétnějšímu přístupu k používání passphrase, můžete ponechat nastavení na hodnotě "*Standardní*". V takovém případě budete muset ručně vstoupit do nabídky Hardware Wallet v levém horním rohu a při každém spuštění kliknout na tlačítko "*+ passphrase*".



Před zahájením tohoto návodu se ujistěte, že jste již inicializovali zařízení Trezor a vygenerovali frázi Mnemonic. Pokud jste tak neučinili a váš Trezor je nový, postupujte podle návodu pro konkrétní model, který je k dispozici na stránce Plan ₿ Network. Po dokončení tohoto kroku se můžete vrátit k tomuto návodu.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Přidání zařízení passphrase do trezoru 3 nebo 5



Jakmile vytvoříte svůj účet Wallet, uložíte účet Mnemonic a nastavíte kód PIN, přejdete do domovské nabídky sady Trezor Suite. V levém horním rohu by se mělo objevit okno s výzvou k aktivaci passphrase BIP39.



![Image](assets/fr/03.webp)



Pokud se toto okno nezobrazí, je třeba ručně aktivovat možnost "*passphrase*" na kartě nastavení "*Zařízení*".



![Image](assets/fr/04.webp)



V tomto okně budete vyzváni k zadání čísla passphrase. Zvolte silnou jednotku passphrase a ihned vytvořte fyzickou zálohu na médiu, jako je papír nebo kov. V tomto příkladu jsem zvolil passphrase: `fH3&kL@9mP#2sD5qR!82`. Jedná se o příklad; doporučuji však zvolit o něco delší kód passphrase. Ideální by bylo 30 až 40 znaků (jako dobré heslo).



samozřejmě byste nikdy neměli sdílet svůj kód passphrase na internetu, jak to dělám v tomto návodu. Tento příklad Wallet bude použit pouze na Testnet a na konci návodu bude smazán.



Konkrétnější doporučení pro výběr passphrase najdete v tomto dalším článku:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Pokud chcete zadat číslo passphrase pomocí klávesnice počítače, zadejte jej do příslušného pole a klikněte na "*Přístup passphrase Wallet*".



![Image](assets/fr/05.webp)



Poté se na displeji Hardware Wallet zobrazí passphrase. Než kliknete na obrazovku a budete pokračovat, ujistěte se, že odpovídá vaší fyzické záloze (papírové nebo kovové).



![Image](assets/fr/06.webp)



Tím získáte přístup ke svému portfoliu chráněnému kódem passphrase.



![Image](assets/fr/07.webp)



Pokud dáváte přednost zvýšení bezpečnosti zadáním passphrase pouze do zařízení Trezor, klikněte na výzvu na "*Zadat passphrase do zařízení Trezor*".



![Image](assets/fr/08.webp)



Na zařízení Trezor se zobrazí klávesnice T9, na které můžete zadat kód passphrase. Po dokončení zadávání klikněte na zaškrtávací políčko Green, čímž se passphrase použije na váš Wallet.



![Image](assets/fr/09.webp)



Poté získáte přístup k zabezpečené jednotce passphrase Wallet.



![Image](assets/fr/10.webp)



Pro použití Sparrow Wallet je postup podobný, ale u modelů T, Safe 3 a Safe 5 se passphrase musí zadat na Hardware Wallet, nikoliv prostřednictvím klávesnice počítače.



Kdykoli bude Sparrow Wallet vyžadovat přístup k vašemu Trezoru a od posledního spuštění ještě nebyl použit passphrase, budete jej muset zadat pomocí klávesnice T9.



![Image](assets/fr/11.webp)



## Přidání zařízení passphrase k modelu One



U modelu One je použití passphrase BIP39 téměř nezbytné. Protože toto zařízení neobsahuje zabezpečený prvek, je poměrně snadné získat citlivé informace. Není proto odolné proti fyzickému napadení. Protože se však po vypnutí zařízení nezachovává, může použití silného (nebrutálního) passphrase ochránit před většinou známých fyzických útoků na tento model.



U modelu One není možné zadat passphrase přímo na Hardware Wallet. Musíte jej zadat prostřednictvím klávesnice počítače.



Jakmile si vytvoříte Wallet, uložíte Mnemonic a nastavíte PIN, přejdete do domovské nabídky sady Trezor Suite. V levém horním rohu by se mělo objevit okno s výzvou k aktivaci passphrase BIP39.



![Image](assets/fr/12.webp)



Pokud se toto okno nezobrazí, je třeba aktivovat možnost "*passphrase*" na kartě "*Zařízení*" v nastavení.



![Image](assets/fr/13.webp)



V tomto okně budete vyzváni k zadání čísla passphrase. Zvolte silný kód passphrase a ihned vytvořte fyzickou zálohu na médiu, jako je papír nebo kov. V tomto příkladu jsem zvolil passphrase: `fH3&kL@9mP#2sD5qR!82`. Jedná se pouze o příklad; doporučuji však zvolit o něco delší kód passphrase. Ideální by bylo 30 až 40 znaků (jako dobré heslo).



Konkrétnější doporučení pro výběr passphrase najdete v tomto dalším článku:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Do příslušného pole zadejte svůj přístroj passphrase a poté klikněte na tlačítko "*Přístup passphrase Wallet*".



![Image](assets/fr/14.webp)



Na displeji Hardware Wallet se zobrazí passphrase. Ujistěte se, že odpovídá vaší fyzické záloze (papírové nebo kovové), a poté pokračujte kliknutím na pravé tlačítko.



![Image](assets/fr/15.webp)



Tím se dostanete do svého portfolia chráněného pomocí passphrase.



![Image](assets/fr/16.webp)



Při následném použití Sparrow Wallet zůstává postup stejný. Pokaždé, když Sparrow vyžaduje přístup k vašemu Hardware Wallet a passphrase nebyl zadán od posledního spuštění zařízení, budete jej muset zadat.



![Image](assets/fr/17.webp)



Gratulujeme, nyní jste se seznámili s používáním passphrase BIP39 v hardwarových peněženkách Trezor. Pokud byste chtěli posunout zabezpečení Wallet o krok dál, podívejte se na tento návod na zálohovací systémy Trezor *Multi-share* (*Shamir's Secret Sharing Scheme*):



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Pokud vám tento návod přišel užitečný, budu vám vděčný, když mi níže zanecháte palec Green. Neváhejte tento článek sdílet na svých sociálních sítích. Děkuji vám!