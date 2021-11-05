FROM python:alpine as download

# Download the relevant machine learning models whose results will be used as input
# For example, for COVID-NET, download COVIDNet-CXR4-B from https://github.com/haydengunraj/COVIDNet-CT/blob/master/docs/models.md
WORKDIR /tmp/models/COVID-Net_CT-1_L
RUN pip install gdown \
  && gdown "https://drive.google.com/uc?id=10WnXSqKOtoTMR57cqSm1vC5Ct3kT1TSZ" \
  && gdown "https://drive.google.com/uc?id=1WDQoNRah1rZt_stfobGUopfx48ldW5eA" \
  && gdown "https://drive.google.com/uc?id=1tHZmTqx006zE05x1TTaXksA_vnj79jvG" \
  && gdown "https://drive.google.com/uc?id=11-HTVNBorqjg6mNEhwjvY4lgA7gYcHSd"

FROM docker.io/fnndsc/tensorflow:1.15.3

LABEL org.opencontainers.image.authors="DarwinAI <support@darwinai.com>"

ENV DEBIAN_FRONTEND=noninteractive

COPY ["apt-requirements.txt", "requirements.txt", "./"]

RUN apt-get update \
  && xargs -d '\n' -a apt-requirements.txt apt-get install -y \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && rm -rf /var/lib/apt/lists/* \
  && rm -f requirements.txt apt-requirements.txt

COPY --from=download /tmp/models /usr/local/lib/ct-covidnet

WORKDIR /usr/local/src
COPY . .
RUN pip install .

CMD ["ct-covidnet", "--help"]
