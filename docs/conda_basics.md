## Set up a Python environment

### Anaconda

Anaconda is an open source software that contains Jupyter, spyder, etc that are used for large data processing, data
analytics, heavy scientific computing.

Anaconda works for R and Python programming language.

Package versions are managed by the package management system conda.

- **Installing Anaconda**: Head over to [anaconda.com](https://www.anaconda.com/products/individual) and install the
  latest version of Anaconda.

### Why do we need to set up a virtual environment?

Like many other languages Python requires a different version for different kind of applications. The application needs
to run on a specific version of the language because it requires a certain dependency that is present in older versions
but changes in newer versions.

Virtual environments makes it easy to ideally separate different applications and avoid problems with different
dependencies.

Using virtual environment we can switch between both applications easily and get them running.

There are multiple ways of creating an environment using virtualenv, venv and conda. Conda command is preferred
interface for managing installations and virtual environments with the **Anaconda** Python distribution.

#### Steps of creating a virtual environment using conda interface

1) Check if conda is installed in your path.
    - Open up a terminal.
    - Type conda -V and press enter.
    - If the conda is successfully installed in your system you should see a similar output.

            user@pc:~$ conda -V
            conda 4.9.2
        
2) Set up the virtual environment.
    - You create a new environment by using: `conda create -y -n [env-name] python=[x.x] `
    - Now replace the `env-name` with the name you want to give to your virtual environment and replace `x.x` with the
      python version you want to use.
    
            user@pc:~$ conda create -y -n env-py38-evoml-python-commons python=3.8
                ...

            # To activate this environment, use
            #
            #     $ conda activate env-py38-evoml-python-commons
            #
            # To deactivate an active environment, use
            #
            #     $ conda deactivate
        
3) Get a list of all my environments Active environment shown with: `conda env list`

            user@pc:~$ conda env list
            # conda environments:
            #
            base             *  /opt/anaconda3
            env-py38-evoml-python-commons      /opt/anaconda3/envs/env-py38-evoml-python-commons
        
4) Activating the virtual environment
    - To activate the virtual environment, enter the given command: `conda activate env-name`
    - Replace your given environment name with `env-name`.
    - When conda environment is activated it modifies the PATH and shell variables points specifically to the isolated
      Python set
        
            user@pc:~$ conda activate env-py38-evoml-python-commons
            (env-py38-evoml-python-commons) user@pc:~$
        
5) Deactivating the virtual environment.
    - To come out of the particular environment type the following command. The settings of the environment will remain
      as it is.
        
            user@pc:~$ conda deactivate
            user@pc:~$
        
6) Deletion of virtual environment.
    - If you no longer require a virtual environment, delete it using the following
      command: `conda env remove -n [env-name]`
    - Replace your environment name with `env-name`
        
            user@pc:~$ conda env remove -n env-py38-evoml-python-commons
        

