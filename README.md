# 取扱説明書

## 実行手順

### step:1

```bash
make clean
make build
```

local の環境をきれいにしてから、docker を build

### step:2

```bash
make run {contest_id}
```

コンテナの中に入る

### step:3

```bash
acc login
```

ログインを済ませる。

### step:4

コンテナの中で実行

```bash
make setup
```

問題と core に定義したファイルがコピーされる。
