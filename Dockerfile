# Use Ubuntu 24.04 parent image
FROM ubuntu:24.04

# Avoid tzdata interactive prompt
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies including PyCharm requirements and Python 3.9
# PyCharm needs OpenGL support
RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y \
    python3.9 \
    python3.9-distutils \
    python3.9-venv \
    git \
    wget \
    curl \
    tar \
    sudo \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxtst6 \
    libxi6 \
    libfreetype6 \
    fontconfig \
    fonts-liberation \
    python3.9-tk \
    libgl1 \
    libglib2.0-0 \
    && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.9 \
    && rm -rf /var/lib/apt/lists/*

# Add non-root user 'developer' with sudo privileges
RUN useradd -ms /bin/bash developer && \
    echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Download and extract PyCharm Community Edition
RUN wget -qO /tmp/pycharm.tar.gz https://download.jetbrains.com/python/pycharm-community-2023.3.4.tar.gz && \
    mkdir -p /opt/pycharm && \
    tar -xzf /tmp/pycharm.tar.gz -C /opt/pycharm --strip-components=1 && \
    rm /tmp/pycharm.tar.gz && \
    chown -R developer:developer /opt/pycharm

# Pre-create config directory to avoid permission issues, and set proper ownership
RUN mkdir -p /home/developer/.config/matplotlib \
    /home/developer/.cache/mesa_shader_cache \
    /home/developer/.cache/JetBrains \
    /home/developer/.local/share/JetBrains \
    /home/developer/.config/JetBrains && \
    chown -R developer:developer /home/developer

# Configure user
USER developer
ENV HOME=/home/developer

WORKDIR /home/developer/projects

# Run PyCharm when container launches, clearing any stale lock files first
CMD ["/bin/bash", "-c", "rm -f /home/developer/.config/JetBrains/PyCharm*/.lock && /opt/pycharm/bin/pycharm.sh"]
