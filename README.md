## Unifier Application (UApp) for bank accounting
Application is a solution of the [assessment](https://gist.github.com/Attumm/3927bfab39b32d401dc0a4ca8db995bd)

This repository has 2 branches `master` and `simple`.
- Final solution is in `master` branch, where I implemented Factory Method design pattern
in order to solve the problem.

- There is a simple solution in `simple` branch, which I made at first, then modifying I got master branch

Below will describe the flow of the application `master` 

- Import multiple files (currently supported csv files, 
  but there are placeholders for supporting json and xml files)
  
- Parse imported files

- Uniform parsed files

- Unify uniformed files

- export unified files

Unifiers implementation can be found in [unifiers.py](unifier.py) file

Currently implemented unifiers:
  - CSVUnifier

Exporters implementation can be found in [exporters.py](exporter.py) file

Currently implemented exporters:
  - CSVExporter
  - JSONExporter

Application is configuring using [config.py](config.py),
where are defined:

    1. Supported schemes
    2. Uniform_scheme
    3. Mapping rules
        - Mapping functions (amount, date convertion)

In order to run application type

    python main.py
