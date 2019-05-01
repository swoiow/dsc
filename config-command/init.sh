#!/bin/bash

mv ~/.bashrc ~/.bashrc.bak
cp ./.bashrc ~/.bashrc
cp ./.zshrc ~/.zshrc
cp ./.git-completion.bash ~/.git-completion.bash
cat ./.bash_aliases > ~/.bash_aliases
cd ../config-tmux
sh init.sh
cd ../config-vim
cp ./.vimrc ~/.vimrc