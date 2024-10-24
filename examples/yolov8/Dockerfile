# hadolint global ignore=DL3008,SC3009
FROM docker.io/ultralytics/ultralytics:latest-cpu as build

USER 0

# install os dependencies
# RUN apt-get update && \
#     apt-get install -y libgl1 && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# COPY requirements.txt ${HOME}/

# RUN pip install --no-cache-dir -U pip setuptools wheel && \
# pip install --no-cache-dir -r requirements.txt

ENV STI_SCRIPTS_PATH=/usr/libexec/s2i/
COPY s2i/bin/ ${STI_SCRIPTS_PATH}

RUN ${STI_SCRIPTS_PATH}/assemble

FROM nvcr.io/nvidia/tritonserver:24.08-py3 as inference

ENV STI_SCRIPTS_PATH=/usr/libexec/s2i/
COPY s2i/bin/ ${STI_SCRIPTS_PATH}

USER 1001

ARG MODEL_NAME=yolov8s
COPY --chown=1001:0 \
     --chmod=775 \
     --from=build /ultralytics/${MODEL_NAME}/ /models/${MODEL_NAME}/

ENV MODEL_REPOSITORY=/models

EXPOSE 8000 8001 8002

# ENTRYPOINT /opt/nvidia/nvidia_entrypoint.sh
CMD ${STI_SCRIPTS_PATH}/run
