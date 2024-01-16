#!/usr/bin/python3
<<<<<<< HEAD
"""
Console DOC
"""
import cmd
import re
=======
"""Defines the HBnB console"""
import cmd
import re
from shlex import split
from models.engine.file_storage import FileStorage  # Use relative import
>>>>>>> a3272ac7d07d8af2b500c61934582aa4edd7da40
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
<<<<<<< HEAD
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """
    HBNB command
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        do quit
        """
        return True

    def do_EOF(self, args):
        """
        do EOF
        """
        return True

    def emptyline(self):
        """
        empty line
        """
        pass

    def do_create(self, arg):
        """
        do create
        """
        if len(arg) > 0:
            lines = arg.split()
            if len(lines) > 0:
                if lines[0] == "BaseModel":
                    obj = BaseModel()
                    obj.save()
                    print(obj.id)
                elif lines[0] == "User":
                    obj = User()
                    obj.save()
                    print(obj.id)
                elif lines[0] == "State":
                    obj = State()
                    obj.save()
                    print(obj.id)
                elif lines[0] == "City":
                    obj = City()
                    obj.save()
                    print(obj.id)
                elif lines[0] == "Amenity":
                    obj = Amenity()
                    obj.save()
                    print(obj.id)
                elif lines[0] == "Place":
                    obj = Place()
                    obj.save()
                    print(obj.id)
                elif lines[0] == "Review":
                    obj = Review()
                    obj.save()
                    print(obj.id)
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        do show
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if len(arg) > 0:
            lines = arg.split()
            if len(lines) > 0:
                class_name = lines[0]
                if class_name in allowed_classes:
                    if len(lines) > 1:
                        objs_dict = models.storage.all()
                        search_string = "{}.{}".format(
                                class_name, lines[1])
                        if search_string in objs_dict:
                            print(objs_dict[search_string])
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        do destroy
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if len(arg) > 0:
            lines = arg.split()
            if len(lines) > 0:
                class_name = lines[0]
                if class_name in allowed_classes:
                    if len(lines) > 1:
                        objs_dict = models.storage.all()
                        search_string = "{}.{}".format(
                                class_name, lines[1])
                        if search_string in objs_dict:
                            del (objs_dict[search_string])
                            models.storage.save()
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
        do all
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if len(arg) > 0:
            lines = arg.split()
            if len(lines) > 0:
                class_name = lines[0]
                if class_name in allowed_classes:
                    final_list = []
                    for key, value in models.storage.all().items():
                        if (class_name in key):
                            final_list.append(str(value))
                    print(final_list)
                else:
                    print("** class doesn't exist **")
        else:
            final_list = []
            for key, value in models.storage.all().items():
                final_list.append(str(value))
            print(final_list)

    def do_update(self, arg):
        """
        do updates
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if len(arg) > 0:
            lines = arg.split()
            if len(lines) > 0:
                class_name = lines[0]
                if class_name in allowed_classes:
                    if len(lines) > 1:
                        objs_dict = models.storage.all()
                        search_string = "{}.{}".format(
                                class_name, lines[1])
                        if search_string in objs_dict:
                            if len(lines) > 2:
                                if len(lines) > 3:
                                    if (lines[3]
                                            not in
                                            ["created_at",
                                                "updated_at", "id"]):
                                        setattr(objs_dict[search_string], str(
                                            lines[2]), str(lines[3]))
                                else:
                                    print("** value missing **")
                            else:
                                print("** attribute name missing **")
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_User(self, arg):
        """
        do user
        """
        class_name = "User"
        self.data_model_func(arg, class_name)

    def do_BaseModel(self, arg):
        """
        do base models
        """
        class_name = "BaseModel"
        self.data_model_func(arg, class_name)

    def do_State(self, arg):
        """
        do state
        """
        class_name = "State"
        self.data_model_func(arg, class_name)

    def do_City(self, arg):
        """
        do city
        """
        class_name = "City"
        self.data_model_func(arg, class_name)

    def do_Amenity(self, arg):
        """
        do amenity
        """
        class_name = "Amenity"
        self.data_model_func(arg, class_name)

    def do_Place(self, arg):
        """
        do place
        """
        class_name = "Place"
        self.data_model_func(arg, class_name)

    def do_Review(self, arg):
        """
        do review
        """
        class_name = "Review"
        self.data_model_func(arg, class_name)

    def data_model_func(self, arg, class_name):
        """
        data models funct
        """
        allowed_methods = [".all()", ".count()"]
        show_regex = re.compile(r"\.show\(\"(.*?)\"\)")
        delete_regex = re.compile(r"\.destroy\(\"(.*?)\"\)")
        update_regex = re.compile(r"\.update\(\"(.*?)\", \"(.*?)\", (.*?)\)")
        update_dict_regex = re.compile(r"\.update\(\"(.*?)\",(.*?)\)")
        if len(arg) > 0:
            lines = arg.split()
            if len(lines) > 0:
                command_method = lines[0]
                if command_method in allowed_methods:
                    if command_method == ".all()":
                        self.do_all(class_name)
                    if command_method == ".count()":
                        self.get_count(class_name)
                elif (show_regex.search(lines[0]) is not None):
                    obj_id = show_regex.search(lines[0]).group(1)
                    self.do_show("{} {}".format(class_name, obj_id))
                elif (delete_regex.search(lines[0]) is not None):
                    obj_id = delete_regex.search(lines[0]).group(1)
                    self.do_destroy("{} {}".format(class_name, obj_id))
                elif (update_regex.search(arg) is not None):
                    obj_id = update_regex.search(arg).group(1)
                    obj_attr_name = update_regex.search(arg).group(2)
                    obj_attr_value = update_regex.search(arg).group(3)
                    self.do_update("{} {} {} {}".format(
                        class_name, obj_id, obj_attr_name, obj_attr_value))
                elif (update_dict_regex.search(arg) is not None):
                    obj_id = update_dict_regex.search(arg).group(1)
                    obj_dict = eval(update_dict_regex.search(arg).group(2))
                    for key, value in obj_dict.items():
                        self.do_update("{} {} {} {}".format(
                            class_name, obj_id, key, value))

    def get_count(self, class_name):
        """
        get count
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if class_name in allowed_classes:
            final_list = []
            for key, value in models.storage.all().items():
                if (class_name in key):
                    final_list.append(str(value))
            print(len(final_list))
        else:
            print("** class doesn't exist **")
=======
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


# Create an instance of FileStorage
storage = FileStorage()
storage.reload()  # Load data from the JSON file, if available


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter

    Attributes:
        prompt (str): command prompt
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        display the string representation of a class instance of a given id
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id"""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects"""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class"""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary"""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for key, value in eval(argl[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valtype(value)
                else:
                    obj.__dict__[key] = value
        storage.save()
>>>>>>> a3272ac7d07d8af2b500c61934582aa4edd7da40


if __name__ == "__main__":
    HBNBCommand().cmdloop()

