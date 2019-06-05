from time import sleep

"""
Active Directory

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct
this hierarchy as such. Where User is represented by str representing their ids.
"""


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def __repr__(self):
        return self.name

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    if not group.get_groups():
        return False
    print('subgroups: ', group.get_groups())
    sleep(0.1)
    for sub_gr in group.get_groups():
        print('starting recursion for user "{}" in subgroup "{}"...'.format(user, sub_gr))
        return is_user_in_group(user, sub_gr)



parent = Group("parent")
child = Group("child")
child2 = Group("child2")
parent.add_group(child)
parent.add_group(child2)

sub_child = Group("sub_child")
child.add_group(sub_child)

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

sub_child_user1 = "sub_child_user1"

# Test case 1
print('\nTest Case 1__________________________________')
print(is_user_in_group(sub_child_user, sub_child))

# Test case 2
print('\nTest Case 2__________________________________')
print(is_user_in_group(sub_child_user, child))

# Test case 3
print('\nTest Case 3__________________________________')
print(is_user_in_group(sub_child_user, parent))

# Test case 4
print('\nTest Case 3__________________________________')
print(is_user_in_group(sub_child_user1, parent))

