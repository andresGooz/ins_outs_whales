FROM python:3.9

ADD requeriments.txt /

RUN pip install -r requeriments.txt

ADD scraping.py /

ADD best_coin.py /

CMD [ "python", "./scraping.py" ]

#CMD [ "python", "./best_coin.py" ]
