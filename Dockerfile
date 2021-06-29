FROM python as base

RUN useradd -ms /bin/bash app
USER app

WORKDIR /home/app/app
ENV PYTHONUNBUFFURED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt requirements.txt

FROM base as development

COPY ./requirements-dev.txt requirements-dev.txt

RUN pip install --upgrade pip && pip install -r requirements-dev.txt --user

COPY . .


FROM base as production

COPY ./requirements-prod.txt requirements-prod.txt

RUN pip install --upgrade pip && pip install -r requirements-dev.txt --user

COPY . .

ENTRYPOINT [ "docker-entrypoint.sh" ]