#!/bin/bash
# install webp


if [ ! -f libwebp-0.4.1-linux-x86-64.tar.gz ]; then
    wget 'http://downloads.webmproject.org/releases/webp/libwebp-0.4.1-linux-x86-64.tar.gz'
fi

rm -r libwebp-0.4.1-linux-x86-64
tar -xvzf libwebp-0.4.1-linux-x86-64.tar.gz

sudo tar -xvf libwebp-0.4.1-linux-x86-64.tar.gz
ls libwebp-0.4.1-linux-x86-64
ls libwebp-0.4.1-linux-x86-64/bin
ls libwebp-0.4.1-linux-x86-64/include
ls libwebp-0.4.1-linux-x86-64/include/webp
ls libwebp-0.4.1-linux-x86-64/lib
sudo cp -r libwebp-0.4.1-linux-x86-64/bin/* /usr/local/bin
sudo cp -r libwebp-0.4.1-linux-x86-64/include/* /usr/local/include
sudo cp -r libwebp-0.4.1-linux-x86-64/lib/* /usr/local/lib
sudo ls /usr/local/include
sudo ls /usr/local/include/webp
sudo ls /usr/local/lib
sudo ls /usr/local/bin

# pushd libwebp-0.4.1-linux-x86-64

# ./configure --prefix=/usr --enable-libwebpmux --enable-libwebpdemux && make && sudo make install

# popd

