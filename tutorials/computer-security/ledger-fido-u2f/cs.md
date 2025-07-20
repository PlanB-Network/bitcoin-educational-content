---
name: Ledger U2F & FIDO2
description: Zlepšete své online zabezpečení pomocí Ledger
---
![cover](assets/cover.webp)



Zařízení Ledger jsou hardwarové peněženky původně určené k zabezpečení Bitcoin Wallet, ale mají také pokročilé možnosti silného ověřování na webu. Díky kompatibilitě s protokoly **U2F** a **FIDO2** umožňují zabezpečit přístup k online účtům nastavením druhého ověřovacího faktoru.



Protokol U2F (Universal 2nd Factor) představily společnosti Google a Yubico v roce 2014 a poté jej standardizovala aliance FIDO. Umožňuje při přihlašování přidat druhý fyzický ověřovací faktor (2FA). Po jeho aktivaci musí uživatelé kromě klasického hesla schválit každý pokus o připojení ke svému účtu stisknutím tlačítka na Ledger. V tomto kontextu funguje Ledger podobně jako Yubikey. U2F je ve skutečnosti dílčí součástí standardu FIDO2, který zahrnuje a zároveň přináší významná vylepšení, včetně nativní podpory moderních prohlížečů a větší flexibility při správě ověřovacích klíčů.



Tyto metody jsou založeny na asymetrické kryptografii: nepřenášejí se žádná tajná data, takže phishingové nebo odposlechové útoky jsou neúčinné. U2F a FIDO2 jsou nyní podporovány mnoha online službami.



V tomto návodu vám ukážeme, jak aktivovat U2F a FIDO2 pro dvoufaktorové ověřování pomocí zařízení Ledger.



**Poznámka:** U2F a FIDO2 jsou podporovány na všech zařízeních Ledger vybavených nejnovějším firmwarem: od verze 2.1.0 pro Nano X a Nano S classic a od verze 1.1.0 pro Nano S Plus. Modely Stax a Flex jsou nativně kompatibilní.



## Instalace aplikace Ledger Security Key



Pokud používáte zařízení Ledger, pravděpodobně víte, že samotný firmware neobsahuje všechny funkce potřebné pro správu kryptopeněženek. Chcete-li například používat zařízení Bitcoin Wallet, musíte si nainstalovat aplikaci "*Bitcoin*". Podobně pro správu klíčů MFA je třeba nainstalovat aplikaci "*Security Key*".



Než začnete, ujistěte se, že jste nastavili Bitcoin Wallet na Ledger. Je důležité, abyste správně uložili svůj Mnemonic, protože klíče používané pro 2FA jsou odvozeny od tohoto Mnemonic. Pokud dojde ke ztrátě nebo poškození vašeho zařízení Ledger, můžete obnovit přístup ke svým klíčům zadáním fráze Mnemonic na jiném zařízení Ledger (prozatím nejsou identifikátory FIDO2 v režimu "*bez hesla*" na zařízeních Ledger podporovány, takže neexistují žádné rezidentní identifikátory).



Připojte zařízení Ledger k počítači a odemkněte jej.



![Image](assets/fr/01.webp)



Chcete-li aplikaci nainstalovat, otevřete software [Ledger Live] (https://www.Ledger.com/Ledger-live) a přejděte na kartu "*My Ledger*". Najděte aplikaci "*Security Key*" a nainstalujte ji do svého zařízení.



![Image](assets/fr/02.webp)



Aplikace "*Bezpečnostní klíč*" by se nyní měla objevit vedle ostatních aplikací nainstalovaných v zařízení Ledger.



![Image](assets/fr/03.webp)



Klikněte na aplikaci a nechte ji otevřenou pro další kroky v tutoriálu.



![Image](assets/fr/04.webp)



## Použití U2F/FIDO2 pro 2FA s Ledger



Získejte přístup k účtu, který chcete zabezpečit pomocí dvoufaktorového ověřování. Já například použiji účet Bitwarden. Možnost 2FA obvykle najdete v nastavení služby na kartách "*authentication*", "*security*", "*login*" nebo "*password*".



![Image](assets/fr/05.webp)



V části věnované dvoufaktorovému ověřování vyberte možnost "*Passkey*" (termín se může lišit v závislosti na používaném webu).



![Image](assets/fr/06.webp)



Často budete požádáni o potvrzení aktuálního hesla.



![Image](assets/fr/07.webp)



Bezpečnostní klíč pojmenujte pro snadnější rozpoznání a klikněte na "*Přečíst klíč*".



![Image](assets/fr/08.webp)



Na displeji Ledger se zobrazí údaje o vašem účtu. Potvrďte stisknutím tlačítka "*Register*" (nebo oběma tlačítky současně, v závislosti na modelu, který používáte).



![Image](assets/fr/09.webp)



Přístupový klíč byl úspěšně zaregistrován.



![Image](assets/fr/10.webp)



Zaregistrujte tento bezpečnostní klíč.



![Image](assets/fr/11.webp)



Od nynějška budete při přihlašování k účtu kromě obvyklého hesla požádáni o připojení účtu Ledger.



![Image](assets/fr/12.webp)



Poté můžete na displeji Ledger stisknout tlačítko "*Log in*" a potvrdit tak ověření (nebo obě tlačítka současně, v závislosti na modelu, který používáte).



![Image](assets/fr/13.webp)



Výhodou použití Hardware Wallet Ledger pro dvoufaktorové ověřování je, že díky frázi Mnemonic můžete snadno obnovit své klíče. Kromě této základní zálohy můžete použít také nouzový kód poskytovaný každou službou, u které jste aktivovali 2FA. Tento nouzový kód vám umožní připojit se k účtu, pokud ztratíte bezpečnostní klíč. V případě potřeby tedy nahrazuje 2FA pro připojení.



Například v systému Bitwarden se k tomuto kódu dostanete kliknutím na "*Zobrazit kód pro obnovení*".



![Image](assets/fr/14.webp)



Doporučuji, abyste tento kód uchovávali na jiném místě než hlavní heslo, abyste zabránili jejich společné krádeži. Pokud máte heslo uloženo například ve správci hesel, uchovávejte nouzový kód 2FA odděleně na papíře.



Tento přístup nabízí dvě úrovně zálohování v případě ztráty vašeho účtu Ledger pro ověřování 2FA: první zálohu pomocí fráze Mnemonic pro všechny vaše účty a druhou zálohu pro konkrétní účet pomocí nouzových kódů. Je však důležité **nezaměňovat úlohu fráze Mnemonic s úlohou nouzového kódu** :




- Fráze Mnemonic o 12 nebo 24 slovech vám umožní přístup nejen ke klíčům používaným pro 2FA na všech vašich účtech, ale také k bitcoinům zabezpečeným pomocí Ledger ;
- Nouzový kód umožňuje dočasně obejít požadavek 2FA pouze na daném účtu (v tomto příkladu pouze na Bitwarden).



Blahopřejeme, nyní již umíte používat nástroj Ledger pro makrofinanční pomoc! Pokud pro vás byl tento návod užitečný, budu vám velmi vděčný, když níže zanecháte palec Green. Neváhejte prosím sdílet tento návod na svých sociálních sítích. Děkujeme vám!



Doporučuji také tento další tutoriál, ve kterém se podíváme na jiné řešení pro ověřování U2F a FIDO2:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e