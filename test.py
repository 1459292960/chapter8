# def describe_pet(pet_name,animal_type="dog"):
#     print("\nI have a "+animal_type+".")
#     print("My "+animal_type+"'s name is "+pet_name.title()+".")
# def formatted_name(first_name,last_name,middle_name):
#     full_name=first_name+" "+middle_name+" "
#     return full_name.title()
# name=formatted_name("bin","peng")
# print(name)
def get_formatted_name(fisrt_name,last_name,middle_name=""):
    if middle_name:
        return (   fisrt_name+" "+middle_name+" "+last_name).title();
    else:
        return (fisrt_name+" "+last_name).title();
name=get_formatted_name("Bin",'peng','xiao')
def build_person(first_name,last_name,age=""):
    person={"first_name":first_name,"last_name":last_name}
    if age:
        person["age"]=age
    return person
abin=build_person("Benny","Peng")
# while True:
#     print("Please tell me your name!")
#     print("enter 'q'to quit")
#     f_name=input("first_name:")
#     if f_name == "q":
#         break
#     l_name=input("last_name:")
#     name=get_formatted_name(f_name,l_name )
#     print("Hello,"+name+" !")
def greet_users(names):
    '''向每位用户都发出简单的问候'''
    for name in names:
        msg="Hello,"+name.title()+"!"
        print(msg)
# user_name=['hannah','ty','margot']
# greet_users(user_name)
def print_models(unprinted_designs,completed_designs):
    while unprinted_models:
        current_design = unprinted_designs.pop()
        print("Printing model:" + current_design)
        completed_designs.append(current_design)


def show_completed_models(completed_designs):
    print("The following designs have been completed:")
    for model in completed_designs:
        print(model)
unprinted_models = ["apple","huawei","mi"]
completed_models = []
print_models(unprinted_models,completed_models)
show_completed_models(completed_models)
