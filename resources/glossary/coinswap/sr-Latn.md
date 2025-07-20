---
term: COINSWAP
---

Protokol za tajni prenos Ownership između korisnika. Ova metoda ima za cilj prenos vlasništva nad bitkoinima sa jedne osobe na drugu, i obrnuto, bez da ovaj Exchange bude eksplicitno vidljiv na Blockchain. Coinwap koristi pametne ugovore kako bi izvršio prenos bez potrebe za poverenjem između strana.


Zamislimo naivan primer (koji ne funkcioniše) sa Alisom i Bobom. Alisa drži 1 BTC osiguran privatnim ključem $A$, a Bob takođe drži 1 BTC osiguran privatnim ključem $B$. Teoretski, mogli bi Exchange svoje privatne ključeve putem spoljnog komunikacionog kanala da izvrše tajni transfer. Međutim, ovaj naivni metod predstavlja visok rizik u smislu poverenja. Ništa ne sprečava Alisu da zadrži kopiju privatnog ključa $A$ nakon Exchange i kasnije ga iskoristi da ukrade bitkoine, kada ključ bude u Bobovim rukama. Štaviše, nema garancije da Alisa neće primiti Bobov privatni ključ $B$ i nikada ne prosledi svoj privatni ključ $A$ u Exchange. Ovaj Exchange stoga se oslanja na prekomerno poverenje između strana i neefikasan je u osiguravanju sigurnog, tajnog transfera Ownership.


Da bismo rešili ove probleme i omogućili coinswap između strana koje ne veruju jedna drugoj, koristićemo Smart contract sisteme koji čine Exchange "atomskim". To mogu biti HTLC (*Hash Ugovori sa vremenskim zaključavanjem*) ili PTLC (*Ugovori sa vremenskim zaključavanjem tačke*). Ova dva protokola funkcionišu na sličan način, koristeći sistem vremenskog zaključavanja koji osigurava da je Exchange ili uspešno završen ili potpuno otkazan, čime se štiti integritet sredstava obe strane. Glavna razlika između HTLC i PTLC je u tome što HTLC koristi hešove i preimage za osiguranje transakcije, dok PTLC koristi Adaptor potpise.


U scenariju zamene novčića koristeći HTLC ili PTLC između Alise i Boba, Exchange se odvija na siguran način: ili uspe i svako dobije BTC onog drugog, ili ne uspe i svako zadrži svoj BTC. Ovo onemogućava bilo kojoj strani da prevari ili ukrade BTC onog drugog.


Upotreba Adaptor Signatures je posebno zanimljiva u ovom kontekstu, jer omogućava izostavljanje tradicionalnih skripti (mehanizam koji se ponekad naziva "_scriptless scripts_"). Ovo smanjuje troškove povezane sa Exchange. Još jedna velika prednost Adaptor Signatures je što ne zahtevaju upotrebu zajedničkog Hash za obe strane u transakciji, čime se izbegava potreba za otkrivanjem direktne veze između njih u određenim tipovima Exchange.