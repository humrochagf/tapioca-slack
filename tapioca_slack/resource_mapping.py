# coding: utf-8

RESOURCE_MAPPING = {
    # api
    'api_test': {
        'resource': 'api.test',
        'docs': 'https://api.slack.com/methods/api.test'
    },

    # auth
    'auth_test': {
        'resource': 'auth.test',
        'docs': 'https://api.slack.com/methods/auth.test'
    },

    # channels
    'channels_archive': {
        'resource': 'channels.archive',
        'docs': 'https://api.slack.com/methods/channels.archive'
    },
    'channels_create': {
        'resource': 'channels.create',
        'docs': 'https://api.slack.com/methods/channels.create'
    },
    'channels_history': {
        'resource': 'channels.history',
        'docs': 'https://api.slack.com/methods/channels.history'
    },
    'channels_info': {
        'resource': 'channels.info',
        'docs': 'https://api.slack.com/methods/channels.info'
    },
    'channels_kick': {
        'resource': 'channels.kick',
        'docs': 'https://api.slack.com/methods/channels.kick'
    },
    'channels_leave': {
        'resource': 'channels.leave',
        'docs': 'https://api.slack.com/methods/channels.leave'
    },
    'channels_list': {
        'resource': 'channels.list',
        'docs': 'https://api.slack.com/methods/channels.list'
    },
    'channels_mark': {
        'resource': 'channels.mark',
        'docs': 'https://api.slack.com/methods/channels.mark'
    },
    'channels_rename': {
        'resource': 'channels.rename',
        'docs': 'https://api.slack.com/methods/channels.rename'
    },
    'channels_set_purpose': {
        'resource': 'channels.setPurpose',
        'docs': 'https://api.slack.com/methods/channels.setPurpose'
    },
    'channels_set_topic': {
        'resource': 'channels.setTopic',
        'docs': 'https://api.slack.com/methods/channels.setTopic'
    },
    'channels_unarchive': {
        'resource': 'channels.unarchive',
        'docs': 'https://api.slack.com/methods/channels.unarchive'
    },

    # chat
    'chat_delete': {
        'resource': 'chat.delete',
        'docs': 'https://api.slack.com/methods/chat.delete'
    },
    'chat_post_message': {
        'resource': 'chat.postMessage',
        'docs': 'https://api.slack.com/methods/chat.postMessage'
    },
    'chat_update': {
        'resource': 'chat.update',
        'docs': 'https://api.slack.com/methods/chat.update'
    },

    # emoji
    'emoji_list': {
        'resource': 'emoji.list',
        'docs': 'https://api.slack.com/methods/emoji.list'
    },

    # files
    'files_delete': {
        'resource': 'files.delete',
        'docs': 'https://api.slack.com/methods/files.delete'
    },
    'files_info': {
        'resource': 'files.info',
        'docs': 'https://api.slack.com/methods/files.info'
    },
    'files_list': {
        'resource': 'files.list',
        'docs': 'https://api.slack.com/methods/files.list'
    },
    'files_upload': {
        'resource': 'files.upload',
        'docs': 'https://api.slack.com/methods/files.upload'
    },

    # groups
    'groups_archive': {
        'resource': 'groups.archive',
        'docs': 'https://api.slack.com/methods/groups.archive'
    },
    'groups_close': {
        'resource': 'groups.close',
        'docs': 'https://api.slack.com/methods/groups.close'
    },
    'groups_create': {
        'resource': 'groups.create',
        'docs': 'https://api.slack.com/methods/groups.create'
    },
    'groups_create_child': {
        'resource': 'groups.createChild',
        'docs': 'https://api.slack.com/methods/groups.createChild'
    },
    'groups_history': {
        'resource': 'groups.history',
        'docs': 'https://api.slack.com/methods/groups.history'
    },
    'groups_info': {
        'resource': 'groups.info',
        'docs': 'https://api.slack.com/methods/groups.info'
    },
    'groups_invite': {
        'resource': 'groups.invite',
        'docs': 'https://api.slack.com/methods/groups.invite'
    },
    'groups_kick': {
        'resource': 'groups.kick',
        'docs': 'https://api.slack.com/methods/groups.kick'
    },
    'groups_leave': {
        'resource': 'groups.leave',
        'docs': 'https://api.slack.com/methods/groups.leave'
    },
    'groups_list': {
        'resource': 'groups.list',
        'docs': 'https://api.slack.com/methods/groups.list'
    },
    'groups_mark': {
        'resource': 'groups.mark',
        'docs': 'https://api.slack.com/methods/groups.mark'
    },
    'groups_open': {
        'resource': 'groups.open',
        'docs': 'https://api.slack.com/methods/groups.open'
    },
    'groups_rename': {
        'resource': 'groups.rename',
        'docs': 'https://api.slack.com/methods/groups.rename'
    },
    'groups_set_purpose': {
        'resource': 'groups.setPurpose',
        'docs': 'https://api.slack.com/methods/groups.setPurpose'
    },
    'groups_set_topic': {
        'resource': 'groups.setTopic',
        'docs': 'https://api.slack.com/methods/groups.setTopic'
    },
    'groups_unarchive': {
        'resource': 'groups.unarchive',
        'docs': 'https://api.slack.com/methods/groups.unarchive'
    },

    # im
    'im_close': {
        'resource': 'im.close',
        'docs': 'https://api.slack.com/methods/im.close'
    },
    'im_history': {
        'resource': 'im.history',
        'docs': 'https://api.slack.com/methods/im.history'
    },
    'im_list': {
        'resource': 'im.list',
        'docs': 'https://api.slack.com/methods/im.list'
    },
    'im_mark': {
        'resource': 'im.mark',
        'docs': 'https://api.slack.com/methods/im.mark'
    },
    'im_open': {
        'resource': 'im.open',
        'docs': 'https://api.slack.com/methods/im.open'
    },

    # oauth
    'oauth_access': {
        'resource': 'oauth.access',
        'docs': 'https://api.slack.com/methods/oauth.access'
    },

    # pins
    'pins_add': {
        'resource': 'pins.add',
        'docs': 'https://api.slack.com/methods/pins.add'
    },
    'pins_list': {
        'resource': 'pins.list',
        'docs': 'https://api.slack.com/methods/pins.list'
    },
    'pins_remove': {
        'resource': 'pins.remove',
        'docs': 'https://api.slack.com/methods/pins.remove'
    },

    # reactions
    'reactions_add': {
        'resource': 'reactions.add',
        'docs': 'https://api.slack.com/methods/reactions.add'
    },
    'reactions_get': {
        'resource': 'reactions.get',
        'docs': 'https://api.slack.com/methods/reactions.get'
    },
    'reactions_list': {
        'resource': 'reactions.list',
        'docs': 'https://api.slack.com/methods/reactions.list'
    },
    'reactions_remove': {
        'resource': 'reactions.remove',
        'docs': 'https://api.slack.com/methods/reactions.remove'
    },

    # rtm
    'rtm_start': {
        'resource': 'rtm.start',
        'docs': 'https://api.slack.com/methods/rtm.start'
    },

    # search
    'search_all': {
        'resource': 'search.all',
        'docs': 'https://api.slack.com/methods/search.all'
    },
    'search_files': {
        'resource': 'search.files',
        'docs': 'https://api.slack.com/methods/search.files'
    },
    'search_messages': {
        'resource': 'search.messages',
        'docs': 'https://api.slack.com/methods/search.messages'
    },

    # stars
    'stars_add': {
        'resource': 'stars.add',
        'docs': 'https://api.slack.com/methods/stars.add'
    },
    'stars_list': {
        'resource': 'stars.list',
        'docs': 'https://api.slack.com/methods/stars.list'
    },
    'stars_remove': {
        'resource': 'stars.remove',
        'docs': 'https://api.slack.com/methods/stars.remove'
    },

    # team
    'team_access_logs': {
        'resource': 'team.accessLogs',
        'docs': 'https://api.slack.com/methods/team.accessLogs'
    },
    'team_info': {
        'resource': 'team.info',
        'docs': 'https://api.slack.com/methods/team.info'
    },

    # users
    'users_get_presence': {
        'resource': 'users.getPresence',
        'docs': 'https://api.slack.com/methods/users.getPresence'
    },
    'users_info': {
        'resource': 'users.info',
        'docs': 'https://api.slack.com/methods/users.info'
    },
    'users_list': {
        'resource': 'users.list',
        'docs': 'https://api.slack.com/methods/users.list'
    },
    'users_set_active': {
        'resource': 'users.setActive',
        'docs': 'https://api.slack.com/methods/users.setActive'
    },
    'users_set_presence': {
        'resource': 'users.setPresence',
        'docs': 'https://api.slack.com/methods/users.setPresence'
    },
}
