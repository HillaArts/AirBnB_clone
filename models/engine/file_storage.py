#!/usr/bin/python3
"""Defines the file storage class"""
import json
from models.base_model import BaseModel

class FileStorage:
    """Represents a File storage engine
    Attributes:
        __file_path (str): name of the file to save objects to
        __objects (dict): dictionary of instantiated objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """serializes __objects to the json __file_path"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path) as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the json file __file_path to __objects, if it exists"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for i in objdict.values():
                    cls_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls_name)**i)
        except FileNotFoundError:
            return