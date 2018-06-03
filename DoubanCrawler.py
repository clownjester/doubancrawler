"""
任务1：获取每个地区、每个类型页面的URL
实现函数构造对应类型和地区的URL地址
"""
def getMovieUrl(category,location):
	url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影," + category + "," + location
	return url


#任务2: 获取电影页面 HTML

import requests
import expanddouban
from bs4 import BeautifulSoup
import csv
"""
任务3: 定义电影类
"""
class Movie(object):

	def __init__(self,name,rate,location,category,info_link,cover_link):
		self.name = name
		self.rate = rate
		self.location = location
		self.category = category
		self.info_link = info_link
		self.cover_link = cover_link
		self.info = name + "," + rate + "," + location + "," + category + "," 
		          + info_link + "," + cover_link 

	def show_info(self):
		print("name:{} , rate:{} , location:{} , category:{}".format(self.name,self.rate,
			self.location,self.category))
		print("info_link:{}".format(self.info_link))
		print("cover_link:{}".format(self.cover_link))

"""
任务4: 获得豆瓣电影的信息
通过URL返回的HTML，我们可以获取网页中所有电影的名称，评分，海报图片链接和页面链接，同时我们在任务1构造
URL时，也有类型和地区的信息，因为我们可以完整的构造每一个电影，并得到一个列表。
实现以下函数
return a list of Movie objects with the given category and location.
def getMovies(category, location)
	return []
提示：你可能需要在这个任务中，使用前三个任务的代码或函数。
"""
#引入bs4的BeautifulSoup类进行网页导航
from bs4 import BeautifulSoup
#定义函数getMovies
def getMovies(category,location):
	lst_Movies =[]	#用于储存Movie的列表
	#根据要求创建html，转化为soup类型
	html = expanddouban.getHtml(getMovieUrl(category,location),loadmore = True,waittime = 1)
	soup = BeautifulSoup(html,"html.parser")
	#获取全部影片的连接标签
	movie_items = soup.find_all("a",class_="item")
	#遍历每一部影片，获取信息，创建Movie实例,加入列表
	for item in movie_items:
		info_link = item["href"]
		cover_link = item.div.span.img["src"]
		name = item.p.find("span",class_="title").string
		rate = item.p.find("span",class_="rate").string
		m = Movie(name,rate,category,location,info_link,cover_link)
		lst_Movies.append(m)
	return lst_Movies
"""
test
cate = input("category: ")
loc = input("location: ")
lst = getMovies(cate,loc)
for m in lst:
	m.show_info()"""

"""
任务5: 构造电影信息数据表
从网页上选取你最爱的三个电影类型，然后获取每个地区的电影信息后，我们可以获得一个包含三个类型、所有地区，
评分超过9分的完整电影对象的列表。将列表输出到文件 movies.csv，格式如下:
肖申克的救赎,9.6,美国,剧情,https://movie.douban.com/subject/1292052/,https://img3.doubanio.com/
view/movie_poster_cover/lpst/public/p480747492.jpg
霍伊特团队,9.0,香港,动作,https://movie.douban.com/subject/1307914/,https://img3.doubanio.com/
view/movie_poster_cover/lpst/public/p2329853674.jpg
....
"""
all_areas = ["中国大陆","美国","香港","台湾","日本","韩国","英国","法国","德国","意大利","西班牙",
             "印度","泰国","俄罗斯","伊朗","加拿大","澳大利亚","爱尔兰","瑞典","巴西","丹麦"]
all_movies = []
sifi_movies_info = [] 		#储存科幻片信息的列表
sus_movies_info = []		#储存悬疑片信息的列表
act_movies_info = []		#储存动作片信息的列表
#获取科幻片列表，整理为信息列表

#获取悬疑片列表，整理为信息列表

#获取动作片列表，整理为信息列表

"""
任务6: 统计电影数据
统计你所选取的每个电影类别中，数量排名前三的地区有哪些，分别占此类别电影总数的百分比为多少？
你可能需要自己把这个任务拆分成多个步骤，统计每个类别的电影个数，统计每个类别每个地区的电影个数，排序找
到最大值，做一定的数学运算等等，相信你一定可以的！
请将你的结果输出文件 output.txt
"""
