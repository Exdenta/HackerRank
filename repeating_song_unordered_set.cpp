#include <stdexcept>
#include <iostream>
#include <unordered_set>

class Song
{
public:
    Song(std::string name): name(name), nextSong(NULL) {}
    
    void next(Song* song)
    {
        this->nextSong = song;
    }

    bool isRepeatingPlaylist()
    {
        std::unordered_set<Song*> seen_songs;
        Song* song = this;
        while(true)
        {
            if(!song) return false;
            if (seen_songs.find(song) != seen_songs.end()) // O(1)
            {
                return true;
            }
            
            seen_songs.insert(song); // O(1)
            song = song->nextSong;
        }
    }

private:
    const std::string name;
    Song* nextSong;
};

#ifndef RunTests
int main()
{
    Song* first = new Song("Hello");
    Song* second = new Song("Eye of the tiger");
    
    first->next(second);
    second->next(first);

    std::cout << std::boolalpha << first->isRepeatingPlaylist();
}
#endif