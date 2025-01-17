---
term: RASKUSTE KORRIGEERIMINE

---
Raskuste kohandamine on perioodiline protsess, mis määrab uuesti kindlaks Bitcoini töö tõestusmehhanismi (kaevandamise) raskuse eesmärgi. See sündmus toimub iga 2016 ploki järel (umbes iga kahe nädala tagant). Selle eesmärk on suurendada või vähendada raskustegurit (mida nimetatakse ka raskuse sihtmärgiks) sõltuvalt sellest, kui kiiresti leiti viimased 2016. aasta plokid. Kohandamise eesmärk on säilitada stabiilne ja prognoositav plokitootmise kiirus, mille sagedus on üks plokk iga 10 minuti järel, hoolimata kaevurite poolt kasutatava arvutusvõimsuse kõikumisest. Raskuse muutus kohandamise ajal on piiratud 4-kordajaga. Valem, mida sõlmed täidavad uue eesmärgi arvutamiseks, on järgmine:

$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$$

&nbsp;

Kus:


- $N$: Uus sihtmärk;
- $A$: Viimase 2016. aasta plokkide vana sihtmärk;
- $T$: Viimase 2016 ploki tegelik koguaeg sekundites;
- $1,209,600$: Sihttööaeg sekundites, et toota 2016 plokki, mille vahel on 10-minutiline intervall.

> ► *Fransi keeles kasutatakse mõnikord ka terminit "reciblage", mis tähistab kohandamist. Inglise keeles nimetatakse seda "Difficulty Adjustment "*