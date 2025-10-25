---
name: Electrum OP_RETURN
description: Registar uma mensagem sobre o Blockchain Bitcoin com Electrum
---

![cover](assets/cover.webp)




Este tutorial passo a passo mostra como escrever uma mensagem no Blockchain Bitcoin usando o Wallet Electrum. Esta operação utiliza a instrução OP_RETURN para inserir texto numa transação, visível publicamente no Blockchain. Siga estes passos simples para um registo bem sucedido.



---
## Pré-requisitos





- Um computador (Windows, macOS ou Linux).
- Ligação à Internet.
- Alguns satoshis (Sats) ou bitcoins (BTC) no seu Wallet para cobrir o montante da transação e as taxas.
- Um conversor de texto para hexadecimal (por exemplo, um sítio em linha) ou uma ferramenta específica como [este gerador de guião OP_RETURN] (https://resources.davidcoen.it/opreturnelectrum/).



---

## Passo 1: Descarregar e instalar Electrum



![image](assets/fr/01.webp)



1. Visite o sítio Web oficial da Electrum: [electrum.org](https://electrum.org/).


2. Descarregue a versão correspondente ao seu sistema operativo (Windows, macOS, Linux).


3. Instale o Electrum de acordo com as instruções do instalador.


4. Verificar a integridade do ficheiro descarregado (opcional, mas recomendado por razões de segurança), comparando a assinatura do ficheiro ou o Hash.



→ Mais detalhes no tutorial Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Passo 2: Criar ou importar um Wallet



1. Lançar Electrum.


2. Selecione Criar um novo Wallet ou Restaurar um Wallet existente se já tiver uma frase seed (frase de recuperação).


3. Siga as instruções para configurar o Wallet :




 - Para um novo Wallet, tome nota da sua frase seed e guarde-a num local seguro (papel, cofre, etc.).
 - Para um Wallet existente, introduza a sua frase seed para o restaurar.


4. Definir uma palavra-passe para proteger o Wallet.



→ Mais detalhes no tutorial Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Passo 3: Verificar os fundos disponíveis



Certifica-te de que o teu Wallet contém bitcoins (BTC) ou satoshis (Sats) suficientes para :




- Montante da transação (por exemplo, 0,00001 BTC ou 1000 Sats).
- Taxas de transação, que variam em função da dimensão da rede (geralmente alguns milhares de Sats).



Consulte o Saldo em Electrum para verificar os seus fundos.



![image](assets/fr/02.webp)



Se necessário, transfira BTC ou Sats para alimentar o seu Wallet. Para o fazer, aceda ao separador "Receber" e clique em "Criar pedido":



![image](assets/fr/03.webp)



Isto mostrará uma receção Address:



![image](assets/fr/04.webp)



→ Mais detalhes no tutorial Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Etapa 4: Preparar a mensagem a inscrever



Selecionar a mensagem que se pretende introduzir (por exemplo, "Obrigado Satoshi"). Nota: As mensagens OP_RETURN estão limitadas a 80 bytes, ou seja, cerca de 80 caracteres ASCII.



*Pensem um pouco: o que escreverem no Blockchain Bitcoin é eterno e acessível a todos, por isso :*




- deixar uma bela expressão da nossa humanidade,
- evite introduzir conteúdos de que se possa arrepender



*O espaço Blockchain e os seus bitcoins são preciosos, utilize-os sabiamente e com intenção*



Converta a sua mensagem em hexadecimal :




- Pode utilizar uma [ferramenta em linha] (https://www.rapidtables.com/convert/number/ascii-to-hex.html), mas tenha cuidado para não tratar aí dados sensíveis (embora, em princípio, as informações destinadas a publicação no Blockchain Bitcoin através de um OP_RETURN não apresentem quaisquer problemas de confidencialidade);
- Para maior confidencialidade, efectue a conversão localmente utilizando um pequeno ficheiro Python :



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



Exemplo: `Obrigado Satoshi` em ASCII dá `5468616e6b73205361746f736869` em hexadecimal.



Preparar o script da transação. Aqui está um exemplo do formato esperado:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



que é constituído por :





- **Destino Address**: Um Bitcoin Address válido. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. Este pode ser o seu próprio Address, caso pretenda devolver os fundos transferidos a si próprio;
- **Montante transferido**: o montante da transação, aqui `0.00001` BTC. **Atenção**: como a unidade usada em Electrum é BTC, o valor indicado no script da transação também deve ser expresso em BTC, e não em Sats ;
- Script **OP_RETURN**: A mensagem convertida para hexadecimal precedida por script(`OP_RETURN <messsage>), 0`. Aqui, `5468616e6b73205361746f736869` para a mensagem em hexadecimal.



⚠️ **Cuidado**: É muito importante indicar `0` após o OP_RETURN, uma vez que este código de operação marca o script como inválido, tornando a saída permanentemente impossível de gastar. Os nós da rede eliminarão esta saída do seu conjunto UTXO. Se introduzir um valor diferente de `0`, este será irremediavelmente perdido: os seus bitcoins serão considerados queimados. Por isso, deve sempre introduzir `0` num OP_RETURN para registar os dados desejados, mas sem lhe associar fundos, que se perderiam.



Dica: Utiliza a ferramenta [OP_RETURN Generator] (https://resources.davidcoen.it/opreturnelectrum/) para criar automaticamente o script generate. Mesmo que esta ferramenta sugira introduzir o montante em BTC, mantém a unidade configurada em Electrum.



![image](assets/fr/05.webp)



Para mudar a unidade usada pela Electrum, na barra de menu encontre "Preferences", depois na aba "Units" selecione BTC / mBTC / bits ou Sats :



![image](assets/fr/06.webp)




---

## Passo 5: Enviar a transação



Em Electrum, aceda ao separador Enviar.



![image](assets/fr/07.webp)



No campo "Pagar a", cole o guião preparado (por exemplo, o guião acima).



![image](assets/fr/08.webp)



O campo "Pagar a" deve ser apresentado em Green e o montante da transação deve aparecer na linha abaixo.



Verificar o montante e a sua unidade no campo Montante.



Clique em "Pagar..." e ajuste as suas taxas de transação de acordo com o montante que está disposto a pagar e a velocidade a que pretende que a sua transação seja processada por um Miner e integrada num bloco.



![image](assets/fr/09.webp)



Clique em OK e confirme a transação com a sua palavra-passe. Aparecerá uma janela de confirmação.




---

## Passo 6: Verificar o registo



Quando a transação tiver sido confirmada (o que pode demorar alguns minutos), vá para o separador "Histórico".



![image](assets/fr/10.webp)



Clique com o botão direito do rato na transação e selecione "Ver no Explorer" para ver os detalhes.



Em alternativa, copie o Address de destino (por exemplo, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) e visualize-o num explorador Blockchain, como [Mempool.space](https://Mempool.space/) ou [blockstream.info](https://blockstream.info/).



Procure o campo OP_RETURN nos detalhes da transação para ver a sua mensagem.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Sugestões e melhores práticas





- Teste com uma pequena quantia: Comece com uma pequena transação (por exemplo, Sats 1000) para evitar erros dispendiosos.
- Certifique-se de que a saída que contém OP_RETURN é igual a zero, caso contrário os seus bitcoins serão permanentemente perdidos.
- Verifique a unidade: Certifique-se de que o montante introduzido corresponde à unidade apresentada em Electrum (BTC, mBTC ou Sats).
- Taxa de transação: Se a rede estiver congestionada, aumente a taxa para uma confirmação mais rápida.
- Mensagem curta: As entradas OP_RETURN estão limitadas a 80 bytes. Planeie a sua mensagem em conformidade.



---

## Recursos úteis





- Descarregar Electrum: [electrum.org](https://electrum.org/)
- Gerador de guiões OP_RETURN: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Exploradores Blockchain: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)