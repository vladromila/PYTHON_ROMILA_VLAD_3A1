def camelToSnake():
    str = input("Enter your string: ")
    print(''.join(['_'+c.lower() if c.isupper()
          else c for c in str]).lstrip('_'))
