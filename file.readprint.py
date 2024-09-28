# with open('C:\\Users\\ALI\\OneDrive\\Desktop\\Chat bot\\Information','r') as info_read:
#     var_check_name = info_read.readline()
#     var_check_birth_year = info_read.readline()
#     var_check_gender = info_read.readline()

# print(var_check_name)
# print(var_check_birth_year)
# print(var_check_gender)



a_file = open('C:\\Users\\ALI\\OneDrive\\Desktop\\Chat bot\\User Information','r')
lines_to_read = [0, 2]
for position, line in enumerate(a_file):
    if position in lines_to_read:
        print(line)

# print(lines_to_read)