ARG BASE_IMAGE=ubuntu:20.04
FROM $BASE_IMAGE

WORKDIR /root/

# install packges
ENV DEBIAN_FRONTEND=noninteractive
RUN dpkg --add-architecture i386 

RUN apt-get clean && apt-get update && apt-get -y upgrade
RUN apt-get install -y build-essential wget curl zsh git file
RUN apt-get install -y vim net-tools netcat iputils-ping xxd binwalk tmux
RUN apt-get install -y libc6 libc6-dbg libc6:i386 libc6-dbg:i386 lib32stdc++6
RUN apt-get install -y g++-multilib cmake libffi-dev libssl-dev
RUN apt-get install -y python3-dev python3-pip python3 python3-distutils
RUN apt-get install -y ruby ruby-dev
RUN apt-get install -y strace ltrace nasm gdb gdb-multiarch
RUN apt-get install -y patchelf gawk bison rpm2cpio cpio zstd jq

# setup locales
RUN apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# setup zsh
RUN wget -nv -O - https://raw.githubusercontent.com/zimfw/install/master/install.zsh | zsh
RUN chsh -s $(which zsh)

# install tools
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade pwntools
RUN python3 -m pip install --no-cache-dir capstone ropgadget ipython smmap2 ropper unicorn pebble r2pipe pycryptodome
RUN python3 -m pip install --no-cache-dir z3-solver angr cvc5
## temporary line for pyelftools breaking pwntools
RUN python3 -m pip install --no-cache-dir pyelftools==0.29
RUN gem install one_gadget seccomp-tools

# setup gdb
RUN wget -O ~/.gdbinit-gef.py -q https://gef.blah.cat/py
RUN git clone https://github.com/scwuaptx/Pwngdb.git Pwngdb
## setup gef
RUN echo "source ~/.gdbinit-gef.py" >> ~/.gdbinit && tail -n +2 Pwngdb/.gdbinit >> ~/.gdbinit
COPY .gef.rc .gef.rc

# setup rust from rustup
ENV PATH="/root/.cargo/bin:$PATH"
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain nightly

# install r2 and radius2
RUN git clone https://github.com/radareorg/radare2.git radare2
RUN radare2/sys/install.sh
RUN cargo install radius2

# libc, glibc
RUN git clone https://github.com/niklasb/libc-database.git libc-database

COPY --from=skysider/glibc_builder64:2.19 /glibc/2.19/64 /glibc/2.19/64
COPY --from=skysider/glibc_builder32:2.19 /glibc/2.19/32 /glibc/2.19/32

COPY --from=skysider/glibc_builder64:2.23 /glibc/2.23/64 /glibc/2.23/64
COPY --from=skysider/glibc_builder32:2.23 /glibc/2.23/32 /glibc/2.23/32

COPY --from=skysider/glibc_builder64:2.24 /glibc/2.24/64 /glibc/2.24/64
COPY --from=skysider/glibc_builder32:2.24 /glibc/2.24/32 /glibc/2.24/32

COPY --from=skysider/glibc_builder64:2.26 /glibc/2.26/64 /glibc/2.26/64
COPY --from=skysider/glibc_builder32:2.26 /glibc/2.26/32 /glibc/2.26/32

COPY --from=skysider/glibc_builder64:2.27 /glibc/2.27/64 /glibc/2.27/64
COPY --from=skysider/glibc_builder32:2.27 /glibc/2.27/32 /glibc/2.27/32

COPY --from=skysider/glibc_builder64:2.28 /glibc/2.28/64 /glibc/2.28/64
COPY --from=skysider/glibc_builder32:2.28 /glibc/2.28/32 /glibc/2.28/32

COPY --from=skysider/glibc_builder64:2.29 /glibc/2.29/64 /glibc/2.29/64
COPY --from=skysider/glibc_builder32:2.29 /glibc/2.29/32 /glibc/2.29/32

COPY --from=skysider/glibc_builder64:2.30 /glibc/2.30/64 /glibc/2.30/64
COPY --from=skysider/glibc_builder32:2.30 /glibc/2.30/32 /glibc/2.30/32

COPY --from=skysider/glibc_builder64:2.31 /glibc/2.31/64 /glibc/2.31/64
COPY --from=skysider/glibc_builder32:2.31 /glibc/2.31/32 /glibc/2.31/32
