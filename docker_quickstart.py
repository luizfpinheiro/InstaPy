import random
from instapy import InstaPy

# Write your automation here
# Stuck ? Look at the github page or the examples in the examples folder

insta_username = 'username'
insta_password = 'pass'

dont_like = ['fotografico', 'book', 'ensaio', 'photoshoot']
ignore_words = ['fotografico', 'book', 'ensaio', 'photoshoot']
friend_list = ['friend1', 'friend2', 'friend3']

# If you want to enter your Instagram Credentials directly just enter
# username=<your-username-here> and password=<your-password> into InstaPy
# e.g like so InstaPy(username="instagram", password="test1234")

bot = InstaPy(username=insta_username, password=insta_password, selenium_local_session=False)
bot.set_selenium_remote_session(selenium_url='http://selenium:4444/wd/hub')
bot.login()
bot.set_relationship_bounds(enabled=True,
                potency_ratio=None,
                delimit_by_numbers=True,
                max_followers=5000,
                max_following=50000,
                min_followers=250,
                min_following=2)
                  
# bot.set_do_comment(True, percentage=10)
# bot.set_comments(['Cool!', 'Awesome!', 'Nice!'])
bot.set_dont_include(friend_list)
bot.set_dont_like(dont_like)
#bot.set_ignore_if_contains(['ensaio, fotográfico, fotografia'])
# bot.like_by_tags(['#fender', '#prsguitar', #guitarhero'], amount=100)

# curtir imagens do tipo especifico
# bot.session.like_from_image(url='https://www.instagram.com/p/BhH4DoQlfRs/', amount=10, media='Photo')

bot.set_do_follow(enabled=True, percentage=80, times=2)

# curtir posts que utilizaram as tags-location especificas
#bot.like_by_locations(['213088733/brasilia-brazil/', '224768052/taguatinga-federal-district/'], amount=32)

usernames = ['lxfidalgo','thigrafias', 'bsb.photograph', 'miike.ph', 'thaislimafotos', 'giovanakarimeretratos', 'andre_esf', 'laricwsphotography', 'caioc.jpg', 'thirodrigo']

# seguir seguidores de um perfil especifico
bot.follow_user_followers(usernames, amount=11, randomize=True, sleep_delay=random.randint(55,110))
#seguir pessoas que curtiram as ultimas fotos de um perfil especifico
bot.follow_likers(usernames, amount=82)

bot.end()
