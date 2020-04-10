from bs4 import BeautifulSoup
import json
import re

with open('zipcode.html') as f:
    soup = BeautifulSoup(f, features='html.parser')

chicago_zip_codes = []

title_pattern = re.compile('ZIP Code \d{5}')
for child in soup.descendants:
    if child.name == 'a' and 'title' in child.attrs:
        if title_pattern.match(child.attrs['title']):
            chicago_zip_codes.append(child.contents[0].replace(
                'ZIP Code ', ''))

with open('chicago_zip_codes.txt', 'w') as f:
    for z in chicago_zip_codes:
        f.write(z + '\n')

# print(zip_to_neighb)

# candidates = [
#     60428,
#     60429,
#     # 60631, 60642, 60616, 60093, 60077, 60527, 60469, 60120,
#     # 60607, 60644, 60827, 60645, 60714, 60062, 60624, 60074, 60612, 60402,
#     # 60172, 60452, 60176, 60625, 60647, 60641, 60646, 60606, 60661, 60477,
#     # 60133, 60602, 60601, 60613, 60103, 60478, 60654, 60525, 60192, 60459,
#     # 60523, 60605, 60609, 60803, 60610, 60126, 60643, 60455, 60633, 60131,
#     # 60618, 60056, 60482, 60614, 60621, 60476, 60804, 60638, 60195, 60657,
#     # 60637, 60534, 60611, 60639, 60458, 60016, 60091, 60558, 60107, 60438,
#     # 60162, 60634, 60608, 60173, 60130, 60067, 60007, 60153, 60620, 60619,
#     # 60193, 60656, 60005, 60628, 60018, 60615, 60626, 60651, 60632, 60623,
#     # 60706, 60659, 60630, 60010, 60053, 60439, 60603, 60089, 60406, 60521,
#     # 60164, 60480, 60425, 60068, 60640, 60649, 60636, 60617, 60473, 60660,
#     # 60622, 60426, 60430, 60409, 60546, 60712, 60163, 60418, 60707, 60004,
#     # 60453, 60305, 60629, 60419, 60304, 60443, 60008, 60025, 60090, 60604,
#     # 60015, 60076, 60445, 60475, 60465, 60655, 60472, 60456, 60666, 60652,
#     # 60415, 60411, 60302, 60457, 60805, 60104, 60202, 60471, 60513, 60201,
#     # 60169, 60464, 60462, 60194, 60501, 60022, 60026, 60154, 60301, 60160,
#     # 60467, 60203, 60171, 60653, 60487, 60423, 60165, 60463, 60070, 60466,
#     # 60526, 60155, 60043, 60118, 60035, 60422, 60461
# ]

# # chicago_regions_and_zips = dict()

regions = {
    'North': [],
    'Central': [],
    'South': [],
    'Far South': [],
    'Southwest': [],
    'West': [],
    'Northwest': []
}

for z in chicago_zip_codes:
    region = 'null'

    while region not in regions.keys():
        print('Zip code is {}.'.format(z))
        region = input(
            'Choose a region [North, Central, South, Far South, Southwest, West, Northwest]: '
        )

    regions[region].append(z)

with open('regions.json', 'w') as f:
    json.dump(regions, f)
