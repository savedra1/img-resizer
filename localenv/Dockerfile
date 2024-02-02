FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir resize-img

CMD ["resize-img", "git.jpg"]