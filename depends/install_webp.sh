#!/bin/bash
# install webp

if [ ! -f libwebp-0.4.3.tar.gz ]; then
#     wget 'http://downloads.webmproject.org/releases/webp/libwebp-0.4.3.tar.gz'
    wget 'http://downloads.webmproject.org/releases/webp/libwebp-0.4.3-linux-x86-32.tar.gz'
fi



# rm -r libwebp-0.4.3
# tar -xvzf libwebp-0.4.3.tar.gz
rm -r libwebp-0.4.3-linux-x86-32
tar -xvzf libwebp-0.4.3-linux-x86-32.tar.gz

pushd libwebp-0.4.3-linux-x86-32

ls

popd
