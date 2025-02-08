#include <fstream>
#include <regex>
#include <filesystem>

void parseFile(const char* filename, const char* outfilename);
void crawlDirectory(const std::string& dir);

int main (void)
{
  const std::string path = "/home/calvin/Documents/AppState/Data_With_Python/Project/Vsauce/Videos";
  crawlDirectory(path);
  return 0;
}

void parseFile(const std::string& filename, const std::string& outfilename)
{
  std::string line;
  std::ifstream infile;
  std::ofstream outfile;

  infile.open(filename);
  outfile.open(outfilename);
  outfile << "Start Time,End Time,Text" << std::endl;

  if (!infile.is_open() || !outfile.is_open())
  {
    printf("Error opening file.");
  }
  //skip over 4 lines at beginning of files
  for (int i = 0; i < 4; i++)
  {
    std::getline(infile,line);
  }
  //timestamp is hh:mm:ss.mmm
  std::regex timestamp_pattern(R"((\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3}))");

  std::string start, end, text;
  std::smatch match;

  while (std::getline(infile, line)) 
  {
    if (line.empty())
    {
      continue;
    }

    if (std::regex_search(line, match, timestamp_pattern))
    {
      start = match[1].str();
      end = match[2].str();

      text.clear();
      while(std::getline(infile, line) && !line.empty())
      {
        text += line + " ";
      }
      if (!text.empty())
      {
        text.pop_back();
      }
      outfile << start << "," << end << "," << text << std::endl;
    }
  }
  infile.close();
  outfile.close();
}

void crawlDirectory(const std::string& dir)
{
  std::string outputDir = "/home/calvin/Documents/AppState/Data_With_Python/Project/Vsauce/Videos2/";
  for (const auto& entry : std::filesystem::directory_iterator(dir))
  {
    if (entry.is_regular_file() && entry.path().extension() == ".vtt")
    {
      std::string inputFile = entry.path().string();
      std::string outputFile = outputDir + entry.path().stem().string() + ".csv";
      parseFile(inputFile, outputFile);
    }
  }
}
