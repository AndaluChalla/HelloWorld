links = [
    'https://onecognizantexternal.com',
    'https://youtube.com/shorts/ACuXn0EQfS0',
    'https://chatgpt.com'
]
for link in links:
    # print(link)
    # print(link.lstrip("https://"))
    # print(link.removeprefix("https://"))
    altered_str = link.removeprefix("https://")
    print(altered_str)