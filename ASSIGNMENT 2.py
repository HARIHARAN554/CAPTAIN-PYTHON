file_extensions = {"py":"python",
                  "docx":"document",
                  "java":"java",
                  "txt":"text",
                  "pdf":"PDF",
                  "ppt":"ppt",
                  ".c":"C",
                  ".CPP":"C++" }
filename = input("Input the Filename: ")
f_extns = filename.split(".")
output = file_extensions.get((f_extns[-1]))
print ("The extension of the file is : " + output)                  