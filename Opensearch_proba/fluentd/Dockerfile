FROM fluent/fluentd:latest

USER root

COPY fluent.conf /fluentd/etc/fluent.conf

RUN mkdir -p /fluentd/selflogs /fluentd/pos \
    && chmod -R 755 /fluentd/selflogs \
    && chown -R root:root /fluentd \
    && gem install fluent-plugin-opensearch --no-document

CMD ["fluentd", "-c", "/fluentd/etc/fluent.conf", "-v"]

