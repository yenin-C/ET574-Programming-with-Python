## Demonstrate a function with arbitrary keyword argument

def main():
    user_profile = build_profile('albert', 'einstein',
                                 location='princeton',
                                 field='physics')
    print(user_profile)
    print()
    stu_profile = build_profile('john', 'smith',
                                 location='cuny',
                                 field='csis')
    print(stu_profile)
    print()

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

main()
