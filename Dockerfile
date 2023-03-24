FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_md
EXPOSE 80
CMD ["python", "-m", "http.server", "80"]