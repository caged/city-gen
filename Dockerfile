FROM python:2.7.9


WORKDIR /app

RUN git clone https://github.com/josauder/procedural_city_generation.git

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash"]
