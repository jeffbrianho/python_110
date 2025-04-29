# Write a function that, given a URL as a string, parses out just the domain
# name and returns it.

def domain_name(string_url):
    domain_name = ''
    words_list = string_url.split('//')
    no_period_word_list = words_list[1].split('.')
    for word in no_period_word_list:
        if word != 'www' and not word.startswith('com'):
            domain_name += word
    print(domain_name)
# Examples:
domain_name("http://github.com/carbonfive/raygun") # should return "github"
domain_name("https://www.cnet.com") # should return "cnet"