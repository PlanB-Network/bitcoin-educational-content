---
term: CARIMBOS

---
Um protocolo que permite a integração de dados de imagem formatados diretamente na blockchain da Bitcoin através de transacções de assinatura múltipla em bruto (P2MS). O Stamps codifica o conteúdo binário de uma imagem na base 64 e adiciona-o às chaves de um 1/3 P2MS. Uma chave é real e é usada para gastar os fundos, enquanto as outras duas são chaves fictícias (a chave privada associada é desconhecida) que armazenam os dados. Ao codificar os dados diretamente como chaves públicas em vez de usar saídas `OP_RETURN`, as imagens armazenadas com o protocolo Stamps são particularmente intensivas em termos de carga de trabalho para os nós. Este método cria, nomeadamente, múltiplos UTXOs, o que aumenta o tamanho do conjunto de UTXOs e coloca problemas aos nós completos.