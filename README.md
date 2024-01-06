Mock RPM Action
===

This GitHub Action provides a friendly interface for building RPMs using Mock.

For building source RPMs (SRPMs) please see the [`jw3/mock-srpm`](https://github.com/jw3/mock-srpm) action.

## Example workflow

```yaml
name: build
on: [push, pull_request]

jobs:
  rpm:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: jw3/mock-srpm@v0
        with:
          chroot: fedora-39-x86_64
          spec: test/simple/simple.spec
      - uses: jw3/mock-rpm@v0
        with:
          chroot: fedora-39-x86_64
          srpm: simple-*.src.rpm
```

## Inputs

| Name           | Required | Default | Description                                                                                                     |
|----------------|----------|---------|-----------------------------------------------------------------------------------------------------------------|
| **chroot**     | Y        |         | Mock chroot id ([_list_](https://github.com/rpm-software-management/mock/tree/main/mock-core-configs/etc/mock)) |
| **srpm**       | Y        |         | Path to the src rpm                                                                                             |
| **result-dir** | Y        | .       | Path to write rpmbuild outputs                                                                                  |
| debug          | N        | true    | Show rpmbuild logs on success (auto on-fail)                                                                    |




## About Mock

Mock is used by the Fedora Build system to populate a chroot environment, which is then used in building a source-RPM (SRPM). It can be used for long-term management of a chroot environment, but generally a chroot is populated (using DNF), an SRPM is built in the chroot to generate binary RPMs, and the chroot is then discarded.

https://github.com/rpm-software-management/mock

## License

MIT
