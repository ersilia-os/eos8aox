FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install signaturizer3d==0.1.7
RUN pip install torch==2.2.1 torchvision==0.17.1  --index-url https://download.pytorch.org/whl/cpu

WORKDIR /repo
COPY . /repo
