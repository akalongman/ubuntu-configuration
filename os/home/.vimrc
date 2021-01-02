" break with the busted old vi junk
" must be first
set nocompatible
filetype off

""""""""""""""""""""""""""""""""""""""""
" Plugins
""""""""""""""""""""""""""""""""""""""""

" vundle stuff
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" vundle repo
Bundle 'VundleVim/Vundle.vim'

" github repos
Plugin 'rking/ag.vim'
Plugin 'tpope/vim-pathogen'
Plugin 'scrooloose/nerdtree'
Plugin 'kien/ctrlp.vim'
Plugin 'flazz/vim-colorschemes'
Plugin 'akalongman/vim-longishdark-theme'
Plugin 'hail2u/vim-css3-syntax'
Plugin 'pangloss/vim-javascript'
Plugin 'tpope/vim-markdown'
Plugin 'othree/html5.vim'
Plugin 'jnwhiteh/vim-golang'
Plugin 'hdima/python-syntax'
Plugin 'Glench/Vim-Jinja2-Syntax'
Plugin 'StanAngeloff/php.vim'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

" For vim-markdown
autocmd BufNewFile,BufReadPost *.md set filetype=markdown

" custom file ignores
let g:ctrlp_custom_ignore = {
    \ 'dir':  '\.git$\|\.hg$\|\.svn$\|bower_components$\|dist$\|node_modules$\|project_files$\|test$',
    \ 'file': '\.exe$\|\.so$\|\.dll$\|\.pyc$' }


""""""""""""""""""""""""""""""""""""""""
" General VIM
""""""""""""""""""""""""""""""""""""""""

" show line numbers
set number

" show lines in lower right
set ruler

" don't wrap lines ever
set nowrap

" Set to auto read when a file is changed from the outside
set autoread

" global text columns
set textwidth=80

" don't automatically break long lines unless they are new
set formatoptions+=l

" detect file type, turn on that type's plugins and indent preferences
" Turned off -- This was annoying when copy/pasting causes indent problems
" filetype plugin indent on

" Show matching brackets when text indicator is over them
set showmatch

" How many tenths of a second to blink when matching brackets
set mat=2

" No annoying sound on errors
set noerrorbells
set novisualbell
set t_vb=
set tm=500

" allow background buffers
set hidden

" global tab settings
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set smarttab

" ignore these nonsense files
set wildignore=*.swp,*.bak,*.pyc,*.class

" Return to last edit position when opening files
autocmd BufReadPost *
     \ if line("'\"") > 0 && line("'\"") <= line("$") |
     \   exe "normal! g`\"" |
     \ endif

" Remember info about open buffers on close
set viminfo^=%

" no backups, please!
set nobackup
set noswapfile

" keep a longer history
set history=1000

" enable folding
"set foldmethod=indent
"set foldlevel=99

" make file/command tab completion useful
set wildmode=list:longest

" clipboard fusion!
set clipboard^=unnamed clipboard^=unnamedplus

" Source the vimrc file after saving it.
" This way, you don't have to reload Vim to see the changes.
if has("autocmd")
 augroup myvimrchooks
  au!
  autocmd bufwritepost .vimrc source ~/.vimrc
 augroup END
endif

" easier window navigation
nmap <C-h> <C-w>h
nmap <C-j> <C-w>j
nmap <C-k> <C-w>k
nmap <C-l> <C-w>l

""""""""""""""""""""""""""""""""""""""""
" Searching
""""""""""""""""""""""""""""""""""""""""

" show search matches as you type
set incsearch

" clear the search buffer when hitting return
nnoremap <CR> :nohlsearch<cr>

" Ignore case when searching
set ignorecase

" When searching try to be smart about cases
set smartcase

" highlight search results
set hlsearch

""""""""""""""""""""""""""""""""""""""""
" Aestehtics
""""""""""""""""""""""""""""""""""""""""

" keep cursor somewhat centered
set scrolloff=3

" highlight current line
:set cursorline

" invert and bold status line
set highlight=sbr

" enable syntax highlighting
syntax on

"tell the term has 256 colors
set t_Co=256

colorscheme LongishDark
set guifont=Inconsolata\ Medium\ 10

" highlight col 80
"set colorcolumn=80
"highlight ColorColumn guibg=#333

" extra whitespace sucks, make it RED
highlight ExtraWhitespace ctermbg=red guibg=red
autocmd ColorScheme * highlight ExtraWhitespace ctermbg=red guibg=red
match ExtraWhitespace /\s\+$/
