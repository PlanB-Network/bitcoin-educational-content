---
name: pfSense
description: Instalando o Pfsense
---
![cover](assets/cover.webp)



___



*Este tutorial é baseado no conteúdo original de Florian BURNEL publicado em [IT-Connect](https://www.it-connect.fr/). Licença [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Foram efectuadas alterações importantes ao texto original do autor para atualizar o tutorial.*



___



![Image](assets/fr/027.webp)



## I. Apresentação



o pfSense é um sistema operativo gratuito e de código aberto que transforma qualquer computador, servidor dedicado ou dispositivo de hardware num router e firewall de alto desempenho e altamente configurável. Baseado no FreeBSD e conhecido pela sua arquitetura de rede estável e robusta, o pfSense tem vindo a definir o padrão para firewalls de código aberto para empresas, autoridades locais e utilizadores domésticos exigentes há mais de quinze anos.



As suas principais funções evoluíram consideravelmente ao longo dos anos e foram melhoradas a cada nova versão. Até à data, o pfSense oferece:





- Administração completa e centralizada através de um moderno, intuitivo e seguro Interface web Interface.
- Firewall stateful de alto desempenho com suporte avançado a NAT (incluindo NAT-T) e gerenciamento granular de regras.
- Suporte multi-WAN nativo, permitindo a agregação ou redundância de ligações à Internet.
- Servidor e retransmissão DHCP integrados.
- Alta disponibilidade graças ao protocolo CARP para failover e a possibilidade de configurar clusters pfSense.
- Balanceamento de carga entre várias ligações ou servidores.
- Suporte VPN completo: IPsec, OpenVPN e WireGuard (substituindo o L2TP, atualmente obsoleto).
- Portal cativo configurável para controlo do acesso dos hóspedes, especialmente em ambientes públicos ou hoteleiros.



o pfSense também possui um sistema de pacotes extensível que facilita a adição de recursos avançados, como um proxy transparente (Squid), filtragem de URL ou IDS/IPS (Snort ou Suricata) diretamente da web do Interface.



o pfSense é distribuído apenas para plataformas de 64 bits, de acordo com as recomendações atuais do FreeBSD. Ele pode ser instalado em hardware padrão (PCs, servidores rack) ou em plataformas embarcadas de baixo consumo de energia, como appliances Netgate ou certas caixas x86 de baixo perfil, que são muito mais poderosas do que as antigas caixas Alix.



Finalmente, vale a pena lembrar que o pfSense requer pelo menos duas interfaces de rede físicas: uma dedicada à zona externa (WAN) e uma dedicada à rede interna (LAN). Dependendo da complexidade de sua infraestrutura (DMZ, VLAN, várias WANs), várias interfaces adicionais podem ser necessárias para aproveitar todos os seus recursos.



## II. Descarregar imagem



A última versão estável do pfSense, no momento da redação deste tutorial, é a 2.8 (lançada em junho de 2025). Pode descarregar a imagem ISO ou o ficheiro de instalação adaptado ao seu ambiente de hardware diretamente do sítio Web oficial:





- [Descarregar pfSense] (https://www.pfsense.org/download/)



O portal de descarregamento permite-lhe selecionar:





- Arquitetura (geralmente **AMD64** para todo o hardware moderno).
- Tipo de imagem (**Installer USB Memstick** para instalação através de pen USB, **ISO Installer** para gravação ou edição virtual).
- O espelho de transferência mais próximo, para otimizar a velocidade de transferência.



Para aqueles que desejam implementar o pfSense em um ambiente virtualizado (Proxmox, VMware ESXi, VirtualBox...), uma imagem **OVA** também está disponível. Essa máquina virtual pronta para uso simplifica muito a instalação e a configuração inicial. Certifique-se apenas de que ajusta os recursos atribuídos (CPU, RAM, interfaces de rede) de acordo com a carga esperada e a sua topologia de rede.



Antes da instalação, recomendamos que verifique a integridade do ficheiro transferido, verificando o **SHA256** fornecido na página oficial de transferência. Isto garante que a imagem não foi alterada ou corrompida.



## III. Instalação



Neste exemplo, a instalação é efectuada numa máquina virtual com o VirtualBox. O procedimento permanece estritamente idêntico numa máquina física ou em qualquer outro hipervisor, exceto no que diz respeito à gestão de dispositivos virtuais.



### 1. Requisitos mínimos de hardware



Para uma implantação padrão, recomendamos o:





- 1 GB de RAM** no mínimo (recomenda-se 2 GB ou mais para permitir pacotes adicionais ou suporte a ZFS).
- 8 GB de espaço em disco** (20 GB ou mais é preferível para configurações mais avançadas, especialmente se estiver a instalar uma cache de proxy, IDS/IPS ou registos detalhados).
- Pelo menos duas interfaces de rede virtuais** (uma para a WAN e outra para a LAN). No VirtualBox, adicione-as às configurações da VM antes da inicialização.



### 2. Arranque do instalador



Monte a imagem ISO descarregada como uma unidade ótica virtual no VirtualBox ou insira a chave USB se estiver a instalar numa máquina física. No arranque, aparece um menu de arranque:



Se não selecionar nenhuma opção, o pfSense arrancará automaticamente com as opções predefinidas após alguns segundos. Prima a tecla "**Enter**" para iniciar o arranque normal.



![Image](assets/fr/027.webp)



Quando aparecer o menu principal, prima rapidamente o botão "**I**" para iniciar a instalação.



![Image](assets/fr/001.webp)



### 3. Definições iniciais do instalador



O primeiro ecrã permite-lhe definir alguns parâmetros regionais, como o tipo de letra do ecrã e a codificação dos caracteres. Estas definições são úteis em casos específicos (teclados não normalizados, ecrãs de série, línguas orientais). Para a maioria das instalações, mantenha os valores predefinidos e selecione "**Aceitar estas definições**".



![Image](assets/fr/002.webp)



### 4. Escolha do modo de instalação



Selecione "**Quick/Easy Install**" para executar uma instalação automática com as opções recomendadas. Este método elimina o disco selecionado e configura o pfSense com o particionamento predefinido.



![Image](assets/fr/003.webp)



Aparece um aviso que indica que todos os dados do disco serão apagados. Confirmar com "**OK**".



O instalador copia então os ficheiros necessários para o disco. Dependendo do seu hardware, isto pode demorar alguns segundos a alguns minutos.



### 5. Seleção do núcleo



Quando o instalador lhe pedir para escolher o tipo de kernel, deixe "**Standard Kernel**" selecionado. Este kernel genérico é perfeitamente adequado para implementações padrão, seja num PC, servidor ou VM.



### 6. Fim da instalação e reinício



Quando a instalação estiver concluída, selecione "**Reboot**" para reiniciar a sua máquina na sua nova instância pfSense.



**Nota importante**: remova a imagem ISO ou desligue a chave USB de instalação antes de reiniciar, para evitar reiniciar o programa de instalação na próxima vez que arrancar.



## IV. Iniciar o pfSense pela primeira vez



Na primeira inicialização, o pfSense deve ser configurado para reconhecer e atribuir corretamente suas interfaces de rede (WAN, LAN, DMZ, VLANs, etc.). A identificação cuidadosa das placas de rede é essencial para evitar quaisquer erros de configuração que possam privá-lo do acesso à web do Interface ou tornar seu firewall inoperante.



Ao ser iniciado, o pfSense detecta e lista automaticamente todas as interfaces de rede disponíveis, indicando o MAC Address para cada uma. Isso facilita a distinção entre elas.



### 1. VLANs



A primeira pergunta diz respeito à configuração de VLANs. Nesta fase, para uma configuração básica, não vamos ativar quaisquer VLANs. Por isso, prima a tecla "**N**" para saltar esta etapa.



![Image](assets/fr/004.webp)



### 2. WAN e LAN Interface Assignment



o pfSense então pede para definir qual Interface será usado para WAN (acesso à Internet). É possível escolher entre:





- Introduza o nome do Interface manualmente (recomendado para ambientes virtuais).
- Utilizar a deteção automática premindo "**A**". Esta opção é útil num anfitrião físico, desde que os cabos de rede estejam ligados e as ligações estejam activas.



![Image](assets/fr/005.webp)



Neste exemplo, configuramos manualmente a WAN. Digite o nome exato do Interface. Para uma placa Intel, o nome geralmente será "**em0**" no FreeBSD, mas pode variar dependendo do hardware. Por exemplo, uma placa Realtek geralmente será exibida como "**re0**".



![Image](assets/fr/006.webp)



Repetir a mesma operação para definir a LAN Interface. Aqui, utilizamos "**em1**".



o pfSense confirma que a LAN Interface ativa o firewall e o NAT para proteger sua rede interna e gerenciar a tradução do Address.



Se tiver outras interfaces físicas, pode configurar interfaces adicionais (DMZ, Wi-Fi, VLANs específicas) nesta fase. Cada Interface lógico requer uma placa de rede correspondente ou um Interface virtual. Para a configuração inicial, limitar-nos-emos à WAN e à LAN.



Uma vez que as atribuições tenham sido completadas, o pfSense exibe um resumo claro das correspondências entre interfaces físicas e funções atribuídas. Confirmar com "**Y**".



### 3. Consola PfSense



Quando esta etapa é concluída, o menu principal do console pfSense é exibido. Ele oferece várias opções úteis para administração direta, como redefinir a senha web, reinicializar, recarregar a configuração ou reatribuir interfaces.



![Image](assets/fr/007.webp)



Você também verá um resumo das configurações de rede atuais, incluindo o IP padrão do Interface LAN Address, geralmente **192.168.1.1**. Este é o Address que terá de introduzir no seu browser para aceder à web de administração do Interface.



**Nota**: Se a sua rede interna utilizar uma gama Address diferente, selecione "**2)** Set Interface(s) IP Address" no menu para atribuir um IP Address adequado ao seu ambiente.



Por padrão, se a WAN do Interface estiver conectada a uma caixa ou modem configurado com DHCP, o pfSense recuperará automaticamente um IP público Address. Assim, deve beneficiar de acesso imediato à Internet ao ligar um cliente à LAN do pfSense Interface.



## V. Primeiro acesso à Web da Interface



Uma vez que a inicialização tenha sido concluída e as interfaces de rede configuradas, é possível acessar o Interface web do pfSense para finalizar e ajustar a configuração.



### 1. Ligação inicial



Conecte um computador à porta LAN (ou à LAN virtual Interface em seu hipervisor) e atribua a ele um IP Address no mesmo intervalo, se necessário (por padrão, o pfSense distribui automaticamente um Address via DHCP na LAN).



No seu navegador, vá para o Address indicado pelo console (por padrão `https://192.168.1.1`). Observe que o pfSense requer HTTPS mesmo para a primeira conexão - portanto, espere um aviso de certificado autoassinado, que pode ser ignorado adicionando uma exceção.



É apresentado o ecrã de início de sessão. As credenciais predefinidas são:




- Nome do utilizador:** `admin`
- Palavra-passe:** `pfsense`



Estes identificadores serão modificados durante o assistente de configuração inicial.



## VI. Assistente de configuração



Na primeira ligação, o pfSense pede-lhe para seguir o seu **Assistente de Configuração**. Recomendamos vivamente que o utilize para garantir que todos os parâmetros essenciais estão corretamente definidos.



### 1. Parâmetros gerais



Pode:




- Especifique um nome de anfitrião e um domínio local (exemplo: `pfsense` e `lan.local`).
- Defina os servidores DNS e escolha se o pfSense deve usar o DNS do seu ISP ou um serviço externo (Cloudflare, OpenDNS, Quad9...).



### 2. Fuso horário



Indique o fuso horário do seu sítio para que os registos e os horários sejam consistentes (por exemplo, `Europa/Paris`).



### 3. Configuração da WAN



Configurar a ligação WAN:




- A predefinição é **DHCP** (suficiente se estiver atrás de uma caixa).
- Se tiver um IP fixo, introduza os parâmetros (IP estático, máscara, gateway, DNS) manualmente.
- Se necessário, defina uma VLAN ou autenticação PPPoE (comum em alguns ISPs).



### 4. Configuração da LAN



O assistente sugere a alteração da sub-rede LAN predefinida. Se tiver um plano de endereçamento específico, é a altura certa para o adaptar.



### 5. Alterar a palavra-passe do administrador



Proteja seu pfSense definindo imediatamente uma senha forte para o usuário `admin`.



## VII. Verificação e actualizações



Antes de implementar a firewall, certifique-se de que tem a versão mais recente do:





- Aceda a **Sistema > Atualizar**.
- Selecione o canal de atualização (normalmente **Estável**).
- Verificar se existem actualizações e aplicá-las.



É uma boa ideia ativar as notificações de atualização para o manter informado sobre os patches de segurança.



## VIII. Guardar a configuração



Antes de efetuar quaisquer alterações importantes, implemente uma política de cópias de segurança:





- Aceda a **Diagnóstico > Cópia de segurança e restauro**.
- Descarrega uma cópia da configuração atual (`config.xml`).
- Guarde-o num local seguro (suporte externo encriptado).



Para ambientes de missão crítica, considere a possibilidade de efetuar uma cópia de segurança automática da configuração num servidor externo ou através de um script programado.



## IX. Melhores práticas após a instalação



Para terminar o seu destacamento com paz de espírito:





- Modificar regras de firewall**: por padrão, o pfSense permite todo o tráfego de saída na LAN e bloqueia o tráfego de entrada na WAN. Ajuste essas regras conforme necessário.
- Configurar o acesso remoto seguro**: se necessário, permitir o acesso à Web do Interface a partir da WAN apenas através de VPN ou com restrições de IP.
- Ativar notificações**: configurar um servidor SMTP para receber alertas (falhas, actualizações, erros).
- Instalar extensões úteis**: por exemplo, IDS/IPS (Snort, Suricata), proxy (Squid), filtragem de DNS (pfBlockerNG).



Seu firewall pfSense está agora em funcionamento, pronto para proteger sua rede. Graças à sua flexibilidade e comunidade ativa, tem uma ferramenta poderosa e escalável que pode adaptar-se às suas necessidades futuras (multi-WAN, VLAN, VPN site a site, portal cativo, etc.).



Consulte a documentação oficial ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) regularmente para descobrir novas funcionalidades e certificar-se de que a sua configuração está actualizada e segura.