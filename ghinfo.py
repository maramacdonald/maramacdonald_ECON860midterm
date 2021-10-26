import json
import requests
import pandas
import csv

df = pandas.DataFrame()


f = open("token1", "r")
token1 = f.read()
f.close()
#print(token1)

f = open("username", "r")
username = f.read()
f.close()
#print(username)

github_session = requests.Session()
github_session.auth = (username, token1)

userList = list(csv.reader(open("parsed_files/gitusersdata.csv")))

access_point = "https://api.github.com"

for rows in range(len(userList)):
	if rows > 0:
		idString = userList[rows][0]
		user_url = access_point + "/users/"+ idString
		ghdata = json.loads(github_session.get(user_url).text)
		#print(ghdata)

		gitid=ghdata['id']
		print(gitid)
		#avatar=ghdata['avatar']
		#print('avatar')
		url=ghdata['url']
		print(url)
		followers=ghdata['followers']
		print(followers)
		following=ghdata['following']
		print(following)
		repos=ghdata['public_repos']
		print(repos)
		#for repo in repos:
			#stars = repo.stargazers_count
			#	print(stars)
		name=ghdata['name']
		print(name)
		company=ghdata['company']
		print(company)
		blog=ghdata['blog']
		print(blog)
		location=ghdata['location']
		print(location)
		email=ghdata['email']
		print(email)
		hireable=ghdata['hireable']
		print(hireable)
		created_at=ghdata['created_at']
		print(created_at)
		updated_at=ghdata['updated_at']
		print(updated_at)
		bio=ghdata['bio']
		print(bio)


		df=df.append({
			'ID': gitid,
			#'Avatar URL': avatar,
			'URL': url,
			'Follower Count': followers,
			'Following Count': following,
			'Reposts': repos,
			'Name': name,
			'Company': company,
			'Blog': blog,
			'Location': location,
			'Email': email,
			'Hired Time': hireable,
			'Created At': created_at,
			'Last Update': updated_at,
			'Bio': bio,
			}, ignore_index = True)

df.to_csv("parsed_files/ghinfo.csv", index=False)





