#! /bin/bash

mongoimport --host mongodb --db yt_data --collection projet_cs --type json --file /mongo_seed/data.json --jsonArray