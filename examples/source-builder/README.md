# s2i Triton model serving

## Why Builder Images

Benefits of Source to Image / Builder Images:

- Use a secure base container image that has all the security policies built in (ex: run as non root user)
- Only focus on the code you are developing
- Script in files, not `Dockerfile`

## Folder Info

Triton model folder structure:

```sh
models (provide this dir as source / MODEL_REPOSITORY )
└─ [ model name ]
    └─ 1 (version)
        └── model.savedmodel
            ├── saved_model.pb
```

## Usage

NOTE: `oc new-app` commands will error before the builder image is built; be patient.

### Build S2I Image

Setup new project

```sh
# new project
NAMESPACE=demo-triton-cli

oc new-project "${NAMESPACE}" \
  --description "A model serving example" \
  --display-name "Demo - Triton (cli)"
```

Build s2i image in Openshift

```sh
oc new-build \
  -n "${NAMESPACE}" \
  https://github.com/codekow/s2i-triton.git#main \
  --name triton-builder \
  --context-dir /examples/source-builder/builder-image \
  --strategy docker
```

### Use S2I Image to serve models

Deploy model via git repo

```sh
APP_NAME=triton-server-simple
APP_LABEL="app.kubernetes.io/part-of=${APP_NAME}"

oc new-app \
  -n "${NAMESPACE}" \
  triton-builder:latest~https://github.com/codekow/s2i-triton.git#main \
  --name "${APP_NAME}" \
  -l "${APP_LABEL}" \
  --strategy source \
  --context-dir /examples/source-builder/models
```

Deploy model via git repo .s2i

```sh
APP_NAME=triton-server-custom
APP_LABEL="app.kubernetes.io/part-of=${APP_NAME}"

oc new-app \
  -n "${NAMESPACE}" \
  triton-builder:latest~https://github.com/codekow/s2i-triton.git#main \
  --name "${APP_NAME}" \
  -l "${APP_LABEL}" \
  --strategy source \
  --context-dir /examples/source-builder/mobilenet
```

Deploy model via s3

```sh
APP_NAME=triton-server-s3
APP_LABEL="app.kubernetes.io/part-of=${APP_NAME}"

oc new-app \
  -n "${NAMESPACE}" \
  triton-builder:latest \
  --name "${APP_NAME}" \
  -l "${APP_LABEL}"

oc set env \
  -n "${NAMESPACE}" \
  "deployment/${APP_NAME}" \
  AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION} \
  AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} \
  AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} \
  MODEL_REPOSITORY=s3://bucket/triton/models
```

Deploy model via local folder

```sh
APP_NAME=triton-server-local
APP_LABEL="app.kubernetes.io/part-of=${APP_NAME}"

# configure new build config
oc new-build \
  -n "${NAMESPACE}" \
  --name "${APP_NAME}" \
  -l "${APP_LABEL}" \
  --image-stream triton-builder:latest \
  --strategy source \
  --binary \
  --context-dir models
```

```sh
# start build from local folder
oc start-build \
  -n "${NAMESPACE}" \
  "${APP_NAME}" \
  --follow \
  --from-dir models
```

```sh
# deploy from model image
oc new-app \
  -n "${NAMESPACE}" \
  "${APP_NAME}" \
  -l "${APP_LABEL}" \
  --allow-missing-imagestream-tags

# fix: crashing on gpu nodes
oc set env deployment "${APP_NAME}" \
  -n "${NAMESPACE}" \
  --env TF_GPU_ALLOCATOR=cuda_malloc_async
```

Expose API / model server - Route

```sh
oc expose service \
  -n "${NAMESPACE}" \
  "${APP_NAME}" \
  -l "${APP_LABEL}" \
  --port 8000 \
  --overrides='{"spec":{"tls":{"termination":"edge"}}}'
```

Expose metrics  - Route (optional)

```sh
oc expose service \
  -n "${NAMESPACE}" \
  "${APP_NAME}" \
  --name "${APP_NAME}-metrics" \
  --port 8002 \
  --overrides='{"spec":{"tls":{"termination":"edge"}}}'

HOST=$(oc get route "${APP_NAME}-metric" --template={{.spec.host}})
curl -s https://${HOST}/metrics | python -m json.tool
```

Test model server / metrics

```sh
APP_NAME=triton-server

# test via route
HOST=$(oc get route "${APP_NAME}" --template={{.spec.host}})

curl -s https://${HOST}/v2 | python -m json.tool
curl -s -X POST https://${HOST}/v2/repository/index | python -m json.tool
curl -s https://${HOST}/v2/models/simple | python -m json.tool
```

```sh
# https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_model_repository.html#index
curl -X POST -H "Content-Type: application/json" \
     -d @scripts/model.json \
     ${HOST}:8000/v2/models/simple/infer | python -m json.tool
```

```json
{
    "name": "simple",
    "versions": [
        "1"
    ],
    "platform": "tensorflow_graphdef",
    "inputs": [
        {
            "name": "INPUT0",
            "datatype": "INT32",
            "shape": [
                -1,
                16
            ]
        },
        {
            "name": "INPUT1",
            "datatype": "INT32",
            "shape": [
                -1,
                16
            ]
        }
    ],
    "outputs": [
        {
            "name": "OUTPUT0",
            "datatype": "INT32",
            "shape": [
                -1,
                16
            ]
        },
        {
            "name": "OUTPUT1",
            "datatype": "INT32",
            "shape": [
                -1,
                16
            ]
        }
    ]
}
```

```sh
# test via localhost
oc get pods

oc exec deploy/${APP_NAME} -- curl -s localhost:8000/metrics
oc exec deploy/${APP_NAME} -- curl -s localhost:8000/v2
oc exec deploy/${APP_NAME} -- curl -s localhost:8000/v2/repository/index
oc exec deploy/${APP_NAME} -- curl -s localhost:8000/v2/models/simple
oc exec deploy/${APP_NAME} -- curl -s localhost:8000/v2/models/simple/config
```

## Links

- https://github.com/redhat-na-ssa/s2i-patch
- https://github.com/triton-inference-server/server
- https://github.com/openshift/source-to-image
- https://github.com/sclorg/container-common-scripts
