# Telter

### Telter is an CLI utility for an inline blog posts

Telter uses markdown as the main markup tool
It quite limited in [tags](http://telegra.ph/api#NodeElement) but it's more than enough for a comfortable writing

![Telter](http://i.imgur.com/q7UMfmp.png)

Once submitted, it would update your Twitter profile link to your article

### Install  
Open *Terminal*:  
```bash
sudo pip install twitter telegraph
sudo pip install markdown prompt_toolkit
git clone https://github.com/mrtheyann/Telter.git
chmod +x Telter/Telter
```

### Create Twitter Application
+ Go to [Twitter.Apps](https://apps.twitter.com/app/new)
+ Fill in all fields
+ Push *Create...* button  

### Configuration  
+ Go to *Key and Access Tokens* page for your application
+ Generate new *Access Token*
+ Fill *access_token*, *access_token_secret*, *consumer_key*, *consumer_secret* fields in *Telter* file

##### Cygwin is currently non-supportable
##### Still fuzzy and buggy
