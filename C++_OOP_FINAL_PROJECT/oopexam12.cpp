#include <iostream>
#include <cstring>
#include <stdexcept>
struct Contact {
    char name[30];
    char phone[15];
};
class BaseContact {
public:
    virtual ~BaseContact() {}
    virtual void showInfo() const = 0;
    virtual const char* getName() const = 0;
    virtual const char* getPhone() const = 0;
};
class PersonalContact : public BaseContact {
private:
    Contact* contact;
    char birthday[11];  
public:
    PersonalContact(const char* name, const char* phone, const char* bday) {
        contact = new Contact();
        strncpy(contact->name, name, 29);
        contact->name[29] = '\0';
        strncpy(contact->phone, phone, 14);
        contact->phone[14] = '\0';
        strncpy(birthday, bday, 10);
        birthday[10] = '\0';
    }
    ~PersonalContact() {
        delete contact;
    }
    void showInfo() const {
        std::cout << "Personal Contact: " << contact->name 
                  << ", Phone: " << contact->phone
                  << ", Birthday: " << birthday << std::endl;
    }
    const char* getName() const { return contact->name; }
    const char* getPhone() const { return contact->phone; }
    const char* getBirthday() const { return birthday; }
};
class BusinessContact : public BaseContact {
private:
    Contact* contact;
    char company[20];  
public:
    BusinessContact(const char* name, const char* phone, const char* comp) {
        contact = new Contact();
        strncpy(contact->name, name, 29);
        contact->name[29] = '\0';
        strncpy(contact->phone, phone, 14);
        contact->phone[14] = '\0';
        strncpy(company, comp, 19);
        company[19] = '\0';
    }
    ~BusinessContact() {
        delete contact;
    }
    void showInfo() const {
        std::cout << "Business Contact: " << contact->name 
                  << ", Phone: " << contact->phone
                  << ", Company: " << company << std::endl;
    }
    const char* getName() const { return contact->name; }
    const char* getPhone() const { return contact->phone; }
    const char* getCompany() const { return company; }
};
struct Group {
    char groupName[20];
    BaseContact** members;
    int memberCount;
    int capacity;
    Group(const char* name) : memberCount(0), capacity(5) {
        strncpy(groupName, name, 19);
        groupName[19] = '\0';
        members = new BaseContact*[capacity];
    }
    ~Group() {
        delete[] members;
    } 
    void addMember(BaseContact* contact) {
        if (memberCount == capacity) {
            capacity *= 2;
            BaseContact** newMembers = new BaseContact*[capacity];
            for (int i = 0; i < memberCount; ++i) {
                newMembers[i] = members[i];
            }
            delete[] members;
            members = newMembers;
        }
        members[memberCount++] = contact;
    }
    bool removeMember(const char* name) {
        for (int i = 0; i < memberCount; ++i) {
            if (strcmp(members[i]->getName(), name) == 0) {
                for (int j = i; j < memberCount - 1; ++j) {
                    members[j] = members[j + 1];
                }
                memberCount--;
                return true;
            }
        }
        return false;
    }
    void showMembers() const {
        std::cout << "Group '" << groupName << "' members:" << std::endl;
        for (int i = 0; i < memberCount; ++i) {
            members[i]->showInfo();
        }
    }
};
class ContactManager {
private:
    BaseContact** allContacts;
    int contactCount;
    int contactCapacity;
    Group** groups;
    int groupCount;
    int groupCapacity;
public:
    ContactManager() : contactCount(0), contactCapacity(10), groupCount(0), groupCapacity(5) {
        allContacts = new BaseContact*[contactCapacity];
        groups = new Group*[groupCapacity];
    }
    ~ContactManager() {
        for (int i = 0; i < contactCount; ++i) {
            delete allContacts[i];
        }
        delete[] allContacts;
        for (int i = 0; i < groupCount; ++i) {
            delete groups[i];
        }
        delete[] groups;
    }
    void addContact(BaseContact* contact) {
        if (contactCount == contactCapacity) {
            contactCapacity *= 2;
            BaseContact** newContacts = new BaseContact*[contactCapacity];
            for (int i = 0; i < contactCount; ++i) {
                newContacts[i] = allContacts[i];
            }
            delete[] allContacts;
            allContacts = newContacts;
        }
        allContacts[contactCount++] = contact;
    }
    bool removeContact(const char* name) {
        for (int i = 0; i < contactCount; ++i) {
            if (strcmp(allContacts[i]->getName(), name) == 0) {
                for (int g = 0; g < groupCount; ++g) {
                    groups[g]->removeMember(name);
                }
                delete allContacts[i];
                for (int j = i; j < contactCount - 1; ++j) {
                    allContacts[j] = allContacts[j + 1];
                }
                contactCount--;
                return true;
            }
        }
        return false;
    }
    BaseContact* getContact(const char* name) {
        for (int i = 0; i < contactCount; ++i) {
            if (strcmp(allContacts[i]->getName(), name) == 0) {
                return allContacts[i];
            }
        }
        return NULL;  
    }
    void showAllContacts() const {
        std::cout << "All Contacts:" << std::endl;
        for (int i = 0; i < contactCount; ++i) {
            allContacts[i]->showInfo();
        }
    }
    void addGroup(const char* groupName) {
        if (groupCount == groupCapacity) {
            groupCapacity *= 2;
            Group** newGroups = new Group*[groupCapacity];
            for (int i = 0; i < groupCount; ++i) {
                newGroups[i] = groups[i];
            }
            delete[] groups;
            groups = newGroups;
        }
        groups[groupCount++] = new Group(groupName);
    }
    bool removeGroup(const char* groupName) {
        for (int i = 0; i < groupCount; ++i) {
            if (strcmp(groups[i]->groupName, groupName) == 0) {
                delete groups[i];
                for (int j = i; j < groupCount - 1; ++j) {
                    groups[j] = groups[j + 1];
                }
                groupCount--;
                return true;
            }
        }
        return false;
    }
    Group* getGroup(const char* groupName) {
        for (int i = 0; i < groupCount; ++i) {
            if (strcmp(groups[i]->groupName, groupName) == 0) {
                return groups[i];
            }
        }
        return NULL;  
    }
    void showAllGroups() const {
        std::cout << "All Groups:" << std::endl;
        for (int i = 0; i < groupCount; ++i) {
            groups[i]->showMembers();
        }
    }
};
int main() {
    ContactManager manager;
    manager.addContact(new PersonalContact("Jean", "0789325476", "2000-05-15"));
    manager.addContact(new BusinessContact("David", "0798123456", "New Species"));
    manager.addContact(new PersonalContact("Francois", "0798765432", "2002-11-20"));
    manager.showAllContacts();
    manager.addGroup("Family");
    manager.addGroup("Work");
    Group* family = manager.getGroup("Family");
    if (family) {
        BaseContact* contact = manager.getContact("Jean");
        if (contact) family->addMember(contact);
        contact = manager.getContact("Francois");
        if (contact) family->addMember(contact);
    }
    Group* work = manager.getGroup("Work");
    if (work) {
        BaseContact* contact = manager.getContact("David");
        if (contact) work->addMember(contact);
    }
    manager.showAllGroups();
    manager.removeContact("Jean");
    manager.showAllGroups();
    manager.removeGroup("Work");
    manager.showAllContacts();
    manager.showAllGroups();
    return 0;
}
