# Source to Image - Source Build

This folder can represent a git repo used for a source build.

Here is a simple way to embed models with Triton without having to define a `Dockerfile`.

This folder offers two examples to provide a model to a source build:

- A git repository - **NOT recommended**
- A local folder you can build into a container - purpose: quick prototyping

## Folder structure

```sh
.
└── simple
    ├── 1
    │   └── model.graphdef
    └── config.pbtxt
```

TODO: more documentation
