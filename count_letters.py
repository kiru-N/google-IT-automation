def groups_per_user(group_dictionary):
    user_groups = {}
    groups = []
    for group, users in group_dictionary.items():
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)

    return (user_groups)


print(groups_per_user({"local": ["admin", "userA"],
                       "public": ["admin", "userB"],
                       "administrator": ["admin"]}))
