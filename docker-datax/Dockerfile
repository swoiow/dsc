FROM openjdk:8u171-jdk

WORKDIR /opt
RUN curl https://datax-opensource.oss-cn-hangzhou.aliyuncs.com/datax.tar.gz |tar zx \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/opt/datax/bin/datax.py"]
CMD ["--help"]