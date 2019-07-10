from django.shortcuts import render
import requests


def save_user_profile(backend, response, *args, **kwargs):
    access_token = response['access_token']

    if backend.name == 'vk-oauth2':
        api_url = requests.get('https://api.vk.com/method/friends.get',
                                params={
                                    'access_token': access_token,
                                    'count': 5,
                                    'fields': 'nickname',
                                    'order': 'random',
                                    'v': 5.92,
                                })
        data = api_url.json()['response']['items']
        result = [item['first_name'] for item in data]
        fileWithNames(result)
        print(result)


def fileWithNames(result):
    with open('fileWithNames.txt', 'w') as file:
        print(*result, file=file, sep="\n")
