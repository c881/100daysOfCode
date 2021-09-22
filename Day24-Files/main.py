# Absolute folder
# with open("/Users/c881/Desktop/my_file.txt","w") as m_file:
#     m_file.write("Hello Again")

# Relative folder
with open("../../../Desktop/my_file.txt","r") as file:
    print(file.read())