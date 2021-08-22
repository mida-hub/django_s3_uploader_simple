# 公式からpython3.8 on alpine linuxイメージをpull
FROM python:3.8-alpine

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1

# ホストのpipfileをコンテナの作業ディレクトリにコピー
COPY ./Pipfile /usr/src/app/
COPY ./Pipfile.lock /usr/src/app/

# Pipenvをインストール
# pipfileからパッケージをインストールしてDjango環境を構築
RUN pip install --upgrade pip \
&& pip install pipenv \
&& pipenv install --system --dev

# ホストのカレントディレクトリ（現在はappディレクトリ）を作業ディレクトリにコピー
COPY . /usr/src/app/

# entrypoint.shを実行
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
