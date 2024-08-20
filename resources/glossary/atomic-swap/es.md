---
term: ATOMIC SWAP
---

Tecnología que permite el intercambio directo de criptomonedas entre dos partes, sin necesidad de confianza y sin requerir un intermediario. Estos intercambios se llaman "atómicos" porque solo pueden resultar en dos resultados:
* O bien el intercambio es exitoso, y ambos participantes han intercambiado efectivamente sus criptomonedas;
* O el intercambio falla, y ambos participantes se retiran con sus criptomonedas originales.

Los Atomic Swaps pueden realizarse tanto con la misma criptomoneda, en cuyo caso también se le denomina "*coinswap*", como entre diferentes criptomonedas. Históricamente, se basaban en "Hash Time-Locked Contracts" (HTLC), un sistema de bloqueo por tiempo que garantiza la finalización o cancelación total del intercambio, preservando así la integridad de los fondos de las partes involucradas. Este método requería protocolos capaces de manejar tanto scripts como timelocks. Sin embargo, en los últimos años, la tendencia ha cambiado hacia el uso de *Adaptor Signatures*. Este segundo enfoque tiene la ventaja de eliminar la necesidad de scripts, reduciendo así los costos operativos. Su otro gran beneficio es que no requiere el uso de hashing idéntico para ambas partes de la transacción, lo que ayuda a evitar revelar un vínculo entre ellas.