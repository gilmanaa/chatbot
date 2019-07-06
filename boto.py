"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json

def response_classification(user_message):
    user_sentence = user_message.split(" ")
    swear_words = ["fuck","shit","bitch","ass","fucker","dick"]
    positive_words = ["great","amazing","wonderful","fantastic","good","well"]
    negative_words = ["no","nope","can't","won't","don't","stop"]
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if any(x in swear_words for x in user_sentence):
        return swearing_response(user_sentence,swear_words)
    elif any(x in positive_words for x in user_sentence):
        return ["laughing", "I love the positive energy"]
    elif user_message.endswith("?"):
        return answer_question(user_message)
    elif user_message[0] in capital_letters:
        return ["inlove","Nice to meet you {0}".format(user_message)]
    elif "what's" in user_message and "up" in user_message:
        return ["money","straight chillin, what's up with you"]
    elif "bro" in user_message:
        return ["crying","technically it's impossible for us to be brothers"]
    elif "okay" in user_message:
        return ["okay", "Dude I'm a robot okay is my middle name"]
    elif any(x in negative_words for x in user_sentence):
        return ["no","Stop being so negative, just do it! Don't let your dreams be dreams!"]
    else:
        return["bored","let me get back to you later"]

def answer_question(user_message):
    if "how" in user_message and "you" in user_message:
        return ["excited", "I'm great! What about you?"]
    elif "weather" in user_message:
        return ["dancing","I'm not sure but I hope it's sunny!"]
    elif "sports" in user_message:
        return ["takeoff","We should go play some basketball"]
    elif "news" in user_message:
        return ["dog","I'm too busy with my dog to know"]
    else:
        return ["confused", "Hmm not sure"]

def swearing_response(user_sentence,swear_words):
    swears = [swear in swear_words for swear in user_sentence]
    swear_counter = 0
    for words in swears:
        if words == True:
            swear_counter += 1
    if swear_counter == 1:
        return ["giggling","Hey that's not very nice"]
    elif swear_counter == 2:
        return ["heartbroke","Why are you speaking to me like this"]
    else:
        return ["afraid","Please stop I can't take it anymore"]

@route('/', method='GET')
def index():
    return template("chatbot.html",template_lookup=['C:/Dev/website_building/chatbot'])


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    boto_response = response_classification(user_message)
    return json.dumps({"animation": boto_response[0], "msg": boto_response[1]})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
