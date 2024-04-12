FROM python:3.11-slim-buster

COPY requirements.txt pyproject.toml ./
COPY Makefile README.md  ./
COPY src/ src/

ENV VIRTUAL_ENV /usr/local/

RUN python -m pip install --upgrade uv pip && \ 
	uv pip install -r requirements.txt --no-cache-dir && \
	uv pip install . --no-cache-dir 

WORKDIR /

EXPOSE 80

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "80"]
