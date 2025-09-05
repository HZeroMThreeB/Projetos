Nosso projeto consiste num ***servidor de e-mail*** [[Postfix]] para manipular o protocolo [[SMTP - Simple Mail Transfer Protocol]], que será acessado por meio do cliente ***Mozilla Thunderbird***. Quem irá permitir o acesso às mailboxes dos usuários será o protocolo [[IMAP - Internet Message Access Protocol]], que será manipulado por meio do [[Dovecot - Insecure]].

As recomendações são para que o servidor ***IMAP*** esteja na mesma máquina do servidor ***SMTP***, já que a separação deles, se não for muito bem tratada e num caso bem específico, pode resultar em latência no serviço.

`SMTP/Postfix` - é o servidor de e-mail, cujo acesso será feito por meio da porta 25

`IMAP/Dovecot` - é o servidor que nos permite acesso às inboxes dos usuários, por meio da porta 143

`Mozilla Thunderbird` - é o cliente SMTP, que fará envio de e-mails utilizando também o protocolo ***SMTP*** e acessará às inboxes por meio do ***IMAP***


Ao chegar à ==etapa de configuração== do ***Mozilla Thunderbird***, basta adicionar as credenciais para login e ele deve detectar as suas configurações automaticamente.