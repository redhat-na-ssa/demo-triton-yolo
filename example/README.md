# Source to Image Override Scripts

This folder can represent a git repo used for a source build.

Here is a simple way to embed models with Triton without having to define a `Dockerfile`.

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
