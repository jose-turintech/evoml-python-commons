## Useful scripts

- [Makefile](../Makefile): This file defines a set of `global` tasks to be executed using the `make` utility.

    ```shell
    (env-py38) user@pc:~/evoml-python-commons$ make
     Usage: make <task>
       task options:
            help                           This help.
            clean-dist                     Remove 'dist' folder.
            clean-build                    Remove construction artifacts, except 'dist' folder.
            clean-pyc                      Remove Python file artifacts.
            lint                           Check style with flake8 and pylint.
            test                           Run tests quickly with the default Python.
            type-check                     Run type checking using mypy.
            format-check                   Run format checks using black.
            format-apply                   Apply the black format to all the code.
            check-all                      Run all clean code checks.
            check-all-file                 Run all clean code checks and save the result to a file.
            req-install                    Install all the requirements in the activated local environment.
            req-install-prod               Install the production required libraries in the activated local environment.
            req-remove                     Uninstall all the libraries installed in the Python environment.
            req-clean                      Remove all items from the pip cache.
            package                        Package the library as a .whl file.
    ```

- [Makefile](../setup/Makefile): Tasks related to the `setup`.

    ```shell
    (env-py38) user@pc:~/evoml-python-commons/setup$ make
     Usage: make <task>
       task options:
            help                           This help.
            install-req-prod               Install the production required libraries in the activated local environment.
            install-req                    Install all the requirements in the activated local environment.
            remove-req                     Uninstall all the libraries installed in the Python environment.
            cache-purge                    Remove all items from the pip cache.
    ```
