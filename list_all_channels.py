#-*- coding: utf8  -*-
import os
from slackclient import SlackClient

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def get_user(userid):
    """get real name from user info"""        
    api_call = slack_client.api_call(
        'users.info',
        user = userid)
    if api_call.get('ok'):
        user =  api_call.get('user')
        return user.get('real_name')

# Public
print 'Get Public Channels...'
api_call = slack_client.api_call('channels.list')
for chn in api_call['channels']:
	#print chn
	print '*', chn['name'], chn['id']

# Private
print 'Get Private Channels...'
api_call = slack_client.api_call('groups.list')
for chn in api_call['groups']:
	#print chn
	print '*', chn['name'], chn['id']
  
# IM
print 'Get IM...'
api_call = slack_client.api_call('im.list')
for chn in api_call['ims']:
        print '*', chn['user'], chn['id'], get_user(chn['user'])

# MPIM
print 'Get MPIM...'
api_call = slack_client.api_call('mpim.list')
for chn in api_call['groups']:
        print '*', chn['name'], chn['id']

