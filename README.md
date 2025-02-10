 db_proj
==========

## To download transcripts:
- Clone the directory:
  ```bash
  git clone https://github.com/innovationsquared/db_proj.git
  ```
- Run:
```bash
yt-dlp --skip-download --sub-langs "en" --write-subs -o "%(uploader)s/%(title)s.%(ext)s" "youtube.com/yourplaylisthere"
```
This will download .vtt files into a directory named after the creator in the directory you ran the command in. To convert to .csv for easier use with data viz programs, 
1. Edit vtt2csv.cpp to include your paths
2. Compile it,
   ```bash
   g++ vtt2csv.cpp -o convert
   ```
3. Then run 
```bash
./convert
```
You now have .csv files! Happy analyzing :)
