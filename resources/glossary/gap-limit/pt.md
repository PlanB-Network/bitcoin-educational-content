---
term: GAP LIMIT
---

Um parâmetro usado em softwares de carteira Bitcoin para determinar o número máximo de endereços consecutivos não utilizados a serem gerados antes de parar a busca por transações adicionais. Ajustar esse parâmetro é frequentemente necessário ao recuperar uma carteira para garantir que todas as transações sejam encontradas. Um Gap Limit insuficiente pode resultar na perda de algumas transações se endereços foram pulados durante as fases de derivação. Aumentar o Gap Limit permite que a carteira procure mais adiante na sequência de endereços, a fim de recuperar todas as transações associadas.

De fato, um único `xpub` pode teoricamente derivar mais de 4 bilhões de endereços de recebimento (tanto endereços internos quanto externos). No entanto, softwares de carteira não podem derivar e verificar todos eles quanto ao uso sem incorrer em um enorme custo operacional. Assim, eles procedem em ordem de índice, já que esta é normalmente a ordem na qual todos os softwares de carteira geram endereços. O software registra cada endereço usado antes de passar para o próximo, e ele para sua busca quando encontra um número de endereços vazios consecutivamente. Esse número é o que se chama de Gap Limit.

Se, por exemplo, o Gap Limit for definido como `20`, e o endereço `m/84'/0'/0'/0/15/` estiver vazio, a carteira derivará endereços até `m/84'/0'/0'/0/34/`. Se essa faixa de endereços permanecer não utilizada, a busca para ali. Consequentemente, uma transação usando o endereço `m/84'/0'/0'/0/40/` não seria detectada neste exemplo.