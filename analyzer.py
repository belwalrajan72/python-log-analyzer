

def read_logs(filepath):
     with  open(filepath) as file :
         text = file.read()
         split = text.split()
         return  list(split)
     
lines = read_logs("sample.log")

def count_log_levels(lines):
     dictionary = {}
     for i in lines :
         if i == "INFO" or i =="ERROR":
          dictionary[i] = dictionary.get(i,0) +1 

         else :
            dictionary["other"] = dictionary.get("other",0) +1
     return dictionary

count  = count_log_levels(lines)

def print_reports(counts):
     for word, frequency in counts.items():
           print(f"{word}:  {frequency}")
     

print_reports(count)

