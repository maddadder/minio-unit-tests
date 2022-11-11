cd /home/alice/git3/minio-unit-tests
python3 -m venv ./env
source env/bin/activate
pip install -r requirements.txt

kubectl port-forward service/minio-neon 9000:80 --namespace neon-system

cd /home/alice/git3/minio-unit-tests
source env/bin/activate
python test_port_forward.py

