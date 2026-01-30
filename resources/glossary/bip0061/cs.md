---
term: BIP0061

definition: Zpráva o odmítnutí mezi uzly signalizující, proč je transakce nebo blok neplatný. Od verze Bitcoin Core 0.20.0 se již nepoužívá.
---
Zavedení zprávy o odmítnutí do komunikačního protokolu mezi uzly. Cílem BIP61 je přidat mechanismus zpětné vazby, když uzel obdrží od jiného uzlu transakci nebo blok, který považuje za neplatný. Tato zpráva o odmítnutí by umožnila uzlu signalizovat odesílateli důvod odmítnutí. Tento typ komunikace měl zlepšit interoperabilitu mezi různými klienty a komunikaci mezi plnými uzly a klienty SPV. Funkce, které přinesl BIP61, byly nakonec od verze 0.20.0 jádra bitcoinu opuštěny, protože byly považovány za zbytečné a zároveň s sebou nesly zvýšené nároky na šířku pásma.