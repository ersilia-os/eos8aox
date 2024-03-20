FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN python -m pip install signaturizer3d
RUN conda install pytorch torchvision torchaudio cpuonly -c pytorch

WORKDIR /repo
COPY . /repo
