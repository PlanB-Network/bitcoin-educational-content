---
name: COLDCARD Mk4
description: Průvodce nastavením a používáním COLDCARD Mk4 s Sparrow Wallet
---

![cover-mk4](assets/cover.webp)


**Hardware wallet** jsou fyzická zařízení vyrobená pouze pro bezpečné uložení soukromého klíče Bitcoin. Ukládají soukromé klíče offline, což znamená, že se k nim hackeři nedostanou přes internet. Zatímco **softwarové wallet** se používají hlavně pro každodenní transakce, **hardwarové wallet** se často používají k bezpečnému uložení většího množství bitcoinů na dlouhou dobu. Při provádění transakcí Bitcoin pomocí **hardwarových wallet** může wallet podepisovat transakce uvnitř zařízení, takže soukromý klíč není nikdy vystaven prostředí připojenému k internetu.


V tomto návodu se budeme zabývat jedním z nejoblíbenějších hardwarových wallet vyráběných společností Coinkite, Coldcard Mk4. Podíváme se, jak tuto hardwarovou kartu wallet nastavit a používat k provádění transakcí Bitcoin.


## Coldcard Mk4 Přehled


Coldcard Mk4 je hardwarová karta wallet vyrobená společností Coinkite. Toto zařízení je vybaveno obrazovkou, numerickou klávesnicí a ochranným posuvným krytem. Kromě toho zařízení nabízí několik způsobů připojení a interakce, včetně USB-C, provozu na vzduchu pomocí karty MicroSD, NFC a režimu virtuálního disku. Model Mk4 obsahuje také pokročilé bezpečnostní funkce, jako je BIP39 passphrase a trikové kódy PIN, které uživatelům poskytují větší kontrolu a ochranu nad zařízením Bitcoin.


## Počáteční nastavení: PIN a slova proti phishingu


Chcete-li začít, můžete si Coldcard Mk4 zakoupit přímo na [webových stránkách Coinkite](https://store.coinkite.com/store). Kupující si také mohou zvolit platbu fiat měnou nebo kartou Bitcoin. Kromě toho budete potřebovat také kartu MicroSD (stačí 4 GB) a zdroj napájení, který lze připojit pomocí kabelu USB-C (Coldcard Mk4 má pouze vstupní port USB-C). Upozorňujeme, že jelikož karta Mk4 nemá vestavěnou baterii, musí být po celou dobu používání připojena ke zdroji napájení.


Sadu Mk4 obdržíte v sáčku, který je zabezpečen proti manipulaci. Ujistěte se, že sáček nebyl porušen. Pokud si všimnete něčeho, co by mohlo být problémem, například poškození nebo protržení sáčku, můžete o tom informovat společnost Coinkite zasláním e-mailu na adresu support@coinkite.com. Kromě toho najdete na sáčku s ochranou proti manipulaci také 12místné číslo, které budeme označovat jako číslo sáčku Mk4. Toto číslo sáčku bude později použito k ověření, že se zařízením nebylo během přepravy manipulováno a že pochází přímo od společnosti Coinkite. Číslo sáčku je bezpečně uloženo v kartě Coldcard secure element pomocí flash paměti OTP (One-Time-Programmable), což znamená, že po naprogramování jej nelze změnit. Při prvním zapnutí zařízení musí číslo zobrazené na displeji odpovídat číslu na sáčku. Tím je zajištěno, že zařízení Mk4, které jste obdrželi, je originální zařízení z výroby a nebylo vyměněno nebo upraveno. Ačkoli toto ověření potvrzuje integritu zařízení pouze v okamžiku prvního zapnutí, secure element nadále chrání vaše soukromé klíče, kód PIN a passphrase, takže je velmi obtížné, aby jakýkoli zásah ohrozil vaše zařízení Bitcoin. Kromě toho správné postupy, jako je řádné zabezpečení dat souvisejících s kartou wallet, budou přínosem pro celkové zabezpečení samotné karty Cold. Další informace naleznete v tomto [článku](https://blog.coinkite.com/understanding-mk4-security-model/), který podrobně popisuje bezpečnostní model karty Cold.


Klávesnice se skládá z 10 číselných tlačítek, tlačítka OK (`✓`) a tlačítka zrušit (`✕`). Některá číselná tlačítka lze použít také pro navigaci: `5` pro navigaci nahoru (`^`), `7` pro navigaci doleva (`<`), `8` pro navigaci dolů `˅` a `9` pro navigaci doprava (`>`).


![01](assets/en/01.webp)


Pokud nejsou s obalem žádné problémy, můžete sáček otevřít. Zařízení Mk4 se dodává se záložní kartou wallet, na kterou lze uložit informace týkající se kódu PIN zařízení, slov proti phishingu a karty seedphrase. Při inicializaci postupujte podle následujících kroků:


1. Připravte si papír a pero.

2. Připojte Mk4 ke zdroji napájení (kabel USB-C) a vložte kartu MicroSD.

3. Po prvním zapnutí zařízení se na obrazovce zobrazí zpráva o podmínkách prodeje a používání společnosti Coldcard. Přejděte dolů a pokračujte stisknutím tlačítka `✓`.

4. Poté se na obrazovce zobrazí 12místné číslo. Zkontrolujte toto číslo s číslem na sáčku s ochranou proti manipulaci a s dodatečnou kopií čísla sáčku, která byla přiložena k sáčku s ochranou proti manipulaci, abyste se ujistili, že se zařízením nebylo manipulováno. Pokud se čísla neshodují, obraťte se před dalším postupem okamžitě na podporu společnosti Coinkite. V opačném případě pokračujte stisknutím tlačítka `✓`.


![02](assets/en/02.webp)


5. Zvolte `Zvolit kód PIN`.

6. Při čtení pokynů přejděte na další krok.


![03](assets/en/03.webp)


7. Na zařízení Mk4 vytvořte a zadejte předponu PIN (musí mít 2 až 6 znaků), zapište ji a pokračujte stisknutím tlačítka `✓`.

8. Zapište dvě slova zobrazená na obrazovce. Jedná se o slova proti phishingu. Stiskněte tlačítko `✓` a pokračujte.


![04](assets/en/04.webp)


9. Vytvořte a zadejte příponu PIN (nebo zbytek PIN, musí mít 2 až 6 znaků) a zapište si ji. Pro pokračování stiskněte `✓`.

10. Znovu zadejte předponu PIN. Pro pokračování stiskněte `✓`.


![05](assets/en/05.webp)


11. Zkontrolujte, zda se slova proti phishingu shodují s těmi, která jste napsali v kroku 8. Stiskněte tlačítko `✓` a pokračujte.

12. Znovu zadejte příponu PIN (nebo zbytek kódu PIN). Pro pokračování stiskněte `✓`.


![06](assets/en/06.webp)


13. Kód PIN a slova proti phishingu jsou nyní úspěšně vytvořeny a uloženy v zařízení Mk4.


![07](assets/en/07.webp)


Všimněte si, že Mk4 vás při každém zapnutí zařízení vždy požádá o zadání kódu PIN. Bez tohoto kódu PIN nebudete mít k zařízení Coldcard Mk4 přístup. Proto se ujistěte, že jste si vytvořili dostatečnou zálohu kódu PIN a slov proti phishingu.


## Nastavení zařízení Wallet


Dalším krokem je nastavení systému wallet. To můžete provést třemi způsoby:


- Vytvoření nové položky wallet (standardní)
- Vytvoření nového wallet s hody kostkou
- Importování modelu wallet


### Vytvoření nové položky wallet (standardní)


Chcete-li vytvořit novou položku wallet, proveďte následující kroky.


1. Zvolte `Nový Wallet` (nebo `Nová osnova slov`) > Zvolte `12 slov` nebo `24 slov (výchozí)` podle svých preferencí.


![08](assets/en/08.webp)


2. Zařízení vygeneruje 12 nebo 24 slov jako seedphrase podle vaší volby. Při pečlivém zapisování jednotlivých slov ve správném pořadí navigujte dolů. Poté pokračujte stisknutím tlačítka `✓`.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

3. Přístroj vás požádá o ověření vašeho kódu seedphrase otázkami v náhodném pořadí (například "Slovo 1 je?", pak "Slovo 5 je?", pak "Slovo 12 je?" atd.) a u každé otázky budou tři možnosti výběru slov. Podívejte se na poznámku z kroku 2 a vyberte správně slova (stisknutím `1`, `2` nebo `3`, podle toho, které odpovídá správnému slovu), abyste dokončili tvorbu wallet.


![09](assets/en/09.webp)


4. Mk4 se poté zeptá, zda chcete povolit NFC/Tap, nebo ne. Pro tuto možnost zatím vyberte možnost `✕`. V budoucnu lze tuto možnost v nastavení změnit.

5. A konečně, pokud chcete vypnout port USB (který lze použít pro přenos dat, která nejsou připojena přes airgapp), Mk4 také vypne. Pro tuto možnost prozatím vyberte možnost `✓`. V budoucnu lze tuto volbu v nastavení změnit.

6. Na obrazovce se nyní zobrazí hlavní nabídka s nápisem `Připraveno k podpisu` v horní části. Tím je proces vytváření wallet dokončen.


![10](assets/en/10.webp)


### Vytvoření nového wallet s hodem kostkou


Můžete také zvolit generování nového kódu seedphrase pomocí entropie. Udělejte to, pokud nedůvěřujete čerstvě vygenerovanému seedphrase z Mk4.


Postup u modelu Coldcard Mk4 je následující:


1. Zvolte `Nový Wallet` (nebo `Nová klíčová slova`) > Zvolte `Hod 12 slovními kostkami` nebo `Hod 24 slovními kostkami` podle svých preferencí.

2. Budete vyzváni k zadání výsledků hodů kostkou. Každý hod kostkou přidává do procesu vytváření wallet náhodnost, což zajišťuje, že váš seedphrase je generován zcela bezpečným a nepředvídatelným způsobem. Minimální počet hodů je 50 pro 12slovný seedphrase a 99 pro 24slovný seedphrase. Po zadání alespoň 99 hodnot hodu kostkou stiskněte tlačítko `✓`.


![11](assets/en/11.webp)


3. Zařízení vygeneruje 12 nebo 24 slov jako seedphrase podle vaší volby. Při pečlivém zapisování jednotlivých slov ve správném pořadí navigujte dolů. Poté pokračujte stisknutím tlačítka `✓`.

4. Přístroj vás požádá o ověření vašeho čísla seedphrase otázkami v náhodném pořadí (například "Slovo 1 je?", pak "Slovo 5 je?", pak "Slovo 12 je?" atd.) a u každé otázky budou tři možnosti výběru slov. Podívejte se na poznámku z kroku 3 a vyberte správně slova (stisknutím `1`, `2` nebo `3`, podle toho, které odpovídá správnému slovu), abyste dokončili tvorbu wallet.


![12](assets/en/12.webp)


5. Mk4 se poté zeptá, zda chcete povolit NFC/Tap, nebo ne. Pro tuto možnost zatím vyberte možnost `✕`. V budoucnu lze tuto možnost v nastavení změnit.

6. A konečně, pokud chcete zakázat port USB (který lze použít pro přenos dat bez airgappingu), Mk4 také vypne. Pro tuto možnost prozatím vyberte možnost `✓`. V budoucnu lze tuto volbu v nastavení změnit.

7. Na obrazovce se nyní zobrazí hlavní nabídka s nápisem `Připraveno k podpisu` v horní části. Tím je proces vytváření wallet ukončen.


![13](assets/en/13.webp)


### Import modelu wallet


Poslední možností je importovat soubor wallet. To můžete udělat, pokud chcete obnovit model wallet z modelu seedphrase, který již máte. Můžete postupovat podle následujících kroků:


1. Vyberte možnost `Importovat existující`.

2. Vyberte `24 slov`, `18 slov` nebo `12 slov` v závislosti na počtu slov seedphrase.


![14](assets/en/14.webp)


3. Karta Coldcard Mk4 se vás poté zeptá, co je každé slovo v pořadí za sebou. U každého slova přejděte dolů nebo nahoru, dokud nenajdete předponu pro psaní každého slova. Přístroj bude zužovat možnosti, dokud nenajdete správné slovo. Stejně postupujte i u ostatních slov.

4. Pro poslední slovo zobrazí karta Coldcard Mk4 pouze omezený počet možných slov. Pokud se nenajde žádná shoda, je možné, že jste slova zadali špatně. V opačném případě vyberte slovo, které odpovídá slovu na kartě seedphrase.


![15](assets/en/15.webp)


5. Mk4 se poté zeptá, zda chcete povolit NFC/Tap, nebo ne. Pro tuto možnost zatím vyberte možnost `✕`. V budoucnu lze tuto možnost v nastavení změnit.

6. A konečně, pokud chcete zakázat port USB (který lze použít pro přenos dat bez airgappingu), Mk4 také vypne. Pro tuto možnost prozatím vyberte možnost `✓`. V budoucnu lze tuto volbu v nastavení změnit.

7. Na obrazovce se nyní zobrazí hlavní nabídka s nápisem `Připraveno k podpisu` v horní části. Tím je proces vytváření wallet ukončen.


![16](assets/en/16.webp)


Vezměte na vědomí, že seedphrase je jediným přístupem k obnově wallet. Vytvořte si zálohu zařízení seedphrase a uložte ji na bezpečném místě. **Nejsou to vaše klíče, nejsou to vaše mince**, kdokoli má váš seedphrase, má přístup k vašim bitcoinům!


## Nastavení passphrase


Jedním z nejlepších postupů při použití Bitcoin je použití passphrase. passphrase funguje jako 13. nebo 25. slovo navíc ke slovu seedphrase. Liší se tím, že si můžete vybrat libovolnou frázi, zatímco seedphrase se vybírá z předem určeného seznamu 2048 slov. Ve výchozím nastavení po nastavení wallet začínáte s wallet s prázdným passphrase. Chcete-li nastavit neprázdnou položku passphrase, jednoduše proveďte následující kroky:


1. Přejděte na `Passphrase`.

2. Přejděte dolů a přečtěte si popis passphrase, poté stiskněte `✓` a pokračujte.

3. Vyberte možnost `Upravit frázi`.


![17](assets/en/17.webp)


4. Zadejte číslo passphrase:


   - Stisknutím `1` (písmena), `2` (číslice) nebo `3` (symboly) vyberte typ znaku.
   - Stisknutím tlačítka `4` můžete přepínat mezi malými a velkými písmeny (lze použít pouze při zadávání písmen).
   - Pomocí `^` nebo `˅` vyberte znak pro passphrase.
   - Mezi znaky se pohybujete pomocí `<` nebo `>`. Pomocí `>` můžete také přidávat mezery.
   - Stisknutím tlačítka `✕` znaky odstraníte.
   - Po dokončení úprav passphrase stiskněte tlačítko `✓`.

5. Ostatní možnosti mají navíc tyto funkce:


   - Funkce `Přidat slovo` nebo `Přidat čísla` slouží k přidání písmen/čísel k právě upravovanému záznamu passphrase.
   - Stisknutím tlačítka `Vymazat vše` vynulujete právě upravovaný model passphrase.
   - Stisknutím tlačítka `CANCEL` se vrátíte do hlavní nabídky.

6. Jako zálohu si zapište passphrase.

7. Stisknutím tlačítka `APPLY` zpřístupníte wallet s právě nastaveným passphrase.

8. Mk4 poté zobrazí 8 znaků dlouhý otisk hlavního klíče. Ten lze považovat za "ID" wallet. Zapište si tento otisk a pokračujte stisknutím tlačítka `✓`.


![18](assets/en/18.webp)


9. Nyní se na displeji wallet zobrazí hlavní nabídka wallet se zadanou hodnotou passphrase.

10. Je důležité si uvědomit, že kód wallet vám neřekne, že jste zadali nesprávný kód passphrase, protože každý kód passphrase odpovídá každému vlastnímu kódu wallet s jedinečnou identitou (otisk hlavního klíče). Proto je vhodné znovu zadat stejný klíč passphrase a zkontrolovat, zda se při něm vytvoří stejný otisk klíče wallet, a ujistit se, že jste jej zadali správně. Za tímto účelem proveďte kroky 11 až 14.

11. V hlavní nabídce vyberte možnost `Restore Master` a stiskněte tlačítko `✓`. Nyní jste zpět v hlavní nabídce wallet s prázdným passphrase.


![19](assets/en/19.webp)


12. Znovu přejděte na `Passphrase` a pokračujte stisknutím `✓`.

13. Znovu vložte číslo passphrase, které jste zapsali v kroku 6, a stiskněte tlačítko `APPLY`.

14. Zkontrolujte 8 znaků dlouhý otisk hlavního klíče s otiskem, který jste si zapsali v kroku 8. Pokud se oba otisky neshodují, je možné, že jste zadali nesprávné znaky. Místo toho můžete vybrat nový klíč passphrase a zopakovat postup od kroku 1. Pokud se však oba otisky prstů shodují, znamená to, že jste kód passphrase zadali správně.

15. Přístroj wallet s vybraným přístrojem passphrase je připraven k použití.


## Exportování Wallet do Sparrow


Stejně jako ostatní hardwarové karty wallet nelze kartu Coldcard Mk4 používat samostatně. Je třeba ji propojit se softwarovou kartou wallet, která slouží jako rozhraní. Softwarová karta wallet umožňuje prohlížet zůstatek, vytvářet transakce a spravovat adresy, zatímco karta Cold tyto transakce bezpečně podepisuje, aniž by kdy došlo k vyzrazení vašich soukromých klíčů.


V tomto výukovém programu použijeme jako rozhraní Sparrow Wallet. Postup exportu wallet je následující:


1. Ujistěte se, že je v zařízení Mk4 vložena karta MicroSD.

2. Proveďte kroky "Nastavení passphrase" na wallet s passphrase, který chcete exportovat. Pokud chcete exportovat wallet s prázdným passphrase, můžete tento krok přeskočit.

3. Přejděte na `Pokročilé/Nástroje` > Zvolte `Exportovat Wallet` > Vyberte `Generický JSON` > Přejděte dolů, jak si přečtete pokyny, a pak stiskněte `✓`.


![20](assets/en/20.webp)


4. Mk4 nyní vytvořila na kartě MicroSD soubor ve formátu `.json`.


![21](assets/en/21.webp)


5. Vyjměte kartu MicroSD z karty Cold a vložte ji do zařízení, ve kterém je nainstalována karta Sparrow Wallet.

6. Otevřít Sparrow Wallet.

7. Klikněte na `Soubor`


![22](assets/en/22.webp)


Dále klikněte na `Nový Wallet`


![23](assets/en/23.webp)


Poté zadejte název zařízení wallet


![24](assets/en/24.webp)


Poté klikněte na `Vytvořit Wallet`


![25](assets/en/25.webp)


8. Vyberte `Script Type`.


![26](assets/en/26.webp)


9. V části Úložiště klíčů vyberte možnost `Airgapped Hardware Wallet`.


![27](assets/en/27.webp)


10. Vyhledejte položku Coldcard a klikněte na tlačítko `Importovat soubor...`.


![28](assets/en/28.webp)


11. Vyberte soubor vytvořený v kroku 4 (soubor ve formátu `.json`).


![29](assets/en/29.webp)


12. V přístroji Mk4 se vraťte do hlavní nabídky a přejděte na `Rozšířené/Nástroje` > `Zobrazit identitu`. Ujistěte se, že otisk prstu zobrazený na obrazovce Mk4 odpovídá otisku prstu na Sparrow Wallet (otisk prstu Master v sekci Keystore)

13. Klikněte na tlačítko `Použít` v pravém dolním rohu.


![30](assets/en/30.webp)


14. Volitelně můžete také přidat heslo pro exportovaný soubor wallet. Toto heslo je vyžadováno při každém otevření aplikace Sparrow Wallet pro přístup ke wallet. Pokud heslo v budoucnu zapomenete, můžete jednoduše zopakovat kroky 1-13 a zvolit nové heslo.


![31](assets/en/31.webp)


15. Model wallet je nyní úspěšně exportován a připraven k použití.


![32](assets/en/32.webp)


## Přijímání bitcoinů


Dále se naučíme přijímat signál Bitcoin pomocí zařízení Mk4. Tento postup je poměrně jednoduchý, protože nemusíte používat samotné zařízení Mk4. Pokud jste již vyexportovali zařízení wallet do zařízení Sparrow, můžete přijímat Bitcoin přímo prostřednictvím Sparrow Wallet. Chcete-li přijímat bitcoiny pomocí zařízení Mk4, postupujte podle následujících kroků:


1. Otevřít Sparrow Wallet.

2. Vyberte možnost `Otevřít Wallet` > Vyberte soubor wallet, do kterého chcete přijímat bitcoiny > Zadejte heslo přiřazené k tomuto souboru wallet.


![33](assets/en/33.webp)


3. V rozhraní Sparrow klikněte na kartu `Příjem` na levé straně rozhraní.


![34](assets/en/34.webp)


4. V horní části se zobrazí adresa a QR kód. Adresu můžete zkopírovat a vložit nebo QR kód naskenovat pomocí wallet, který budete používat k odesílání bitcoinů na Sparrow Wallet. Volitelně můžete zadat označení pro přijaté bitcoiny.


![35](assets/en/35.webp)


5. Po odeslání bitcoinů klikněte v rozhraní Sparrow na záložku `Transakce` na levé straně rozhraní. V horní části historie transakcí uvidíte nový záznam, který odpovídá právě provedené transakci.


![36](assets/en/36.webp)


6. Na levé straně rozhraní můžete také přejít na záložku `UTXOs` a zobrazit právě obdržené bitcoiny.


![37](assets/en/37.webp)


## Odesílání bitcoinů


Na rozdíl od přijímání bitcoinů je k utrácení bitcoinů spojených s kartou Cold nutné použít kartu Cold k podepisování transakcí. Postup odesílání bitcoinů pomocí Mk4 je následující:


1. Vložte kartu MicroSD do zařízení, ve kterém je nainstalována karta Sparrow Wallet.

2. Otevřít Sparrow Wallet.

3. Vyberte možnost `Otevřít Wallet` > Vyberte soubor wallet, který chcete použít k odesílání bitcoinů > Zadejte heslo spojené s tímto souborem wallet.


![38](assets/en/38.webp)


4. V rozhraní Sparrow klikněte na záložku `Odeslat` na levé straně rozhraní.


![39](assets/en/39.webp)


5. Na kartě `Platit na` zadejte adresu, na kterou chcete bitcoiny poslat.

6. Přidání štítku pro transakci.

7. Zadejte částku bitcoinů, kterou chcete poslat.

8. Poplatek zadáte přepnutím tlačítka `Range` nebo přímo zadáním čísla do části `Fee`.


![40](assets/en/40.webp)


9. V pravém dolním rohu klikněte na tlačítko `Vytvořit transakci`.


![41](assets/en/41.webp)


10. Zobrazí se nová karta transakce, jejíž název odpovídá štítku, který jste zadali v kroku 6. Klikněte na tlačítko `Finalizovat transakci k podpisu`.


![42](assets/en/42.webp)


11. Klikněte na `Uložit transakci` a uložte transakci na kartu MicroSD. V případě potřeby soubor přejmenujte. Tímto krokem se transakce uloží jako soubor PSBT.


![43](assets/en/43.webp)


12. Vyjměte kartu MicroSD a vložte ji do karty Coldcard Mk4.

13. Zapněte zařízení Mk4 připojením ke zdroji napájení.

14. Zadejte kód PIN.

15. Přejděte na `Passphrase` a zadejte číslo passphrase z čísla wallet, které chcete použít k odeslání bitcoinů. Pokud chcete použít wallet s prázdným passphrase, tento krok přeskočte.

16. Ujistěte se, že otisk hlavního klíče je stejný jako otisk klíče Sparrow Wallet. Můžete to zkontrolovat na kartě `Nastavení` v levé části rozhraní Sparrow Wallet. Poté stiskněte tlačítko `✓` na zařízení Mk4 a pokračujte. Tím se dostanete do hlavní nabídky.

17. V hlavní nabídce Mk4 vyberte možnost `Připraveno k podpisu`. Na obrazovce se zobrazí zpráva `OKAY TO SEND?`. Ujistěte se, že částka bitcoinů, kterou chcete odeslat, a adresa příjemce jsou správné. Stisknutím tlačítka `✓` potvrdíte nebo `✕` zrušíte.

18. Pokud je na výběr více souborů PSBT, zobrazí Mk4 zprávu `Vyberte soubor PSBT k podpisu`. Pro pokračování stiskněte `✓`. Poté vyberte soubor PSBT, který chcete podepsat, pohybem dolů nebo nahoru. U této transakce proveďte krok 17.


![44](assets/en/44.webp)


19. Mk4 nyní zobrazí zprávu `PSBT Signed` spolu s názvem souboru podepsaného PSBT. Pro pokračování stiskněte `✓`.

20. Vyjměte kartu MicroSD z karty Cold a vložte ji do zařízení, kde je nainstalována karta Sparrow Wallet.

21. V okně Sparrow Wallet klikněte na tlačítko `Načíst transakci`.


![45](assets/en/45.webp)


22. Vyberte soubor se stejným názvem jako soubor vytvořený v kroku 19.


![46](assets/en/46.webp)


23. Klikněte na tlačítko `Vysílání transakce`.


![47](assets/en/47.webp)


24. Vaše transakce byla odeslána a je zpracovávána. Stav potvrzení transakce si můžete prohlédnout na kartě `Transakce`.


![48](assets/en/48.webp)


## Aktualizace firmwaru


### Kontrola verze firmwaru


Firmware Coldcard Mk4 lze vždy aktualizovat na novější verzi. Chcete-li zkontrolovat, zda byl váš Mk4 aktualizován na nejnovější verzi, proveďte následující kroky:

1. Zapněte zařízení Mk4 připojením ke zdroji napájení.

2. Zadejte kód PIN.

3. Přejděte na `Rozšířené/Nástroje` > vyberte `Upgrade firmwaru` > vyberte `Zobrazit verzi`.


![49](assets/en/49.webp)


Zkontrolujte verzi zobrazenou na obrazovce Mk4 oproti verzi na [webové stránce Coinkite](https://coldcard.com/downloads). Pokud se verze liší, můžete firmware aktualizovat na novější verzi.


![50](assets/en/50.webp)


### Aktualizace firmwaru


Pokud chcete firmware aktualizovat na nejnovější verzi, proveďte následující kroky:


1. Vložte kartu MicroSD do notebooku/PC.

2. Přejděte na [webové stránky Coinkite](https://coldcard.com/downloads) a stáhněte si nejnovější firmware na kartu MicroSD (červené tlačítko vpravo od obrázku Mk4 s číslem verze).


![51](assets/en/51.webp)


Kliknutím na `Všechny soubory na Mk4` a vyhledáním verze, kterou chcete stáhnout, si můžete stáhnout i další verze. Stažený soubor bude ve formátu `.dfu`.


![52](assets/en/52.webp)


3. Vyjměte kartu MicroSD a vložte ji do zařízení Mk4.

4. Zapněte zařízení Mk4 připojením ke zdroji napájení.

5. Zadejte kód PIN.

6. Přejděte na `Rozšířené/Nástroje` > Vyberte `Upgrade firmwaru` > Vyberte `Z MicroSD` > Přejděte dolů a přečtěte si pokyny a stiskněte `✓`.


![53](assets/en/53.webp)


7. Vyberte soubor `.dfu`, který jste stáhli v kroku 2.

8. Coldcard Mk4 zobrazí zprávu `Install this new firmware?`. Přejděte dolů a přečtěte si pokyny, poté stiskněte `✓`.


![54](assets/en/54.webp)


9. Počkejte, až Mk4 dokončí instalaci nového firmwaru. Během instalace neodpojujte zdroj napájení.

10. Po dokončení se Mk4 restartuje. Můžete zadat PIN a provést kroky "Kontrola verze firmwaru", abyste zkontrolovali, zda byl firmware aktualizován, nebo ne.


## Pokročilé funkce


### Změna kódu PIN


Pokud chcete změnit přihlašovací kód PIN, proveďte následující kroky:


1. Připravte si pero a list papíru.

2. Zapněte zařízení Mk4 připojením ke zdroji napájení.

3. Zadejte kód PIN.

4. Přejděte do `Nastavení` > vyberte `Nastavení přihlášení` > vyberte `Změnit hlavní PIN`

5. Při čtení zprávy přejděte dolů a pokračujte stisknutím tlačítka `✓`.


![55](assets/en/55.webp)


6. Zadejte svůj starý kód PIN.

7. Zadejte novou předponu PIN (musí mít 2 až 6 znaků) a zapište si ji.

8. Mk4 nyní zobrazí dvě nová slova proti phishingu, zapište si je a pokračujte stisknutím tlačítka `✓`.

9. Zadejte novou příponu PIN (nebo zbytek PIN, musí mít 2 až 6 znaků) a zapište si ji.


![56](assets/en/56.webp)


10. Znovu zadejte novou předponu PIN.

11. Zkontrolujte, zda se slova proti phishingu shodují se slovy, která jste napsali v kroku 8.

12. Znovu zadejte novou příponu PIN (nebo zbytek kódu PIN).


![57](assets/en/57.webp)


13. Váš PIN byl úspěšně změněn.


### PINy triků - Přidat nový trik


Trick PIN je alternativní kód PIN odlišný od kódu, který jste použili při prvním nastavení karty Coldcard Mk4. Když zapnete kartu Mk4, můžete zadat trikový kód PIN místo hlavního kódu PIN a spustit tak určité akce. Chcete-li v Mk4 nakonfigurovat trikový PIN, můžete provést následující kroky:


1. Připravte si pero a list papíru.

2. Zapněte zařízení Mk4 připojením ke zdroji napájení.

3. Zadejte kód PIN.

4. Přejděte do `Nastavení` > vyberte `Nastavení přihlášení` > vyberte `Trikové kódy PIN` > vyberte `Přidat nový trik`.


![58](assets/en/58.webp)


5. Zadejte trikový předčíslí PIN (musí mít 2 až 6 znaků) a zapište si ho.

6. Mk4 nyní zobrazí dvě nová slova proti phishingu, zapište si je a pokračujte stisknutím tlačítka `✓`.

7. Zadejte svou trikovou příponu PIN (nebo zbytek kódu PIN, musí mít 2 až 6 znaků) a zapište si ji.


![59](assets/en/59.webp)


8. Přejděte dolů nebo nahoru a vyberte akci, kterou chcete spárovat s právě vytvořeným trikovým kódem PIN. Seznam akcí je následující:


    - pokud zvolíte možnost `Brick Self`, čipy vašeho Mk4 budou po zadání PIN zničeny, takže váš Mk4 bude trvale nepoužitelný.
    - `Wipe Seed`, můžete si vybrat z následujících akcí:
      - `Vymazat a restartovat`: Po zadání PIN kódu se karta seed vymaže a karta Cold se restartuje.
      - `Silent Wipe`: Karta seed se vymaže bezhlučně, avšak karta Cold se bude chovat, jako by byl PIN zadán nesprávně.
      - `Wipe -> Wallet`: Karta seed se v tichosti vymaže a karta Cold vás přenese do nátlakového režimu wallet.
    - `Duress Wallet`, pokud je vybrána, váš Mk4 povede po zadání kódu PIN k duress wallet.
    - `Odpočítávání přihlášení`, můžete si vybrat z následujících akcí:
      - `Wipe & Countdown`: seed se okamžitě vymaže a Mk4 začne zobrazovat odpočítávání.
      - `Countdown & Brick`: Mk4 se po uplynutí času sama zazdí.
      - `Just Countdown`: Mk4 zahájí odpočítávání a po uplynutí času se restartuje.
    - pokud je vybrána možnost `Look Blank`, po zadání trikového kódu PIN se karta Cold chová, jako by byla vymazána, ale ve skutečnosti je stále v paměti.
    - `Just Reboot`, pokud je tato možnost vybrána, karta Cold se po zadání trikového kódu PIN sama restartuje.
    - `Delta Mode`, Tato pokročilá funkce je určena pro zkušené uživatele a je navržena tak, aby chránila před závažnými hrozbami, jako je například nátlak ze strany osoby s důvěrnými informacemi. Po aktivaci režimu Delta Mode se karta COLDCARD tváří, že otevírá skutečnou kartu wallet, což útočníkovi umožňuje procházet ji a potvrdit, že vypadá jako pravá. Tajně však blokuje podepisování všech transakcí, takže nelze odeslat žádné bitcoiny. Zakáže také přístup k frázi seed a jakýkoli pokus o její zobrazení ji zcela vymaže. Aby falešný kód wallet vypadal přesvědčivěji, musí trikový kód PIN použitý pro režim Delta začínat stejnými čísly jako skutečný kód PIN (takže zobrazuje stejná slova proti phishingu), ale končit jinak.
    - `Odemknout politiku`, pokud je tato možnost vybrána, bude po zadání trikového kódu PIN vypnuta politika SSSP (Single Signer Spending Policy).
    - `Policy Unlock & Wipe`, po jehož výběru se předstírá, že se SSSP zakáže, ale při tom se vymaže seedphrase.

9. Po výběru akce, kterou chcete spárovat s trikovým kódem PIN, potvrďte výběr stisknutím tlačítka `✓`. Váš trikový kód PIN je úspěšně nakonfigurován.

10. V části `Nastavení` > `Nastavení přihlášení` > `Trikové kódy PIN` můžete zobrazit seznam vytvořených trikových kódů PIN a s nimi spojených akcí. Můžete se rozhodnout, zda chcete trikové kódy PIN a akce s nimi spárované znovu nakonfigurovat. Můžete je také skrýt nebo odstranit tak, že vyberete PIN a poté zvolíte `Skrýt trik` nebo `Odstranit trik`.


![60](assets/en/60.webp)


### Záludné kódy PIN - Přidat, pokud je to špatně


Případně můžete přidat akci `Přidat při chybě`, která se spustí po určitém počtu zadání nesprávného kódu PIN. Tuto akci můžete nakonfigurovat provedením následujících kroků:


1. Zapněte zařízení Mk4 připojením ke zdroji napájení.

2. Zadejte kód PIN.

3. Přejděte do `Nastavení` > vyberte `Nastavení přihlašování` > vyberte `Trikové kódy PIN` > vyberte `Přidat při chybě`.


![61](assets/en/61.webp)


4. Mk4 zobrazí zprávu o tomto nastavení. Při čtení vysvětlení přejděte dolů a pokračujte stisknutím tlačítka `✓`.

5. Zadejte počet chybných pokusů, které jsou nutné pro spuštění akce. Poznámka: Maximální počet pokusů je `12`. Je to proto, že Mk4 je navržen tak, že pokud je nesprávný PIN zadán `13`krát, zařízení se samo zablokuje, čímž se stane trvale nepoužitelným. Po zadání čísla pokračujte stisknutím tlačítka `✓`.

6. Pro výběr akce přejděte nahoru nebo dolů. K dispozici jsou následující akce:


   - `Wipe, Stop`: seedphrase se vymaže a na displeji se zobrazí "Seed is wiped, Stop"
   - `Vymazat a restartovat`: seedphrase se vymaže a zařízení se restartuje bez jakéhokoli hlášení.
   - `Silent Wipe`: seedphrase je vymazán tiše a zařízení se chová jako při pokusu o vymazání chybného PINu (bez zjevné zprávy o vymazání).
   - `Brick Self`: Zařízení je trvale deaktivováno a zobrazuje pouze "Bricked"
   - `Poslední šance`: Zadejte znovu špatný PIN a zařízení bude vymazáno.
   - `Just Reboot`: Zařízení se jednoduše restartuje a nic jiného se nemění.

Vyberte akci, kterou chcete použít, a stiskněte `✓` pro pokračování


![62](assets/en/62.webp)


7. Budete přeneseni zpět do adresáře `Nastavení > Nastavení přihlášení > Trick PINs`. V adresáři `Trick PINs:` najdete seznam trikových PINů spolu s akcí `WRONG PIN`. Můžete jej také skrýt nebo odstranit tak, že vyberete PIN a poté zvolíte `Skrýt trik` nebo `Odstranit trik`.


![63](assets/en/63.webp)



## Závěr


Tento návod obsahuje návod, jak nastavit Mk4, jak provádět transakce Bitcoin pomocí Mk4 a jak používat některé pokročilé funkce Mk4. Nabízí bezpečné a flexibilní způsoby ukládání a správy bitcoinů. Jeho konstrukce zajišťuje, že soukromé klíče nikdy neopustí zařízení, zatímco funkce, jako jsou passphrase, trikové PINy a vzduchem řízené transakce, poskytují uživatelům plnou kontrolu nad jejich bezpečnostním nastavením. Lze jej spárovat s Sparrow Wallet a získat tak uživatelsky přívětivé prostředí pro vytváření, podepisování a správu transakcí Bitcoin, aniž by bylo ohroženo soukromí nebo bezpečnost.


Pokud chcete prozkoumat další funkce, můžete se podívat do dokumentace na webových stránkách Coinkite [zde](https://coldcard.com/docs/). Doufám, že pro vás bude tento návod při používání karty Coldcard Mk4 přínosný. Děkuji a příště na shledanou!