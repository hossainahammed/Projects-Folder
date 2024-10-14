class Institution:
    pass

class School:
    pass


school_object = School()


if isinstance(school_object, Institution):
    print("The school_object is an instance of the Institution class.")
else:
    print("The school_object is not an instance of the Institution class.")
