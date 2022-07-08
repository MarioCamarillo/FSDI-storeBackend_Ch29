

from audioop import add


def run_test():
    print("Test 1 - Dictionaries")

    me = {
        "first": "Mario",
        "last": "Camarillo",
        "age": 41,
        "hobbies": [],
        "address": {
            "street": "mia",
            "number": 123,
            "city": "Mesa",
            "state": "Camarillo",
            "zip": 91234
        }
    }

    print(me)
    print(me["fist"])

    print(me["fist"] + " " + me["last"])

    me["age"] = me["age"] + 1

    print(me["age"])

    ################################
    # add new keys
    ################################
    me["preferred_color"] = "black"
    print(me["preferred_color"])

    ################################
    # read if the key exists
    ################################
    if "middle_name" in me:
        print(me["middle_name"])

    ################################################################
    # print the full address in a single line
    ################################################################
    address = me["address"]
    print("------------------address----------------")
    print(address)
    print(type(address))

    print(
        f'{address["street"]} #{address["number"]}, {address["city"]}, {address["state"]}, {address["zip"]}')


run_test()
