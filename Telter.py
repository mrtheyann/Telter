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

access_token = 'access_token'
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

def confirm_mode():
  html = set(['html', 'h', 'HTML', 'H'])
  markdown = set(['markdown', 'm', 'md', 'MD'])

  while True:
    mode = input('> ').lower()
    if mode in markdown:
      return True
    elif mode in html:
      return False
    else:
      print("Please, respond with 'html' or 'markdown'")


#Creating telegraph post with markdown formatting
def new_post(title, content, mode):
  if mode is True:
    content = markdown(content, output_format='xhtml5')

  telegraph.create_account(short_name=user.screen_name)
  response = telegraph.create_page(
    author_name='{0} | @{1}'.format(user.name, user.screen_name),
    title=title,
    html_content=content
    )
  
  link = response['path']
  print(content)
  return 'http://telegra.ph/{}'.format(link)

#Updating twitter status
def update_status(url):
  api.UpdateProfile(profileURL=url)
  print('Profile URL updated successfully')
  sys.exit()
  pass

#Main controller
def main():
  print('Enter the title of your article:')
  title = prompt('> ')
  
  print('Enter the markup format (html/markdown):')
  mode = confirm_mode()
  print(mode)

  print('Enter the content of your article.' '\n'
   'Once done, press Meta+Enter (Or Escape followed by Enter) in order to accept the input.')


  content = prompt('> ', multiline=True) 
  post = new_post(title, content, mode)

  print(post)
  update_status(post)

if __name__ == '__main__':
  main()