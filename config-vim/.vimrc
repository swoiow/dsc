set nocompatible              " be iMproved, required
filetype off                  " required

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'

Plugin 'Valloric/YouCompleteMe'

Plugin 'jnurmine/Zenburn'
Plugin 'altercation/vim-colors-solarized'

Plugin 'scrooloose/nerdtree'

call vundle#end()            " required
filetype plugin indent on    " required


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


" 键盘命令
""""""""""""""""""""""""""""""""""""""""""""""""""
map <C-A> ggVGY
set pastetoggle=<F12>

map <F5> :call CompileRunGcc()<CR>
func! CompileRunGcc()
    exec "w"
    if &filetype == 'c'
            exec "!g++ % -o %<"
            exec "!time ./%<"
    elseif &filetype == 'cpp'
            exec "!g++ % -o %<"
            exec "!time ./%<"
    elseif &filetype == 'java'
            exec "!javac %"
            exec "!time java %<"
    elseif &filetype == 'sh'
            :!time bash %
    elseif &filetype == 'python'
            exec "!clear"
            exec "!time python3 %"
    elseif &filetype == 'html'
            exec "!firefox % &"
    elseif &filetype == 'go'
            " exec "!go build %<"
            exec "!time go run %"
    elseif &filetype == 'mkd'
            exec "!~/.vim/markdown.pl % > %.html &"
            exec "!firefox %.html &"
    endif
endfunc


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


" VIM Plugin Config
""""""""""""""""""""""""""""""""""""""""""""""""""

" YCM
let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

" Theme
if has('gui_running')
  set background=dark
  colorscheme solarized
else
  colorscheme zenburn
endif
call togglebg#map("<F3>")

" NERDTree
map <C-n> :NERDTreeToggle<CR>
