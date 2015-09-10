#!/bin/bash
# install webp

pushd ~

if [ ! -f libwebp-0.4.3.tar.gz ]; then
#     wget 'http://downloads.webmproject.org/releases/webp/libwebp-0.4.3.tar.gz'
    wget 'http://downloads.webmproject.org/releases/webp/libwebp-0.4.3-linux-x86-32.tar.gz'
fi

popd

# rm -r libwebp-0.4.3
# tar -xvzf libwebp-0.4.3.tar.gz
rm -r libwebp-0.4.3-linux-x86-32
tar -xvzf libwebp-0.4.3-linux-x86-32.tar.gz  -C ~

# pushd libwebp-0.4.3-linux-x86-32
#
# ls
#
# popd
