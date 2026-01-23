---
term: Address spoofing
definition: Um ataque em que um ator malicioso cria um endereço muito semelhante ao da vítima para enganá-la e desviar seus pagamentos.
---

Ataque em que um ator malicioso cria um Address (ou outro identificador de pagamento) muito semelhante ao da vítima. O objetivo é induzir o utilizador a copiar este Address errado durante uma transação, o que resulta no envio de bitcoins para o atacante em vez do destino pretendido.



O atacante explora a pressa do utilizador para copiar o Address errado se este efetuar a transação sem verificar a sua exatidão. Em geral, para implementar este ataque, o atacante efectua pagamentos com pequenas quantias para o Wallet da vítima para integrar o Address falso no seu histórico de transacções. Este ataque tende a ser utilizado com altcoins, onde é prática comum reutilizar os mesmos endereços de receção, ao contrário do Bitcoin, onde a utilização de endereços em branco para cada transação é uma prática mais generalizada. No entanto, os utilizadores de Bitcoin não estão imunes a este ataque.



Outro método para apresentar um endereço incorreto à vítima é a utilização de software fraudulento de gestão de carteiras que imita software legítimo, ou a modificação do endereço quando uma máquina está comprometida, entre o momento em que é copiado e aquele em que a transação é construída. Isto é por vezes designado como '"*address swapping*"'.



Para se proteger contra estes diferentes métodos de ataque, é importante verificar vários caracteres do Address, especialmente a sua soma de controlo (no final), no ecrã do dispositivo de assinatura antes de assinar a transação.



Este ataque é por vezes também designado como '"*address poisoning*"'.