---
name: Bacca
description: Configuração de um ledger sem o software Ledger Live
---
![cover](assets/cover.webp)

Se utiliza um Ledger, provavelmente já descobriu que tem de passar pelo software Ledger Live, pelo menos para a configuração inicial do dispositivo, para verificar a sua autenticidade e instalar a aplicação Bitcoin no mesmo. No entanto, após esta configuração, muitos bitcoiners preferem utilizar um software especializado de gestão de carteiras Bitcoin, como o Sparrow ou o Liana, em vez do Ledger Live. Embora a Ledger produza excelentes carteiras de hardware que incluem rapidamente os últimos recursos do Bitcoin, seu software não é necessariamente adaptado às necessidades específicas dos bitcoiners. De facto, o Ledger Live inclui muitas funcionalidades concebidas para altcoins, enquanto as opções dedicadas à gestão de carteiras Bitcoin são limitadas. Mas o problema do Sparrow e do Liana (de momento) é que não permitem instalar a aplicação Bitcoin no Ledger.

Para contornar a necessidade de utilizar o Ledger Live durante a configuração inicial do seu Ledger, pode utilizar a ferramenta Bacca, (ou "Ledger Installer"). Este software permite-lhe instalar e atualizar a aplicação Bitcoin, verificar a autenticidade do seu Ledger e até atualizar posteriormente o firmware do dispositivo. Bacca foi criado por Antoine Poinsot (Darosior), desenvolvedor do Bitcoin Core no Chaincode Labs, cofundador [de Revault e Liana] (https://wizardsardine.com/), e Pythcoiner.

Neste tutorial, vou mostrar-lhe como utilizar esta ferramenta, para que possa prescindir definitivamente do software Ledger Live e continuar a desfrutar dos dispositivos Ledger. Funciona em todos os dispositivos: Nano S Classic, Nano S Plus, Nano X, Flex e Stax.

---
*Tenha em atenção que esta ferramenta é bastante recente e os seus criadores especificam que ainda se encontra **em fase de teste**. Recomendam a sua utilização apenas para fins de teste, e não para um dispositivo destinado a alojar uma carteira Bitcoin real, embora seja possível fazê-lo. A este respeito, recomendo que siga as recomendações dos criadores desta ferramenta, que estão especificadas [no README do seu repositório GitHub] (https://github.com/darosior/ledger_installer).*

---
## Pré-requisitos

No seu computador, precisará de duas ferramentas para utilizar o Bacca:


- Git ;
- Ferrugem.

Se já os tiver instalado, pode saltar este passo.

**Linux:**

Numa distribuição Linux, o Git é geralmente pré-instalado. Para verificar se o Git está instalado no seu sistema, pode escrever o seguinte comando no terminal :

```bash
git --version
```

Se não tiver o Git instalado no seu sistema, aqui está o comando para o instalar num sistema Debian :

```bash
sudo apt install git
```

Finalmente, para instalar o seu ambiente de desenvolvimento Rust, utilize o comando :

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**Windows:**

Para instalar o Git, vá para [o sítio Web oficial do projeto] (https://git-scm.com/). Descarregue o software e siga as instruções de instalação.

![BACCA](assets/fr/01.webp)

Proceda da mesma forma para instalar o Rust a partir do [sítio Web oficial] (https://www.rust-lang.org/tools/install).

![BACCA](assets/fr/02.webp)

**MacOS:**

Se o Git ainda não estiver instalado no seu sistema, abra um terminal e execute o seguinte comando para o instalar:

```bash
git --version
```

Se o Git não estiver instalado no seu sistema, será aberta uma janela que lhe oferece a instalação do Xcode, que inclui o Git. Basta seguir as instruções no ecrã para prosseguir com a instalação.

Para instalar o Rust, execute o seguinte comando:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## Instalação do Bacca

Abra um terminal e vá para a pasta onde pretende guardar o software, depois execute o seguinte comando:

```bash
git clone https://github.com/darosior/ledger_installer.git
```

Navegar para o diretório do software:

```bash
cd ledger_installer
```

Em seguida, use o Cargo para compilar o projeto e executar a GUI do Bacca:

```bash
cargo run -p ledger_manager_gui
```

Tem agora acesso à interface do software.

![BACCA](assets/fr/03.webp)

## Configurar o Ledger

Antes de começar, se o seu Ledger for novo, certifique-se de que configurou o código PIN e guardou a frase de recuperação. Não precisa do Ledger Live para estes passos iniciais. Basta ligar o Ledger através do cabo USB para o alimentar. Se não tiver a certeza de como proceder com estes dois passos, pode consultar o início do tutorial específico para o seu modelo:

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Utilização de Bacca

Ligue o seu Ledger ao computador e desbloqueie-o utilizando o código PIN que definiu. O Bacca deve detetar automaticamente o seu Ledger.

![BACCA](assets/fr/04.webp)

Para confirmar a autenticidade do seu Ledger, clique no botão "*Verificar*". Terá de autorizar a ligação no seu dispositivo Ledger para continuar.

![BACCA](assets/fr/05.webp)

O Bacca informará se o seu Ledger é genuíno. Se não for, isso indica que o dispositivo foi comprometido ou que é uma falsificação. Nesse caso, pare de usá-lo imediatamente.

![BACCA](assets/fr/06.webp)

No menu "*Apps*", pode consultar a lista de aplicações já instaladas no seu Ledger.

![BACCA](assets/fr/07.webp)

Para instalar a aplicação Bitcoin, clique em "*Instalar*" e, em seguida, autorize a instalação no seu Ledger.

![BACCA](assets/fr/08.webp)

A aplicação está bem instalada.

![BACCA](assets/fr/09.webp)

Caso não tenha a versão mais recente do aplicativo Bitcoin instalada, o Bacca exibirá um botão "*Update*" em vez da indicação "*Latest*". Basta clicar nesse botão para atualizar o aplicativo.

![BACCA](assets/fr/10.webp)

Agora que o seu Ledger está corretamente configurado com a versão mais recente da aplicação Bitcoin, está pronto para importar e utilizar a sua carteira em software de gestão como o Sparrow ou o Liana, sem ter de passar pelo Ledger Live!

Se achou este tutorial útil, agradecia que deixasse um polegar verde abaixo. Sinta-se à vontade para partilhar este artigo nas suas redes sociais. Muito obrigado!

Também recomendo que dê uma vista de olhos neste tutorial sobre GnuPG, que explica como verificar a integridade e autenticidade do seu software antes de o instalar. Esta é uma prática importante, especialmente quando se instala software de gestão de portefólio como o Liana ou o Sparrow :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

