def town_location(soup):
    location = soup.find("h1", itemprop="name", class_="main-heading").text
    current_location = location.split(" ")

    if current_location[2] != " ":
        loc = current_location[1] + " " + current_location[2]
    else:
        loc = current_location[1]

    return loc




print('Hello World')
