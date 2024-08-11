name = input('first enter name here which you want to talk about: ')
post = input('enter post here: ')
if(name.lower() in post.lower()):
    print(f"he is talking about {name}")

else:
    print("he is talking about",name)
