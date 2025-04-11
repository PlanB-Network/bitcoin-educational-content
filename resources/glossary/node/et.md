---
term: NODE

---
Bitcoini võrgus on sõlme (või inglise keeles "node") arvuti, millel töötab Bitcoini protokolli klient (näiteks Bitcoin Core). See osaleb võrgus, säilitades plokiahela koopiat, edastades ja verifitseerides tehinguid ja uusi plokke ning osaledes valikuliselt kaevandamisprotsessis. Kõikide Bitcoini sõlmede summa moodustab Bitcoini võrgu enda.

Bitcoinis on mitut tüüpi sõlmed, sealhulgas täis- ja kergsõlmed. Täissõlmed hoiavad täielikku koopiat plokiahelast, kontrollivad kõiki tehinguid ja plokke vastavalt konsensusreeglitele ning osalevad aktiivselt tehingute ja plokkide levitamises kogu võrgus. Seevastu kerged sõlmed ehk SPV-sõlmed (*Simple Payment Verification*) hoiavad ainult plokkide päiseid ja sõltuvad tehinguinfo saamisel täis sõlmedest.

> ► * Mõni eristab ka nn "kärbitud sõlmede" ("pruned node" inglise keeles) vahel. Need on täielikud sõlmed, mis laadivad alla ja kontrollivad kõiki Genesis'i plokke, kuid säilitavad mälus ainult kõige uuemad plokid.* *