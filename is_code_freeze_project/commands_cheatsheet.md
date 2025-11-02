#### Registrar runner
gitlab-runner register --url http://gitlabExternalURL:PORT --executor docker \ 
--description "Runner docker" \ 
--registration-token GITLAB_RUNNER_TOKEN \ 
--docker-extra-hosts "***gitlab_container_name***:***IP***"
