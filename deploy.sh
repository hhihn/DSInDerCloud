#!/bin/bash
set -e

echo "Beende alle Pods und Services"
kubectl delete all --all
echo "Deployment gestartet"
kubectl apply -f kubernetes

echo "Pods:"
kubectl get pods

echo "Services"
kubectl get services

echo "Jobs"
kubectl get jobs