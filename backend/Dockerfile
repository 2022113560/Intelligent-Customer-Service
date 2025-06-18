FROM jenkins/jenkins:lts

USER root

RUN rm -rf /etc/apt/sources.list.d/* && \
    echo 'deb https://mirrors.tuna.tsinghua.edu.cn/debian bullseye main contrib non-free' > /etc/apt/sources.list && \
    echo 'deb https://mirrors.tuna.tsinghua.edu.cn/debian-security bullseye-security main contrib non-free' >> /etc/apt/sources.list && \
    echo 'deb https://mirrors.tuna.tsinghua.edu.cn/debian bullseye-updates main contrib non-free' >> /etc/apt/sources.list && \
    apt-get clean && \
    apt-get -o Acquire::Retries=3 update && \
    apt-get -o Acquire::Retries=3 install -y docker.io

USER jenkins
ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/bin/jenkins.sh"]

