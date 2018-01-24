import os
from slackclient import SlackClient

BOT_NAME = 'bot'
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

if __name__ == '__main__':
    api_call = slack_client.api_call('users.list')
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            DESC = 'User'
            real_name = 'None'

            if 'name' in user and BOT_NAME in user.get('name') :
                DESC = 'Bot'

            if user.get('real_name'):
                real_name = user.get('real_name')

            print(DESC + " ID for '" + user['name'] + "' (" + real_name + ") is " + user.get('id') + " and team_id is " + user['team_id'])
    else:
        print('could not find bot user with the name ' + BOT_NAME)

