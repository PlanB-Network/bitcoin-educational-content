---
term: PODPIS ADAPTÉRU

---
Kryptografická metoda, která umožňuje kombinovat pravý podpis s dalším podpisem (tzv. "adaptorovým podpisem") a odhalit tak tajnou část dat. Tato metoda funguje tak, že znalost dvou prvků mezi platným podpisem, adaptorovým podpisem a tajným údajem umožňuje odvodit chybějící třetí prvek. Jednou ze zajímavých vlastností této metody je, že pokud známe podpis adaptéru našeho protějšku a konkrétní bod na eliptické křivce spojený s tajemstvím použitým k výpočtu tohoto podpisu adaptéru, můžeme pak odvodit vlastní podpis adaptéru, který bude odpovídat stejnému tajemství, aniž bychom měli přímý přístup k samotnému tajemství. Při výměně mezi dvěma zúčastněnými stranami, které si navzájem nedůvěřují, umožňuje tato technika současné odhalení dvou citlivých informací mezi účastníky. Tento proces eliminuje potřebu důvěry v okamžitých transakcích, jako je výměna mincí nebo atomová výměna. Pro lepší pochopení si uveďme příklad. Alice a Bob si chtějí poslat 1 BTC, ale navzájem si nedůvěřují. Použijí proto adaptérové podpisy, aby v této výměně negovali potřebu důvěry v druhou stranu (čímž se z ní stane "atomická" výměna). Postupují následujícím způsobem:


- Tuto výměnu atomů iniciuje Alice. Vytvoří transakci $m_A$, která pošle Bobovi 1 BTC. Vytvoří podpis $s_A$, který tuto transakci potvrdí pomocí jejího soukromého klíče $p_A$ ($P_A = p_A \cdot G$) a pomocí nonce $n_A$ a tajemství $t$ ($N_A = n_A \cdot G$ a $T = t \cdot G$):

$$s_A = n_A + t + H(N_A + T \paralelní P_A \paralelní m_A) \cdot p_A$$

&nbsp;


- Alice vypočítá podpis adaptéru $s_A'$ z tajenky $t$ a svého skutečného podpisu $s_A$:

$$s_A' = s_A - t$$

&nbsp;


- Alice pošle Bobovi svůj podpis adaptéru $s_A'$, svou nepodepsanou transakci $m_A$, bod odpovídající tajemství $T$ a bod odpovídající nonce $N_A$. Těmto informacím říkáme "adaptér". Všimněte si, že pouze s těmito informacemi není Bob schopen obnovit Alicin BTC.
- Bob si však může ověřit, že ho Alice nepodvádí. Za tímto účelem zkontroluje, zda Alicin podpis adaptéru $s_A'$ odpovídá slíbené transakci $m_A$. Pokud je následující rovnice správná, je přesvědčen, že Alicin podpis adaptéru je platný:

$$s_A' \cdot G = N_A + H(N_A + T \paralelní P_A \paralelní m_A) \cdot P_A$$

&nbsp;


- Toto ověření poskytuje Bobovi záruky od Alice, takže může s klidným svědomím pokračovat v procesu výměny atomů. Poté vytvoří vlastní transakci $m_B$, kterou Alici pošle 1 BTC, a svůj vlastní podpis adaptéru $s_B'$, který bude spojen se stejným tajemstvím $t$, které zná prozatím pouze Alice (Bob nezná tuto hodnotu $t$, ale pouze její odpovídající bod $T$, který mu Alice poskytla): $$s_B' = n_B + H(N_B + T \paralelní P_B \paralelní m_B) \cdot p_B$$

&nbsp;


- Bob pošle Alici svůj podpis adaptoru $s_B'$, svou nepodepsanou transakci $m_B$, bod odpovídající tajemství $T$ a bod odpovídající nonce $N_B$. Alice nyní může zkombinovat Bobův podpis adaptoru $s_B'$ s tajemstvím $t$, které zná pouze ona, a vypočítat platný podpis $s_B$ pro transakci $m_B$, která jí posílá Bobovy BTC:

$$s_B = s_B' + t$$

&nbsp;

$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \paralelní P_B \paralelní m_B) \cdot P_B$$

&nbsp;


- Alice tuto podepsanou transakci $m_B$ odvysílá v blockchainu Bitcoinu, aby získala zpět BTC, které jí Bob slíbil. Bob se o této transakci dozví v blockchainu. Je tedy schopen získat podpis $s_B = s_B' + t$. Z této informace může Bob izolovat známé tajemství $t$, které potřeboval:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$

&nbsp;


- Toto tajemství $t$ však bylo jedinou chybějící informací, aby Bob mohl z Alicina adaptéru podpisu $s_A'$ vytvořit platný podpis $s_A$, který mu umožní ověřit transakci $m_A$ odesílající BTC od Alice Bobovi. Poté vypočítá $s_A$ a postupně odvysílá transakci $m_A$: $$s_A = s_A' + t$$

&nbsp;

$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \paralelní P_A \paralelní m_A) \cdot P_A$$