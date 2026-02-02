---
name: Specter DIY
description: Guia de configuração do Specter DIY
---

![cover](assets/cover.webp)


## Espectro-DIY


> Os Cypherpunks escrevem código. Sabemos que alguém tem de escrever software para defender a privacidade e, uma vez que não podemos ter privacidade se não o fizermos todos, vamos escrevê-lo.

*Manifesto de um Cypherpunk - Eric Hughes - 9 de março de 1993*


A ideia do projeto é construir um hardware wallet a partir de componentes prontos a usar.

Apesar de termos uma placa de extensão que coloca tudo num formato agradável e o ajuda a evitar qualquer soldadura, continuaremos a apoiar e a manter a compatibilidade com os componentes padrão.


![image](assets/fr/01.webp)


Também queremos manter o projeto flexível, de modo que ele possa funcionar em qualquer outro conjunto de componentes com mudanças mínimas. Talvez se queira fazer um hardware wallet numa arquitetura diferente (RISC-V?), com um modem áudio como canal de comunicação - deve ser possível fazê-lo. Deve ser fácil adicionar ou alterar a funcionalidade do Specter e tentamos abstrair os módulos lógicos tanto quanto possível.


Os códigos QR são uma forma predefinida de o Specter comunicar com o anfitrião. Os códigos QR são bastante práticos e permitem ao utilizador controlar a transmissão de dados - cada código QR tem uma capacidade muito limitada e a comunicação é unidirecional. Além disso, a comunicação é feita por via aérea - não é necessário ligar o wallet ao computador em nenhum momento.


Para o armazenamento de segredos, suportamos o modo agnóstico (o wallet esquece todos os segredos quando é desligado), o modo imprudente (armazena segredos na memória flash do microcontrolador da aplicação) e a integração do secure element está para breve.


Nosso foco principal é a configuração multisignature com outras carteiras de hardware, mas o wallet também pode funcionar como um único signatário. Tentamos torná-lo compatível com o Bitcoin Core sempre que possível - PSBT para transações não assinadas, descritores wallet para importar/exportar carteiras multisig. Para facilitar a comunicação com o Bitcoin Core também estamos a trabalhar no [Specter Desktop app](https://github.com/cryptoadvance/specter-desktop) - um pequeno servidor python flask que fala com o seu nó Bitcoin Core.


A maior parte do firmware é escrita em MicroPython, o que torna o código fácil de auditar e alterar. Usamos a biblioteca [secp256k1](https://github.com/bitcoin-core/secp256k1) do Bitcoin Core para cálculos de curvas elípticas e a biblioteca [LittlevGL](https://lvgl.io/) para GUI.


## Declaração de exoneração de responsabilidade


O projeto amadureceu significativamente, ao ponto de o nível de segurança do Specter-DIY ser agora comparável ao das carteiras de hardware comerciais no mercado. Implementámos um carregador de arranque seguro que verifica as actualizações de firmware, para que possa ter a certeza de que apenas o firmware assinado pode ser carregado no dispositivo após a configuração inicial. No entanto, ao contrário dos dispositivos de assinatura comerciais, o carregador de arranque tem de ser instalado manualmente pelo utilizador e não é definido na fábrica do fornecedor do dispositivo. Por isso, preste atenção extra durante a instalação inicial do firmware e certifique-se de que verificou as assinaturas PGP e de que faz o flash do firmware a partir de um computador seguro.


Se algo não funcionar, abra um problema aqui ou faça uma pergunta no nosso [grupo do Telegram](https://t.me/+VEinVSYkW5TUl5Ai).


## Lista de compras para o Specter-DIY


Aqui descrevemos o que comprar e, na próxima parte da montagem, explicamos como montá-la e algumas notas sobre a placa - jumpers de alimentação, portas USB, etc.


### Quadro de descoberta


A parte principal do dispositivo é a placa de desenvolvimento:



- Placa de desenvolvimento STM32F469I-DISCO (ou seja, de [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) ou [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Cabo mini**USB
- Cabo MicroUSB standard para comunicar através de USB


Facultativo mas recomendado:


- [Waveshare QR code scanner](https://www.waveshare.com/barcode-scanner-module.htm) com conectores de pinos longos como [estes](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) ou [estes](https://www.amazon.com/gp/product/B015KA0RRU/) para ligar o scanner à placa (são necessários 4 conectores de pinos).


Estamos atualmente a trabalhar numa placa de extensão que inclui uma ranhura para cartão inteligente, um leitor de código QR, uma bateria e uma caixa impressa em 3D, mas não inclui a parte principal - a placa de descoberta que tem de ser encomendada separadamente. Desta forma, o ataque à cadeia de abastecimento continua a não ser um problema, uma vez que os componentes críticos para a segurança são comprados numa loja de eletrónica aleatória.


Pode começar a utilizar o Specter mesmo sem quaisquer componentes adicionais, mas poderá comunicar com ele através de USB ou da ranhura para cartões SD incorporada. A utilização do Specter através de USB significa que não está ligado ao ar, pelo que perde uma importante propriedade de segurança.


### Leitor QR


Para o leitor de código QR, existem várias opções.


**Opção 1. Recomendado.** Scanner muito bom da Waveshare (40$)


[Waveshare scanner](https://www.waveshare.com/barcode-scanner-module.htm) - terá de encontrar uma forma de o montar corretamente, talvez utilizando algum tipo de protótipo Arduino e alguma fita adesiva.


Não é necessário soldar, mas se tiveres conhecimentos de soldadura podes tornar o wallet muito mais bonito ;)


**Opção 2: Um scanner muito bom da Mikroe, mas bastante caro (150$):


[Clique no código de barras](https://www.mikroe.com/barcode-click) + [Adaptador](https://www.mikroe.com/arduino-uno-click-shield)


**Opção 3: Qualquer outro scanner QR


É possível encontrar alguns scanners baratos na China. A sua qualidade nem sempre é muito boa, mas pode arriscar. Talvez até a ESPcamera sirva para o efeito. Só precisa de ligar a alimentação, a UART (pinos D0 e D1) e o gatilho ao D5.


**Opção 4.** Sem scanner.


Nesse caso, só pode utilizar o Specter com USB / cartão SD.


A menos que construa o seu próprio módulo de comunicação que utilize outra coisa em vez de códigos QR - audiomodem, bluetooth ou outra coisa qualquer. Assim que puder ser acionado e enviar os dados por série, pode fazer o que quiser.


### Componentes opcionais


Se adicionar um pequeno powerbank ou um carregador/booster de bateria e energia, o seu wallet torna-se completamente autónomo ;)



## Montagem do Specter-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### Ligar o leitor de códigos de barras Waveshare


O firmware do wallet configurará o scanner para si na primeira execução, pelo que não é necessária qualquer pré-configuração manual.


Eis como se liga o scanner à placa:


![image](assets/fr/02.webp)


Para maior comodidade, pode comprar uma proteção Arduino Protype e soldar e montar tudo nela (ou seja, [esta](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Gestão de energia


Na parte superior da placa, existe um jumper que define a fonte de alimentação. Pode mudar a posição do jumper e selecionar a fonte de alimentação para uma das portas USB ou para o pino VIN e ligar aí uma bateria externa (deve ser de 5V).


### Caixa para bricolage


Consulte a pasta [enclosures](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures).


### Seja criativo!


Monte o seu próprio Specter-DIY e envie-nos as imagens (faça um pull request ou entre em contacto connosco).


Vê a [Galeria](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) com Espectros reunidos pela comunidade!




## Instalar o código compilado


Com o carregador de arranque seguro, a instalação inicial do firmware é ligeiramente diferente. As actualizações são mais fáceis e não requerem a ligação do hardware wallet ao computador.


![video](https://youtu.be/eF4cgK_L6T4)


### Flashing do firmware inicial


**Nota** Se não quiser usar binários dos lançamentos veja a [documentação do bootloader](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md) que explica como compilar e configurar para usar as suas chaves públicas em vez das nossas.



- Se estiver a atualizar a partir de versões inferiores a `1.4.0` ou a carregar o firmware pela primeira vez, utilize o `initial_firmware_<version>.bin` da página [releases](https://github.com/cryptoadvance/specter-diy/releases).
 - Verificar a assinatura do ficheiro `sha256.signed.txt` em relação à [chave PGP do Stepan](https://stepansnigirev.com/ss-specter-release.asc)
 - Verifique o hash do arquivo `initial_firmware_<version>.bin` em relação ao hash armazenado no arquivo `sha256.signed.txt`
- Se estiver a atualizar a partir de um carregador de arranque vazio ou se vir a mensagem de erro do carregador de arranque a indicar que o firmware não é válido, consulte a secção seguinte - Flashing do firmware Specter assinado.
- Certifique-se de que o jumper de alimentação da sua placa de descoberta está na posição STLK
- Ligue a placa de descoberta ao seu computador através do cabo **miniUSB** na parte superior da placa.
    - A placa deve aparecer como um disco amovível com o nome `DIS_F469NI`.
- Copiar o ficheiro `initial_firmware_<version>.bin` para a raiz do sistema de ficheiros `DIS_F469NI`.
- Quando a placa terminar de fazer o flash do firmware, a placa irá reiniciar-se a si própria e reiniciar para o bootloader. O bootloader verificará o firmware e arrancará para o firmware principal. Se vir uma mensagem de erro a indicar que não foi encontrado firmware - siga as instruções de atualização e carregue o firmware através do cartão SD.
- Agora podes ligar o jumper de alimentação onde quiseres e alimentar a placa a partir do powerbank ou da bateria.


A atualização do firmware inicial através do copiar-colar do ficheiro `.bin` por vezes falha - frequentemente devido ao cabo, ou se ligar o dispositivo através de um hub USB. Neste caso, pode tentar mais algumas vezes (normalmente funciona em 2-3 tentativas).


Se estiver sempre a falhar, pode utilizar a ferramenta de código aberto [stlink](https://github.com/stlink-org/stlink/releases/latest). Instale-a e digite no seu terminal: `st-flash write <path/to/initial_firmare.bin> 0x8000000`. Normalmente funciona de forma muito mais fiável.


### Atualização do firmware



- Faça o download do `specter_upgrade_<version>.bin` a partir de [releases](https://github.com/cryptoadvance/specter-diy/releases).
- Copie este binário para a raiz do cartão SD (formatado em FAT, 32 GB no máximo)
 - Certifique-se de que apenas um arquivo `specter_upgrade***.bin` está no diretório raiz
- Insira o cartão SD na ranhura SD da placa de descoberta e ligue a placa
- O Bootloader irá atualizar o firmware e notificá-lo-á quando estiver concluído.
- Reinicie a placa - verá agora a interface Specter-DIY, que lhe sugerirá que selecione o seu código PIN


Sempre que uma nova versão é lançada, basta fazer o download do `specter_upgrade_<version>.bin` a partir das versões, colocá-lo no cartão SD e atualizar o dispositivo como no passo anterior. O Bootloader irá garantir que apenas firmware assinado possa ser carregado na placa.


### Como saber a versão do firmware


Aceda ao menu `Definições do dispositivo` - o número da versão será apresentado sob o título do ecrã.


## Utilizar o Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Segurança do Specter-DIY


### Hardware


O ecrã é controlado pela MCU da aplicação.


A integração de elementos seguros ainda não está concluída - atualmente, os segredos também são armazenados na MCU principal. Mas é possível utilizar o wallet sem armazenar o segredo - é necessário introduzir sempre a frase de recuperação. Porquê lembrar-se do longo passphrase se pode lembrar-se de toda a mnemónica?


O dispositivo utiliza flash externo para armazenar alguns ficheiros (QSPI), mas todos os ficheiros do utilizador são assinados pelo wallet e verificados quando carregados.


A funcionalidade de leitura de QR está num microcontrolador separado, pelo que todo o processamento da imagem é efectuado fora da MCU de segurança crítica. Atualmente, o USB e o cartão SD continuam a ser geridos pela MCU principal, pelo que não se deve utilizar o cartão SD e o USB se se quiser reduzir a superfície de ataque.


### Proteção por PIN (autenticação do utilizador)


Durante o primeiro arranque, é gerado um segredo único na MCU principal. Este segredo permite-lhe verificar se o dispositivo não foi substituído por um dispositivo malicioso - quando introduz o código PIN, vê uma lista de palavras que permanecerão inalteradas enquanto o segredo estiver presente.


O seu código PIN, juntamente com este segredo único, são utilizados para criar uma chave de desencriptação para as suas chaves Bitcoin (se as armazenar). Assim, se o atacante conseguir contornar o ecrã PIN, a desencriptação falhará na mesma.


Se tiveres bloqueado o firmware (TODO: adiciona aqui o link para as instruções), o segredo também será bloqueado, por isso, se o atacante colocar um firmware diferente na placa, o segredo é apagado e poderás reconhecê-lo quando começares a introduzir o código PIN - a sequência de palavras será diferente.


### Geração da frase de recuperação


Esta é uma das partes mais importantes do wallet - para generate a chave de forma segura. Para o fazer bem, utilizamos múltiplas fontes de entropia:



- TRNG do microcontrolador. Proprietário, certificado e provavelmente bom, mas não confiamos nele
- Ecrã tátil. Sempre que se toca no ecrã, medimos a posição e o momento em que o toque ocorreu (em ticks do microcontrolador a 180MHz).
- Microfones incorporados - ainda não. A placa tem dois microfones, pelo que o hardware wallet pode ouvi-lo e misturar esses dados com o pool de entropia.


Toda esta entropia é combinada em hash e convertida na sua frase de recuperação. A entropia resultante é sempre melhor do que qualquer uma das fontes individuais.


### Lógica de alto nível - carteiras


O Specter funciona como um armazenamento de chaves. Ele contém chaves privadas HD que podem ser envolvidas em carteiras. As carteiras são definidas pelos seus descritores. Também suportamos miniscriptos.


Cada wallet pertence a uma rede específica. Isto significa que, se importou um wallet na `testnet`, este não estará disponível na `mainnet` ou na `regtest` - terá de mudar para esta rede e importar o wallet separadamente.


### Verificação das transacções


As seguintes regras aplicam-se às transacções que o wallet assinará:



- se forem encontradas entradas mistas de carteiras diferentes, o utilizador é avisado ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- as saídas de alteração mostram o nome do wallet para o qual são enviadas
- para utilizar um multisig ou miniscript, é necessário importar o wallet adicionando o descritor wallet (por QR, USB ou cartão SD)


## Apoio aos descritores


Todos os descritores normais do Bitcoin funcionam. Para além disso, temos algumas extensões:


### Ramos múltiplos em descritores


Para poupar algum espaço nos códigos QR, permitimos adicionar descritores com várias ramificações de uma só vez. Se pretender utilizar `wpkh(xpub/0/*)` para endereços de receção e `wpkh(xpub/1/*)` para endereços de alteração, pode combiná-los num único descritor: `wpkh(xpub/{0,1}/*)` - o wallet tratará o primeiro índice da parte do conjunto `{}` como o ramo para endereços de receção e o segundo como endereços de alteração.


Também é possível especificar mais do que dois ramos, e os índices dos ramos podem ser diferentes para diferentes co-signatários, pelo que este descritor é muito estranho mas totalmente válido:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Aqui, para receber o endereço número 17, o wallet utilizará o script de `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))`.


O único requisito é que o número de índices em todos os conjuntos seja o mesmo (3 no caso acima).


### Derivações por defeito


Se o descritor contiver chaves públicas mestras mas não contiver derivações curinga, a derivação padrão `/{0,1}/*` será adicionada a todas as chaves estendidas no descritor. Se pelo menos um dos xpubs tiver uma derivação curinga, o descritor não será alterado.


O descritor `wpkh(xpub)` será convertido em `wpkh(xpub/{0,1}/*)`.


### Miniscript


O Specter suporta miniscript, mas não suporta compilação de política para miniscript (porque é muito caro). Nós realizamos algumas verificações no miniscript, então apenas scripts `B` são permitidos no nível superior e todos os argumentos em sub-miniscripts têm que ter propriedades de acordo com a [spec](http://bitcoin.sipa.be/miniscript/).


Pode utilizar [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) para generate um descritor de uma política e depois importá-lo para o wallet.


Por exemplo, uma apólice "Posso gastar agora, ou daqui a 100 dias a minha mulher pode gastar" pode ser convertida no wallet da seguinte forma:


Política: `ou(9@pk(xpubA),and(older(14400),pk(B)))` (a minha chave tem 9 vezes mais probabilidades)


Miniscript: `ou_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`


Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))`


Como aqui não temos nenhuma derivação curinga, as derivações padrão de `/{0,1}/*` serão anexadas aos xpubs.



---

Licença MIT


Direitos de autor (c) 2019 cryptoadvance


---