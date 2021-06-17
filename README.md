## Unifier Application (UApp) for bank accounting

Below will describe the flow of the application

- Import multiple files (currently supported csv files, 
  but there are placeholders for supporting json and xml files)
  
- Parse imported files

- Uniform parsed files

- Unify uniformed files

- export unified files

Unifiers implementation can be found in [unifiers.py](unifier.py) file

Exporters implementation can be found in [exporters.py](exporter.py) file

Application is configuring using [config.py](config.py),
where are defined:

    1. Supported schemes
    2. Uniform_scheme
    3. Mapping rules
        - Mapping functions (amount, date convertion)

In order to run application type

    python main.py
