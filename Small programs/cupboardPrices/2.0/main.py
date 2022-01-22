import prices


# take measurement of cupboard
while True:
    try:
        width = float(input("Width in cm: ")) / 100
    except ValueError:
        width = 0

    try:
        height = float(input("Height in cm: ")) / 100
        depth = float(input("Depth in cm: ")) / 100
        break
    except ValueError:
        continue


# asks how many sections
sections = int(input("How many sections?: "))
# size of sections



    

        




















# if width == 0:
#     for i in range(section_width):
#         width += section_width[i]
# else:
#     sections_total = 0
#     for i in range(section_width):
#         sections_total += section_width[i]
    
#     if sections_total > width:
#         print(f"The section sizes {section_width} are too big for the cupboards width {width}.")
#         redo = input("Do you want to change the width sections?: ")

#         if 


# number of pieces(preferably 1)
pieces = int(input("Number of pieces: "))
# labes the sections 
# draws the box
# asks number of shelfs for each sections
# asks number of drawer(s) for each section 
# draws the box
# get number of doors
# draws the box
# handle type
# how many mirrors
# which section(s) have mirror on which door if section has more than 1 door
#  
