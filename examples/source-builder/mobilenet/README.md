# Source to Image - Custom Scripts

Here is a simple way for users to embed models with Triton without having to define a `Dockerfile`... But still make customizations via scripts.

This example requires a [source builder image](../builder-image/).

The following files are used for scripting:

- `assemble` - defines what happens during a source build process
- `run` - defines what to run; similar to `CMD` or `ENTRYPOINT`
- `environment` - sets environment parameters inside the container

## Folder structure

```sh
.
├── mobilenet
│   ├── 1
│   │   └── metadata
│   ├── 2
│   │   └── metadata
│   ├── 3
│   │   └── metadata
│   └── config.pbtxt
└── .s2i
    ├── bin
    │   ├── assemble
    │   └── run
    └── environment
```

TODO: more documentation
