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
            slot = row['slot']
            title = row['title']
            event_slug = "2023"
            speakers = row['speaker'].split(", ")
            time_start = row['time_start']
            time_end = row['time_end']
            abstract = row['abstract']
#            video = row['video']
#            slides = row['slides']    
            
            print(f"row: {slot}, {title}, {speakers}, {time_start},{time_end}")

            dirname = "sessions/"+event_slug
            try:
                os.mkdir(dirname)
            except FileExistsError:
                pass
            except OSError:
                print ("Creation of the directory "+dirname+" failed" )


            slug = slugify(title)
            filename =  f"sessions/{event_slug}/{slot}-{slug}.md"

            with open(filename, "w") as f:
                f.write("---\n")
                f.write(f"title: \"{title}\"\n")
                f.write(f"slug: {slug}\n")
                f.write("speakers:\n")
                for s in speakers:
                    f.write(f" - {s}\n")
                f.write(f"time_start: {time_start}\n")
                f.write(f"time_end: {time_end}\n")
#                f.write(f"video: {video}\n")
#                f.write(f"slides: {slides}\n")
                f.write("---\n\n")
                f.write(abstract)

def clean_date(strdate):
    tmpstr = strdate  

    return tmpstr

if __name__ == "__main__": 
	main() 
