---
termi: RPC (REMOTE PROCEDURE CALL)
---

Tietokoneprotokolla, joka mahdollistaa ohjelman suorittaa menettelyn toisella etäkoneella kuin se suoritettaisiin paikallisesti. Erityisesti Bitcoinin kontekstissa sitä käytetään mahdollistamaan sovellusten vuorovaikutus bitcoind:n kanssa. Sitä voidaan käyttää suorittamaan komentoja Bitcoin-solmussa, kuten transaktioiden lähettäminen, lompakoiden hallinta tai tiedon saaminen lohkoketjusta. Tämän vuorovaikutuksen turvallisuus varmistetaan autentikoinnin kautta `.cookie` tiedoston tai tunnistetietojen avulla, jotta vain valtuutetut asiakkaat voivat suorittaa RPC-kutsuja solmussa.

> ► *Englanniksi se voidaan kääntää "Remote Procedure Call" eli "Etämenettelykutsu".*