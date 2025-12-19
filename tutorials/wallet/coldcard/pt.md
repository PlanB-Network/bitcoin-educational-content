---
name: COLDCARD Mk

description: Criação, backup e uso de uma chave privada Bitcoin com um dispositivo Coldcard e Bitcoin Core
---

![cover](assets/cover.webp)

Criação, backup e uso de uma chave privada Bitcoin com um dispositivo Coldcard e Bitcoin Core

## Guia completo para gerar uma chave privada usando uma Coldcard e usá-la através da interface do seu nó Bitcoin Core!

No cerne do uso da rede Bitcoin está o conceito de criptografia assimétrica: um par de chaves - uma privada e outra pública - que têm a função de criptografar e descriptografar dados, um conceito que garante a confidencialidade de uma comunicação.

No caso do Bitcoin, é gerando esse par de chaves privada e pública que somos capazes de armazenar bitcoins (UTXO ou Unspent Transaction Output) e assinar transações para gastá-los.

Hoje, existem várias ferramentas para facilitar a geração aleatória de uma chave privada e seu backup em formato de texto usando o BIP 39 - um padrão que determina como as carteiras associam uma frase mnemônica (seed phrase) às chaves de criptografia. Mais frequentemente do que não, a frase mnemônica é composta por 12 ou 24 palavras, que devem ser armazenadas de forma segura para permitir a recuperação de uma carteira e seus bitcoins.

Neste artigo, vamos aprender a gerar uma chave privada usando uma Coldcard Mk4, um dos dispositivos mais populares e seguros no mundo do Bitcoin, usando o método de lançamento de dados (Dice roll) para garantir o máximo de entropia, e usá-la com o Bitcoin Core de forma isolada (air-gapped)!

> 🧰| Tenha os seguintes materiais à mão para seguir o guia:
>
> - Dispositivo Coldcard (Mk3 ou Mk4)
> - Cartão microSD (4GB são suficientes)
> - Um cabo USB magnético apenas para energia (mini-usb para Mk3, usb-c para Mk4)
> - Um ou mais dados de qualidade

## Geração de uma nova frase mnemônica com uma Coldcard

Vamos começar o processo de criação da chave privada desde o início, assumindo que você tenha uma Coldcard recém-desembalada na qual um PIN já tenha sido configurado (siga as etapas na Coldcard durante a inicialização do dispositivo).

> 🚨 | Para redefinir a chave privada de uma Coldcard já configurada, siga estas etapas:
> Advanced/Tools > Danger Zone > Seed Functions > Destroy Seed> ✓
>
> _Atenção_: sua Coldcard esquecerá a chave privada após essas etapas. Certifique-se de ter feito o backup da sua frase mnemônica corretamente se quiser poder recuperá-la posteriormente.

## Etapas a seguir:

Conectar a Coldcard com o PIN > Novas Palavras Semente > Rolagem de Dados de 24 Palavras

Faça 100 lançamentos de dados, registrando o resultado de 1 a 6 na Coldcard após cada jogada. Ao praticar esse método, você cria 256 bytes de entropia, favorecendo assim a criação de uma chave privada completamente aleatória. A Coinkite também fornece a documentação necessária para a verificação independente de seu sistema de geração de entropia.

![Screenshot Visuel Cold Card](assets/guide-agora/1.webp)

Após concluir os 100 lançamentos de dados, pressione ✓ e anote as 24 palavras obtidas na ordem. Verifique duas vezes e pressione ✓. Por fim, basta completar o teste de verificação das 24 palavras na Coldcard e pronto, sua nova chave privada está criada!

Em seguida, escolha se deseja ativar ou não as funções NFC (Mk4) e USB, seguindo as etapas exibidas. Uma vez no menu principal, é hora de atualizar o microfirmware do dispositivo. Vá para Avançado/Ferramentas > Atualizar Firmware > Mostrar Versão e consulte o site oficial para validar e baixar a versão mais recente disponível. É recomendável atualizar a Coldcard para obter o máximo de segurança.

Antes de prosseguir, é recomendável anotar a Impressão Digital da Chave Mestra (XFP) associada à chave privada. Esses dados permitem validar rapidamente se você está no wallet correto em caso de recuperação, por exemplo. Vá para Avançado/Ferramentas > Visualizar Identidade > Impressão Digital da Chave Mestra (XFP) e anote a sequência de oito caracteres alfanuméricos obtida. O XFP pode ser anotado no mesmo local da frase mnemônica, não é um dado sensível.

> 💡 É recomendável testar seu backup de frase mnemônica em um software diferente. Para fazer isso de forma segura, consulte nosso artigo Verificar o backup de uma carteira Bitcoin com o Tails em menos de 5 minutos.

## Bônus de segurança: a "Frase Secreta" (opcional)

'Uma frase secreta (passphrase) é um elemento poderoso a ser adicionado a uma configuração de carteira para adicionar uma camada de segurança para proteger seus bitcoins. A frase secreta funciona de certa forma como uma 25ª palavra para a frase mnemônica. Uma vez que você adiciona uma, uma carteira completamente nova é criada, juntamente com uma chave privada e sua frase mnemônica associada. Não é necessário anotar a nova frase mnemônica, pois esta carteira pode ser acessada combinando a frase mnemônica original com a frase secreta escolhida.

O objetivo é anotar a frase secreta separadamente da frase mnemônica, pois um invasor que tenha acesso a esses dois elementos terá acesso aos fundos contidos neles. Por outro lado, um invasor que tenha acesso a apenas um desses dois elementos não terá acesso aos fundos, e é essa vantagem específica que otimiza o nível de segurança da configuração da carteira.

![Adicionar uma frase secreta leva a uma carteira completamente diferente](assets/guide-agora/2.webp)

## Etapas para adicionar uma frase secreta com a Coldcard:

Passphrase > Add Words (recomendado) > Apply. O dispositivo exibirá o XFP da carteira recém-gerada com a frase secreta, que é recomendado anotar juntamente com a frase secreta pelos mesmos motivos mencionados anteriormente.

> 💡 Recursos adicionais relacionados à frase secreta:

> https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af > https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/ > https://armantheparman.com/passphrase/

## Exportando a carteira para o Bitcoin Core

A carteira está pronta para ser exportada para um software para interagir com a rede Bitcoin. Neste guia, vamos usar o Bitcoin Core (v24.1).

Consulte nossos guias de instalação e configuração do Bitcoin Core:

> Executando seu próprio nó com o Bitcoin Core - https://agora256.com/faire-tourner-son-propre-noeud-avec-bitcoin-core/
>
> Configurando o Tor para um nó do Bitcoin Core - https://agora256.com/configuration-tor-bitcoin-core/

Primeiro, insira um cartão micro SD na Coldcard e exporte a carteira para o Bitcoin Core seguindo estas etapas: Advanced/Tools > Export Wallet > Bitcoin Core. Dois arquivos serão gravados no cartão micro SD: bitcoin-core.sig e bitcoin-core.txt. Insira o cartão micro SD no computador em que o Bitcoin Core está instalado e abra o arquivo .txt. Você verá a linha "Para carteira com a chave mestra de impressão digital". Verifique se o XFP de oito caracteres corresponde ao que você anotou ao criar sua chave privada.'

Antes de seguir as instruções do arquivo, vamos começar preparando a carteira na interface do Bitcoin Core, seguindo estes passos: vá para a guia Arquivo > Criar uma carteira. Escolha um nome para sua carteira (termo intercambiável com "porte-monnaie" no Core) e marque as opções Desativar chaves privadas, Criar uma carteira vazia e Carteira de descritores, conforme ilustrado na imagem abaixo. Em seguida, pressione o botão Criar.

![criar uma carteira](assets/guide-agora/3.webp)

Depois de criar a carteira no Bitcoin Core, vá para a guia Janela > Console e verifique se a carteira selecionada no topo da página exibe corretamente o nome da carteira que você criou.

Agora, no arquivo .txt gerado anteriormente pela Coldcard, copie a linha que começa com "importdescriptors" e cole-a no console do Bitcoin Core. Uma resposta que inclua a linha "success": true deve ser retornada.

![janela de nós](assets/guide-agora/4.webp)

Se a resposta contiver "message": "Ranged descriptors should not have a label", apague a entrada "label": "Coldcard xxxx0000" na linha copiada do arquivo .txt e cole novamente a linha completa no console do Bitcoin Core.

Ajuda: https://github.com/Coldcard/firmware/blob/master/docs/bitcoin-core-usage.md

## Validação da importação da carteira no Bitcoin Core

Para garantir que a operação foi bem-sucedida, é necessário validar que a carteira desejada foi importada para o Bitcoin Core. Uma maneira simples de confirmar isso é verificar se os endereços gerados na Coldcard correspondem aos endereços gerados no Bitcoin Core.

Bitcoin Core: Receber > Criar um novo endereço de recebimento
Coldcard: Address Explorer > Escolher o endereço que começa com bc1q. O endereço Coldcard 'bc1q' deve corresponder ao endereço exibido no Bitcoin Core.
Recebendo e enviando transações no modo 'air-gapped'

Receber uma transação é extremamente simples; basta pressionar Receber, rotular a transação (opcional, mas recomendado) e criar um novo endereço de recebimento. Em seguida, basta compartilhar o endereço com o remetente.

Agora, o elemento-chave dessa configuração Coldcard + Bitcoin Core é enviar transações sem que a Coldcard e sua chave privada estejam conectadas à internet, usando um método chamado air-gapped, que utiliza a função TBSP (PSBT - Partially Signed Bitcoin Transactions) do Bitcoin.

Essencialmente, usamos a interface Bitcoin Core para construir uma transação, que posteriormente exportamos para o Coldcard através do cartão micro SD para assinar, e então retornamos o arquivo de transação assinado para o Bitcoin Core e transmitimos a transação para a rede. Precisamos fazer isso porque, de qualquer forma, a carteira importada no Bitcoin Core não possui uma chave privada, apenas a chave pública (que nos permite gerar nossos endereços de recebimento), e, portanto, não é possível assinar uma transação diretamente no software para gastar nossos bitcoins.

Antes de prosseguir, verifique se as seguintes opções estão ativadas em Configurações > Carteira:

> - Ativar funções de controle de moedas
> - Gastar moedas não confirmadas (Opcional)
> - Ativar controles TBPS

![opção](assets/guide-agora/5.webp)

### Etapas para enviar no modo air-gapped:

Enviar > Inputs > escolher o utxo desejado e inserir o endereço do destinatário em Pagar para. Taxa de transação: Escolher... > Personalizado > Inserir a taxa de transação (Bitcoin Core calcula em sats/kilobyte em vez de sat/byte como a maioria das soluções de carteira alternativas. Assim, 4000 sats/kilobyte = 4 sats/byte). Criar uma transação não assinada > salvar o arquivo no seu cartão micro SD e inserir o cartão na Coldcard.

Na Coldcard, pressione Pronto para assinar, verifique os detalhes da transação e pressione ✓ e, uma vez gerados os arquivos assinados, coloque o cartão micro SD de volta no computador.

De volta ao Bitcoin Core, vá para a guia Arquivo > Carregar TBSP de um arquivo e insira o arquivo de transação assinado .psbt. A caixa de diálogo Operações PSBT será exibida na tela, confirmando que a transação está completamente assinada e pronta para ser transmitida. Agora é só pressionar Transmitir transação.

![Operações PSBT](assets/guide-agora/6.webp)

### Conclusão

A combinação do dispositivo Coldcard com o Bitcoin Core, no qual você executa seu próprio nó, é poderosa. Adicione a isso uma chave privada gerada com 100 lançamentos de dados e uma frase secreta, e sua configuração de carteira se torna uma fortaleza sofisticada e robusta.

Não hesite em entrar em contato conosco para compartilhar seus comentários e perguntas! Nosso objetivo é compartilhar nosso conhecimento e aumentar nosso conhecimento dia após dia.
