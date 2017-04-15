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


#Updating twitter status
def update_status(url):
  api.UpdateProfile(profileURL=url)
  print('Profile URL updated successfully')
  sys.exit()
  pass

#Creating telegraph post
def new_post(title, content):
  telegraph.create_account(short_name=user.screen_name)
  response = telegraph.create_page(
    author_name='{0} | @{1}'.format(user.name, user.screen_name),
    title=title,
    html_content=markdown(content, output_format='xhtml5')
    )
  print('http://telegra.ph/{}'.format(post))
  return response['path']


#Main controller
def main():
  print('Enter the title of your article:')
  title = prompt('> ')
  print('Enter the content of your article.' '\n'
   'Once done, press Meta+Enter (Or Escape followed by Enter) in order to accept the input.'))

  content = prompt('> ', multiline=True) 
  post = new_post(title, content)
  update_status('http://telegra.ph/{}'.format(post))
  pass

if __name__ == '__main__':
  main()