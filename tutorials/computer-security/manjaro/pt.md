---
name: Manjaro
description: Tornando o poder do Arch Linux mais acessível
---
![cover](assets/cover.webp)



O Arch Linux é um sistema operativo popular em muitos domínios, graças à sua robustez e estabilidade. No entanto, pode ser difícil para os utilizadores principiantes familiarizarem-se com ele. É precisamente para resolver este problema que o **Manjaro** foi criado: para oferecer o poder do Arch Linux, mas com uma experiência mais simples e acessível, baseada num Interface intuitivo e fácil de aprender.



## Começar a utilizar o Manjaro



Um dos maiores trunfos do Manjaro é o seu **sistema de atualização simples e eficiente**. Não precisa de as gerir manualmente: O Manjaro trata delas por si! Um ícone na área de notificação (a localização varia de acordo com a edição) alerta-o quando uma atualização está disponível. Tudo o que tem de fazer é seguir as instruções, e o processo é rápido e sem esforço.



O Manjaro também oferece um **vastíssimo catálogo de aplicações**. Uma vez que o Manjaro é baseado no Arch Linux, beneficia de acesso direto aos seus repositórios oficiais, ricos numa variedade de software, incluindo aplicações proprietárias. O Manjaro atrasa ligeiramente algumas actualizações do Arch Linux para testes adicionais; isto melhora a estabilidade à custa de um ligeiro atraso nas novas versões. E se esta escolha não for suficiente para si, também pode aceder ao **AUR (*Arch User Repository*)**, uma enorme biblioteca gerida pela comunidade. Se um programa não existir nos repositórios oficiais, é provável que esteja disponível no AUR.



Outra vantagem do Manjaro é o facto de ser **muito menos consumidor de recursos** do que sistemas como o Windows ou o macOS. Consome menos RAM e potência de computação, o que o torna uma escolha ideal para computadores mais antigos ou menos potentes: a sua máquina ganha em fluidez e velocidade, recuperando uma segunda juventude.



Para além de tudo isto, o Manjaro é **inteiramente gratuito**. Ao contrário do Windows ou do macOS, não tem de pagar nada para o instalar e tirar o máximo partido dele. Por fim, oferece uma **segurança reforçada** graças a actualizações regulares e rápidas, limitando a exposição a vulnerabilidades. A sua comunidade ativa também garante que quaisquer problemas sejam rapidamente corrigidos e que sejam propostas soluções eficazes.



## Descobrir o Manjaro OS



Antes de começar a instalar o Manjaro, é importante saber que esta distribuição está disponível em várias edições. Cada uma destas edições oferece um ambiente de trabalho único que influencia tanto o seu fluxo de trabalho como o consumo de recursos do sistema. Existem três edições oficiais principais do Manjaro.



![0_01](assets/fr/01.webp)





- A edição **KDE Plasma** é a mais personalizável. Se está à procura de um sistema visualmente elegante e de alto desempenho, o KDE Plasma é uma excelente escolha. Este ambiente de trabalho estável é ideal para utilizadores que pretendem um controlo total e uma experiência personalizada.





- Para máquinas com recursos mais limitados, a edição **Xfce** é a solução ideal. O seu Interface é leve e intuitivo, garantindo um funcionamento suave mesmo em computadores mais antigos. Além disso, o seu layout faz lembrar o Windows, tornando a transição para o Linux mais fácil para os novos utilizadores.





- Finalmente, a edição **GNOME** oferece uma abordagem totalmente diferente. O seu design simplificado dá ênfase à produtividade e organização através de espaços de trabalho virtuais. Este fluxo de trabalho centrado em actividades é particularmente apelativo para utilizadores já familiarizados com o Linux e que procuram um ambiente minimalista e altamente eficiente.



### Outras edições do Manjaro



![0_02](assets/fr/02.webp)



Para além das edições oficiais, a comunidade Manjaro também oferece outras versões. Estas edições alternativas foram concebidas para satisfazer necessidades específicas e oferecem uma variedade de ambientes de trabalho.



A edição **Cinnamon** é uma excelente escolha se estiver a começar e estiver à procura de um Interface familiar. Foi concebido para ser fácil de utilizar, mantendo as convenções clássicas dos ambientes de escritório tradicionais.



Para os utilizadores mais avançados, existem edições como o **i3 Window Manager** ou o **Sway**. Muito mais leves e rápidos, requerem, no entanto, um bom domínio da linha de comandos para serem totalmente configurados e explorados. Estes ambientes são ideais para aqueles que pretendem um controlo total sobre o seu sistema e que colocam a eficiência acima de tudo.



## Requisitos técnicos



Para que o Manjaro funcione da melhor forma, o seu computador deve cumprir alguns requisitos mínimos. Recomendamos que tenha pelo menos o :





- Um processador de 64 bits (x86_64)
- **4 GB de RAM recomendados (mínimo de 2 GB)** (ver abaixo)
- 30 GB de espaço em disco (mais se criar uma partição `/home` dedicada)



## Instalação do Manjaro



Para descarregar, vá ao [sítio Web oficial do Manjaro](https://manjaro.org/) e escolha a edição que melhor se adapta às suas necessidades. Depois de ter descarregado o ficheiro, terá de criar uma chave USB de arranque com a imagem ISO do Manjaro.



Depois, vá ao sítio Web do software [Rufus](https://rufus.ie/fr/) e descarregue-o. Execute o programa, ligue a sua chave USB, selecione a imagem ISO do Manjaro e comece a flashear. Aguarde que o processo termine antes de remover a chave. Pode então reiniciar o seu computador.



![0_03](assets/fr/03.webp)



Para instalar o Manjaro no seu computador, primeiro desligue-o completamente. Depois ligue a chave USB, volte a ligar a máquina e aceda ao menu de arranque ou ao firmware UEFI/BIOS premindo **F2, F10, F12, Escape** ou **Delete** (dependendo do fabricante).



Em seguida, escolha a chave USB como dispositivo de arranque para iniciar o processo de instalação do SO.



### Ecrã de arranque



A primeira vez que iniciar o Manjaro a partir da chave USB, será levado diretamente para o menu de instalação. Antes de iniciar a instalação, pode alterar a disposição do teclado ou o idioma do sistema.



Depois selecione a opção **Boot with open source drivers** para iniciar a instalação do Manjaro. Estes controladores de código aberto são compatíveis com a maioria do hardware e serão suficientes na maioria dos casos. Se tem uma placa gráfica NVIDIA, por exemplo, ou necessita de um desempenho gráfico superior, pode escolher **Boot with proprietary drivers**, que utiliza drivers proprietários.



![0_04](assets/fr/04.webp)



O sistema será iniciado no **modo live predefinido**. Isto permite-lhe testar a funcionalidade do Manjaro para ver se se adequa às suas necessidades antes de o instalar permanentemente. Quando estiver pronto, clique na opção **Instalar o Manjaro Linux**.



Selecione o idioma pretendido para a sua instalação e clique em **Próximo**.



![0_06](assets/fr/06.webp)



Em seguida, escolha a sua localização para definir o fuso horário correto. Nesta fase, também pode alterar o idioma e o formato da data.



![0_07](assets/fr/07.webp)



Selecionar a disposição do teclado. Está disponível um campo de teste para verificar se as teclas digitadas correspondem aos caracteres esperados.



![0_08](assets/fr/08.webp)



### Particionamento de disco


Existem duas opções para particionar o disco.





- A primeira, e mais simples, é apagar todo o disco e instalar o Manjaro nele.
- O segundo permite **particionamento manual**.



![0_09](assets/fr/09.webp)



Para uma instalação limpa, recomendamos a criação de pelo menos três partições:





- Uma primeira partição de **516 MB** (primária) para o **boot**.
- Uma segunda partição **2 GB** (lógica) para **swap**.
- Uma terceira partição para os seus **dados pessoais**.



Se desejar instalar outro sistema em paralelo, tem de dividir esta última partição e atribuir apenas uma parte ao Manjaro (pelo menos **15 GB** para garantir o funcionamento correto do sistema).


### Criar uma conta de utilizador



Criar uma conta de utilizador no sistema, preenchendo as informações necessárias. Finalmente, defina a palavra-passe do administrador (**root**). Este administrador é um **super-utilizador** com todos os direitos sobre o sistema e a capacidade de executar comandos avançados.



![0_10](assets/fr/10.webp)



### Escolha a suite de escritório correta



O Manjaro permite-lhe escolher entre o **FreeOffice** e o **LibreOffice**.





- O **LibreOffice** é mais completo, com uma gama mais vasta de software e funcionalidades avançadas.
- O **FreeOffice**, por outro lado, é mais leve e inclui apenas o essencial: **TextMaker**, **PlanMaker** e **Presentations**.



![0_11](assets/fr/11.webp)



### Resumo da configuração



Um ecrã de resumo mostra-lhe todos os parâmetros que definiu. Pode voltar atrás para fazer alterações, se necessário, sem afetar outras definições que já tenha efectuado.



Em seguida, clique em **Instalar** e confirme para iniciar a instalação efectiva.



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



### Fim da instalação



No final do processo, marque a caixa **Restart now**, depois clique em **Done**. O sistema será reiniciado e o **Manjaro estará pronto a ser utilizado**.



![0_13](assets/fr/14.webp)



## Primeiros passos com o Manjaro



A instalação do Manjaro é apenas o primeiro passo. Para tirar o máximo proveito do seu sistema, aqui estão algumas coisas úteis para saber.



### Atualizar o sistema



O Manjaro simplifica muito as actualizações. Para atualizar os seus pacotes :



```shell
sudo pacman -Syu
```



Este comando descarrega e instala as versões mais recentes disponíveis. Recomendamos que o execute regularmente para manter o seu sistema **seguro e estável**.



### Configuração de um ambiente de desenvolvimento



Para desenvolver aplicações Web no Manjaro, instale as ferramentas essenciais com um único comando:



```shell
sudo pacman -S nodejs npm git yarn
```



Este comando instala o Node.js e o npm para executar e gerir os seus projectos JavaScript e TypeScript, o Git para gestão de versões e o Yarn como um gestor de pacotes alternativo.



### Instalação de um Bitcoin Wallet



Para gerir os seus bitcoins no Manjaro, pode instalar o **Electrum**, um Wallet leve e seguro:



```shell
sudo pacman -S electrum  # Install Electrum
```



Electrum permite-lhe **receber e enviar bitcoins** com facilidade, ao mesmo tempo que oferece funcionalidades avançadas como a gestão de múltiplos Wallet e a proteção passphrase. Para um guia completo de utilização da Electrum, consulte o nosso tutorial dedicado que explica como criar um Wallet, proteger os seus fundos e efetuar transacções.



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

## Proteger o seu sistema Manjaro



A segurança é um aspeto crucial de qualquer instalação Linux. É importante para si proteger a confidencialidade e a integridade dos seus dados.



### Configuração da firewall



O Manjaro inclui o UFW (*Uncomplicated Firewall*), um programa para gerir firewalls de filtros de rede, mas tem de o ativar manualmente:



```bash
# Installation if not present
sudo pacman -S ufw

# Firewall activation
sudo systemctl enable ufw.enable

sudo ufw enable

# Allow SSH connections (optional)
sudo ufw allow ssh

# Check the status
sudo ufw status verbose
```



![verbose](assets/fr/15.webp)



### Gerir as permissões dos utilizadores



1. **Criar um utilizador não privilegiado**



```shell
sudo useradd -m username
sudo passwd username
```



2. **Configuração do ficheiro sudoers**



```shell
sudo EDITOR=nano visudo
```



Agora está pronto para utilizar o Manjaro Linux na sua máquina. Graças à sua **instalação simples**, **atualizações fáceis** e **flexibilidade**, terá um sistema potente e de elevado desempenho, adequado para o desenvolvimento, a utilização diária e a gestão dos seus bitcoins com ferramentas como Electrum.



O Manjaro combina **estabilidade, velocidade e segurança**, mantendo-se **inteiramente livre**, o que o torna uma escolha ideal tanto para principiantes como para utilizadores avançados. Aproveite o tempo para explorar as suas várias funcionalidades e personalizar o seu ambiente de acordo com as suas necessidades. Se desejar obter mais conhecimentos e descobrir o sistema Arch Linux, o nosso tutorial é altamente recomendado.



https://planb.academy/tutorials/computer-security/operating-system/arch-linux-7a3dc8a8-629b-4971-bb0d-4eab94f93973