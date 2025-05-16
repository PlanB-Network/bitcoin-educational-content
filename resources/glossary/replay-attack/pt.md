---
term: REPETIR O ATAQUE
---

No contexto do Bitcoin, um ataque de repetição ocorre quando uma transação válida num Blockchain é maliciosamente reproduzida noutro Blockchain que tenha o mesmo historial de transacções. Por outras palavras, uma transação difundida num canal pode ser reproduzida noutro canal sem o consentimento do remetente da primeira transação.


Tomemos o exemplo de um hipotético Hard Fork a partir do Bitcoin, denominado "*BitcoinBis*". Se fizer um pagamento em bitcoins para comprar uma baguete a um padeiro no Blockchain Bitcoin real, esse mesmo padeiro pode reproduzir essa transação legítima no *BitcoinBis* para obter o mesmo montante em criptomoedas neste Fork, sem qualquer ação da sua parte.


Este tipo de ataque só pode ocorrer no caso de uma ramificação Blockchain com 2 cadeias independentes que persistem ao longo do tempo. Normalmente, este seria o caso do Hard Fork. Para que um ataque de repetição seja possível, as 2 cadeias de blocos devem ter um histórico comum e a transação duplicada deve consumir como entradas UTXOs criadas a partir de transacções anteriores que ocorreram antes da divisão das duas cadeias, ou de transacções anteriores que já tenham sido repetidas num ataque de repetição anterior.


De um modo geral, em informática, um ataque de repetição consiste em intercetar e reutilizar dados válidos para enganar um sistema, repetindo a transmissão original. Isto pode, por vezes, levar à usurpação de identidade numa rede.


> ► *No caso de um ataque de repetição a uma transação Bitcoin, este é por vezes referido simplesmente como uma "transação de repetição". "*