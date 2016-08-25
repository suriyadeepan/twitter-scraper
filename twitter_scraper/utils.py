import pandas as pd


''' Get the list of urls from dataset '''
def get_urls(filename='seeds.csv'):
    df = pd.read_csv(filename,dtype=object)
    tweet_ids = df.ix[:,-1]
    return [ 'https://twitter.com/anyuser/status/' + tweet_id for tweet_id in list(tweet_ids) ]

''' extract tweet_id from url '''
def url2id(url):
    return url.split('/')[-1].replace('/','')

