---
term: BIP
---

Akronim za "Bitcoin Improvement Proposal." Bitcoin Improvement Proposal (BIP) je formalan proces za predlaganje i dokumentovanje poboljšanja i promena Bitcoin protokola i njegovih standarda. Pošto Bitcoin nema centralni entitet koji odlučuje o ažuriranjima, BIP-ovi omogućavaju zajednici da predlaže, diskutuje i implementira poboljšanja na strukturiran i transparentan način. Svaki BIP detaljno opisuje ciljeve predloženog poboljšanja, opravdanja, potencijalne uticaje na kompatibilnost, kao i prednosti i nedostatke. BIP-ove može pisati bilo koji član zajednice, ali ih moraju odobriti drugi programeri i urednici koji održavaju Bitcoin Core GitHub bazu podataka: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun i Ruben Somsen. Međutim, važno je razumeti da uloga ovih pojedinaca u uređivanju BIP-ova ne znači da oni kontrolišu Bitcoin. Ako neko predloži poboljšanje koje nije prihvaćeno u okviru formalnog BIP okvira, i dalje ga može predstaviti direktno Bitcoin zajednici ili čak kreirati Fork uključujući svoju modifikaciju. Prednost BIP procesa leži u njegovoj formalnosti i centralizaciji, što olakšava debatu kako bi se izbegla podela među Bitcoin korisnicima, nastojeći da se ažuriranja implementiraju na konsenzualan način. Na kraju, princip ekonomske većine određuje dinamiku moći unutar protokola.


BIP-ovi su klasifikovani u tri glavne kategorije:


- Standardi Prate BIP-ove*: Odnose se na izmene koje direktno utiču na Bitcoin implementacije, kao što su pravila validacije transakcija i blokova;
- Informativni BIP-ovi*: Pružaju informacije ili preporuke bez predlaganja direktnih promena u protokolu;
- Obradite BIP-ove*: Opišite promene u procedurama koje se odnose na Bitcoin, kao što su procesi upravljanja.


Standardni i informativni BIP-ovi su takođe klasifikovani prema "Layer":


- Konsenzus Layer*: BIP-ovi u ovom Layer odnose se na pravila konsenzusa Bitcoin, kao što su izmene pravila validacije blokova ili transakcija. Ovi predlozi mogu biti ili Soft forkovi (unazad kompatibilne izmene) ili Hard forkovi (nekompatibilne izmene). Na primer, BIP-ovi za SegWit i Taproot pripadaju ovoj kategoriji;
- Peer Services*: Ovaj Layer se odnosi na rad Bitcoin mreže čvorova, odnosno kako čvorovi pronalaze i komuniciraju jedni s drugima na Internetu.
- API/RPC*: BIP-ovi ovog Layer odnose se na Application Programming Interfaces (API) i Remote Procedure Calls (RPC) koji omogućavaju Bitcoin softveru interakciju sa čvorovima;
- Applications Layer*: Ovaj Layer se odnosi na aplikacije izgrađene na Bitcoin. BIP-ovi u ovoj kategoriji obično se bave modifikacijama na nivou Bitcoin Wallet standarda.


Proces podnošenja BIP-a počinje konceptualizacijom i diskusijom ideje na *Bitcoin-dev* mejling listi. Ako je ideja obećavajuća, autor sastavlja nacrt BIP-a prateći specifičan format i podnosi ga putem Pull Request-a na Core GitHub repozitorijumu. Urednici pregledaju ovaj predlog kako bi verifikovali da ispunjava sve kriterijume. BIP mora biti tehnički izvodljiv, koristan za protokol, u skladu sa potrebnim formatiranjem i u skladu sa filozofijom Bitcoin. Ako BIP ispunjava ove uslove, zvanično se integriše u GitHub repozitorijum BIP-ova. Tada mu se dodeljuje broj. Ovaj broj obično određuje urednik, često Luke Dashjr, i dodeljuje se logički: BIP-ovi koji se bave sličnim temama često dobijaju uzastopne brojeve.


BIP-ovi zatim prolaze kroz različite statusne faze tokom svog životnog ciklusa. Trenutni status je naveden u zaglavlju svakog BIP-a:


- Nacrt: Predlog je još uvek u fazi izrade i rasprave;
- Predloženo: BIP se smatra dovršenim i spremnim za pregled od strane zajednice;
- Odloženo: BIP je stavljen na čekanje za kasnije od strane šampiona ili urednika;
- Odbijeno: BIP se klasifikuje kao odbijen ako nije pokazao nikakvu aktivnost tokom 3 godine. Njegov autor može odlučiti da ga kasnije nastavi, što bi mu omogućilo da se vrati u status nacrta;
- Povučen: BIP je povučen od strane autora;
- Final: BIP je prihvaćen i široko implementiran na Bitcoin;
- Aktivno: Samo za BIP-ove procesa, ovaj status se dodeljuje kada se postigne određeni konsenzus;
- Zamenjeno / Zastarelo: BIP više nije primenljiv ili je zamenjen novijim predlogom koji ga čini nepotrebnim.


![](../../dictionnaire/assets/25.webp)


> ► *BIP je akronim za "Bitcoin Improvement Proposal". Na francuskom se može prevesti kao "Proposition d'amélioration de Bitcoin". Međutim, većina francuskih tekstova direktno koristi akronim "BIP" kao zajedničku imenicu, ponekad ženskog, ponekad muškog roda.*