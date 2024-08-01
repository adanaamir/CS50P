# import emoji
# import sys

# # text = input("Input: ")
# if len(sys.argv) == 2:
#     emo = emoji.emojize("Output:" + sys.argv[1])
#     print(emo)

import emoji

text = input("Input: ")
emo = emoji.emojize(text, language='alias')
print("Output:", emo)