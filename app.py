from flask import Flask , render_template, request
from selenium import webdriver
import time
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




app = Flask(__name__)

# # data = (
# #     ('channu','jkd','1234'),
# #     ('channu','jkd','1234'),
# #     ('channu','jkd','1234')
# # )

# name=['ml','fsds','1234']
# mentor=['alex','sudh','kiddo']
# price=['123','567','234','787']

# allitems = zip(name,mentor,price)

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("one.html")


@app.route("/all",methods=['POST'])
def Allcourse():
        # client = pymongo.MongoClient("mongodb+srv://channu:123@cluster0.8jieu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        # db = client.test
        # db= client['ChannauDb']
        # col = db['machine_learning_courses']

        # scraping website without opeaning it
        option = webdriver.ChromeOptions()
        option.add_argument('headless')

        # chrome website driver
        driver = webdriver.Chrome(executable_path='C:\\Users\\Channabasav Angadi\\Downloads\\chromedriver.exe',options=option)
        driver.maximize_window()

        # getting user input for search
        # string = input("enter the course site").replace(' ','-')
        # capitalize = string.title()

        searchString = request.form['content'].replace(' ','-')
        serachtext = searchString.title()
        driver.get("https://courses.ineuron.ai/category/"+serachtext)

        # making selenium to scroll hole window
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        driver.implicitly_wait(10)

        # Getting prefered items
        courses = driver.find_elements(By.XPATH,"//h5[contains(@class,'Course_course-title__2rA2S')]")
        prices = driver.find_elements(By.XPATH,"//div[contains(@class,'Course_course-price__3-3_U')]")
        mentors = driver.find_elements(By.XPATH,"//div[contains(@class,'Course_course-instructor__1bsVq')]")


        # adding scraped element into list containers
        course=[]
        mentor=[]
        price=[]
        for i in courses:
            course.append(i.text)
        for j in mentors:
            mentor.append(j.text)
        for k in prices:
            price.append(k.text)

            
        # deleting empty items from the list
        # del course[0:4]
        # del mentor[0:4]
        # del price[0:4]
        # zipping the list 
        # allitems=[]
        allzip = zip(course,mentor,price)
        # for a in list(allzip):
        #     allitems.append(a)


        heading = ('name','menotr','price')
        return render_template('onetable.html',heading=heading , data = allzip)


@app.route("/second",methods=['POST'])
def alldeatails():

    # scraping website without opeaning it
    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    # chrome website driver
    driver = webdriver.Chrome(executable_path='C:\\Users\\Channabasav Angadi\\Downloads\\chromedriver.exe',options=option)
    driver.maximize_window()

    # getting user input for search
    searchString1 = request.form['content'].replace(' ','-')
    serachtext1 = searchString1.title()
    driver.get("https://courses.ineuron.ai/"+serachtext1)

    # making selenium to scroll hole window
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    driver.implicitly_wait(10)

    # Getting prefered items
    coursesa = driver.find_elements(By.XPATH,"//h3[contains(@class,'Hero_course-title__1a-Hg')]")
    pricesa = driver.find_elements(By.XPATH,"//div[contains(@class,'CoursePrice_dis-price__3xw3G')]")
    mentorsa = driver.find_elements(By.XPATH,"//div[contains(@class,'InstructorDetails_left__3jo8Z')]/h5")
    conceptsa = driver.find_elements(By.XPATH,"//div[contains(@class,'CourseLearning_card__WxYAo card')]/ul/li")

    # adding scraped element into list containers
    coursed=[]
    mentord=[]
    priced=[]
    conceptd=[]
    for i in coursesa:
        coursed.append(i.text)
    for j in mentorsa:
        mentord.append(j.text)
    for k in pricesa:
        priced.append(k.text)
    for l in conceptsa:
        conceptd.append(l.text)


    # zipping the list 
    allzipd = zip(coursed,mentord,priced)

        
    headingd = ('Course','Mentor','What You Will learn','Price')
    return render_template('twotable.html',headingd=headingd ,con=allzipd)
 

if __name__ == "__main__":
    app.run(debug=True,port=2000)