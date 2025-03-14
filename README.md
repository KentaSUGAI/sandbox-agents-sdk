# OpenAI Agents SDK サンドボックス

このプロジェクトは、OpenAI Agents SDKを使用した実験的な開発環境です。

## 環境要件

- Python 3.8以上
- OpenAI API キー

## セットアップ

1. 仮想環境のアクティベート:
```bash
source .venv/bin/activate  # Unix/macOS
.venv\Scripts\activate     # Windows
```

2. 依存パッケージのインストール:
```bash
pip install -r requirements.txt
```

3. 環境変数の設定:
```bash
export OPENAI_API_KEY=your-api-key-here
```

## プロジェクト構造

```
.
├── .venv/              # Python仮想環境
├── src/               # ソースコード
│   └── examples/     # サンプルコード
│       ├── agent_with_trace.py
│       ├── search.py
│       └── hello_world.py
├── tests/             # テストコード
├── requirements.txt   # 依存パッケージ
└── README.md         # このファイル
```

## 使用方法

### サンプルコードの実行

`src/examples` ディレクトリには以下のサンプルコードが含まれています：

- `hello_world.py`: 基本的なエージェントの使用例
- `agent_with_trace.py`: トレース機能を使用したエージェントの実行例
- `search.py`: Web検索機能を使用した例

サンプルコードは以下のように実行できます：

```bash
python src/examples/hello_world.py
```

## ライセンス

MIT
