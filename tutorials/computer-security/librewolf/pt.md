---
name: LibreWolf
description: Como utilizar o navegador de privacidade LibreWolf
---

![cover](assets/cover.webp)



Cada clique, cada pesquisa, cada sítio visitado: o seu navegador Web tornou-se um sofisticado informador que alimenta um sistema de vigilância comercial global. O Google Chrome, utilizado por mais de 3 mil milhões de pessoas, transforma a sua navegação diária em dados lucrativos para os gigantes da publicidade. Até o Firefox, apesar da sua reputação de navegador "ético", ativa por defeito mecanismos de telemetria que transmitem os seus hábitos de navegação à Mozilla.



Esta realidade levanta uma questão essencial: será que ainda é possível navegar livremente na Internet sem ser constantemente espiado e perfilado? Felizmente, a resposta é afirmativa, graças a projectos comunitários que colocam o utilizador no centro das suas preocupações.



O LibreWolf encarna esta filosofia de resistência digital. A ideia de uma comunidade de programadores independentes, este navegador transforma o Firefox num verdadeiro escudo contra a vigilância online. Enquanto os browsers comerciais procuram rentabilizar a sua atenção, o LibreWolf faz o oposto: torna-o invisível para os trackers, preservando uma experiência de navegação fluida e moderna.



Neste tutorial, vamos descobrir como o LibreWolf pode transformar a maneira como você navega na web, oferecendo proteção robusta contra rastreamento sem sacrificar o desempenho ou a compatibilidade com a web.



![LIBREWOLF](assets/fr/01.webp)


*Quota de mercado dos navegadores Web: O Chrome domina com 65% do mercado, seguido do Safari e do Edge. Este domínio levanta questões sobre a diversidade da Web e a privacidade*



## Apresentação do LibreWolf



**O FreeWolf** é um navegador Web de código aberto derivado do Mozilla Firefox, desenvolvido e mantido por uma comunidade independente de entusiastas de software livre. O seu principal objetivo é oferecer uma navegação centrada na privacidade, segurança e liberdade do utilizador.



Em termos concretos, o LibreWolf utiliza o motor Gecko do Firefox, mas com uma filosofia radicalmente diferente: enquanto o Firefox tem de equilibrar a privacidade e a facilidade de utilização, o LibreWolf opta pela privacidade por defeito. O projeto elimina tudo o que possa violar a sua privacidade (telemetria, recolha de dados, módulos patrocinados), integrando simultaneamente definições de segurança melhoradas.



### Objectivos: privacidade e liberdade



O LibreWolf visa maximizar a proteção contra o rastreio e a recolha de impressões digitais, reforçando simultaneamente a segurança do navegador. Os seus principais objectivos incluem:





- Eliminar toda a telemetria e recolha de dados** no Firefox
- Desativar funções que vão contra a liberdade do utilizador**, tais como módulos DRM proprietários
- Aplicar definições de privacidade/segurança** e correcções específicas desde o início
- O desenvolvimento comunitário garante a transparência e a independência** dos interesses comerciais



Resumindo, o LibreWolf apresenta-se como "o Firefox como teria sido se a privacidade fosse a principal prioridade" - um navegador que o respeita por defeito, sem necessidade de qualquer configuração adicional.



### Principais caraterísticas



Desde o início, o LibreWolf oferece uma série de recursos orientados para a privacidade:



**Sem telemetria ou coleta de dados:** Ao contrário do Chrome ou Firefox, que enviam certas estatísticas de uso, o LibreWolf não coleta absolutamente nada da sua navegação. Sem relatórios de falhas, sem estudos de utilizadores, sem sugestões patrocinadas.



**O LibreWolf integra nativamente a extensão uBlock Origin, um dos melhores bloqueadores de anúncios e rastreadores do mercado. Por padrão, o LibreWolf filtra agressivamente qualquer coisa que possa rastreá-lo online (anúncios intrusivos, scripts de rastreamento, criptomoeda Mining).



**Motor de busca privado por padrão:** O LibreWolf usa por padrão o DuckDuckGo como seu motor de busca inicial, que não retém nenhum histórico de suas consultas. Outras alternativas orientadas para a privacidade (Searx, Qwant, Whoogle) também estão disponíveis.



**Proteção anti-fingerprint reforçada:** A impressão digital permite que um navegador seja identificado de forma única através da sua configuração, mesmo sem cookies. Para contrariar isto, o LibreWolf ativa a tecnologia RFP (Resist Fingerprinting) do projeto Tor, para tornar o seu navegador o mais genérico possível. Testes mostram que um Firefox padrão é ~90% único em ferramentas como coveryourtracks.eff.org, comparado com apenas ~10-20% para o LibreWolf (estes números são indicativos e podem variar de acordo com a configuração de software e hardware e extensões instaladas).



![LIBREWOLF](assets/fr/07.webp)


*Página de teste da EFF [Cover Your Tracks] (https://coveryourtracks.eff.org/) com o botão TEST YOUR BROWSER. Esta página é utilizada para avaliar a proteção contra localizadores e recolha de impressões digitais



![LIBREWOLF](assets/fr/08.webp)


*Resultado do teste Cover Your Tracks. A mensagem "tem uma forte proteção contra o rastreio da Web" é apresentada, mostrando a eficácia da proteção do LibreWolf.*



**O LibreWolf ativa definições de segurança rigorosas por defeito. A Proteção Melhorada contra Rastreio do Firefox é levada ao nível Estrito para bloquear milhares de rastreadores, cookies de terceiros e conteúdo malicioso. Também ativa o isolamento de sites e cookies (*Total Cookie Protection*) para dividir os dados por cada domínio e restringe o WebRTC (limitando *ICE candidates* e encaminhando via proxy quando um proxy está presente) para reduzir o risco de fuga de IP Address.



**Atualizações rápidas do motor:** O projeto segue os desenvolvimentos do Firefox muito de perto: O LibreWolf é sempre baseado na última versão estável do Firefox, e os mantenedores se esforçam para lançar uma nova versão dentro de 24 a 72 horas de cada lançamento oficial do Firefox.



## Vantagens e desvantagens



### Benefícios





- Sem telemetria ou conexões indesejadas:** O LibreWolf não transmite dados de uso, garantindo total respeito à sua privacidade.





- Código aberto e baseado na comunidade:** O projeto é 100% de código aberto e mantido por voluntários. Esta independência garante que nenhum modelo de publicidade influenciará o desenvolvimento.





- Pré-configurado para privacidade:** O LibreWolf poupa-lhe tempo precioso: não precisa de passar horas a endurecer as definições do Firefox, já está tudo feito.





- Bloqueador/rastreador de anúncios nativo:** O uBlock Origin está integrado como padrão, pelo que não tem de fazer nada para se proteger contra anúncios e bugs.





- Excelente proteção anti-impressão digital:** Graças ao RFP e às numerosas configurações de privacidade, o LibreWolf reduz drasticamente a sua pegada digital única na web.





- Desempenho melhorado e peso leve:** Ao remover a telemetria e certos recursos não essenciais, o LibreWolf pode ser um pouco mais rápido e consumir menos energia que o Firefox padrão.



### Desvantagens e limitações





- Sem atualizações automáticas integradas:** O LibreWolf não se atualiza sozinho. Cabe a você instalar novas versões assim que elas forem lançadas, para se manter seguro.





- Compatibilidade reduzida com certos serviços:** Devido às suas configurações muito rígidas, o LibreWolf pode encontrar problemas em certos sites. As plataformas de streaming Netflix e Disney+ não funcionarão, pois o LibreWolf desativa o Widevine DRM por padrão.





- Sem rede anónima integrada:** Ao contrário do Navegador Tor, o LibreWolf não roteia o tráfego através do Tor ou de uma VPN por si só. Se precisar de anonimato de rede, terá de configurar manualmente um proxy/VPN.





- Cookies e sessões não persistentes (padrão):** Por razões de confidencialidade, o LibreWolf apaga os cookies, o histórico e os dados do site cada vez que você fecha o navegador. Terá de iniciar sessão nas suas contas novamente sempre que iniciar sessão.





- Sem versão móvel ou sincronização na nuvem:** O LibreWolf está disponível apenas no computador (Windows, Linux, macOS). Não existe uma aplicação móvel e, portanto, não há sincronização de contas ou marcadores através de uma nuvem.



## Instalando o LibreWolf



**Site oficial:** [librewolf.net](https://librewolf.net)



O LibreWolf está disponível para todos os principais sistemas operativos de secretária: Linux, Windows e macOS. Para baixar o LibreWolf, visite o site oficial:



![LIBREWOLF](assets/fr/02.webp)


*Página inicial do LibreWolf (librewolf.net) mostrando o logotipo do navegador, um botão azul Instalar, e os links Código Fonte e Documentação. Uma grande seta azul aponta para o botão Instalar*



Clique no botão "Instalação" para aceder a instruções detalhadas para o seu sistema operativo:



![LIBREWOLF](assets/fr/03.webp)


*Página de seleção do sistema operativo para download do LibreWolf.*



A instalação difere consoante o seu sistema operativo:



### No Linux


O LibreWolf oferece compilações para muitas distribuições. No Debian/Ubuntu e derivados, um repositório APT oficial está disponível. Alternativamente, o LibreWolf é publicado em Flatpak no Flathub:


```
flatpak install flathub io.gitlab.librewolf-community
```



### No Windows


Descarregue o instalador (.exe) do sítio Web oficial ou utilize o ficheiro:




- Chocolatey:** `choco install librewolf`
- WinGet:** `winget install librewolf`



### No macOS


O LibreWolf está disponível como um pacote .dmg para Mac. Baixe a imagem de disco do site oficial e arraste e solte o aplicativo LibreWolf na pasta Aplicativos. Em alternativa, pode instalá-lo através do Homebrew.




## Configuração e primeira utilização



No primeiro arranque, irá reparar no familiar Firefox Interface, exceto que é mais despojado: a página inicial contém apenas a barra de pesquisa e não contém sugestões patrocinadas. Verá o ícone do uBlock Origin na barra de ferramentas - um sinal de que o bloqueador está ativo.



![LIBREWOLF](assets/fr/04.webp)


*Página inicial do LibreWolf com extensões e menu. Uma seta azul no canto superior direito indica o ícone do menu (três barras horizontais)



O LibreWolf carrega automaticamente suas páginas em modo "estrito" (anti-rastreamento), e o mecanismo de busca padrão será o DuckDuckGo. Você pode tentar visitar um site de teste de rastreamento (por exemplo, amiunique.org) para observar a pegada exposta - ela deve ser muito mais genérica do que com um navegador padrão.



### Definições de privacidade



O LibreWolf já está configurado de forma ideal para a privacidade. No Menu → Opções → Privacidade e Segurança, você verá que o LibreWolf está configurado para o modo de Proteção Avançada de Rastreamento: Estrito. Este modo bloqueia:




- Localizadores inter-sítios
- Cookies de terceiros
- Conteúdo de rastreio conhecido
- Criptomineração
- Detectores de impressões digitais



![LIBREWOLF](assets/fr/05.webp)


*Página do separador Segurança e privacidade que mostra as definições de segurança do LibreWolf.*



O WebRTC está desativado (evitando fugas de IP) e a Proteção Total de Cookies está em vigor. A telemetria e os inquéritos do Firefox estão totalmente desactivados.



### Gestão de cookies e do histórico



Por padrão, o LibreWolf exclui cookies e armazenamento local cada vez que é fechado. Se esse comportamento o incomoda, você pode ajustá-lo em Privacidade e Segurança → Cookies e dados do site, desmarcando "Excluir cookies e dados do site ao fechar o LibreWolf".



![LIBREWOLF](assets/fr/06.webp)


*A mesma página, um pouco mais abaixo, mostra a opção de apagar os cookies quando o browser é fechado*



### Adicionar extensões úteis



Por uma questão de princípio, o LibreWolf desencoraja a adição de extensões desnecessárias, pois cada extensão pode ser um vetor de rastreamento. No entanto, algumas extensões de boa reputação podem melhorar a sua experiência:




- Firefox Multi-Account Containers** (da Mozilla) para navegação compartimentada
- Decentraleyes** ou **LocalCDN** para servir bibliotecas comuns localmente



Evite sobretudo extensões "VPN gratuitas" ou proxies duvidosos - o uBlock Origin já cobre 99% das suas necessidades.



## Utilização quotidiana



### Navegação diária na Web


Utilize o LibreWolf para as suas actividades quotidianas na Internet. A principal diferença em relação aos outros navegadores é que deixa muito menos vestígios de publicidade. Os banners de "aceitar cookies" desaparecem em muitos sites, graças às listas de filtragem do uBlock.



### Utilizar separadores privados para compartimentar


Mesmo que o LibreWolf apague tudo no final da sessão, pode ser útil abrir uma janela privada do navegador (Ctrl+Shift+P) para certas tarefas durante a sessão, a fim de separar uma identidade específica.



### Tirar partido de contentores com várias contas


A instalação da extensão Multi-Account Containers pode ajudá-lo bastante a segmentar as suas actividades em silos estanques. Por exemplo, pode definir um contentor "Banca" para os seus sites bancários, um contentor "Redes sociais" para o Facebook/Twitter, etc. Cada contentor tem os seus próprios cookies, sessões e armazenamento isolado. Cada contentor tem os seus próprios cookies, sessões e armazenamento isolado.



### Gestão de permissões afinada por sítio


O LibreWolf permite controlar as permissões que você dá aos sites (Localização, Câmera, Microfone, Notificações) caso a caso. Conceda permissões apenas a sites em que confia e quando necessário.



## Melhores práticas com o LibreWolf



1. **Mantenha o LibreWolf atualizado:** Verifique o site regularmente para novas versões, especialmente após um lançamento estável do Firefox.



2. **Evitar misturar identidade pessoal e navegação privada:** Idealmente, não deve iniciar sessão com as suas contas pessoais na mesma sessão em que está a fazer investigação sensível.



3. **Não sobrecarregue o LibreWolf com extensões supérfluas:** Cada extensão que você instala pode introduzir riscos de segurança ou de impressão digital.



4. **Use uma VPN ou proxy Tor adicionalmente:** O LibreWolf não o torna anónimo para o seu ISP. Para anonimato na rede, você pode usar o LibreWolf por trás de uma VPN confiável.



5. **Guarde os seus dados importantes:** Marcadores, palavras-passe, se armazenados localmente. Considere um gestor de palavras-passe externo (KeePassXC, Bitwarden) em vez do gestor de palavras-passe básico do browser.



## Comparação com outros navegadores



O LibreWolf faz parte da "caixa de ferramentas" dos navegadores orientados para a privacidade:



**LibreWolf vs. Firefox:** O LibreWolf já chega fortalecido e sem qualquer telemetria. O Firefox mantém a vantagem da sincronização de vários dispositivos e uma base de utilizadores muito grande, mas requer configuração manual para atingir o nível de confidencialidade do LibreWolf.



**O Brave utiliza o código do Chrome/Chromium e integra um modelo de negócio através do seu programa de publicidade opcional. O LibreWolf, sendo um Fork comunitário para o Firefox, mantém o ecossistema livre da Mozilla e não tem ligações à Google.



**LibreWolf vs Tor Browser:** O Tor Browser é insubstituível para o anonimato face a uma vigilância poderosa, mas é lento e desconfortável na utilização quotidiana. O LibreWolf, para a navegação quotidiana na Web clássica, é muito mais rápido e prático.



**LibreWolf vs Mullvad Browser:** O Mullvad Browser vai ainda mais longe na estandardização, mas à custa de uma usabilidade reduzida (impossível manter um cookie de login). O LibreWolf consegue um equilíbrio: muito privado, mas utilizável no dia a dia.



## Conclusão



O LibreWolf representa uma excelente solução para quem procura um navegador ultra-privado para o "dia a dia" sem chegar ao anonimato extremo do Tor. É a escolha ideal para activistas, jornalistas, programadores ou utilizadores avançados que pretendem uma navegação clássica na Web (rápida, compatível com sítios modernos), escapando ao rastreio de anúncios e às grandes empresas tecnológicas.



Embora tenha certas limitações (sem actualizações automáticas, compatibilidade reduzida com certos serviços), o LibreWolf é uma ferramenta valiosa no arsenal de qualquer pessoa que deseje recuperar o controlo da sua privacidade digital. A sua facilidade de utilização e configuração predefinida fazem dele uma escolha sensata para utilizadores preocupados com a privacidade.



## Recursos



### Documentação oficial




- [Sítio Web oficial do LibreWolf](https://librewolf.net)
- [Código fonte em Codeberg](https://codeberg.org/librewolf)
- [FAQ oficial](https://librewolf.net/docs/faq)



### Guias e comparações




- [Guias de privacidade] (https://www.privacyguides.org/en/desktop-browsers/)
- [Testes comparativos de privacidade] (https://privacytests.org)



### Apoio comunitário




- [Subreddit r/LibreWolf](https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf](https://matrix.to/#/#librewolf:matrix.org)