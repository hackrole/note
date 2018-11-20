# note

[![Build Status](https://travis-ci.com/hackrole/note.svg?branch=master)](https://travis-ci.com/hackrole/note)

tmp to save to daily note.
[github pages url](https://hackrole.github.io)

使用rst来记录笔记/博客.使用org来记录个人计划和任务管理。

使用travis ci自动发布到github pages

## install

better to use *virtualenvwrapper*.

```bash
pip install pipenv
git clone git@github.com/hackrole/note
cd note
pipenv install
fab build
fab serve
```
