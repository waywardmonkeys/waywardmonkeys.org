AUTHOR = u"Bruce Mitchener, Jr."
SITENAME = u"Notes from a Wayward Monkey"
SITEURL = 'http://waywardmonkeys.org'

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

DEFAULT_CATEGORY = 'General'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Pages
PAGES = ()

# Blogroll
LINKS =  (('Dylan Foundry', 'http://dylanfoundry.org/'),
          ('Open Dylan', 'http://opendylan.org/'))

# Social widget
SOCIAL = (('icon-twitter', '@ArmyOfBruce', 'https://twitter.com/ArmyOfBruce'),)

TWITTER_USERNAME = 'ArmyOfBruce'

DEFAULT_PAGINATION = 10

SUMMARY_MAX_LENGTH = 200

THEME = 'theme'
