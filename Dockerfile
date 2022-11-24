FROM ubuntu:22.04

RUN apt update -y \
    && apt upgrade -y \
    && apt install wget curl -y

RUN wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup \
    && echo "367a80b01083c34899958cdd62525104a3de6069161d309039e84048d89ee98b  mariadb_repo_setup" \
    | sha256sum -c -



RUN chmod +x mariadb_repo_setup \
    && ./mariadb_repo_setup \
   --mariadb-server-version="mariadb-10.6"

#Install python
COPY python_installer.sh python_installer.sh
RUN chmod +x python_installer.sh \
    && ./python_installer.sh

# Install and configure mariadb-server
COPY mariadbSserver_install_configure.sh mariadbSserver_install_configure.sh
RUN chmod +x mariadbSserver_install_configure.sh \
    && ./mariadbSserver_install_configure.sh
#RUN apt-get update -y \
    #&& apt-get install -y libmariadb3 \
    #&& wget http://archive.ubuntu.com/ubuntu/pool/universe/m/mariadb-10.6/libmariadb-dev_10.6.7-2ubuntu1_amd64.deb \
    #&& wget http://archive.ubuntu.com/ubuntu/pool/main/g/glibc/libc6_2.35-0ubuntu3.1_amd64.deb \
RUN apt-get install libc6 \
    && wget http://archive.ubuntu.com/ubuntu/pool/universe/m/mariadb-10.6/libmariadb3_10.6.7-2ubuntu1_amd64.deb \
    && dpkg -i libmariadb3_10.6.7-2ubuntu1_amd64.deb \
    #&& wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl-dev_3.0.2-0ubuntu1_amd64.deb \
    && rm -Rf /etc/apt/sources.list.d/mariadb.list.old_1 \
    && apt-get update \
    && apt-get install libssl-dev -y \
    && apt-get install libmariadb-dev -y \
    && pip3 install mariadb

WORKDIR /app
COPY . .