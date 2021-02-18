# Copyright (C) 2019-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
FROM ubuntu:18.04

LABEL Description="This is the dev image for Intel(R) Distribution of OpenVINO(TM) toolkit on Ubuntu 18.04 LTS"
LABEL Vendor="Intel Corporation"

# hadolint ignore=DL3002
USER root
WORKDIR /

SHELL ["/bin/bash", "-xo", "pipefail", "-c"]

# creating non-root user
RUN useradd -ms /bin/bash -G video,users openvino && \
    chown openvino -R /home/openvino

# installing needed python runtime dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3-pip python3-dev && \
    rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir setuptools wheel

ADD ${package_url} /home/openvino

#installing openvino as root user
RUN python3 -m pip install --user --no-cache-dir /home/openvino/openvino*.whl

# installing openvino for openvino user
RUN chown openvino:openvino /home/openvino/*.whl
USER openvino
WORKDIR /home/openvino
RUN python3 -m pip install --user --no-cache-dir /home/openvino/openvino*.whl && \
    rm /home/openvino/openvino*.whl

RUN printf "\nexport PATH=$PATH:~/.local/bin\n" >> ~/.bashrc