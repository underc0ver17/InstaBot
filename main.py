import argparse

from instabot import Bot
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

Green = Fore.LIGHTGREEN_EX
Magenta = Fore.LIGHTMAGENTA_EX
Cyan = Fore.LIGHTCYAN_EX
Red = Fore.LIGHTRED_EX

def display_banner():
    banner_text = ''' 
  _____           _        ____        _   
 |_   _|         | |      |  _ \      | |  
   | |  _ __  ___| |_ __ _| |_) | ___ | |_ 
   | | | '_ \/ __| __/ _` |  _ < / _ \| __|
  _| |_| | | \__ \ || (_| | |_) | (_) | |_ 
 |_____|_| |_|___/\__\__,_|____/ \___/ \__|

InstaBot 1.0
Coded by underc0ver17
https://github.com/underc0ver17
                                      
    '''
    print(banner_text)

def get_arguments():
    parser = argparse.ArgumentParser(description=display_banner())

def main():

    bot = Bot()
    bot.login(username=input(Green + "Username: "),password=input(Green + "Password: "))

    User_Choice = input(Green + "[*] What do you want to do (Post_Photo, Follow, Unfollow, Send_Message, Following_List, Followers_List, Block_User): ")

    if User_Choice == str("Post_Photo"):
        print(Red + "You will need to upload the image file here first!")
        user_photo = input(Green + "[*] Image File name: ")
        photo_caption = input(Green + "[*] Caption: ")
        bot.upload_photo(user_photo,caption=photo_caption)

    if User_Choice == str("Follow"):
        user_follow = input(Green + "[*] Who do you want to follow?: ")
        bot.follow(user_follow)

    if User_Choice == str("Unfollow"):
        user_unfollow = input(Green + "[*] Who do you want to unfollow?: ")
        bot.unfollow(user_unfollow)

    if User_Choice == str("Send_Message"):
        message_recipient = input(Green + "[*] Who would you like to send a message to?(If multiple, add comma. Jon, Mack): ")
        user_message = input(Green + "[*] What is the message?: ")
        bot.send_message(user_message,[message_recipient])

    if User_Choice == str("Following_List"):
        user_following = input(Green + "[*] Who's following list do you want to see?(May not work if user is private): ")
        followings = bot.get_user_following(user_following)
        for following in followings:
            print(bot.get_user_info(following))

    if User_Choice == str("Followers_List"):
        user_followers = input(Green + "[*] Who's followers list do you want to see?(May not work if user is private): ")
        followers = bot.get_user_followers(user_followers)
        for follower in followers:
            print(bot.get_user_info(follower))

    if User_Choice == str("Block_User"):
        block_user = input(Green + "[*] Who do you want to block?: ")
        bot.block(block_user)

    def main(error):
        restart = input(Green + "[*] Do you want to do something else?(Yes/No): ").lower()
        if restart == str("yes"):
            main()

        if restart == str("no"):
            exit()
        else:
            print(Red + "Error, answer not recognized. Try again")
            main(error)
    

main()
