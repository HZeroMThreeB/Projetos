Este projeto consiste no monitoramento de recursos de um sistema operacional. Utilizaremos containers para isolar as aplicações e facilitar o gerenciamento.

Nossa stack de monitoramento é composta por:
- ***CAdvisor***(container) - Realiza a coleta de métricas do sistema operacional e alimenta o ***Prometheus***.

- ***Prometheus***(container) - Representa o núcleo da nossa stack, já que é ele quem irá realizar o scrapping das métricas fornecidas pelo ***CAdvisor***, armazená-las em seu próprio ***TSDB*** (Time Series Database) e enviar para o ***AlertManager***.

- ***AlertManager***(container) - É o responsável pelo management e routing dos nossos alertas, é por meio dele que faremos o roteamento para o ***webhook***.

- ***Python Webhook***(container/Dockerfile) - Recebe os alertas e permite a livre manipulação deles. É uma simples rota `/alerts` que recebe um `HTTP POST` contendo um ***JSON*** e armazena num arquivo dentro de um diretório chamado ***dump_data***. O diretório ***dump_data*** estará em bind mountig com o diretório (criado automaticamente) ***appJsonStore*** do nosso Docker Host.


