---
term: FEE SNIPING

---
Scénář útoku, při kterém se těžaři snaží přepsat nedávno potvrzený blok, aby si nárokovali transakční poplatky, které obsahuje, a zároveň přidat transakce s vysokými poplatky, které mezitím dorazily do mempoolu. Konečným cílem tohoto útoku pro těžaře je zvýšit svou ziskovost. Odstřelování poplatků může být stále ziskovější s tím, jak se snižuje odměna za blok a transakční poplatky představují větší část příjmů těžařů. Může být také výhodný, když jsou poplatky obsažené v předchozím bloku výrazně vyšší než poplatky v dalším nejlepším kandidátském bloku. Zjednodušeně lze říci, že těžař stojí z hlediska motivace před touto volbou:


- Těžte normálním způsobem po posledním bloku s vysokou pravděpodobností výhry nízké odměny;
- Pokus o vytěžení předchozího bloku (fee sniping) s nízkou pravděpodobností získání vysoké odměny.

Tento útok představuje riziko pro systém Bitcoin, protože čím více těžařů jej přijme, tím více jsou ostatní těžaři, původně poctiví, motivováni k tomu, aby udělali totéž. Pokaždé, když se totiž k těm, kteří se pokoušejí o fee sniping, připojí nový těžař, zvyšuje se pravděpodobnost, že některý z útočících těžařů uspěje, a pravděpodobnost, že některý z poctivých těžařů řetězec prodlouží, se naopak snižuje. Pokud by byl tento útok prováděn masivně a dlouhodobě, potvrzení bloku by již nebylo spolehlivým ukazatelem neměnnosti bitcoinové transakce. To by mohlo potenciálně způsobit nepoužitelnost systému.

Aby se tomuto riziku zabránilo, většina softwaru peněženek automaticky vyplňuje pole `nLocktime` tak, aby podmínila ověření transakce zařazením do další výšky bloku. Tím se stává nemožným zahrnout transakci do přepisu předchozího bloku. Pokud si uživatelé Bitcoinu rozšířené používání pole `nLocktime` osvojí, výrazně se tím sníží motivace k odstřelování poplatků. Ve skutečnosti podporuje spíše progresi blockchainu než jeho přepisování tím, že snižuje potenciální zisky z něj. Pro transakce Taproot navrhuje BIP326 používat pole `nSequence` podobným způsobem, aby se dosáhlo rovnocenného účinku pole `nLocktime` pro jiné typy transakcí. Tímto použitím by se zabily dvě mouchy jednou ranou, protože by se zároveň zlepšilo soukromí protokolů druhé vrstvy, které používají stejné pole.