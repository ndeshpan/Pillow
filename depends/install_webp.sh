#!/bin/bash
# install webp

pushd ~

if [ ! -f libwebp-0.4.3.tar.gz ]; then
#     wget 'http://downloads.webmproject.org/releases/webp/libwebp-0.4.3.tar.gz'
    wget 'http://downloads.webmproject.org/releases/webp/libwebp-0.4.3-linux-x86-32.tar.gz'
fi

rm -r libwebp-0.4.3-linux-x86-32
tar -xvzf libwebp-0.4.3-linux-x86-32.tar.gz  -C ~  --strip-components=1

popd

