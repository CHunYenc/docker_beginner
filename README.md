# docker_beginner

1. git clone --recursive git@github.com:CHunYenc/docker_beginner.git
2. cd flask_hello_docker
3. python3 -m venv venv
4. source venv/bin/activate

## 學習順序

1. flask_hello_docker/
2. flask_redis/
3. flask_docker_compose/
4. flask_docker_compose_scaling/
5. voting_app/

## docker 小撇步

1. docker images == docker image ls
2. docker run `-d` `--name` redis redis (`-d 背景執行 --name dockername`)

## docker-compose

1. docker-compose up `默認當前位置的 dock-compose.yaml`
2. docker-compose up -d `-d 可以讓 docker 背景執行`
3. docker-compose -f composefile.yaml up `-f 可以指定其他檔案`
4. docker-compose build

### docker-compose scaling

scaling 相關資料夾 `./docker_beginner/flask_docker_compose_scaling`

超酷, 可以實現附載均衡 ... 指令如下

1. docker-compose up
2. docker-compose scale web=3 `services=num 因為範例 docker-compose.yml's services 叫 web 是我們要啟動的, 一次啟動三個.`
3. docker-compose up --scale web=3
4. docker-compose ps

## Linux 小技巧

### more 查看文件

### awk 搜尋

```
docker container ls -f status=exited | awk '{print$1}' | awk 'NR>1' | xargs docker container rm
```
