# Changelog

## [0.3.2](https://github.com/ustuehler/py-jpdb/compare/v0.3.1...v0.3.2) (2022-09-28)


### CI/CD Workflows

* rename GitHub Actions workflows for consistency ([8d2c840](https://github.com/ustuehler/py-jpdb/commit/8d2c84033b5a919718b3274b59c8eba8f4250804))


### Documentation

* add CONTRIBUTING.md and update LICENSE, README.md ([ac60e9a](https://github.com/ustuehler/py-jpdb/commit/ac60e9a7faafe23b95d41f6bf1bddd04fbd39e1e))

## [0.3.1](https://github.com/ustuehler/py-jpdb/compare/v0.3.0...v0.3.1) (2022-09-24)


### Bug Fixes

* ensure that due_items returned are always up-to-date ([7d9cbcb](https://github.com/ustuehler/py-jpdb/commit/7d9cbcb6edc65d68b087f2d0cdd6e29af246418f))

## [0.3.0](https://github.com/ustuehler/py-jpdb/compare/v0.2.0...v0.3.0) (2022-09-24)


### Features

* return `Reviews` class from `reviews` property ([de2cf2f](https://github.com/ustuehler/py-jpdb/commit/de2cf2f82ad5ec22e856cacd9fe06962ff646fef))


### CI/CD Workflows

* use Python 3.9 since we now rely on zoneinfo ([9c0539a](https://github.com/ustuehler/py-jpdb/commit/9c0539aef64d77aa8d114c044a874a629ad4d3f2))

## [0.2.0](https://github.com/ustuehler/py-jpdb/compare/v0.1.1...v0.2.0) (2022-09-24)


### Features

* support exporting the review history for all cards ([0c80a0c](https://github.com/ustuehler/py-jpdb/commit/0c80a0ca118db512bf1e707abadcd7823ad027f6))


### Build System

* fix transitive dependencies when using this library ([feab566](https://github.com/ustuehler/py-jpdb/commit/feab5663e022be8376e8dde35b79ce411982b72e))


### Documentation

* add installation and usage examples to README.md ([cc5f0cb](https://github.com/ustuehler/py-jpdb/commit/cc5f0cbe13bd9b9bda410d87be362b90f6e26509))

## [0.1.1](https://github.com/ustuehler/py-jpdb/compare/v0.1.0...v0.1.1) (2022-08-24)


### Documentation

* add link to CHANGELOG.md ([bcb1e64](https://github.com/ustuehler/py-jpdb/commit/bcb1e647b1653ff99bcf60d8a50fcd30d06833ab))

## 0.1.0 (2022-08-24)


### Features

* add validation of login credentials (username & password) ([45c5b46](https://github.com/ustuehler/py-jpdb/commit/45c5b4612c0c18479af00a4d05b5443f08104724))
* get number of due items (vocabulary & Kanji) ([9a0360f](https://github.com/ustuehler/py-jpdb/commit/9a0360f62b3a65a8569fb3cb32edc18e14e3b42b))


### Build System

* add project configuration for Intellij IDE CE ([54e862d](https://github.com/ustuehler/py-jpdb/commit/54e862d3945cc3852ba43992a30d4a17773750ce))


### CI/CD Workflows

* add GitHub test and release workflows ([e6f9b24](https://github.com/ustuehler/py-jpdb/commit/e6f9b248177eaba3744d5d52ed9f4b6193548c3e))
* expand list of changelog-relevant commit types ([7f74a00](https://github.com/ustuehler/py-jpdb/commit/7f74a00b93c86c38ddb01197816f9961eee1ebfe))
* fix integration test job in CI workflow ([0b6b44b](https://github.com/ustuehler/py-jpdb/commit/0b6b44b231e28034a6f7a16badbc384ef45c97fe))
