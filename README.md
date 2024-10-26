# Nvidia Triton for OpenShift Source to Image (s2i)

This repo shows how to package a ML model with a Nvidia Triton server container.

## Quickstart

> [!NOTE]
> In this example Triton server is configured to serve models from:
>
> `/models`

### Run Triton - Use an Init Container to setup model

```sh
oc apply -k gitops/overlays/triton-init
```

### Run Triton - Load models from S3 bucket at runtime

> [!NOTE]
> Modify `triton-s3-models` secret with s3 credentials

```sh
oc apply -k gitops/overlays/triton-s3
```

### Run Triton - Polling mode (PVC storage)

> [!NOTE]
> You can copy models from local storage via `oc cp`
> to a PVC or ephemeral storage
>
> models path: `/models`

```sh
oc apply -k gitops/overlays/triton-only

# get pod name
POD=$(oc get pod -l app=triton-server -o custom-columns=POD:.metadata.name --no-headers)

# copy model into /models
oc cp examples/source-builder/models/simple $POD:/models/
```

### Run Builder Demos

```sh
oc apply -k gitops/
```

## More Info

See [examples](examples) for more details

## Links

- [Triton Walkthrough](https://neuralbits.substack.com/p/how-to-use-nvidia-triton-server-the)
