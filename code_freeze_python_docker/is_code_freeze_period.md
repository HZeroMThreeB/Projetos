No nosso contexto, teremos um arquivo ***docker-compose.yml*** para realizar o setup dos nossos 3 containers: 
- ***gitlab*** - sendo uma instância local
- ***gitlab-runner*** - utilizaremos os runners do tipo "docker"
- ***dind*** - Docker in Docker

A estrutura consiste basicamente no container ***gitlab*** gerenciando tudo por meio de uma pipeline. A partir do momento em que a pipeline for iniciada, nosso ***gitlab*** fará contato com o container rodando o ***gitlab-runner***, que por sua vez fará contato com o container do ***dind***, por meio da porta ***2376***. A vantagem de utilizar o ***dind***, além de um nível a mais de isolamento, é justamente sobre o fato de que podemos matar/recriar esses runners de acordo com a nossa necessidade e capacidade do hardware.

Basicamente, precisaremos de dois repositórios dentro da nossa plataforma CI/CD (Gitlab neste exemplo). Um repositório (projeto) contendo a nossa aplicação desejada, e outro repositório contendo o código que irá validar o período de ***Code Freezing***.


***SUGESTÃO para ambiente de TESTES:***
- Application repo: aplicação com a nossa pipeline `.gitlab-ci.yml`
- Scripts repo: code freezing script e dependências


Na nossa plataforma de CI/CD, devemos procurar por ***triggers de merge request*** e devemos habilita-los para que um gatilho seja acionado por meio da nossa pipeline e o merge request seja evitado em caso de ***Code Freezing***.


