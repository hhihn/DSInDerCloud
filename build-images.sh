#!/bin/bash
set -e

echo "Minikube Docker Environment setzen"
eval $(minikube docker-env)

echo "Model Service Image bauen"
docker build -t model-service:latest model_service

echo "Images erfolgreich gebaut"