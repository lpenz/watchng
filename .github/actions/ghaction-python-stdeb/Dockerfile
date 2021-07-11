FROM debian:buster

ENV DEBIAN_FRONTEND noninteractive
RUN set -e -x; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        fakeroot python3-stdeb dh-python build-essential python3-all python-all

COPY entrypoint /
CMD /entrypoint
