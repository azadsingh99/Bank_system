#include<iostream>
using namespace std;

class Account
{
    private:
        long AccountNumber;
        string firstname;
        string lastname;
        float balance;
        static long accountnum;
    
    public:
        Account(string fname, string lname, float bal);
        void setAccountNumber();
        void setFirstName(string fname);
        void setLastName(string lname);
        void setBalance(float bal);
        void display();
};

long Account :: accountnum=0;

Account :: Account(string fname, string lname, float bal)
{
    setAccountNumber();
    setFirstName(fname);
    setLastName(lname);
    setBalance(bal);
}

void Account :: setAccountNumber()
{
        accountnum++;
        AccountNumber = accountnum;
}

void Account :: setFirstName(string fname)
{
    firstname = fname;
}

void Account :: setLastName(string lname)
{
    lastname = lname;
}

void Account :: setBalance(float bal)
{
    balance = bal;
}

void Account :: display()
{
    cout << "First Name      : " << firstname << endl;
    cout << "Last  Name      : " << lastname << endl;
    cout << "Account Number  : " << AccountNumber << endl;
    cout << "Balance         : " << balance << endl;
    cout << "-------------------------------------------" << endl;
}
int main()
{
    int n;
    string fname, lname;
    float bal;

    cout << "Enter the total account to create: ";
    cin >> n;

    Account *acc[n];
    for(int i=0; i<n; i++)
    {
        cout << "Enter the " << i+1 << " Account To Create " << endl;
        cout << "Enter First Name : ";
        cin >> fname;
        cout << "Enter Last Name : ";
        cin >> lname;
        cout << "Enter Initial Balance : ";
        cin >> bal;

        acc[i] = new Account(fname, lname, bal);
    }

    for(int i=0; i<n; i++)
    {
        acc[i]->display();
    }

    return 0;
}