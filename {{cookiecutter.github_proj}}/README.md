# Repo Description

# The docker image
The dockerfile stored in the .devcontainer directory is used to create a docker image that is used for CI testing and the Codespaces environment. This image is rebuilt (with some caching) for every push to github. The image that is used for caching is built and pushed to the docker registry when changes are added to  the development branch. Rebuilding locally for development can be useful to recapitulate failures on CI

### Conda environments
A folder for `.yml` files for creating various conda enviroments. The unpinned file is used to create the docker image. You may consider creating a pinned version of this file and using that for the image build instead. This can greatly create the time it takes to build the image... it adds extra overhead when changing the environment though. It still might be worth considering using a pinned environment to more explicitly track the exact versions of dependencies used so that people using Linux can rebuild the exact environment at a later date.

### external
Add external dependencies as git submodules here if desired.


