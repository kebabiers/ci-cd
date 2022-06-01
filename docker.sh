# !/bin/bash
echo "jefasse tout"
sudo docker stop test2
sudo docker container rm test2

echo "pull"
sudo docker pull tiangolo/uvicorn-gunicorn-fastapi

sudo docker run -d --name test2 -v /:/app tiangolo/uvicorn-gunicorn-fastapi

#echo "run run run"
#sudo docker run -d --name test2 -p 0.0.0.0:80:80 -v /:/app tiangolo/uvicorn-gunicorn-fastapi

#echo "install dependencies"
#sudo docker exec test2 /usr/local/bin/pip3 install "fastapi[all]" 

#echo "coupi"
#sudo docker cp main.py test2:app/

#echo "stoupi"
#sudo docker stop test2

#echo "runner latopeuh"
#sudo docker run -d --name test2 -p 0.0.0.0:80:80 -v ./:/app
#sudo docker start test2

#echo "restare"
#sudo docker restart test2
