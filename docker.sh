# !/bin/bash
echo "jefasse tout"
sudo docker container stop test

echo "pull"
sudo docker pull tiangolo/uvicorn-gunicorn-fastapi

echo "runner latopeuh"
sudo docker run -d --name test2 -p 0.0.0.0:80:80 tiangolo/uvicorn-gunicorn-fastapi:latest

echo "coupi"
sudo docker cp main.py test2:app/

echo "restare"
sudo docker restart test2
