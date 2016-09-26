import config as c 
import tweepy
import datetime
import time
import random
###authentication, you have to do this once for every app###
def authenticate():
	auth = tweepy.OAuthHandler(c.c_key, c.c_secret)
	auth.set_access_token(c.a_key, c.a_secret)
	api = tweepy.API(auth)

def create_phraselist():
	phraselist=['Infinite is the best','Infinite forever','Infinite fighting','I <3 this comeback']
	return phraselist

def create_phrasefile(inputfile,phraselist):
	with open(inputfile, 'w') as f:
		for item in phraselist:
			f.write(item + '\n')

def post_tweets(api,count,tweet):
	###post tweet if length does not exceed 140 chars###
	### post using randomized interval
	if len(tweet)<140:
		api.update_status(tweet)
		minsecs,maxsecs,incr=intervals()
		sleepy_time = random.randrange(minsecs,maxsecs,incr)
		print (str(sleepy_time) + ' seconds until the next tweet')
		time.sleep(sleepy_time) #tweet every [interval] minute(s)
		return sleepy_time
def tweet_input():
	### provide required tweet content here###
	mention='@Inspirit4You'
	hash1='#인피니트'
	hash2='#태풍'	
	return mention,hash1,hash2

def intervals():
	### provide desired tweeting intervals	
	minsecs=60 # interval btw 2 tweets is min 1min
	maxsecs=120 # interval btw 2 tweets is max 2min
	incr=2 # intervals vary between 1 and 2 min, in 2s increments
	return minsecs,maxsecs,incr

def times(start,end):
	### calculate time difference between given start and end datetimes###
	timediffs=end-start
	timediff=int(timediffs.seconds/60)
	return timediff

def info_start(start,end):
	##print welcome text, tweeting date ranges, start and ending times
	datenow=datetime.datetime.utcnow().strftime
	startdate=start.strftime('%Y-%m-%d')
	starttime=start.strftime(' %H:%M')
	enddate=end.strftime('%Y-%m-%d')
	endtime=end.strftime(' %H:%M')
	print('*'*10)
	print ('Hello, my name is inft_pie, I\'m here to help Infinite win The Show')
	print ('Today is '+datenow('%Y-%m-%d'))
	print ('I\'ll start tweeting on %s, at %s' % (startdate,starttime))
	print (' and I\'ll stop on %s, at %s' % (enddate,endtime))
	print('*'*10)

def info_instance(i):
	###print current time and current instance number###
	datenow=datetime.datetime.utcnow().strftime
	print('*'*10)
	print ('The current time is '+str(datenow(' %H:%M'))+', I\'ll keep tweeting')
	print ('This is instance: '+str(i))

def write_instance():
	with (open('instance.txt','w')) as f: 
		f.write('0')

def load_instance():
	with (open('instance.txt','r')) as f:
		for line in f:
			last_instance=int(line)
	return last_instance

def tweeting_now(api,start,end,timediff,last_instance):
	### provide info on start and end times###
	info_start(start,end)
	mention,hash1,hash2=tweet_input()
	if datetime.datetime.now() > start:
		print ('Let\'s go!')
		for i in range(last_instance,last_instance+timediff,1):
			if datetime.datetime.now() < end:
				###provide info on current instance and time to next tweet###
				info_instance(i)
				line = random.choice(open('inft_phrases.txt').readlines())
				tweet=mention+' '+line+' '+hash1+' '+str(i)+' '+hash2
				sleepy_time=post_tweets(api,i,tweet)
			else:
				instance=i
				with (open('instance.txt','w')) as f: 
					f.write(str(instance))
				print('Time is up! Well done, inft_pie')
				return last_instance

def main():
	#phraselist=create_phraselist()
	#create_phrasefile('inft_phrases.txt',phraselist)

	###authenticate###
	auth = tweepy.OAuthHandler(c.c_key, c.c_secret)
	auth.set_access_token(c.a_key, c.a_secret)
	api = tweepy.API(auth)

	###specify start and end dates###
	start=datetime.datetime(2016,9,25,14,25)
	end=datetime.datetime(2016,9,25,15,34)
	timediff=times(start,end)
	### posts a tweet from a dataset every [interval] minutes 
	#between specified [start] and [end] datetimes
	print (start,end,timediff)
	#write_instance()
	last_instance=load_instance()
	print (last_instance)
	last_instance=tweeting_now(api,start,end,timediff,last_instance)

if __name__ == "__main__":
	main() 



###loops through tweets in a timeline printing the text and ignoring images etc###
#for status in infinite_timeline:
#	print(status.text.encode('utf8'))



#infinite_timeline = api.user_timeline("infiniteupdates")
#api.retweet(infinite_timeline[0].id)
# myself = api.me()
# print (myself.screen_name)
# print (datetime.datetime.now())
# start=datetime.datetime(2016,9,25,11,37)
# end=datetime.datetime(2016,9,25,11,39)
# print (start)
# print (end)
#post_tweets(api,start,end,'inft_phrases.txt',interval,mention,hash1,hash2,minsecs,maxsecs,incr)
