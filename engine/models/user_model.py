from pydantic import BaseModel

class UserData(BaseModel):
    username:str
    alias:str = ""
    location:str = ""

    def Create_User():
        print("----- WELCOME TO NOVA-02 -----")
        while(True):
            username = input("Introduce your username: ")
            if username == "":
                print("Is necessary to introduce a username: ")
            else: break

        alias = input("Introduce your alias (optional): ")
        location = input("Introduce your location (optional): ")

        new_user = UserData(
            username = username,
            alias = alias,
            location = location
        )

        return new_user



    