""""""""""""""""""""""""""""""""""""""""""""""""""
" 显示相关
""""""""""""""""""""""""""""""""""""""""""""""""""
" autocmd InsertEnter * se cul
" autocmd InsertLeave * se nocul
colorscheme desert
set encoding=utf-8
set fileencodings=utf-8,gbk,ucs-bom,cp936
set ignorecase smartcase
set noerrorbells
set nowrapscan
set number
set scrolloff=3
set shortmess=atI
set termencoding=utf-8
syntax on

""""""""""""""""""""""""""""""""""""""""""""""""""
" 键盘命令
""""""""""""""""""""""""""""""""""""""""""""""""""
map <C-A> ggVGY
set pastetoggle=<F12>

""""""""""""""""""""""""""""""""""""""""""""""""""
" 实用设置
""""""""""""""""""""""""""""""""""""""""""""""""""
" set autoindent
set autowrite
set cindent
set clipboard+=unnamed
set expandtab
set hlsearch
set incsearch
set magic
set nobackup
set noeb
set noswapfile
set ruler
set shiftwidth=4
set softtabstop=4
set tabstop=4
set mouse=v

" 可以在buffer的任何地方使用鼠标（类似office中在工作区双击鼠标定位）
" set mouse=a
" set selection=exclusive
" set selectmode=mouse,key
