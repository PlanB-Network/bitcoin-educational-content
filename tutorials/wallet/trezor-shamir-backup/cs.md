---
name: Trezor Shamir Záloha
description: Fráze Mnemonic s jedním a více sdíleními na serveru Trezor
---
![cover](assets/cover.webp)



*Image credit: [Trezor.io](https://trezor.io/)*



## Nové možnosti zálohování v systému Trezor



Od roku 2023 nabízí společnost Trezor nový formát zálohování s názvem ***Single-share Backup***, který postupně nahrazuje klasický přístup založený na BIP39, jenž se vyskytuje u většiny portfolií. Na rozdíl od tradičních 12- nebo 24slovných frází Mnemonic je tento nový formát založen na jediné 20slovné frázi odvozené ze standardu vyvinutého společností SatoshiLabs: **SLIP39**. Cílem je zlepšit robustnost a čitelnost zálohování a zároveň umožnit hladký přechod na distribuovaný model zálohování.



Tento distribuovaný model se nazývá ***Multi-share Backup***. Je založen na stejném principu, ale místo generování jediné věty Mnemonic ji rozdělí na několik fragmentů zvaných ***shares***, z nichž každý je samostatnou větou Mnemonic. Pro obnovení portfolia je třeba určitý počet těchto *dílů* (definovaný *prahovou hodnotou*) znovu spojit. Například ve schématu 3 z 5 obnoví portfolio libovolné 3 *díly* z 5. Vezměte prosím na vědomí, že distribuovaný systém zálohování Trezoru se liší od peněženek Multisig. K utrácení bitcoinů je zapotřebí pouze peněženka Trezor Hardware Wallet. Je vyžadován pouze jeden podpis. Distribuce se uplatňuje pouze na úrovni věty Mnemonic, tj. zálohy.



![Image](assets/fr/01.webp)



Tento systém řeší problém jediného bodu selhání věty Mnemonic bez nevýhod spojených se správou BIP39 Multisig nebo passphrase. Proces obnovy již není založen na jediné informaci, ale na několika, přičemž další výhodou je tolerance ztráty díky prahové hodnotě.



Uživatelé, kteří si vytvořili portfolio pomocí *Zálohování na jedno sdílení*, mohou kdykoli přejít na *Zálohování na více sdílení*, aniž by museli své portfolio migrovat. Přijímací adresy a účty zůstanou stejné. Systém *Multi-share* ovlivňuje pouze zálohování, zatímco zbytek portfolia zůstává beze změny.



Zálohování s více sdíleními* je k dispozici v zařízeních Trezor Model T, Safe 3 a Safe 5. Trezor Model One tuto funkci nepodporuje.



**Důležitá poznámka:** Systém *Multi-share* společnosti Trezor je kryptograficky bezpečný, protože k distribuci používá schéma *Shamir's Secret Sharing*. Důrazně nedoporučujeme aplikovat podobný systém ručně, a to tak, že si sami rozdělíte klasickou frázi Mnemonic. Je to špatná praxe, která výrazně zvyšuje riziko krádeže a ztráty vašich bitcoinů, takže to nedělejte. Klasická fráze Mnemonic je uložena celá.



## Shamirovo tajné sdílení v SLIP39



Kryptografický mechanismus, který je základem zálohování *Multi-share* v systému Trezor, je *Shamir's Secret Sharing Scheme* (SSSS). Jeho princip je následující: tajná informace (v tomto případě seed portfolia) je transformována do matematického polynomu. Poté se vypočítá několik bodů tohoto polynomu, z nichž každý se stane podílem. Původní tajná informace je rekonstruována interpolací polynomu, a to shromážděním minimálního počtu bodů (prahové hodnoty).



Z počtu sdílení pod prahovou hodnotou nelze odvodit žádnou tajnou informaci, což zaručuje dokonalou teoretickou bezpečnost tajné informace. Jinými slovy, ani útočník s neomezeným výpočetním výkonem nemůže uhodnout seed, pokud není dosaženo prahové hodnoty.



SLIP39 používá toto schéma k distribuci portfolia seed. Každý podíl je věta o 20 slovech sestavená ze seznamu 1024 slov (odlišného od seznamu BIP39).



## Nastavení zálohování s více sdíleními v zařízení Trezor



Při vytváření portfolia na Trezoru máte tři různé možnosti:




- Použijte klasickou větu BIP39 Mnemonic o 12 nebo 24 slovech;
- Použijte větu Mnemonic s jedním sdílením (SLIP39);
- Konfigurace více frází Mnemonic v režimu Multi-share (SLIP39).



Pokud se rozhodnete pro frázi SLIP39 Mnemonic s jedním podílem, budete moci později přejít na frázi s více podíly, aniž byste museli portfolio resetovat. Na druhou stranu, pokud začnete s klasickým portfoliem BIP39 (12- nebo 24slovná fráze), nebudete jej moci převést přímo na Multi-share. Budete muset vytvořit nové portfolio Multi-share od začátku a převést své prostředky ze starého portfolia do nového prostřednictvím jedné nebo více transakcí Bitcoin. Jedná se o složitější a nákladnější operaci. Pokud chcete tento přechod provést, doporučuji vám zakoupit nový Trezor Hardware Wallet, abyste nemuseli zadávat svůj seed do portfoliového softwaru.



V tomto tutoriálu se nejprve podíváme na to, jak nastavit více podílů při vytváření portfolia, a v další části se podíváme na to, jak převést jeden podíl na více podílů ve stávajícím portfoliu.



Pokud potřebujete pomoci s počátečním nastavením zařízení, máme pro každý model Trezoru také podrobný návod:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### O novém portfoliu



Nyní jste dokončili počáteční konfiguraci zařízení Trezor a jste připraveni vytvořit portfolio. V aplikaci Trezor Suite klikněte na tlačítko "*Vytvořit nový Wallet*".



![Image](assets/fr/02.webp)



Zvolte možnost "*Zálohování na více sdílení*" a klikněte na "*Vytvořit Wallet*".



![Image](assets/fr/03.webp)



Přijměte podmínky používání na zařízení Trezor a potvrďte vytvoření portfolia.



![Image](assets/fr/04.webp)



V aplikaci Trezor Suite klikněte na "*Pokračovat v zálohování*".



![Image](assets/fr/05.webp)



Pečlivě si přečtěte pokyny, potvrďte je a klikněte na "*Vytvořit zálohu Wallet*".



![Image](assets/fr/06.webp)



Pro více informací o správném způsobu ukládání a správy frází Mnemonic vřele doporučuji tento další návod, zejména pokud jste začátečník:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

V zařízení Trezor vyberte celkový počet sdílených položek, které chcete nakonfigurovat. Nejběžnější konfigurace jsou 2-de-3 a 3-de-5. Pro tento příklad vytvořím 2-de-3, takže vyberu 3 sdílení. Každá sdílená složka bude představovat frázi Mnemonic o 20 slovech.



*Uživatelé zařízení Safe 5 sice na obrazovce uvidí nápis "*Tap to continue*", ale pro potvrzení je třeba přejet prstem nahoru



![Image](assets/fr/07.webp)



Poté potvrďte prahovou hodnotu, tj. počet akcií potřebných k získání přístupu ke Wallet a bitcoinům, které obsahuje.



![Image](assets/fr/08.webp)



Trezor vytvoří různé podíly (fráze Mnemonic) pomocí generátoru náhodných čísel. Ujistěte se, že vás během této operace nikdo nesleduje. Zapište slova uvedená na obrazovce na vámi zvolené fyzické médium. Je důležité, aby byla slova očíslována a seřazena za sebou.



Doporučuji, abyste si každou sdílenou složku zapsali na samostatné médium a pečlivě spravovali jejich ukládání, abyste se vyhnuli tomu, že jich bude několik přístupných na stejném místě. Například v případě konfigurace 2 ze 3, jako je ta moje, by jednou z možností bylo uchovávat jeden podíl u sebe doma, další u důvěryhodného přítele a poslední v bankovním sejfu. Výběr místa uložení bude záviset na vaší osobní bezpečnostní strategii.



V horní části obrazovky vidíte, které sdílení právě sledujete.



samozřejmě nesmíte tato slova nikdy sdílet na internetu, jako to dělám já v tomto návodu. Tento příklad Wallet bude použit pouze na Testnet a na konci návodu bude smazán.**_



![Image](assets/fr/09.webp)



Chcete-li přejít na další slova, klikněte na spodní část obrazovky. Posunutím dolů se můžete vrátit zpět. Jakmile zapíšete všechna slova, podržte prst na obrazovce, abyste se přesunuli na další podíl, a operaci opakujte.



![Image](assets/fr/10.webp)



Na konci každého záznamu sdílení budete vyzváni k výběru slov ve větě Mnemonic, abyste potvrdili, že jste je zapsali správně.



![Image](assets/fr/11.webp)



A to je vše, úspěšně jste zálohovali své portfolio pomocí možnosti Multi-share. Nyní můžete pokračovat ve zbytku pokynů ke konfiguraci.



### Na stávajícím portfoliu s jednou akcií



Pokud již máte Trezor Wallet se zálohou pro jedno sdílení (fráze SLIP39 Mnemonic, nikoli klasická fráze BIP39) a chcete zlepšit dostupnost a bezpečnost své zálohy Wallet, můžete si nastavit systém pro více sdílení, aniž byste museli převádět své bitcoiny.



Za tímto účelem připojte a odemkněte zařízení Hardware Wallet. V aplikaci Trezor Suite přejděte do části Nastavení.



![Image](assets/fr/12.webp)



Přejděte na kartu "*Zařízení*".



![Image](assets/fr/13.webp)



Poté klikněte na "*Vytvořit zálohu více sdílení*".



![Image](assets/fr/14.webp)



Přečtěte si pokyny a klikněte na "*Vytvořit zálohu pro více sdílení*".



![Image](assets/fr/15.webp)



Na obrazovce zařízení Trezor pak musíte zadat aktuální frázi Mnemonic (single-share). Zvolte počet slov (výchozí hodnota je 20).



![Image](assets/fr/16.webp)



Poté pomocí klávesnice na obrazovce zařízení Trezor zadejte jednotlivá slova aktuální fráze Mnemonic.



![Image](assets/fr/17.webp)



Podle pokynů uvedených v předchozí části pak můžete zvolit konfiguraci zálohování s více sdíleními.



![Image](assets/fr/18.webp)



Po vytvoření zálohy pro více sdílení se musíte rozhodnout, co uděláte s původní frází Mnemonic pro jedno sdílení. Protože portfolio Bitcoin zůstává stejné, tato jediná fráze k němu bude vždy umožňovat přístup. To bude záviset na vaší bezpečnostní strategii, ale obecně je vhodné tuto frázi zničit, aby se eliminoval tento jediný bod selhání, což je právě cílem zálohování Multi-share Backup. Pokud se rozhodnete ji zničit, ujistěte se, že tak učiníte bezpečně, protože **stále umožňuje přístup k vašim bitcoinům**.



Gratulujeme, nyní jste se seznámili s používáním zálohování s jedním a více sdíleními v hardwarových peněženkách Trezor. Pokud byste chtěli posunout zabezpečení Wallet ještě o krok dál, podívejte se na tento návod o přístupových frázích BIP39:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Pokud vám tento návod přišel užitečný, budu vám vděčný, když mi níže zanecháte palec Green. Neváhejte tento článek sdílet na svých sociálních sítích. Děkuji vám mnohokrát!



## Další zdroje





- [SLIP-0039: Shamirovo sdílení tajemství pro kódy Mnemonic](https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Multi-share Backup on Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Shamirovo sdílení tajemství](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).