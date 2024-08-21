---
term: INDEKS (VÕTME NUMBER)
---

HD rahakoti kontekstis viitab see järjestikusele numbrile, mis on määratud lapsevõtmele, mis on genereeritud vanemvõtmest. Seda indeksit kasutatakse koos vanemvõtme ja vanemahela koodiga, et deterministlikult tuletada unikaalseid lapsevõtmeid. See võimaldab struktureeritud korraldust ja mitme sama vanemvõtmest pärineva lapsevõtmepaari korduvat genereerimist. See on 32-bitine täisarv, mida kasutatakse `HMAC-SHA512` tuletusfunktsioonis. See number seega eristab HD rahakotis olevaid õdede-vendade lapsevõtmeid.