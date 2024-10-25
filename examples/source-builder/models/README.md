# Source to Image - Source Build

Here is a simple way for users to embed models with Triton without having to define a `Dockerfile`.

This example requires a [source builder image](../builder-image/).

This includes the following sources:

- A git repository - **NOT recommended** (for obvious reasons)
- A local folder you can build into a container - **purpose: quick prototyping**

## Folder structure

```sh
.
└── simple
    ├── 1
    │   └── model.graphdef
    └── config.pbtxt
```

TODO: more documentation
