def main():
    file_name = input("File name: ")
    check_ext(file_name)

def check_ext(file_name):
    extensions = {
        ".gif" : "image/gif",
        ".jpg" : "image/jpg",
        ".jpeg" : "image/jpeg",
        ".png" : "image/png", 
        ".pdf" : "application/pdf",
        ".txt" : "text/plain",
    }
    
    period_index = file_name.rfind(".")
    if period_index != -1:
        ext = file_name[period_index:]  # Get everything after the last period
    else:
        ext = ''  # No extension found
    
    print(extensions.get(ext, "application/octet-stream"))
   
main()