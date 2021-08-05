FROM python:3.9

ADD requeriments.txt /

RUN pip install -r requeriments.txt

ADD scraping.py /

CMD [ "python", "./scraping.py" ]
