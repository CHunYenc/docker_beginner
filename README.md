# docker_beginner

1. git clone project
2. cd flask_hello_docker
3. python3 -m venv venv
4. source venv/bin/activate

## docker 小撇步

1. docker images == docker image ls
2. docker run `-d` `--name` redis redis (`-d 背景執行 --name dockername`)

## Linux 小技巧

### awk 搜尋

```
docker container ls -f status=exited | awk '{print$1}' | awk 'NR>1' | xargs docker container rm
```
