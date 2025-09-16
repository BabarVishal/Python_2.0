# Dictionary are used to store DataValue in Key-value pairs;
#They are unordered, Mutable and dont allow duplicate key;

Dictionary = {
    "name":"Vishal",
    "age":22,
    "Gender":"Male",
    "Email":"vishalbabar@gmail.com",
    "Subjects":["math","Bio","Phy"]
};

print(Dictionary);
print(type(Dictionary));
print(Dictionary["name"]);
Dictionary["name"] = "Vishal";
Dictionary["surname"] = "Babar";
print(Dictionary);

Hostel_Boys = {};
print(Hostel_Boys);
Hostel_Boys["Name"] = ["01","Vishal Babar", "age:21", "RoomNum:07"];
print(Hostel_Boys);

#Nested Dic...
Student = {
    "Name":"Vishal Babar",
    "Subject" : {
       "Math": 22,
       "Phy":33,
       "Che":44
    }
};
print(Student);
print(Student["Subject"]);
print(Student["Subject"]["Che"]);

#Dic Method....
print(Student.keys()); #Give all key;
print(len(list(Student.values())));
print(Student.items());
print(Student.get("Name"));
