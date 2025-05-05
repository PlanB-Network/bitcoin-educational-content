---
name: Olvid
description: Soukromé zasílání zpráv pro všechny
---
![cover](assets/cover.webp)



Olvid je francouzská aplikace pro zasílání rychlých zpráv, která byla spuštěna v roce 2019 a je navržena tak, aby nabízela vysokou úroveň zabezpečení bez omezení soukromí. Na rozdíl od aplikací WhatsApp nebo Signal nepožaduje Olvid při registraci žádné osobní údaje: žádné telefonní číslo, žádný e-mail, nic. Identifikace mezi uživateli je založena na Exchange klíčích, bez adresářového serveru nebo sdílené knihy Address.



Všechny zprávy jsou šifrovány end-to-end pomocí originálního kryptografického protokolu, který je navržen tak, aby chránil i metadata: nikdo neví, s kým a kdy mluvíte. Klientský kód je open source, ale centrální server používaný k směrování šifrovaných zpráv zůstává proprietární a je umístěn na AWS.



Olvid nabízí bezplatnou verzi a verzi s předplatným za 4,99 EUR měsíčně. Bezplatná verze nabízí plnou funkčnost s výjimkou uskutečňování audio a video hovorů (ačkoli je možné je přijímat) a neumožňuje synchronizaci účtu mezi více zařízeními. Pokud tedy plánujete používat výhradně chytrý telefon a nepotřebujete uskutečňovat hovory, je Olvid vynikajícím řešením.



Společnost Olvid je certifikována ANSSI (francouzský úřad pro kybernetickou bezpečnost). Tato aplikace je vynikající alternativou k tradičním službám pro zasílání zpráv (WhatsApp, Facebook Messenger, WeChat...) pro ty, kteří hledají soukromí při zachování jednoduchosti používání.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| **Olvid**                | **✅**              | **✅**              | **✅**                   | **✅**                          | **❌**                           | **❌**                    | **2019**              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end šifrování*



## Instalace aplikace Olvid



Olvid je k dispozici na všech platformách. Aplikaci si můžete stáhnout přímo z obchodu s aplikacemi v telefonu:




- [Google Play](https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store](https://apps.apple.com/app/olvid/id1414865219);



V systému Android je také možné [instalovat přes APK](https://www.olvid.io/download/).



V tomto návodu se zaměříme na mobilní verzi, ale upozorňujeme, že k dispozici jsou také [počítačové verze](https://www.olvid.io/download/) (MacOS, Linux a Windows). Pokud si vyberete placenou verzi, budete moci synchronizovat svůj účet na více zařízeních.



![Image](assets/fr/01.webp)



## Vytvoření účtu na Olvidu



Při prvním spuštění aplikace klikněte na tlačítko "*Jsem nový uživatel*".



![Image](assets/fr/02.webp)



Vyberte si přezdívku nebo zadejte své jméno a příjmení.



![Image](assets/fr/03.webp)



Přidejte profilovou fotografii.



![Image](assets/fr/04.webp)



Váš účet je nyní vytvořen.



![Image](assets/fr/05.webp)



Abyste zabránili ztrátě přístupu k účtu Olvid, doporučujeme nastavit automatické zálohování. Za tímto účelem otevřete nastavení kliknutím na tři tečky v pravém horním rohu okna Interface a poté vyberte možnost "*Nastavení*".



![Image](assets/fr/06.webp)



Přejděte do nabídky "*Uložit klíče a kontakty*".



![Image](assets/fr/07.webp)



Poté klikněte na "*generate a backup key*". Tento klíč zašifruje vaše zálohy. Pokud budete potřebovat obnovit svůj účet na jiném zařízení a nebudete k němu mít přístup, budete k dešifrování potřebovat jak zálohu, tak tento klíč.



![Image](assets/fr/08.webp)



Tento klíč uchovávejte na bezpečném místě. Můžete si také pořídit papírovou kopii.



![Image](assets/fr/09.webp)



Poté si můžete vybrat, zda chcete vytvořit místní zálohu nebo automatickou zálohu v cloudové službě. Tuto druhou možnost důrazně doporučujeme, abyste si zajistili přístup k účtu Olvid za všech okolností, a to i v případě ztráty telefonu.



![Image](assets/fr/10.webp)



Ujistěte se, že je zaškrtnuta možnost "*Povolit automatické zálohování*".



![Image](assets/fr/11.webp)



Můžete také prozkoumat další dostupná nastavení a přizpůsobit aplikaci svým potřebám.



![Image](assets/fr/12.webp)



## Odesílání zpráv pomocí služby Olvid



Abyste mohli odesílat zprávy, musíte nejprve přidat kontakty. Na domovské stránce klikněte na modré tlačítko "*+*".



![Image](assets/fr/13.webp)



Olvid poté zobrazí vaše ID uživatele. To pak můžete předat lidem, se kterými chcete komunikovat, aby si vás mohli přidat jako kontakt.



Chcete-li přidat osobu, naskenujte její průkaz totožnosti fotoaparátem nebo jej vložte ručně kliknutím na tři malé tečky v pravém horním rohu.



![Image](assets/fr/14.webp)



Po naskenování ID můžete nechat kontakt naskenovat zobrazený QR kód nebo mu poslat žádost o vzdálené připojení kliknutím na "*Vzdálený kontakt*".



![Image](assets/fr/15.webp)



Spojení je nyní navázáno.



![Image](assets/fr/16.webp)



Nyní si můžete začít vyměňovat zprávy a další obsah se svým korespondentem!



![Image](assets/fr/17.webp)



Na domovské stránce najdete všechny své konverzace.



![Image](assets/fr/18.webp)



Druhá karta obsahuje všechny kontakty.



![Image](assets/fr/19.webp)



Můžete také vytvářet skupinové diskuse.



![Image](assets/fr/20.webp)



Gratulujeme, nyní jste se seznámili s používáním aplikace Olvid messaging, která je skvělou alternativou k aplikaci WathsApp! Pokud se vám tento návod zdál užitečný, budu vám velmi vděčný, když mi níže zanecháte palec Green. Neváhejte prosím sdílet tento návod na svých sociálních sítích. Děkuji vám mnohokrát!



Doporučuji také tento další tutoriál, ve kterém vám představím Proton Mail, alternativu Gmailu, která je mnohem šetrnější k soukromí:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2