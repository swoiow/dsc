# GIT 使用技巧
- - -

[TOC]

- - -
## 日常技巧
- `git remote prune origin`

    *说明：remote上的一个分支被其他人删除后，需要更新本地的分支列表*

- `git push -f origin master`

    *说明：强制push本地代码，例如在本地进行 amend 模式的commit的时候，实际上是重写了原来的commit，如果直接push会出错，此时需要强制push，让remote端与本地一致*

- `git checkout [COMMIT_ID] [FILE_PATH]`

    *说明：部分恢复。当我们修改很多次之后，可能想恢复之前某个commit时的某个或者某些文件，本命令就提供了这个支持*

- - -
## Git分支管理策略

### 开发分支Develop
  * Git创建Develop分支的命令：
    `git checkout -b develop master`

  * 将Develop分支发布到Master分支的命令：
    # 切换到Master分支
    `git checkout master`
    # 对Develop分支进行合并
    `git merge --no-ff develop`


### 功能分支
  * 创建一个功能分支：
    `git checkout -b feature-x develop`

  * 开发完成后，将功能分支合并到develop分支：
    `git checkout develop`
    `git merge --no-ff feature-x`

  * 删除feature分支：
    `git branch -d feature-x`

### 预发布分支
  * 创建一个预发布分支：
    `git checkout -b release-1.2 develop`

  * 确认没有问题后，合并到master分支：
    `git checkout master`
    `git merge --no-ff release-1.2`
    # 对合并生成的新节点，做一个标签
    `git tag -a 1.2`

  * 再合并到develop分支：
    `git checkout develop`
    `git merge --no-ff release-1.2`

  * 最后，删除预发布分支：
    `git branch -d release-1.2`

- - -

## 推荐阅读
- [Git分支管理策略](http://www.ruanyifeng.com/blog/2012/07/git.html)
