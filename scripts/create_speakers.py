# Script to create the session content files for Hugo from a csv file.

import csv
import os
from slugify import slugify

with open('dataday-speakers.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        title = row['title']
        events = row['events'].split(", ")
        designation = row['designation']
        bio = row['bio']
        twitter = row['twitter']
        linkedin = row['linkedin']

        slug = slugify(title)

        dirname = "speakers/"+slug
        try:
            os.mkdir(dirname)
        except FileExistsError:
            print("Dir "+dirname+" exists")
        except OSError:
            print ("Creation of the directory "+dirname+" failed" )
        else:
            print ("Successfully created the directory "+dirname)

        filename = dirname+"/_index.md"

        with open(filename, "w") as f:

            f.write("---\n")
            f.write("title: \""+title+"\"\n")
            f.write("designation: \""+designation+"\"\n")
            f.write("twitter: \""+twitter+"\"\n")
            f.write("linkedin: \""+linkedin+"\"\n")
            f.write("events:\n")
            for s in events:
                f.write(" - "+s+"\n")
            f.write("---\n\n")
            f.write(bio)


