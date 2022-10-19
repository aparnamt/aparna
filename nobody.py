#!usr/bin/env python3
import re
string='''Nobody by Shel Silverstein,
Nobody loves me,
Nobody cares,
Nobody picks me peaches and pears.
Nobody offers me candy and Cokes,
Nobody listens and laughs at me jokes.
Nobody helps when I get in a fight,
Nobody does all my homework at night.
Nobody misses me,
Nobody cries,
Nobody thinks Im a wonderful guy.
So if you ask me whos my best friend, in a whiz,
Ill stand up and tell you that Nobody is.
But yesterday night I got quite a scare,
I woke up and Nobody just wasnt there.
I called out and reached out for Nobodys hand,
In the darkness where Nobody usually stands.
Then I poked through the house, in each cranny and nook,
But I found somebody each place that I looked.
I searched till Im tired, and now with the dawn,
Theres no doubt about it-
Nobodys gone!'''
find=re.findall(r"(Nobody)",string)
print(find)

new_str=re.sub(r"(Nobody)","Rheo",string)
print(new_str)

