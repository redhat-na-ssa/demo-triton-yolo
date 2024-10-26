# Nvidia Triton for OpenShift Source to Image (s2i)

This repo shows how to package a ML model with a Nvidia Triton server container.

## Quickstart

```sh
oc apply -k gitops/
```

Use an Init Container to setup model in Triton

```sh
oc apply -k gitops/overlays/triton-init
```

Run Triton - pull models from S3 bucket

Note: Modify secret with s3 credentials

```sh
oc apply -k gitops/overlays/triton-s3
```

Run Triton in polling mode (PVC storage)

```sh
oc apply -k gitops/overlays/triton-only
```

See [examples](examples) for more info

## Links

- [Triton Walkthrough](https://neuralbits.substack.com/p/how-to-use-nvidia-triton-server-the)
