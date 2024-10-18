# Customize Nvidia Triton for OpenShift Source to Image (s2i) builds

## Customize s2i via `assemble` or `run`

`#TheEasierWay`

Use `assemble` when you **DO NOT** need `root` for commands.

This allows you to customize your container via whatever scripting method you prefer (by default it is `bash`).

Move the mess of `ENTRYPOINT` scripts and `Dockerfile` (non root) `RUN` lines to `.s2i/bin/run` or `.s2i/bin/assemble` .

Move `ENV` lines to `.s2i/environment`.

See [builder-image/s2i/bin/assemble](builder-image/s2i/bin/assemble)

## Links

- [Source to Image - OpenShift Docs](https://docs.openshift.com/container-platform/4.14/openshift_images/using_images/using-s21-images.html)
- [Source to Image - Python](https://docs.openshift.com/container-platform/4.17/openshift_images/using_images/using-s21-images.html)
- [Source to Image - GitHub](https://github.com/openshift/source-to-image)
