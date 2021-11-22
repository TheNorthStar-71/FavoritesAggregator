import requests # here we import requests which allows us to get info from websites
from bs4 import BeautifulSoup # importing beautiful soup to parse through data
import pandas as pd # analyze data
import smtplib # allows you to send emails to people
import time # allows you to sleep a program and have it rerun after a period of time
import re # allows us to search for specifc words in a string
from datetime import date
from datetime import timedelta
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from requests import Session
from email.message import EmailMessage

#All the blogs
tim = 'https://tim.blog/'
ramit = 'https://www.iwillteachyoutoberich.com/blog/'
cal = 'https://www.calnewport.com/blog/'
scott = 'https://www.scotthyoung.com/blog/'
clear = 'https://jamesclear.com/articles'
altucher = 'https://jamesaltucher.com/blog/'
Jacobs = 'https://ajjacobs.com/articles-essays/'
graham = 'http://paulgraham.com/articles.html'
manson = 'https://markmanson.net/'

#i Don't know what this does
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36' }


#timBlog
def timNewBlogs():
    #code for the dates of the blogs
    #Dates are stored in strings in a list as timTime2
    #links are stored as strings in a list as timLink4
    pageTim = requests.get(tim, headers = headers)
    soupTime = BeautifulSoup(pageTim.content, 'html.parser')
    timTime = str(BeautifulSoup((str(soupTime.find_all('time', {'class': "entry-date published"}))),'lxml'))
    timTime2 = []
    for i in range(len(timTime)-8):
        if (timTime[i:i+8] == 'datetime'):
            timTime2.append(timTime[i+10:i+20])

    today = str(date.today())
    today1 = date.today()
    yesterday = str(today1 - timedelta(days=1))

    timTodayLinks = []
    Count1 = 0
    for i in timTime2:
        if ((today[-2:] == i[-2:]) or ( yesterday[-2:] == i[-2:])):
            timTodayLinks.append(i)
            Count1 +=1

    timLink = str(BeautifulSoup((str(soupTime.find_all('a', {'rel': "bookmark"}))),features="lxml"))
    timLink2 = ''
    for i in range(len(timLink)-4):
        if (timLink[i:i+4] == 'href'):
            timLink2 += (timLink[i+6:i+120])

    timLink3 = []
    end = None
    counter = 0
    for i in range(len(timLink2)-4):
        if (timLink2[i:i+4] == 'http'):
            #x = re.finditer('rel', timLink2)
            hello = [x.start() for x in re.finditer('rel', timLink2)]
            timLink3.append(timLink2[i:hello[counter]])
            counter +=1

    timLink4 = []
    for i in timLink3:
        if i not in timLink4:
            timLink4.append(i)

    actuallyNewBlogsTim = timLink4[:2]

    return(actuallyNewBlogsTim)

def ramitNewBlogs():
    #all links for ramit website
    pageRamit = requests.get(ramit, headers = headers)
    soupRamit = BeautifulSoup(pageRamit.content, 'html.parser')
    ramitLink = soupRamit.find_all('a')
    ramitAllLinks =[]

    for link in ramitLink:
        new_string = str(link)
        if (('blog' in new_string) & ('https://www.facebook.com/' not in new_string) & ('https://twitter.com/share' not in new_string) & ('https://plus.google.com/share?url' not in new_string) & ('category' not in new_string) & (link.get('href') not in ramitAllLinks) ):
            ramitAllLinks.append(link.get('href'))

    ramitAllLinks2 = []
    for i in ramitAllLinks:
        ramitAllLinks2.append('https://www.iwillteachyoutoberich.com' + str(i))

    ramitToCheck = ramitAllLinks2[1:3]

    return(ramitToCheck)

def calNewBlogs():
    #all links for Cal's website
    pageCal = requests.get(cal, headers = headers)
    soupCal = BeautifulSoup(pageCal.content, 'html.parser')
    calLink = soupCal.find_all('a', href = re.compile('blog'))
    calAllLinks =[]

    for link in calLink:
        new_string = str(link)
        for i in range(len(new_string)):
            if (new_string[i:i+5] == 'https') & ('#comments' not in new_string) & (link.get('href') not in calAllLinks) :
                calAllLinks.append(link.get('href'))

    calAllLinksActual = calAllLinks[1:3]

    return(calAllLinksActual)

def scottNewBlogs():
    #all links for scott's website
    pageScott = requests.get(scott, headers = headers)
    soupScott = BeautifulSoup(pageScott.content, 'html.parser')
    scottLink = soupScott.find_all('a', {'class':'entry-title-link'})
    scottAllLinks =[]

    for link in scottLink:
        new_string = str(link)
        for i in range(len(new_string)):
            if new_string[i:i+5] == 'https':
                scottAllLinks.append(link.get('href'))
    scottAllLinksActual = scottAllLinks[:2]

    return(scottAllLinksActual)

def clearNewBlogs():
    #all links for clear's website
    pageClear = requests.get(clear, headers = headers)
    soupClear = BeautifulSoup(pageClear.content, 'html.parser')
    clearLink = soupClear.find_all('a')
    clearAllLinks =[]

    for link in clearLink:
        new_string = str(link)
        for i in range(len(new_string)):
            if (new_string[i:i+5] == 'https'):
                clearAllLinks.append(link.get('href'))
    creativity = clearAllLinks[12]
    decisions = clearAllLinks[17]
    focus = clearAllLinks[22]
    habits = clearAllLinks[27]
    lifeLessons = clearAllLinks[32]
    Motivation = clearAllLinks[37]
    productivity = clearAllLinks[42]
    self_improve = clearAllLinks[47]
    All_new = []
    All_new.append(creativity)
    All_new.append(decisions)
    All_new.append(focus)
    All_new.append(habits)
    All_new.append(lifeLessons)
    All_new.append(Motivation)
    All_new.append(productivity)
    All_new.append(self_improve)

    listttt = []
    for a in All_new:
        listttt.append(f'{a}')

    return(listttt)


def altucherNewBlogs():
    #all links for altucher's website
    pageAltucher = requests.get(altucher, headers = headers)
    soupAltucher = BeautifulSoup(pageAltucher.content, 'html.parser')
    altucherLink = soupAltucher.find_all('a', href = re.compile('blog'))
    altucherAllLinks =[]

    for link in altucherLink:
        new_string = str(link)
        for i in range(len(new_string)):
            if new_string[i:i+5] == 'https':
                altucherAllLinks.append(link.get('href'))

    altucherAllLinksActual =altucherAllLinks[2:4]

    return(altucherAllLinksActual)

def grahamNewBlogs():
    #all links for graham's website
    pageGraham = requests.get(graham, headers = headers)
    soupGraham = BeautifulSoup(pageGraham.content, 'html.parser')
    grahamLink = soupGraham.find_all('a',  href = re.compile('.html'))
    grahamAllLinks =[]

    for link in grahamLink:
        new_string = str(link)
        for i in range(len(new_string)):
            if ('html' in new_string) & (link.get('href') not in grahamAllLinks) :
                grahamAllLinks.append(link.get('href'))

    grahamAllLinks2 = []
    for i in grahamAllLinks:
        grahamAllLinks2.append('http://paulgraham.com/'+i)

    grahamAllLinks2Actual = grahamAllLinks2[4:6]
    return(grahamAllLinks2Actual)

def masonNewBlogs():
    #all links for Manson's website
    pageManson = requests.get(manson, headers = headers)
    soupManson = BeautifulSoup(pageManson.content, 'html.parser')
    mansonLink = soupManson.find_all('a', {'rel':'bookmark'})
    mansonAllLinks =[]

    for link in mansonLink:
        new_string = str(link)
        for i in range(len(new_string)):
            if link.get('href') not in mansonAllLinks:
                mansonAllLinks.append(link.get('href'))

    mansonAllLinks2 = []
    for i in mansonAllLinks:
        mansonAllLinks2.append('https://markmanson.net'+i)

    mansonAllLinks2Actual = mansonAllLinks2[0:2]
    return(mansonAllLinks2)

def getALlPodcasts():
    # Start the session
    session = requests.Session()
    #this allows you to login to google podcasts

    # #This logs me into my page
    gmailId = '-----'
    passWord = '---------'

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(r'https://podcasts.google.com/subscriptions?sa=X&ved=0CAEQ6tUFahcKEwjgmdTI5IXuAhUAAAAAHQAAAAAQfg' + \
               'https://accounts.google.com/signin/v2/challenge/pwd?passive=1209600&continue=https%3A%2F%2Fpodcasts.google.com%2F&followup=https%3A%2F%2Fpodcasts.google.com%2F&ec=GAZA2wM&flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=1&navigationDirection=forward&TL=AM3QAYar5Yna4v7-6bkia40yX9w9xbld9qbpJ-voiR4Gv5JGtWgm0Dc8hj7ziAq1' + \
               'https://podcasts.google.com/subscriptions')
    driver.implicitly_wait(15)

    loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
    loginBox.send_keys(gmailId)

    nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
    nextButton[0].click()

    passWordBox = driver.find_element_by_xpath(
        '//*[@id ="password"]/div[1]/div / div[1]/input')
    passWordBox.send_keys(passWord)

    nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
    nextButton[0].click()

    listOfPodcastTitles = []
    for x in driver.find_elements_by_class_name('kMNxad'):
        listOfPodcastTitles.append(x.text)

    listOfPodcastTitles2 =[]

    listOfPodcastLinks = []

    for i in driver.find_elements_by_class_name('jJ8Epb'):
        listOfPodcastLinks.append(i.get_attribute('href'))
    listOfPodcastLinks2 = []

    names_of_podcasts = []
    names_of_podcasts2 = []
    for a in driver.find_elements_by_class_name('ZTClBb'):
        names_of_podcasts.append(a.text)

    counter = 0
    for x in driver.find_elements_by_class_name("c5Vdrc"):
        if 'hours' in x.text:
            counter += 1
        listOfPodcastLinks2 = listOfPodcastLinks[:counter]
        listOfPodcastTitles2 = listOfPodcastTitles[:counter]
        names_of_podcasts2 = names_of_podcasts[:counter]

    t1 = list(zip(names_of_podcasts2, listOfPodcastTitles2))

    t2 = list(zip(t1,listOfPodcastLinks2))


    return(t2)


def todays_WeekArticle():
    #all links for the Week's website
    headers1 = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    week = 'https://theweek.com/10things'

    pageWeek = requests.get(week, headers = headers1)
    soupWeek = BeautifulSoup(pageWeek.content, 'html.parser')
    weekLink = soupWeek.find_all('a')
    weekAllLinks =[]

    for link in weekLink:
        new_string = str(link)
        for i in range(len(new_string)):
            if str(link.get('href')) not in weekAllLinks:
                weekAllLinks.append(str(link.get('href')))

    weekAllLinks2 = []
    today = str(date.today())

    for i in weekAllLinks:
        if ((today[:4] in i) and ((today[-1:] == i[-6]) or (today[-2:] == i[-7:-6]))):
            weekAllLinks2.append('https://theweek.com'+str(i))

    return(weekAllLinks2)

def youtube_Aggreagte():
    # Start the session
    session = requests.Session()
    #this allows you to login to google podcasts

    # #This logs me into my page
    gmailId = '------'
    passWord = '------'

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(r'https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252Ffeed%252Fsubscriptions&hl=en-GB&flowName=GlifWebSignIn&flowEntry=ServiceLogin' + \
               'https://accounts.google.com/signin/v2/challenge/pwd?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252Ffeed%252Fsubscriptions&hl=en-GB&flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=1&navigationDirection=forward&TL=AM3QAYZNpA9y36YLzTiG4nUtG5IqfDMOGG-kgav_FgFAmZYKAot2FeG-lVYXqsWg' + \
               'https://www.youtube.com/feed/subscriptions')

    driver.implicitly_wait(15)

    loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
    loginBox.send_keys(gmailId)

    nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
    nextButton[0].click()

    passWordBox = driver.find_element_by_xpath(
        '//*[@id ="password"]/div[1]/div / div[1]/input')
    passWordBox.send_keys(passWord)

    nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
    nextButton[0].click()

    #get all the video titles
    listOfVideosTitles = []
    for x in driver.find_elements_by_xpath('//*[@id ="video-title"]'):
        listOfVideosTitles.append(x.text)

    listOfVideosTitles2 =[]

    listOfVideosLinks = []


    for i in driver.find_elements_by_xpath('//*[@id ="video-title"]'):
        listOfVideosLinks.append(i.get_attribute('href'))
    listOfVideosLinks2 = []

    listOfVideosTitles3 =[]
    listOfVideosTitles4 =[]

    count = 0

    for qwe in driver.find_elements_by_xpath('//*[@class ="yt-simple-endpoint style-scope yt-formatted-string"]'):
        listOfVideosTitles3.append(qwe.text)

    for x in driver.find_elements_by_class_name("style-scope ytd-grid-video-renderer"):
        if 'hours' in x.text:
            count += 1
        listOfVideosLinks2 = listOfVideosLinks[:count]
        listOfVideosTitles2 = listOfVideosTitles[:count]
        listOfVideosTitles4 = listOfVideosTitles3[:count]


    newlistofVideos = list(zip(listOfVideosTitles2, listOfVideosLinks2))
    newlistofVideos2 = list(zip(listOfVideosTitles4, newlistofVideos))

    lisstttt = []
    for asd in newlistofVideos2:
        lisstttt.append(f'{asd}')


    return(lisstttt)


def getOtherLinks():
    Other_sites = {'linkForNewSpotify': 'https://spotifyreleaselist.netlify.app/',
                   'productHunt': 'https://www.producthunt.com/', 'reddit': 'https://www.reddit.com/',
                   'twitter': 'https://twitter.com/explore/tabs/trending',
                   'hackerNews': 'https://news.ycombinator.com/news',
                   'hackerNewsAsk': 'https://news.ycombinator.com/ask',
                   'harvardEmail': 'https://mail.google.com/mail/u/2/#inbox',
                   'regularGmail': 'https://mail.google.com/mail/u/1/#inbox',
                   'groupMe': 'https://web.groupme.com/chats', 'slickDeals': 'https://slickdeals.net/',
                   'offerUp': 'https://offerup.com/', 'facebookMarketPlace': 'https://www.facebook.com/marketplace/',
                   'linkForNewSpotify': 'https://spotifyreleaselist.netlify.app/'}

    newList = []
    for i, x in Other_sites.items():
        newList.append(f'{i}: {x}')

    return(newList)

#emailing yourself



#this is the process of emailing
def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('------', '------')

    tim = timNewBlogs()
    tim2 = ''
    for i in tim:
        tim2 = tim2 + i + '\n\n\n'
    ramit = ramitNewBlogs()
    ramit2 = ''
    for i in ramit:
        ramit2 = ramit2 + i + '\n\n\n'
    cal = calNewBlogs()
    cal2 = ''
    for i in cal:
        cal2 = cal2 + i + '\n\n\n'
    scott = scottNewBlogs()
    scott2 = ''
    for i in scott:
        scott2 = scott2 + i + '\n\n\n'
    clear = clearNewBlogs()
    clear2 = ''
    for i in clear:
        clear2 = clear2 + i + '\n\n\n'
    altucher = altucherNewBlogs()
    altucher2 = ''
    for i in altucher:
        altucher2 = altucher2 + i + '\n\n\n'
    graham=grahamNewBlogs()
    graham2 = ''
    for i in graham:
        graham2 = graham2 + i + '\n\n\n'
    mason=masonNewBlogs()
    mason2 = ''
    for i in mason:
        mason2 = mason2 + i + '\n\n\n'
    podcasts = list(getALlPodcasts())
    podcasts2 = ''
    for i in podcasts:
        podcasts2 = str(podcasts2) + str(i) + '\n\n\n'
    WeekArticle=todays_WeekArticle()
    WeekArticle2 = ''
    for i in WeekArticle:
        WeekArticle2 = WeekArticle2 + i + '\n\n\n'
    youtube=youtube_Aggreagte()
    youtube2 = ''
    for i in youtube:
        youtube2 = youtube2 + i + '\n\n\n'
    OtherLinks = getOtherLinks()
    OtherLinks2 = ''
    for i in OtherLinks:
        OtherLinks2 = OtherLinks2 + i + '\n\n\n'

    subject = 'Custom Morning Brief'
    body = f'Check the Links:\n\nTim Blogs:\n {tim2}\n\nRamit Rich Blogs:\n {ramit2}\n\nCal Newport Blogs:\n {cal2}\n\nScott Blogs:\n {scott2}\n\nClear Blogs:\n {clear2}\n\nAltucher Blogs:\n {altucher2}\n\nGraham Essays: {graham2}\n\nMason Blogs:\n {mason2}\n\nPodcasts:\n {podcasts2}\n\n10ThingsWeek:\n {WeekArticle2}\n\nYoutube Videos:\n {youtube2}\n\nOther sites:\n {OtherLinks2}'

    msg = f"Subject: {subject}\n\n{body}"

   
    fmt = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n{}'
    em = EmailMessage()
    to_ = '------'
    from_ = '------'
    em.set_content(fmt.format(to_, from_, subject, msg))
    em['To'] = to_
    em['From'] = from_
    em['Subject'] = subject
    server.send_message(em)
    print("hey email has been sent")

    server.quit()

send_email()
