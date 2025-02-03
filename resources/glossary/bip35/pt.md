---
term: BIP35

---
Proposta que permite a um nó Bitcoin abrir informações sobre o seu mempool, ou seja, as transacções que aguardam confirmação. Graças a isto, outros participantes podem receber dados em tempo real sobre transacções não confirmadas, enviando uma mensagem específica a um nó. Antes da adoção do BIP35, os nós só podiam aceder às informações sobre as transacções já confirmadas. Esta melhoria oferece às carteiras SPV a possibilidade de receber informações sobre transacções não confirmadas, permite que um mineiro evite perder transacções com taxas elevadas durante um reinício e facilita a análise das informações do mempool por serviços externos.