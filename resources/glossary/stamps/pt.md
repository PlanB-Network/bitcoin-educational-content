---
term: STAMPS
---

Um protocolo que permite a integração de dados de imagem formatados diretamente na blockchain do Bitcoin por meio de transações multisignature brutas (P2MS). Stamps codifica o conteúdo binário de uma imagem em base 64 e o adiciona às chaves de um P2MS 1/3. Uma chave é real e é usada para gastar os fundos, enquanto as outras duas são chaves fictícias (a chave privada associada é desconhecida) que armazenam os dados. Ao codificar os dados diretamente como chaves públicas, em vez de usar saídas `OP_RETURN`, as imagens armazenadas com o protocolo Stamps são particularmente intensivas em termos de carga de trabalho para os nós. Este método cria notavelmente múltiplos UTXOs, o que aumenta o tamanho do conjunto de UTXOs e apresenta problemas para os nós completos.