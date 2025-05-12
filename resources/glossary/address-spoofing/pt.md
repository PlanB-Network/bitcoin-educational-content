---
term: Address SPOOFING
---

Ataque em que um ator malicioso cria um Address (ou outro identificador de pagamento) muito semelhante ao da vítima. O objetivo é induzir o utilizador a copiar este Address errado durante uma transação, o que resulta no envio de bitcoins para o atacante em vez do destino pretendido.


O atacante explora a pressa do utilizador para copiar o Address errado se este efetuar a transação sem verificar a sua exatidão. Em geral, para implementar este ataque, o atacante efectua pagamentos com pequenas quantias para o Wallet da vítima para integrar o Address falso no seu histórico de transacções. Este ataque tende a ser utilizado com altcoins, onde é prática comum reutilizar os mesmos endereços de receção, ao contrário do Bitcoin, onde a utilização de endereços em branco para cada transação é uma prática mais generalizada. No entanto, os utilizadores de Bitcoin não estão imunes a este ataque.


Outro método de colocar o Address errado à frente da vítima é a utilização de software de gestão do Wallet fraudulento que imita o software legítimo, ou a alteração do Address quando uma máquina é comprometida, entre o momento em que é copiado e o momento em que a transação é efectuada. Isto é por vezes referido como "*Address swapping*".


Para se proteger contra estes diferentes métodos de ataque, é importante verificar vários caracteres do Address, especialmente a sua soma de controlo (no final), no ecrã do dispositivo de assinatura antes de assinar a transação.


> ► *Este ataque também é por vezes referido como Address Poisoning