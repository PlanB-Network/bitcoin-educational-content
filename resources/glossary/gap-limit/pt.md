---
term: GAP LIMIT

---
Um parâmetro usado no software da carteira Bitcoin para determinar o número máximo de endereços consecutivos não utilizados a serem gerados antes de parar a busca por transações adicionais. Ajustar este parâmetro é muitas vezes necessário quando se recupera uma carteira para garantir que todas as transacções são encontradas. Um Gap Limit insuficiente pode resultar na perda de algumas transacções se os endereços forem ignorados durante as fases de derivação. Aumentar o Limite de intervalo permite que a carteira pesquise mais na sequência de endereços, de modo a recuperar todas as transacções associadas.

De facto, um único `xpub` pode teoricamente derivar mais de 4 mil milhões de endereços de receção (tanto endereços internos como externos). No entanto, o software da carteira não pode derivar e verificar todos eles para uso sem incorrer em um enorme custo operacional. Assim, eles procedem por ordem de índice, pois esta é normalmente a ordem em que todos os softwares de carteira geram endereços. O software regista cada endereço utilizado antes de passar ao seguinte, e pára a sua pesquisa quando encontra um número de endereços consecutivamente vazios. Este número é o chamado Gap Limit.

Se, por exemplo, o Gap Limit estiver definido para `20`, e o endereço `m/84'/0'/0'/0'/0/15/` estiver vazio, a carteira irá derivar endereços até `m/84'/0'/0'/0'/0/34/`. Se este intervalo de endereços não for utilizado, a pesquisa pára aí. Consequentemente, uma transação usando o endereço `m/84'/0'/0'/0'/0/40/` não seria detectada neste exemplo.