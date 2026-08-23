FROM container-registry.oracle.com/os/oraclelinux:8-slim

COPY rpms /tmp/

WORKDIR /fluent-bit

RUN microdnf update -y && \
    microdnf install -y libpq && \
    microdnf clean all && \
    rpm -i /tmp/*.rpm && \
    rm /tmp/*.rpm

COPY conf/fluent-bit.conf \
     conf/parsers.conf \
     conf/parsers_ambassador.conf \
     conf/parsers_java.conf \
     conf/parsers_extra.conf \
     conf/parsers_openstack.conf \
     conf/parsers_cinder.conf \
     conf/plugins.conf \
     /fluent-bit/etc/

# Generate schema and include as part of the container image
RUN /fluent-bit/bin/fluent-bit -J > /fluent-bit/etc/schema.json

EXPOSE 2020

# Entry point
ENTRYPOINT [ "/fluent-bit/bin/fluent-bit" ]
CMD ["/fluent-bit/bin/fluent-bit", "-c", "/fluent-bit/etc/fluent-bit.conf"]

