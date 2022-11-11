cd /home/alice/git3/minio-unit-tests
python3 -m venv ./env
source env/bin/activate
pip install -r requirements.txt

kubectl apply -f virtual-service.yaml --namespace neon-system

cd /home/alice/git3/minio-unit-tests
source env/bin/activate
python test_via_istio.py

kubectl delete -f virtual-service.yaml --namespace neon-system
