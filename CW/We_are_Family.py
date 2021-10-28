
class Person:
    def __init__(self, name=None):
        self.name = name
        self.gender = None
        self.parent = []
        self.child = []

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Family:
    def __init__(self):
        self.members = []
        self.previous = []

    def get_member(self, name):
        for i in self.members:
            if i.name == name:
                return i
        return None

    def set_member(self, name):
        member = Person(name)
        self.members.append(member)
        return member

    def male(self, name):
        member = self.get_member(name)
        if member:
            if member.gender:
                if member.gender == "M":
                    if member.child != []:
                        for i in member.child[0].parent:
                            if i.name != name:
                                i.gender = "F"
                    return True
                else:
                    return False
            else:
                member.gender = "M"
                if member.child != []:
                    for i in member.child[0].parent:
                        if i.name != name:
                            i.gender = "F"
                return True
        else:
            member = self.set_member(name)
            member.gender = "M"
            return True

    def is_male(self, name):
        member = self.get_member(name)
        if member:
            if member.gender == "M":
                return True
            else:
                return False
        else:
            return False

    def female(self, name):
        member = self.get_member(name)
        if member:
            if member.gender:
                if member.gender == "F":
                    if member.child != []:
                        for i in member.child[0].parent:
                            if i.name != name:
                                i.gender = "M"
                    return True
                else:
                    return False
            else:
                member.gender = "F"
                return True
        else:
            member = self.set_member(name)
            member.gender = "F"
            if member.child != []:
                for i in member.child[0].parent:
                    if i.name != name:
                        i.gender = "M"
            return True

    def is_female(self, name):
        member = self.get_member(name)
        if member:
            if member.gender == "F":
                return True
            else:
                return False
        else:
            return False

    def is_parent_of(self, child_name, parent_name):
        child_name = self.get_member(child_name)
        for parent in child_name.parent:
            if parent.name == parent_name:
                return True
        return False

    def is_child_of(self, child_name, parent_name):
        parent_name = self.get_member(parent_name)
        for child in parent_name.child:
            if child.name == child_name:
                return True
        return False

    def set_parent_of(self, child_name, parent_name):

        child_member = self.get_member(child_name)
        parent_member = self.get_member(parent_name)

        if not child_member:
            child_member = self.set_member(child_name)
        if not parent_member:
            parent_member = self.set_member(parent_name)

        if child_name == parent_name:
            return False

        try:
            if self.previous[0] == child_name and self.previous[1] == parent_name:
                return True
        except:
            pass

        if self.is_parent_of(child_name, parent_name):
            return False

        if self.is_child_of(child_name, parent_name):
            return False
        
        if self.is_parent_of(parent_name, child_name):
            return False

        if self.is_child_of(parent_name, child_name):
            return False

        parent_member.child.append(child_member)
        child_member.parent.append(parent_member)
        self.previous = [child_name, parent_name]
        return True

    def get_children_of(self, name):
        member = self.get_member(name)
        if member:
            if member.child != []:
                return sorted([i.name for i in member.child])
            else:
                return []
        else:
            return []

    def get_parents_of(self, name):
        member = self.get_member(name)
        if member:
            if member.parent != []:
                return sorted([i.name for i in member.parent])
            else:
                return []
        else:
            return []


fam = Family()
fam.set_parent_of("Frank", "Morgan")
fam.set_parent_of("Morgan", "Frank")
