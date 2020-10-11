from bs4 import BeautifulSoup
import requests
import csv

teamnames = {
    'Los Angeles Chargers': 'LAC',
    'Denver Broncos': 'DEN',
    'Las Vegas Raiders': 'LV',
    'Kansas City Chiefs': 'KC',
    'Los Angeles Rams': 'LAR',
    'Seattle Seahawks': 'SEA',
    'San Francisco 49ers': 'SF',
    'Arizona Cardinals': 'ARI',
    'Houston Texans': 'HOU',
    'Indianapolis Colts': 'IND',
    'Jacksonville Jaguars': 'JAX',
    'Tennessee Titans': 'TEN',
    'Carolina Panthers': 'CAR',
    'New Orleans Saints': 'NO',
    'Atlanta Falcons': 'ATL',
    'Tampa Bay Buccaneers': 'TB',
    'New England Patriots': 'NE',
    'Miami Dolphins': 'MIA',
    'New York Jets': 'NYJ',
    'Buffalo Bills': 'BUF',
    'Dallas Cowboys': 'DAL',
    'Philadelphia Eagles': 'PHI',
    'New York Giants': 'NYG',
    'Washington Football Team': 'WSH',
    'Minnesota Vikings': 'MIN',
    'Green Bay Packers': 'GB',
    'Detroit Lions': 'DET',
    'Chicago Bears': 'CHI',
    'Pittsburgh Steelers': 'PIT',
    'Cleveland Browns': 'CLE',
    'Baltimore Ravens': 'BAL',
    'Cincinnati Bengals': 'CIN',
    'LA Chargers': 'LAC',
    'Denver': 'DEN',
    'Las Vegas': 'LV',
    'Kansas City': 'KC',
    'LA Rams': 'LAR',
    'Seattle': 'SEA',
    'San Francisco': 'SF',
    'Arizona': 'ARI',
    'Houston': 'HOU',
    'Indianapolis': 'IND',
    'Jacksonville': 'JAX',
    'Tennessee': 'TEN',
    'Carolina': 'CAR',
    'New Orleans': 'NO',
    'Atlanta': 'ATL',
    'Tampa Bay': 'TB',
    'New England': 'NE',
    'Miami': 'MIA',
    'Buffalo': 'BUF',
    'Dallas': 'DAL',
    'Philadelphia': 'PHI',
    'Washington': 'WSH',
    'Minnesota': 'MIN',
    'Green Bay': 'GB',
    'Detroit': 'DET',
    'Chicago': 'CHI',
    'Pittsburgh': 'PIT',
    'Cleveland': 'CLE',
    'Baltimore': 'BAL',
    'Cincinnati': 'CIN'
}

StartEm = []
SitEm = []
Enigma = []
RB = []
WR = []
Flex = []
TE = []
QB = []
K = []
DST = []
positions = ['quarterbacks', 'wide-receivers', 'running-backs', 'tight-ends', 'kickers', 'defenses']
scoring = ''


def getWeek():
    url = 'http://nfl.com/schedules/'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'html.parser')
    return soup.find('main').find('h2').text[12]


week = getWeek()
urls = ['https://www.nbcsports.com/washington/football-team/start-em-sit-em-best-fantasy-football-plays-week-' + week,
        'https://walterfootball.com/fantasy2020startsit.php',
        'https://fantasydata.com/start-em-sit-em-week-' + week,
        'https://www.nfl.com/news/nfl-fantasy-football-start-em-sit-em-week-' + week + '-'
        ]


class Player:
    def __init__(self, position, positivementions, negativementions, name, team, opponent):
        self.position = position
        self.positivementions = positivementions
        self.negativementions = negativementions
        self.name = name
        self.team = team
        self.opponent = opponent



def add(position, setting, name, team, opponent):
    while name.endswith('I'):
        name = name[0:-1]
    if name.endswith('JR.') or name.endswith('SR.') or name.endswith('Jr.') or name.endswith('Sr.') or name.endswith(
            'jr.') \
            or name.endswith('sr.'):
        name = name[0:-3]
    elif name.endswith('JR') or name.endswith('SR') or name.endswith('Jr') or name.endswith('Sr') \
            or name.endswith('jr') or name.endswith('sr'):
        name = name[0:-2]
    name = name.strip()
    if position == 'qb':
        if setting == 'start':
            QB.append(Player(position, 1, 0, name, team, opponent))
        else:
            QB.append(Player(position, 0, 1, name, team, opponent))
    elif position == 'rb':
        if setting == 'start':
            RB.append(Player(position, 1, 0, name, team, opponent))
        else:
            RB.append(Player(position, 0, 1, name, team, opponent))
    elif position == 'wr':
        if setting == 'start':
            WR.append(Player(position, 1, 0, name, team, opponent))
        else:
            WR.append(Player(position, 0, 1, name, team, opponent))
    elif position == 'te':
        if setting == 'start':
            TE.append(Player(position, 1, 0, name, team, opponent))
        else:
            TE.append(Player(position, 0, 1, name, team, opponent))
    elif position == 'k':
        if setting == 'start':
            K.append(Player(position, 1, 0, name, team, opponent))
        else:
            K.append(Player(position, 0, 1, name, team, opponent))
    else:
        if setting == 'start':
            DST.append(Player(position, 1, 0, name, team, opponent))
        else:
            DST.append(Player(position, 0, 1, name, team, opponent))


def compare(name, position, team, opponent, setting):
    if position == 'qb':
        match = 0
        for player in QB:
            if player.name == name and player.team == team and player.opponent == opponent:
                match = 1
                if setting == 'start':
                    player.positivementions += 1
                else:
                    player.negativementions += 1
                break
        if match == 0:
            add(position, setting, name, team, opponent)
    elif position == 'rb':
        match = 0
        for player in RB:
            if player.name == name and player.team == team and player.opponent == opponent:
                match = 1
                if setting == 'start':
                    player.positivementions += 1
                else:
                    player.negativementions += 1
                break
        if match == 0:
            add(position, setting, name, team, opponent)
    elif position == 'rb':
        match = 0
        for player in WR:
            if player.name == name and player.team == team and player.opponent == opponent:
                match = 1
                if setting == 'start':
                    player.positivementions += 1
                else:
                    player.negativementions += 1
                break
        if match == 0:
            add(position, setting, name, team, opponent)
    elif position == 'te':
        match = 0
        for player in TE:
            if player.name == name and player.team == team and player.opponent == opponent:
                match = 1
                if setting == 'start':
                    player.positivementions += 1
                else:
                    player.negativementions += 1
                break
        if match == 0:
            add(position, setting, name, team, opponent)
    elif position == 'k':
        match = 0
        for player in K:
            if player.name == name and player.team == team and player.opponent == opponent:
                match = 1
                if setting == 'start':
                    player.positivementions += 1
                else:
                    player.negativementions += 1
                break
        if match == 0:
            add(position, setting, name, team, opponent)
    else:
        match = 0
        for player in DST:
            if player.name == name and player.team == team and player.opponent == opponent:
                match = 1
                if setting == 'start':
                    player.positivementions += 1
                else:
                    player.negativementions += 1
                break
        if match == 0:
            add(position, setting, name, team, opponent)


def sort():
    for player in QB:
        if player.positivementions > player.negativementions:
            StartEm.append(player)
        elif player.positivementions < player.negativementions:
            SitEm.append(player)
        else:
            Enigma.append(player)
    for player in RB:
        if player.positivementions > player.negativementions:
            StartEm.append(player)
        elif player.positivementions < player.negativementions:
            SitEm.append(player)
        else:
            Enigma.append(player)
    for player in WR:
        if player.positivementions > player.negativementions:
            StartEm.append(player)
        elif player.positivementions < player.negativementions:
            SitEm.append(player)
        else:
            Enigma.append(player)
    for player in TE:
        if player.positivementions > player.negativementions:
            StartEm.append(player)
        elif player.positivementions < player.negativementions:
            SitEm.append(player)
        else:
            Enigma.append(player)
    for player in K:
        if player.positivementions > player.negativementions:
            StartEm.append(player)
        elif player.positivementions < player.negativementions:
            SitEm.append(player)
        else:
            Enigma.append(player)
    for player in DST:
        player.position = 'D/ST'
        if player.positivementions > player.negativementions:
            StartEm.append(player)
        elif player.positivementions < player.negativementions:
            SitEm.append(player)
        else:
            Enigma.append(player)


def quicksort(list, compare_func):
    quicksort_(list, 0, len(list) - 1, compare_func)
    return list


def quicksort_(list, leftPointer, rightPointer, compare_func):
    if leftPointer < rightPointer:
        finalPivot = part(list, leftPointer, rightPointer, compare_func)
        quicksort_(list, leftPointer, finalPivot - 1, compare_func)
        quicksort_(list, finalPivot + 1, rightPointer, compare_func)


def part(list, leftPointer, rightPointer, compare_func):
    pivot = list[rightPointer]
    i = leftPointer - 1
    for j in range(leftPointer, rightPointer):
        if compare_func(list[j], pivot):
            i += 1
            swap(list, i, j)
    swap(list, i + 1, rightPointer)
    return i + 1


def swap(list, one, two):
    temp = list[one]
    list[one] = list[two]
    list[two] = temp


def scrape(url):
    counter = 0
    setting = 'start'
    if url == 'https://www.nbcsports.com/washington/football-team/start-em-sit-em-best-fantasy-football-plays-week-' + week:
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'html.parser')
        for player in soup.find_all('li'):
            text = player.text
            name = ''
            opponent = ''
            team = ''
            if counter < 6:
                position = 'qb'
                if counter > 2:
                    setting = 'sit'
            elif counter < 12:
                position = 'rb'
                if counter > 8:
                    setting = 'sit'
            elif counter < 18:
                position = 'wr'
                if counter > 14:
                    setting = 'sit'
            elif counter < 22:
                position = 'te'
                if counter > 20:
                    setting = 'sit'
            else:
                position = 'dst'
                if counter > 23:
                    setting = 'sit'
            if position != 'dst':
                while text[0] != ',':
                    name += text[0]
                    text = text[1:]
                text = text[1:]
                while text[0] != '(':
                    team += text[0]
                    text = text[1:]
                opponent = text[1:]
                opponent = opponent[0:-1]
                while opponent[0] != ' ':
                    opponent = opponent[1:]
            elif position == 'dst':
                team += text[0]
                text = text[1:]
                while text[0].isupper() is False:
                    team += text[0]
                    text = text[1:]
                name = team
                opponent = text[7:]
                while opponent[0].isupper() is False:
                    opponent = opponent[1:]
                opponent = opponent[0:-1]
            add(position, setting, name.strip(), team.strip(), opponent.strip())
            counter += 1
    elif url == 'https://fantasydata.com/start-em-sit-em-week-' + week:
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'html.parser')
        for div in soup.findAll('div', class_='blog-post-container'):
            for element in div.findAll(['h4', 'strong']):
                if element.text == "Sit 'Em":
                    setting = 'sit'
                if element.name == 'strong':
                    text = element.text
                    name = ''
                    team = ''
                    while text[0] != '(':
                        name += text[0]
                        text = text[1:]
                    name = name.strip()
                    position = text[1:3].lower()
                    text = text[5:].strip()
                    while text[0:3] != 'at ' and text[0:3] != 'vs.':
                        team += text[0]
                        text = text[1:]
                    if text[0] == 'a':
                        opponent = text[3:-1]
                    else:
                        opponent = text[4:-1]
                    compare(name.strip(), position, teamnames[team.strip()], teamnames[opponent.strip()], setting)
    elif url == 'https://www.nfl.com/news/nfl-fantasy-football-start-em-sit-em-week-' + week + '-':
        for position in positions:
            setting = 'start'
            source = requests.get(url + position).text
            soup = BeautifulSoup(source, 'html.parser')
            for div in soup.findAll('div', class_='d3-l-col__col-8'):
                for strong in div.findAll('strong'):
                    if strong.text == "Sit 'em":
                        setting = 'sit'
                for info in div.findAll('div', class_='nfl-o-ranked-item__outer'):
                    if position != 'defenses':
                        team = ''
                        name = info.find('div', class_='nfl-o-ranked-item__title').text.strip()
                        position = info.find('div', class_='nfl-o-ranked-item__info').text
                        while position[0] != '·':
                            team += position[0]
                            position = position[1:]
                        position = position[2:].lower().strip()
                        opponent = info.find('div',
                                             class_='nfl-o-ranked-item nfl-o-ranked-item--reversed nfl-o-ranked-item--side-by-side').find(
                            'div', class_='nfl-o-ranked-item__title').text
                        while opponent[0].isupper() is False:
                            opponent = opponent[1:]
                        while opponent.endswith('s') is False and opponent.endswith('m') is False:
                            opponent = opponent[0:-1]
                    else:
                        name = info.find('div', class_='nfl-o-ranked-item__title').text.strip()
                        team = name
                        opponent = info.find('div',
                                             class_='nfl-o-ranked-item nfl-o-ranked-item--reversed nfl-o-ranked-item--side-by-side nfl-o-ranked-item--team-team').find(
                            'div', class_='nfl-o-ranked-item__title').text
                        while opponent[0].isupper() is False:
                            opponent = opponent[1:]
                        while opponent.endswith('s') is False and opponent.endswith('m') is False:
                            opponent = opponent[0:-1]
                    compare(name, position.lower().strip(), teamnames[team.strip()], teamnames[opponent], setting)


def getStarted():
    for url in urls:
        scrape(url)

    sort()
    quicksort(StartEm, lambda x, y: x.positivementions >= y.positivementions)
    quicksort(SitEm, lambda x, y: x.negativementions >= y.negativementions)

