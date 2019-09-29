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
onvenv(){
    if [ -d "venv" ]; then
        source venv/bin/activate
    else
        source .venv/bin/activate
    fi
}

vim_install(){
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
alias docker-prune='docker system prune -af --volumes'
alias dk='docker'
alias dki='docker images'
alias dkp='docker-compose'
alias vim_update='vim +PluginClean +qall && vim +PluginInstall +qall'
alias gi='git'

onproxy(){
    export http_proxy="http://127.0.0.1:1081/"
    export https_proxy="http://127.0.0.1:1081/"
    export all_proxy="http://127.0.0.1:1081/"
    export no_proxy="http://127.0.0.1:1081/"
    export HTTP_PROXY="http://127.0.0.1:1081/"
    export HTTPS_PROXY="http://127.0.0.1:1081/"
    export ALL_PROXY="http://127.0.0.1:1081/"
    export NO_PROXY="http://127.0.0.1:1081/"
}

offproxy(){
    unset http_proxy 
    unset https_proxy
    unset all_proxy
    unset no_proxy
    unset HTTP_PROXY
    unset HTTPS_PROXY
    unset ALL_PROXY
    unset NO_PROXY
}
