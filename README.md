<p align="center">
    <img alt="Krypton Actions Logo" src="https://raw.githubusercontent.com/silverbackhq/krypton/master/assets/images/logo.png" height="100" />
    <h3 align="center">Krypton Actions</h3>
    <p align="center">Open Source Workflow Automation</p>
    <p align="center">
        <a href="https://travis-ci.org/Clivern/krypton-actions"><img src="https://travis-ci.org/Clivern/krypton-actions.svg?branch=master"></a>
        <a href="https://github.com/Clivern/krypton-actions/releases"><img src="https://img.shields.io/badge/Version-0.4.1-red.svg"></a>
        <a href="https://github.com/Clivern/krypton-actions/blob/master/LICENSE"><img src="https://img.shields.io/badge/LICENSE-Apache--2.0-orange.svg"></a>
    </p>
</p>


## Documentation

#### Krypton as a Github Action:

To install krypton github action, add the following to your `workflow.yml`.

```yml
name: workflow_name

on:
    # may vary based on modules enabled

jobs:
  krypton-actions:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2 # required to clone your code
      - name: krypton-actions
        uses: clivern/krypton-actions@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Then add `.krypton.yml` to your repository root directory. This file to configure the enabled krypton modules and their settings. It should look like:

```yml
modules:
  - "first_issue"
```


## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, Krypton Actions is maintained under the [Semantic Versioning guidelines](https://semver.org/) and release process is predictable and business-friendly.

See the [Releases section of our GitHub project](https://github.com/clivern/krypton-actions/releases) for changelogs for each release version of Krypton Actions. It contains summaries of the most noteworthy changes made in each release.


## Bug tracker

If you have any suggestions, bug reports, or annoyances please report them to our issue tracker at https://github.com/clivern/krypton-actions/issues


## Security Issues

If you discover a security vulnerability within Krypton Actions, please send an email to [hello@clivern.com](mailto:hello@clivern.com)


## Contributing

We are an open source, community-driven project so please feel free to join us. see the [contributing guidelines](CONTRIBUTING.md) for more details.


## License

© 2019, Clivern. Released under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

**Krypton-Actions** is authored and maintained by [@Clivern](https://github.com/clivern).
