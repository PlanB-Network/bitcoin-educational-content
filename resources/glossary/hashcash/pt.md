---
term: HASHCASH
---

HashCash é um sistema de prova de trabalho projetado por Adam Back em 1997 para combater spam e ataques DoS. Baseia-se no princípio de que o remetente deve realizar uma tarefa computacional (especificamente, encontrar uma colisão parcial em uma função de hash criptográfica) para provar seu trabalho. Esta tarefa é custosa em termos de tempo e energia para o remetente, mas verificar o resultado pelo destinatário é rápido e simples. Este protocolo provou ser particularmente adequado para combater spam em comunicações por email, pois é minimamente oneroso para usuários legítimos enquanto representa um obstáculo significativo para spammers. De fato, enviar um único email requer alguns segundos de computação, mas replicar esta operação milhões de vezes torna-se extremamente custoso em termos de energia e tempo, o que muitas vezes anula o interesse econômico de campanhas de spam, sejam elas para fins de marketing ou maliciosos. Além disso, permite a preservação do anonimato do remetente.

HashCash foi rapidamente adotado por cypherpunks que estavam procurando desenvolver um sistema de moeda eletrônica anônima sem intermediários. De fato, a inovação de Adam Back introduziu o conceito de escassez no mundo digital pela primeira vez. O conceito de prova de trabalho é então encontrado em vários sistemas de moeda eletrônica anteriores ao Bitcoin, incluindo:
* b-money por Wei Dai publicado em 1998;
* R-POW por Hal Finney publicado em 2004;
* BitGold por Nick Szabo publicado em 2005.

O princípio do HashCash também é encontrado dentro do protocolo Bitcoin, onde é usado como um mecanismo de proteção contra ataques Sybil.