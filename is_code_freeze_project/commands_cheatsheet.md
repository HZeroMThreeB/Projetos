#### Registrar runner
`gitlab-runner register --url http://gitlabExternalURL:PORT --esxecutor docker \ 
--description "Runner docker" \ 
--registration-token GITLAB_RUNNER_TOKEN \ 
--docker-extra-hosts "GITLAB_CONTAINER_NAME:IP"`
