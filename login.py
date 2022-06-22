def get_data(firstName, lastName, Number):

    fullName = ""

    if len(firstName) > 3:
        fullName = firstName
    else:
        fullName = firstName[0:4]

    if len(lastName) < 3:
        fullName += lastName
    else:
        fullName += lastName[0:3]

    fullName += Number

    return fullName








