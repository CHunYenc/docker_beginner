# docker_beginner

1. git clone project
2. cd flask_hello_docker
3. python3 -m venv venv
4. source venv/bin/activate

## docker 小撇步

1. docker images == docker image ls
2. docker run `-d` `--name` redis redis (`-d 背景執行 --name dockername`)
3. docker-compose up 默認當前位置的 dock-compose.yaml
4. docker-compose up -d -d 可以讓 docker 背景執行
5. docker-compose -f composefile.yaml up -f 可以指定其他檔案
6. docker-compose build

## Linux 小技巧

### more 查看文件

### awk 搜尋

```
docker container ls -f status=exited | awk '{print$1}' | awk 'NR>1' | xargs docker container rm
```
