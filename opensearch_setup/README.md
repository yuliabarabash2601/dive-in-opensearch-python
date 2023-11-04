# Here we describe how to start open search on your local machine.


## Run OpenSearch on your local machine

The file with name docker-compose.yml contains the configuration to start OpenSearch on your local machine.
The file is located in the folder opensearch_setup.
The file contains the following services:
1. opensearch-node
2. opensearch-dashboards

Execute the following command to start OpenSearch on your local machine:

```bash
cd ./opensearch_setup
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

## Setup OpenSearch Index
