# Cities API

A tiny API to get and post cities.

## Installation

You need [Python 3.8](https://www.python.org/downloads/release/python-3813/), [Pipenv](https://pypi.org/project/pipenv/) and [Docker compose](https://docs.docker.com/compose/) to run this project.

Then, run the following commands.

```bash
$ cd path/to/cities/api
$ pipenv install
```

## Run Locally

You can run the project with the following command.

```bash
$ cd path/to/cities/api
$ ./scripts/run-dev
```

And you can test it with these ones.

```bash
$ cd path/to/cities/api
$ ./scripts/run-test
```

## Deployment

Before being able to deploy the project, you have to enable an ingress controller. If you're using Minikube, you can run the following command:

```bash
$ minkube addons enable ingress
```

### Automatically

You can trigger the deployment of a new version by pushing a new git tag.

```bash
$ git tag -a <version> -m <version name>
$ git push origin <version>
```

### By hand

You can deploy the project with [Kubernetes](https://kubernetes.io/) and [Helm](https://helm.sh/).

After creating a new k8s cluster, run the following commands.

```bash
$ cd path/to/cities/api
$ helm install db db/
$ helm install api api/
$ helm install prometheus prometheus/
$ helm install grafana grafana/
```

You will be able to check that everything is available by running the following commands:

```bash
$ curl -H "Host: api.localhost" http://<ingress-host>/city
$ curl -H "Host: grafana.localhost" http://<ingress-host>
```

> If the grafana is working, you'll get a 503 error page. Don't worry, it's working.

> If you're using Minikube, you can get `ingress-host` with the following command: `minikube service list`

Here is a schema of what you will obtain.

![Cluster schema](https://github.com/WoodenMaiden/CICD-TP/blob/master/doc/k8s-schema.png?raw=true)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file.

If you are planning to deploy this project with k8s, don't forget to change environment variables in `api/templates/deployment.yaml` and `db/templates/deployment.yaml`.

### API

**`CITY_API_DB_NAME`**

The name of the postgres database to store and load data.

**`CITY_API_DB_URL`**

The url of the database.

**`CITY_API_DB_USER`**

The user to login with to the database.

**`CITY_API_DB_PWD`**

The password to login with to the database.

**`CITY_API_ADDR`**

The host to listen on.

### DB

**`POSTGRES_USER`**

Same as `CITY_API_DB_USER`.

**`POSTGRES_PASSWORD`**

Same as `CITY_API_DB_PWD`.

**`POSTGRES_DB`**

Same as `CITY_API_DB_NAME`.
