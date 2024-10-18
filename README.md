# Customize Nvidia Triton for OpenShift Source to Image (s2i) builds

## Builder Images

Benefits of Source to Image / Builder Images:

- Use a secure base container image that has all the security policies built in (ex: run as non root user)
- Only focus on the code you are developing
- Script in files, not `Dockerfile`

## Source to Image Simplified

Customize Source Builds (s2i) in git via:

- `.s2i/bin/assemble`
- `.s2i/bin/run`

Use `assemble` when you **DO NOT** need `root` for commands.

Use `run` as your `ENTRYPOINT`

This allows you to customize your container via whatever scripting method you prefer (by default it is `bash`).

Move the mess of `ENTRYPOINT` scripts and `Dockerfile` (non root) `RUN` lines to `.s2i/bin/run` or `.s2i/bin/assemble` .

Move `ENV` lines to `.s2i/environment`.

See [builder-image/s2i/bin](builder-image/s2i/bin)

## Links

- [Source to Image - OpenShift Docs](https://docs.openshift.com/container-platform/4.14/openshift_images/using_images/using-s21-images.html)
- [Source to Image - Python](https://docs.openshift.com/container-platform/4.17/openshift_images/using_images/using-s21-images.html)
- [Source to Image - GitHub](https://github.com/openshift/source-to-image)
