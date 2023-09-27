import re

# Open the original SQL script file and read its contents
with open('platforms11.sql', 'r') as file:
    original_script = file.read()

# Use regular expressions to find all INSERT statements and modify them
modified_script = re.sub(r"INSERT INTO platform VALUES\('(.+)',(.+),'(.+)','(.+)',(.+),'(.+)'\);", r"INSERT INTO platform VALUES('\6','\1',\2,'\3','\4',\5, '');", original_script)

# Write the modified SQL script to a new file
with open('platforms111.sql', 'w') as file:
    file.write(modified_script)
