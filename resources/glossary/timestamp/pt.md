---
term: HORODATAGEM
---

A marcação de tempo, ou "Timestamp" em inglês, é um mecanismo que permite associar uma marca temporal exacta a um evento, dado ou mensagem. No contexto geral dos sistemas informáticos, a marcação temporal é utilizada para determinar a ordem cronológica das operações e para verificar a integridade dos dados ao longo do tempo.


No caso específico do Bitcoin, as marcas de tempo são utilizadas para estabelecer a cronologia das transacções e dos blocos. Cada bloco no Blockchain contém um Timestamp que indica a hora aproximada da sua criação. Satoshi Nakamoto fala mesmo de um "servidor Timestamp", no seu Livro Branco, para descrever aquilo a que hoje chamaríamos "Blockchain". O papel do timestamping no Bitcoin é determinar a cronologia das transacções, de modo a que, sem a intervenção de uma autoridade central, se possa determinar qual a transação que chegou primeiro. Este mecanismo permite a cada utilizador verificar a inexistência de uma transação no passado, evitando assim que um utilizador mal intencionado faça uma despesa dupla. Este mecanismo é justificado por Satoshi Nakamoto no seu Livro Branco com a famosa frase: "Este padrão é baseado no tempo Unix, que representa o número total de segundos passados desde 1 de janeiro de 1970.


> ► *Os carimbos de tempo dos blocos são relativamente flexíveis no Bitcoin, uma vez que, para que um Timestamp seja considerado válido, basta que seja superior ao tempo mediano dos 11 blocos que o precedem (MTP) e inferior à mediana dos tempos devolvidos pelos nós (tempo ajustado pela rede) mais 2 horas.*