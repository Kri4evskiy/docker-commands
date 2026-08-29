# Docker Команды

## Просмотр и информация
* `docker version` — информация о клиенте и сервере (демоне) Docker.
  > 💡 **Подсказка:** вывод разделен на две секции — `Client:` и `Server:`. Если отображается только `Client:` или появляется ошибка подключения (`Cannot connect to the Docker daemon`), значит Docker Server (демон / Docker Desktop) не запущен.
* `docker ps` — показать только запущенные контейнеры
* `docker ps -a` — показать все контейнеры (включая остановленные)
* `docker images` — показать все локальные образы

## Запуск и управление контейнерами
* `docker run -d -it <image>` — запустить контейнер в фоновом интерактивном режиме
* `docker run -d --name <container_name> -p <host_port>:<container_port> <image>` — запустить контейнер с собственным именем и пробросом порта
* `docker stop <container_name/container_id>` — остановить работающий контейнер
* `docker start <container_name/container_id>` — запустить ранее остановленный контейнер
* `docker restart <container_name/container_id>` — перезапустить контейнер

### Флаги запуска (`docker run`):
* `-d` — запуск в фоновом режиме (detach)
* `-p <host_port>:<container_port>` — проброс порта с хоста в контейнер (например, `-p 8080:80`)
* `--name <name>` — задать контейнеру понятное имя вместо случайного
* `-v <volume_name>:<container_path>` — подключить том (volume) для постоянного хранения данных
* `-v <host_path>:<container_path>` — примонтировать локальную папку с хоста (bind mount)
* `-i` — интерактивный режим (оставляет открытым ввод STDIN)
* `-t` — выделение псевдотерминала (TTY)
* `-it` — запуск в интерактивном режиме с консолью (терминалом)

## Логи, доступ и отладка
* `docker logs <container_name/container_id>` — посмотреть логи контейнера
* `docker logs -f <container_name/container_id>` — следить за логами контейнера в реальном времени (stream)
* `docker exec -it <container_name/container_id> bash` (или `sh`) — подключиться к терминалу внутри работающего контейнера

## Инспектирование (Проверка состояния)
* `docker container inspect <container_name/container_id>` — получить подробную JSON-информацию о контейнере (IP, пути, настройки)
* `docker container port <container_name/container_id>` — посмотреть, какие порты контейнера открыты на хосте

## Тома (Volumes)
* `docker volume ls` — показать все созданные тома
* `docker volume create <volume_name>` — создать новый том вручную
* `docker volume inspect <volume_name>` — посмотреть подробную информацию о томе
* `docker volume rm <volume_name>` — удалить конкретный том

## Удаление и очистка

### Удаление конкретных объектов
* `docker rm <container_name/container_id>` — удалить остановленный контейнер
* `docker rm -f <container_name/container_id>` — принудительно остановить и удалить контейнер
* `docker rmi <image_name/image_id>` — удалить конкретный образ

### Очистка неиспользуемого (Prune)
* `docker container prune` — удалить все остановленные контейнеры
* `docker image prune` — удалить все неиспользуемые/висячие (`<none>`) образы
* `docker volume prune` — удалить все неиспользуемые тома
* `docker system prune` — комплексная очистка: остановленные контейнеры, неиспользуемые сети, висячие образы и кэш сборщика
* `docker system prune -a` — то же самое, но с удалением **всех** неиспользуемых образов (даже с тегами)
* `docker system prune --volumes` — очистить всё неиспользуемое, включая тома
