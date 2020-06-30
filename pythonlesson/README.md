# 独学プログラマ 提出コード

まずはCloneしてディレクトリに移動

```
$ git clone https://github.com/it-students/pythonlesson.git
$ cd pythonlesson.git
```


学籍番号でブランチをきって移動する

```
$ git checkout -b ***学籍番号***
```

ブランチの確認 カレントのブランチが学籍番号になっていること

```
$ git branch
```

コードをcpしてステージする

```
$ cp -r ***プログラムをおいているディレクトリのすべてのファイル*** ./
$ git add -A
```

コミットしてPushする

```
$ git commit -m 'submit'
$ git push origin ***学籍番号***
```