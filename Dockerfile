FROM python:3.9
RUN mkdir /Folder
WORKDIR /Folder

COPY requeriments.txt /Folder/

RUN pip install -r requeriments.txt

COPY best_coin.py /Folder/

COPY scraping.py /Folder/

CMD [ "python", "./scraping.py" ]

#CMD [ "python", "./best_coin.py" ]
