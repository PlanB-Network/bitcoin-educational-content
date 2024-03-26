---
name: Noeud Bitcoin Core (mac & windows)
description: Instalar o Bitcoin Core no Mac ou Windows
---

Instalar o Bitcoin Core no seu computador regular pode ser feito, mas não é ideal. Se você não se importa de deixar o seu computador ligado 24 horas por dia, 7 dias por semana, então isso funcionará bem. Se você precisar desligar o computador, é irritante ter que esperar o software sincronizar toda vez que você o ligar novamente.

Estas instruções são para usuários de Mac ou Windows. Usuários de Linux provavelmente não precisarão da minha ajuda, mas as instruções para Linux são muito semelhantes às do Mac.

## Comece Limpo

Idealmente, você deseja usar um computador limpo, sem malware. Mesmo se você usar uma carteira de hardware, o malware pode enganá-lo e roubar suas moedas.

Você pode limpar um computador antigo e usá-lo como um computador dedicado ao Bitcoin, ou comprar um computador / laptop dedicado.

## O Disco Rígido

O Bitcoin Core ocupará cerca de 400 gigabytes de dados no seu disco e continuará crescendo. Você pode usar o seu disco interno, mas também pode conectar um disco rígido externo. Explicarei ambas as opções. Idealmente, você deve usar um disco de estado sólido. Se você tiver um computador antigo, provavelmente não terá um desses internamente. Basta comprar um SSD externo de 1 ou 2 terabytes e usá-lo. O disco regular provavelmente funcionará, mas você pode ter problemas e será muito mais lento.

![image](assets/1.webp)

## Baixe o Bitcoin Core

Vá para bitcoin.org (certifique-se de não ir para bitcoin.com, que é um site de shitcoin de propriedade de Roger Ver, enganando as pessoas para comprar Bitcoin Cash em vez de Bitcoin)

Uma vez lá, não é óbvio onde obter o software. Vá para o menu de recursos e clique em "Bitcoin Core", como mostrado abaixo:

![image](assets/2.webp)

Isso o levará à página de download:

![image](assets/3.webp)

Clique no botão laranja "Download Bitcoin Core":

![image](assets/4.webp)

Existem várias opções para escolher, dependendo do seu computador. As duas primeiras são relevantes para este guia; escolha Windows ou Mac na barra lateral esquerda. O download começará depois de clicar nele, provavelmente para o seu diretório de Downloads.

## Verifique o download (parte 1)

Você precisa do arquivo que contém os hashes de várias versões. Este arquivo costumava estar na página de downloads do bitcoin.org, mas agora foi movido para bitcoincore.org/en/download:

![image](assets/5.webp)

Você precisa do arquivo de hashes binários SHA256. Este arquivo contém os hashes SHA256 dos vários pacotes de download do Bitcoin Core.

Em seguida, precisamos calcular o hash do download do Bitcoin Core e compará-lo com o que o arquivo diz que o hash deve ser. Assim, saberemos que o download é idêntico ao esperado, de acordo com o bitcoincore.org.

Navegue novamente até o diretório de Downloads e execute este comando (substitua os X's pelo nome completo do arquivo de download do nó completo do Bitcoin):

```
PARA MAC —–> shasum -a 256 XXXXXXXXXXXX
PARA WINDOWS —–> certutil -hashfile XXXXXXXXXXX SHA256
```

Você receberá um resultado de hash. Anote-o e compare-o com o hash contido no arquivo SHA256SUMS.
Se os resultados forem idênticos, então você verificou que nenhum bit de dados foi adulterado... quase. Ainda precisamos ter certeza de que o arquivo SHA256SUMS não é malicioso.
Para prosseguir com a próxima etapa, precisamos ter o gpg instalado em nosso computador.

Para fazer isso, consulte meu guia SHA256/gpg e role até a seção "Download gpg", procurando o subtítulo do seu sistema operacional. Em seguida, volte aqui.

## Obtenha a Chave Pública

De volta à página de download, obtenha o arquivo de assinaturas de hash SHA256

![image](assets/6.webp)

Clique nele e salve o arquivo no disco, de preferência no diretório Downloads.

Este arquivo contém assinaturas de várias pessoas, do arquivo SHA256SUMS.

Queremos a chave pública do desenvolvedor principal, Wladimir J. van der Laan, em nosso chaveiro do computador. O ID da sua chave pública é:
1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964

Copie esse texto para o seguinte comando:

```
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```

Por curiosidade, a qualquer momento, você pode ver quais chaves estão no chaveiro do computador com este comando:

```
gpg --list-keys
```

## Verifique o download (parte 2)

Temos a chave pública, então agora podemos verificar o arquivo SHA256SUMS, que contém os hashes do download do Bitcoin Core, e a assinatura para esses hashes.

Abra o Terminal ou CMD novamente e certifique-se de estar no diretório Downloads. A partir daí, execute este comando:

```
gpg –verify SHA256SUMS.asc SHA256SUMS
```

O primeiro arquivo listado é a grafia exata do arquivo de assinatura. O segundo arquivo listado deve ser a grafia exata do arquivo de texto contendo os hashes. Ambos os arquivos devem estar no mesmo diretório e você precisa estar no diretório dos arquivos, caso contrário, você terá que digitar o caminho completo para cada arquivo.

Este é o resultado que você deve obter

![image](assets/7.webp)

É seguro ignorar a mensagem de AVISO - isso apenas lembra que você não encontrou Wladimir em uma parte importante e pessoalmente perguntou qual era a chave pública dele e, em seguida, disse ao seu computador para confiar completamente nessa chave.

Se você recebeu esta mensagem, agora sabe que o arquivo SHA256SUMS.asc não foi adulterado após a assinatura de Wladimir.

## Instale o Bitcoin Core

Você não deve precisar de instruções detalhadas sobre como instalar o programa.

![image](assets/8.webp)

## Execute o Bitcoin Core

Em um Mac, você pode receber um aviso (a Apple ainda é contra o Bitcoin)

![image](assets/9.webp)

Clique em OK e depois abra suas Preferências do Sistema

![image](assets/10.webp)

Clique no ícone Segurança e Privacidade:

![image](assets/11.webp)

Em seguida, clique em "abrir mesmo assim":

![image](assets/12.webp)

O erro aparecerá novamente, mas desta vez você terá um botão ABRIR disponível. Clique nele.

![image](assets/13.webp)

O Bitcoin Core deve carregar e você será apresentado a algumas opções:

![image](assets/14.webp)

Aqui você pode escolher usar o caminho padrão para onde o blockchain será baixado, ou você pode escolher sua unidade externa. Eu recomendo não alterar o caminho padrão se você for usar a unidade interna, pois facilita a configuração ao instalar outros softwares para se comunicar com o Bitcoin Core.

Você pode optar por executar um nó podado, o que economiza espaço, mas limita o que você pode fazer com seu nó. De qualquer forma, você estará baixando o blockchain inteiro e verificando-o de qualquer maneira, então, se tiver espaço, mantenha o que baixou e não faça poda se puder evitar.

Depois de confirmar, o blockchain começará a ser baixado. Isso levará vários dias.

![image](assets/15.webp)

Você pode desligar o computador e voltar para fazer o download se quiser, não causará nenhum dano.
