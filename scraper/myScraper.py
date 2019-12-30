# Imports
import requests
from bs4 import BeautifulSoup


# Utils


def getLikesAndDislikes(soup):
    likes_and_dislikes = []
    french_titles = ["J'aime ce contenu", "Je n'aime pas ce contenu"]

    for title in french_titles:
        likes_and_dislikes.append(
            list(soup.find('button', title=title).children)[0].get_text())

    return likes_and_dislikes


def getLikes(soup):
    return int(''.join(getLikesAndDislikes(soup)[0].split()))


def getDislikes(soup):
    return int(''.join(getLikesAndDislikes(soup)[1].split()))


def getTags(soup):
    return [tag.get('content') for tag in
            list(soup.find_all('meta', property='og:video:tag'))]


def getTitle(soup):
    return soup.find('meta', property='og:title').get('content')


def getImageUrl(soup):
    return soup.find('meta', property='og:image').get('content')


def getDescription(soup):
    return soup.find('meta', property='og:description').get('content')


def getChannelId(soup):
    return soup.find('meta', itemprop='channelId').get('content')


def getDuration(soup):
    duration = soup.find('meta', itemprop='duration').get('content')

    letters = []
    for character in duration:
        if(character.isdigit() is False):
            letters.append(character)

    for letter in letters:
        duration = duration.replace(letter, ' ')

    duration = [int(element) for element in duration.split()]

    effective_duration = 0
    if(len(duration) == 1):
        effective_duration += duration[0]
    elif(len(duration) == 2):
        effective_duration += 60 * duration[0] + duration[1]
    elif(len(duration) == 3):
        effective_duration += 60 * 60 * \
            duration[0] + 60 * duration[1] + duration[2]

    return effective_duration


def getIsFamilyFriendly(soup):
    return soup.find('meta', itemprop='isFamilyFriendly').get('content')


def getUploadDate(soup):
    return soup.find('meta', itemprop='uploadDate').get('content')


def getDatePublished(soup):
    return soup.find('meta', itemprop='datePublished').get('content')


def getGenre(soup):
    return soup.find('meta', itemprop='genre').get('content')


def getViews(soup):
    return int(soup.find('meta', itemprop='interactionCount').get('content'))


def getChannelSubscribers(soup):
    sub_count_raw = soup.find('span', tabindex="0").get_text().split()
    sub_count = float(sub_count_raw[0].replace(',', '.'))
    if(len(sub_count_raw) >= 2):
        if(sub_count_raw[1] == 'k'):
            sub_power = 1000
        elif(sub_count_raw[1] == 'M'):
            sub_power = 1000000
    sub_count *= sub_power
    return int(sub_count)


def getChannelName(soup):
    return soup.find('meta', property='og:title').get('content')


def getFeatures(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    featuresGetters = [getLikes, getDislikes, getTags, getTitle,
                       getImageUrl, getDescription, getChannelId,
                       getDuration, getIsFamilyFriendly, getUploadDate,
                       getDatePublished, getGenre, getViews]
    featuresNames = ['likes', 'dislikes', 'tags', 'title',
                     'imageurl', 'description', 'channelid',
                     'duration', 'familyfriendly', 'uploaddate',
                     'datepublished', 'genre', 'views']

    features = {}
    for name, getter in zip(featuresNames, featuresGetters):
        features[name] = getter(soup)

    # channel_url = 'https://www.youtube.com/channel/' + features['channelid']
    # channel_page = requests.get(channel_url)
    # channel_soup = BeautifulSoup(channel_page.content, 'html.parser')

    # channelFeaturesGetters = [getChannelName, getChannelSubscribers]
    # channelFeaturesNames = ['channelname', 'subscribers']

    # for name, getter in zip(channelFeaturesNames, channelFeaturesGetters):
    #     features[name] = getter(channel_soup)

    return features


# print(getFeatures())
