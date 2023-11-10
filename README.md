# dive-in-opensearch-python

# Quick Setup


## Run OpenSearch on your local machine

The file with name docker-compose.yml contains the configuration to start OpenSearch on your local machine.

The file is located in the folder opensearch_setup folder.

The file contains the following services:
1. opensearch-node
2. opensearch-dashboards

Execute the following command to start OpenSearch on your local machine:

```bash
cd opensearch_setup/
docker-compose up
```

The command will start OpenSearch and OpenSearch Dashboards on your local machine.
To access and test OpenSearch Dashboards, open the following URL in your browser: http://localhost:5601.

Credentials for OpenSearch Dashboards:

login: admin
password: admin

To stop OpenSearch and OpenSearch Dashboards, execute the following command:

```bash
docker-compose down
```
## Dataset
You can find the netflix.csv data on `backend/helpers/netflix.csv`.

## Setup OpenSearch Index

Install dependencies:

```bash
pip3 install -r requirements.txt
```

You can send documents to your opensearch cluster using the following script:

```python
python3 send_data_to_opensarch.py
```

If you want to visualize the documents on your OpenSearch Dashboards, you need to create an index pattern in your OpenSearch Dshboard.


