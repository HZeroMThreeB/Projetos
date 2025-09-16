Nesse projeto, nosso objetivo será o mesmo do HAProxy - DNSRR - Docker, mas não será realizado da mesma maneira. Na nossa estrutura com servidor DNS, é ele que resolverá os IPs dos NODES e fará o balanceamento das requisições entre os nodes. Ao mesmo tempo, cada node também vai realizar o seu próprio balanceamento. 


Falando num contexto de ambiente ***on-premisses***, teremos um domínio registrado num DNS (que será o Bind9); a ideia é que esse mesmo domínio retorne o endereço IP dos nodes que servem o website, sabendo que utilizaremos Routing Mesh, temos uma porta 80 (ou qualquer outra que você queira) aberta em todos os nodes que estiverem servindo esse website, portanto, o DNS irá escolher os endereços IP de forma aleatória, usando DNSRR - DNS Round Robin.  Ao encontrar o IP, o servidor DNS fará um ***GET /*** na porta escolhida para servir o website no NODE, chegará ao Routing Mesh e encontrará o container do nginx.


Usando como teste a imagem ***ubuntu:bionic***, quando já tivermos conferido o ***Dockerfile*** e os demais arquivos de configuração, basta executar o ***bind9*** dentro do container já ativo:
`docker exec -d CONTAINER_ID /etc/init.d/Bind9 start` 

***O comando pode mudar, isso vai depender da distro utilizada***.

Ao entrar no container com:
`docker exec -it CONTAINER_ID /bin/bash`

Você verá que a porta ***53 está em uso***, ou seja, o bind9 está ativo.



***RESUMINDO:***
O cliente faz a request ao servidor DNS, e esse, por sua vez, realiza um balanceamento entre os IPS já existentes que redirecionam para aquele mesmo domínio. A partir do momento em que o DNS escolhe um IP (node), ele realiza o envio e o IP (node) faz um outro balanceamento entre os outros nodes da rede. O serviço utilizado como container dentro dos nodes foi o ***Nginx***.