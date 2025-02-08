 db_proj
==========

## To download transcripts:
Run:
```bash
yt-dlp --skip-download --sub-langs "en" --write-subs -o "%(uploader)s/%(title)s.%(ext)s" "youtube.com/yourplaylisthere"
```
This will download .vtt files into the directory the command is ran from. To convert, 
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
