#!/usr/bin/env python
# -*- coding: utf-8 -*

from os import environ

from _internal_utils import exec_bash, lines, pf
from fabric.api import cd, settings, sudo


if not environ.get("VIM"):
    environ["VIM"] = "8.1.0630"


def depend_debian():
    """
    apt-get install -y libncurses5-dev libncursesw5-dev
    """
    for line in lines(depend_debian):
        sudo(line)


def depend_redhat():
    """
    yum install -y ncurses-devel
    """
    for line in lines(depend_redhat):
        sudo(line)


def depend():
    depend_map = [
        ("debian", depend_debian),
        ("redhat", depend_redhat),
    ]

    dict(depend_map)[pf()]()


def download():
    """
    curl -sL https://github.com/vim/vim/archive/v{var}.tar.gz | tar -xz
    """

    with cd("/usr/src/"), settings(warn_only=True):
        for line in lines(download):
            sudo(line.format(var=environ["VIM"]))


def install():
    """
    ./configure --enable-python3interp --enable-luainterp --enable-cscope --prefix=/usr/local/vim/
    make -s -j2
    make install
    ln -sf /usr/local/vim/bin/vim /usr/bin/vim
    """

    depend()

    download()

    with cd("/usr/src/vim-{var}".format(var=environ["VIM"])), settings(warn_only=True):
        for line in lines(install):
            sudo(line)


@exec_bash
def install_plug():
    """
    #yum install install -y cmake gcc-c++ make cmake3
    #git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
    #curl -sL -o ~/.vimrc https://github.com/swoiow/dsc/raw/master/config-vim/.vimrc
    vim +PluginInstall +qall
    cd ~/.vim/bundle/YouCompleteMe && python3 install.py
    """
