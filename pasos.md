
PASOS para subir swap

1- sudo fallocate -l 4G /swapfile

2 - chmod 600 /swapfile

3 - sudo mkswap /swapfile

4 - swapon /swapfile

5 - sudo apt install vim

6 - sudo vi /etc/fstab  > /swapfile none sw 0 0


para usar docker

1- curl https://get.docker.com > install-docker.sh
2- chmod 775 install-docker.sh
3- sudo ./install-docker.sh

4- sudo usermod -aG docker cardenas.vico

5 https://docs.docker.com/compose/install/

6- installar como en la doc y ejecutar los permisos

instalar git

1 - sudo apt install git
2 - git clone https://github.com/asielcabrera/sanic_angular_mogdb
3 - cd sanic_angular_mogdb 

construir y desplegar con docker-compose

1- docker-compose build 
2- docker-compose up -d 

en una pestanna nueva del navegador 

pues 