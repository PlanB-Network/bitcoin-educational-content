---
term: ADAPTOR SIGNATURE
---

Kryptografická metoda, která umožňuje kombinovat pravý podpis s dalším podpisem (nazývaným "adaptor signature") k odhalení tajného kusu dat. Tato metoda funguje tak, že znalost dvou prvků z platného podpisu, adaptor signature a tajemství umožňuje odvodit chybějící třetí prvek. Jednou z zajímavých vlastností této metody je, že pokud známe adaptor signature naší protistrany a specifický bod na eliptické křivce spojený s tajemstvím použitým k výpočtu tohoto adaptor signature, můžeme poté odvodit vlastní adaptor signature, který bude odpovídat stejnému tajemství, aniž bychom k tomuto tajemství měli přímý přístup. Výměna mezi dvěma zainteresovanými stranami, které si nevěří, tato technika umožňuje současné odhalení dvou citlivých informací mezi účastníky. Tento proces eliminuje potřebu důvěry v okamžité transakce, jako je Coin Swap nebo Atomic Swap. Pojďme si to lépe vysvětlit na příkladu. Alice a Bob si chtějí poslat navzájem 1 BTC, ale nevěří si. Proto použijí adaptor signatures, aby eliminovali potřebu důvěry v druhou stranu této výměny (čímž se stává "atomickou" výměnou). Postupují takto:
* Alice zahájí tuto atomickou výměnu. Vytvoří transakci $m_A$, která pošle 1 BTC Bobovi. Vytvoří podpis $s_A$, který tuto transakci ověří pomocí svého soukromého klíče $p_A$ ($P_A = p_A \cdot G$) a pomocí nonce $n_A$ a tajemství $t$ ($N_A = n_A \cdot G$ a $T = t \cdot G$): 
$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$
&nbsp;
* Alice vypočítá adaptor signature $s_A'$ z tajemství $t$ a jejího skutečného podpisu $s_A$:  
$$s_A' = s_A - t$$
&nbsp;
* Alice pošle Bobovi svůj adaptor signature $s_A'$, její nepodepsanou transakci $m_A$, bod odpovídající tajemství $T$ a bod odpovídající nonce $N_A$. Tyto informace nazýváme "adaptor". Poznamenejme, že pouze s těmito informacemi Bob není schopen získat Aliceiny BTC.
* Bob však může ověřit, že ho Alice neklame. K tomu ověří, že Alicein adaptor signature $s_A'$ odpovídá slíbené transakci $m_A$. Pokud následující rovnice platí, je přesvědčen, že Alicein adaptor signature je platný: 
$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$
&nbsp;
* Toto ověření poskytuje Bobovi jistoty od Alice, takže může pokračovat v procesu atomického swapu s klidem na duši. Poté vytvoří svou vlastní transakci $m_B$, která pošle 1 BTC Alice a jeho vlastní adaptor signature $s_B'$, který bude spojen se stejným tajemstvím $t$, které zatím zná pouze Alice (Bob toto hodnotu $t$ nezná, ale pouze její odpovídající bod $T$, který mu Alice poskytla): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$
&nbsp;
* Bob posílá Alici svůj adaptérní podpis $s_B'$, jeho nepodepsanou transakci $m_B$, bod odpovídající tajemství $T$ a bod odpovídající nonce $N_B$. Alice nyní může kombinovat Bobův adaptérní podpis $s_B'$ s tajemstvím $t$, které zná pouze ona, aby vypočítala platný podpis $s_B$ pro transakci $m_B$, která jí pošle Bobovy BTC: $$s_B = s_B' + t$$
&nbsp;
$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$
&nbsp;
* Alice vysílá tuto podepsanou transakci $m_B$ na Bitcoin blockchain, aby získala BTC, které jí Bob slíbil. Bob se o této transakci dozví na blockchainu. Tím je schopen extrahovat podpis $s_B = s_B' + t$. Z této informace může Bob izolovat slavné tajemství $t$, které potřeboval:
$$t = (s_B' + t) - s_B' = s_B - s_B'$$
&nbsp;
* Toto tajemství $t$ však byla jediná chybějící informace pro Boba, aby mohl vyrobit platný podpis $s_A$, z adaptérního podpisu Alice $s_A'$, který mu umožní ověřit transakci $m_A$ posílající BTC od Alice k Bobovi. Poté vypočítá $s_A$ a na oplátku vysílá transakci $m_A$: $$s_A = s_A' + t$$
&nbsp;
$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$