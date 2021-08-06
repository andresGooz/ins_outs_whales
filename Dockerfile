FROM python:3.9
RUN mkdir /Folder
WORKDIR /Folder
COPY requeriments.txt /Folder/
RUN pip install -r requeriments.txt
COPY scraping.py /Folder/
COPY best_coin.py /Folder/
