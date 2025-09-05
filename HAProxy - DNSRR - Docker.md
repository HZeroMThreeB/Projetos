Consiste basicamente num ***DNS Service Discovery*** com ***HAProxy***, ou seja, o ***Service Discovery*** vai basicamente entregar registros DNS de forma dinâmica, caso você tenha 10 registros DNS, eles precisam ser entregues de forma dinâmica, mesmo que algum seja removido/derrubado ou acrescentado. O sistema precisa se adaptar automaticamente à remoção ou acréscimo de um novo registro, realizando o balanceamento. O ***roteamento*** será feito pelo ***HAProxy***, do tipo ***[[Routing Mesh]]***. O ***HAProxy*** fará contato com o ***DNS*** do ***Docker*** irá coleta-los de forma dinâmica. Quem irá distribuir as requests entre os ***containers*** será o ***HAProxy***, incluindo ***[[HealthCheck]]*** pelo próprio ***HAProxy***.


O ***conjunto de containers*** (serviço) não será feito com ***[[VIP - Virtual IP]]***, mas sim com ***DNS Round Robin*** 


#### Instruções 
Você vai precisar de um `service` com ao menos dois (poderia ser um, mas aí na haveria ***load balance***) containers ***NGINX***, você pode criar com:
`docker service create --network NETWORK_NAME -d --name SERVICE_NAME --replicas 10 --endpoint-mode dnsrr`

Não publicaremos porta alguma para o `service` ***NGINX***, pois estamos utilizando ***==A MESMA REDE DO `SERVICE` HAProxy==***

O `service` ***NGINX*** ***==PRECISA ESTAR ==*** com endpoint-mode em [[DNSRR - DNS Round Robin]], caso esteja como [[VIP - Virtual IP]], o ***HAProxy*** reconhecerá apenas um único endereço IP (afinal, em modo VIP, é disponibilizado apenas um endereço IP para o serviço) e não haverá balanceamento de carga por meio do ***HAProxy***, ele servirá apenas como um "proxy comum" e quem fará o balanceamento de carga será a própria ***Docker Swarm Engine***.


Depois disso, você precisará de um arquivo `haproxy.cfg` dentro do `/etc` configurado adequadamente. Então, basta:
`docker service create --replicas 1 --name haproxy-service --network NETWORK_NAME --publish published=80,target=80,protocol=tcp,mode=ingress --mount type=bind,src=/etc/haproxy/,dst=/etc/haproxy,ro=true --dns=127.0.0.11 HAPROXY_IMAGE_NAME_AND_TAG`

Teremos ***uma réplica*** de nome `haproxy-service`, que fará parte da network `NETWORK_NAME` e o serviço terá a porta 80 publicada por ***redirect*** da porta 80 do ***Docker Host***, específico pro protocolo ***TCP*** e a rede estará em modo ***ingress***. O tipo de `mount` é ***[[Bind Mounting]]***, a origem da montagem será o diretório `/etc/haproxy/` do ***Docker Host*** dentro do `/etc/haproxy` do container. O servidor DNS será ***127.0.0.11*** e a imagem você escolhe.