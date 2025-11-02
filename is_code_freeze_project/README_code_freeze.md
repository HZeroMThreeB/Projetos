Tecnologias escolhidas para este projeto:
- ***Python***
- ***Docker***
- ***GitLab CI/CD***

#### Lógica do projeto
Nosso projeto para detecção de períodos de ***code freezing*** irá consistir numa lógica simples, em que utilizamos ***alguma linguagem de programação*** para construção do nosso script, é esse script que realizará a busca em ***alguma base de dados*** (ou banco de dados em si) e irá ***validar se o usuário atual tem permissão*** para transpassar o período de ***code freezing***, ou se ainda estamos no período de ***code freezing***. Na plataforma de ***CI/CD***, vamos utilizar alguns *triggers* para manipulação do fluxo de execução das pipelines, mais precisamente, *triggers* de ***MERGE REQUEST***  e a nossa própria ***pipeline*** que falhará em conformidade com o código de saída(exit code) do ***job de validação de code freezing*** (que fará a execução do nosso script), e para isso precisaremos de opções relacionadas ao ***sucesso de pipelines*** para evitarmos o MERGE (*`pipelines must succeed`* e *`All threads must be resolved`*).


#### Estrutura e Configuração 
Para a estrutura do nosso projeto, utilizaremos um ambiente voltado para o Docker, que consiste em:
- ***GitLab*** container
- ***dind*** - Docker in Docker
- ***GitLab Runner*** Docker

Nossos arquivos de configuração e script são:
- `.gitlab-ci.yml` - arquivo que realizará a construção da nossa pipeline

- `config.yml` - nossa base de dados

- `code_freeze_python.py` - script para validação de usuário e período de code freezing
- `requirements_python.txt` - dependências para o nosso script funcionar corretamente

- `docker-compose.yml` - setup do nosso ambiente Docker


#### Set up
Basta realizarmos um `docker compose up -d` e aguardar pela inicialização do ***container GitLab***, a partir do acesso a ele, podemos organizar o nosso laboratório em *DOIS PROJETOS* (repositórios), sendo um para a nossa aplicação e outro para o nosso ***script de validação***; chamaremos os repositórios de ***my_app*** e ***valida_freeze***.
Os *triggers* de merge devem ser aplicados ao repositório ***my_app***, de modo que também é interessante ocultar o nosso ***TOKEN DE ACESSO GITLAB***, obtido por meio das configurações de *`Access Token`* do GitLab é que será necessário no nosso arquivo `.gitlab-ci.yml`; para ocultar o token, podemos simplesmente utilizar uma variável de ambiente, que pode ser criada por meio das configurações de `CI/CD` do nosso repositório/projeto, e então marcar as opções de *`protect variable`* (que permitirá a exportação dessa variável apenas à pipelines que estejam em execução em branches protegidas.) e *`Masked`* (que irá mascarar a variável nos logs do JOB). Nosso ***TOKEN DE ACESSO GITLAB*** precisará da *`role`* do tipo `Maintainer` e das permissões de *`read_api`* e *`read_repository`*.

Já no ***container Docker runner***, devemos nos atentar a configuração inicial do nosso primeiro ***Runner***, informando, resumidamente: o ***Token*** (obtido na sessão de Runners do GitLab); a ***GitLab URL***; o tipo do runner (***Docker***); e uma flag/configuração `--docker-extra-hosts "CONTAINER_GITLAB_NAME|HOSTNAME:IP"`


##### Organização dos arquivos
Nossos arquivos estarão separados da seguinte maneira:
- `.gitlab-ci.yml` - repositório ***my_app***

- `code_freeze_tester.py` - repositório ***valida_freeze***

- `requirements_python.txt` - depende se você pretende instalar as dependências com `pip install -r file` ou simplesmente `pip install lib_name`, mas tratando-se de uma única lib num container que deve ser efêmero e não há quaisquer preocupações com conflitos de lib fora de ***virtual environments***, basta uma sessão de `script:` para realizar o download dessa lib individual com `pip install lib_name`, no nosso arquivo de pipeline.

- `config.yml` - repositório ***valida_freeze***


#### Considerações finais
A partir do momento em que o ***Docker Runner*** estiver devidamente configurado e realizando comunicação com o container ***GitLab***, você verá o acionamento e execução automática da pipeline, se obter sucesso na saída do nosso comando `curl` contido no `config.yml`, deu tudo certo! 





***NOTA***:
O `docker-compose.yml` foi gerado com base nas entradas descritas para cada imagem dentro do próprio ***Docker HUB***, alguns utilizam ajustes simples para comunicação, mas de resto é tranquilo de achar e remontar.