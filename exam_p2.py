def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    """check if this code is right"""
    # names = open('F://babynames/' + file_name)
    # data_name = [line.split()[0].lower for line in names if line != '']
    # return data_name

    names = open('babynames/' + file_name)
    names_edit = [line.strip('\n').split(',') for line in names if line != '']
    return names_edit

def year_list(year):
    string_year = str(year)
    return process_file('yob' + string_year + '.txt')

def total_births(year, gender):
    """
    #MAKE SURE TO CONVERT THE YEAR INTO AN INTEGER!!!
    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    births = 0
    for i in year_list(year):
        if gender == i[1]:
            births += int(i[2])
    return births
   
    


def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    for i in year_list(year):
        if i[0].lower == name.lower() and i[1] == gender:
            return float(i[2]) / total_births(year, gender)


def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    proportions = {}
    for year in range(1880,2011):
        p = proportion(name, gender, year)
        if p:
            proportions[str(year)] = p
    return max(proportions, key = proportions.get)


def main():
    print("My name appeared the most among the females in the year:")
    print(highest_year('Pranjal', 'F'))

if __name__ == '__main__':
    main()
