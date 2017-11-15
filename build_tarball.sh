#!/bin/bash

mkdir -p .tmp
cd .tmp
git clone https://github.com/digitalocean/ceph_exporter.git
cd ceph_exporter
VER=`git tag | tail -1`
HASH=`git rev-parse --short $VER`
DATE=`date +%Y%m%d`
git archive --format=tar \
            --prefix=ceph_exporter-${VER}+git${DATE}.${HASH}/ \
            $VER | \
            gzip > ../../ceph_exporter-${VER}+git${DATE}.${HASH}.tar.gz

cd ..
cd ..
rm -rf .tmp

cat ceph_exporter.spec.in | \
    sed -e "s/##VERSION##/${VER}+git${DATE}.${HASH}/g" > \
    ceph_exporter.spec

