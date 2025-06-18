---
term: TWEAK
---

U kriptografiji, "podešavanje" javnog ključa znači modifikaciju korišćenjem aditivne vrednosti koja se naziva "podešavanje", tako da ostane upotrebljiv uz poznavanje i originalnog privatnog ključa i podešavanja. Tehnički, podešavanje je skalarna vrednost koja se dodaje originalnom javnom ključu. Ako je $P$ javni ključ, a $t$ je podešavanje, podešeni javni ključ postaje :


$$
P' = P + tG
$$


Gde je $G$ generator korišćene eliptičke krive. Ova operacija proizvodi novi javni ključ izveden iz originalnog, dok zadržava određene kriptografske osobine koje omogućavaju njegovo korišćenje. Na primer, ova metoda se koristi za Taproot (P2TR) adrese, kako bi se omogućilo trošenje ili predstavljanjem Schnorr potpisa na tradicionalan način, ili ispunjavanjem jednog od uslova postavljenih u Merkle Tree, takođe poznatom kao "MAST".