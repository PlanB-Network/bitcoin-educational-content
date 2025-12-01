---
name: Ashigaru - Černý pasažér
description: Jak mohu provést transakci Payjoin na Ashigaru?
---
![cover](assets/cover.webp)



> *Přinutit blockchainové špiony, aby přehodnotili vše, co si myslí, že vědí.*

Payjoin je struktura transakcí Bitcoin, která je navržena tak, aby zvýšila důvěrnost informací o uživateli tím, že zahrnuje přímou spolupráci s příjemcem platby. Existuje několik implementací, které usnadňují její provádění a automatizují proces. Nejznámější z nich je bezpochyby Stowaway, původně vyvinutá týmem Samurai Wallet a nyní integrovaná do jeho fork Ashigaru.



## Jak Stowaway funguje?



Jak již bylo zmíněno, Ashigaru integruje nástroj PayJoin s názvem `Stowaway`. Ten je k dispozici v aplikaci Ashigaru pro Android. Aby bylo možné provést Payjoin, musí příjemce (který zároveň přebírá roli spolupracovníka) používat software kompatibilní se Stowaway, tj. prozatím pouze Ashigaru.



Černý pasažér je založen na kategorii transakcí, které Samurajové označují jako "Cahoots". Cahoot je kolaborativní transakce mezi několika uživateli, která zahrnuje výměnu informací mimo blockchain Bitcoin. Ashigaru v současné době nabízí dva nástroje Cahoots: Stowaway (Payjoins) a StonewallX2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Transakce Cahoots vyžadují výměnu částečně podepsaných transakcí mezi uživateli. Tento proces může být zdlouhavý, zejména pokud se provádí na dálku. Stále je však možné jej provádět ručně, pokud se spolupracující osoby nacházejí na stejném místě. Konkrétně jde o postupné skenování pěti QR kódů, které si vymění dva účastníci.



Na dálku se tato metoda stává příliš složitou. Aby to Samourai napravil, vyvinul šifrovaný komunikační protokol na bázi Toru s názvem "*Soroban*". Díky Sorobanu jsou výměny potřebné pro Payjoin automatizované a probíhají na pozadí.



Tato šifrovaná komunikace vyžaduje spojení a ověření mezi účastníky systému Cahoot. Proto Soroban spoléhá na Paynymy uživatelů. Pokud ještě nejste obeznámeni s tím, jak Paynyms fungují, podívejte se na tento specializovaný tutoriál, kde se dozvíte více:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

Paynym je stručně řečeno jedinečný identifikátor přiřazený k vašemu účtu wallet, který vám umožňuje aktivovat různé funkce včetně šifrovaných výměn. Má podobu identifikátoru doplněného obrázkem. Zde je například ten, který používám na Testnet:



![Image](assets/fr/01.webp)



**Shrnuto a podtrženo:**





- payjoin" = specifická struktura transakce spolupráce;





- `Stowaway` = implementace Payjoin dostupná na Ashigaru ;





- `Cahoots` = název, který Samouraiové dali všem typům svých kooperativních transakcí, zejména Payjoin `Stowaway`, který dnes převzali na Ashigaru;





- soroban = Šifrovaný komunikační protokol vytvořený na Toru, který umožňuje spolupráci s ostatními uživateli v rámci transakce `Cahoots`;





- paynym" = Jedinečný identifikátor wallet, který se používá k navázání komunikace s jiným uživatelem na platformě "Soroban" za účelem provedení transakce "Chahoots".



Pokud se chcete podrobněji podívat na to, jak Payjoins fungují a jak jsou užitečné pro ochranu soukromí v řetězci, doporučuji tento další tutoriál:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Jak navážu spojení mezi službami Paynyms?



Abyste mohli začít, musíte si samozřejmě nainstalovat Ashigaru a vytvořit :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Chcete-li provést vzdálenou transakci Cahoots, včetně PayJoin (*Stowaway*) prostřednictvím Ashigaru, musíte nejprve "sledovat" uživatele, se kterým chcete spolupracovat, pomocí jeho Paynym. V případě Stowaway to znamená sledovat osobu, které chcete poslat bitcoiny. Pokud ještě nevíte, jak sledovat jiný Paynym, podrobný postup najdete v tomto návodu :



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Jak mohu provést Payjoin na Ashigaru?



Chcete-li provést transakci Stowaway, klikněte na obrázek svého Paynymu v levém horním rohu obrazovky a poté otevřete nabídku `Spolupracovat`. Osoba, která se s vámi účastní transakce, musí udělat totéž, pokud si QR kódy nevyměňujete osobně.



![Image](assets/fr/02.webp)



Máte dvě možnosti: vyberte `Initiate`, pokud jste odesílatelem platby, nebo `Participate`, pokud jste příjemcem této platby.



![Image](assets/fr/03.webp)



Pokud jste příjemcem, je postup velmi jednoduchý. Pro vzdálenou spolupráci prostřednictvím sítě Soroban klikněte na `Učastnit se`, zvolte účet, který chcete použít, a poté stiskněte `ČEKAT NA POŽADAVKY NA ÚČET` a vyčkejte na požadavek zaslaný plátcem.



![Image](assets/fr/04.webp)



Naopak při osobní spolupráci prostřednictvím skenování QR kódu přejděte na domovskou stránku wallet, stiskněte ikonu QR kódu v horní části obrazovky a poté naskenujte QR kód poskytnutý plátcem, který transakci iniciuje.



![Image](assets/fr/05.webp)



Pokud jste v roli plátce, tj. iniciátora transakce, přejděte do nabídky `Spolupracovat` a vyberte možnost `Iniciovat`.



![Image](assets/fr/06.webp)



Protože chceme provést transakci Payjoin Stowaway, zvolte tuto možnost.



![Image](assets/fr/07.webp)



Poté si můžete vybrat mezi online spoluprací (*Cahoots* přes *Soroban*) nebo osobní spoluprací s výměnou QR kódů.



![Image](assets/fr/08.webp)



### Cahoots online



Pokud jste zvolili možnost `Online`, vyberte příjemce ze sledovaných systémů Paynyms.



![Image](assets/fr/09.webp)



Klikněte na `Nastavit transakci` a poté vyberte účet, ze kterého chcete provést výdaj.



![Image](assets/fr/10.webp)



Na další stránce zadejte údaje o transakci: částku, která má být odeslána příjemci, a sazbu poplatku. Adresu příjemce není třeba zadávat, protože příjemce ji předá sám při výměně PSBT.



Poté klikněte na `Přehlédnout nastavení transakce`.



![Image](assets/fr/11.webp)



Pečlivě zkontrolujte informace, ujistěte se, že váš spolupracovník poslouchá požadavky *Cahoots*, a poté klikněte na zelené tlačítko `Začít TRANSAKCI` pro zahájení výměny PSBT prostřednictvím Sorobanu.



![Image](assets/fr/12.webp)



Počkejte, dokud oba účastníci transakci nepodepíší, a pak ji odvysílejte v síti Bitcoin.



![Image](assets/fr/13.webp)



### Osobní diskuse



Pokud chcete výměnu provést osobně, vyberte typ transakce `STONEWALL X2` a poté možnost `Osobně / ručně`.



![Image](assets/fr/14.webp)



Klikněte na `Nastavit transakci` a poté vyberte účet, ze kterého chcete provést výdaj.



![Image](assets/fr/15.webp)



Na další stránce zadejte údaje o transakci: částku, která má být odeslána příjemci, a sazbu poplatku. Adresu příjemce není třeba zadávat, protože příjemce ji předá sám při výměně PSBT.



Poté klikněte na `Přehlédnout nastavení transakce`.



![Image](assets/fr/16.webp)



Zkontrolujte údaje a poté stiskněte zelené tlačítko `Začít transakci` a začněte vyměňovat PSBT prostřednictvím skenování QR kódu.



![Image](assets/fr/17.webp)



Výměna se provádí střídavým skenováním se spolupracovníkem: kliknutím na `ZOBRAZIT QR KÓD` zobrazíte svůj QR kód spolupracovníkovi, který jej naskenuje. On pak kliknutím na `ZOBRAZIT QR KÓD` zobrazí svůj kód a vy jej naskenujete pomocí `ZAPOJIT QR skener`. Tento postup opakujte, dokud nebude dokončeno všech pět kroků výměny.



![Image](assets/fr/18.webp)



Po dokončení všech výměn zkontrolujte podrobnosti transakce a poté ji uvolněte přetažením zelené šipky v dolní části obrazovky.



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). Její struktura je následující:



![Image](assets/fr/20.webp)



*Kredit: [mempool.space](https://mempool.space/)*



Analyzujeme-li tuto transakci, vidíme na vstupní straně můj UTXO ve výši `164 211 sats` a také UTXO ve výši `190 002 sats`, který patří skutečnému příjemci platby. Na výstupní straně obdržím výměnný UTXO ve výši `63 995 sats`, zatímco příjemce obdrží UTXO ve výši `290 002 sats`. Porovnáme-li vstupy a výstupy, vidíme, že příjemce skutečně vydělal `100 000 sats`, což odpovídá výši mé skutečné platby, a že já jsem přišel o `100 000 sats`, k nimž jsem připočetl náklady mining.



Tuto strukturu mohu samozřejmě popsat, protože jsem transakci sám vytvořil. Ale pro vnějšího pozorovatele je obecně nemožné určit, které UTXO patří kterému účastníkovi, ať už na vstupu nebo na výstupu.



Chcete-li prohloubit své znalosti o správě soukromí v onchainu na platformě Bitcoin, doporučuji vám absolvovat mé školení BTC 204 na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c