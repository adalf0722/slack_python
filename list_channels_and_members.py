#-*- coding: utf8  -*-
import os
from slackclient import SlackClient

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
BOT_NAME = 'bot'
USER = {}

api_call = slack_client.api_call('users.list')
if api_call.get('ok'):
	# retrieve all users
	users = api_call.get('members')
	for user in users:
		DESC = 'User'
		if 'name' in user and BOT_NAME in user.get('name') :
			DESC = 'Bot'
		USER[str(user.get('id'))] = str(user['name'])
else:
	print("could not find bot user with the name " + BOT_NAME)


# Public
print 'Public Channels...'
api_call = slack_client.api_call('channels.list')
for chn in api_call['channels']:
	#print chn
	print 'Public Channel:', chn['name'], chn['id']
	for member in chn['members']:
		print '*****member:', member, USER[str(member)]

# Private
print 'Private Channels...'
api_call = slack_client.api_call('groups.list')
for chn in api_call['groups']:
	#print chn
	print 'Private Channel:', chn['name'], chn['id']
	for member in chn['members']:
		print '*****member:', member, USER[str(member)]
