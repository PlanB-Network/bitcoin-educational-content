---
term: ENTROPIE (ANALÝZA)

---
Ve specifickém kontextu řetězové analýzy je entropie také název ukazatele, odvozený od Shannonovy entropie, kterou vynalezl LaurentMT. Tento ukazatel umožňuje měřit nedostatek znalostí, které mají analytici o přesné konfiguraci bitcoinové transakce. Jinými slovy, čím vyšší je entropie transakce, tím obtížnější je pro analytiky identifikovat pohyby bitcoinů mezi vstupy a výstupy.

V praxi entropie odhaluje, zda transakce z pohledu vnějšího pozorovatele představuje více možných interpretací, a to pouze na základě množství vstupů a výstupů, bez zohlednění dalších vnějších nebo vnitřních vzorců a heuristik. Vysoká entropie je pak synonymem lepší důvěrnosti transakce.

Entropie je definována jako binární logaritmus počtu možných kombinací. Zde je použit vzorec, kde $E$ představuje entropii transakce a $C$ počet možných interpretací:

$$
E = \log_2(C)
$$

S přihlédnutím k hodnotám UTXO zapojených do transakce představuje počet interpretací $C$ počet způsobů, jakými lze vstupy přiřadit k výstupům. Jinými slovy určuje počet interpretací, které může transakce vyvolat z pohledu vnějšího pozorovatele, který ji analyzuje.