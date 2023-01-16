# Script to create the session content files for Hugo from a csv file.


def main():
    import csv, sys, os
    from slugify import slugify
    
    if len(sys.argv) > 1:
        source_file = sys.argv[1]
    else:
        source_file = "sessions.csv"

    with open(source_file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            nid = row['nid']
            title = row['title']
            event_slug = row['event_slug']
            speakers = row['speakers'].split(", ")
            date = clean_date(row['date'])
            time_start = clean_date(row['time_start'])
            time_end = clean_date(row['time_end'])
            abstract = row['description']
            video = row['video']
            slides = row['slides']    

            dirname = "sessions/"+event_slug
            try:
                os.mkdir(dirname)
            except FileExistsError:
                pass
            except OSError:
                print ("Creation of the directory "+dirname+" failed" )


            slug = slugify(title)
            filename =  f"sessions/{event_slug}/{slug}.md"

            with open(filename, "w") as f:
                f.write("---\n")
                f.write(f"title: \"{title}\"\n")
                f.write("speakers:\n")
                for s in speakers:
                    f.write(f" - {s}\n")
                f.write(f"date: {date}\n")
                f.write(f"time_start: {time_start}\n")
                f.write(f"time_end: {time_end}\n")
                f.write(f"video: {video}\n")
                f.write(f"slides: {slides}\n")
                f.write("---\n\n")
                f.write(abstract)

def clean_date(strdate):
    tmpstr = strdate  

    if tmpstr.endswith("12:00"):
        tmpstr = tmpstr.replace("12:00", "12:00:00")
    if tmpstr.endswith("13:00"):
        tmpstr = tmpstr.replace("13:00", "13:00:00")

    tmpstr = tmpstr.replace(" 12:00", "T12:00")
    tmpstr = tmpstr.replace(" 13:00", "T13:00")

    return tmpstr

if __name__ == "__main__": 
	main() 
