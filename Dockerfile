FROM python:3.5.2

RUN set -ex && pip install pipenv --upgrade

ENV PYTHONPATH "/app/vendor/procedural_city_generation:$PYTHONPATH"

WORKDIR /app

# Install Python requirements
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN set -ex && pipenv install --deploy --system --dev

CMD ["bash"]
