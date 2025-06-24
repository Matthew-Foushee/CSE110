dialogPrompts = [
    {"prompt" : "You wake up in a cold dark room. After feeling around you find a LIGHT SWITCH and a DOOR HANDLE.", "res1" : {"phrase" : "LIGHT SWITCH", "index": 2}, "res2": {"phrase": "DOOR HANDLE", "index": 1}},
    {"prompt" : "After Opening the door you slip out into another room, you notice a ruined environment with rubble everywhere and some huge windows with a dense jungle through them with moonlight streaming in. You can THROW a rock at the windows or RETURN back into the only other room being the one you came from and turn on the lights", "res1" : { "phrase" : "THROW", "index": 3}, "res2": {"phrase" :"RETURN", "index": 2}},
    {"prompt" : "Upon turning on the lights they suddenly flick on showing you a very bland and white room. After a few seconds the lights get brighter and brighter. You once again find yourself in a new place. You are on top of clouds and a golden gate in the distance. You can JUMP down from the clouds or WALK towards the gate", "res1" : { "phrase" : "JUMP", "index": 4}, "res2": {"phrase": "WALK", "index": 5}},
    {"prompt" : "When you throw the rock it bounces off the windows and nothing happens... How sad... You can THROW another rock or INSPECT the room more", "res1" : { "phrase" : "THROW", "index": 3}, "res2": {"phrase": "INSPECT", "index": 6}},
    {"prompt" : "You fall further down and down and find yourself in a firey pit with demons all around. You are now in Hell, Have fun.", "res1" : { "phrase" : "", "index": -1}, "res2": {"phrase": "", "index": -1}},
    {"prompt" : "While approaching the gate they swing open for you and somw angelic trumpet sounds play welcoming you to heaven. Good job. You did it.", "res1" : { "phrase" : "", "index": -1}, "res2": {"phrase": "", "index": -1}},
    {"prompt" : "While inspecting the room you step on a particular brick and the entire floor suddenly is gone and you start falling. You can either PRAY or SCREAM", "res1" : { "phrase" : "PRAY", "index": 5}, "res2": {"phrase": "SCREAM", "index": 6}}
    ]

currentOption = 0

while True:
    #This is the extracted data from the dictionary.
    current_prompt = dialogPrompts[currentOption]["prompt"]
    response1_keyword = dialogPrompts[currentOption]["res1"]["phrase"]
    response2_keyword = dialogPrompts[currentOption]["res2"]["phrase"]
    response1_next_option = dialogPrompts[currentOption]["res1"]["index"]
    response2_next_option = dialogPrompts[currentOption]["res2"]["index"]

    #The actual loop logic

    #Print current prompt
    print(current_prompt)

    #If there is no keyword and therefor no next stage then exit
    if(response1_keyword == ""):
        break

    #Get next keyword
    response = input("What is your choice? ").upper()

    #Determine next prompt to go to
    if(response == response1_keyword):
        currentOption = response1_next_option
    if(response == response2_keyword):
        currentOption = response2_next_option