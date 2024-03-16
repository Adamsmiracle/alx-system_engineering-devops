#include <iostream>
#include <list>
#include <string>

using namespace std;

class YoutubeChannel
{

private:
    string Name;
    string OwnerName;
    int SubscriberCount;
    list<string> PublishedVideoTitles;

public:
    YoutubeChannel(string name, string ownerName)
    {
        Name = name;
        OwnerName = ownerName;
        SubscriberCount = 0;
    }

    void GetInfo()
    {
        cout << "Name: " << Name << endl;
        cout << "Owner Name: " << OwnerName << endl;
        cout << "Number of Subscribers: " << SubscriberCount << endl;
        cout << "Videos: " << endl;

        for (string videoTitle : PublishedVideoTitles)
        {
            cout << videoTitle << endl;
        }
    }

    void subscribe()
    {
        ++SubscriberCount;
    }

    void unsubscribe()
    {
        if (SubscriberCount > 0)
            --SubscriberCount;
    }

    string getname() const
    {
        return Name;
    }

    void publishvideo(string video)
    {
        PublishedVideoTitles.push_back(video);
    }

    void getinfo()
    {
        cout << "Name of channel: " << Name << endl;
        cout << "Name of owner: " << OwnerName << endl;
        cout << "Number of subscribers: " << SubscriberCount << endl;
        cout << "                     videos published              " << endl;
        for (string video : PublishedVideoTitles)
        {
            cout << video << endl;
        }
    }
};

int main()
{
    cout << "Hello world!" << endl;

    YoutubeChannel ytchannel("Tech", "Achala Elijah");
    ytchannel.publishvideo("intro to Tech");
    ytchannel.getinfo();
    for (int i = 1; i <= 20; ++i)
    {
        ytchannel.subscribe();
    }

    ytchannel.getinfo();

    return 0;
}
