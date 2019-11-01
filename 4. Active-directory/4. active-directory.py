class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

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
    if not user or not group or type(group) is not Group:
        print("Invalid arguments")
        return None

    if user in group.users:
        return True

    found = False
    for g in group.groups:
        found = is_user_in_group(user, g)
        if found:
            break
    return found


if __name__ == '__main__':
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    sub_child_user2 = "sub_child_user_2"
    sub_child_2 = Group("subchild2")
    sub_child_2.add_user(sub_child_user2)
    parent.add_group(sub_child_2)

    print(is_user_in_group(sub_child_user, parent))  # True
    print(is_user_in_group(sub_child_user2, parent))  # True

    print(is_user_in_group(None, parent))  # User arg cannot be None
    print(is_user_in_group(sub_child_user2, None))  # Group arg cannot be None
    print(is_user_in_group(sub_child_user2, "None"))  # Group arg must be Group type
    print(is_user_in_group("", parent))  # Invalid user
