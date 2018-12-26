#!/usr/bin/env bash

file=~/.bash_aliases
if [ ! -f "$file" ]; then
    curl -sL -o "$file" https://github.com/swoiow/dsc/raw/master/config-command/.bash_aliases
fi

file=~/.git-completion.bash
if [ ! -f "$file"  ]; then
    curl -sL -o "$file" https://github.com/swoiow/dsc/raw/master/config-command/.git-completion.bash
fi

file=~/.zshrc
if [ ! -f "$file" ]; then
    curl -sL -o "$file" https://github.com/swoiow/dsc/raw/master/config-command/.zshrc
fi

export ZSH="/usr/local/oh-my-zsh"
sudo sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
sudo chown -R root:users /usr/local/oh-my-zsh