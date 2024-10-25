# Builder Image

A builder image is a special container that is structured in a way to take basic content to build and deploy a container.

See the following:

- [Source to Image - CLI](https://github.com/openshift/source-to-image)
- [Source to Image - OpenShift](https://docs.openshift.com/container-platform/4.16/openshift_images/using_images/using-s21-images.html)

## Crash course in Source to Image

Customize Source Builds (s2i) in git via:

- `.s2i/bin/assemble`
- `.s2i/bin/run`
- `.s2i/environment`

Use `assemble` when you **DO NOT** need `root` for commands.

Use `run` as your `ENTRYPOINT`

This allows you to customize your container via whatever scripting method you prefer (by default it is `bash`).

Move the mess of `ENTRYPOINT` scripts and `Dockerfile` (non root) `RUN` lines to `.s2i/bin/run` or `.s2i/bin/assemble`.

Move `ENV` lines to `.s2i/environment`.

This project consists of how to create a container with a model for serving on triton