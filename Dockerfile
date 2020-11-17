FROM ubuntu:20.04

# Labels
LABEL company="GDIT"
LABEL maintainer="Janek Claus"
LABEL email="Janek.Claus@GDIT.com"

# OS tools
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    git \
    jq \
  && rm -rf /var/lib/apt/lists/*

# AWS CLI
RUN wget --quiet https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip \
  && unzip awscli-exe-linux-x86_64.zip \
  && ./aws/install

# Terraform
RUN wget --quiet https://releases.hashicorp.com/terraform/0.13.5/terraform_0.13.5_linux_amd64.zip \
  && unzip terraform_0.12.28_linux_amd64.zip \
  && mv terraform /usr/bin \
  && rm terraform_0.12.28_linux_amd64.zip

# Vault
RUN wget --quiet https://releases.hashicorp.com/vault/1.4.2/vault_1.4.2_linux_amd64.zip \
  && unzip vault_1.4.2_linux_amd64.zip \
  && mv vault /usr/bin \
  && rm vault_1.4.2_linux_amd64.zip

# Helm
RUN wget --quiet https://get.helm.sh/helm-v3.2.4-linux-amd64.tar.gz \
  && tar -zxf helm-v3.2.4-linux-amd64.tar.gz \
  && mv linux-amd64/helm /usr/bin \
  && rm helm-v3.2.4-linux-amd64.tar.gz

# Kubectl
RUN wget --quiet https://storage.googleapis.com/kubernetes-release/release/v1.18.0/bin/linux/amd64/kubectl \
  && chmod +x ./kubectl \
  && mv kubectl /usr/bin

# yq
RUN wget --quiet https://github.com/mikefarah/yq/releases/download/3.3.2/yq_linux_amd64 \
  && mv yq_linux_amd64 yq \
  && chmod +x ./yq \
  && mv yq /usr/bin

# kops
RUN wget --quiet https://github.com/kubernetes/kops/releases/download/v1.18.2/kops-linux-amd64 \
  && chmod +x kops-linux-amd64 \
  && mv kops-linux-amd64 /usr/local/bin/kops

# Application
WORKDIR /platform
COPY . .

# Start/run
CMD [ "/platform/build-all" ]
