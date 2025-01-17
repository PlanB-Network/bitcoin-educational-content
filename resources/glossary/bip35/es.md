---
term: BIP35

---
Propuesta que permite a un nodo Bitcoin abrir información sobre su mempool, es decir, las transacciones que esperan confirmación. Gracias a esto, otros participantes pueden recibir datos en tiempo real sobre transacciones sin confirmar enviando un mensaje específico a un nodo. Antes de la adopción del BIP35, los nodos sólo podían acceder a información sobre transacciones ya confirmadas. Esta mejora ofrece a los monederos SPV la posibilidad de recibir información sobre transacciones no confirmadas, permite a un minero evitar perder transacciones con altas comisiones durante un reinicio, y facilita el análisis de la información del mempool por parte de servicios externos.