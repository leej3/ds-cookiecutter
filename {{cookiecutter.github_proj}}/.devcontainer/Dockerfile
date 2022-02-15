# Pin image to a number version for reproducibility
FROM mcr.microsoft.com/vscode/devcontainers/base:0.202.3-bullseye

# [Option] Install zsh
ARG INSTALL_ZSH="false"
# [Option] Upgrade OS packages to their latest versions
ARG UPGRADE_PACKAGES="false"

# Install needed packages and setup non-root user. Use a separate RUN statement to add your own dependencies.
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Install vscode maintained list of tools
RUN mkdir /tmp/library-scripts
ADD https://raw.githubusercontent.com/microsoft/vscode-dev-containers/253314b9ead0f86568aba9cd6477faa17cdd5152/script-library/azcli-debian.sh /tmp/library-scripts
ADD https://raw.githubusercontent.com/microsoft/vscode-dev-containers/253314b9ead0f86568aba9cd6477faa17cdd5152/script-library/common-debian.sh /tmp/library-scripts
RUN bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" "true" "true" \
    # Install the Azure CLI
    && bash /tmp/library-scripts/azcli-debian.sh \
    # Clean up
    && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts

# Install some additional OS packages
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends bzip2 libgl1-mesa-glx \
    # Clean up
    && apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/library-scripts

# Install micromamba
ENV MAMBA_ROOT_PREFIX="/opt/conda"

RUN wget -O Mambaforge.sh https://github.com/conda-forge/miniforge/releases/download/4.10.3-7/Mambaforge-Linux-x86_64.sh \
    && bash Mambaforge.sh -b -p ${MAMBA_ROOT_PREFIX} \
    && rm Mambaforge.sh

# Codespaces uses an interactive shell (set via userEnvProbe) and so sources the following setup script
RUN ${MAMBA_ROOT_PREFIX}/condabin/mamba init
RUN cat ~/.bashrc |grep -v '#' >>  /etc/bash.bashrc
ENV PATH=${MAMBA_ROOT_PREFIX}/condabin:${PATH}

# Use bash in Dockerfile RUN commands and make sure bashrc is sourced when
# executing commands with /bin/bash -c
# Needed to have the micromamba activate command configured etc.
SHELL ["/bin/bash", "-c"]

# Allows to set the environment name from CI, args are like ENV variables but
# they do not persist past build time and they can be overwritten using
# --build-args in the build command
ARG \
   CONDA_ENV={{cookiecutter.pkg_name}} \
    # Avoid hardcoded paths and envs for flexibility
    CONDA_ENVS_DIR=environments \
   # Adding an env for doc creation will likely be useful
   #  DOCS_CONDA_FILE=environment_docs_pinned
   # Standard environment that can be used by default:
    CONDA_FILE=environment_unpinned

# # Copy over needed files
COPY ./${CONDA_ENVS_DIR}/${CONDA_FILE}.yml /tmp/${CONDA_FILE}.yml
# COPY ./${CONDA_ENVS_DIR}/${DOCS_CONDA_FILE}.yml /tmp/${DOCS_CONDA_FILE}.yml

# # Create conda envs
RUN \
   # mamba env create -y -f /tmp/${DOCS_CONDA_FILE}.yml -n ${CONDA_ENV_DOCS} --quiet && \
   mamba env create -f /tmp/${CONDA_FILE}.yml -n ${CONDA_ENV} --quiet && \
   mamba clean --all -y && \
   rm -rf /tmp/*


# Make end containers use the new environment... this doesn't work if the
# entrypoint is overwritten
# See the following for info on the various shell setup files:
# https://en.wikipedia.org/wiki/Unix_shell#Configuration_files:
RUN export SETUP=". /opt/conda/etc/profile.d/conda.sh || true ; conda activate ${CONDA_ENV} || true" ; \
    for f in ~/.profile ~/.bashrc ~/.shrc /etc/profile /etc/bash.bashrc /etc/sh.shrc ; do \
    echo "$SETUP" >> $f; \
    done
# This will work if the entrypoint uses a shell
ENV ENV="/etc/bash.bashrc"

CMD ["/bin/bash"]

