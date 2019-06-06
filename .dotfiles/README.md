# DOTFILES

Repo of 2xRon's dotfiles for linux. Stolen from many sources.
Based on a code snippet from StreakyCobra on hackernews:
https://news.ycombinator.com/item?id=11070797

## User Guide
### Setup
```sh
git init --bare $HOME/.dotfiles
alias dotfiles='git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
dotfiles remote add origin git@github.com:2xRon/dotfiles.git
```

### Replication
```sh
git clone --separate-git-dir=$HOME/.dotfiles https://github.com/2xRon/dotfiles.git dotfiles-tmp
rsync --recursive --verbose --exclude '.git' dotfiles-tmp $HOME/
rm --recursive dotfiles-tmp
```

### Configuration
```sh
dotfiles config status.showUntrackedFiles no
dotfiles remote set-url origin git@github.com:2xRon/dotfiles.git
```

### Usage
```sh
dotfiles status
dotfiles add .gitconfig
dotfiles commit -m 'add gitconfig'
dotfiles push
```

