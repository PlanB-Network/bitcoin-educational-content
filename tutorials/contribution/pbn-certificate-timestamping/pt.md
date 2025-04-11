---
name: Carimbo de Tempo de certificados e diplomas da Rede Plan ₿
description: Entenda como a Rede Plan ₿ emite prova verificável para o seu certificado e diplomas
---

![cover](assets/cover.webp)

Se você está lendo isso, há uma grande probabilidade de você receber um Certificado Bitcoin ou um diploma de conclusão de um dos cursos que fez na Rede Plan ₿, então parabéns por esta conquista!

Neste tutorial, vamos ver como a Rede Plan ₿ emite prova verificável para o seu Certificado Bitcoin ou qualquer Diploma de Conclusão de Curso. Em seguida, na segunda parte, veremos como verificar a autenticidade dessas provas.

# Mecanismo de prova da Rede Plan ₿

Na Rede Plan ₿, oferecemos a você um certificado e diplomas que são assinados criptograficamente por nós e carimbados no Timechain (ou seja, o blockchain do Bitcoin). Para alcançar isso, tivemos que criar um mecanismo de prova que depende de 2 operações criptográficas:

1. Uma assinatura GPG em um arquivo de texto que sintetiza suas conquistas
2. O carimbo de tempo deste arquivo assinado via [opentimestamps](https://opentimestamps.org/).

Basicamente, a primeira operação permite que você verifique quem emitiu o certificado (ou diploma), enquanto a segunda permite que você verifique quando foi emitido.
Acreditamos que este simples mecanismo de prova nos permite emitir certificados e diplomas com provas inegáveis que qualquer um pode verificar por conta própria.

![image](./assets/proof-mechanism.webp)

Note que, graças a este mecanismo de prova, qualquer tentativa de alterar até o menor detalhe do seu certificado ou diploma criará um hash sha256 completamente diferente do arquivo assinado, o que revelaria imediatamente a adulteração porque a assinatura e o carimbo de tempo não seriam mais válidos. Além disso, se alguém tentar forjar maliciosamente alguns certificados ou diplomas em nome da Rede Plan ₿, uma simples verificação da assinatura revelaria a fraude.

## Como funciona a assinatura GPG?

A assinatura GPG é obtida com o uso de um software de código aberto chamado GNU Private Guard. Este software permite que qualquer pessoa crie facilmente chaves privadas, assine e verifique assinaturas e também criptografe e descriptografe arquivos. Para o escopo deste tutorial, saiba que a Rede Plan ₿ usa GPG para criar sua chave privada/pública e para assinar qualquer Certificado Bitcoin ou Diploma de Conclusão de Curso.

Por outro lado, se alguém quiser verificar a autenticidade de um arquivo assinado, pode usar o GPG para importar a chave pública do emissor e verificar. Na segunda parte do tutorial, veremos como fazer isso com um terminal.

Para aqueles que estão curiosos e querem aprender mais sobre este fantástico software, você pode se referir a ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)

## Como funciona o carimbo de tempo?

Qualquer pessoa pode usar o OpenTimestamps para carimbar um arquivo no tempo e obter uma prova verificável da existência do arquivo. Em outras palavras, ele não fornece uma prova de quando o arquivo foi criado, mas uma prova de existência não posterior a um determinado momento.
O OpenTimestamps é capaz de oferecer este serviço gratuitamente graças a uma maneira altamente eficiente de armazenar tal prova no Blockchain do Bitcoin. Ele usa o hash sha256 do arquivo como um identificador único do seu arquivo e constrói uma árvore de Merkle com outros hashes de arquivos enviados por outros usuários e apenas ancora o hash da estrutura da Árvore de Merkle em uma Transação OpReturn.
Uma vez que esta transação estiver em algum bloco, qualquer pessoa com o arquivo inicial e o arquivo `.ots` associado a ele pode verificar a autenticidade da marcação de tempo. Na segunda parte do tutorial, veremos como verificar seu Certificado Bitcoin ou qualquer Diploma de Conclusão de Curso com um terminal e com uma interface gráfica através do site do OpenTimestamps.

# Como verificar um Certificado da Rede Plan ₿ ou Diploma

## Passo 1. Baixe seu Certificado ou Diploma

Faça login no seu painel PBN pessoal.

![image](./assets/login.webp)

Vá para a página de Credenciais clicando no menu lateral esquerdo e selecione sua sessão de exame ou seu Diploma de Conclusão de Curso.

![image](./assets/credential.webp)

Baixe o arquivo zip.

![image](./assets/download.webp)

Extraia o conteúdo clicando com o botão direito no arquivo `.zip` e selecionando "Extrair". Você encontrará três arquivos diferentes dentro:

- Arquivo de texto assinado (por exemplo, certificate.txt)
- Arquivo de timestamp aberto (OTS) (por exemplo, certificate.txt.ots)
- Certificado em PDF (por exemplo, certificate.pdf)

## Passo 2: Verificando a Assinatura do Arquivo de Texto

Primeiro abra um terminal na pasta onde os arquivos estão (clicando com o botão direito na janela da pasta e clicando em "Abrir no Terminal"). Em seguida, siga as instruções abaixo

1. Importe a chave pública PGP da Rede Plan ₿ com o seguinte comando:

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```

Você deve ver uma mensagem como a seguinte se você importou a Chave PGP com sucesso

```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

NOTA: se você ver que 1 chave foi processada e 0 importada, provavelmente você já importou a mesma chave anteriormente e está tudo bem.

2. Verifique a assinatura do certificado ou diploma com o seguinte comando:

```bash
gpg --verify certificate.txt
```

Este comando deve mostrar detalhes sobre a assinatura, incluindo:

- Quem assinou (Rede Plan ₿)
- Quando foi assinado
- Se a assinatura é válida

Este é um exemplo do resultado:

```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```

Se você ver uma mensagem como "BAD signature", isso significa que o arquivo foi adulterado.

## Passo 3: Verificando o Open Timestamp

### Verificando via Interface Gráfica

1. Visite o site do OpenTimestamps: https://opentimestamps.org/
2. Clique na aba "Stamp & Verify".
3. Arraste e solte o arquivo OTS (por exemplo, `certificate.txt.ots`) na área designada.
4. Arraste e solte o arquivo com timestamp (por exemplo, `certificate.txt`) na área designada.
5. O site verificará automaticamente o timestamp aberto e exibirá o resultado.

Se você ver uma mensagem como a seguinte, seu timestamp é válido:
![cover](assets/opentimestamp_wegui_verified.webp)

### Método CLI

NOTA: este procedimento **exigirá um nó local do Bitcoin em execução**

1. Instale o cliente OpenTimestamps a partir do repositório oficial: https://github.com/opentimestamps/opentimestamps-client executando o seguinte comando:

```
pip install opentimestamps-client
```

2. Navegue até o diretório que contém os arquivos do certificado extraídos.

3. Execute o seguinte comando para verificar o carimbo de tempo aberto:

```
ots verify certificate.txt.ots
```

Este comando irá:

- Verificar o carimbo de tempo contra o blockchain do Bitcoin
- Mostrar exatamente quando o arquivo foi carimbado com data e hora
- Confirmar a autenticidade do carimbo de tempo

### Resultados finais

Note que a verificação é bem-sucedida se **ambas** as mensagens a seguir forem exibidas:

1. A assinatura GPG é relatada como **"Boa assinatura da Rede Plan ₿"**
2. A verificação do OpenTimestamps mostra um carimbo de data e hora de um bloco específico do Bitcoin e relata **"Sucesso! O bloco do Bitcoin [altura do bloco] atesta que os dados existiam a partir de [carimbo de data e hora]"**

Agora que você sabe como a Rede Plan ₿ emite prova verificável para qualquer Certificado de Bitcoin e Diploma de Conclusão de Curso, você pode facilmente verificar a integridade dele.

