# A cookiecutter for cloud driven data-science

**TLDR: pip install cookiecutter; cookiecutter github.com/leej3/ds-cookiecutter**

While cloud hosted systems for continuous integration have been around for a while they are typically coupled with a development approach where the compute and development environments are hosted locally, either on a personal computer, a company server, or perhaps a locally managed compute cluster. A relatively recent addition to the offerings from cloud computing providers is a cloud hosted development environment, exemplified by Gitpod and Codespaces among others. These services enable a full migration of a companies compute needs to the cloud (excepting the local thin client to use to connect to it). In a world of frequent reports of data breaches this prospect becomes increasingly appealing.

In this repository we propose a template that is a blend of several technologies that can be used to meet one's data-science needs. This blend of technologies enables data-scientists achieve their goals... rather than crippling them with a series of well-meaning constraints in the name of security: a frustration that most of us are all grimly familiar with. The set of technologies include the following:
+ docker: to fully capture a compute environment in a manner that can be reused seamlessly in different contexts
+ docker buildkit: It is worth noting this plugin, recently reaching maturity, has started to become the default build backend for docker. It provides the remote build caching functionality that is essential to keep everything here working smoothly without constantly recomputing the same environments in different runtime contexts.
+ conda: This can capture the data-science stack in a manner that allows one to tune one's level of flexibility, reproducibility, and support for multiple operating systems.
+ Github Actions: CI testing provides a convenient infrastructure to automate this full system that we describe and is a must for piece of mind in collaborative projects with many moving pieces and heterogenous areas of expertise.
+ Codespaces: A cloud hosted development service, this enables remote development in an environment that you define but on a compute infrastruture that you only pay for as you use. Among the many benefits, some that stand out are an in browser VS Code development environment that is consistent across developers, Microsoft backed security, and trivially scalable compute resources.

Concisely, this repository proposes the following project organization to allow a team to efficiently collaborate on a data-science project:
+ A docker image is used to capture the development environment. This image is built on CI and is used for the project's test-suite, to launch a Codespaces cloud development environment for any person on the project, and can be pulled locally for those who wish to local development or debugging (this setting will/should likely have no access to the projects data and other cloud services).
+ A conda environment file is used loosely specifies the data-science stack used for the project. The full solve for this environment, as dependencies change, is done on CI as part of the docker image build. If desired, the fully constrained set of dependencies can be stored in a separate environment file that can be used to more reproducibly track the projects dependencies and speed up usage of the environment in other contexts. Similarly, a conda file could be added to track the solve for MacOS or other operating systems if support for local development on these systems is desired.
+ A .devcontainer directory is used to specify all of the details of the cloud development environment. This largely consists of the Dockerfile to build the docker image but can include additional customizations to the Codespaces experience.


For further information on cookiecutter (the tool used here to help create a generic data-science template) see [these docs](https://cookiecutter.readthedocs.io/en/2.0.2/overview.html).

To use this repo to generate a new project run:

```
# Install cookiecutter (this assumes you have pip and are using a python environment etc)
pip install cookiecutter

# Download this repository to your system
git clone https://github.com/leej3/ds-cookiecutter

# Create your own project by following the instructions...
cookiecutter ds-cookiecutter
```	
