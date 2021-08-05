#!/bin/bash

docker build -t python-barcode .
docker run python-barcode

# chmod +x init.sh
