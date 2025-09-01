---
name: Navegador Orion
description: Como utilizar o Orion Browser para proteger a sua privacidade no Mac e no iPhone?
---

![cover](assets/cover.webp)



## Introdução



Num contexto em que a maioria dos browsers recolhe massivamente os nossos dados pessoais, a escolha de um browser amigo da privacidade torna-se crucial. O Chrome domina com 65% do mercado global, mas o seu modelo de negócio baseia-se na exploração dos seus dados de navegação. O Safari, embora integrado no ecossistema Apple, carece de funcionalidades de proteção avançadas e não suporta de forma flexível extensões de terceiros.



![Répartition du marché des navigateurs](assets/fr/01.webp)


*Repartição do mercado dos programas de navegação Web: O Chrome domina com mais de 65% de quota de mercado, seguido do Safari, Edge e Firefox*



**O Orion Browser** apresenta-se como uma alternativa inovadora para os utilizadores Apple. Desenvolvido pela Kagi, este navegador combina a velocidade do motor WebKit com uma filosofia de telemetria zero. Ao contrário dos seus concorrentes, o Orion não envia dados para servidores remotos e bloqueia nativamente 99,9% dos anúncios e rastreadores, incluindo o YouTube.



A sua caraterística única? O Orion é o **único navegador WebKit** que instala nativamente extensões do Chrome **e** Firefox, oferecendo o melhor dos dois mundos. Esta compatibilidade, combinada com um consumo de memória 2 a 3 vezes inferior ao de outros navegadores e uma integração perfeita com o ecossistema Apple (iCloud, Keychain), torna-o a escolha ideal para utilizadores de Mac e iPhone preocupados com a privacidade.



## Porquê escolher o Orion Browser?



### Principais benefícios



**Máxima proteção logo à saída da caixa**: O Orion bloqueia 99,9% dos anúncios (incluindo o YouTube) e todos os rastreadores próprios e de terceiros por padrão. A sua tecnologia combina a Prevenção Inteligente de Rastreio do WebKit com as listas EasyPrivacy para máxima eficiência. Caraterística única: O Orion bloqueia os scripts de impressão digital **antes de serem executados**, tornando o rastreio literalmente impossível - uma abordagem mais radical do que outros navegadores que apenas tentam "mascarar" os dados.



**Zero telemetria verificável**: O Orion adopta uma abordagem radical à privacidade, com zero telemetria por conceção. Ao contrário de outros browsers, que fazem centenas de pedidos de rede no arranque (expoente IP, impressão digital do browser, informações pessoais), o Orion nunca "telefona para casa". Esta diferença fundamental elimina completamente o risco de fuga não intencional de dados.



**Desempenho excecional**: Baseado em uma versão otimizada do WebKit, o Orion iguala ou até supera o Safari em velocidade no Mac. Os testes do Speedometer 2.0/2.1 o colocam consistentemente em primeiro lugar nos processadores Apple Silicon. O bloqueio nativo de anúncios acelera ainda mais o carregamento da página em 20 a 40%.



**Suporte universal a extensões**: Uma grande inovação, o Orion permite-lhe instalar extensões a partir da Chrome Web Store **e** Mozilla Add-ons. O suporte para WebExtensions é atualmente experimental, com um objetivo de compatibilidade a 100% na versão beta. Pode utilizar muitas extensões populares como o uBlock Origin, Bitwarden, mesmo no iPhone - uma estreia mundial no iOS, embora algumas possam não funcionar na perfeição.



### Limitações a ter em conta





- Disponibilidade limitada**: Atualmente reservado para macOS e iOS/iPadOS. Uma versão para Linux está a atingir os marcos de desenvolvimento (marco 2 em 2025), mas não está disponível uma versão pública. O Windows e o Android não estão a ser desenvolvidos por falta de recursos.
- Código-fonte fechado**: Embora alguns componentes sejam de código aberto, o Orion continua a ser predominantemente proprietário, um ponto de debate na comunidade da privacidade.
- Extensões experimentais**: O suporte de extensões permanece em versão beta, com incompatibilidades frequentes. As extensões podem afetar o desempenho e algumas não funcionam de todo.
- Segurança do WebKit**: Ao contrário do Chromium, o WebKit não oferece um isolamento de processos por site tão robusto, o que pode representar riscos de segurança em determinados cenários.
- Testes de bloqueio**: O Orion tem um desempenho deliberadamente fraco nos testes de publicidade online (26-35%), uma vez que a Kagi considera que estes testes são "fundamentalmente imperfeitos". A eficácia real na utilização quotidiana é muito superior.



## Instalação do Orion Browser



### No macOS



![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)


*A página inicial da Kagi apresenta o Orion Browser como "um navegador sem anúncios com proteção total da privacidade e suporte universal de extensões "*





- Aceder a [kagi.com/orion](https://kagi.com/orion/)
- Clique em "**Download do Orion para macOS**"



![Page de téléchargement d'Orion Browser](assets/fr/03.webp)


*A página de transferência do Orion Browser mostra a disponibilidade para macOS e iOS, com ligações para a App Store*





- Abra o ficheiro `.dmg` transferido
- Arraste a aplicação Orion para a pasta Aplicações
- No primeiro arranque, o macOS pede-lhe para confirmar a abertura



**Alternativa Homebrew**:


```bash
brew install --cask orion
```



### No iPhone/iPad





- Abrir a **App Store**
- Procurar por "**Orion Browser by Kagi**"
- Instalar a aplicação gratuita (compatível com iOS 15+)



### Configuração inicial



No primeiro lançamento, o Orion guia-o através de vários passos:



**1. Ecrã de boas-vindas


![Écran de bienvenue d'Orion](assets/fr/04.webp)


*O ecrã de boas-vindas do Orion Browser destaca as principais caraterísticas: navegação mais rápida, telemetria zero, bloqueio de anúncios e suporte de extensões*



**2. Personalização do Interface


![Options de personnalisation](assets/fr/05.webp)


*O ecrã de personalização permite-lhe configurar o aspeto dos separadores e do Interface de acordo com as suas preferências*





- Importação de dados**: Transfere facilmente os favoritos e as palavras-passe do Safari, Chrome ou Firefox
- Sincronização ICloud**: Ativar para encontrar os seus favoritos e separadores em todos os seus dispositivos Apple



**3. Instalação em dispositivos móveis**


![Installation sur iOS](assets/fr/06.webp)


*Ecrã de instalação no iOS com o código QR para descarregar rapidamente o Orion Browser da App Store*



**4. Boas-vindas e ferramentas essenciais do Interface



![Page d'accueil Orion](assets/fr/07.webp)


*Página inicial do Orion Browser Interface: a seta indica as três principais ferramentas acessíveis diretamente a partir da barra Address*



Quando a configuração estiver concluída, descobrirá o Interface simplificado do Orion com as suas **três ferramentas essenciais** (indicadas pela seta):





- Escudo 🛡️**: Apresenta o Relatório de Privacidade com o número de itens bloqueados na página atual
- Pincel 🖌️**: Personalizar a apresentação da página (tema, tipo de letra, remover Elements que distrai)
- Engrenagem ⚙️**: Configurar parâmetros específicos do sítio Web (permissões, bloqueio, etc.)



Estas ferramentas estão sempre disponíveis e permitem-lhe controlar a sua experiência de navegação site a site.



**Importante**: O Orion é gratuito e não requer registo ou criação de conta para funcionar.



![Orion+ dans les préférences](assets/fr/08.webp)


*Ecrã de subscrição do Orion+ nas preferências, oferecendo uma subscrição opcional para apoiar o desenvolvimento*



**Orion+ (opcional)**: Para apoiar o desenvolvimento de projectos, a Kagi oferece o Orion+ ($5/mês, $50/ano ou $150 vitalício). Esta subscrição voluntária permite:




- Comunicar diretamente com a equipa de desenvolvimento
- Influenciar a evolução do browser de acordo com as suas necessidades
- Aceder a versões Nightly com as mais recentes funcionalidades experimentais
- Beneficie do mais recente motor WebKit
- Obter um distintivo distintivo no fórum de comentários



Orion+ garante a independência do projeto: "A sua contribuição financeira ajuda-nos a permanecer independentes e a manter a nossa promessa de nos tornarmos o melhor navegador para os nossos utilizadores". É este modelo de financiamento pelos utilizadores que mantém o Orion livre de anúncios e de telemetria.



## Configuração para máxima confidencialidade



### Parâmetros essenciais



Aceder às preferências através de **Orion → Preferências** (ou ⌘,):



**1. Pesquisa - Motor de pesquisa privado**



![Configuration du moteur de recherche](assets/fr/09.webp)


*Configuração predefinida do motor de busca: DuckDuckGo está selecionado para máxima privacidade*





- Motor predefinido**: Selecionar **DuckDuckGo**, **Startpage** ou **Kagi** para uma privacidade ideal (evitar Google/Bing)
- Sugestões de pesquisa**: Desactivá-las para evitar que as teclas digitadas sejam transmitidas aos servidores dos motores de busca



**2. Privacidade - proteção geral**



![Content Blocker dans les préférences](assets/fr/12.webp)


*Definições de privacidade Orion mostrando o Bloqueador de Conteúdos com 119.156 regras activas, opções de remoção de rastreadores e agente de utilizador personalizado*



**Bloqueador de conteúdos ativo por defeito**:




- EasyList**: mais de 119 mil regras de bloqueio de anúncios
- EasyPrivacy**: Proteção contra o rastreio
- Gerenciar listas de filtros**: Adicionar listas adicionais (recomendado pelo Hagezi)



**Opções de privacidade**:




- Remover localizadores de URLs**: "Apenas para navegação privada" limpa as hiperligações copiadas
- Partilhar relatórios de acidentes**: "Depois de pedir aprovação" respeita o seu consentimento
- Agente de utilizador personalizado**: Pode ser modificado para contornar certos bloqueios



![YouTube avec Privacy Report](assets/fr/10.webp)


*Exemplo de YouTube visualizado com Orion: nenhuma publicidade visível e Relatório de Privacidade que mostra os muitos Elements bloqueados*



**3. Definições do sítio Web - Controlo por sítio**



![Website Settings pour YouTube](assets/fr/11.webp)


*Definições do sítio Web para o YouTube com opções de compatibilidade, bloqueio de conteúdos e permissões específicas do sítio*



**Acesso rápido**: Clique na engrenagem ⚙️ na barra Address para ajustar:




- Modo de compatibilidade**: Resolve problemas de visualização suspendendo as extensões
- Bloqueadores de conteúdo**: Desativar o bloqueio de um sítio específico, se necessário
- JavaScript/Cookies**: Controlo granular por site
- Permissões**: Câmara, microfone, localização configurados individualmente



**4. Filtros personalizados avançados** (ver abaixo)



**Criar filtros personalizados** (Privacidade → Gerir listas de filtros → Filtros personalizados):



**Sintaxe simplificada** (compatível com Adblock Plus):




- `reddit.com##.promotedlink`: Oculta posts patrocinados do Reddit
- `||ads.example.com^`: Bloqueia completamente um domínio de publicidade
- `@@||site-utile.com^`: Cria uma exceção para um site



**Dica: Visite [FilterLists.com] (https://filterlists.com) para obter milhares de listas especializadas prontas a utilizar.



### Extensões recomendadas



O Orion suporta nativamente as extensões do Chrome e do Firefox. Instale-as diretamente a partir das lojas oficiais:



**Elementos essenciais**:




- uBlock Origin**: Adiciona controlo granular ao bloqueador nativo
- Bitwarden**: Gestor de senhas de código aberto
- ClearURLs**: Elimina os parâmetros de rastreamento de URL



**Opcional**:




- LocalCDN**: Serve bibliotecas partilhadas localmente
- Exclusão automática de cookies**: Elimina automaticamente os cookies depois de fechar os separadores
- NoScript**: Controlo total sobre a execução de JavaScript (utilizadores avançados)



Para instalar um:




- Visite [chrome.google.com/webstore](https://chrome.google.com/webstore) ou [addons.mozilla.org](https://addons.mozilla.org)
- Clique em "Adicionar ao Chrome/Firefox"
- O Orion interceptará e instalará a extensão automaticamente



**Atenção**: Como o suporte de extensões é experimental, muitas extensões podem não funcionar corretamente ou podem afetar o desempenho. Em caso de problema (sítio que deixa de funcionar, lentidão), desativar as extensões uma a uma para identificar a origem.



## Utilização diária



### Interface e caraterísticas únicas




![Outil de personnalisation pinceau](assets/fr/13.webp)


*Menu do pincel Orion para personalizar o ecrã: tamanho da letra, tema (claro/escuro), desativação de cabeçalhos autocolantes e remoção de Elements* que distraem



**Ferramenta de pincel: personalização avançada



A ferramenta **brush** do Orion é uma caraterística única que lhe permite personalizar a apresentação de cada sítio Web:



**Opções de tema**:




- Alternar entre temas claros e escuros para cada sítio
- Adaptação automática às preferências do seu sistema



**Controlo tipográfico**:




- Tamanho da letra**: Ajustar a legibilidade com os botões A- e A+
- Estilo do tipo de letra**: Alterar a família do tipo de letra (predefinida ou personalizada)



**Limpeza do Interface**:




- Desativar cabeçalhos fixos**: Remove os cabeçalhos que ficam presos no topo quando se desloca
- Eliminar o Elements**: Remover permanentemente o irritante Elements (anúncios, pop-ups, banners de cookies)
  - Clique em "+ Apagar" e selecione o item a ocultar
  - Muito útil para sítios com anúncios persistentes ou rastreio visual Elements



**Persistência**: Todas estas definições são guardadas por domínio e automaticamente reaplicadas na próxima vez que o utilizador as visita.



**Gestão avançada de separadores**:




- Separadores verticais**: Ativar através da barra de menus (função Separadores laterais)
- Separadores compactos**: Em Preferências → Separadores → Layout "Compacto" para poupar espaço
- Grupos de separadores**: Organize as suas sessões por tema
- Múltiplos perfis**: Criar identidades separadas através da barra de menu (função Perfis) com dados completamente isolados



**Modo de baixo consumo**: Inspirado no iPhone, este modo suspende automaticamente os separadores inactivos após 5 minutos e pode reduzir o consumo de energia até 90%. Active-o através da barra de menus do Orion no Mac ou nas definições no iOS.



**Ferramentas incorporadas** (menu Editar e outras):




- Editar texto na página**: modificar temporariamente qualquer texto (menu Editar)
- Permitir copiar e colar**: Ultrapassa as restrições de cópia (menu Editar)
- Copiar ligação limpa**: Clique com o botão direito do rato numa ligação para remover os parâmetros de rastreio
- Modo Focus**: navegação em ecrã inteiro sem distracções
- Picture-in-Picture**: Ver vídeos numa janela flutuante
- Abrir no Arquivo da Internet**: Acesso direto às versões arquivadas
- Relatório de privacidade**: Clique no escudo 🛡️ para ver os itens bloqueados por página



### Gestão da navegação privada



A navegação privada do Orion (⌘⇧N) oferece:




- Isolamento completo de cookies e sessões
- Eliminação automática no encerramento
- Histórico e desativação da cache
- Proteção reforçada contra a recolha de impressões digitais



**Dica**: Para uma compartimentação avançada, crie **perfis separados** através da barra de menus (função Perfis). Cada perfil aparece como uma aplicação separada na Dock, com as suas próprias definições, extensões e dados completamente isolados.



### Otimização do desempenho e privacidade



Para manter Orion rápido e privado:




- Extensões**: Limitar ao mínimo estritamente necessário (pode reduzir o desempenho)
- Modo de baixo consumo**: Ativar para sessões longas (90% de poupança possível)
- Relatório de privacidade**: Clique no escudo 🛡️ para ver os bloqueios em tempo real
- Personalização visual**: Utilize o pincel 🖌️ para adaptar o ecrã e remover o Elements que distrai
- Copiar ligação limpa**: Clique com o botão direito do rato para copiar ligações sem localizadores
- Perfis separados**: Utilize perfis dedicados para compartimentar as suas actividades
- Definições do sítio Web**: Clique na engrenagem ⚙️ para adaptar as permissões por sítio
- Limpeza regular**: Limpar a cache através do Orion → Limpar dados de navegação



## Comparação com alternativas



| Critère | Orion | Safari | Chrome | Firefox | Brave |
|---------|-------|--------|---------|----------|--------|
| **Télémétrie** | Aucune | Minimale | Extensive | Modérée | Minimale |
| **Bloqueur natif** | 99,9% efficace | Basique | Absent | Partiel | Complet |
| **Extensions** | Chrome + Firefox | Limitées | Chrome uniquement | Firefox uniquement | Chrome uniquement |
| **Performance Mac** | Excellente | Excellente | Bonne | Moyenne | Bonne |
| **Consommation RAM** | Très faible | Faible | Élevée | Moyenne | Moyenne |
| **Open Source** | Partiel | Partiel (WebKit) | Partiel | Complet | Complet |
| **Plateformes** | Mac/iOS | Mac/iOS | Toutes | Toutes | Toutes |

**Contra o Safari**: O Orion oferece uma proteção superior com o seu avançado bloqueador e suporte de extensões, mantendo o desempenho do WebKit.



**Versus Chrome**: privacidade inigualável sem comprometer a compatibilidade, graças ao suporte para extensões do Chrome.



**Versus Firefox**: Mais rápido no Mac, Interface mais intuitivo, mas menos controlo granular e não é de código aberto.



**Contra o Brave**: Filosofia semelhante, mas o Orion evita controvérsias sobre criptografia/BAT e oferece uma melhor integração com a Apple.



## Casos de utilização recomendados



**Ideal para**:




- Os utilizadores da Apple procuram mais privacidade do que o Safari
- Pessoas que pretendem bloquear todos os anúncios (incluindo o YouTube) sem extensões
- Os programadores necessitam de ferramentas de desenvolvimento WebKit com proteção de privacidade integrada
- Os utilizadores do iPhone querem extensões do ambiente de trabalho no telemóvel (inovação única)
- Profissionais que necessitam de compartimentar as suas actividades (perfis múltiplos)
- Utilizadores móveis que procuram uma melhor gestão da bateria (modo de baixo consumo)



**Evitar se**:




- Utiliza principalmente o Windows/Linux (nenhuma versão disponível)
- O código aberto completo é essencial para o seu modelo de ameaças
- Depende de extensões específicas que podem não funcionar
- Necessita de sincronização entre plataformas para além do ecossistema Apple
- Prefere uma solução comprovada e estável (estado beta permanente desde 2021)



## Pontos de atenção e segurança



### Caraterísticas de segurança únicas



**Proteção revolucionária contra impressões digitais**: O Orion é o único navegador que bloqueia completamente a execução de scripts de impressão digital antes que eles possam verificar seu sistema. Esta abordagem "nenhum script em execução = nenhuma impressão digital possível" supera os métodos tradicionais de mascaramento utilizados por outros navegadores.



**Lista branca transparente**: O Orion mantém uma pequena lista pública de sites (browserbench.org, wizzair.com) em que o bloqueio é automaticamente desativado para evitar problemas de funcionamento. Esta transparência permite que os utilizadores compreendam exatamente quando e porque é que o bloqueio é aliviado.



**Extensões não auditadas**: O suporte para extensões do Chrome/Firefox introduz riscos adicionais, uma vez que estas extensões não foram concebidas para o WebKit e não são especificamente auditadas para este ambiente.



### Manutenção e actualizações





- Actualizações automáticas**: O Orion é atualizado automaticamente no macOS através do Sparkle
- Controlo de vulnerabilidades**: Verificar regularmente as notas de lançamento para correcções de segurança
- Relatório de erros**: Utilize [orionfeedback.org] (https://orionfeedback.org) para comunicar problemas




## Conclusão



O Orion Browser representa um avanço significativo para a privacidade no macOS e iOS. A sua abordagem de telemetria zero, combinada com um bloqueador nativo ultra-eficiente e um suporte único para extensões universais, torna-o uma excelente escolha para utilizadores Apple preocupados com a privacidade.



**Importante**: O Orion permanece em versão beta permanente desde 2021, com limitações de compatibilidade de extensão e riscos inerentes ao WebKit. Avalie estas compensações de acordo com o seu modelo de ameaças.



Para uma utilização quotidiana num Mac ou iPhone, é provavelmente o melhor compromisso entre confidencialidade, desempenho e facilidade de utilização disponível no ecossistema Apple, desde que se aceitem as suas limitações.



Lembre-se: a proteção da sua privacidade não depende apenas do seu browser. Combine o Orion com as melhores práticas (palavras-passe fortes, 2FA, VPN, se necessário) para uma segurança online optimizada.



## Recursos e apoio



### Documentação oficial




- Sítio Web oficial**: [kagi.com/orion](https://kagi.com/orion/)
- FAQ completo**: [browser.kagi.com/faq](https://browser.kagi.com/faq)
- Fórum da comunidade**: [community.kagi.com](https://community.kagi.com)
- Acompanhamento de bugs**: [orionfeedback.org](https://orionfeedback.org)
- GitHub Orion**: [github.com/OrionBrowser](https://github.com/OrionBrowser) - Componentes de código aberto
- Blogue Kagi**: [blog.kagi.com](https://blog.kagi.com) - Notícias e actualizações



### Ensaios de verificação recomendados



Após a configuração, teste a sua instalação:




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/) - Teste às impressões digitais
- [Teste de Fuga de DNS](https://www.dnsleaktest.com/) - Verificar se há fugas de DNS
- [BrowserLeaks](https://browserleaks.com/) - Conjunto completo de testes de privacidade



### Alternativas ao Plan ₿ Network


Para uma proteção máxima, consulte os nossos outros guias:




- [Firefox reforçado](https://planb.network/tutorials/computer-security/firefox) - Configuração avançada multiplataforma
- [Tor Browser](https://planb.network/tutorials/computer-security/tor-browser) - Anonimato total na rede
- [Mullvad Browser](https://planb.network/tutorials/computer-security/mullvad-browser) - Máxima proteção das impressões digitais



Se quiser saber mais sobre a história e o funcionamento dos navegadores, bem como sobre os principais objectos digitais da sua vida quotidiana, convido-o a descobrir o nosso novo curso de formação gratuito SCU 202, disponível em Plan ₿ Network:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1