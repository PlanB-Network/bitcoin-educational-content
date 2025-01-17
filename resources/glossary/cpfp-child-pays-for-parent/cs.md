---
term: CPFP (DÍTĚ PLATÍ ZA RODIČE)

---
Transakční mechanismus, jehož cílem je urychlit potvrzení transakce s bitcoiny, podobně jako je tomu u funkce Replace-by-Fee (RBF), ale ze strany příjemce. Když transakce s příliš nízkými poplatky ve srovnání s trhem zůstane zaseknutá v mempoolech uzlů a nepotvrdí se dostatečně rychle, může příjemce provést novou transakci a utratit bitcoiny získané v zablokované transakci, i když ještě není potvrzená. Tato druhá transakce nutně vyžaduje vytěžení první transakce, aby mohla být potvrzena. Těžaři jsou tedy nuceni zahrnout obě transakce dohromady. Druhá transakce si na transakčních poplatcích vydělá mnohem více než první, a to takovým způsobem, že průměrný poplatek motivuje těžaře k zahrnutí obou transakcí. Dceřiná transakce (druhá) platí za zaseknutou rodičovskou transakci (první). Proto se tato transakce označuje jako "CPFP"

CPFP tak umožňuje příjemci získat své prostředky rychleji i přes nízké počáteční poplatky, které vzniknou odesílateli, na rozdíl od RBF (*Replace-By-Fee*), který umožňuje odesílateli převzít iniciativu k urychlení vlastní transakce zvýšením poplatků.