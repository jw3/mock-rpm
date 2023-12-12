Mock RPM Build
===

This GitHub Action provides a friendly interface for building RPMs using Fedora Mock.

## Example workflow

```yaml
name: build
on: [push, pull_request]

jobs:
  test:
    name: rpm
    runs-on: ubuntu-latest
    steps:
    - uses: jw3/mock-rpm-action@v1
      with:
        chroot: fedora-39-x86_64
        srpm: simple-0.0.0.fc39.src.rpm
```

## License

MIT
