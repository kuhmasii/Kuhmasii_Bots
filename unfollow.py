import tweepy
import bot

api_key, api_sec  = bot.getAPIkeys()
access = bot.getAccess(api_key, api_sec)

def my_followers(username):
    
    list_names = []
    list_username = []

    for pals in tweepy.Cursor(
        access.get_followers, screen_name=username).items(100):
        
        list_names.append(pals.name)
        list_username.append(pals.screen_name)

    return list_names, list_username

def unfollow_nonfollowers(username, name):
    list_of_unfollowers = []

    dont_unfollower = ["osca_ado_ekiti",'TDevCommunityNG', "restframework", "Fransunisoft"]
    _name, _scr_name = my_followers(name)
    _scr_name.extend(dont_unfollower)
    
    for _unfollow in tweepy.Cursor(
        access.get_friends, screen_name=username).items(100):

            # checking whether the user is a 
            # verified user or a well known 
            # account yet to be verified
            if _unfollow.followers_count < 2000 and _unfollow.verified == False:

                # checking whether user is following the authenticated user
                if _unfollow.name not in _name and _unfollow.screen_name not in _scr_name:
                    list_of_unfollowers.append(
                        f"{_unfollow.screen_name}, username: {_unfollow.name}")
                    
                    print(f"Ready to unfollow {_unfollow.name}")
                    
                    # unfollowing non-followers
                    access.destroy_friendship(
                        screen_name=_unfollow.screen_name, user_id=_unfollow.id
                    )

    return list_of_unfollowers

unfollow = unfollow_nonfollowers('kuhmasii', "kuhmasii")
print(unfollow)