#!/usr/bin/env python
# coding: utf8

'''
Dependencies: python-twitter, telegraph, python-markdown, prompt_toolkit
'''

import twitter
import sys

from telegraph import Telegraph
from markdown import markdown
from prompt_toolkit import prompt

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


#updating twitter status
def update_status(url):
  api.UpdateProfile(profileURL=url)
  print('Profile URL updated successfully')
  sys.exit()
  pass

#dummy function, skeleton for posting function
def new_post(title, content):
  telegraph.create_account(short_name=user.screen_name)
  
  response = telegraph.create_page(
    author_name='{0} | @{1}'.format(user.name, user.screen_name),
    title,
    html_content=markdown(content, output_format='xhtml5')
    )
  
  print('http://telegra.ph/{}'.format(response['path']))
  pass


#currently deep debuging no idea whats going on here
def main():
  print('Enter the title of your article:')
  title = prompt('> ')
  print ('''
Enter the content of your article.
Once done, press Meta+Enter (Or Escape followed by Enter) in order to accept the input.''')

  content = prompt('> ', multiline=True) 
  new_post(title, content)
  pass

if __name__ == '__main__':
  main()
