---
name: LineageOS
description: Sistema operativo Android gratuito e sem fios para smartphones
---

![cover](assets/cover.webp)



Os sistemas Android convencionais pré-instalados nos nossos smartphones apresentam uma série de problemas bem conhecidos: integração intensiva dos serviços Google que conduzem a um rastreio constante dos dados, aplicações patrocinadas indesejadas (bloatware) impostas pelos fabricantes e o abandono do rastreio de actualizações ao fim de alguns anos, condenando os dispositivos que ainda funcionam à obsolescência programada.



O LineageOS apresenta-se como uma resposta elegante a estes problemas. Produto da comunidade de código aberto e sucessor direto do CyanogenMod (descontinuado no final de 2016), o LineageOS é um sistema operativo móvel gratuito baseado no Android que devolve aos utilizadores o controlo dos seus smartphones. Lançado oficialmente em dezembro de 2016, o projeto conta agora com mais de 4,4 milhões de instalações activas em todo o mundo e suporta centenas de modelos de telemóveis de mais de 20 marcas diferentes.



![lineageos-homepage](assets/fr/01.webp)



*Sítio Web oficial do LineageOS que apresenta o projeto e os seus objectivos*



## O que é o LineageOS?



### Filosofia e objectivos



O LineageOS é um sistema operativo móvel de código aberto baseado no Android Open Source Project (AOSP), desenvolvido por uma vasta comunidade de colaboradores voluntários em todo o mundo. O seu lema não oficial poderia ser "O seu dispositivo, as suas regras": o projeto tem como objetivo prolongar a vida útil dos smartphones, ao mesmo tempo que oferece uma experiência Android simplificada e amiga da privacidade.



O projeto surgiu das cinzas da CyanogenMod, uma das ROMs Android alternativas mais populares da história. Quando a CyanogenMod Inc. fechou as portas em dezembro de 2016, a comunidade mobilizou-se para criar o LineageOS, mantendo o espírito de inovação e a filosofia de código aberto que caracterizou o seu antecessor.



Ao contrário das distribuições Android OEM, o LineageOS não pré-instala quaisquer aplicações Google por defeito e elimina completamente o bloatware. Os utilizadores começam com um sistema minimalista que inclui apenas as aplicações essenciais (telefone, mensagens, câmara, navegador) e são livres de escolher o que querem adicionar mais tarde.



### Impacto e comunidade



As estatísticas oficiais revelam a dimensão do projeto: com mais de 4,4 milhões de instalações activas em 224 países, o LineageOS representa uma das alternativas Android mais adoptadas no mundo. O Brasil lidera com mais de 2 milhões de utilizadores, seguido da China e dos EUA, demonstrando o apelo universal de um Android gratuito e personalizável.




## Principais caraterísticas



### Interface e experiência do utilizador



**Android puro**: O LineageOS oferece uma experiência Android autêntica próxima do AOSP, sem sobreposições de fabricantes ou aplicações supérfluas. O Interface permanece familiar para os utilizadores do Android, oferecendo uma fluidez óptima graças à ausência de bloatware.



**Sem Google por defeito**: Nenhum serviço Google está pré-instalado, por razões legais e éticas. Esta abordagem "sem Google" garante um controlo total sobre os seus dados pessoais e melhora o desempenho, evitando a execução de serviços em segundo plano.



### Personalização e segurança



**Personalização avançada**: O LineageOS desbloqueia muitas opções que não estão disponíveis no Android stock: reconfiguração dos botões de navegação, temas de sistema personalizáveis, perfis de utilização adaptados a diferentes contextos (trabalho, pessoal, jogos).



**Confiança Útil**: Funcionalidade integrada que monitoriza o estado de segurança do seu dispositivo e alerta-o para potenciais ameaças, proporcionando visibilidade em tempo real da segurança do seu sistema.



**Actualizações prolongadas**: A comunidade LineageOS está empenhada em fornecer patches de segurança mensais, permitindo que os dispositivos descontinuados pelos seus fabricantes continuem a receber os mais recentes patches de segurança do Android.



## Dispositivos compatíveis



O LineageOS suporta centenas de dispositivos de mais de 20 fabricantes: Samsung, Xiaomi, OnePlus, Motorola, Sony, Google Pixel, Fairphone e muitos outros. Esta ampla compatibilidade é uma das principais vantagens do projeto em relação a alternativas como o GrapheneOS, que se limitam aos dispositivos Pixel.



![devices-compatibility](assets/fr/02.webp)



*Página de dispositivos compatíveis com o LineageOS com filtros por fabricante*



![google-devices](assets/fr/03.webp)



*Dispositivos Google suportados, incluindo o Pixel 4 (nome de código "flame")*



### Dispositivos populares



De acordo com as estatísticas oficiais, os modelos mais utilizados incluem uma variedade de dispositivos que abrangem diferentes faixas de preço e idade, demonstrando a capacidade do LineageOS para dar nova vida a smartphones mais antigos, bem como para otimizar os mais recentes.



### Pontos cruciais antes da instalação



**Carregador de arranque desbloqueável**: Verifique se o seu fabricante/operador permite o desbloqueio. Algumas marcas, como a Huawei, eliminaram esta possibilidade em modelos recentes, enquanto outras impõem procedimentos específicos.



**Modelo exato**: É crucial descarregar a ROM que corresponde exatamente ao seu dispositivo. Dois modelos com nomes comerciais semelhantes podem diferir tecnicamente (Galaxy S10 vs S10 5G, por exemplo) e exigir imagens diferentes.



**Suporte escalável**: Os dispositivos mais recentes podem não ser suportados imediatamente, uma vez que a portabilidade requer um programador voluntário para tratar deles. Por outro lado, o suporte pode parar se o mantenedor de um dispositivo se retirar do projeto.



## Instalação



### Pré-requisitos essenciais



⚠️ **Leia estas instruções na íntegra antes de começar** para evitar quaisquer problemas!



**Regressar ao firmware de origem (se necessário) :**




- Ferramenta Android Flash**: Utilize a ferramenta oficial da Google [flash.android.com](https://flash.android.com) para restaurar facilmente o seu dispositivo Pixel para o Android original a partir do seu navegador Web (é necessário o Chrome/Edge)
- Alternativa**: Imagens de fábrica manualmente a partir de [developers.google.com/android/images](https://developers.google.com/android/images)



**Testes de pré-requisitos obrigatórios




- Arranque o seu dispositivo pelo menos uma vez** com o sistema de stock original
- Teste todas as funcionalidades**: SMS, chamadas, Wi-Fi, dados móveis
- Importante**: Verifica se consegues enviar/receber SMS e fazer/receber chamadas (incluindo via WiFi e 4G/5G). Se não funcionar no sistema stock, também não funcionará no LineageOS!
- Dispositivos recentes**: Alguns exigem que o VoLTE/VoWiFi seja utilizado pelo menos uma vez no sistema de stock para aprovisionar o IMS



**Preparação do sistema




- Remova todas as contas Google** do seu dispositivo para evitar a proteção contra reposição de fábrica, que pode bloquear a ativação
- Cópia de segurança completa** : O processo irá apagar completamente o seu telemóvel. Cópia de segurança de fotografias, contactos, aplicações e ficheiros importantes



**Ferramentas ADB e Fastboot:** Siga o [guia oficial do LineageOS](https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot) para instalar as ferramentas da plataforma Android SDK. Verifique a instalação com `adb version` e `fastboot --version`.



**Configuração do telefone:**




- Ativar **Opções do programador**: Definições > Acerca de > tocar em "Número de compilação" 7 vezes



![android-version](assets/fr/06.webp)



*Navegue até Definições > Acerca do telefone para ativar o modo de programador*





- Ativar a **depuração USB** nas Opções de Programador
- Ativar **OEM Unlock** (essencial para desbloquear o carregador de arranque)



![developer-options](assets/fr/07.webp)



*Ativar as Opções de Programador, a depuração USB e o desbloqueio OEM*



### Instalação pormenorizada



⚠️ **Estas instruções são específicas do LineageOS 22.2. Siga cada passo com precisão. Não avance se algo falhar!



#### Passo 1: Verificação do firmware



**Firmware necessário**: O seu dispositivo deve ter o Android 13 instalado antes de continuar (para o Pixel 4). O firmware refere-se às imagens específicas do dispositivo incluídas no sistema de stock.



![pixel4-info](assets/fr/04.webp)



*Página oficial do Pixel 4 com ligações de transferência e guias de instalação*



![downloads-page](assets/fr/05.webp)



*Página de descarregamento da compilação do LineageOS e ficheiros*



**Transferências específicas do Pixel 4:**




- Compilar o LineageOS**: [download.lineageos.org/devices/flame/builds](https://download.lineageos.org/devices/flame/builds)
- Ficheiros necessários**: Descarregue os 3 ficheiros necessários a partir desta página (serão utilizados nos passos seguintes):
  - `lineage-22.2-YYYYMMDD-nightly-flame-signed.zip` (ROM principal)
  - dtbo.img` (bolha da árvore de dispositivos de partição)
  - `boot.img` (recuperação do LineageOS)



⚠️ **Importante**: Verifica a versão do Android, não a versão do sistema operativo do fabricante. O facto de estar a utilizar uma ROM personalizada (mesmo o LineageOS) não garante que este requisito seja cumprido.



💡 **Dica**: Em caso de dúvida sobre o seu firmware, volte ao sistema stock antes de continuar!



#### Passo 2: Desbloquear o carregador de arranque



⚠️ **Este passo elimina todos os seus dados!





- Testar a ligação ADB**: Ligue o seu dispositivo através de USB e teste-o com o comando `adb devices` a partir do terminal do seu computador



![adb-devices](assets/fr/08.webp)



*Verificar a ligação ADB com o comando `adb devices`*





- Autorizar a ligação** no seu telemóvel



![usb-debugging-auth](assets/fr/09.webp)



*Depuração USB activada com a impressão digital RSA do computador*





- Arrancar no modo de carregador de arranque** :


```
adb -d reboot bootloader
```


Ou mantenha premido **Volume Down + Power** para desligar o dispositivo





- Verificar a ligação fastboot**:


```
fastboot devices
```



![fastboot-mode](assets/fr/10.webp)



*Comandos Fastboot no terminal para verificar a ligação*



![bootloader-screen](assets/fr/11.webp)



*Ecrã de arranque rápido do Pixel 4 com informações do sistema*





- Desbloquear o carregador de arranque** :


```
fastboot flashing unlock
```


No dispositivo, utilize as teclas de volume para navegar e prima o botão **Power** para selecionar "Desbloquear o carregador de arranque" e confirme a operação



![unlock-bootloader](assets/fr/12.webp)



*Confirmação do desbloqueio do carregador de arranque no dispositivo*



⚠️ **O telemóvel será reiniciado automaticamente** após a confirmação do desbloqueio





- Após o reinício automático**, reativar a depuração USB nas opções do programador




#### Etapa 3: Colocar partições adicionais em flash



⚠️ **Requerido para que a recuperação funcione corretamente**





- Reiniciar o carregador de arranque**: Diminuir volume + Ligar
- Flash** (substitua `/path/to/` pela pasta onde descarregou o ficheiro) :


```
fastboot flash dtbo /chemin/vers/dtbo.img
```



![flash-partitions](assets/fr/13.webp)



*Flash das partições dtbo e boot.img via fastboot*



#### Passo 4: Instalar a recuperação do LineageOS





- Recuperação flash** (substitua `/path/to/` pela pasta onde descarregou o ficheiro) :


```
fastboot flash boot /chemin/vers/boot.img
```




- Reiniciar em recuperação** para verificar



#### Passo 5: Instalar o LineageOS





- Reiniciar em recuperação**: Diminuir volume + Ligar → Modo de recuperação



![recovery-mode](assets/fr/14.webp)



*Interface a partir da recuperação do LineageOS com o menu principal*





- Reposição de fábrica** : Digitar "Reposição de fábrica" → "Formatar dados / reposição de fábrica"



![factory-reset](assets/fr/15.webp)



*Processo de reposição de fábrica na recuperação do LineageOS*





- Regressar ao menu principal**
- Carregamento lateral do LineageOS** :
   - No dispositivo: "Aplicar atualização" → "Aplicar a partir de ADB"
   - No PC: `adb -d sideload /path/to/lineageos.zip`



![apply-update](assets/fr/16.webp)



*Selecione "Apply Update" e depois "Apply from ADB" na recuperação*



![sideload-process](assets/fr/17.webp)



*Instalação do LineageOS em curso através de sideload*



![sideload-terminal](assets/fr/18.webp)



*Comando Sideload no terminal com o progresso da instalação*



💡 **Normal**: O processo pode parar a 47% ou apresentar erros de "Sucesso" - isto é normal!



#### Passo 6: Primeiro arranque





- Reiniciar**: "Reiniciar o sistema agora"
- Primeira inicialização**: Pode demorar até 15 minutos



**Instalação concluída!**



### Pontos de atenção



⚠️ **Aviso**: O LineageOS é fornecido "tal como está", sem garantia. Apesar de fazermos todos os esforços para garantir que tudo funciona, a instalação é feita por sua conta e risco!



**Controlos críticos




- Compatibilidade de firmware**: Certifique-se de que verifica a versão de firmware necessária na página de transferência do seu modelo
- Nunca voltar a bloquear** o carregador de arranque depois de instalar o LineageOS
- Siga as instruções específicas** para o seu dispositivo



## Configuração e aplicações



### Primeiro arranque


Interface simplificado, próximo do Android stock, sem Google. Configuração simples: idioma, Wi-Fi, sem necessidade de conta.



### Aplicações alternativas



**Fontes de aplicação seguras:**



**F-Droid** : A loja de aplicações de código aberto de referência, pré-instalada com o LineageOS para o microG ou descarregável diretamente. O F-Droid oferece apenas software de código aberto que foi verificado e compilado de forma transparente, garantindo a ausência de trackers ou componentes maliciosos.



**Aurora Store**: Cliente anónimo para aceder à Google Play Store sem uma conta Google. O Aurora utiliza contas anónimas partilhadas, permitindo-lhe descarregar as principais aplicações, preservando a sua privacidade.



**Aplicações alternativas essenciais





- Navegação**: Mapas orgânicos (mapas offline baseados no OpenStreetMap)
- Comunicação**: Signal (mensagens encriptadas de ponta a ponta), K-9 Mail (cliente de correio eletrónico gratuito)
- Media**: NewPipe (YouTube sem anúncios e sem rastreio), VLC (leitor multimédia universal)
- Produtividade**: Nextcloud (nuvem auto-hospedada), Simple Calendar (sincronização CalDAV)
- Segurança**: Bitwarden (gestor de palavras-passe), Aegis Authenticator (códigos 2FA)



Estas aplicações, a maioria das quais está disponível através do F-Droid, formam um ecossistema coerente que pode substituir totalmente os serviços Google, oferecendo uma experiência de utilizador moderna e funcional.



## Utilização e manutenção



### Experiência quotidiana



O LineageOS transforma a experiência Android, dando prioridade à fluidez e à capacidade de resposta. O Interface simplificado é particularmente eficaz em dispositivos mais antigos, aos quais é dado um novo sopro de vida, com um desempenho geralmente superior ao das ROMs do fabricante graças à ausência de sobreposições pesadas e processos supérfluos.



As funcionalidades básicas (chamadas, SMS, fotografias, navegação) funcionam sem problemas, enquanto as ferramentas de personalização permitem que o sistema seja ajustado às preferências individuais sem comprometer a estabilidade.



### Sistema de atualização OTA



O LineageOS dispõe de um sistema de atualização Over-The-Air particularmente fácil de utilizar. As novas versões são propostas automaticamente através de notificações e a instalação demora apenas alguns cliques, sem necessidade de intervenção técnica complexa. O processo preserva totalmente os dados e as aplicações instaladas.



Estas actualizações regulares são um trunfo importante, especialmente para os dispositivos que foram descontinuados pelos seus fabricantes, que podem continuar a beneficiar dos mais recentes patches de segurança do Android.



### Melhores práticas recomendadas



**Segurança pós-instalação:**




- Definir um PIN ou uma palavra-passe forte para desbloquear
- Verificar se a encriptação do armazenamento está activada (normalmente por predefinição)
- Instalar um gestor de palavras-passe como o Bitwarden através do F-Droid



**Manutenção preventiva:**




- Actualizações regulares OTA para segurança
- Limitar a instalação de aplicações a fontes fidedignas (F-Droid, Aurora Store)
- Rever periodicamente as permissões concedidas às aplicações
- Os reinícios ocasionais optimizam o desempenho e libertam memória



## Vantagens e limitações



✅ **Benefícios:**




- Privacidade predefinida (sem rastreio do Google)
- Ampla compatibilidade (mais de 300 modelos)
- Desempenho superior (sem bloatware)
- Actualizações alargadas em dispositivos mais antigos



**Limitações:**




- Instalação técnica
- Sem Android Auto/Google Pay
- As aplicações bancárias podem ser problemáticas



## GrapheneOS vs LineageOS: Qual é a diferença?



### Abordagens distintas



*o *GrapheneOS** centra-se exclusivamente na segurança máxima e funciona apenas nos Google Pixels para explorar os seus chips de segurança dedicados. O sistema incorpora numerosas atenuações avançadas contra exploits e reforça consideravelmente a proteção das aplicações.



**O LineageOS** equilibra segurança, privacidade e conveniência no maior número possível de dispositivos. A abordagem é mais pragmática, visando uma compatibilidade alargada em vez de uma segurança absoluta.



### Gerir os serviços Google



**GrapheneOS**: Oferece um sistema opcional de sandbox do Google Play. O Google Play pode ser instalado, mas é executado numa sandbox rigorosa, sem privilégios especiais do sistema. Esta abordagem única torna possível a utilização do ecossistema Google, mantendo um controlo de segurança rigoroso.



**LineageOS**: Permite ao utilizador optar por instalar os serviços Google (GApps), microG (alternativa gratuita) ou permanecer totalmente livre do Google. Máxima flexibilidade para se adaptar às suas necessidades.



### Comparação técnica



| **Aspect** | **GrapheneOS** | **LineageOS** |
|------------|----------------|---------------|
| **Compatibilité** | Pixels uniquement | Centaines d'appareils |
| **Sécurité** | Mitigations avancées | Sécurité AOSP standard |
| **Google Play** | Sandboxé optionnel | Installation classique possible |
| **Installation** | Interface web + USB | Procédure manuelle technique |
| **Philosophie** | Sécurité avant tout | Équilibre et liberté de choix |

### Recomendações de utilização



**Escolha GrapheneOS** se tiver um Pixel, se a segurança máxima for a sua prioridade e se aceitar restrições para uma proteção melhorada.



**Opte pelo LineageOS** se tiver um dispositivo não-Pixel, se estiver à procura de um bom equilíbrio entre privacidade e praticidade ou se quiser ter a liberdade de escolher o seu nível de compromisso com o ecossistema Google.



## Conclusão



O LineageOS oferece uma alternativa madura para recuperar o controlo do seu smartphone Android. Experiência sem compromissos, desempenho ótimo, compatibilidade alargada: a escolha ideal para combinar privacidade e praticidade no dia a dia.



## Recursos



### Documentação oficial




- [Sítio Web oficial do LineageOS](https://lineageos.org)
- [LineageOS Wiki](https://wiki.lineageos.org) - Guias de instalação por modelo
- [LineageOS para microG](https://lineage.microg.org) - Versão com microG integrado



### Comunidade




- [Subreddit r/LineageOS](https://reddit.com/r/LineageOS)
- [Conta Mastodon @LineageOS](https://fosstodon.org/@LineageOS)



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1