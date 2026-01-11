

def read_logs(filepath):
     try :
        with  open(filepath) as file :
          text = file.read()
          split = text.split()
          
     except Exception as e :
        split = e 
     return split



test_list = ["INFO",  "User",  "logged", "in",
"ERROR", "Database", "timeout",
"INFO", "User", "logged", "out",
"ERROR", "API", "failed",
"ERROR", "Database", "timeout",
"Info", "this", "is", "a", "new" "line" ]  

lines = read_logs("C:/Users/belwa/OneDrive/Desktop/python_log_analyzer/python-log-analyzer/sample.log")
# lines = test_list
def count_log_levels(lines):
     dictionary = {}
     if isinstance(lines, list) and lines != None :
      for i in lines :
          if i == "INFO" or i =="ERROR" or  i == "Info":
           dictionary[i] = dictionary.get(i,0) +1 

          else :
             dictionary["other"] = dictionary.get("other",0) +1
     
     else :
           dictionary
     return dictionary
     

count  = count_log_levels(lines)

def print_reports(counts):
     if isinstance(count, dict) and len(count) != 0 :
      for word, frequency in counts.items():
           print(f"{word}:  {frequency}")
     else :
      print(f"The dictionary is empty")



print_reports(count)

