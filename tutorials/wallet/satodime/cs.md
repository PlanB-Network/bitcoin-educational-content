---
name: Satodime
description: Zjistěte, jak používat Satodime pomocí mobilní aplikace
---
![cover](assets/cover.webp)



Tento průvodce vás provede instalací, konfigurací a používáním mobilní aplikace Satodime. Dozvíte se, jak převzít kartu, vytvořit trezor, přidat finanční prostředky, odpečetit a obnovit soukromé klíče. Přílohy poskytují zdroje, osvědčené postupy a technická vysvětlení.



## Úvod



**Satodime**, vyvinutý společností **[Satochip](https://satochip.io/fr/)**, je bezpečná karta na doručitele pro hmatatelné a jednoduché ukládání Bitcoin. Funguje jako samoobslužný hardware wallet, kde máte plnou kontrolu nad svými soukromými klíči bez závislosti na třetí straně. Má otevřený zdrojový kód a certifikaci EAL6+ a podporuje až tři nezávislé trezory.



### Pozadí produktu



Satodime, **carte au porteur, patří tomu, kdo jej fyzicky vlastní**, bez nutnosti předchozí registrace nebo identifikace. Vyhovuje potřebě bezpečného přenosného úložiště bitcoinů a umožňuje každému, kdo kartu vlastní, ji používat nebo převádět bitcoiny tím, že ji naskenuje prostřednictvím mobilní aplikace a převezme ji do vlastnictví nebo odpečetí trezory. Na rozdíl od papírové bankovky používá k zapečetění soukromých klíčů bezpečný čip, který se odhalí až po rozpečetění, čímž se karta podobá hotovosti, kde je vlastnictví určeno fyzickým držením. Je ideální pro darování bitcoinů jako dárku, protože usnadňuje bezpečný přenos bitcoinů z ruky do ruky, zatímco mobilní aplikace využívá NFC pro přístupnou interakci se smartphonem.





- Bezpečnost**: Soukromé klíče generované a uložené v čipu odolném proti manipulaci; viditelný stav (zapečetěný, odpečetěný, prázdný).
- Vlastnosti**: Koupit bitcoiny přímo přes aplikaci (partner Paybis); spravovat Mainnet a Testnet.
- Open-source**: Kód pod licencí AGPLv3, ověřitelný na GitHubu.



### Průběžný vývoj



Aplikace se pravidelně vyvíjí. Aktualizace najdete na webových stránkách nebo v obchodech Satochip. Mohou být například přidány nové blockchainy nebo nákupní funkce. Průběžný vývoj sledujte na [Satochip GitHub](https://github.com/Toporin/Satodime-Applet).



## 1. Předpoklady



Než začnete používat **Satodime**, ujistěte se, že máte následující položky:





- Kompatibilní smartphone**: Zařízení se systémem Android nebo iOS s povolenou funkcí NFC.
- Karta Satodime**: Neinicializovaná nebo nová.
- Připojení k internetu**: Pro stažení aplikace.
- Základní znalosti**: Pochopení soukromých/veřejných klíčů a rizik jejich ztráty (nevratné).
- Bezpečné médium**: (papír, kov; nikdy ne digitální).



## 2. Instalace





- Stáhněte si aplikaci** :
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Obchod Google Play](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Zkontrolujte vývojáře (Satochip), abyste se vyhnuli podvodu.
 - Satodime je **open-source**. Zdrojový kód : [Satodime GitHub](https://github.com/Toporin/Satodime-Applet).





- Nainstalujte a spusťte aplikaci**: V případě potřeby aktivujte NFC v telefonu.



![image](assets/fr/01.webp)



## 3. Počáteční konfigurace



### 3.1 Spusťte aplikaci a skenujte



Otevřete aplikaci a postupujte podle průvodce. Přiložte kartu Satodime ke čtečce NFC v telefonu (obvykle na zadní straně). Po celou dobu operace ji držte stisknutou, abyste zajistili stabilní připojení.





- Pokud funkce NFC nefunguje, zkontrolujte nastavení telefonu.
- Přípitek potvrzuje úspěch: "Úspěšné čtení".



![image](assets/fr/02.webp)



Obecně platí, že **všechny následující operace vyžadují potvrzení naskenováním karty Satodime**



### 3.2 Převzetí karty (*Ownership*)



Při prvním použití se staňte vlastníkem karty, abyste ji zabezpečili:





- V aplikaci klikněte na "*Take Ownership*".
- Potvrzení operace: vygeneruje se jedinečný klíč vlastníka.
- Chcete-li změny použít, znovu mapu naskenujte.
- Upozornění**: Tento krok je nevratný. Viz [článek o *vlastnictví*](https://satochip.io/satodime-ownership-explained/).



![image](assets/fr/03.webp)




## 4. Vytvoření bezpečného



Satodime podporuje až 3 trezory. Vytvořte si jeden pro uložení bitcoinů:





- Vyberte prázdný trezor (např. Trezor 01).
- Vyberte blokový řetězec (Bitcoin).
- Klikněte na "*Vytvořit a Seal*".
- Naskenujte kartu do generate a zapečetěte soukromý klíč (neznámý, dokud není odpečetěn).
- Gratulujeme**: Váš trezor je nyní zapečetěn a připraven přijímat finanční prostředky.



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5. Přidání finančních prostředků



Po zapečetění vložte do trezoru bitcoiny:





- Vyberte trezor.
- Klikněte na "*Přidat prostředky*".
- Zkopírujte veřejnou adresu nebo naskenujte QR kód.
- Odeslání prostředků z jiného účtu wallet.
- Zkontrolujte zůstatek po potvrzení v blockchainu.
- Možnost nákupu: Kliknutím na "*Nákup*" můžete nakupovat přímo přes Paybis (Visa, Mastercard atd.). Příslušné poplatky.



![image](assets/fr/06.webp)



## 6. Odpečetění trezoru



Chcete-li získat přístup k soukromému klíči a převést prostředky jinam, odpečetěte trezor:





- Vyberte zapečetěný trezor.
- Klikněte na "Unseal".
- Potvrďte varování: tato operace je nevratná.
- Naskenujte kartu a rozpečetěte ji.
- Trezor je nastaven na "*Unsealed*"; soukromý klíč lze nyní zobrazit/exportovat.
- Upozornění**: Po odpečetění je soukromý klíč přístupný. Pokud se někdo zmocní vašeho chytrého telefonu, může se k tomuto klíči dostat, a získat tak zpět finanční prostředky v trezoru (nevratně).



![image](assets/fr/07.webp)



## 7. Obnovení soukromého klíče



Po rozpečetění vyexportujte klíč pro použití v jiném zařízení wallet :





- Ujistěte se, že jste v bezpečném prostředí.
- Klikněte na "*Zobrazit soukromý klíč*".
- Zvolte formát: Vyberte formát Legacy, SegWit, WIF atd.
- Zkopírujte klíč nebo naskenujte QR kód.
- Bezpečnost**: Nikdy nesdílejte svůj soukromý klíč. Ukládejte jej offline.
- Importujte jej do softwarového programu wallet kompatibilního se správou fondů (například Sparrow Wallet nebo Electrum).



![image](assets/fr/08.webp)





## 8. Resetování kmene



Resetováním trezoru se nevratně odstraní přidružený soukromý klíč. Jinými slovy, pokud jste si nezajistili kopii svého soukromého klíče nebo jej neimportovali do jiné aplikace wallet, resetování trezoru způsobí nevratnou ztrátu prostředků v něm uložených.



![image](assets/fr/09.webp)



Resetováním kmene se slot vyprázdní a je připraven pro nový kmen.



## 9. Převod vlastnictví



Chcete-li například nabízet bitcoiny prostřednictvím služby Satodime, musíte :




- Převezměte vlastnictví karty,
- Vytvořte trezor Bitcoin,
- Přestupní sedačky tam,
- Převod vlastnictví karty: další osoba, která kartu naskenuje, se stane jejím vlastníkem,
- Předejte kartu Satodime vybrané osobě a vyzvěte ji, aby si stáhla aplikaci a poté kartu naskenovala, čímž ji převezme do vlastnictví - a získá tak přístup k bitcoinům, které jsou na ní "uloženy".



![image](assets/fr/10.webp)




## PŘÍLOHY



### A1. Osvědčené postupy



Bezpečné používání služby **Satodime** :





- Zabezpečte kartu**: Ztráta karty = ztráta finančních prostředků, pokud se nejedná o majitele.
- Klíčová záloha**: Po odpečetění nahrajte soukromé klíče na bezpečné fyzické médium. Nikdy ne v digitální podobě.
- Zkontrolujte stav**: Vždy skenujte, abyste potvrdili vlastnictví karty a stav zapečetěných/nezapečetěných trezorů.
- Důvěrnost**: Používejte nové adresy; vyhněte se centralizovaným výměnám pro přenosy.
- Aktualizace**: Aktualizace: Udržujte aplikaci aktuální prostřednictvím obchodů.
- Zotavení**: V případě ztráty karty, která je v držení, jsou prostředky v blockchainu; v případě odpečetění použijte soukromý klíč.



### A2. Další zdroje



Specifické pro Satodime :




- [produkt Satodime](https://satochip.io/fr/product/satodime/)
- [Mobilní průvodce](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Academy](https://planb.academy/) pro výukové programy o self-custody, soukromých klíčích atd.



**Uložte si frázi pro obnovení** :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Návod na Satochip (první výrobek značky) :**



https://planb.academy/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Návody pro ošetřovatele semen:**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. O společnosti Satochip



**Oficiální odkazy** :




- [Site Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Podpora: info@satochip.io



**Satochip** je belgická společnost, která vyvíjí hardwarová a softwarová řešení pro správu a ukládání bitcoinů a dalších kryptoměn. Její vlajkový produkt, hardwarová karta Satochip wallet, je karta NFC vybavená čipem secure element s certifikací EAL6+. Doplněna o Seedkeeper, správce mnemotechnických frází a tajemství, a Satodime, kartu na doručitele, nabízí společnost Satochip ucelený sortiment přizpůsobený potřebám uživatelů. Její zařízení, poháněná softwarem s otevřeným zdrojovým kódem, mají za cíl demokratizovat zabezpečení na Bitcoin.