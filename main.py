#!/usr/bin/env python
# coding: utf8

'''
Dependencies: python-twitter, telegraph, python-markdown
'''

import twitter
import sys

from telegraph import Telegraph
from markdown import markdown


'''
Twitter OAuth data
'''

access_token = 'access_token '
access_secret = 'access_secret'
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'

'''
Initialization for both twitter and telegraph APIs'
'''

telegraph = Telegraph()

api = twitter.Api(consumer_key = consumer_key,
                  consumer_secret = consumer_secret,
                  access_token_key = access_token,
                  access_token_secret = access_secret)

user = api.VerifyCredentials(include_entities=False, skip_status=True, include_email=False)



#debug function, testing if we're in
def post(tweet):
  if len(tweet)<=140:
    status = api.PostUpdate(tweet)
    print('Tweet "'{0}'" was published.'.format(tweet))
  else:
    print('Error! Tweet length more than 140 characters.')
    sys.exit()
  pass


#updating twitter status
def update_status(url):
  api.UpdateProfile(profileURL=url)
  print('Profile URL updated successfully')
  sys.exit()
  pass

#dummy function, skeleton for posting function
def new_post(content):
  telegraph.create_account(short_name='test')
  response = telegraph.create_page(
    'Hey',
    html_content=markdown_to_html(content)
    )
  print('http://telegra.ph/{}'.format(response['path']))
  pass

#converts input text in markdown to html
def markdown_to_html(file_name):
  fp = open(file_name)
  contents = fp.read()
  print(markdown(contents, output_format = 'html5'))
  fp.close()
  pass

#currently deep debuging no idea whats going on here
def main(content):
  #post(content)
  #update_status(content)
  print('{0} | @{1}'.format(user.name, user.screen_name))
  pass

if __name__ == '__main__':
  main(sys.argv[1])

'''
TODOs: 

try

from prompt_toolkit import prompt

prompt('> ', multiline=True)

'''