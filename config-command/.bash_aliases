# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"

    export LS_OPTIONS='--color=auto'

    alias ls='ls $LS_OPTIONS'
    alias la='ls $LS_OPTIONS -CFA'
    alias ll='ls $LS_OPTIONS -l'

    alias dir='dir $LS_OPTIONS'
    alias vdir='vdir $LS_OPTIONS'

    alias grep='grep $LS_OPTIONS'
    alias fgrep='fgrep $LS_OPTIONS'
    alias egrep='egrep $LS_OPTIONS'
fi


# function
onvenv () {
    if [ -d "venv" ]; then
        source venv/bin/activate
    else
        source .venv/bin/activate
    fi
}

vim_install () {
    yum install -y install cmake gcc-c++ make git
    git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
    vim_update
    cd ~/.vim/bundle/YouCompleteMe
    python3 install.py
}

# alias screen='screen -U -r'
alias initvenv='python3 -m venv .venv'
alias offvenv='deactivate'
alias where='whereis'
alias vi='vim'
alias docker-rmi-none='docker rmi $(docker images -q -f dangling=true)'
alias docker-rm-exit='docker rm $(docker ps --all -q -f status=exited)'
alias dk='docker'
alias dki='docker images'
alias dkp='docker-compose'
alias vim_update='vim +PluginClean +qall && vim +PluginInstall +qall'
