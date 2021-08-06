from pypresence import Presence
#import time

currentProject = "exampleProject"
client_id = "872972608302358588"
RPC = Presence(client_id)
RPC.connect()

# Config
RPC.update(state="Ursina Editor", large_image="large", large_text="Alpha 1.0", details="Working on: " + currentProject)

# for updating the Presence State
#while true:
#    time.sleep(15)