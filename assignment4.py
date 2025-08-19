#1.File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

#create input.txt with some text

with open("input.txt", "w") as f:
    f.write("Python makes programming fun.\n")
    f.write("Error handling is very important.\n")
    f.write("Files can be read and written in Python.\n")
    f.write("Practice helps you master coding.\n")
    f.write("Keep learning every day!\n")



#read the contents of input.txt

with open("input.txt", "r") as f:
    data= f.read()

print(data)

# Modify the text
modified_version= data.upper()
print(modified_version)

# Step 3: Save the modified content into output.txt
with open("output.txt", "w") as f:
    f.write(modified_version)


print("Modified version has been saved into output.txt")


#2.Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.



#error handling lab
filename = input("Enter the filename you want to open: ")

try:
    with open(filename, "r") as f:
        data = f.read()
    print("\n File content successfully read:\n")
    print(data)

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename.")

except PermissionError:
    print("Error: You don’t have permission to read this file.")

except Exception as e:
    print(f" An unexpected error occurred: {e}")


