---
term: LABEL (TIHIH PLAĆANJA)
---

U okviru protokola Silent Payments, oznake su celi brojevi korišćeni za modifikaciju početne statičke Address kako bi se kreirale mnoge druge statičke adrese. Korišćenje ovih oznaka omogućava segregaciju uplata poslatih putem Silent Payments, koristeći različite statičke adrese za svaku upotrebu, bez prekomernog povećanja operativnog opterećenja za detekciju ovih uplata (skeniranje). Bob koristi statički Address $B$, sastavljen od dva javna ključa: $B_{\text{scan}}$ za skeniranje i $B_{\text{spend}}$ za trošenje. Hash od $b_{\text{scan}}$ i ceo broj $m$, skalarno pomnožen sa tačkom generatora $G$, dodaje se javnom ključu za trošenje $B_{\text{spend}}$ kako bi se kreirao svojevrsni novi javni ključ za trošenje $B_m$:


$$  B_m = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G  $$


Na primer, prvi ključ $B_1$ se dobija na sledeći način:


$$  B_1 = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$


Staticki Address koji je objavio Bob sada će biti sastavljen od $B_{\text{scan}}$ i $B_m$. Na primer, prvi statički Address sa oznakom $1$ biće:


$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$


Počinjemo samo od oznake $1$, jer je oznaka $0$ rezervisana za promenu. Alisa, koja želi da pošalje bitkoine na označeni statički Address koji je obezbedio Bob, izvešće jedinstvenu uplatu Address $P_0$ koristeći novi $B_1$ umesto $B_{\text{spend}}$:


$$  P_0 = B_1 + \text{Hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$


U stvarnosti, Alice možda čak i ne zna da Bob ima označen Address, jer ona jednostavno koristi drugi deo statičkog Address koji je on obezbedio, što je u ovom slučaju vrednost $B_1$ umesto $B_{\text{spend}}$. Da bi skenirao uplate, Bob će uvek koristiti vrednost svog početnog statičkog Address sa $B_{\text{spend}}$ na sledeći način:


$$   P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$

Zatim će jednostavno oduzeti vrednost koju pronađe za $P_0$ od svakog izlaza jedan po jedan. Zatim proverava da li jedan od rezultata ovih oduzimanja odgovara vrednosti jedne od oznaka koje koristi na svom Wallet. Ako se poklapa, na primer, za izlaz #4 sa oznakom $1$, to znači da je ovaj izlaz Tih Plaćanje povezano sa njegovim statičkim Address označenim sa $B_1$:

$$ Out_4 - P_0 = \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


Ovo funkcioniše zato što:


$$  B_1 = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$


Zahvaljujući ovoj metodi, Bob može koristiti mnoštvo statičkih adresa (sa $B_1$, $B_2$, $B_3$...), sve izvedene iz njegove osnovne statičke Address ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$), kako bi pravilno razdvojio upotrebe.


Međutim, ovo razdvajanje statičkih adresa je validno samo iz perspektive ličnog upravljanja Wallet, ali ne omogućava razdvajanje identiteta. Pošto svi imaju isti $B_{\text{scan}}$, vrlo je lako povezati sve statičke adrese zajedno i zaključiti da pripadaju jednom entitetu.