---
name: Firefox
description: Como configurar o Firefox para proteger a sua privacidade?
---

![cover](assets/cover.webp)



## Introdução



Todos nós passamos horas online, muitas vezes sem nos apercebermos do que o nosso browser está a revelar sobre nós. Cada clique, cada pesquisa, cada sítio que visitamos alimenta uma enorme indústria de recolha de dados pessoais.



![Statistiques navigateurs 2024](assets/fr/01.webp)


*Quota de mercado dos navegadores Web: O Chrome domina com 65% do mercado, seguido do Safari e do Edge. Fonte: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



Como mostra este gráfico, o Google Chrome domina maciçamente, com mais de 65% da utilização mundial. Esta hegemonia significa que a maioria dos utilizadores da Internet confia os seus dados de navegação à Google, uma empresa cujo modelo de negócio se baseia na publicidade direcionada. O Firefox, com apenas 3% do mercado, representa uma alternativa desenvolvida pela Mozilla, uma organização sem fins lucrativos que não tem qualquer interesse comercial em explorar os seus dados.



Mas escolher o Firefox é apenas o primeiro passo. Por defeito, até o Firefox necessita de ajustes para maximizar a sua proteção. Este guia leva-o passo a passo, do mais simples ao mais avançado, para transformar o Firefox num verdadeiro escudo contra o rastreio, preservando uma experiência de navegação agradável.



### Porquê o Firefox?





- Gratuito e de código aberto** (motor Gecko): código auditável e transparente
- Organização sem fins lucrativos**: Fundação Mozilla, missão de interesse geral
- Protecções nativas incorporadas**: Proteção Melhorada contra Rastreio (ETP), Proteção Total contra Cookies (TCP), Particionamento de Estado, modo apenas HTTPS, DNS sobre HTTPS (DoH)
- Personalização avançada**: ao contrário do Chrome, o Firefox permite-lhe modificar o seu comportamento em profundidade



### Princípios importantes antes de começar





- Não existe uma receita universal**: quanto mais se modifica, mais se corre o risco de se destacar (impressão digital). O objetivo é estar mais bem protegido sem se destacar da multidão.
- Progresso passo a passo**: Altere uma definição, teste os seus sítios habituais e, em seguida, continue. Não é necessário alterar tudo de uma vez.
- Equilíbrio pessoal**: Encontre o SEU compromisso entre privacidade e facilidade de utilização.



## Instalação rápida



![Téléchargement Firefox](assets/fr/02.webp)



**Transferência oficial:** Aceda a [firefox.com/browsers/desktop] (https://www.firefox.com/en-US/browsers/desktop/). Nesta página, selecione o seu sistema operativo (Windows, macOS, Linux) para aceder à página de transferência adequada com instruções de instalação específicas.





- Windows**: transfira o instalador `.exe`, faça duplo clique e siga o assistente de instalação
- macOS**: descarregue o ficheiro `.dmg`, abra-o e arraste o Firefox para a pasta Aplicações
- Linux**: várias opções disponíveis - pacote `.deb`/`.rpm`, Flatpak (Flathub), Snap, ou via gerenciador de pacotes (apt, dnf, pacman). Prefira os fontes oficiais da Mozilla.



**Dica:** Uma vez instalado, verifique se existem actualizações através de Ajuda → **Sobre o Firefox** (importante para correcções de segurança).



![Configuration initiale Firefox](assets/fr/03.webp)


*Primeiro ecrã ao iniciar o Firefox: defina o Firefox como o seu navegador predefinido, adicione-o aos seus atalhos e clique em "Guardar e continuar "*



![Création compte Firefox](assets/fr/04.webp)


*Passo opcional: criar ou iniciar sessão numa conta Firefox. Pode saltar este passo clicando em "Agora não" no canto inferior direito*



![Page d'accueil Firefox](assets/fr/05.webp)


*Ecrã inicial do Firefox quando a configuração estiver concluída. Note o menu ☰ no canto superior direito, que dá acesso a Definições e Extensões para personalizar o Firefox*



## Protecções já activadas por defeito (tranquilizador)





- Isolamento de sítios (Fissão)**: em implementação progressiva. Esta funcionalidade executa cada site num processo separado para impedir que um separador malicioso aceda aos dados de outro. Verifique seu status em `about:support` (procure por "Fission"). Se não estiver ativado, pode activá-lo manualmente em `about:config` com `fission.autostart = true`.
- Proteção total de cookies (TCP)**: ativa por predefinição. Os cookies e outros tipos de armazenamento estão confinados ao sítio da primeira parte (um "jarro" por sítio), o que neutraliza o rastreio entre sítios. Quando necessário, são feitas excepções temporárias através da API de acesso ao armazenamento (botões de início de sessão integrados).
- Proteção de Rastreio de Saltos/Redireccionamento**: O Firefox detecta e limpa automaticamente os cookies deixados pelos sites de rejeição (links que o redireccionam através de um rastreador antes do destino), reduzindo este canal de rastreamento sem qualquer ação da sua parte.



## Nível 1 - Essencial (≤ 10 minutos)



Objetivo: grandes ganhos de privacidade sem quebrar a Web. Para 90% dos utilizadores.



Para aceder às definições, clique no menu ☰ no canto superior direito e depois em **"Definições "**:



![Paramètres généraux](assets/fr/07.webp)


*Página de definições do Firefox - separador "Geral". É aqui que configura a maioria das suas opções de privacidade*



**Proteção de rastreio (ETP)**




- Mudar **ETP** para **Strict**. Bloqueia mais localizadores (cookies entre sítios, impressões digitais, criptomineração, widgets sociais...).
- Se um site for interrompido (vídeo, botão de início de sessão...), desactive a proteção apenas para esse site através do escudo 🛡️ e, em seguida, actualize o separador.



Eis os diferentes níveis de segurança das ETP:




- Padrão** (equilibrado, compatibilidade máxima)
  - Bloqueios: rastreadores sociais, cookies entre sites (todas as janelas), rastreamento de conteúdo em navegação privada, mineradores de criptomoedas, detectores de impressões digitais.
  - Inclui **Proteção total de cookies** (TCP): um frasco por sítio.
- Estrito** (recomendado para a confidencialidade)
  - Bloqueia também conteúdos de rastreio em todas as janelas + impressões digitais conhecidas e suspeitas.
  - Pode quebrar alguns sites; utilize o escudo 🛡️ para uma exceção local.
- Personalizado** (avançado)
  - Afinação fina: cookies, rastreio de conteúdos, menores, impressões digitais (conhecidas/suspeitas).



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Cookies e dados do sítio




- Ativar **"Eliminar cookies e dados do sítio ao fechar "** para reiniciar de forma limpa sempre que reiniciar.
- Acrescente **Excepções** para 2-3 sítios essenciais, se desejar (correio eletrónico, banco).


**Entrada automática de dados, sugestões e página inicial




- Desativar o **preenchimento automático** (IDs, endereços, cartões). Em vez disso, utilize um gestor de palavras-passe.
- Pesquisar**: desativar **"Mostrar sugestões de pesquisa "**.
- Barra Address**: cortar **"Sugestões patrocinadas "** e **"Sugestões contextuais "**.
- Página inicial**: desativar **Pocket** e **conteúdos patrocinados**.



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**Apenas HTTPS




- Ativar **"Modo HTTPS apenas em todas as janelas "**.


![Configuration DNS over HTTPS](assets/fr/09.webp)



**Medição de telemetria e publicidade




- Em "Recolha de dados pelo Firefox", **desmarque tudo**.
- Desativar **"Medidas de publicidade respeitadoras da privacidade "** (PPA).
- Navegação segura**: mantenha-a activada (recomendado). O Firefox verifica os sites em relação a listas de ameaças através de consultas com hash e verificações locais, protegendo contra phishing e malware com um impacto mínimo na privacidade.



**Controlo global de privacidade (opcional)**




- Ativar o **GPC** para assinalar a sua recusa em vender/partilhar dados.



**Motor de pesquisa




- Mudar para **DuckDuckGo**, **Startpage**, **Qwant** ou **Brave Search** (Definições → Pesquisar).



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**Navegação privada




- Janelas privadas (Ctrl/Cmd+Shift+P) para sessões únicas (presentes, contas secundárias...). Evite o modo "sempre privado": as extensões podem ficar inactivas e as excepções de cookies menos úteis.



**Extensões essenciais** (instalar a partir do catálogo oficial)




- uBlock Origin**: bloqueia anúncios e o rastreio atual, leve.
- Privacy Badger**: aprende a bloquear o que o segue; envia Do Not Track / GPC.
- ClearURLs** (opcional): O Firefox (ETP Strict) e o uBO já limpam muito; mantenha-o se ainda vir URLs "sujos" (utm, fbclid).
- Contentores de várias contas Firefox**: **isola cookies/sessões e armazenamento por contentor; multi-contas paralelas; menos rastreio entre sites**. Extensão oficial: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



**Palavras-passe e 2FA




- Utilizar um gestor de palavras-passe dedicado** (Bitwarden, KeePassXC). **Evitar** armazenar palavras-passe no browser. **Ativar a 2FA** sempre que possível.



## Nível 2 - Reforçado (compartimentação e rede)



Objetivo: compartimentar as actividades e reduzir as fugas na rede.



**DNS sobre HTTPS (DoH)**




- Estado por defeito**: Ativado automaticamente em algumas regiões (EUA, Canadá, Rússia, Ucrânia). Noutras regiões, é necessária a ativação manual.
- Configuração**: Definições → Geral → Definições de rede → **Ativar DoH** → **Cloudflare** ou **Quad9** → **Proteção máxima**.
- Proteção máxima = apenas TRR** (sem recurso ao DNS do sistema). Se uma rede corporativa/hotel bloquear, volte a mudar para **Standard** ou desactive o DoH.
- Redundância**: Se já estiver a utilizar uma VPN de confiança com o seu próprio DNS seguro, o DoH pode ser redundante.
- Teste de verificação**: `https://www.dnsleaktest.com/` deve apresentar apenas o fornecedor de DoH selecionado.



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**Compartimentação com contentores e perfis




- Contentores multi-contas**: criar espaços (Pessoal, Trabalho, Finanças, Redes Sociais, Compras, Descartáveis). Configure **"Abrir sempre neste contentor "** para os seus sites recorrentes. Extensão oficial: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- Porquê utilizá-los?
  - Forte isolamento** de cookies/sessões/armazenamento por espaço.
  - Menos rastreio entre sítios**: limitar os gigantes (Facebook, Google).
  - Várias contas simultâneas** no mesmo serviço.
  - Menor risco de CSRF/XSS** entre identidades segmentadas.
  - Sugestão: no mínimo, contentores dedicados para Redes Sociais/Google, Trabalho, Finanças.
- Contentor Facebook** (opcional): uma versão simplificada dedicada ao FB/Instagram.
- Perfis separados**: via `about:profiles` (perfil principal, perfil mínimo "ultra-seguro", perfil de teste). Compartimentação total de dados e extensões.



**Extensões avançadas** (a reservar)




- Cookie AutoDelete**: apaga os cookies de um site assim que o separador é fechado (útil se o Firefox estiver aberto durante muito tempo).
- LocalCDN**: serve as bibliotecas actuais localmente (reduz as chamadas para o Google/Microsoft). Compatibilidade parcial.



**Telemóvel (Android)**




- Firefox Android + uBlock Origin**: proteção semelhante em movimento.



## Nível 3 - Especialista (about:config & Arkenfox)



Objetivo: endurecimento avançado com compromissos aceites. Recomendado num **perfil separado**.



Escolha apenas uma das duas abordagens seguintes:



**Abordagem A - Modificações manuais**: Alguns ajustes específicos através de `about:config` (controlo mais simples e mais preciso)


**Abordagem B - Arkenfox user.js**: Configuração totalmente automatizada (mais complexa, proteção máxima)



➡️ **O Arkenfox já inclui TODAS as alterações do about:config mencionadas abaixo** + centenas de outras. Se escolher o Arkenfox, ignore a secção about:config.



### Abordagem A: Modificações manuais via about:config



Digite `about:config` na barra Address → Aceitar risco.



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- Resistência à recolha de impressões digitais (herdada do navegador Tor)


```text
privacy.resistFingerprinting = true
```


Efeitos: Fuso horário UTC, **letterboxing** (tamanhos de janela padrão), User-Agent/políticas padronizadas, restrições Canvas/WebGL/AudioContext. Mais uniformidade, mas algumas "peculiaridades" (hora deslocada, por vezes um pouco de inglês).





- Desativar WebRTC (evita fugas de IP; quebra o Web visio)


```text
media.peerconnection.enabled = false
```





- Referer plus compatível (predefinição)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


Opção estrita (pode quebrar pagamentos/SSO):


```text
network.http.referer.XOriginPolicy = 2
```





- Limitar as APIs e a especulação


```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```



Regra de ouro: se algo se estragar, voltar à última alteração.



### Abordagem B: Arkenfox user.js (configuração totalmente automatizada)



O projeto **Arkenfox** fornece um ficheiro `user.js` mantido pela comunidade que aplica automaticamente centenas de preferências do Firefox orientadas para a privacidade e segurança. Ao reiniciar, o Firefox lê este ficheiro a partir do seu perfil e aplica estas definições.





- Qual é o objetivo? Partir de uma **base sólida e consistente** sem "clicar em todo o lado"; reduzir os descuidos; poupar tempo.
- O que muda (exemplos): corte de telemetria, cookies/cache/referrer/HTTPS reforçados, **RFP** + letterboxing, **WebRTC desativado**, ajustes DoH/TLS, APIs de conversação limitadas.
- Quando usar: se quiser o Firefox reforçado em 10 minutos e aceitar algumas excepções (DRM/streaming, Web visio, SSO/pagamentos).
- Vantagens: rápido, consistente, **atualizado** (alinhado com ESR), muito bem **documentado** (wiki + comentários), **customizável** através de substituições.
- Limitações: compatibilidade (algumas aplicações Web), conforto (UTC, tamanhos de janela) e um lembrete: **não é o Tor** (não há anonimato na rede).



Instalação (idealmente num **perfil dedicado**)


1. Guardar perfil/favoritos e listar os seus sítios com excepções de cookies.


2. Descarregar `user.js` de `https://github.com/arkenfox/user.js` (versão ESR/estável).


3. Localize a sua pasta de perfis através de `sobre:perfis`:




   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Biblioteca/Apoio a Aplicações/Firefox/Profiles/...`


4. Feche o Firefox e mova `user.js` para a raiz da pasta de perfil.


5. Reiniciar; personalizar através de `about:config` ou de um ficheiro de substituições.



Actualizações




- Siga as versões do Arkenfox (alinhadas com o ESR), substitua o `user.js`, reinicie o Firefox; leia as notas de lançamento.



**Personalização através de substituições



O Arkenfox é deliberadamente restritivo por padrão. Para adaptar certas configurações às suas necessidades (streaming, visio, sites específicos), você pode criar um arquivo `user-overrides.js` na mesma pasta que `user.js`. Este ficheiro permite-lhe "sobrepor" certas preferências do Arkenfox sem modificar o ficheiro principal.



Crie `user-overrides.js` e adicione as suas personalizações:


```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```



Melhores práticas




- Utilize um perfil **"Arkenfox" separado** e mantenha um perfil "normal" para maior conforto.
- Minimize as extensões (uBlock Origin OK) para limitar a superfície de ataque e a exclusividade.
- Adicionar excepções site a site (proteger 🛡️, uBO, NoScript se utilizado) quando necessário.
- Teste após cada alteração: Fugas WebRTC/DNS, Cover Your Tracks, CreepJS.



## Melhores práticas





- Actualizações**: Firefox e extensões actualizados.
- Extensões**: razoáveis e fiáveis; atenção aos resgates "duvidosos".
- Transferências**: cuidado; testar ficheiros sensíveis no VirusTotal.
- Senhas**: **gerenciador dedicado** (Bitwarden, KeePassXC); **2FA** ativado; evitar armazenar no browser.
- Higiene**: confinar o Google/Facebook a contentores; fechar/abrir regularmente para "reiniciar" o contexto.



## Limites e alternativas





- Um navegador reforçado ≠ anonimato da rede: sem **VPN**, o seu IP permanece visível; mesmo com ele, a correlação continua a ser possível.
- Modificar demasiado pode tornar-te **único**. *o *RFP** padroniza; as ferramentas de aleatorização (por exemplo, Chameleon) podem... diferenciá-lo. Teste, compare, ajuste.
- Alternativas/complementos:
 - Navegador Tor: anonimato de rede através do Tor; mais lento. Veja o nosso guia completo de instalação e configuração**:



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Navegador Mullvad: "Tor sem Tor", para ser combinado com VPN; pegada padronizada. Descobre como o instalar no nosso tutorial dedicado**:



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- Combinações recomendadas: Firefox (Nível 2) + VPN para utilização diária; Tor/Mullvad para actividades sensíveis; perfis separados para compartimentação.



## Conclusão



Ao seguir este guia passo-a-passo, transformou o Firefox num verdadeiro baluarte contra a vigilância digital. Desde definições essenciais de Nível 1 a configurações avançadas do Arkenfox, cada alteração reforça a sua privacidade sem comprometer a sua experiência de navegação.



**A sua privacidade está agora melhor protegida**: rastreadores de anúncios bloqueados, cookies compartimentados, fugas de IP Address neutralizadas, telemetria desactivada. O Firefox já não é apenas um navegador, mas uma ferramenta de resistência digital adaptada às suas necessidades.



**Lembre-se: a confidencialidade nunca é um dado adquirido. Teste a sua proteção regularmente, actualize as suas definições e não hesite em ajustar a sua configuração à medida que os seus hábitos mudam. O seu anonimato online depende tanto das suas ferramentas como das suas práticas.



## Recursos



### Plan ₿ Network




- SCU 202 - Melhorar a sua segurança digital pessoal: Para saber mais sobre os conceitos de segurança digital abordados neste tutorial**



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Documentação do Mozilla




- [Proteção Avançada de Rastreio](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Guia oficial da proteção de rastreio melhorada
- [Particionamento de estados](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Documentação técnica sobre particionamento de estados
- [MDN Web Security](https://developer.mozilla.org/docs/Web/Security): Referência completa sobre segurança na web



### Arkenfox




- [Wiki e guia de instalação](https://github.com/arkenfox/user.js/wiki): Documentação completa do projeto Arkenfox
- [Depósito e lançamentos](https://github.com/arkenfox/user.js): Descarregar o ficheiro user.js e acompanhar as actualizações



### Guias e comunidades




- [PrivacyGuides - Browsers de ambiente de trabalho](https://www.privacyguides.org/en/desktop-browsers/): Recomendações e comparações de browsers
- Reddit**: r/firefox, r/privacy para comentários e apoio
- Fórum PrivacyGuides**: discussões técnicas aprofundadas



### Ferramentas de teste




- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/): Impressão digital e eficácia anti-rastreamento
- [Teste de Fuga de DNS](https://www.dnsleaktest.com/): Teste de vazamento de DNS e eficiência do DoH
- [BrowserLeaks](https://browserleaks.com/): Conjunto completo de testes (WebRTC, Canvas, Fontes, etc.)
- [BadSSL](https://badssl.com/): Testes de validação de certificados SSL/TLS
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): Análise avançada de mais de 50 vectores de impressão digital
- [Cloudflare DNS Test](https://1.1.1.1/help): Verificando se o Cloudflare DoH está funcionando corretamente
