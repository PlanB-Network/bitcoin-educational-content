---
term: Label (silent payments)
definition: Heltal som används för att skapa härledda statiska adresser som separerar användningsområden i Silent Payments.
---

Inom Silent Payments-protokollet är etiketter heltal som används för att modifiera den ursprungliga statiska Address för att skapa många andra statiska adresser. Användningen av dessa etiketter gör det möjligt att separera betalningar som skickas via Silent Payments genom att använda olika statiska adresser för varje användning, utan att i alltför hög grad öka den operativa bördan för att upptäcka dessa betalningar (skanning). Bob använder en statisk Address $B$, som består av två publika nycklar: $B_{\text{scan}}$ för scanning och $B_{\text{spend}}$ för utgifter. Hash av $b_{\text{scan}}$ och ett heltal $m$, skalarmultiplicerat med generatorpunkten $G$, läggs till den publika nyckeln för utgifter $B_{\text{spend}}$ för att skapa en sorts ny publik nyckel för utgifter $B_m$:


$$ B_m = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G $$


Till exempel erhålls den första nyckeln $B_1$ på detta sätt:


$$ B_1 = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


Den statiska Address som publiceras av Bob kommer nu att bestå av $B_{\text{scan}}$ och $B_m$. Till exempel, den första statiska Address med etiketten $1$ kommer att vara:


$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$


Vi börjar bara från etikett $1$, eftersom etikett $0$ är reserverad för förändring. Alice, som vill skicka bitcoins till den märkta statiska Address som tillhandahålls av Bob, kommer att härleda den unika betalningen Address $P_0$ med hjälp av den nya $B_1$ istället för $B_{\text{spend}}$:


$$ P_0 = B_1 + \text{Hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$


I verkligheten kanske Alice inte ens vet att Bob har en märkt Address, eftersom hon helt enkelt använder den andra delen av den statiska Address som han tillhandahöll, vilket i det här fallet är värdet $B_1$ snarare än $B_{\text{spend}}$. För att skanna efter betalningar kommer Bob alltid att använda värdet av sin ursprungliga statiska Address med $B_{\text{spend}}$ på detta sätt:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$$

Sedan subtraherar han helt enkelt det värde han hittar för $P_0$ från varje utdata en efter en. Han kontrollerar sedan om något av resultaten av dessa subtraktioner matchar värdet på någon av de etiketter han använder på sin Wallet. Om det stämmer, till exempel för utmatning #4 med etiketten $1$, betyder det att denna utmatning är en Silent Payment associerad med hans statiska Address märkt $B_1$:

$$ Out_4 - P_0 = \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


Detta fungerar eftersom:


$$ B_1 = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


Tack vare denna metod kan Bob använda en mängd statiska adresser (med $B_1$, $B_2$, $B_3$...), som alla härrör från hans statiska bas Address ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$), för att korrekt separera användningar.


Denna separation av statiska adresser är dock endast giltig ur ett personligt Wallet-hanteringsperspektiv, men tillåter inte separation av identiteter. Eftersom de alla har samma $B_{\text{scan}}$ är det mycket lätt att associera alla statiska adresser tillsammans och dra slutsatsen att de tillhör en enda enhet.