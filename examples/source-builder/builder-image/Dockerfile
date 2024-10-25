# hadolint global ignore=SC3009,DL3025
FROM nvcr.io/nvidia/tritonserver:24.08-py3

ENV STI_SCRIPTS_PATH=/usr/libexec/s2i/
COPY s2i/bin/ ${STI_SCRIPTS_PATH}
COPY usr/ /usr/

# default s2i path
ENV APP_ROOT=/opt/app-root

# create basic folder structure
RUN mkdir -p ${APP_ROOT}/{bin,src,include} && \
    chmod -R u+x ${APP_ROOT}/bin && \
    chgrp -R 0 ${APP_ROOT} && \
    chmod -R g=u ${APP_ROOT}

ENV PATH=${APP_ROOT}/bin:${PATH} \
    HOME=${APP_ROOT}/src

WORKDIR ${HOME}

USER 1001

EXPOSE 8000 8001 8002

# ENTRYPOINT /opt/nvidia/nvidia_entrypoint.sh
CMD ${STI_SCRIPTS_PATH}/run
