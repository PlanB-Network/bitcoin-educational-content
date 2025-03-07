---
name: Peněženka Proton
description: Instalace a používání peněženky Proton Bitcoin
---
![cover](assets/cover.webp)

Proton je švýcarská společnost specializující se na digitální soukromí, kterou v roce 2014 založili vědci z CERNu. Společnost Proton je známá svými řešeními s otevřeným zdrojovým kódem a nabízí sadu služeb včetně Proton Mail, Proton VPN a Proton Drive.

Společnost Proton nedávno představila Proton Wallet, peněženku s otevřeným zdrojovým kódem, která je k dispozici jako mobilní aplikace nebo webový klient a je propojena s vaším účtem Proton. Funkce peněženky jsou prozatím relativně klasické, se základními nástroji, které se od dobré bitcoinové peněženky očekávají, jako je RBF (*Replace-By-Fee*), tagování nebo možnost přidat přístupovou frázi BIP39.

Zvláštností této peněženky je možnost posílat bitcoiny pomocí e-mailové adresy příjemce, pro kterou Proton automaticky vygeneruje prázdnou bitcoinovou adresu spojenou s peněženkou uživatele. Proton plánuje v budoucnu přidat nové funkce, včetně Lightningu a coinjoins (pravděpodobně pomocí Whirlpoolu, jak naznačuje aktivita na jejich repozitáři GitHub).

## Vytvoření účtu Proton

Chcete-li používat peněženku Proton, potřebujete účet Proton. Ten si můžete zdarma vytvořit podle prvních kroků tohoto návodu věnovaného vytvoření schránky Proton (pouze část "*Vytvoření účtu Proton*"). Jakmile máte účet zřízen, můžete pokračovat ve zbytku tohoto návodu.

https://planb.network/tutorials/others/general/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## Připojení k peněžence Proton

Přejděte na [webové stránky Proton Wallet](https://proton.me/wallet) a klikněte na tlačítko "*Get Proton Wallet*".

![Image](assets/fr/01.webp)

Vyberte možnost předplatného "*zdarma*" a klikněte na "*Přihlásit se*".

![Image](assets/fr/02.webp)

Pro přihlášení zadejte e-mail a heslo spojené s vaším účtem Proton.

![Image](assets/fr/03.webp)

Nyní by se měl zobrazit váš účet. Klikněte na "*Začněte používat Proton Wallet*".

![Image](assets/fr/04.webp)

## Vytvoření peněženky Bitcoin

Vyberte výchozí fiat měnu pro svůj účet a klikněte na "*Vytvořit novou peněženku*".

![Image](assets/fr/05.webp)

Vaše peněženka Bitcoin byla vytvořena. Teoreticky ji můžete začít používat ihned, ale je velmi důležité, abyste si nejprve uložili mnemotechnickou pomůcku. To provedete tak, že v pravém horním rohu rozhraní kliknete na "*Secure your wallet*".

![Image](assets/fr/06.webp)

Pokud jste tak ještě neučinili, budete vyzváni k nastavení zálohy účtu a jeho zabezpečení pomocí metody 2FA. Tato bezpečnostní opatření se sice vztahují na celý váš účet Proton, ale o to větší význam mají, když je do něj integrována vaše bitcoinová peněženka. Důrazně doporučuji, abyste je zavedli.

![Image](assets/fr/07.webp)

Chcete-li mnemotechnickou frázi uložit, klikněte na "*Zálohovat úvodní frázi této peněženky*".

![Image](assets/fr/08.webp)

Zadejte své heslo Proton.

![Image](assets/fr/09.webp)

Poté klikněte na "*Zobrazit seed frázi peněženky*" a zobrazte mnemotechnickou frázi své peněženky.

![Image](assets/fr/10.webp)

Peněženka Proton zobrazí vaši 12slovnou mnemotechnickou frázi. **Tato mnemotechnická pomůcka vám dává plný, neomezený přístup ke všem vašim bitcoinům**. Kdokoli, kdo tuto frázi zná, může vaše prostředky ukrást, a to i bez přístupu k vašemu účtu Proton. Tuto frázi o 12 slovech lze použít k obnovení přístupu k vašim bitcoinům, pokud ztratíte přístup ke svému účtu. Je proto velmi důležité si ji pečlivě uložit a uložit na bezpečném místě.

Můžete ho napsat na kus papíru, nebo pro větší bezpečnost doporučuji vyrýt ho na nerezový podstavec, který ho ochrání před požárem, povodní nebo zřícením.

![Image](assets/fr/11.webp)

Pro více informací o správném způsobu ukládání a správy mnemotechnických frází vřele doporučuji sledovat tento další návod, zejména pokud jste začátečníci:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

_**Na rozdíl od toho, co dělám v tomto návodu, byste tato slova samozřejmě nikdy neměli fotit.**_

Po uložení fráze klikněte na tlačítko "*Done*".

![Image](assets/fr/12.webp)

## Objevte rozhraní

Rozhraní peněženky Proton je velmi intuitivní. Vlevo najdete různé peněženky a k nim přiřazené účty. Účet "*Primary*" je váš hlavní účet. Z důvodu důvěrnosti jsou bitcoiny přijaté prostřednictvím e-mailové adresy Protonu umístěny na samostatném účtu s názvem "*Bitcoin prostřednictvím e-mailu*".

![Image](assets/fr/13.webp)

Chcete-li přidat nový účet, klikněte na "*Přidat účet*".

![Image](assets/fr/14.webp)

Chcete-li vytvořit nové portfolio, klikněte na symbol "*+*" vedle položky "*Peněženky*".

![Image](assets/fr/15.webp)

Zde můžete do nové peněženky přidat přístupovou frázi BIP39.

![Image](assets/fr/16.webp)

Chcete-li si prohloubit znalosti o přístupové frázi, doporučuji tento výukový program:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Přijímání bitcoinů

Chcete-li přijmout bitcoiny do své peněženky, vyberte požadovaný účet v levé části rozhraní a poté klikněte na tlačítko "*Přijmout*".

![Image](assets/fr/17.webp)

Peněženka Proton pak automaticky vygeneruje novou, prázdnou adresu.

![Image](assets/fr/18.webp)

Po dokončení transakce ji najdete v části "*Transakce*". Kliknutím na tlačítko "*+Přidat*" přiřadíte transakci štítek.

![Image](assets/fr/19.webp)

## Odeslat bitcoiny

Když už máte bitcoiny v peněžence, můžete je poslat. V levé části rozhraní vyberte vybraný účet a poté klikněte na "*Odeslat*".

![Image](assets/fr/20.webp)

Zadejte adresu Bitcoin příjemce. QR kód můžete naskenovat kliknutím na malé logo. Chcete-li odeslat na e-mailovou adresu, zadejte ji přímo do tohoto pole. Po zadání adresy Bitcoin klikněte na malou šipku a poté na "*Potvrdit*".

![Image](assets/fr/21.webp)

Zadejte částku, která má být odeslána, buď ve fiat měně, nebo v bitcoinech, a klikněte na tlačítko "*Review*".

![Image](assets/fr/22.webp)

Zvolte poplatek za transakci podle aktuální situace na trhu.

![Image](assets/fr/23.webp)

Přidejte k transakci štítek a překontrolujte všechny údaje. Pokud je vše v pořádku, klikněte na "*Potvrdit a odeslat*" a transakci podepište a odešlete.

![Image](assets/fr/24.webp)

Vaše transakce se nyní zobrazí v části "*Transakce*" vašeho účtu a čeká na potvrzení.

![Image](assets/fr/25.webp)

## Přihlášení do aplikace

Kromě webového klienta je peněženka Proton Wallet dostupná také prostřednictvím mobilní aplikace. Propojením peněženky s vaším účtem Proton můžete synchronizovat peněženku mezi webovým klientem a mobilní aplikací.

Stáhněte si Proton Wallet z obchodu s aplikacemi:


- [V App Store](https://apps.apple.com/us/app/proton-wallet-secure-btc/id6479609548);
- [V obchodě Google Play](https://play.google.com/store/apps/details?id=me.proton.wallet.android).

![Image](assets/fr/26.webp)

Po instalaci klikněte na "*Přihlásit*" a zadejte svou e-mailovou adresu a heslo Proton.

![Image](assets/fr/27.webp)

Poté budete mít přístup ke své peněžence Bitcoin se stejnými funkcemi jako ve webovém klientovi.

![Image](assets/fr/28.webp)

Gratulujeme, nyní víte, jak nastavit a používat peněženku Proton. Pokud se vám tento návod zdál užitečný, budu vám vděčný, když mi níže zanecháte zelený palec. Neváhejte tento článek sdílet na svých sociálních sítích. Děkuji za sdílení!

Pokud chcete jít dál, doporučuji tento návod na Jade Plus, nejnovější hardwarovou peněženku společnosti Blockstream:

https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
