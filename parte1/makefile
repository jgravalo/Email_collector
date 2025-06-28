all:
	docker-compose up --build -d

down:
	docker-compose down

ls:
#	docker-compose ps -q
# List all containers
	docker ps -a
# List all images
	docker images
# List all volumes
	docker volume ls
# List all networks
	docker network ls

clean: down
	# Remove all stopped containers, networks not used by at least one container, all dangling images, and all build cache
	docker system prune -f
	# Remove all unused volumes
	docker volume prune -f
	# Remove all stopped containers
	docker container prune -f
	# Remove all unused networks
	docker network prune -f
	# Remove all dangling images
	docker image prune -f
#	rm -rf vault/data/sys/token/id/*
#	rm -rf vault/data/sys/token/accessor/*
#	rm -rf vault/data/sys/expire/id/auth/approle/login/*
	@echo "Deteniendo y eliminando contenedores..."
	@if [ ! -z "$$(docker ps -aq)" ]; then \
		docker stop $$(docker ps -aq); \
		docker rm $$(docker ps -aq); \
	fi
	@echo "Eliminando imágenes..."
	@docker rmi -f $$(docker images -aq) 2>/dev/null || true
	@echo "Eliminando volúmenes..."
	@docker volume rm $$(docker volume ls -q) 2>/dev/null || true
	@echo "Eliminando redes personalizadas..."
	@docker network rm $$(docker network ls -q --filter type=custom) 2>/dev/null || true
#	docker-compose rm -f

re: clean all

.PHONY: all down ls clean re